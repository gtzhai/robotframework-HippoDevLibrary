from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from HippoDevLibrary.HippoDev import HippoDev
from HippoDevLibrary.HippoSession import HippoSession
from HippoDevLibrary.robotlibcore import DynamicCore

__version__ = '0.0.1.dev1'


class HippoDevLibrary(DynamicCore):
    """HippoDevLibrary dev lib is for test and control instruments for Robot Framework

    This document explains how to use keywords provided by HippoDevLibrary.
    For more information about Robot Framework, see http://robotframework.org.

    == Table of contents ==
    - `Keywords`
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        session = HippoSession()
        libraries = [
            session,
            HippoDev(session),
        ]

        DynamicCore.__init__(self, libraries)

