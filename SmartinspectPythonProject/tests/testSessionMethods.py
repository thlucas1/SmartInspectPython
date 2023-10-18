from array import array as arr
from datetime import datetime
import threading
from inspect import FrameInfo
import inspect
import os
import sys

# our package imports.
from smartinspectpython.sisession import SISession
from smartinspectpython.silevel import SILevel
from smartinspectpython.sicolor import SIColors, SIColor
from smartinspectpython.sisourceid import SISourceId
from smartinspectpython.siviewerid import SIViewerId
from smartinspectpython.sitextcontext import SITextContext
from smartinspectpython.sivaluelistviewercontext import SIValueListViewerContext
from smartinspectpython.sicontrolcommandtype import SIControlCommandType
from smartinspectpython.silogentrytype import SILogEntryType
from smartinspectpython.siprocessflowtype import SIProcessFlowType
from smartinspectpython.siwatchtype import SIWatchType


# import classes used for test scenarios.
from testClassDefinitions import TestMethodTracking, TestFileAccessHelper, TestLogObjectHelper

# auto-generate the "__all__" variable with classes decorated with "@export".
from smartinspectpython.siutils import export


@export
class TestSessionMethods:
    """
    Helper class for SmartInspect SISession class testing.
    """

    # TestAllMethods method message count values for each log level type.
    TestAllMethods_LogEntryCounts = {}
    TestAllMethods_LogEntryCounts[str(SILevel.Debug.name)] = 983
    TestAllMethods_LogEntryCounts[str(SILevel.Verbose.name)] = 768
    TestAllMethods_LogEntryCounts[str(SILevel.Message.name)] = 656
    TestAllMethods_LogEntryCounts[str(SILevel.Warning.name)] = 538
    TestAllMethods_LogEntryCounts[str(SILevel.Error.name)] = 428
    TestAllMethods_LogEntryCounts[str(SILevel.Fatal.name)] = 313

    @staticmethod
    def TestAllMethods(logsi:SISession) -> None:
        """
        Tests all session methods (Log, Watch, Clear, etc).

        Args:
            logsi
                SmartInspect session object.
        """

        # data used by various tests.
        exedir = os.path.dirname(sys.argv[0])
        testdataPfx:str = exedir + "/testdata/"
        testdataPath:str = ""
        testtext:str = ""
        testdate:datetime = datetime.now()
        binaryBytes:bytes = bytes([0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f,0x10,0x11,0x12,0x13,0x14,0x15,0x16])
        argsVar1:str="Argument 1 Value"
        argsVar2:int=1000

        print("-----------------------------------------------------------------------------------------")
        print("Test ALL Session Methods Starting")
        print("- SI Parent Level = " + logsi.Parent.Level.name)
        print("- SI Parent Default Level = " + logsi.Parent.DefaultLevel.name)
        print("- SI Session Level = " + logsi.Level.name)
        print("- Test Data Path Prefix = " + os.path.abspath(testdataPfx))
        print("-----------------------------------------------------------------------------------------")

        # log the following with SILevel.Error so it is always logged.
        logsi.LogSeparator(SILevel.Fatal)
        logsi.LogColored(SILevel.Fatal, SIColors.White, "Test ALL Session Methods Starting")
        logsi.LogValue(SILevel.Fatal, "SI Parent Level", logsi.Parent.Level)
        logsi.LogValue(SILevel.Fatal, "SI Parent Default Level", logsi.Parent.DefaultLevel)
        logsi.LogValue(SILevel.Fatal, "SI Session Level", logsi.Level)
        logsi.LogValue(SILevel.Fatal, "Test Data Path Prefix", os.path.abspath(testdataPfx))

        try:

            # ClearAll Examples.
            #logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ClearAll Examples.")
            #logsi.LogColored(SILevel.Fatal, SIColors.White, "Clearing all entries in the SI Console.")
            #logsi.ClearAll(SILevel.Fatal)

            # ClearAutoViews Examples.
            #logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ClearAutoViews Examples.")
            #logsi.LogColored(SILevel.Fatal, SIColors.White, "Clearing all AutoView entries used in this test.  AutoViews are defined in the SI Console under Edit.AutoViews.")
            #logsi.ClearAutoViews(SILevel.Fatal)

            ## ClearLog Examples.
            #logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ClearLog Examples.")
            #logsi.LogColored(SILevel.Fatal, SIColors.White, "Clearing all Log entries used in this test.  Log entries are located in the Log Entry toolbox panel of the SI Console.")
            #logsi.ClearLog(SILevel.Fatal)

            # ClearProcessFlow Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ClearProcessFlow Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Clearing all Process Flow entries used in this test.  Process Flow entries are located in the Process Flow toolbox panel of the SI Console.")
            logsi.ClearProcessFlow(SILevel.Fatal)

            # ClearWatches Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ClearWatches Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Clearing all Watch values used in this test.  Watch values are located in the Watches panel of the SI Console.")
            logsi.ClearWatches(SILevel.Fatal)

            # ResetCallStack Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ResetCallstack Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Resetting CallStack entries.  Call Stack entries are located in the Call Stack panel of the SI Console.")
            logsi.ResetCallstack(None)    # reset call stack, since we are looping thru this Example.
            logsi.ResetCallstack(SILevel.Debug)
            logsi.ResetCallstack(SILevel.Verbose)
            logsi.ResetCallstack(SILevel.Message)
            logsi.ResetCallstack(SILevel.Warning)
            logsi.ResetCallstack(SILevel.Error)
            logsi.ResetCallstack(SILevel.Fatal)

            # AddCheckpoint / ResetCheckpoint Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ResetCheckpoint Examples (Resetting All CheckPoint Names).")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Resetting ALL Checkpoint names used in this test.")
            logsi.ResetCheckpoint()    # reset all checkpoints, since we are looping thru this Example.
            logsi.ResetCheckpoint("MyCheckPointName NoLevel")
            logsi.ResetCheckpoint("MyCheckPointName NoLevel NoTitle")
            logsi.ResetCheckpoint("MyCheckPointName Debug")
            logsi.ResetCheckpoint("MyCheckPointName Verbose")
            logsi.ResetCheckpoint("MyCheckPointName Message")
            logsi.ResetCheckpoint("MyCheckPointName Warning")
            logsi.ResetCheckpoint("MyCheckPointName Error")
            logsi.ResetCheckpoint("MyCheckPointName Fatal")

            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.AddCheckpoint Examples (2 checkpoints per Level).")
            logsi.AddCheckpoint(None, "MyCheckPointName NoLevel", "AddCheckpoint NoLevel MyCheckpointName 01 Example.")
            logsi.AddCheckpoint(SILevel.Debug, "MyCheckPointName Debug", "AddCheckpoint Debug MyCheckpointName 01 Example.")
            logsi.AddCheckpoint(SILevel.Verbose, "MyCheckPointName Verbose", "AddCheckpoint Verbose MyCheckpointName 01 Example.")
            logsi.AddCheckpoint(SILevel.Message, "MyCheckPointName Message", "AddCheckpoint Message MyCheckpointName 01 Example.")
            logsi.AddCheckpoint(SILevel.Warning, "MyCheckPointName Warning", "AddCheckpoint Warning MyCheckpointName 01 Example.")
            logsi.AddCheckpoint(SILevel.Error, "MyCheckPointName Error", "AddCheckpoint Error MyCheckpointName 01 Example.")
            logsi.AddCheckpoint(SILevel.Fatal, "MyCheckPointName Fatal", "AddCheckpoint Fatal MyCheckpointName 01 Example.")

            logsi.AddCheckpoint(None, "MyCheckPointName NoLevel", "AddCheckpoint NoLevel MyCheckpointName 02 Example.")
            logsi.AddCheckpoint(SILevel.Debug, "MyCheckPointName Debug", "AddCheckpoint Debug MyCheckpointName 02 Example.")
            logsi.AddCheckpoint(SILevel.Verbose, "MyCheckPointName Verbose", "AddCheckpoint Verbose MyCheckpointName 02 Example.")
            logsi.AddCheckpoint(SILevel.Message, "MyCheckPointName Message", "AddCheckpoint Message MyCheckpointName 02 Example.")
            logsi.AddCheckpoint(SILevel.Warning, "MyCheckPointName Warning", "AddCheckpoint Warning MyCheckpointName 02 Example.")
            logsi.AddCheckpoint(SILevel.Error, "MyCheckPointName Error", "AddCheckpoint Error MyCheckpointName 02 Example.")
            logsi.AddCheckpoint(SILevel.Fatal, "MyCheckPointName Fatal", "AddCheckpoint Fatal MyCheckpointName 02 Example.")

            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.AddCheckpoint Examples (4 checkpoints, No Level, No Title).")
            logsi.AddCheckpoint("MyCheckPointName NoLevel NoTitle")
            logsi.AddCheckpoint("MyCheckPointName NoLevel NoTitle")
            logsi.AddCheckpoint("MyCheckPointName NoLevel NoTitle")
            logsi.AddCheckpoint("MyCheckPointName NoLevel NoTitle")

            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.AddCheckpoint Examples (4 checkpoints, No Level, No Title, No Name).")
            logsi.AddCheckpoint()
            logsi.AddCheckpoint()
            logsi.AddCheckpoint()
            logsi.AddCheckpoint()

            # CurrentMethodName Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.CurrentMethodName, CurrentMethodNameClass, CurrentMethodNameClassNamespace Examples.")
            logsi.LogValue(SILevel.Fatal, "SISession.CurrentMethodName", SISession.CurrentMethodName())
            logsi.LogValue(SILevel.Fatal, "SISession.CurrentMethodNameClass", SISession.CurrentMethodNameClass())
            logsi.LogValue(SILevel.Fatal, "SISession.CurrentMethodNameClassNamespace", SISession.CurrentMethodNameClassNamespace())

            # DecCounter / ResetCounter Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ResetCounter Examples (Resetting All PyDecCounter1 values).")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Resetting ALL PyDecCounter1 value used in this test.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyDecCounter1 values are located in the Watches panel of the SI Console.")
            logsi.ResetCounter("PyDecCounter1 NoLevel")  # reset all counters, since we are looping thru this Example.
            logsi.ResetCounter("PyDecCounter1 Debug")
            logsi.ResetCounter("PyDecCounter1 Verbose")
            logsi.ResetCounter("PyDecCounter1 Message")
            logsi.ResetCounter("PyDecCounter1 Warning")
            logsi.ResetCounter("PyDecCounter1 Error")
            logsi.ResetCounter("PyDecCounter1 Fatal")

            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.IncCounter Examples (PyDecCounter1 count=0 per Level).")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyDecCounter1 values are located in the Watches panel of the SI Console.")
            logsi.IncCounter(None, "PyDecCounter1 NoLevel")
            logsi.IncCounter(SILevel.Debug, "PyDecCounter1 Debug")
            logsi.IncCounter(SILevel.Verbose, "PyDecCounter1 Verbose")
            logsi.IncCounter(SILevel.Message, "PyDecCounter1 Message")
            logsi.IncCounter(SILevel.Warning, "PyDecCounter1 Warning")
            logsi.IncCounter(SILevel.Error, "PyDecCounter1 Error")
            logsi.IncCounter(SILevel.Fatal, "PyDecCounter1 Fatal")

            logsi.DecCounter(None, "PyDecCounter1 NoLevel")
            logsi.DecCounter(SILevel.Debug, "PyDecCounter1 Debug")
            logsi.DecCounter(SILevel.Verbose, "PyDecCounter1 Verbose")
            logsi.DecCounter(SILevel.Message, "PyDecCounter1 Message")
            logsi.DecCounter(SILevel.Warning, "PyDecCounter1 Warning")
            logsi.DecCounter(SILevel.Error, "PyDecCounter1 Error")
            logsi.DecCounter(SILevel.Fatal, "PyDecCounter1 Fatal")

            # EnterMethod / LeaveMethod Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.EnterMethod, LeaveMethod Examples.")
            logsi.EnterMethod(None, "EnterMethod NoLevel Example")
            logsi.EnterMethod(SILevel.Debug, "EnterMethod Debug Example")
            logsi.EnterMethod(SILevel.Verbose, "EnterMethod Verbose Example")
            logsi.EnterMethod(SILevel.Message, "EnterMethod Message Example")
            logsi.EnterMethod(SILevel.Warning, "EnterMethod Warning Example")
            logsi.EnterMethod(SILevel.Error, "EnterMethod Error Example")
            logsi.EnterMethod(SILevel.Fatal, "EnterMethod Fatal Example")
            logsi.LogDebug("EnterMethod Debug Example - This is a debug message.  It will not be displayed if Level=Verbose or above.")
            logsi.LogVerbose("EnterMethod Verbose Example - This is a verbose message.  It will not be displayed if Level=Message or above.")
            logsi.LogMessage("EnterMethod Message Example - This is a message.  It will not be displayed if Level=Warning or above.")
            logsi.LogWarning("EnterMethod Warning Example - This is a warning message.  It will not be displayed if Level=Error or above.")
            logsi.LogError("EnterMethod Error Example - This is a error message.  It will not be displayed if Level=Fatal or above.")
            logsi.LogFatal("EnterMethod Fatal Example - This is a fatal message.")
            logsi.LeaveMethod(SILevel.Fatal, "LeaveMethod Fatal Example")
            logsi.LeaveMethod(SILevel.Error, "LeaveMethod Error Example")
            logsi.LeaveMethod(SILevel.Warning, "LeaveMethod Warning Example")
            logsi.LeaveMethod(SILevel.Message, "LeaveMethod Message Example")
            logsi.LeaveMethod(SILevel.Verbose, "LeaveMethod Verbose Example")
            logsi.LeaveMethod(SILevel.Debug, "LeaveMethod Debug Example")
            logsi.LeaveMethod(None, "LeaveMethod NoLevel Example")

            logsi.LogColored(SILevel.Fatal, SIColors.White, "The following tests will display the current method name since no Title is specified on the EnterMethod and LeaveMethod call.")
            logsi.EnterMethod(None)
            logsi.EnterMethod(SILevel.Debug)
            logsi.EnterMethod(SILevel.Verbose)
            logsi.EnterMethod(SILevel.Message)
            logsi.EnterMethod(SILevel.Warning)
            logsi.EnterMethod(SILevel.Error)
            logsi.EnterMethod(SILevel.Fatal)
            logsi.LogDebug("EnterMethod Debug Example - This is a debug message.  It will not be displayed if Level=Verbose or above.")
            logsi.LogVerbose("EnterMethod Verbose Example - This is a verbose message.  It will not be displayed if Level=Message or above.")
            logsi.LogMessage("EnterMethod Message Example - This is a message.  It will not be displayed if Level=Warning or above.")
            logsi.LogWarning("EnterMethod Warning Example - This is a warning message.  It will not be displayed if Level=Error or above.")
            logsi.LogError("EnterMethod Error Example - This is a error message.  It will not be displayed if Level=Fatal or above.")
            logsi.LogFatal("EnterMethod Fatal Example - This is a fatal message.")
            logsi.LeaveMethod(SILevel.Fatal)
            logsi.LeaveMethod(SILevel.Error)
            logsi.LeaveMethod(SILevel.Warning)
            logsi.LeaveMethod(SILevel.Message)
            logsi.LeaveMethod(SILevel.Verbose)
            logsi.LeaveMethod(SILevel.Debug)
            logsi.LeaveMethod(None)

            # EnterProcess / LeaveProcess Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.EnterProcess, LeaveProcess Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Process Names are located in the Process Flow panel of the SI Console.")
            logsi.EnterProcess(None, "My Process NoLevel")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "My Process NoLevel has been entered.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "My Process NoLevel is exiting ...")
            logsi.LeaveProcess(None, "My Process NoLevel")

            logsi.EnterProcess(SILevel.Debug, "My Process Debug")
            logsi.LogColored(SILevel.Debug, SIColors.White, "My Process Debug has been entered.")
            logsi.LogColored(SILevel.Debug, SIColors.White, "My Process Debug is exiting ...")
            logsi.LeaveProcess(SILevel.Debug, "My Process Debug")

            logsi.EnterProcess(SILevel.Verbose, "My Process Verbose")
            logsi.LogColored(SILevel.Verbose, SIColors.White, "My Process Verbose has been entered.")
            logsi.LogColored(SILevel.Verbose, SIColors.White, "My Process Verbose is exiting ...")
            logsi.LeaveProcess(SILevel.Verbose, "My Process Verbose")

            logsi.EnterProcess(SILevel.Message, "My Process Message")
            logsi.LogColored(SILevel.Message, SIColors.White, "My Process Message has been entered.")
            logsi.LogColored(SILevel.Message, SIColors.White, "My Process Message is exiting ...")
            logsi.LeaveProcess(SILevel.Message, "My Process Message")

            logsi.EnterProcess(SILevel.Warning, "My Process Warning")
            logsi.LogColored(SILevel.Warning, SIColors.White, "My Process Warning has been entered.")
            logsi.LogColored(SILevel.Warning, SIColors.White, "My Process Warning is exiting ...")
            logsi.LeaveProcess(SILevel.Warning, "My Process Warning")

            logsi.EnterProcess(SILevel.Error, "My Process Error")
            logsi.LogColored(SILevel.Error, SIColors.White, "My Process Error has been entered.")
            logsi.LogColored(SILevel.Error, SIColors.White, "My Process Error is exiting ...")
            logsi.LeaveProcess(SILevel.Error, "My Process Error")

            logsi.EnterProcess(SILevel.Fatal, "My Process Fatal")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "My Process Fatal has been entered.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "My Process Fatal is exiting ...")
            logsi.LeaveProcess(SILevel.Fatal, "My Process Fatal")

            # EnterThread / LeaveThread Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.EnterThread, LeaveThread Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Thread Names are located in the Process Flow panel of the SI Console.")
            logsi.EnterThread(None, "My Thread NoLevel")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "My Thread NoLevel has been entered.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "My Thread NoLevel is exiting ...")
            logsi.LeaveThread(None, "My Thread NoLevel")

            logsi.EnterThread(SILevel.Debug, "My Thread Debug")
            logsi.LogColored(SILevel.Debug, SIColors.White, "My Thread Debug has been entered.")
            logsi.LogColored(SILevel.Debug, SIColors.White, "My Thread Debug is exiting ...")
            logsi.LeaveThread(SILevel.Debug, "My Thread Debug")

            logsi.EnterThread(SILevel.Verbose, "My Thread Verbose")
            logsi.LogColored(SILevel.Verbose, SIColors.White, "My Thread Verbose has been entered.")
            logsi.LogColored(SILevel.Verbose, SIColors.White, "My Thread Verbose is exiting ...")
            logsi.LeaveThread(SILevel.Verbose, "My Thread Verbose")

            logsi.EnterThread(SILevel.Message, "My Thread Message")
            logsi.LogColored(SILevel.Message, SIColors.White, "My Thread Message has been entered.")
            logsi.LogColored(SILevel.Message, SIColors.White, "My Thread Message is exiting ...")
            logsi.LeaveThread(SILevel.Message, "My Thread Message")

            logsi.EnterThread(SILevel.Warning, "My Thread Warning")
            logsi.LogColored(SILevel.Warning, SIColors.White, "My Thread Warning has been entered.")
            logsi.LogColored(SILevel.Warning, SIColors.White, "My Thread Warning is exiting ...")
            logsi.LeaveThread(SILevel.Warning, "My Thread Warning")

            logsi.EnterThread(SILevel.Error, "My Thread Error")
            logsi.LogColored(SILevel.Error, SIColors.White, "My Thread Error has been entered.")
            logsi.LogColored(SILevel.Error, SIColors.White, "My Thread Error is exiting ...")
            logsi.LeaveThread(SILevel.Error, "My Thread Error")

            logsi.EnterThread(SILevel.Fatal, "My Thread Fatal")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "My Thread Fatal has been entered.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "My Thread Fatal is exiting ...")
            logsi.LeaveThread(SILevel.Fatal, "My Thread Fatal")

            # GetMethodName Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.GetMethodName Examples.")
            logsi.LogValue(SILevel.Fatal, "SISession.GetMethodName(0)", SISession.GetMethodName(0, True, True))
            logsi.LogValue(SILevel.Fatal, "SISession.GetMethodName(1)", SISession.GetMethodName(1, True, True))
            logsi.LogValue(SILevel.Fatal, "SISession.GetMethodName(2)", SISession.GetMethodName(2, True, True))
            logsi.LogValue(SILevel.Fatal, "SISession.GetMethodName(0) no namespace", SISession.GetMethodName(0, False, True))
            logsi.LogValue(SILevel.Fatal, "SISession.GetMethodName(0) no class", SISession.GetMethodName(0, False, False))

            # IncCounter / ResetCounter Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ResetCounter Examples (Resetting All PyIncCounter1 values).")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Resetting ALL PyIncCounter1 value used in this test.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyIncCounter1 values are located in the Watches panel of the SI Console.")
            logsi.ResetCounter("PyIncCounter1 NoLevel")  # reset all counters, since we are looping thru this Example.
            logsi.ResetCounter("PyIncCounter1 Debug")
            logsi.ResetCounter("PyIncCounter1 Verbose")
            logsi.ResetCounter("PyIncCounter1 Message")
            logsi.ResetCounter("PyIncCounter1 Warning")
            logsi.ResetCounter("PyIncCounter1 Error")
            logsi.ResetCounter("PyIncCounter1 Fatal")

            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.IncCounter Examples (PyIncCounter1 count=2 per Level).")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyIncCounter1 values are located in the Watches panel of the SI Console.")
            logsi.IncCounter(None, "PyIncCounter1 NoLevel")
            logsi.IncCounter(SILevel.Debug, "PyIncCounter1 Debug")
            logsi.IncCounter(SILevel.Verbose, "PyIncCounter1 Verbose")
            logsi.IncCounter(SILevel.Message, "PyIncCounter1 Message")
            logsi.IncCounter(SILevel.Warning, "PyIncCounter1 Warning")
            logsi.IncCounter(SILevel.Error, "PyIncCounter1 Error")
            logsi.IncCounter(SILevel.Fatal, "PyIncCounter1 Fatal")

            logsi.IncCounter(None, "PyIncCounter1 NoLevel")
            logsi.IncCounter(SILevel.Debug, "PyIncCounter1 Debug")
            logsi.IncCounter(SILevel.Verbose, "PyIncCounter1 Verbose")
            logsi.IncCounter(SILevel.Message, "PyIncCounter1 Message")
            logsi.IncCounter(SILevel.Warning, "PyIncCounter1 Warning")
            logsi.IncCounter(SILevel.Error, "PyIncCounter1 Error")
            logsi.IncCounter(SILevel.Fatal, "PyIncCounter1 Fatal")

            # LogAppDomain Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogAppDomain Examples.")
            logsi.LogAppDomain(None, "LogAppDomain NoLevel Example")
            logsi.LogAppDomain(SILevel.Debug, "LogAppDomain Debug Example")
            logsi.LogAppDomain(SILevel.Verbose, "LogAppDomain Verbose Example")
            logsi.LogAppDomain(SILevel.Message, "LogAppDomain Message Example")
            logsi.LogAppDomain(SILevel.Warning, "LogAppDomain Warning Example")
            logsi.LogAppDomain(SILevel.Error, "LogAppDomain Error Example")
            logsi.LogAppDomain(SILevel.Fatal, "LogAppDomain Fatal Example")

            # LogArray Examples.
            arrayInteger:arr = arr('i', [3, 6, 9, 12])
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogArray Examples.")
            logsi.LogArray(None, "LogArray NoLevel [int] Example", arrayInteger)
            logsi.LogArray(SILevel.Debug, "LogArray Debug [int] Example", arrayInteger)
            logsi.LogArray(SILevel.Verbose, "LogArray Verbose [int] Example", arrayInteger)
            logsi.LogArray(SILevel.Message, "LogArray Message [int] Example", arrayInteger)
            logsi.LogArray(SILevel.Warning, "LogArray Warning [int] Example", arrayInteger)
            logsi.LogArray(SILevel.Error, "LogArray Error [int] Example", arrayInteger)
            logsi.LogArray(SILevel.Fatal, "LogArray Fatal [int] Example", arrayInteger)

            arrayString:arr = arr('u', 'hello \u2641')
            logsi.LogArray(None, "LogArray NoLevel [string] Example", arrayString)
            logsi.LogArray(SILevel.Debug, "LogArray Debug [string] Example", arrayString)
            logsi.LogArray(SILevel.Verbose, "LogArray Verbose [string] Example", arrayString)
            logsi.LogArray(SILevel.Message, "LogArray Message [string] Example", arrayString)
            logsi.LogArray(SILevel.Warning, "LogArray Warning [string] Example", arrayString)
            logsi.LogArray(SILevel.Error, "LogArray Error [string] Example", arrayString)
            logsi.LogArray(SILevel.Fatal, "LogArray Fatal [string] Example", arrayString)

            arrayLong:arr = arr('l', [1, 2, 3, 4, 5])
            logsi.LogArray(None, "LogArray NoLevel [long] Example", arrayLong)
            logsi.LogArray(SILevel.Debug, "LogArray Debug [long] Example", arrayLong)
            logsi.LogArray(SILevel.Verbose, "LogArray Verbose [long] Example", arrayLong)
            logsi.LogArray(SILevel.Message, "LogArray Message [long] Example", arrayLong)
            logsi.LogArray(SILevel.Warning, "LogArray Warning [long] Example", arrayLong)
            logsi.LogArray(SILevel.Error, "LogArray Error [long] Example", arrayLong)
            logsi.LogArray(SILevel.Fatal, "LogArray Fatal [long] Example", arrayLong)

            arrayDecimal:arr = arr('d', [1.0, 2.0, 3.14])
            logsi.LogArray(None, "LogArray NoLevel [decimal] Example", arrayDecimal)
            logsi.LogArray(SILevel.Debug, "LogArray Debug [decimal] Example", arrayDecimal)
            logsi.LogArray(SILevel.Verbose, "LogArray Verbose [decimal] Example", arrayDecimal)
            logsi.LogArray(SILevel.Message, "LogArray Message [decimal] Example", arrayDecimal)
            logsi.LogArray(SILevel.Warning, "LogArray Warning [decimal] Example", arrayDecimal)
            logsi.LogArray(SILevel.Error, "LogArray Error [decimal] Example", arrayDecimal)
            logsi.LogArray(SILevel.Fatal, "LogArray Fatal [decimal] Example", arrayDecimal)

            arrayFloat:arr = arr('f', [1.0, 2.1, 3.14159])
            logsi.LogArray(None, "LogArray NoLevel [float] Example", arrayFloat)
            logsi.LogArray(SILevel.Debug, "LogArray Debug [float] Example", arrayFloat)
            logsi.LogArray(SILevel.Verbose, "LogArray Verbose [float] Example", arrayFloat)
            logsi.LogArray(SILevel.Message, "LogArray Message [float] Example", arrayFloat)
            logsi.LogArray(SILevel.Warning, "LogArray Warning [float] Example", arrayFloat)
            logsi.LogArray(SILevel.Error, "LogArray Error [float] Example", arrayFloat)
            logsi.LogArray(SILevel.Fatal, "LogArray Fatal [float] Example", arrayFloat)

            # LogAssert Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogAssert Examples")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Note that LogAssert messages will only show for SILevel.Error and below.")
            logsi.LogAssert(True == True, "LogAssert condition is TRUE Example")
            logsi.LogAssert(True == False, "LogAssert condition is FALSE Example")

            # LogAssigned Examples.
            parametervalue:str = "is not null"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogAssigned Examples")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Note that LogAssigned messages will only show for SILevel.Message and below.")
            logsi.LogAssigned(None, "LogAssigned NoLevel is assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Debug, "LogAssigned Debug is assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Verbose, "LogAssigned Verbose is assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Message, "LogAssigned Message is assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Warning, "LogAssigned Warning is assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Error, "LogAssigned Error is assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Fatal, "LogAssigned Fatal is assigned Example", parametervalue)

            parametervalue = None
            logsi.LogAssigned(None, "LogAssigned NoLevel is not assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Debug, "LogAssigned Debug is not assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Verbose, "LogAssigned Verbose is not assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Message, "LogAssigned Message is not assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Warning, "LogAssigned Warning is not assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Error, "LogAssigned Error is not assigned Example", parametervalue)
            logsi.LogAssigned(SILevel.Fatal, "LogAssigned Fatal is not assigned Example", parametervalue)

            # LogBinary Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogBinary Examples.")
            logsi.LogBinary(None, "LogBinary NoLevel Example", binaryBytes)
            logsi.LogBinary(SILevel.Debug, "LogBinary Debug Example", binaryBytes)
            logsi.LogBinary(SILevel.Verbose, "LogBinary Verbose Example", binaryBytes)
            logsi.LogBinary(SILevel.Message, "LogBinary Message Example", binaryBytes)
            logsi.LogBinary(SILevel.Warning, "LogBinary Warning Example", binaryBytes)
            logsi.LogBinary(SILevel.Error, "LogBinary Error Example", binaryBytes)
            logsi.LogBinary(SILevel.Fatal, "LogBinary Fatal Example", binaryBytes)

            logsi.LogBinary(None, "LogBinary NoLevel Example - Skip first 5 bytes, include 2 bytes after [5:2]", binaryBytes, 5, 2)
            logsi.LogBinary(SILevel.Debug, "LogBinary Debug Example - Skip first 5 bytes, include 2 bytes after [5:2]", binaryBytes, 5, 2)
            logsi.LogBinary(SILevel.Verbose, "LogBinary Verbose Example - Skip first 5 bytes, include 2 bytes after [5:2]", binaryBytes, 5, 2)
            logsi.LogBinary(SILevel.Message, "LogBinary Message Example - Skip first 5 bytes, include 2 bytes after [5:2]", binaryBytes, 5, 2)
            logsi.LogBinary(SILevel.Warning, "LogBinary Warning Example - Skip first 5 bytes, include 2 bytes after [5:2]", binaryBytes, 5, 2)
            logsi.LogBinary(SILevel.Error, "LogBinary Error Example - Skip first 5 bytes, include 2 bytes after [5:2]", binaryBytes, 5, 2)
            logsi.LogBinary(SILevel.Fatal, "LogBinary Fatal Example - Skip first 5 bytes, include 2 bytes after [5:2]", binaryBytes, 5, 2)

            # LogBinaryFile Examples.
            testdataPath = testdataPfx + "TestSourceHTML.html"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogBinaryFile Examples.")
            logsi.LogBinaryFile(None, "LogBinaryFile NoLevel Example", testdataPath)
            logsi.LogBinaryFile(SILevel.Debug, "LogBinaryFile Debug Example", testdataPath)
            logsi.LogBinaryFile(SILevel.Verbose, "LogBinaryFile Verbose Example", testdataPath)
            logsi.LogBinaryFile(SILevel.Message, "LogBinaryFile Message Example", testdataPath)
            logsi.LogBinaryFile(SILevel.Warning, "LogBinaryFile Warning Example", testdataPath)
            logsi.LogBinaryFile(SILevel.Error, "LogBinaryFile Error Example", testdataPath)
            logsi.LogBinaryFile(SILevel.Fatal, "LogBinaryFile Fatal Example", testdataPath)

            # LogBinaryStream Examples.
            testdataPath = testdataPfx + "TestSourceHTML.html"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogBinaryStream Examples.")
            with open(testdataPath, 'rb') as binaryStream: 
                logsi.LogBinaryStream(None, "LogBinaryStream NoLevel Example", binaryStream)
                logsi.LogBinaryStream(SILevel.Debug, "LogBinaryStream Debug Example", binaryStream)
                logsi.LogBinaryStream(SILevel.Verbose, "LogBinaryStream Verbose Example", binaryStream)
                logsi.LogBinaryStream(SILevel.Message, "LogBinaryStream Message Example", binaryStream)
                logsi.LogBinaryStream(SILevel.Warning, "LogBinaryStream Warning Example", binaryStream)
                logsi.LogBinaryStream(SILevel.Error, "LogBinaryStream Error Example", binaryStream)
                logsi.LogBinaryStream(SILevel.Fatal, "LogBinaryStream Fatal Example", binaryStream)

            # LogBitmapFile Examples.
            testdataPath = testdataPfx + "TestBMP.bmp"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogBitmapFile Examples.")
            logsi.LogBitmapFile(None, "LogBitmapFile NoLevel Example", testdataPath)
            logsi.LogBitmapFile(SILevel.Debug, "LogBitmapFile Debug Example", testdataPath)
            logsi.LogBitmapFile(SILevel.Verbose, "LogBitmapFile Verbose Example", testdataPath)
            logsi.LogBitmapFile(SILevel.Message, "LogBitmapFile Message Example", testdataPath)
            logsi.LogBitmapFile(SILevel.Warning, "LogBitmapFile Warning Example", testdataPath)
            logsi.LogBitmapFile(SILevel.Error, "LogBitmapFile Error Example", testdataPath)
            logsi.LogBitmapFile(SILevel.Fatal, "LogBitmapFile Fatal Example", testdataPath)

            # LogBitmapStream Examples.
            testdataPath = testdataPfx + "TestBMP.bmp"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogBitmapStream Examples.")
            with open(testdataPath, 'rb') as binaryStream:
                logsi.LogBitmapStream(None, "LogBitmapStream NoLevel Example", binaryStream)
                logsi.LogBitmapStream(SILevel.Debug, "LogBitmapStream Debug Example", binaryStream)
                logsi.LogBitmapStream(SILevel.Verbose, "LogBitmapStream Verbose Example", binaryStream)
                logsi.LogBitmapStream(SILevel.Message, "LogBitmapStream Message Example", binaryStream)
                logsi.LogBitmapStream(SILevel.Warning, "LogBitmapStream Warning Example", binaryStream)
                logsi.LogBitmapStream(SILevel.Error, "LogBitmapStream Error Example", binaryStream)
                logsi.LogBitmapStream(SILevel.Fatal, "LogBitmapStream Fatal Example", binaryStream)

            # LogBool Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogBool Examples.")
            logsi.LogBool(None, "LogBool NoLevel Example", True)
            logsi.LogBool(SILevel.Debug, "LogBool Debug Example", True)
            logsi.LogBool(SILevel.Verbose, "LogBool Verbose Example", True)
            logsi.LogBool(SILevel.Message, "LogBool Message Example", True)
            logsi.LogBool(SILevel.Warning, "LogBool Warning Example", True)
            logsi.LogBool(SILevel.Error, "LogBool Error Example", True)
            logsi.LogBool(SILevel.Fatal, "LogBool Fatal Example", True)

            # LogByte Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogByte Examples.")
            logsi.LogByte(None, "LogByte NoLevel Example", 0xff)
            logsi.LogByte(SILevel.Debug, "LogByte Debug Example", 0xff)
            logsi.LogByte(SILevel.Verbose, "LogByte Verbose Example", 0xff)
            logsi.LogByte(SILevel.Message, "LogByte Message Example", 0xff)
            logsi.LogByte(SILevel.Warning, "LogByte Warning Example", 0xff)
            logsi.LogByte(SILevel.Error, "LogByte Error Example", 0xff)
            logsi.LogByte(SILevel.Fatal, "LogByte Fatal Example", 0xff)

            logsi.LogByte(None, "LogByte hex NoLevel Example", 0xff, True)
            logsi.LogByte(SILevel.Debug, "LogByte hex Debug Example", 0xff, True)
            logsi.LogByte(SILevel.Verbose, "LogByte hex Verbose Example", 0xff, True)
            logsi.LogByte(SILevel.Message, "LogByte hex Message Example", 0xff, True)
            logsi.LogByte(SILevel.Warning, "LogByte hex Warning Example", 0xff, True)
            logsi.LogByte(SILevel.Error, "LogByte hex Error Example", 0xff, True)
            logsi.LogByte(SILevel.Fatal, "LogByte hex Fatal Example", 0xff, True)

            # LogChar Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogChar Examples.")
            logsi.LogChar(None, "LogChar NoLevel string Example", 'A')
            logsi.LogChar(SILevel.Debug, "LogChar Debug string Example", 'A')
            logsi.LogChar(SILevel.Verbose, "LogChar Verbose string Example", 'A')
            logsi.LogChar(SILevel.Message, "LogChar Message string Example", 'A')
            logsi.LogChar(SILevel.Warning, "LogChar Warning string Example", 'A')
            logsi.LogChar(SILevel.Error, "LogChar Error string Example", 'A')
            logsi.LogChar(SILevel.Error, "LogChar Fatal string Example", 'A')

            # LogCollection Examples.
            oColl2 = ["Value2-1", "Value2-2", "Value2-3"]
            oColl = ["Value1-1", "Value1-2", "Value1-3", oColl2]
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogCollection Examples.")
            logsi.LogCollection(None, "LogCollection NoLevel Example", oColl)
            logsi.LogCollection(SILevel.Debug, "LogCollection Debug Example", oColl)
            logsi.LogCollection(SILevel.Verbose, "LogCollection Verbose Example", oColl)
            logsi.LogCollection(SILevel.Message, "LogCollection Message Example", oColl)
            logsi.LogCollection(SILevel.Warning, "LogCollection Warning Example", oColl)
            logsi.LogCollection(SILevel.Error, "LogCollection Error Example", oColl)
            logsi.LogCollection(SILevel.Fatal, "LogCollection Fatal Example", oColl)

            # LogColored Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogColored Examples.")
            logsi.LogColored(None, SIColors.Orange, "LogColored NoLevel Orange Example")
            logsi.LogColored(SILevel.Debug, SIColors.ForestGreen, "LogColored Debug ForestGreen Example")
            logsi.LogColored(SILevel.Verbose, SIColors.DimGray, "LogColored Verbose DimGray Example")
            logsi.LogColored(SILevel.Message, SIColors.AliceBlue, "LogColored Message AliceBlue Example")
            logsi.LogColored(SILevel.Warning, SIColors.Gold, "LogColored Warning Gold Example")
            logsi.LogColored(SILevel.Error, SIColors.Red, "LogColored Error Red Example")
            logsi.LogColored(SILevel.Fatal, SIColors.LightCoral, "LogColored Fatal LightCoral Example")

            # LogColored Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogColored (by value) Examples.")
            logsi.LogColored(None, 0x00FFA500, "LogColored (by value) NoLevel Orange (0x00FFA500) Example")
            logsi.LogColored(SILevel.Debug, SIColors.ForestGreen.value, "LogColored (by value) Debug ForestGreen Example")
            logsi.LogColored(SILevel.Verbose, SIColors.DimGray.value, "LogColored (by value) Verbose DimGray Example")
            logsi.LogColored(SILevel.Message, SIColors.AliceBlue.value, "LogColored (by value) Message AliceBlue Example")
            logsi.LogColored(SILevel.Warning, SIColors.Gold.value, "LogColored (by value) Warning Gold Example")
            logsi.LogColored(SILevel.Error, SIColors.Red.value, "LogColored (by value) Error Red Example")
            logsi.LogColored(SILevel.Fatal, 0x00F08080, "LogColored (by value) Fatal LightCoral (0x00F08080) Example")

            # LogComplex Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogComplex Examples.")
            logsi.LogComplex(None, "LogComplex NoLevel Example", complex(3,5))
            logsi.LogComplex(SILevel.Debug, "LogComplex Debug Example", complex(3,5))
            logsi.LogComplex(SILevel.Verbose, "LogComplex Verbose Example", complex(3,5))
            logsi.LogComplex(SILevel.Message, "LogComplex Message Example", complex(3,5))
            logsi.LogComplex(SILevel.Warning, "LogComplex Warning Example", complex(3,5))
            logsi.LogComplex(SILevel.Error, "LogComplex Error Example", complex(3,5))
            logsi.LogComplex(SILevel.Fatal, "LogComplex Fatal Example", complex(3,5))

            # LogConditional Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogConditional Examples.")
            logsi.LogConditional(None, True == True, "LogConditional NoLevel condition is TRUE Example")
            logsi.LogConditional(SILevel.Debug, True == True, "LogConditional Debug condition is TRUE Example")
            logsi.LogConditional(SILevel.Verbose, True == True, "LogConditional Verbose condition is TRUE Example")
            logsi.LogConditional(SILevel.Message, True == True, "LogConditional Message condition is TRUE Example")
            logsi.LogConditional(SILevel.Warning, True == True, "LogConditional Warning condition is TRUE Example")
            logsi.LogConditional(SILevel.Error, True == True, "LogConditional Error condition is TRUE Example")
            logsi.LogConditional(SILevel.Fatal, True == True, "LogConditional Fatal condition is TRUE Example")

            logsi.LogConditional(None, True == False, "LogConditional NoLevel condition is FALSE Example")
            logsi.LogConditional(SILevel.Debug, True == False, "LogConditional Debug condition is FALSE Example")
            logsi.LogConditional(SILevel.Verbose, True == False, "LogConditional Verbose condition is FALSE Example")
            logsi.LogConditional(SILevel.Message, True == False, "LogConditional Message condition is FALSE Example")
            logsi.LogConditional(SILevel.Warning, True == False, "LogConditional Warning condition is FALSE Example")
            logsi.LogConditional(SILevel.Error, True == False, "LogConditional Error condition is FALSE Example")
            logsi.LogConditional(SILevel.Fatal, True == False, "LogConditional Fatal condition is FALSE Example")

            # LogCurrentAppDomain Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogCurrentAppDomain Examples.")
            logsi.LogCurrentAppDomain(None, "LogCurrentAppDomain NoLevel Example")
            logsi.LogCurrentAppDomain(SILevel.Debug, "LogCurrentAppDomain Debug Example")
            logsi.LogCurrentAppDomain(SILevel.Verbose, "LogCurrentAppDomain Verbose Example")
            logsi.LogCurrentAppDomain(SILevel.Message, "LogCurrentAppDomain Message Example")
            logsi.LogCurrentAppDomain(SILevel.Warning, "LogCurrentAppDomain Warning Example")
            logsi.LogCurrentAppDomain(SILevel.Error, "LogCurrentAppDomain Error Example")
            logsi.LogCurrentAppDomain(SILevel.Fatal, "LogCurrentAppDomain Fatal Example")

            # LogCurrentStackTrace Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogCurrentStackTrace Examples.")
            logsi.LogCurrentStackTrace(None, "LogCurrentStackTrace NoLevel Example")
            logsi.LogCurrentStackTrace(SILevel.Debug, "LogCurrentStackTrace Debug Example")
            logsi.LogCurrentStackTrace(SILevel.Verbose, "LogCurrentStackTrace Verbose Example")
            logsi.LogCurrentStackTrace(SILevel.Message, "LogCurrentStackTrace Message Example")
            logsi.LogCurrentStackTrace(SILevel.Warning, "LogCurrentStackTrace Warning Example")
            logsi.LogCurrentStackTrace(SILevel.Error, "LogCurrentStackTrace Error Example")
            logsi.LogCurrentStackTrace(SILevel.Fatal, "LogCurrentStackTrace Fatal Example")

            logsi.LogCurrentStackTrace()
            logsi.LogCurrentStackTrace(SILevel.Debug)
            logsi.LogCurrentStackTrace(SILevel.Verbose)
            logsi.LogCurrentStackTrace(SILevel.Message)
            logsi.LogCurrentStackTrace(SILevel.Warning)
            logsi.LogCurrentStackTrace(SILevel.Error)
            logsi.LogCurrentStackTrace(SILevel.Fatal)

            # LogCurrentThread Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogCurrentThread Examples.")
            logsi.LogCurrentThread(None, "LogCurrentThread NoLevel Example")
            logsi.LogCurrentThread(SILevel.Debug, "LogCurrentThread Debug Example")
            logsi.LogCurrentThread(SILevel.Verbose, "LogCurrentThread Verbose Example")
            logsi.LogCurrentThread(SILevel.Message, "LogCurrentThread Message Example")
            logsi.LogCurrentThread(SILevel.Warning, "LogCurrentThread Warning Example")
            logsi.LogCurrentThread(SILevel.Error, "LogCurrentThread Error Example")
            logsi.LogCurrentThread(SILevel.Fatal, "LogCurrentThread Fatal Example")

            logsi.LogCurrentThread()
            logsi.LogCurrentThread(SILevel.Debug)
            logsi.LogCurrentThread(SILevel.Verbose)
            logsi.LogCurrentThread(SILevel.Message)
            logsi.LogCurrentThread(SILevel.Warning)
            logsi.LogCurrentThread(SILevel.Error)
            logsi.LogCurrentThread(SILevel.Fatal)

            # LogCustomContext Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogCustomContext Examples.")
            ctxtext:SITextContext = SITextContext(SIViewerId.Data)
            ctxtext.AppendLine("The title of this entry will appear in bold-faced font in the Si Console viewer.")
            ctxtext.AppendLine("This is Line 2 of text")
            ctxtext.AppendLine("This is the last line of text")
            logsi.LogCustomContext(None, "LogCustomContext NoLevel Comment ViewerId Example", SILogEntryType.Comment, ctxtext)
            logsi.LogCustomContext(SILevel.Debug, "LogCustomContext Debug Comment ViewerId Example", SILogEntryType.Comment, ctxtext)
            logsi.LogCustomContext(SILevel.Verbose, "LogCustomContext Verbose Comment ViewerId Example", SILogEntryType.Comment, ctxtext)
            logsi.LogCustomContext(SILevel.Message, "LogCustomContext Message Comment ViewerId Example", SILogEntryType.Comment, ctxtext)
            logsi.LogCustomContext(SILevel.Warning, "LogCustomContext Warning Comment ViewerId Example", SILogEntryType.Comment, ctxtext)
            logsi.LogCustomContext(SILevel.Error, "LogCustomContext Error Comment ViewerId Example", SILogEntryType.Comment, ctxtext)
            logsi.LogCustomContext(SILevel.Fatal, "LogCustomContext Fatal Comment ViewerId Example", SILogEntryType.Comment, ctxtext)

            ctxlistview:SIValueListViewerContext = SIValueListViewerContext()
            ctxlistview.AppendKeyValue("Usage", "12345")           # LStatus.dwMemoryLoad)
            ctxlistview.AppendKeyValue("Total physical", "12345")  # BytesAsString(LStatus.dwTotalPhys))
            ctxlistview.AppendKeyValue("Free physical", "12345")   # BytesAsString(LStatus.dwAvailPhys))
            ctxlistview.AppendKeyValue("Total pagefile", "12345")  # BytesAsString(LStatus.dwTotalPageFile))
            ctxlistview.AppendKeyValue("Free pagefile", "12345")   # BytesAsString(LStatus.dwAvailPageFile))
            ctxlistview.AppendKeyValue("Total virtual", "12345")   # BytesAsString(LStatus.dwTotalVirtual))
            ctxlistview.AppendKeyValue("Free virtual", "12345")    # BytesAsString(LStatus.dwAvailVirtual)) 
            logsi.LogCustomContext(None, "LogCustomContext NoLevel MemoryStatistic Example", SILogEntryType.MemoryStatistic, ctxlistview)
            logsi.LogCustomContext(SILevel.Debug, "LogCustomContext Debug MemoryStatistic Example", SILogEntryType.MemoryStatistic, ctxlistview)
            logsi.LogCustomContext(SILevel.Verbose, "LogCustomContext Verbose MemoryStatistic Example", SILogEntryType.MemoryStatistic, ctxlistview)
            logsi.LogCustomContext(SILevel.Message, "LogCustomContext Message MemoryStatistic Example", SILogEntryType.MemoryStatistic, ctxlistview)
            logsi.LogCustomContext(SILevel.Warning, "LogCustomContext Warning MemoryStatistic Example", SILogEntryType.MemoryStatistic, ctxlistview)
            logsi.LogCustomContext(SILevel.Error, "LogCustomContext Error MemoryStatistic Example", SILogEntryType.MemoryStatistic, ctxlistview)
            logsi.LogCustomContext(SILevel.Fatal, "LogCustomContext Fatal MemoryStatistic Example", SILogEntryType.MemoryStatistic, ctxlistview)

            # LogCustomFile Examples.
            testdataPath = testdataPfx + "TestSourceHTML.html"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogCustomFile Examples.")
            logsi.LogCustomFile(None, "LogCustomFile NoLevel Html Source Example", testdataPath, SILogEntryType.Source, SIViewerId.HtmlSource)
            logsi.LogCustomFile(SILevel.Debug, "LogCustomFile Debug Html Source Example", testdataPath, SILogEntryType.Source, SIViewerId.HtmlSource)
            logsi.LogCustomFile(SILevel.Verbose, "LogCustomFile Verbose Html Source Example", testdataPath, SILogEntryType.Source, SIViewerId.HtmlSource)
            logsi.LogCustomFile(SILevel.Message, "LogCustomFile Message Html Source Example", testdataPath, SILogEntryType.Source, SIViewerId.HtmlSource)
            logsi.LogCustomFile(SILevel.Warning, "LogCustomFile Warning Html Source Example", testdataPath, SILogEntryType.Source, SIViewerId.HtmlSource)
            logsi.LogCustomFile(SILevel.Error, "LogCustomFile Error Html Source Example", testdataPath, SILogEntryType.Source, SIViewerId.HtmlSource)
            logsi.LogCustomFile(SILevel.Fatal, "LogCustomFile Fatal Html Source Example", testdataPath, SILogEntryType.Source, SIViewerId.HtmlSource)

            # LogCustomReader Examples.
            testdataPath = testdataPfx + "TestSourceXML.xml"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogCustomReader Examples.")
            with open(testdataPath, 'r') as textReader:
                logsi.LogCustomReader(None, "LogCustomReader NoLevel Xml Source Example", textReader, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomReader(SILevel.Debug, "LogCustomReader Debug Xml Source Example", textReader, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomReader(SILevel.Verbose, "LogCustomReader Verbose Xml Source Example", textReader, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomReader(SILevel.Message, "LogCustomReader Message Xml Source Example", textReader, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomReader(SILevel.Warning, "LogCustomReader Warning Xml Source Example", textReader, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomReader(SILevel.Error, "LogCustomReader Error Xml Source Example", textReader, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomReader(SILevel.Fatal, "LogCustomReader Fatal Xml Source Example", textReader, SILogEntryType.Source, SIViewerId.XmlSource)

            # LogCustomStream Examples.
            testdataPath = testdataPfx + "TestSourceXML.xml"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogCustomStream Examples.")
            with open(testdataPath, 'rb') as binaryStream:
                logsi.LogCustomStream(None, "LogCustomStream NoLevel Xml Source Example", binaryStream, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomStream(SILevel.Debug, "LogCustomStream Debug Xml Source Example", binaryStream, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomStream(SILevel.Verbose, "LogCustomStream Verbose Xml Source Example", binaryStream, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomStream(SILevel.Message, "LogCustomStream Message Xml Source Example", binaryStream, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomStream(SILevel.Warning, "LogCustomStream Warning Xml Source Example", binaryStream, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomStream(SILevel.Error, "LogCustomStream Error Xml Source Example", binaryStream, SILogEntryType.Source, SIViewerId.XmlSource)
                logsi.LogCustomStream(SILevel.Fatal, "LogCustomStream Fatal Xml Source Example", binaryStream, SILogEntryType.Source, SIViewerId.XmlSource)

            with open(testdataPath, 'rb') as binaryStream:
                logsi.LogCustomStream(None, "LogCustomStream NoLevel Xml Binary Example", binaryStream, SILogEntryType.Source, SIViewerId.Binary)
                logsi.LogCustomStream(SILevel.Debug, "LogCustomStream Debug Xml Binary Example", binaryStream, SILogEntryType.Source, SIViewerId.Binary)
                logsi.LogCustomStream(SILevel.Verbose, "LogCustomStream Verbose Xml Binary Example", binaryStream, SILogEntryType.Source, SIViewerId.Binary)
                logsi.LogCustomStream(SILevel.Message, "LogCustomStream Message Xml Binary Example", binaryStream, SILogEntryType.Source, SIViewerId.Binary)
                logsi.LogCustomStream(SILevel.Warning, "LogCustomStream Warning Xml Binary Example", binaryStream, SILogEntryType.Source, SIViewerId.Binary)
                logsi.LogCustomStream(SILevel.Error, "LogCustomStream Error Xml Binary Example", binaryStream, SILogEntryType.Source, SIViewerId.Binary)
                logsi.LogCustomStream(SILevel.Fatal, "LogCustomStream Fatal Xml Binary Example", binaryStream, SILogEntryType.Source, SIViewerId.Binary)

            # LogCustomText Examples.
            testtext = "The title of this entry will appear in bold-faced font in the Si Console viewer.\nThis is some text to log.\nLine 3"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogCustomText Examples.")
            logsi.LogCustomText(None, "LogCustomText NoLevel Example", testtext, SILogEntryType.Comment, SIViewerId.Data)
            logsi.LogCustomText(SILevel.Debug, "LogCustomText Debug Example", testtext, SILogEntryType.Comment, SIViewerId.Data)
            logsi.LogCustomText(SILevel.Verbose, "LogCustomText Verbose Example", testtext, SILogEntryType.Comment, SIViewerId.Data)
            logsi.LogCustomText(SILevel.Message, "LogCustomText Message Example", testtext, SILogEntryType.Comment, SIViewerId.Data)
            logsi.LogCustomText(SILevel.Warning, "LogCustomText Warning Example", testtext, SILogEntryType.Comment, SIViewerId.Data)
            logsi.LogCustomText(SILevel.Error, "LogCustomText Error Example", testtext, SILogEntryType.Comment, SIViewerId.Data)
            logsi.LogCustomText(SILevel.Fatal, "LogCustomText Fatal Example", testtext, SILogEntryType.Comment, SIViewerId.Data)

            ## LogDataSet Examples.
            #dataTableCustomers:DataTable  = TestDBHelper.CreateDataTable(logsi, "Customers", testdataPfx + "TestDBDataTable_Customers.json")
            #DataTable dataTableArtists = TestDBHelper.CreateDataTable(logsi, "Albums", testdataPfx + "TestDBDataTable_Albums.json")
            #DataTable dataTableTracks = TestDBHelper.CreateDataTable(logsi, "Tracks", testdataPfx + "TestDBDataTable_Tracks.json")
            #DataSet datasetMusicStore = new DataSet("MusicStoreData")
            #datasetMusicStore.Tables.Add(dataTableArtists)
            #datasetMusicStore.Tables.Add(dataTableTracks)
            #datasetMusicStore.Tables.Add(dataTableCustomers)
            #logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDataSet Examples.")
            #logsi.LogDataSet(datasetMusicStore)
            #logsi.LogDataSet(SILevel.Debug, datasetMusicStore)
            #logsi.LogDataSet(SILevel.Verbose, datasetMusicStore)
            #logsi.LogDataSet(SILevel.Message, datasetMusicStore)
            #logsi.LogDataSet(SILevel.Warning, datasetMusicStore)
            #logsi.LogDataSet(SILevel.Error, datasetMusicStore)
            #logsi.LogDataSet(SILevel.Fatal, datasetMusicStore)

            ## LogDataTableSchema Examples.
            #logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDataSetSchema Examples.")
            #logsi.LogDataSetSchema(datasetMusicStore)
            #logsi.LogDataSetSchema(SILevel.Debug, datasetMusicStore)
            #logsi.LogDataSetSchema(SILevel.Verbose, datasetMusicStore)
            #logsi.LogDataSetSchema(SILevel.Message, datasetMusicStore)
            #logsi.LogDataSetSchema(SILevel.Warning, datasetMusicStore)
            #logsi.LogDataSetSchema(SILevel.Error, datasetMusicStore)
            #logsi.LogDataSetSchema(SILevel.Fatal, datasetMusicStore)

            ## LogDataTable Examples.
            #logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDataTable Examples.")
            #logsi.LogDataTable(None, "LogDataTable NoLevel Customers Table Example", dataTableCustomers)
            #logsi.LogDataTable(SILevel.Debug, "LogDataTable Debug Customers Table Example", dataTableCustomers)
            #logsi.LogDataTable(SILevel.Verbose, "LogDataTable Verbose Customers Table Example", dataTableCustomers)
            #logsi.LogDataTable(SILevel.Message, "LogDataTable Message Customers Table Example", dataTableCustomers)
            #logsi.LogDataTable(SILevel.Warning, "LogDataTable Warning Customers Table Example", dataTableCustomers)
            #logsi.LogDataTable(SILevel.Error, "LogDataTable Error Customers Table Example", dataTableCustomers)
            #logsi.LogDataTable(SILevel.Fatal, "LogDataTable Fatal Customers Table Example", dataTableCustomers)

            ## LogDataTableSchema Examples.
            #logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDataTableSchema Examples.")
            #logsi.LogDataTableSchema(None, "LogDataTableSchema NoLevel Tracks Table Example", dataTableTracks)
            #logsi.LogDataTableSchema(SILevel.Debug, "LogDataTableSchema Debug Tracks Table Example", dataTableTracks)
            #logsi.LogDataTableSchema(SILevel.Verbose, "LogDataTableSchema Verbose Tracks Table Example", dataTableTracks)
            #logsi.LogDataTableSchema(SILevel.Message, "LogDataTableSchema Message Tracks Table Example", dataTableTracks)
            #logsi.LogDataTableSchema(SILevel.Warning, "LogDataTableSchema Warning Tracks Table Example", dataTableTracks)
            #logsi.LogDataTableSchema(SILevel.Error, "LogDataTableSchema Error Tracks Table Example", dataTableTracks)
            #logsi.LogDataTableSchema(SILevel.Fatal, "LogDataTableSchema Fatal Tracks Table Example", dataTableTracks)

            ## LogDataView Examples.
            #logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDataView Examples.")
            #DataView dataviewCustomers = new DataView(dataTableCustomers, "Country = 'USA'", "LastName ASC, FirstName ASC", DataViewRowState.CurrentRows)
            #logsi.LogDataView(None, "LogDataView NoLevel Customers Country=USA Example", dataviewCustomers)
            #logsi.LogDataView(SILevel.Debug, "LogDataView Debug Customers Country=USA Example", dataviewCustomers)
            #logsi.LogDataView(SILevel.Verbose, "LogDataView Verbose Customers Country=USA Example", dataviewCustomers)
            #logsi.LogDataView(SILevel.Message, "LogDataView Message Customers Country=USA Example", dataviewCustomers)
            #logsi.LogDataView(SILevel.Warning, "LogDataView Warning Customers Country=USA Example", dataviewCustomers)
            #logsi.LogDataView(SILevel.Error, "LogDataView Error Customers Country=USA Example", dataviewCustomers)
            #logsi.LogDataView(SILevel.Fatal, "LogDataView Fatal Customers Country=USA Example", dataviewCustomers)

            # LogDateTime Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDateTime Examples.")
            logsi.LogDateTime(None, "LogDateTime NoLevel Example", testdate)
            logsi.LogDateTime(SILevel.Debug, "LogDateTime Debug Example", testdate)
            logsi.LogDateTime(SILevel.Verbose, "LogDateTime Verbose Example", testdate)
            logsi.LogDateTime(SILevel.Message, "LogDateTime Message Example", testdate)
            logsi.LogDateTime(SILevel.Warning, "LogDateTime Warning Example", testdate)
            logsi.LogDateTime(SILevel.Error, "LogDateTime Error Example", testdate)
            logsi.LogDateTime(SILevel.Fatal, "LogDateTime Fatal Example", testdate)

            # LogDecimal Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDecimal Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Python Si Client does not support this method.")

            # LogDictionary Examples.
            oDict2 = {}
            oDict2["D2Key1"] = "D2Key1 Value"
            oDict2["D2Key2"] = "D2Key2 Value"
            oDict = {}
            oDict["Key1"] = "Key1 Value"
            oDict["Key2"] = oDict2
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDictionary Examples.")
            logsi.LogDictionary(None, "LogDictionary NoLevel Example", oDict)
            logsi.LogDictionary(SILevel.Debug, "LogDictionary Debug Example", oDict)
            logsi.LogDictionary(SILevel.Verbose, "LogDictionary Verbose Example", oDict)
            logsi.LogDictionary(SILevel.Message, "LogDictionary Message Example", oDict)
            logsi.LogDictionary(SILevel.Warning, "LogDictionary Warning Example", oDict)
            logsi.LogDictionary(SILevel.Error, "LogDictionary Error Example", oDict)
            logsi.LogDictionary(SILevel.Fatal, "LogDictionary Fatal Example", oDict)
            logsi.LogDictionary(SILevel.Fatal, "LogDictionary Fatal Example (null object)", None)

            # LogDouble Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDouble Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Python Si Client does not support this method.")

            # LogEnumerable Examples.
            oEnumerable:list[str] = { "Value1-1", "Value1-2", "Value1-3" }
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogEnumerable Examples.")
            logsi.LogEnumerable(None, "LogEnumerable NoLevel Example", oEnumerable)
            logsi.LogEnumerable(SILevel.Debug, "LogEnumerable Debug Example", oEnumerable)
            logsi.LogEnumerable(SILevel.Verbose, "LogEnumerable Verbose Example", oEnumerable)
            logsi.LogEnumerable(SILevel.Message, "LogEnumerable Message Example", oEnumerable)
            logsi.LogEnumerable(SILevel.Warning, "LogEnumerable Warning Example", oEnumerable)
            logsi.LogEnumerable(SILevel.Error, "LogEnumerable Error Example", oEnumerable)
            logsi.LogEnumerable(SILevel.Fatal, "LogEnumerable Fatal Example", oEnumerable)
            logsi.LogEnumerable(SILevel.Fatal, "LogEnumerable Fatal Example (null object)", None)

            # LogException Examples.
            try:
            
                logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogException Examples (next 2 messages should be exception data, no messages if Level=Fatal).")
                raise Exception("This is a forced exception used to test the LogException method.")
                logsi.LogColored(SILevel.Fatal, SIColors.Red.value, "Py LogException Examples - You should not see this message, as an exception was forced in the previous line!")
            
            except Exception as ex:
            
                logsi.LogException("LogException - with Custom title, exception details in SI Console viewer area.", ex)
                logsi.LogException("LogException - with Custom title, exception details in SI Console viewer area. It will not be logged to the SystemLogger.", ex, logToSystemLogger=False)
                logsi.LogException(None, ex)           

            # LogFloat Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogFloat Examples.")
            logsi.LogFloat(None, "LogFloat NoLevel Example", float(10.123456789))
            logsi.LogFloat(SILevel.Debug, "LogFloat Debug Example", float(10.123456789))
            logsi.LogFloat(SILevel.Verbose, "LogFloat Verbose Example", float(10.123456789))
            logsi.LogFloat(SILevel.Message, "LogFloat Message Example", float(10.123456789))
            logsi.LogFloat(SILevel.Warning, "LogFloat Warning Example", float(10.123456789))
            logsi.LogFloat(SILevel.Error, "LogFloat Error Example", float(10.123456789))
            logsi.LogFloat(SILevel.Fatal, "LogFloat Fatal Example", float(10.123456789))

            # LogHtml Examples.
            testSourceHTML:str = "<!DOCTYPE html>\n<html lang=\"en\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>  \n  <meta charset=\"utf-8\" />\n  <title>HTML From Text</title>\n</head>\n<body>\n\n  <h1>HTML From Text</h1>\n  <h2>H2 Header</h2>\n  <h3>H1 Header</h3>\n  <a href=\"https://www.google.com\">This is a Google Link</a>\n\n</body>\n</html>"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogHtml Examples.")
            logsi.LogHtml(None, "LogHtml NoLevel Example", testSourceHTML)
            logsi.LogHtml(SILevel.Debug, "LogHtml Debug Example", testSourceHTML)
            logsi.LogHtml(SILevel.Verbose, "LogHtml Verbose Example", testSourceHTML)
            logsi.LogHtml(SILevel.Message, "LogHtml Message Example", testSourceHTML)
            logsi.LogHtml(SILevel.Warning, "LogHtml Warning Example", testSourceHTML)
            logsi.LogHtml(SILevel.Error, "LogHtml Error Example", testSourceHTML)
            logsi.LogHtml(SILevel.Fatal, "LogHtml Fatal Example", testSourceHTML)

            # LogHtmlFile Examples.
            testdataPath = testdataPfx + "TestSourceHTML.html"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogHtmlFile Examples.")
            logsi.LogHtmlFile(None, "LogHtmlFile NoLevel Example", testdataPath)
            logsi.LogHtmlFile(SILevel.Debug, "LogHtmlFile Debug Example", testdataPath)
            logsi.LogHtmlFile(SILevel.Verbose, "LogHtmlFile Verbose Example", testdataPath)
            logsi.LogHtmlFile(SILevel.Message, "LogHtmlFile Message Example", testdataPath)
            logsi.LogHtmlFile(SILevel.Warning, "LogHtmlFile Warning Example", testdataPath)
            logsi.LogHtmlFile(SILevel.Error, "LogHtmlFile Error Example", testdataPath)
            logsi.LogHtmlFile(SILevel.Fatal, "LogHtmlFile Fatal Example", testdataPath)

            # LogHtmlReader Examples.
            testdataPath = testdataPfx + "TestSourceHTML.html"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogHtmlReader Examples.")
            with open(testdataPath, 'r') as textReader:
                logsi.LogHtmlReader(None, "LogHtmlReader NoLevel Example", textReader)
                logsi.LogHtmlReader(SILevel.Debug, "LogHtmlReader Debug Example", textReader)
                logsi.LogHtmlReader(SILevel.Verbose, "LogHtmlReader Verbose Example", textReader)
                logsi.LogHtmlReader(SILevel.Message, "LogHtmlReader Message Example", textReader)
                logsi.LogHtmlReader(SILevel.Warning, "LogHtmlReader Warning Example", textReader)
                logsi.LogHtmlReader(SILevel.Error, "LogHtmlReader Error Example", textReader)
                logsi.LogHtmlReader(SILevel.Fatal, "LogHtmlReader Fatal Example", textReader)

            # LogHtmlStream Examples.
            testdataPath = testdataPfx + "TestSourceHTML.html"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogHtmlStream Examples.")
            with open(testdataPath, 'rb') as streamReader:
                logsi.LogHtmlStream(None, "LogHtmlStream NoLevel Example", streamReader)
                logsi.LogHtmlStream(SILevel.Debug, "LogHtmlStream Debug Example", streamReader)
                logsi.LogHtmlStream(SILevel.Verbose, "LogHtmlStream Verbose Example", streamReader)
                logsi.LogHtmlStream(SILevel.Message, "LogHtmlStream Message Example", streamReader)
                logsi.LogHtmlStream(SILevel.Warning, "LogHtmlStream Warning Example", streamReader)
                logsi.LogHtmlStream(SILevel.Error, "LogHtmlStream Error Example", streamReader)
                logsi.LogHtmlStream(SILevel.Fatal, "LogHtmlStream Fatal Example", streamReader)

            # LogIconFile Examples.
            testdataPath = testdataPfx + "TestICO.ico"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogIconFile Examples.")
            logsi.LogIconFile(None, "LogIconFile NoLevel Example", testdataPath)
            logsi.LogIconFile(SILevel.Debug, "LogIconFile Debug Example", testdataPath)
            logsi.LogIconFile(SILevel.Verbose, "LogIconFile Verbose Example", testdataPath)
            logsi.LogIconFile(SILevel.Message, "LogIconFile Message Example", testdataPath)
            logsi.LogIconFile(SILevel.Warning, "LogIconFile Warning Example", testdataPath)
            logsi.LogIconFile(SILevel.Error, "LogIconFile Error Example", testdataPath)
            logsi.LogIconFile(SILevel.Fatal, "LogIconFile Fatal Example", testdataPath)

            # LogIconStream Examples.
            testdataPath = testdataPfx + "TestICO.ico"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogIconStream Examples.")
            with open(testdataPath, 'rb') as binaryStream:
                logsi.LogIconStream(None, "LogIconStream NoLevel Example", binaryStream)
                logsi.LogIconStream(SILevel.Debug, "LogIconStream Debug Example", binaryStream)
                logsi.LogIconStream(SILevel.Verbose, "LogIconStream Verbose Example", binaryStream)
                logsi.LogIconStream(SILevel.Message, "LogIconStream Message Example", binaryStream)
                logsi.LogIconStream(SILevel.Warning, "LogIconStream Warning Example", binaryStream)
                logsi.LogIconStream(SILevel.Error, "LogIconStream Error Example", binaryStream)
                logsi.LogIconStream(SILevel.Fatal, "LogIconStream Fatal Example", binaryStream)

            # LogInt Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogInt Examples.")
            logsi.LogInt(None, "LogInt NoLevel Example", int(1234567890))
            logsi.LogInt(SILevel.Debug, "LogInt Debug Example", int(1234567890))
            logsi.LogInt(SILevel.Verbose, "LogInt Verbose Example", int(1234567890))
            logsi.LogInt(SILevel.Message, "LogInt Message Example", int(1234567890))
            logsi.LogInt(SILevel.Warning, "LogInt Warning Example", int(1234567890))
            logsi.LogInt(SILevel.Error, "LogInt Error Example", int(1234567890))
            logsi.LogInt(SILevel.Fatal, "LogInt Fatal Example", int(1234567890))

            logsi.LogInt(None, "LogInt NoLevel hex Example", int(1234567890), True)
            logsi.LogInt(SILevel.Debug, "LogInt Debug hex Example", int(1234567890), True)
            logsi.LogInt(SILevel.Verbose, "LogInt Verbose hex Example", int(1234567890), True)
            logsi.LogInt(SILevel.Message, "LogInt Message hex Example", int(1234567890), True)
            logsi.LogInt(SILevel.Warning, "LogInt Warning hex Example", int(1234567890), True)
            logsi.LogInt(SILevel.Error, "LogInt Error hex Example", int(1234567890), True)
            logsi.LogInt(SILevel.Fatal, "LogInt Fatal hex Example", int(1234567890), True)

            # LogJpegFile Examples.
            testdataPath = testdataPfx + "TestJPG.jpg"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogJpegFile Examples.")
            logsi.LogJpegFile(None, "LogJpegFile NoLevel Example", testdataPath)
            logsi.LogJpegFile(SILevel.Debug, "LogJpegFile Debug Example", testdataPath)
            logsi.LogJpegFile(SILevel.Verbose, "LogJpegFile Verbose Example", testdataPath)
            logsi.LogJpegFile(SILevel.Message, "LogJpegFile Message Example", testdataPath)
            logsi.LogJpegFile(SILevel.Warning, "LogJpegFile Warning Example", testdataPath)
            logsi.LogJpegFile(SILevel.Error, "LogJpegFile Error Example", testdataPath)
            logsi.LogJpegFile(SILevel.Fatal, "LogJpegFile Fatal Example", testdataPath)

            # LogJpegStream Examples.
            testdataPath = testdataPfx + "TestJPG.jpg"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogJpegStream Examples.")
            with open(testdataPath, 'rb') as binaryStream:
                logsi.LogJpegStream(None, "LogJpegStream NoLevel Example", binaryStream)
                logsi.LogJpegStream(SILevel.Debug, "LogJpegStream Debug Example", binaryStream)
                logsi.LogJpegStream(SILevel.Verbose, "LogJpegStream Verbose Example", binaryStream)
                logsi.LogJpegStream(SILevel.Message, "LogJpegStream Message Example", binaryStream)
                logsi.LogJpegStream(SILevel.Warning, "LogJpegStream Warning Example", binaryStream)
                logsi.LogJpegStream(SILevel.Error, "LogJpegStream Error Example", binaryStream)
                logsi.LogJpegStream(SILevel.Fatal, "LogJpegStream Fatal Example", binaryStream)

            # LogLong Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogLong Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Python Si Client does not support this method.")

            # Log Message Types Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogDebug, LogVerbose, LogMessage, LogWarning, LogError, LogFatal Examples.")
            logsi.LogDebug("This is a debug message.  It will not be displayed if Level=Verbose or above.")
            logsi.LogDebug("This is a debug message.  It will not be displayed if Level=Verbose or above. It will not be logged to the SystemLogger.", logToSystemLogger=False)
            logsi.LogDebug("This is a debug message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Verbose or above.", argsVar1, argsVar2)
            logsi.LogDebug("This is a debug message with *args: str1='%s', int2=%i and a 'colorValue=' of Gainsboro.  It will not be displayed if Level=Verbose or above.", argsVar1, argsVar2, colorValue=SIColors.Gainsboro)
            logsi.LogVerbose("This is a verbose message.  It will not be displayed if Level=Message or above.")
            logsi.LogVerbose("This is a verbose message.  It will not be displayed if Level=Message or above. It will not be logged to the SystemLogger.", logToSystemLogger=False)
            logsi.LogVerbose("This is a verbose message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Message or above.", argsVar1, argsVar2)
            logsi.LogVerbose("This is a verbose message with *args: str1='%s', int2=%i and a 'colorValue=' of Gainsboro.  It will not be displayed if Level=Message or above.", argsVar1, argsVar2, colorValue=SIColors.Gainsboro)
            logsi.LogMessage("This is a message.  It will not be displayed if Level=Warning or above.")
            logsi.LogMessage("This is a message.  It will not be displayed if Level=Warning or above. It will not be logged to the SystemLogger.", logToSystemLogger=False)
            logsi.LogMessage("This is a message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Warning or above.", argsVar1, argsVar2)
            logsi.LogMessage("This is a message with *args: str1='%s', int2=%i and a 'colorValue=' of Gainsboro.  It will not be displayed if Level=Warning or above.", argsVar1, argsVar2, colorValue=SIColors.Gainsboro)
            logsi.LogWarning("This is a warning message.  It will not be displayed if Level=Error or above.")
            logsi.LogWarning("This is a warning message.  It will not be displayed if Level=Error or above. It will not be logged to the SystemLogger.", logToSystemLogger=False)
            logsi.LogWarning("This is a warning message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Error or above.", argsVar1, argsVar2)
            logsi.LogWarning("This is a warning message with *args: str1='%s', int2=%i and a 'colorValue=' of Gainsboro.  It will not be displayed if Level=Error or above.", argsVar1, argsVar2, colorValue=SIColors.Gainsboro)
            logsi.LogError("This is a error message.  It will not be displayed if Level=Fatal or above.")
            logsi.LogError("This is a error message.  It will not be displayed if Level=Fatal or above. It will not be logged to the SystemLogger.", logToSystemLogger=False)
            logsi.LogError("This is a error message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Fatal or above.", argsVar1, argsVar2)
            logsi.LogError("This is a error message with *args: str1='%s', int2=%i and a 'colorValue=' of Gainsboro.  It will not be displayed if Level=Fatal or above.", argsVar1, argsVar2, colorValue=SIColors.Gainsboro)
            logsi.LogFatal("This is a fatal error message.")
            logsi.LogFatal("This is a fatal error message. It will not be logged to the SystemLogger.", logToSystemLogger=False)
            logsi.LogFatal("This is a fatal error message with *args: str1='%s', int2=%i.", argsVar1, argsVar2)
            logsi.LogFatal("This is a fatal error message with *args: str1='%s', int2=%i and a 'colorValue=' of Gainsboro.", argsVar1, argsVar2, colorValue=SIColors.Gainsboro)

            # LogMetafileFile Examples.
            testdataPath = testdataPfx + "TestMetaFile.wmf"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogMetafileFile Examples.")
            logsi.LogMetafileFile(None, "LogMetafileFile NoLevel Example", testdataPath)
            logsi.LogMetafileFile(SILevel.Debug, "LogMetafileFile Debug Example", testdataPath)
            logsi.LogMetafileFile(SILevel.Verbose, "LogMetafileFile Verbose Example", testdataPath)
            logsi.LogMetafileFile(SILevel.Message, "LogMetafileFile Message Example", testdataPath)
            logsi.LogMetafileFile(SILevel.Warning, "LogMetafileFile Warning Example", testdataPath)
            logsi.LogMetafileFile(SILevel.Error, "LogMetafileFile Error Example", testdataPath)
            logsi.LogMetafileFile(SILevel.Fatal, "LogMetafileFile Fatal Example", testdataPath)

            # LogMetafileStream Examples.
            testdataPath = testdataPfx + "TestMetaFile.wmf"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogMetafileStream Examples.")
            with open(testdataPath, 'rb') as binaryStream:
                logsi.LogMetafileStream(None, "LogMetafileStream NoLevel Example", binaryStream)
                logsi.LogMetafileStream(SILevel.Debug, "LogMetafileStream Debug Example", binaryStream)
                logsi.LogMetafileStream(SILevel.Verbose, "LogMetafileStream Verbose Example", binaryStream)
                logsi.LogMetafileStream(SILevel.Message, "LogMetafileStream Message Example", binaryStream)
                logsi.LogMetafileStream(SILevel.Warning, "LogMetafileStream Warning Example", binaryStream)
                logsi.LogMetafileStream(SILevel.Error, "LogMetafileStream Error Example", binaryStream)
                logsi.LogMetafileStream(SILevel.Fatal, "LogMetafileStream Fatal Example", binaryStream)

            # LogObject Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogObject Examples.")
            objGetMem:TestLogObjectHelper = TestLogObjectHelper()
            logsi.LogObject(None, "LogObject NoLevel Example", objGetMem)
            logsi.LogObject(SILevel.Debug, "LogObject Debug Example", objGetMem)
            logsi.LogObject(SILevel.Verbose, "LogObject Verbose Example", objGetMem)
            logsi.LogObject(SILevel.Message, "LogObject Message Example", objGetMem)
            logsi.LogObject(SILevel.Warning, "LogObject Warning Example", objGetMem)
            logsi.LogObject(SILevel.Error, "LogObject Error Example", objGetMem)
            logsi.LogObject(SILevel.Fatal, "LogObject Fatal Example", objGetMem)
            logsi.LogObject(SILevel.Fatal, "LogObject Fatal Example (null object)", None)

            logsi.LogObject(None, "LogObject NoLevel (excl non-public) Example", objGetMem, False)
            logsi.LogObject(SILevel.Debug, "LogObject Debug (excl non-public) Example", objGetMem, False)
            logsi.LogObject(SILevel.Verbose, "LogObject Verbose (excl non-public) Example", objGetMem, False)
            logsi.LogObject(SILevel.Message, "LogObject Message (excl non-public) Example", objGetMem, False)
            logsi.LogObject(SILevel.Warning, "LogObject Warning (excl non-public) Example", objGetMem, False)
            logsi.LogObject(SILevel.Error, "LogObject Error (excl non-public) Example", objGetMem, False)
            logsi.LogObject(SILevel.Fatal, "LogObject Fatal (excl non-public) Example", objGetMem, False)

            logsi.LogObject(None, "LogObject Nolevel (incl non-public) Example", objGetMem, True)
            logsi.LogObject(SILevel.Debug, "LogObject Debug (incl non-public) Example", objGetMem, True)
            logsi.LogObject(SILevel.Verbose, "LogObject Verbose (incl non-public) Example", objGetMem, True)
            logsi.LogObject(SILevel.Message, "LogObject Message (incl non-public) Example", objGetMem, True)
            logsi.LogObject(SILevel.Warning, "LogObject Warning (incl non-public) Example", objGetMem, True)
            logsi.LogObject(SILevel.Error, "LogObject Error (incl non-public) Example", objGetMem, True)
            logsi.LogObject(SILevel.Fatal, "LogObject Fatal (incl non-public) Example", objGetMem, True)

            # LogObjectValue Examples.
            testobject:bytes = bytes([0x00,0x01,0x02,0x03])
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogObjectValue Examples.")
            logsi.LogObjectValue(None, "LogObjectValue NoLevel Example", testobject)
            logsi.LogObjectValue(SILevel.Debug, "LogObjectValue Debug Example", testobject)
            logsi.LogObjectValue(SILevel.Verbose, "LogObjectValue Verbose Example", testobject)
            logsi.LogObjectValue(SILevel.Message, "LogObjectValue Message Example", testobject)
            logsi.LogObjectValue(SILevel.Warning, "LogObjectValue Warning Example", testobject)
            logsi.LogObjectValue(SILevel.Error, "LogObjectValue Error Example", testobject)
            logsi.LogObjectValue(SILevel.Fatal, "LogObjectValue Fatal Example", testobject)

            # LogPngFile Examples.
            testdataPath = testdataPfx + "TestPNG.png"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogPngFile Examples.")
            logsi.LogPngFile(None, "LogPngFile NoLevel Example", testdataPath)
            logsi.LogPngFile(SILevel.Debug, "LogPngFile Debug Example", testdataPath)
            logsi.LogPngFile(SILevel.Verbose, "LogPngFile Verbose Example", testdataPath)
            logsi.LogPngFile(SILevel.Message, "LogPngFile Message Example", testdataPath)
            logsi.LogPngFile(SILevel.Warning, "LogPngFile Warning Example", testdataPath)
            logsi.LogPngFile(SILevel.Error, "LogPngFile Error Example", testdataPath)
            logsi.LogPngFile(SILevel.Fatal, "LogPngFile Fatal Example", testdataPath)

            # LogPngStream Examples.
            testdataPath = testdataPfx + "TestPNG.png"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogPngStream Examples.")
            with open(testdataPath, 'rb') as binaryStream:
                logsi.LogPngStream(None, "LogPngStream NoLevel Example", binaryStream)
                logsi.LogPngStream(SILevel.Debug, "LogPngStream Debug Example", binaryStream)
                logsi.LogPngStream(SILevel.Verbose, "LogPngStream Verbose Example", binaryStream)
                logsi.LogPngStream(SILevel.Message, "LogPngStream Message Example", binaryStream)
                logsi.LogPngStream(SILevel.Warning, "LogPngStream Warning Example", binaryStream)
                logsi.LogPngStream(SILevel.Error, "LogPngStream Error Example", binaryStream)
                logsi.LogPngStream(SILevel.Fatal, "LogPngStream Fatal Example", binaryStream)

            # LogReader Examples.
            testdataPath = testdataPfx + "TestSourceXML.xml"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogReader Examples.")
            with open(testdataPath, 'r') as textReader:
                logsi.LogReader(None, "LogReader NoLevel Example", textReader)
                logsi.LogReader(SILevel.Debug, "LogReader Debug Example", textReader)
                logsi.LogReader(SILevel.Verbose, "LogReader Verbose Example", textReader)
                logsi.LogReader(SILevel.Message, "LogReader Message Example", textReader)
                logsi.LogReader(SILevel.Warning, "LogReader Warning Example", textReader)
                logsi.LogReader(SILevel.Error, "LogReader Error Example", textReader)
                logsi.LogReader(SILevel.Fatal, "LogReader Fatal Example", textReader)

            # LogSeparator Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogSeparator Examples.")
            logsi.LogSeparator()
            logsi.LogSeparator(SILevel.Debug)
            logsi.LogSeparator(SILevel.Verbose)
            logsi.LogSeparator(SILevel.Message)
            logsi.LogSeparator(SILevel.Warning)
            logsi.LogSeparator(SILevel.Error)
            logsi.LogSeparator(SILevel.Fatal)

            # LogShort Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogShort Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Python Si Client does not support this method.")

            # LogSource Xml Examples.
            testdataPath = testdataPfx + "TestSourceXML.xml"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogSource Examples.")
            logsi.LogSource(None, "LogSource NoLevel Example", testSourceHTML, SISourceId.Xml)
            logsi.LogSource(SILevel.Debug, "LogSource Debug Example", testSourceHTML, SISourceId.Xml)
            logsi.LogSource(SILevel.Verbose, "LogSource Verbose Example", testSourceHTML, SISourceId.Xml)
            logsi.LogSource(SILevel.Message, "LogSource Message Example", testSourceHTML, SISourceId.Xml)
            logsi.LogSource(SILevel.Warning, "LogSource Warning Example", testSourceHTML, SISourceId.Xml)
            logsi.LogSource(SILevel.Error, "LogSource Error Example", testSourceHTML, SISourceId.Xml)
            logsi.LogSource(SILevel.Fatal, "LogSource Fatal Example", testSourceHTML, SISourceId.Xml)

            # LogSourceFile Html Examples.
            testdataPath = testdataPfx + "TestSourceHTML.Html"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogSourceFile Examples.")
            logsi.LogSourceFile(None, "LogSourceFile NoLevel Html Example", testdataPath, SISourceId.Html)
            logsi.LogSourceFile(SILevel.Debug, "LogSourceFile Debug Html Example", testdataPath, SISourceId.Html)
            logsi.LogSourceFile(SILevel.Verbose, "LogSourceFile Verbose Html Example", testdataPath, SISourceId.Html)
            logsi.LogSourceFile(SILevel.Message, "LogSourceFile Message Html Example", testdataPath, SISourceId.Html)
            logsi.LogSourceFile(SILevel.Warning, "LogSourceFile Warning Html Example", testdataPath, SISourceId.Html)
            logsi.LogSourceFile(SILevel.Error, "LogSourceFile Error Html Example", testdataPath, SISourceId.Html)
            logsi.LogSourceFile(SILevel.Fatal, "LogSourceFile Fatal Html Example", testdataPath, SISourceId.Html)

            # LogSourceFile INI Examples.
            testdataPath = testdataPfx + "TestSourceINI.ini"
            logsi.LogSourceFile(None, "LogSourceFile NoLevel INI Example", testdataPath, SISourceId.Ini)
            logsi.LogSourceFile(SILevel.Debug, "LogSourceFile Debug INI Example", testdataPath, SISourceId.Ini)
            logsi.LogSourceFile(SILevel.Verbose, "LogSourceFile Verbose INI Example", testdataPath, SISourceId.Ini)
            logsi.LogSourceFile(SILevel.Message, "LogSourceFile Message INI Example", testdataPath, SISourceId.Ini)
            logsi.LogSourceFile(SILevel.Warning, "LogSourceFile Warning INI Example", testdataPath, SISourceId.Ini)
            logsi.LogSourceFile(SILevel.Error, "LogSourceFile Error INI Example", testdataPath, SISourceId.Ini)
            logsi.LogSourceFile(SILevel.Fatal, "LogSourceFile Fatal INI Example", testdataPath, SISourceId.Ini)

            # LogSourceFile JavaScript Examples.
            testdataPath = testdataPfx + "TestSourceJavaScript.js"
            logsi.LogSourceFile(None, "LogSourceFile NoLevel JavaScript Example", testdataPath, SISourceId.JavaScript)
            logsi.LogSourceFile(SILevel.Debug, "LogSourceFile Debug JavaScript Example", testdataPath, SISourceId.JavaScript)
            logsi.LogSourceFile(SILevel.Verbose, "LogSourceFile Verbose JavaScript Example", testdataPath, SISourceId.JavaScript)
            logsi.LogSourceFile(SILevel.Message, "LogSourceFile Message JavaScript Example", testdataPath, SISourceId.JavaScript)
            logsi.LogSourceFile(SILevel.Warning, "LogSourceFile Warning JavaScript Example", testdataPath, SISourceId.JavaScript)
            logsi.LogSourceFile(SILevel.Error, "LogSourceFile Error JavaScript Example", testdataPath, SISourceId.JavaScript)
            logsi.LogSourceFile(SILevel.Fatal, "LogSourceFile Fatal JavaScript Example", testdataPath, SISourceId.JavaScript)

            # LogSourceFile Perl Examples.
            testdataPath = testdataPfx + "TestSourcePerl.pl"
            logsi.LogSourceFile(None, "LogSourceFile NoLevel Perl Example", testdataPath, SISourceId.Perl)
            logsi.LogSourceFile(SILevel.Debug, "LogSourceFile Debug Perl Example", testdataPath, SISourceId.Perl)
            logsi.LogSourceFile(SILevel.Verbose, "LogSourceFile Verbose Perl Example", testdataPath, SISourceId.Perl)
            logsi.LogSourceFile(SILevel.Message, "LogSourceFile Message Perl Example", testdataPath, SISourceId.Perl)
            logsi.LogSourceFile(SILevel.Warning, "LogSourceFile Warning Perl Example", testdataPath, SISourceId.Perl)
            logsi.LogSourceFile(SILevel.Error, "LogSourceFile Error Perl Example", testdataPath, SISourceId.Perl)
            logsi.LogSourceFile(SILevel.Fatal, "LogSourceFile Fatal Perl Example", testdataPath, SISourceId.Perl)

            # LogSourceFile Python Examples.
            testdataPath = testdataPfx + "TestSourcePython.py"
            logsi.LogSourceFile(None, "LogSourceFile NoLevel Python Example", testdataPath, SISourceId.Python)
            logsi.LogSourceFile(SILevel.Debug, "LogSourceFile Debug Python Example", testdataPath, SISourceId.Python)
            logsi.LogSourceFile(SILevel.Verbose, "LogSourceFile Verbose Python Example", testdataPath, SISourceId.Python)
            logsi.LogSourceFile(SILevel.Message, "LogSourceFile Message Python Example", testdataPath, SISourceId.Python)
            logsi.LogSourceFile(SILevel.Warning, "LogSourceFile Warning Python Example", testdataPath, SISourceId.Python)
            logsi.LogSourceFile(SILevel.Error, "LogSourceFile Error Python Example", testdataPath, SISourceId.Python)
            logsi.LogSourceFile(SILevel.Fatal, "LogSourceFile Fatal Python Example", testdataPath, SISourceId.Python)

            # LogSourceFile Xml Examples.
            testdataPath = testdataPfx + "TestSourceXML.xml"
            logsi.LogSourceFile(None, "LogSourceFile NoLevel Xml Example", testdataPath, SISourceId.Xml)
            logsi.LogSourceFile(SILevel.Debug, "LogSourceFile Debug Xml Example", testdataPath, SISourceId.Xml)
            logsi.LogSourceFile(SILevel.Verbose, "LogSourceFile Verbose Xml Example", testdataPath, SISourceId.Xml)
            logsi.LogSourceFile(SILevel.Message, "LogSourceFile Message Xml Example", testdataPath, SISourceId.Xml)
            logsi.LogSourceFile(SILevel.Warning, "LogSourceFile Warning Xml Example", testdataPath, SISourceId.Xml)
            logsi.LogSourceFile(SILevel.Error, "LogSourceFile Error Xml Example", testdataPath, SISourceId.Xml)
            logsi.LogSourceFile(SILevel.Fatal, "LogSourceFile Fatal Xml Example", testdataPath, SISourceId.Xml)

            # LogSourceReader Examples.
            testdataPath = testdataPfx + "TestSourceXML.xml"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogSourceReader Examples.")
            with open(testdataPath, 'r') as textReader:
                logsi.LogSourceReader(None, "LogSourceReader NoLevel Xml Example", textReader, SISourceId.Xml)
                logsi.LogSourceReader(SILevel.Debug, "LogSourceReader Debug Xml Example", textReader, SISourceId.Xml)
                logsi.LogSourceReader(SILevel.Verbose, "LogSourceReader Verbose Xml Example", textReader, SISourceId.Xml)
                logsi.LogSourceReader(SILevel.Message, "LogSourceReader Message Xml Example", textReader, SISourceId.Xml)
                logsi.LogSourceReader(SILevel.Warning, "LogSourceReader Warning Xml Example", textReader, SISourceId.Xml)
                logsi.LogSourceReader(SILevel.Error, "LogSourceReader Error Xml Example", textReader, SISourceId.Xml)
                logsi.LogSourceReader(SILevel.Fatal, "LogSourceReader Fatal Xml Example", textReader, SISourceId.Xml)

            # LogSourceStream Examples.
            testdataPath = testdataPfx + "TestSourceXML.xml"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogSourceStream Examples.")
            with open(testdataPath, 'rb') as streamReader:
                logsi.LogSourceStream(None, "LogSourceStream NoLevel Xml Example", streamReader, SISourceId.Xml)
                logsi.LogSourceStream(SILevel.Debug, "LogSourceStream Debug Xml Example", streamReader, SISourceId.Xml)
                logsi.LogSourceStream(SILevel.Verbose, "LogSourceStream Verbose Xml Example", streamReader, SISourceId.Xml)
                logsi.LogSourceStream(SILevel.Message, "LogSourceStream Message Xml Example", streamReader, SISourceId.Xml)
                logsi.LogSourceStream(SILevel.Warning, "LogSourceStream Warning Xml Example", streamReader, SISourceId.Xml)
                logsi.LogSourceStream(SILevel.Error, "LogSourceStream Error Xml Example", streamReader, SISourceId.Xml)
                logsi.LogSourceStream(SILevel.Fatal, "LogSourceStream Fatal Xml Example", streamReader, SISourceId.Xml)

            # LogSql Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogSql Examples.")
            logsi.LogSql(None, "LogSql NoLevel Example", "SELECT *\n FROM UsersTable\n WHERE LastName LIKE \"Smart%\"\n ORDER BY LastName ASC, FirstName ASC")
            logsi.LogSql(SILevel.Debug, "LogSql Debug Example", "SELECT *\n FROM UsersTable\n WHERE LastName LIKE \"Smart%\"\n ORDER BY LastName ASC, FirstName ASC")
            logsi.LogSql(SILevel.Verbose, "LogSql Verbose Example", "SELECT *\n FROM UsersTable\n WHERE LastName LIKE \"Smart%\"\n ORDER BY LastName ASC, FirstName ASC")
            logsi.LogSql(SILevel.Message, "LogSql Message Example", "SELECT *\n FROM UsersTable\n WHERE LastName LIKE \"Smart%\"\n ORDER BY LastName ASC, FirstName ASC")
            logsi.LogSql(SILevel.Warning, "LogSql Warning Example", "SELECT *\n FROM UsersTable\n WHERE LastName LIKE \"Smart%\"\n ORDER BY LastName ASC, FirstName ASC")
            logsi.LogSql(SILevel.Error, "LogSql Error Example", "SELECT *\n FROM UsersTable\n WHERE LastName LIKE \"Smart%\"\n ORDER BY LastName ASC, FirstName ASC")
            logsi.LogSql(SILevel.Fatal, "LogSql Fatal Example", "SELECT *\n FROM UsersTable\n WHERE LastName LIKE \"Smart%\"\n ORDER BY LastName ASC, FirstName ASC")

            # LogStackTrace Examples.
            strace:list[FrameInfo] = inspect.stack()
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogStackTrace Examples.")
            logsi.LogStackTrace(None, "LogStackTrace NoLevel Example", strace)
            logsi.LogStackTrace(SILevel.Debug, "LogStackTrace Debug Example", strace)
            logsi.LogStackTrace(SILevel.Verbose, "LogStackTrace Verbose Example", strace)
            logsi.LogStackTrace(SILevel.Message, "LogStackTrace Message Example", strace)
            logsi.LogStackTrace(SILevel.Warning, "LogStackTrace Warning Example", strace)
            logsi.LogStackTrace(SILevel.Error, "LogStackTrace Error Example", strace)
            logsi.LogStackTrace(SILevel.Fatal, "LogStackTrace Fatal Example", strace)

            logsi.LogStackTrace(None, "LogStackTrace NoLevel (frames 0-4) Example", strace, 0, 5)
            logsi.LogStackTrace(SILevel.Debug, "LogStackTrace Debug (frames 0-4) Example", strace, 0, 5)
            logsi.LogStackTrace(SILevel.Verbose, "LogStackTrace Verbose (frames 0-4) Example", strace, 0, 5)
            logsi.LogStackTrace(SILevel.Message, "LogStackTrace Message (frames 0-4) Example", strace, 0, 5)
            logsi.LogStackTrace(SILevel.Warning, "LogStackTrace Warning (frames 0-4) Example", strace, 0, 5)
            logsi.LogStackTrace(SILevel.Error, "LogStackTrace Error (frames 0-4) Example", strace, 0, 5)
            logsi.LogStackTrace(SILevel.Fatal, "LogStackTrace Fatal (frames 0-4) Example", strace, 0, 5)

            logsi.LogStackTrace("", strace)
            logsi.LogStackTrace(SILevel.Debug, "", strace)
            logsi.LogStackTrace(SILevel.Verbose, "", strace)
            logsi.LogStackTrace(SILevel.Message, "", strace)
            logsi.LogStackTrace(SILevel.Warning, "", strace)
            logsi.LogStackTrace(SILevel.Error, "", strace)
            logsi.LogStackTrace(SILevel.Fatal, "", strace)

            # LogStream Examples.
            testdataPath = testdataPfx + "TestSourceXML.xml"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogStream Examples.")
            with open(testdataPath, 'rb') as binaryStream:
                logsi.LogStream(None, "LogStream NoLevel Xml Example", binaryStream)
                logsi.LogStream(SILevel.Debug, "LogStream Debug Xml Example", binaryStream)
                logsi.LogStream(SILevel.Verbose, "LogStream Verbose Xml Example", binaryStream)
                logsi.LogStream(SILevel.Message, "LogStream Message Xml Example", binaryStream)
                logsi.LogStream(SILevel.Warning, "LogStream Warning Xml Example", binaryStream)
                logsi.LogStream(SILevel.Error, "LogStream Error Xml Example", binaryStream)
                logsi.LogStream(SILevel.Fatal, "LogStream Fatal Xml Example", binaryStream)

            # LogString Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogString Examples.")
            logsi.LogString(None, "LogString Nolevel string Example", "This is a string value")
            logsi.LogString(SILevel.Debug, "LogString Debug string Example", "This is a string value")
            logsi.LogString(SILevel.Verbose, "LogString Verbose string Example", "This is a string value")
            logsi.LogString(SILevel.Message, "LogString Message string Example", "This is a string value")
            logsi.LogString(SILevel.Warning, "LogString Warning string Example", "This is a string value")
            logsi.LogString(SILevel.Error, "LogString Error string Example", "This is a string value")
            logsi.LogString(SILevel.Fatal, "LogString Fatal string Example", "This is a string value")

            # LogStringBuilder Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogStringBuilder Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Python Si Client does not support this method.")

            # LogSystem Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogSystem Examples.")
            logsi.LogSystem(None, "LogSystem Example NoLevel")
            logsi.LogSystem(SILevel.Debug, "LogSystem Debug Example")
            logsi.LogSystem(SILevel.Verbose, "LogSystem Verbose Example")
            logsi.LogSystem(SILevel.Message, "LogSystem Message Example")
            logsi.LogSystem(SILevel.Warning, "LogSystem Warning Example")
            logsi.LogSystem(SILevel.Error, "LogSystem Error Example")
            logsi.LogSystem(SILevel.Fatal, "LogSystem Fatal Example")

            logsi.LogSystem(None)
            logsi.LogSystem(SILevel.Debug)
            logsi.LogSystem(SILevel.Verbose)
            logsi.LogSystem(SILevel.Message)
            logsi.LogSystem(SILevel.Warning)
            logsi.LogSystem(SILevel.Error)
            logsi.LogSystem(SILevel.Fatal)

            # LogText Examples.
            testdataPath = "This is the actual text to log.\nLine 2\r\nLine 3"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogText Examples.")
            logsi.LogText(None, "LogText NoLevel Example", testdataPath)
            logsi.LogText(SILevel.Debug, "LogText Debug Example", testdataPath)
            logsi.LogText(SILevel.Verbose, "LogText Verbose Example", testdataPath)
            logsi.LogText(SILevel.Message, "LogText Message Example", testdataPath)
            logsi.LogText(SILevel.Warning, "LogText Warning Example", testdataPath)
            logsi.LogText(SILevel.Error, "LogText Error Example", testdataPath)
            logsi.LogText(SILevel.Fatal, "LogText Fatal Example", testdataPath)

            # LogTextFile Examples.
            testdataPath = testdataPfx + "TestConfigurationSettings.txt"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogTextFile Examples.")
            logsi.LogTextFile(None, "LogTextFile NoLevel Example", testdataPath)
            logsi.LogTextFile(SILevel.Debug, "LogTextFile Debug Example", testdataPath)
            logsi.LogTextFile(SILevel.Verbose, "LogTextFile Verbose Example", testdataPath)
            logsi.LogTextFile(SILevel.Message, "LogTextFile Message Example", testdataPath)
            logsi.LogTextFile(SILevel.Warning, "LogTextFile Warning Example", testdataPath)
            logsi.LogTextFile(SILevel.Error, "LogTextFile Error Example", testdataPath)
            logsi.LogTextFile(SILevel.Fatal, "LogTextFile Fatal Example", testdataPath)

            # LogTextReader Examples.
            testdataPath = testdataPfx + "TestSourceHTML.html"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogTextReader Examples.")
            with open(testdataPath, 'r') as textReader:
                logsi.LogTextReader(None, "LogTextReader NoLevel Example", textReader)
                logsi.LogTextReader(SILevel.Debug, "LogTextReader Debug Example", textReader)
                logsi.LogTextReader(SILevel.Verbose, "LogTextReader Verbose Example", textReader)
                logsi.LogTextReader(SILevel.Message, "LogTextReader Message Example", textReader)
                logsi.LogTextReader(SILevel.Warning, "LogTextReader Warning Example", textReader)
                logsi.LogTextReader(SILevel.Error, "LogTextReader Error Example", textReader)
                logsi.LogTextReader(SILevel.Fatal, "LogTextReader Fatal Example", textReader)

            # LogTextStream Examples.
            testdataPath = testdataPfx + "TestSourceHTML.html"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogTextStream Examples.")
            with open(testdataPath, 'rb') as streamReader:
                logsi.LogTextStream(None, "LogTextStream NoLevel Example", streamReader)
                logsi.LogTextStream(SILevel.Debug, "LogTextStream Debug Example", streamReader)
                logsi.LogTextStream(SILevel.Verbose, "LogTextStream Verbose Example", streamReader)
                logsi.LogTextStream(SILevel.Message, "LogTextStream Message Example", streamReader)
                logsi.LogTextStream(SILevel.Warning, "LogTextStream Warning Example", streamReader)
                logsi.LogTextStream(SILevel.Error, "LogTextStream Error Example", streamReader)
                logsi.LogTextStream(SILevel.Fatal, "LogTextStream Fatal Example", streamReader)

            # LogThread Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogThread Examples (using threading.currentThread()).")
            logsi.LogThread(None, "LogThread NoLevel Example", threading.currentThread())
            logsi.LogThread(SILevel.Debug, "LogThread Debug Example", threading.currentThread())
            logsi.LogThread(SILevel.Verbose, "LogThread Verbose Example", threading.currentThread())
            logsi.LogThread(SILevel.Message, "LogThread Message Example", threading.currentThread())
            logsi.LogThread(SILevel.Warning, "LogThread Warning Example", threading.currentThread())
            logsi.LogThread(SILevel.Error, "LogThread Error Example", threading.currentThread())
            logsi.LogThread(SILevel.Fatal, "LogThread Fatal Example", threading.currentThread())
            logsi.LogThread(SILevel.Fatal, "LogThread Fatal Example (null object)", None)

            logsi.LogThread(thread=threading.currentThread())
            logsi.LogThread(SILevel.Debug, thread=threading.currentThread())
            logsi.LogThread(SILevel.Verbose, thread=threading.currentThread())
            logsi.LogThread(SILevel.Message, thread=threading.currentThread())
            logsi.LogThread(SILevel.Warning, thread=threading.currentThread())
            logsi.LogThread(SILevel.Error, thread=threading.currentThread())
            logsi.LogThread(SILevel.Fatal, thread=threading.currentThread())

            # LogValue Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py LogValue Examples.")
            logsi.LogValue(None, "LogValue NoLevel bool Example", True)
            logsi.LogValue(SILevel.Debug, "LogValue Debug bool Example", True)
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose bool Example", True)
            logsi.LogValue(SILevel.Message, "LogValue Message bool Example", True)
            logsi.LogValue(SILevel.Warning, "LogValue Warning bool Example", True)
            logsi.LogValue(SILevel.Error, "LogValue Error bool Example", True)
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal bool Example", True)

            logsi.LogValue(None, "LogValue NoLevel byte Example", b'\xff')
            logsi.LogValue(SILevel.Debug, "LogValue Debug byte Example", b'\xff')
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose byte Example", b'\xff')
            logsi.LogValue(SILevel.Message, "LogValue Message byte Example", b'\xff')
            logsi.LogValue(SILevel.Warning, "LogValue Warning byte Example", b'\xff')
            logsi.LogValue(SILevel.Error, "LogValue Error byte Example", b'\xff')
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal byte Example", b'\xff')

            logsi.LogValue(None, "LogValue NoLevel char Example", 'A')
            logsi.LogValue(SILevel.Debug, "LogValue Debug char Example", 'A')
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose char Example", 'A')
            logsi.LogValue(SILevel.Message, "LogValue Message char Example", 'A')
            logsi.LogValue(SILevel.Warning, "LogValue Warning char Example", 'A')
            logsi.LogValue(SILevel.Error, "LogValue Error char Example", 'A')
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal char Example", 'A')

            logsi.LogValue(None, "LogValue NoLevel complex Example", complex(3,5))
            logsi.LogValue(SILevel.Debug, "LogValue Debug complex Example", complex(3,5))
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose complex Example", complex(3,5))
            logsi.LogValue(SILevel.Message, "LogValue Message complex Example", complex(3,5))
            logsi.LogValue(SILevel.Warning, "LogValue Warning complex Example", complex(3,5))
            logsi.LogValue(SILevel.Error, "LogValue Error complex Example", complex(3,5))
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal complex Example", complex(3,5))

            logsi.LogValue(None, "LogValue NoLevel DateTime Example", testdate)
            logsi.LogValue(SILevel.Debug, "LogValue Debug DateTime Example", testdate)
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose DateTime Example", testdate)
            logsi.LogValue(SILevel.Message, "LogValue Message DateTime Example", testdate)
            logsi.LogValue(SILevel.Warning, "LogValue Warning DateTime Example", testdate)
            logsi.LogValue(SILevel.Error, "LogValue Error DateTime Example", testdate)
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal DateTime Example", testdate)

            logsi.LogValue(None, "LogValue NoLevel float Example", float(10.123456789))
            logsi.LogValue(SILevel.Debug, "LogValue Debug float Example", float(10.123456789))
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose float Example", float(10.123456789))
            logsi.LogValue(SILevel.Message, "LogValue Message float Example", float(10.123456789))
            logsi.LogValue(SILevel.Warning, "LogValue Warning float Example", float(10.123456789))
            logsi.LogValue(SILevel.Error, "LogValue Error float Example", float(10.123456789))
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal float Example", float(10.123456789))

            logsi.LogValue(None, "LogValue NoLevel int Example", int(1234567890))
            logsi.LogValue(SILevel.Debug, "LogValue Debug int Example", int(1234567890))
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose int Example", int(1234567890))
            logsi.LogValue(SILevel.Message, "LogValue Message int Example", int(1234567890))
            logsi.LogValue(SILevel.Warning, "LogValue Warning int Example", int(1234567890))
            logsi.LogValue(SILevel.Error, "LogValue Error int Example", int(1234567890))
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal int Example", int(1234567890))

            logsi.LogValue(None, "LogValue NoLevel object Example", testobject)
            logsi.LogValue(SILevel.Debug, "LogValue Debug object Example", testobject)
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose object Example", testobject)
            logsi.LogValue(SILevel.Message, "LogValue Message object Example", testobject)
            logsi.LogValue(SILevel.Warning, "LogValue Warning object Example", testobject)
            logsi.LogValue(SILevel.Error, "LogValue Error object Example", testobject)
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal object Example", testobject)

            logsi.LogValue(None, "LogValue NoLevel string Example", "This is a string value")
            logsi.LogValue(SILevel.Debug, "LogValue Debug string Example", "This is a string value")
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose string Example", "This is a string value")
            logsi.LogValue(SILevel.Message, "LogValue Message string Example", "This is a string value")
            logsi.LogValue(SILevel.Warning, "LogValue Warning string Example", "This is a string value")
            logsi.LogValue(SILevel.Error, "LogValue Error string Example", "This is a string value")
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal string Example", "This is a string value")

            logsi.LogValue(None, "LogValue NoLevel null Example", None)
            logsi.LogValue(SILevel.Debug, "LogValue Debug null Example", None)
            logsi.LogValue(SILevel.Verbose, "LogValue Verbose null Example", None)
            logsi.LogValue(SILevel.Message, "LogValue Message null Example", None)
            logsi.LogValue(SILevel.Warning, "LogValue Warning null Example", None)
            logsi.LogValue(SILevel.Error, "LogValue Error null Example", None)
            logsi.LogValue(SILevel.Fatal, "LogValue Fatal null Example", None)

            # ResetColor Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SISession.ResetColor Examples.")
            logsi.ColorBG = SIColor(SIColors.LightCoral)
            logsi.LogDebug(str.format("This is a debug message in color {0}.  It will not be displayed if Level=Verbose or above.", logsi.ColorBG.ValueHex))
            logsi.LogVerbose(str.format("This is a verbose messge in color {0}.  It will not be displayed if Level=Message or above.", logsi.ColorBG.ValueHex))
            logsi.LogMessage(str.format("This is a message in color {0}.  It will not be displayed if Level=Warning or above.", logsi.ColorBG.ValueHex))
            logsi.LogWarning(str.format("This is a warning message in color {0}.  It will not be displayed if Level=Error or above.", logsi.ColorBG.ValueHex))
            logsi.LogError(str.format("This is a error message in color {0}.  It will not be displayed if Level=Fatal or above.", logsi.ColorBG.ValueHex))
            logsi.LogFatal(str.format("This is a fatal message error in color {0}.", logsi.ColorBG.ValueHex))
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Resetting background color to default.")
            logsi.ResetColor()  # reset color back to default.
            logsi.LogDebug(str.format("This is a debug message in color {0}.  It will not be displayed if Level=Verbose or above.", logsi.ColorBG.ValueHex))
            logsi.LogVerbose(str.format("This is a verbose message in color {0}.  It will not be displayed if Level=Message or above.", logsi.ColorBG.ValueHex))
            logsi.LogMessage(str.format("This is a message in color {0}.  It will not be displayed if Level=Warning or above.", logsi.ColorBG.ValueHex))
            logsi.LogWarning(str.format("This is a warning message in color {0}.  It will not be displayed if Level=Error or above.", logsi.ColorBG.ValueHex))
            logsi.LogError(str.format("This is a error message in color {0}.  It will not be displayed if Level=Fatal or above.", logsi.ColorBG.ValueHex))
            logsi.LogFatal(str.format("This is a fatal message error in color {0}.", logsi.ColorBG.ValueHex))

            # SendCustomControlCommand Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SendCustomControlCommand Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Clearing all AutoViews in the SI Console viewer.")
            logsi.SendCustomControlCommand(None, SIControlCommandType.ClearAutoViews, None)
            logsi.SendCustomControlCommand(SILevel.Debug, SIControlCommandType.ClearAutoViews, None)
            logsi.SendCustomControlCommand(SILevel.Verbose, SIControlCommandType.ClearAutoViews, None)
            logsi.SendCustomControlCommand(SILevel.Message, SIControlCommandType.ClearAutoViews, None)
            logsi.SendCustomControlCommand(SILevel.Warning, SIControlCommandType.ClearAutoViews, None)
            logsi.SendCustomControlCommand(SILevel.Error, SIControlCommandType.ClearAutoViews, None)
            logsi.SendCustomControlCommand(SILevel.Fatal, SIControlCommandType.ClearAutoViews, None)

            # SendCustomLogEntry Examples.
            testdataPath = testdataPfx + "TestBMP.bmp"
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SendCustomLogEntry Examples.")
            with open(testdataPath, 'rb') as binaryStream:
                logsi.SendCustomLogEntry(None, "SendCustomLogEntry Nolevel Bitmap Graphic Example", SILogEntryType.Graphic, SIViewerId.Bitmap, None, binaryStream)
                logsi.SendCustomLogEntry(SILevel.Debug, "SendCustomLogEntry Debug Bitmap Graphic Example", SILogEntryType.Graphic, SIViewerId.Bitmap, None, binaryStream)
                logsi.SendCustomLogEntry(SILevel.Verbose, "SendCustomLogEntry Verbose Bitmap Graphic Example", SILogEntryType.Graphic, SIViewerId.Bitmap, None, binaryStream)
                logsi.SendCustomLogEntry(SILevel.Message, "SendCustomLogEntry Message Bitmap Graphic Example", SILogEntryType.Graphic, SIViewerId.Bitmap, None, binaryStream)
                logsi.SendCustomLogEntry(SILevel.Warning, "SendCustomLogEntry Warning Bitmap Graphic Example", SILogEntryType.Graphic, SIViewerId.Bitmap, None, binaryStream)
                logsi.SendCustomLogEntry(SILevel.Error, "SendCustomLogEntry Error Bitmap Graphic Example", SILogEntryType.Graphic, SIViewerId.Bitmap, None, binaryStream)
                logsi.SendCustomLogEntry(SILevel.Fatal, "SendCustomLogEntry Fatal Bitmap Graphic Example", SILogEntryType.Graphic, SIViewerId.Bitmap, None, binaryStream)

            # SendCustomProcessFlow Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SendCustomProcessFlow Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Adding a 'SendCustomProcessFlow Level Thread' to the Process Flow toolbox in the SI Console viewer.")
            logsi.SendCustomProcessFlow(None, "SendCustomProcessFlow NoLevel Thread", SIProcessFlowType.EnterThread)
            logsi.SendCustomProcessFlow(SILevel.Debug, "SendCustomProcessFlow NoLevel Thread", SIProcessFlowType.EnterThread)
            logsi.SendCustomProcessFlow(SILevel.Verbose, "SendCustomProcessFlow Verbose Thread", SIProcessFlowType.EnterThread)
            logsi.SendCustomProcessFlow(SILevel.Message, "SendCustomProcessFlow Message Thread", SIProcessFlowType.EnterThread)
            logsi.SendCustomProcessFlow(SILevel.Warning, "SendCustomProcessFlow Warning Thread", SIProcessFlowType.EnterThread)
            logsi.SendCustomProcessFlow(SILevel.Error, "SendCustomProcessFlow Error Thread", SIProcessFlowType.EnterThread)
            logsi.SendCustomProcessFlow(SILevel.Fatal, "SendCustomProcessFlow Fatal Thread", SIProcessFlowType.EnterThread)

            logsi.SendCustomProcessFlow(None, "SendCustomProcessFlow NoLevel Thread", SIProcessFlowType.LeaveThread)
            logsi.SendCustomProcessFlow(SILevel.Debug, "SendCustomProcessFlow NoLevel Thread", SIProcessFlowType.LeaveThread)
            logsi.SendCustomProcessFlow(SILevel.Verbose, "SendCustomProcessFlow Verbose Thread", SIProcessFlowType.LeaveThread)
            logsi.SendCustomProcessFlow(SILevel.Message, "SendCustomProcessFlow Message Thread", SIProcessFlowType.LeaveThread)
            logsi.SendCustomProcessFlow(SILevel.Warning, "SendCustomProcessFlow Warning Thread", SIProcessFlowType.LeaveThread)
            logsi.SendCustomProcessFlow(SILevel.Error, "SendCustomProcessFlow Error Thread", SIProcessFlowType.LeaveThread)
            logsi.SendCustomProcessFlow(SILevel.Fatal, "SendCustomProcessFlow Fatal Thread", SIProcessFlowType.LeaveThread)

            # SendCustomWatch Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py SendCustomWatch Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Adding a 'PySendCustomWatch Level' to the Watches panel in the SI Console viewer.")
            logsi.SendCustomWatch(None, "PySendCustomWatch NoLevel", "Custom Watch Value", SIWatchType.String)
            logsi.SendCustomWatch(SILevel.Debug, "PySendCustomWatch Debug", "Custom Watch Value", SIWatchType.String)
            logsi.SendCustomWatch(SILevel.Verbose, "PySendCustomWatch Verbose", "Custom Watch Value", SIWatchType.String)
            logsi.SendCustomWatch(SILevel.Message, "PySendCustomWatch Message", "Custom Watch Value", SIWatchType.String)
            logsi.SendCustomWatch(SILevel.Warning, "PySendCustomWatch Warning", "Custom Watch Value", SIWatchType.String)
            logsi.SendCustomWatch(SILevel.Error, "PySendCustomWatch Error", "Custom Watch Value", SIWatchType.String)
            logsi.SendCustomWatch(SILevel.Fatal, "PySendCustomWatch Fatal", "Custom Watch Value", SIWatchType.String)

            # Watch Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py Watch Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatch(bool) values are located in the Watches panel of the SI Console.")
            logsi.Watch(None, "PyWatch(bool) NoLevel", True)
            logsi.Watch(SILevel.Debug, "PyWatch(bool) Debug", True)
            logsi.Watch(SILevel.Verbose, "PyWatch(bool) Verbose", True)
            logsi.Watch(SILevel.Message, "PyWatch(bool) Message", True)
            logsi.Watch(SILevel.Warning, "PyWatch(bool) Warning", True)
            logsi.Watch(SILevel.Error, "PyWatch(bool) Error", True)
            logsi.Watch(SILevel.Fatal, "PyWatch(bool) Fatal", True)

            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatch(byte) values are located in the Watches panel of the SI Console.")
            logsi.Watch(None, "PyWatch(byte) NoLevel", b'\xff')
            logsi.Watch(SILevel.Debug, "PyWatch(byte) Debug", b'\xff')
            logsi.Watch(SILevel.Verbose, "PyWatch(byte) Verbose", b'\xff')
            logsi.Watch(SILevel.Message, "PyWatch(byte) Message", b'\xff')
            logsi.Watch(SILevel.Warning, "PyWatch(byte) Warning", b'\xff')
            logsi.Watch(SILevel.Error, "PyWatch(byte) Error", b'\xff')
            logsi.Watch(SILevel.Fatal, "PyWatch(byte) Fatal", b'\xff')

            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatch(char) values are located in the Watches panel of the SI Console.")
            logsi.Watch(None, "PyWatch(char) NoLevel", 'A')
            logsi.Watch(SILevel.Debug, "PyWatch(char) Debug", 'A')
            logsi.Watch(SILevel.Verbose, "PyWatch(char) Verbose", 'A')
            logsi.Watch(SILevel.Message, "PyWatch(char) Message", 'A')
            logsi.Watch(SILevel.Warning, "PyWatch(char) Warning", 'A')
            logsi.Watch(SILevel.Error, "PyWatch(char) Error", 'A')
            logsi.Watch(SILevel.Fatal, "PyWatch(char) Fatal", 'A')

            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatch(complex) values are located in the Watches panel of the SI Console.")
            logsi.Watch(None, "PyWatch(complex) NoLevel", complex(3,5))
            logsi.Watch(SILevel.Debug, "PyWatch(complex) Debug", complex(3,5))
            logsi.Watch(SILevel.Verbose, "PyWatch(complex) Verbose", complex(3,5))
            logsi.Watch(SILevel.Message, "PyWatch(complex) Message", complex(3,5))
            logsi.Watch(SILevel.Warning, "PyWatch(complex) Warning", complex(3,5))
            logsi.Watch(SILevel.Error, "PyWatch(complex) Error", complex(3,5))
            logsi.Watch(SILevel.Fatal, "PyWatch(complex) Fatal", complex(3,5))

            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatch(datetime) values are located in the Watches panel of the SI Console.")
            logsi.Watch(None, "PyWatch(datetime) NoLevel", testdate)
            logsi.Watch(SILevel.Debug, "PyWatch(datetime) Debug", testdate)
            logsi.Watch(SILevel.Verbose, "PyWatch(datetime) Verbose", testdate)
            logsi.Watch(SILevel.Message, "PyWatch(datetime) Message", testdate)
            logsi.Watch(SILevel.Warning, "PyWatch(datetime) Warning", testdate)
            logsi.Watch(SILevel.Error, "PyWatch(datetime) Error", testdate)
            logsi.Watch(SILevel.Fatal, "PyWatch(datetime) Fatal", testdate)

            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatch(float) values are located in the Watches panel of the SI Console.")
            logsi.Watch(None, "PyWatch(float) NoLevel", float(10.123456789))
            logsi.Watch(SILevel.Debug, "PyWatch(float) Debug", float(10.123456789))
            logsi.Watch(SILevel.Verbose, "PyWatch(float) Verbose", float(10.123456789))
            logsi.Watch(SILevel.Message, "PyWatch(float) Message", float(10.123456789))
            logsi.Watch(SILevel.Warning, "PyWatch(float) Warning", float(10.123456789))
            logsi.Watch(SILevel.Error, "PyWatch(float) Error", float(10.123456789))
            logsi.Watch(SILevel.Fatal, "PyWatch(float) Fatal", float(10.123456789))

            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatch(int) values are located in the Watches panel of the SI Console.")
            logsi.Watch(None, "PyWatch(int) NoLevel", int(1234567890))
            logsi.Watch(SILevel.Debug, "PyWatch(int) Debug", int(1234567890))
            logsi.Watch(SILevel.Verbose, "PyWatch(int) Verbose", int(1234567890))
            logsi.Watch(SILevel.Message, "PyWatch(int) Message", int(1234567890))
            logsi.Watch(SILevel.Warning, "PyWatch(int) Warning", int(1234567890))
            logsi.Watch(SILevel.Error, "PyWatch(int) Error", int(1234567890))
            logsi.Watch(SILevel.Fatal, "PyWatch(int) Fatal", int(1234567890))

            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatch(string) values are located in the Watches panel of the SI Console.")
            logsi.Watch(None, "PyWatch(string) NoLevel", "Py Watch String Example")
            logsi.Watch(SILevel.Debug, "PyWatch(string) Debug", "Py Watch String Example")
            logsi.Watch(SILevel.Verbose, "PyWatch(string) Verbose", "Py Watch String Example")
            logsi.Watch(SILevel.Message, "PyWatch(string) Message", "Py Watch String Example")
            logsi.Watch(SILevel.Warning, "PyWatch(string) Warning", "Py Watch String Example")
            logsi.Watch(SILevel.Error, "PyWatch(string) Error", "Py Watch String Example")
            logsi.Watch(SILevel.Fatal, "PyWatch(string) Fatal", "Py Watch String Example")

            # WatchBool Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchBool Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatchBool values are located in the Watches panel of the SI Console.")
            logsi.WatchBool(None, "PyWatchBool NoLevel", True)
            logsi.WatchBool(SILevel.Debug, "PyWatchBool Debug", True)
            logsi.WatchBool(SILevel.Verbose, "PyWatchBool Verbose", True)
            logsi.WatchBool(SILevel.Message, "PyWatchBool Message", True)
            logsi.WatchBool(SILevel.Warning, "PyWatchBool Warning", True)
            logsi.WatchBool(SILevel.Error, "PyWatchBool Error", True)
            logsi.WatchBool(SILevel.Fatal, "PyWatchBool Fatal", True)

            # WatchByte Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchByte Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatchByte values are located in the Watches panel of the SI Console.")
            logsi.WatchByte(None, "PyWatchByte NoLevel", 0xff)
            logsi.WatchByte(SILevel.Debug, "PyWatchByte Debug", 0xff)
            logsi.WatchByte(SILevel.Verbose, "PyWatchByte Verbose", 0xff)
            logsi.WatchByte(SILevel.Message, "PyWatchByte Message", 0xff)
            logsi.WatchByte(SILevel.Warning, "PyWatchByte Warning", 0xff)
            logsi.WatchByte(SILevel.Error, "PyWatchByte Error", 0xff)
            logsi.WatchByte(SILevel.Fatal, "PyWatchByte Fatal", 0xff)

            logsi.WatchByte(None, "PyWatchByte(hex) NoLevel", 0xff, True)
            logsi.WatchByte(SILevel.Debug, "PyWatchByte(hex) Debug", 0xff, True)
            logsi.WatchByte(SILevel.Verbose, "PyWatchByte(hex) Verbose", 0xff, True)
            logsi.WatchByte(SILevel.Message, "PyWatchByte(hex) Message", 0xff, True)
            logsi.WatchByte(SILevel.Warning, "PyWatchByte(hex) Warning", 0xff, True)
            logsi.WatchByte(SILevel.Error, "PyWatchByte(hex) Error", 0xff, True)
            logsi.WatchByte(SILevel.Fatal, "PyWatchByte(hex) Fatal", 0xff, True)

            # WatchChar Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchChar Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatchChar values are located in the Watches panel of the SI Console.")
            logsi.WatchChar(None, "PyWatchChar NoLevel", 'A')
            logsi.WatchChar(SILevel.Debug, "PyWatchChar Debug", 'A')
            logsi.WatchChar(SILevel.Verbose, "PyWatchChar Verbose", 'A')
            logsi.WatchChar(SILevel.Message, "PyWatchChar Message", 'A')
            logsi.WatchChar(SILevel.Warning, "PyWatchChar Warning", 'A')
            logsi.WatchChar(SILevel.Error, "PyWatchChar Error", 'A')
            logsi.WatchChar(SILevel.Fatal, "PyWatchChar Fatal", 'A')

            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchComplex Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatchComplex values are located in the Watches panel of the SI Console.")
            logsi.WatchComplex(None, "PyWatchComplex NoLevel", complex(3,5))
            logsi.WatchComplex(SILevel.Debug, "PyWatchComplex Debug", complex(3,5))
            logsi.WatchComplex(SILevel.Verbose, "PyWatchComplex Verbose", complex(3,5))
            logsi.WatchComplex(SILevel.Message, "PyWatchComplex Message", complex(3,5))
            logsi.WatchComplex(SILevel.Warning, "PyWatchComplex Warning", complex(3,5))
            logsi.WatchComplex(SILevel.Error, "PyWatchComplex Error", complex(3,5))
            logsi.WatchComplex(SILevel.Fatal, "PyWatchComplex Fatal", complex(3,5))

            # WatchDateTime Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchDateTime Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatchDateTime values are located in the Watches panel of the SI Console.")
            logsi.WatchDateTime(None, "PyWatchDateTime NoLevel", testdate)
            logsi.WatchDateTime(SILevel.Debug, "PyWatchDateTime Debug", testdate)
            logsi.WatchDateTime(SILevel.Verbose, "PyWatchDateTime Verbose", testdate)
            logsi.WatchDateTime(SILevel.Message, "PyWatchDateTime Message", testdate)
            logsi.WatchDateTime(SILevel.Warning, "PyWatchDateTime Warning", testdate)
            logsi.WatchDateTime(SILevel.Error, "PyWatchDateTime Error", testdate)
            logsi.WatchDateTime(SILevel.Fatal, "PyWatchDateTime Fatal", testdate)

            # WatchDecimal Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchDecimal Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Python Si Client does not support this method.")

            # WatchDouble Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchDouble Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Python Si Client does not support this method.")

            # WatchFloat Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchFloat Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatchFloat values are located in the Watches panel of the SI Console.")
            logsi.WatchFloat(None, "PyWatchFloat NoLevel", float(10.123456789))
            logsi.WatchFloat(SILevel.Debug, "PyWatchFloat Debug", float(10.123456789))
            logsi.WatchFloat(SILevel.Verbose, "PyWatchFloat Verbose", float(10.123456789))
            logsi.WatchFloat(SILevel.Message, "PyWatchFloat Message", float(10.123456789))
            logsi.WatchFloat(SILevel.Warning, "PyWatchFloat Warning", float(10.123456789))
            logsi.WatchFloat(SILevel.Error, "PyWatchFloat Error", float(10.123456789))
            logsi.WatchFloat(SILevel.Fatal, "PyWatchFloat Fatal", float(10.123456789))

            # WatchInt Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchInt Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatchInt values are located in the Watches panel of the SI Console.")
            logsi.WatchInt(None, "PyWatchInt NoLevel", int(1234567890))
            logsi.WatchInt(SILevel.Debug, "PyWatchInt Debug", int(1234567890))
            logsi.WatchInt(SILevel.Verbose, "PyWatchInt Verbose", int(1234567890))
            logsi.WatchInt(SILevel.Message, "PyWatchInt Message", int(1234567890))
            logsi.WatchInt(SILevel.Warning, "PyWatchInt Warning", int(1234567890))
            logsi.WatchInt(SILevel.Error, "PyWatchInt Error", int(1234567890))
            logsi.WatchInt(SILevel.Fatal, "PyWatchInt Fatal", int(1234567890))

            logsi.WatchInt(None, "PyWatchInt(hex) NoLevel", int(1234567890), True)
            logsi.WatchInt(SILevel.Debug, "PyWatchInt(hex) Debug", int(1234567890), True)
            logsi.WatchInt(SILevel.Verbose, "PyWatchInt(hex) Verbose", int(1234567890), True)
            logsi.WatchInt(SILevel.Message, "PyWatchInt(hex) Message", int(1234567890), True)
            logsi.WatchInt(SILevel.Warning, "PyWatchInt(hex) Warning", int(1234567890), True)
            logsi.WatchInt(SILevel.Error, "PyWatchInt(hex) Error", int(1234567890), True)
            logsi.WatchInt(SILevel.Fatal, "PyWatchInt(hex) Fatal", int(1234567890), True)

            # WatchLong Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchLong Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Python Si Client does not support this method.")

            # WatchShort Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchShort Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Python Si Client does not support this method.")

            # WatchString Examples.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py WatchString Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "PyWatchString values are located in the Watches panel of the SI Console.")
            logsi.WatchString(None, "PyWatchString NoLevel", "Py Watch String Example")
            logsi.WatchString(SILevel.Debug, "PyWatchString Debug", "Py Watch String Example")
            logsi.WatchString(SILevel.Verbose, "PyWatchString Verbose", "Py Watch String Example")
            logsi.WatchString(SILevel.Message, "PyWatchString Message", "Py Watch String Example")
            logsi.WatchString(SILevel.Warning, "PyWatchString Warning", "Py Watch String Example")
            logsi.WatchString(SILevel.Error, "PyWatchString Error", "Py Watch String Example")
            logsi.WatchString(SILevel.Fatal, "PyWatchString Fatal", "Py Watch String Example")

            # log message in all known color values.
            logsi.LogColored(SILevel.Fatal, SIColors.LightSkyBlue, "Py Coloring Examples.")
            logsi.LogColored(SILevel.Fatal, SIColors.White, "All Python Log methods support a colorValue property.  The following are the known color values, or you can supply your own color values.")
            for item in SIColors:
                logsi.LogColored(logsi.Parent.Level, item.value, "This is a message in color '{0}' ({1}).".format(item.name, hex(item.value).upper().replace("0X","0x")))
            oColor:SIColor = SIColor.FromRgb(255,0,0)
            logsi.LogColored(logsi.Parent.Level, oColor.Value, "This is a message in a custom color '{0}'.".format(oColor.ValueHex))

            # tests completed.
            logsi.LogColored(SILevel.Fatal, SIColors.White, "Test ALL SISession Methods Completed")

        except Exception as ex:

            logsi.LogException("Unhandled exception!  This should NEVER happen, since it would cause an exception to be thrown in the code that is being debugged!", ex)

        finally:

            pass

        print("TestSessionMethods ended.")



    # TestAllMethods method message count values for each log level type.
    TestMessageMethods_LogEntryCounts = {}
    TestMessageMethods_LogEntryCounts[str(SILevel.Debug.name)] = 5
    TestMessageMethods_LogEntryCounts[str(SILevel.Verbose.name)] = 5
    TestMessageMethods_LogEntryCounts[str(SILevel.Message.name)] = 5
    TestMessageMethods_LogEntryCounts[str(SILevel.Warning.name)] = 5
    TestMessageMethods_LogEntryCounts[str(SILevel.Error.name)] = 5
    TestMessageMethods_LogEntryCounts[str(SILevel.Fatal.name)] = 5

    @staticmethod
    def TestMessageMethods(logsi:SISession) -> None:
        """
        Tests all SISession methods (LogEntry, Watch, ControlCommand, ProcessFlow).

        Args:
            logsi (SISession):
                SmartInspect session object.
        """

        print("TestSessionMethods starting.")

        # log the following with SILevel.Fatal so it is always logged.
        logsi.LogSeparator(SILevel.Fatal)
        logsi.LogText(SILevel.Fatal, "Test ALL SISession Methods Starting", "")
        logsi.LogValue(SILevel.Fatal, "SI Parent Level", logsi.Parent.Level)
        logsi.LogValue(SILevel.Fatal, "SI Session Level", logsi.Level)

        try:

            logsi.EnterMethod()
            
            # log messages.
            logsi.EnterMethod(None,"LogMessageTypes")
            logsi.LogDebug("This is a debug message.  It will not be displayed if Level=Verbose or above.")
            logsi.LogVerbose("This is a verbose message.  It will not be displayed if Level=Message or above.")
            logsi.LogMessage("This is a message.  It will not be displayed if Level=Warning or above.")
            logsi.LogWarning("This is a warning message.  It will not be displayed if Level=Error or above.")
            logsi.LogWarning("This is a warning message in GOLD.  It will not be displayed if Level=Error or above.", SIColors.Gold)
            logsi.LogError("This is a error message in RED.  It will not be displayed if Level=Fatal or above.", SIColors.Red)
            logsi.LogFatal("This is a fatal error message in RED.", SIColors.Red)
            logsi.LeaveMethod(None,"LogMessageTypes")

        except Exception as ex:

            logsi.LogException("Unhandled exception!  This should NEVER happen, since it would cause an exception to be thrown in the code that is being debugged!", ex)

        finally:

            logsi.LeaveMethod()

        print("TestSessionMethods ended.")
