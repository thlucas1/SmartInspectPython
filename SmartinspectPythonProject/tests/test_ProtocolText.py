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

# write packet events to console.
#SIEventHandlerClass.WriteEventPacketsToConsole = True

# set smartinspect connections, and enable logging.
SIAuto.Si.Connections = "text(filename=\"./tests/logfiles/TextProtocol-RotateHourly.txt\", rotate=hourly, maxparts=24, indent=true, pattern=\"%level% [%timestamp%]: %title%\", append=true)"
#SIAuto.Si.Connections = "text(filename=\"./tests/logfiles/TextProtocol-RotateHourly.txt\", rotate=hourly, maxparts=24, indent=false, append=true)"
#SIAuto.Si.Connections = "text(filename=\"./tests/logfiles/TextProtocol-RotateHourly.txt\", rotate=hourly, maxparts=24, indent=true, append=true)"
SIAuto.Si.Enabled = True

# get smartinspect logger reference.
logsi:SISession = SIAuto.Main

# test all session methods, using specified logging level.
# note that we will just change the Parent.Level value for this.
# the Parent.Default and SISession.Level are set to Debug, in the
# event that configuration file contains other values.  this
# makes for a 1-to-1 comparison between level test runs.
logsi.Parent.Level = logsi.Level
logsi.Parent.DefaultLevel = SILevel.Debug
logsi.Level = SILevel.Debug
TestSessionMethods.TestAllMethods(logsi)

# log counters to SI console.
logsi.Watch(SILevel.Fatal, "Total Packets LogEntry", SIEventHandlerClass.LogEntryCount)
logsi.Watch(SILevel.Fatal, "Total Packets ProcessFlow", SIEventHandlerClass.ProcessFlowCount)
logsi.Watch(SILevel.Fatal, "Total Packets ControlCmd", SIEventHandlerClass.ControlCommandCount)
logsi.Watch(SILevel.Fatal, "Total Packets Watch", SIEventHandlerClass.WatchCount)
logsi.Watch(SILevel.Fatal, "Total Packets Filtered", SIEventHandlerClass.FilterCount)
logsi.Watch(SILevel.Fatal, "Total Error", SIEventHandlerClass.ErrorCount)
logsi.Watch(SILevel.Fatal, "Total Info", SIEventHandlerClass.InfoCount)

# print SI event counts, unwire events, and dispose of SmartInspect.
SIEventHandlerClass.PrintResults(SIAuto.Si)
SIEventHandlerClass.UnWireEvents(SIAuto.Si)
SIAuto.Si.Dispose()

print("\nTest Script Ended.")
