import sys
from robot.api import logger
from HippoDevLibrary.robotlibcore import keyword
from HippoDevLibrary.HippoScope import HippoScope
from HippoDevLibrary.HippoDDS import HippoDDS
from HippoDevLibrary.HippoSession import do_if_special_realization_exists
import HippoDevLibrary.eel as eel

class HippoDev(HippoScope, HippoDDS):
    hippo_dev = None
    def __init__(self, session):
        self.session = session
        HippoScope.__init__(self, session)
        HippoDDS.__init__(self, session)
        hippo_dev = self
        pass

    @keyword
    @do_if_special_realization_exists
    @eel.expose
    def get_idn(self, addr):
        #dev = self.session.has_special_realization(addr, sys._getframe().f_code.co_name)
        #if dev != None:
        #    return dev.get_idn(addr)
        idn = self.session.query(addr, '*IDN?')
        logger.warn('test logger' + idn)
        return idn

    @keyword
    @do_if_special_realization_exists
    def reset(self, addr):
        self.session.write(addr, '*RST')

    @keyword
    @do_if_special_realization_exists
    def beeper_status(self,addr):
        ret = self.session.query(addr, 'SYSTem:BEEPer?')
        if ret == 'ON':
            return True
        else:
            return False

    @keyword
    @do_if_special_realization_exists
    def get_language(self, addr):
        ret = self.session.query(addr, 'SYSTem:LANGuage?')
        if ret == 'ENGLish':
            return 'English'
        elif ret == 'SCHinese':
            return 'Chinese'
        else:
            return ret

    @keyword
    @do_if_special_realization_exists
    def set_language(self, addr, lan):
        if lan == 'English':
            self.session.write(addr, 'SYSTem:LANGuage ENGLish')
        elif lan == 'Chinese':
            self.session.write(addr, 'SYSTem:LANGuage SCHinese')
        else:
            logger.warn('no such language' + lan)

