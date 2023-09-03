import sys
sys.path.append("..")

import unittest
from datetime import datetime
import inspect

# our package imports.
from smartinspectpython.smartinspect import SmartInspect
from smartinspectpython.silevel import SILevel
from smartinspectpython.sisession import SISession
from smartinspectpython.sicolor import SIColors

# import classes used for test scenarios.
from testClassDefinitions import SIEventHandlerClass

CONNECTION_TCP:str = "tcp(host=localhost,port=4228,timeout=30000,reconnect=true,reconnect.interval=10s,async.enabled=false)"
CONNECTION_FILE_HOURLY24:str = "file(filename=\"./tests/logfilesVSTest\\FileProtocol-RotateHourly24.sil\", rotate=hourly, maxparts=24, append=true)"

class Test_SISession(unittest.TestCase):
    """
    Test all SISession scenarios.
    """
    
    @staticmethod
    def _CreateSISession(connectionstring:str) -> SISession:
        """
        Creates the base SI object and wires up events.
        """
        try:

            # get calling method name.
            moduleName:str = __name__ + ".py"

            # create new smartinspect instance.
            si = SmartInspect(moduleName)
            si.Connections = connectionstring
            si.Enabled = True
            si.Level = SILevel.Debug
            si.DefaultLevel = SILevel.Debug

            # wire up event handlers.
            SIEventHandlerClass.WireEvents(si)

            # add a new session.
            logsi:SISession = si.AddSession("Main", True)
            logsi.Level = SILevel.Debug

            # return session instance to caller.
            return logsi

        except Exception as ex:

            print(str(ex))
            raise


    def test_LogSeparator(self):
        """
        Test SISession.LogSeparator scenarios.
        """
        try:

            # create a new smartinspect session for logging.
            logsi:SISession = Test_SISession._CreateSISession(CONNECTION_FILE_HOURLY24)

            # perform tests.
            logsi.LogSeparator()
            logsi.LogSeparator(SILevel.Debug)
            logsi.LogSeparator(SILevel.Verbose)
            logsi.LogSeparator(SILevel.Message)
            logsi.LogSeparator(SILevel.Warning)
            logsi.LogSeparator(SILevel.Error)

        except Exception as ex:

            print(str(ex))
            raise


    def test_AllColors(self):
        """
        Test colored message scenarios.
        """
        # create a new smartinspect session for logging.
        #logsi:SISession = Test_SISession._CreateSISession(CONNECTION_TCP)

        try:

            logsi.EnterMethod(SILevel.Debug)
       
            # log message in all known color values.
            for s in SIColors:
                logsi.LogMessage("This is a message in color '{0}'.".format(s.name), s.value)

        except Exception as ex:

            print(str(ex))
            raise

        finally:

            logsi.LeaveMethod(SILevel.Debug)



    def test_Watch(self):
        """
        Test SISession.Watch scenarios.
        """
        try:

            # create a new smartinspect session for logging.
            logsi: SISession = Test_SISession._CreateSISession(CONNECTION_TCP)
       
            # perform tests.
            logsi.Watch(None,"string_cs", "string1 value")
            logsi.Watch(None,"int_cs", int(0))
            logsi.Watch(None,"float_cs", float(3.14159))
            logsi.Watch(None,"datetime_cs", datetime(2023,5,11,12,30,10))
            logsi.Watch(None,"bool_cs", True)
            logsi.Watch(None,"byte_cs", 0xff)

        except Exception as ex:

            print(str(ex))
            raise


    def test_ClearWatches(self):
        """
        Test SISession.ClearWatches scenarios.
        """
        try:

            # create a new smartinspect session for logging.
            logsi:SISession = Test_SISession._CreateSISession(CONNECTION_TCP)

            # perform tests.
            logsi.ClearWatches()

        except Exception as ex:

            print(str(ex))
            raise


    def test_ClearProcessFlow(self):
        """
        Test SISession.ClearProcessFlow scenarios.
        """
        try:

            # create a new smartinspect session for logging.
            logsi:SISession = Test_SISession._CreateSISession(CONNECTION_TCP)

            # perform tests.
            logsi.ClearProcessFlow()

        except Exception as ex:

            print(str(ex))
            raise


    def test_ClearLog(self):
        """
        Test SISession.ClearWatches scenarios.
        """
        try:

            # create a new smartinspect session for logging.
            logsi:SISession = Test_SISession._CreateSISession(CONNECTION_TCP)

            # perform tests.
            logsi.ClearLog()

        except Exception as ex:

            print(str(ex))
            raise


    def test_ClearAll(self):
        """
        Test SISession.ClearAll scenarios.
        """
        try:

            # create a new smartinspect session for logging.
            logsi:SISession = Test_SISession._CreateSISession(CONNECTION_TCP)

            # perform tests.
            logsi.ClearAll()

        except Exception as ex:

            print(str(ex))
            raise


    def test_ClearAutoViews(self):
        """
        Test SISession.ClearAutoViews scenarios.
        """
        try:

            # create a new smartinspect session for logging.
            logsi:SISession = Test_SISession._CreateSISession(CONNECTION_TCP)

            # perform tests.
            logsi.ClearAutoViews()

        except Exception as ex:

            print(str(ex))
            raise


    def test_Instance_GetMembers(self):
        """
        Test instance.getmembers scenarios.
        """
        try:

            # create a new smartinspect session for logging.
            logsi:SISession = Test_SISession._CreateSISession(CONNECTION_TCP)

            inspect.getmembers(logsi)

            # perform tests.
            logsi.ClearAutoViews()

        except Exception as ex:

            print(str(ex))
            raise


# create a new smartinspect session for logging.
logsi:SISession = Test_SISession._CreateSISession(CONNECTION_TCP)

if __name__ == '__main__':
    #logsi:SISession = Test_SISession._CreateSISession(CONNECTION_TCP)
    unittest.main()
