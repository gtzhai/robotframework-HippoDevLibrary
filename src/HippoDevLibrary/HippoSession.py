from robot.api import logger
from HippoDevLibrary.robotlibcore import keyword
import robot
import visa
from HippoDevLibrary.HippoDevTable import HippoDevTable

def do_if_special_realization_exists(fn):
    def decorator(*args):
        fnclass = args[0]
        addr = args[1]
        session = fnclass.session
        #logger.warn('decorator in' + addr + ' ' + fn.__name__)
        #for i in range(len(args)):
        #    logger.warn(args[i])
        dev = session.has_special_realization(addr, fn.__name__)
        if dev == None:
            fn(*args)
        else:
            fns = getattr(dev, fn.__name__)
            if len(args) > 1:
                arg1 = (dev,)
                arg2 = args[1:len(args) - 1]
                argss = arg1 + arg2
                #logger.warn(len(argss))
                #for i in range(len(argss)):
                #    logger.warn(argss[i])
                fns(*argss)
            else:
                fns()
    return decorator

class HippoVisaSession(object):
    _rm = visa.ResourceManager()
    def __init__(self):
        pass

    @staticmethod
    def session_connect(addr):
        visa_dev = HippoVisaSession._rm.open_resource(addr)
        visa_dev.chunk_size = 10240
        visa_dev.timeout = 2000
        return visa_dev

    @staticmethod
    def session_disconnect(visa_dev):
        visa_dev.close()

class HippoSession(object):
    _cache = robot.utils.ConnectionCache('No sessions created')
    _name_cache = robot.utils.ConnectionCache('No sessions created')
    devs = HippoDevTable()

    def __init__(self):
        pass

    def has_special_realization(self, addr, member):
        #logger.warn('in' + addr + ' and member:' + member)
        name = self.session_name_get(addr)
        #logger.warn(name + ' and member:' + member)
        self.devs.is_dev_have_member(name, member)
        return self.devs.get_dev(name)

    def session_exists(self, addr):
        try:
            self._cache[addr]
            return True
        except RuntimeError:
            return False

    def session_get(self, addr):
        return self._cache.get_connection(addr)

    def session_name_get(self, addr):
        return self._name_cache.get_connection(addr)

    @keyword
    def register_specical_dev(self, dev):
        self.devs.register_dev(dev)

    @keyword
    def unregister_specical_dev(self, dev):
        self.devs.unregister_dev(dev.name())

    @keyword
    def session_connect(self, addr, name=''):
        if(not self.session_exists(addr)):
            visa_dev = HippoVisaSession.session_connect(addr)
            self._cache.register(visa_dev, addr)
            if len(name) != 0:
                if name != 'default':
                    self._name_cache.register(name, addr)

    @keyword
    def session_disconnect(self, addr):
        visa_dev = self.session_get(addr)
        HippoVisaSession.session_disconnect(visa_dev)

    @keyword
    def session_reset_all(self):
        self._cache.empty_cache()
        self._name_cache.empty_cache()

    def query(self, addr, content, delay=0):
        visa_dev = self.session_get(addr)
        if(delay != 0):
            return visa_dev.query(content, delay)
        else:
            return visa_dev.query(content)

    def write(self, addr, content):
        visa_dev = self.session_get(addr)
        visa_dev.write(content)
        pass

