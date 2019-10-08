import  inspect
from robot.api import logger

class HippoDevTable:
    table = dict()

    def register_dev(self, dev):
        name = dev.name()
        logger.warn(name+' ready to register')
        if not self.has_dev(name):
            self.table[name] = dev
            logger.warn(name + ' registed')
            pass
        pass

    def unregister_dev(self, name):
        logger.warn(name+' ready to unregister')
        if self.has_dev(name):
            self.table.pop(name)
            logger.warn(name + ' unregisted')

    def get_dev(self, name):
        return self.table.get(name, None)

    def has_dev(self, name):
        if self.table.get(name, None) != None:
            return True
        else:
            return False

    def is_dev_have_member(self, name, member):
        dev = self.table.get(name, None)
        if dev != None:
            for name, func in self._get_members(dev):
                if name == member:
                    return True
        return False

    def _get_members(self, component):
        if inspect.ismodule(component):
            return inspect.getmembers(component)
        if inspect.isclass(component):
            raise TypeError('Libraries must be modules or instances, got '
                            'class {!r} instead.'.format(component.__name__))
        if type(component) != component.__class__:
            raise TypeError('Libraries must be modules or new-style class '
                            'instances, got old-style class {!r} instead.'
                            .format(component.__class__.__name__))
        return self._get_members_from_instance(component)

    def _get_members_from_instance(self, instance):
        # Avoid calling properties by getting members from class, not instance.
        cls = type(instance)
        for name in dir(instance):
            owner = cls if hasattr(cls, name) else instance
            yield name, getattr(owner, name)
