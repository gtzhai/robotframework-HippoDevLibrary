from HippoDevLibrary.robotlibcore import keyword
from robot.api import logger
import time


class HippoDDS(object):

    def __init__(self, session):
        self.session = session
        pass

    @keyword
    def dds_set_wavetype(self, wave):
        pass
