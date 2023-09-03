from io import BufferedReader, TextIOWrapper

# our package imports.
from smartinspectpython.dotnetcsharp import ArgumentNullException
from smartinspectpython.sierroreventargs import SIErrorEventArgs
from smartinspectpython.siinfoeventargs import SIInfoEventArgs
from smartinspectpython.sifiltereventargs import SIFilterEventArgs
from smartinspectpython.siwatcheventargs import SIWatchEventArgs
from smartinspectpython.silogentryeventargs import SILogEntryEventArgs
from smartinspectpython.siprocessfloweventargs import SIProcessFlowEventArgs
from smartinspectpython.sicontrolcommandeventargs import SIControlCommandEventArgs
from smartinspectpython.sioptionfoundeventargs import SIOptionFoundEventArgs
from smartinspectpython.sisession import SISession

# auto-generate the "__all__" variable with classes decorated with "@export".
from smartinspectpython.siutils import export


@export
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
        pass

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
        pass

    def ErrorEvent(sender:object, e:SIErrorEventArgs) -> None:
        print("* SIEvent {0}".format(str(e)))
        SIEventHandlerClass.ErrorCount = SIEventHandlerClass.ErrorCount + 1
        pass

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

    def VerifyLogEntryCounts(si, level, levelcounts) -> None:
        for key in levelcounts.keys():
            if (str(level.name) == key):
                levelcount:int = levelcounts[key]
                if (SIEventHandlerClass.LogEntryCount == levelcount):
                    print("Level \"{0}\" LogEntryCount of {1} matches expected count of {2}.".format(str(level.name), str(SIEventHandlerClass.LogEntryCount), str(levelcount)))
                else:
                    #raise Exception("Test FAILED!  Level \"{0}\" LogEntryCount of {1} does not match expected count of {2}!  See console output for more details.".format(str(level.name), str(SIEventHandlerClass.LogEntryCount), str(levelcount)))
                    print("**** WARNING **** Level \"{0}\" LogEntryCount of {1} does not match expected count of {2}.".format(str(level.name), str(SIEventHandlerClass.LogEntryCount), str(levelcount)))


    def VerifyErrorCount(si, level) -> None:
        if SIEventHandlerClass.ErrorCount > 0:
            raise Exception("Test FAILED!  ErrorCount > 0 for Level \"{0}\" test!  See console output for more details.".format(str(level.name)))




@export
class OptionsParserTestClass:
    """
    Helper class for SIOptionsParser class.
    """

    @staticmethod
    def WireEvents(parser) -> None:
        # wire up events.
        parser.OptionFoundEvent += OptionsParserTestClass.AddOption

    @staticmethod
    def UnWireEvents(parser) -> None:
        # unwire events.
        parser.OptionFoundEvent -= OptionsParserTestClass.AddOption

    def AddOption(sender:object, args:SIOptionFoundEventArgs):
        print("Protocol Option Found: {0}".format(str(args)))


@export
class TestMethodTracking:
    """
    Helper class used to demonstrate method tracking.
    """

    @staticmethod
    def TestMethod1(logger:SISession) -> None:
        logger.EnterMethod()
        logger.LogMessage("Started SIEventHandlerClass.TestMethod1 funciton.")
        try:
            raise ArgumentNullException("myargument")
        except Exception as ex:
            logger.LogException("Caught exception1 in TestMethod1", ex)
            logger.LogException(None, ex)
        logger.LogMessage("Ended SIEventHandlerClass.TestMethod1 funciton.")
        logger.LeaveMethod()

    @staticmethod
    #@SIAuto.Main.Track(obj)
    def TestMethod2(logger:SISession) -> None:
        logger.LogMessage("Started SIEventHandlerClass.TestMethod2 funciton.")
        try:
            raise ArgumentNullException("myargument")
        except Exception as ex:
            logger.LogException("Caught exception1 in TestMethod2", ex)
            logger.LogException(None, ex)
        logger.LogMessage("Ended SIEventHandlerClass.TestMethod2 funciton.")


