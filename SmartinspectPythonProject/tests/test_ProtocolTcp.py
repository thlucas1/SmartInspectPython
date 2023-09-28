# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

# our package imports.
from smartinspectpython.siauto import *

# import classes used for test scenarios.
from testClassDefinitions import SIEventHandlerClass
from testSessionMethods import TestSessionMethods

print("Test Script Starting.")

# test getmethod from module base (not in a class).
#methodName:str = SISession.GetMethodName(0,True)
#methodName:str = SISession.GetMethodName(1,True)

# wire up smartinspect events.
SIEventHandlerClass.WireEvents(SIAuto.Si)

# set smartinspect connections, and enable logging.
#SIAuto.Si.Connections = "tcp(host=win10vm.netlucas.com,port=4228,timeout=30000,reconnect=true,reconnect.interval=10s,async.enabled=false)"  # Test Async Mode
SIAuto.Si.Connections = "tcp(host=192.168.1.1,port=4228,timeout=30000,reconnect=true,reconnect.interval=10s,async.enabled=false)"  # Test Async Mode
SIAuto.Si.Enabled = True

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main

for level in SILevel:

    if (level == SILevel.Control):
        continue

    # reset counters for next test.
    SIEventHandlerClass.ResetCounters(_logsi.Parent)

    # write packet events to console.
    #SIEventHandlerClass.WriteEventPacketsToConsole = True

    # test all session methods, using specified logging level.
    # note that we will just change the Parent.Level value for this.
    # the Parent.Default and SISession.Level are set to Debug, in the
    # event that configuration file contains other values.  this
    # makes for a 1-to-1 comparison between level test runs.
    _logsi.Parent.Level = level
    _logsi.Parent.DefaultLevel = SILevel.Debug
    _logsi.Level = SILevel.Debug
    TestSessionMethods.TestAllMethods(_logsi)

    # log counters to SI console.
    _logsi.Watch(SILevel.Fatal, "Total Packets LogEntry", SIEventHandlerClass.LogEntryCount)
    _logsi.Watch(SILevel.Fatal, "Total Packets ProcessFlow", SIEventHandlerClass.ProcessFlowCount)
    _logsi.Watch(SILevel.Fatal, "Total Packets ControlCmd", SIEventHandlerClass.ControlCommandCount)
    _logsi.Watch(SILevel.Fatal, "Total Packets Watch", SIEventHandlerClass.WatchCount)
    _logsi.Watch(SILevel.Fatal, "Total Packets Filtered", SIEventHandlerClass.FilterCount)
    _logsi.Watch(SILevel.Fatal, "Total Error", SIEventHandlerClass.ErrorCount)
    _logsi.Watch(SILevel.Fatal, "Total Info", SIEventHandlerClass.InfoCount)

    # print SI event counts.
    SIEventHandlerClass.PrintResults(_logsi.Parent)

    # verify log entry counts. fail test if count does not match expected value for the specified level.
    SIEventHandlerClass.VerifyLogEntryCounts(_logsi, level, TestSessionMethods.TestAllMethods_LogEntryCounts)
    SIEventHandlerClass.VerifyErrorCount(_logsi, level)

    print("Test was Successful!")

print("ALL Level Tests were Successful!")

# unwire events, and dispose of SmartInspect.
SIEventHandlerClass.UnWireEvents(SIAuto.Si)
SIAuto.Si.Dispose()

print("Test Script Ended.")
