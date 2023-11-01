import sys
sys.path.append("..")

import unittest

# our package imports.
from smartinspectpython.smartinspect import SmartInspect
from smartinspectpython.sisession import SISession
from smartinspectpython.silevel import SILevel

# import classes used for test scenarios.
from testClassDefinitions import SIEventHandlerClass
from testSessionMethods import TestSessionMethods

class Test_Protocols(unittest.TestCase):
    """
    Test all SISession scenarios.
    """
    
    @staticmethod
    def CreateSISession(connectionstring:str) -> SISession:
        """
        Creates the base SI object and wires up events.
        """
        try:

            # get calling method name.
            moduleName:str = __name__ + ".py"

            # create new smartinspect instance.
            si = SmartInspect(moduleName)

            # wire up event handlers.
            # we do this BEFORE setting the Connections property, just in
            # case the Connections property value contains invalid options.
            SIEventHandlerClass.WireEvents(si)

            # set connections string, and default levels, and enable logging.
            si.Connections = connectionstring
            si.Level = SILevel.Debug
            si.DefaultLevel = SILevel.Debug
            si.Enabled = True

            # add a new session.
            _logsi:SISession = si.AddSession("Main", True)
            _logsi.Level = SILevel.Debug

            # return session instance to caller.
            return _logsi

        except Exception as ex:

            print(str(ex))
            raise


    def test_ProtocolTcp(self):
        """
        Test TCP Protocol scenarios.
        """
        _logsi:SISession = None

        try:

            # set connections string: tcp protocol:
            # - host=localhost (SI Console is running on same machine).
            # - port=4228      (SI Console tcp server is listening is running on same machine).
            conn:str = "tcp(host=localhost,port=4228,timeout=30000,reconnect=true,reconnect.interval=10s,async.enabled=false)"

            # create a new smartinspect session for logging.
            _logsi = Test_Protocols.CreateSISession(conn)

            for level in SILevel:

                # ignore the Control level.
                if (level == SILevel.Control):
                    continue

                # reset counters for next test.
                SIEventHandlerClass.ResetCounters(_logsi.Parent)

                # write packet events to console.
                SIEventHandlerClass.WriteEventPacketsToConsole = True;

                # test all session methods, using specified logging level.
                _logsi.Parent.Level = level
                _logsi.Parent.DefaultLevel = level
                TestSessionMethods.TestAllMethods(_logsi)

                # print SI event counts.
                SIEventHandlerClass.PrintResults(_logsi.Parent)

                # verify log entry counts; fail test if count does not match expected value for the specified level.
                SIEventHandlerClass.VerifyLogEntryCounts(_logsi, level, TestSessionMethods.TestAllMethods_LogEntryCounts)
                SIEventHandlerClass.VerifyErrorCount(_logsi, level)

                print("Test was Successful!")

        except Exception as ex:

            print(str(ex))
            raise

        finally:

            # unwire test events, and dispose of SmartInspect oject.
            if (_logsi != None):
                SIEventHandlerClass.UnWireEvents(_logsi.Parent)
                _logsi.Parent.Dispose()


    def test_ProtocolTcpAsync(self):
        """
        Test TCP Protocol scenarios, using Asyncronous packet processing.
        """
        _logsi:SISession = None

        try:

            # set connections string: tcp protocol:
            # - host=localhost  (SI Console is running on same machine).
            # - port=4228       (SI Console tcp server is listening is running on same machine).
            # - async=true      (Send packets to SI Console asyncronously on a separate thread).
            conn:str = "tcp(host=localhost,port=4228,timeout=30000,reconnect=true,reconnect.interval=10s,async.enabled=true)"

            # create a new smartinspect session for logging.
            _logsi = Test_Protocols.CreateSISession(conn)

            for level in SILevel:

                # ignore the Control level.
                if (level == SILevel.Control):
                    continue

                # reset counters for next test.
                SIEventHandlerClass.ResetCounters(_logsi.Parent)

                # test all session methods, using specified logging level.
                _logsi.Parent.Level = level
                TestSessionMethods.TestAllMethods(_logsi)

                # print SI event counts.
                SIEventHandlerClass.PrintResults(_logsi.Parent)

                # if any errors occured, then fail the test.
                #if SIEventHandlerClass.ErrorCount > 0:
                #    raise Exception("ErrorCount > 0 for level {0} test!  See console output for more details.".format(str(level)))

        except Exception as ex:

            print(str(ex))
            raise

        finally:

            # unwire test events, and dispose of SmartInspect oject.
            if (_logsi != None):
                SIEventHandlerClass.UnWireEvents(_logsi.Parent)
                _logsi.Parent.Dispose()


    def test_ProtocolPipe(self):
        """
        Test Pipe Protocol scenarios.
        """
        _logsi:SISession = None

        try:

            # set connections string: pipe protocol:
            # - pipename=smartinspect (SI Console is running on same machine).
            conn:str = "pipe(pipename=smartinspect,reconnect=true,reconnect.interval=10s,async.enabled=false)"

            # create a new smartinspect session for logging.
            _logsi = Test_Protocols.CreateSISession(conn)

            for level in SILevel:

                # ignore the Control level.
                if (level == SILevel.Control):
                    continue

                # reset counters for next test.
                SIEventHandlerClass.ResetCounters(_logsi.Parent)

                # test all session methods, using specified logging level.
                _logsi.Parent.Level = level
                TestSessionMethods.TestAllMethods(_logsi)

                # print SI event counts.
                SIEventHandlerClass.PrintResults(_logsi.Parent)

                # verify log entry counts; fail test if count does not match expected value for the specified level.
                SIEventHandlerClass.VerifyLogEntryCounts(_logsi, level, TestSessionMethods.TestAllMethods_LogEntryCounts)
                SIEventHandlerClass.VerifyErrorCount(_logsi, level)

                print("Test was Successful!")

        except Exception as ex:

            print(str(ex))
            raise

        finally:

            # unwire test events, and dispose of SmartInspect oject.
            if (_logsi != None):
                SIEventHandlerClass.UnWireEvents(_logsi.Parent)
                _logsi.Parent.Dispose()


    def test_ProtocolPipeAsync(self):
        """
        Test Pipe Protocol scenarios, using Asyncronous packet processing.
        """
        _logsi:SISession = None

        try:

            # set connections string: pipe protocol:
            # - pipename=smartinspect (SI Console is running on same machine).
            # - async=true      (Send packets to SI Console asyncronously on a separate thread).
            conn:str = "pipe(pipename=smartinspect,reconnect=true,reconnect.interval=10s,async.enabled=true)"

            # create a new smartinspect session for logging.
            _logsi = Test_Protocols.CreateSISession(conn)

            for level in SILevel:

                # ignore the Control level.
                if (level == SILevel.Control):
                    continue

                # reset counters for next test.
                SIEventHandlerClass.ResetCounters(_logsi.Parent)

                # test all session methods, using specified logging level.
                _logsi.Parent.Level = level
                TestSessionMethods.TestAllMethods(_logsi)

                # print SI event counts.
                SIEventHandlerClass.PrintResults(_logsi.Parent)

                # verify log entry counts; fail test if count does not match expected value for the specified level.
                SIEventHandlerClass.VerifyLogEntryCounts(_logsi, level, TestSessionMethods.TestAllMethods_LogEntryCounts)
                SIEventHandlerClass.VerifyErrorCount(_logsi, level)

                print("Test was Successful!")

        except Exception as ex:

            print(str(ex))
            raise

        finally:

            # unwire test events, and dispose of SmartInspect oject.
            if (_logsi != None):
                SIEventHandlerClass.UnWireEvents(_logsi.Parent)
                _logsi.Parent.Dispose()


if __name__ == '__main__':
    unittest.main()