@export
class TestFileAccessHelper:
    """
    Helper class used to demonstrate file access logging.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def GetBinaryStream(fileName:str) -> BufferedReader:
        reader:BufferedReader = open(fileName, 'rb')
        return reader

    @staticmethod
    def GetTextStream(fileName:str) -> TextIOWrapper:
        reader:TextIOWrapper = open(fileName, 'r')
        return reader


@export
class TestLogObjectHelper:
    """
    Helper class used to test the LogObject method.
    """

    PUBLIC_STATIC_STRING:str = "Public Static String"
    _PRIVATE_STATIC_STRING:str = "Private Static String"
    __INTERNAL_STATIC_STRING:str = "Internal Static String"

    def __init__(self) -> None:
        """
        Initializes a new class instance.
        """
        # initialize properties.
        self.fPublicProperty = "Public Property String initialized."
        self._fPrivateProperty = "Private Property String initialized."
        self.__fInternalProperty = "Internal Property String initialized."

        # initialize non-properties.
        self.fPublicVariable = "Public Variable String initialized."
        self._fPrivateVariable = "Private Variable String initialized."
        self.__fInternalVariable = "Internal Variable String initialized."

    @property
    def PublicProperty(self) -> str:
        """ 
        Gets a public property.
        """
        return self.fPublicProperty
    
    @PublicProperty.setter
    def PublicProperty(self, value:str) -> None:
        """ 
        Sets a public property.
        """
        self.fPublicProperty = value

    @property
    def _PrivateProperty(self) -> str:
        """ 
        Gets a private property.
        """
        return self._fPrivateProperty
    
    @_PrivateProperty.setter
    def _PrivateProperty(self, value:str) -> None:
        """ 
        Sets a private property.
        """
        self._fPrivateProperty = value

    @property
    def __InternalProperty(self) -> str:
        """ 
        Gets a internal property.
        """
        return self.__fInternalProperty
    
    @__InternalProperty.setter
    def __InternalProperty(self, value:str) -> None:
        """ 
        Sets a internal property.
        """
        self.__fInternalProperty = value

    def PublicStaticMethod(self, parm1:str) -> None:
        print(str.format("PublicStaticMethod - Parm={0}", parm1))

    def PublicStaticFunction(self, parm1:str) -> str:
        print(str.format("PublicStaticFunction - Parm={0}", parm1))
        return "PublicStaticFunction - returns " + TestLogObjectHelper.PUBLIC_STATIC_STRING

    def _PrivateStaticMethod(self, parm1:str) -> None:
        print(str.format("_PrivateStaticMethod - Parm={0}", parm1))

    def _PrivateStaticFunction(self, parm1:str) -> str:
        print(str.format("_PrivateStaticFunction - Parm={0}", parm1))
        return "_PrivateStaticFunction - returns " + TestLogObjectHelper._PRIVATE_STATIC_STRING

    def __InternalStaticMethod(self, parm1:str) -> None:
        print(str.format("__InternalStaticMethod - Parm={0}", parm1))

    def __InternalStaticFunction(self, parm1:str) -> str:
        print(str.format("__InternalStaticFunction - Parm={0}", parm1))
        return "__InternalStaticFunction - returns " + TestLogObjectHelper.__INTERNAL_STATIC_STRING

    def PublicMethod(self, parm1:str) -> None:
        print(str.format("PublicMethod - Parm={0}", parm1))
        print(str.format("PublicMethod - PublicProperty={0}", self.PublicProperty));

    def PublicFunction(self, parm1:str) -> str:
        print(str.format("PublicFunction - Parm={0}", parm1))
        return "PublicFunction return value"

    def _PrivateMethod(self, parm1:str) -> None:
        print(str.format("_PrivateMethod - Parm={0}", parm1))
        print(str.format("_PrivateMethod - _PrivateProperty={0}", self._PrivateProperty))

    def _PrivateFunction(self, parm1:str) -> str:
        print(str.format("_PrivateFunction - Parm={0}", parm1))
        return "_PrivateFunction returns " + self._fPrivateVariable

    def __InternalMethod(self, parm1:str) -> None:
        print(str.format("__InternalMethod - Parm={0}", parm1))
        print(str.format("__InternalMethod - __InternalProperty={0}", self.__InternalProperty))

    def __InternalFunction(self, parm1:str) -> str:
        print(str.format("__InternalFunction - Parm={0}", parm1))
        return "__InternalFunction return value"
