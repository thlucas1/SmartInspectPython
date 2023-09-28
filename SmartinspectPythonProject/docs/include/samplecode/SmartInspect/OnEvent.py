# package imports.
from datetime import datetime
from smartinspectpython.siauto import *

class SIEventHandlerClass:
    """
    Helper class for SmartInspect class testing.
    """

    # static variables.
    WriteEventPacketsToConsole:bool = False
    ErrorCount:int = 0
    InfoCount:int = 0
    FilterCount:int = 0
    FilterCancelCount:int = 0
    WatchCount:int = 0
    LogEntryCount:int = 0
    ProcessFlowCount:int = 0
    ControlCommandCount:int = 0
    TotalCount:int = 0


    @staticmethod
    def WireEvents(si) -> None:
        # wire up events.
        si.ErrorEvent += SIEventHandlerClass.ErrorEvent
        si.InfoEvent += SIEventHandlerClass.InfoEvent
        si.FilterEvent += SIEventHandlerClass.FilterEvent
        si.WatchEvent += SIEventHandlerClass.WatchEvent
        si.LogEntryEvent += SIEventHandlerClass.LogEntryEvent
        si.ProcessFlowEvent += SIEventHandlerClass.ProcessFlowEvent
        si.ControlCommandEvent += SIEventHandlerClass.ControlCommandEvent


    @staticmethod
    def UnWireEvents(si) -> None:
        # unwire events.
        si.ErrorEvent -= SIEventHandlerClass.ErrorEvent
        si.InfoEvent -= SIEventHandlerClass.InfoEvent
        si.FilterEvent -= SIEventHandlerClass.FilterEvent
        si.WatchEvent -= SIEventHandlerClass.WatchEvent
        si.LogEntryEvent -= SIEventHandlerClass.LogEntryEvent
        si.ProcessFlowEvent -= SIEventHandlerClass.ProcessFlowEvent
        si.ControlCommandEvent -= SIEventHandlerClass.ControlCommandEvent


    def ErrorEvent(sender:object, e:SIErrorEventArgs) -> None:
        print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.ErrorCount = SIEventHandlerClass.ErrorCount + 1


    def InfoEvent(sender:object, e:SIInfoEventArgs) -> None:
        print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.InfoCount = SIEventHandlerClass.InfoCount + 1
        pass


    def FilterEvent(sender:object, e:SIFilterEventArgs) -> None:
        if SIEventHandlerClass.WriteEventPacketsToConsole:
            print("* SIEvent {0}".format(str(e)))
        # ignore all warning level packets.
        #if (e.Packet.Level == SILevel.Warning):
        #    SIEventHandlerClass.FilterCancelCount = SIEventHandlerClass.FilterCancelCount + 1
        #    e.Cancel = True
        SIEventHandlerClass.FilterCount = SIEventHandlerClass.FilterCount + 1
        pass


    def WatchEvent(sender:object, e:SIWatchEventArgs) -> None:
        if SIEventHandlerClass.WriteEventPacketsToConsole:
            print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.TotalCount = SIEventHandlerClass.TotalCount + 1
        SIEventHandlerClass.WatchCount = SIEventHandlerClass.WatchCount + 1
        pass


    def LogEntryEvent(sender:object, e:SILogEntryEventArgs) -> None:
        if SIEventHandlerClass.WriteEventPacketsToConsole:
            print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.TotalCount = SIEventHandlerClass.TotalCount + 1
        SIEventHandlerClass.LogEntryCount = SIEventHandlerClass.LogEntryCount + 1
        pass


    def ProcessFlowEvent(sender:object, e:SIProcessFlowEventArgs) -> None:
        if SIEventHandlerClass.WriteEventPacketsToConsole:
            print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.TotalCount = SIEventHandlerClass.TotalCount + 1
        SIEventHandlerClass.ProcessFlowCount = SIEventHandlerClass.ProcessFlowCount + 1
        pass


    def ControlCommandEvent(sender:object, e:SIControlCommandEventArgs) -> None:
        if SIEventHandlerClass.WriteEventPacketsToConsole:
            print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.TotalCount = SIEventHandlerClass.TotalCount + 1
        SIEventHandlerClass.ControlCommandCount = SIEventHandlerClass.ControlCommandCount + 1
        pass


    def ResetCounters(si) -> None:
        print("Resetting all SIEventHandlerClass counters to zero.")
        SIEventHandlerClass.ErrorCount:int = 0
        SIEventHandlerClass.InfoCount:int = 0
        SIEventHandlerClass.FilterCount:int = 0
        SIEventHandlerClass.FilterCancelCount:int = 0
        SIEventHandlerClass.WatchCount:int = 0
        SIEventHandlerClass.LogEntryCount:int = 0
        SIEventHandlerClass.ProcessFlowCount:int = 0
        SIEventHandlerClass.ControlCommandCount:int = 0
        SIEventHandlerClass.TotalCount:int = 0

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
        print("- # Info Events           = " + str(SIEventHandlerClass.InfoCount))
        print("- # Filter Events         = " + str(SIEventHandlerClass.FilterCount))
        print("- # Filter Cancel Events  = " + str(SIEventHandlerClass.FilterCancelCount))
        print("")


# wire up smartinspect events.
SIEventHandlerClass.WireEvents(SIAuto.Si)

# set smartinspect connections, and enable logging.
SIAuto.Si.Connections = "tcp(host=localhost,port=4228,timeout=30000)"
SIAuto.Si.Enabled = True

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main

# test some process flow methods.
_logsi.EnterProcess(None,"My Process")
_logsi.LogMessage("This message is in process My Process.")
_logsi.LogWarning("This warning is in process My Process.")
_logsi.LeaveProcess(None,"My Process")

# test some logentry methods.
_logsi.LogDebug("This is a debug message.")
_logsi.LogVerbose("This is a verbose message.")
_logsi.LogMessage("This is a message.")
_logsi.LogWarning("This is a warning message.")
_logsi.LogError("This is a error message in RED.", SIColors.Red)
_logsi.LogFatal("This is a fatal error message in RED.", SIColors.Red)

# test some control command methods.
_logsi.ClearWatches()

# test some watch methods.
_logsi.Watch(None,"string_py", "string1 value")
_logsi.Watch(None,"int_py", int(0))
_logsi.Watch(None,"float_py", float(3.14159))
_logsi.Watch(None,"datetime_py", datetime(2023,5,11,12,30,10))
_logsi.Watch(None,"bool_py", True)
_logsi.Watch(None,"byte_py", 0xff)

# print SI event counts, unwire events, and dispose of SmartInspect.
SIEventHandlerClass.PrintResults(SIAuto.Si)
SIEventHandlerClass.UnWireEvents(SIAuto.Si)
SIAuto.Si.Dispose()
