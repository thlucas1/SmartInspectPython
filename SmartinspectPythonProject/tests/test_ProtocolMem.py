# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

# our package imports.
from smartinspectpython.siauto import *

# import classes used for test scenarios.
from testClassDefinitions import SIEventHandlerClass
from testSessionMethods import TestSessionMethods

print("Test Script Starting.\n")

# wire up smartinspect events.
SIEventHandlerClass.WireEvents(SIAuto.Si)

# set smartinspect connections, and enable logging.
SIAuto.Si.Connections = "mem(astext=true, indent=true)"
#SIAuto.Si.Connections = "mem(astext=true, indent=true, pattern=\"%level% [%timestamp%]: %title%\")"
#SIAuto.Si.Connections = "mem(astext=false, indent=true, pattern=\"%level% [%timestamp%]: %title%\")"
SIAuto.Si.Enabled = True

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main

# test all session methods, using specified logging level.
# note that we will just change the Parent.Level value for this.
# the Parent.Default and SISession.Level are set to Debug, in the
# event that configuration file contains other values.  this
# makes for a 1-to-1 comparison between level test runs.
_logsi.Parent.Level = _logsi.Level
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

# logging done - write memory stream to output file.
try:

    # set file path and open flags.
    if (SIAuto.Si.Connections.find("astext=true") != -1):
        filePath:str = "./tests/logfiles/MemProtocol-AsTextTrue.txt"
    else:
        filePath:str = "./tests/logfiles/MemProtocol-AsTextFalse.sil"

    # open the log file.
    fileFlags:str = 'wb'    # 'wb' is write as binary; use 'ab' to append to existing file if desired.
    stream = open(filePath, fileFlags)

    # inform the memory protocol to write log data in memory to our log file.
    SIAuto.Si.Dispatch("mem", 0, stream)

    print("In-Memory log was written to log file: " + filePath)

except Exception as ex:

    print(str.format("Could not save log data to file.  Ensure it is a valid file name, and that it is not open in another application.  Log file path: \"{0}\".\nException message:{1}", fileName, str(ex)))

# print SI event counts, unwire events, and dispose of SmartInspect.
SIEventHandlerClass.PrintResults(SIAuto.Si)
SIEventHandlerClass.UnWireEvents(SIAuto.Si)
SIAuto.Si.Dispose()

print("\nTest Script Ended.")
