# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

from datetime import datetime

# our package imports.
from smartinspectpython.siauto import *
from smartinspectpython.sierroreventargs import SIErrorEventArgs
from smartinspectpython.sifiltereventargs import SIFilterEventArgs
from smartinspectpython.siwatcheventargs import SIWatchEventArgs
from smartinspectpython.silogentryeventargs import SILogEntryEventArgs
from smartinspectpython.siprocessfloweventargs import SIProcessFlowEventArgs
from smartinspectpython.sicontrolcommandeventargs import SIControlCommandEventArgs
from smartinspectpython.sicolor import SIColors

class SIEventHandlerClass:

    # static variables.
    ErrorCount:int = 0
    FilterCount:int = 0
    WatchCount:int = 0
    LogEntryCount:int = 0
    ProcessFlowCount:int = 0
    ControlCommandCount:int = 0
    TotalCount:int = 0

    @staticmethod
    def WireEvents(si) -> None:
        # wire up events.
        si.ErrorEvent += SIEventHandlerClass.ErrorEvent
        si.FilterEvent += SIEventHandlerClass.FilterEvent
        si.WatchEvent += SIEventHandlerClass.WatchEvent
        si.LogEntryEvent += SIEventHandlerClass.LogEntryEvent
        si.ProcessFlowEvent += SIEventHandlerClass.ProcessFlowEvent
        si.ControlCommandEvent += SIEventHandlerClass.ControlCommandEvent
        pass

    @staticmethod
    def UnWireEvents(si) -> None:
        # unwire events.
        si.ErrorEvent -= SIEventHandlerClass.ErrorEvent
        si.FilterEvent -= SIEventHandlerClass.FilterEvent
        si.WatchEvent -= SIEventHandlerClass.WatchEvent
        si.LogEntryEvent -= SIEventHandlerClass.LogEntryEvent
        si.ProcessFlowEvent -= SIEventHandlerClass.ProcessFlowEvent
        si.ControlCommandEvent -= SIEventHandlerClass.ControlCommandEvent
        pass

    def ErrorEvent(sender:object, e:SIErrorEventArgs) -> None:
        print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.ErrorCount = SIEventHandlerClass.ErrorCount + 1
        pass

    def FilterEvent(sender:object, e:SIFilterEventArgs) -> None:
        #print("* SIEvent {0}".format(str(e)))
        # ignore all warning level packets.
        #if (e.Packet.Level == SILevel.Warning):
        #    e.Cancel = True
        SIEventHandlerClass.FilterCount = SIEventHandlerClass.FilterCount + 1
        pass

    def WatchEvent(sender:object, e:SIWatchEventArgs) -> None:
        #print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.TotalCount = SIEventHandlerClass.TotalCount + 1
        SIEventHandlerClass.WatchCount = SIEventHandlerClass.WatchCount + 1
        pass

    def LogEntryEvent(sender:object, e:SILogEntryEventArgs) -> None:
        #print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.TotalCount = SIEventHandlerClass.TotalCount + 1
        SIEventHandlerClass.LogEntryCount = SIEventHandlerClass.LogEntryCount + 1
        pass

    def ProcessFlowEvent(sender:object, e:SIProcessFlowEventArgs) -> None:
        #print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.TotalCount = SIEventHandlerClass.TotalCount + 1
        SIEventHandlerClass.ProcessFlowCount = SIEventHandlerClass.ProcessFlowCount + 1
        pass

    def ControlCommandEvent(sender:object, e:SIControlCommandEventArgs) -> None:
        #print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.TotalCount = SIEventHandlerClass.TotalCount + 1
        SIEventHandlerClass.ControlCommandCount = SIEventHandlerClass.ControlCommandCount + 1
        pass

    def PrintResults(si) -> str:
        print("")
        print("SI Protocol Connections string used for this test:\n" + si.Connections)
        print("")
        print("SI Event Handler Results:")
        print("")
        print("- # Watch Events          = " + str(SIEventHandlerClass.WatchCount))
        print("- # LogEntry Events       = " + str(SIEventHandlerClass.LogEntryCount))
        print("- # ProcessFlow Events    = " + str(SIEventHandlerClass.ProcessFlowCount))
        print("- # ControlCommand Events = " + str(SIEventHandlerClass.ControlCommandCount))
        print("")
        print("- # Total Events          = " + str(SIEventHandlerClass.TotalCount))
        print("")
        print("- # Error Events          = " + str(SIEventHandlerClass.ErrorCount))
        print("- # Filter Events         = " + str(SIEventHandlerClass.FilterCount))
        print("")


# wire up smartinspect events.
SIEventHandlerClass.WireEvents(SIAuto.Si)

# set smartinspect connections, and enable logging.
SIAuto.Si.Connections = "tcp(host=localhost,port=4228,timeout=30000)"
SIAuto.Si.Enabled = True

# get smartinspect logger reference.
logsi:SISession = SIAuto.Main

# test some process flow methods.
logsi.EnterProcess(None,"My Process")
logsi.LogMessage("This message is in process My Process.")
logsi.LogWarning("This warning is in process My Process.")
logsi.LeaveProcess(None,"My Process")

# test some logentry methods.
logsi.LogDebug("This is a debug message.")
logsi.LogVerbose("This is a verbose message.")
logsi.LogMessage("This is a message.")
logsi.LogWarning("This is a warning message.")
logsi.LogError("This is a error message in RED.", SIColors.Red.value)
logsi.LogFatal("This is a fatal error message in RED.", SIColors.Red.value)

# test some control command methods.
logsi.ClearWatches()

# test some watch methods.
logsi.Watch(None,"string_py", "string1 value")
logsi.Watch(None,"int_py", int(0))
logsi.Watch(None,"float_py", float(3.14159))
logsi.Watch(None,"datetime_py", datetime(2023,5,11,12,30,10))
logsi.Watch(None,"bool_py", True)
logsi.Watch(None,"byte_py", 0xff)

# print SI event counts, unwire events, and dispose of SmartInspect.
SIEventHandlerClass.PrintResults(SIAuto.Si)
SIEventHandlerClass.UnWireEvents(SIAuto.Si)
SIAuto.Si.Dispose()
