from HippoDevLibrary.robotlibcore import keyword
from HippoDevLibrary.HippoSession import HippoSession
from HippoDevLibrary.HippoSession import do_if_special_realization_exists
from robot.api import logger
import time

class HippoScope(object):

    def __init__(self, session):
        self.session = session
        pass

    @keyword
    @do_if_special_realization_exists
    def autoset(self, addr):
        """exec autoset procedure

        """
        self.session.write(addr, "AUToscale")
        time.sleep(6)

    @keyword
    @do_if_special_realization_exists
    def measure_vpp(self, addr, chn):
        """get special chn's measured vpp value

        """
        self.session.write(addr, "MEASure:ITEM "+chn+", VPP")
        logger.warn('test logger' + "MEASure:ITEM "+chn+", VPP")
        for i in range(100):
            ret = self.session.query(addr, "MEASure:ITEM? "+chn+", VPP", delay=1)
            val = float(ret)
            if val != 99e36:
                return val
            else:
                time.sleep(0.1)
        return float("inf")
        pass

    @keyword
    @do_if_special_realization_exists
    def measure_offset(self, addr, chn):
        """get special chn's measured offset value

        """
        self.session.write(addr, "MEASure:ITEM " + chn + ", VMID")
        for i in range(100):
            ret = self.session.query(addr, "MEASure:ITEM? "+chn+", VMID", delay=1)
            val = float(ret)
            if val != 99e36:
                return val
            else:
                time.sleep(0.1)
        return float("inf")
        pass

    @keyword
    @do_if_special_realization_exists
    def measure_freq(self, chn, addr):
        """get special chn's measured frequncy value

        """
        self.session.write(addr, "MEASure:ITEM " + chn + ", FREQuency")
        for i in range(100):
            ret = self.session.query(addr,"MEASure:ITEM? "+chn+", FREQuency", delay=1)
            val = float(ret)
            if val != 99e36:
                return val
            else:
                time.sleep(0.1)
        return float("inf")
        pass

    @keyword
    @do_if_special_realization_exists
    def measure_on(self, addr):
        self.session.write(addr, "MEASure:ENABle ON")
        pass

    @keyword
    @do_if_special_realization_exists
    def measure_off(self,addr):
        self.session.write(addr, "MEASure:ENABle OFF")
        pass


