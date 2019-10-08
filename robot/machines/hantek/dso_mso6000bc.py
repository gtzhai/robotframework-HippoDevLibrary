from HippoDevLibrary.HippoDevTable import HippoDevTable
from robot.api.deco import keyword
from robot.api import logger

ROBOT_LIBRARY_SCOPE = "GLOBAL"
class DSOMso6KBC:
    def __init__(self):
        pass

    def name(self):
        return "hantek_dso_mso6000bc"


    def get_idn(self, addr):
        logger.warn('test mso 6000bc')
        return "test"


dev = DSOMso6KBC()

def get_hantek_dso_mso6000bc():
    return dev

def get_hantek_dso_mso6000bc_name():
    return dev.name()
