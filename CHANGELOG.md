# Change Log

All notable changes to this project are listed here.
Detailed changes are listed in the module where the change was made.

Change are listed in reverse chronological order (newest to oldest).

<span class="changelog">

###### [ 3.0.33 ] - 2024/02/02

  * Updated `SISession.EnterMethodParmList` to always return a `SIMethodParmListContext` instance regarless of logging level.

###### [ 3.0.32 ] - 2024/02/02

  * Added `SIMethodParmListContext` class to SIAuto for `import *` support.

###### [ 3.0.31 ] - 2024/02/02

  * Added new methods to `SISession` class: EnterMethodParmList, LogMethodParmList.
  * Added `SIMethodParmListContext` class to support logging of input parameter lists.

###### [ 3.0.30 ] - 2023/12/08

  * Modified pretty print settings for `SISession.LogXml` to not add an xml declaration if one was not present on the input xml being logged.

###### [ 3.0.29 ] - 2023/12/08

  * Added pretty print capability to the following `SISession` methods: `LogDictionary`, `LogXml`.

###### [ 3.0.28 ] - 2023/11/25

  * Changed `SIConfigurationTimer` class to use the `watchdog` (1.0.1) package to monitor file system change events.  Prior `threading.Condition` code was consuming large amounts of cpu when monitoring the smartinspect configuration file for changes.

###### [ 3.0.27 ] - 2023/10/31

  * Changed code in the SIProtocol module to see if a directory prefix is specified for the log file.  If not, then it will not try to create a directory structure.  Prior to this fix, it was always expecting a directory specification.

###### [ 3.0.26 ] - 2023/10/20

  * Added new methods to SISession class: LogXml, LogXmlFile.

###### [ 3.0.25 ] - 2023/10/18

  * Added SIAuto to __init__.py __all__  value so that it is included in the global import list.

###### [ 3.0.24 ] - 2023/10/18

  * Changed various SISession methods to not log internal errors if an object to be logged was null.  Prior to this fix, the console viewer would only display a "LogX: X argument is null" message and drop the title text completely.  This fix will allow the title text to be logged, as well as indicate to the user that the supplied object to log was null.  Methods changed were: LogDictionary, LogEnunmerable, LogBool, LogByte, LogChar, LogComplex, LogDateTime, LogFloat, LogInt, LogObject, LogObjectValue, LogSqliteDbSchemaCursor, LogString, LogThread.
  * Changed all SISession methods to immediately check for "if (not self.IsOn(level)): return" so Python returns execution immediately if the level criteria is not satisfied.  Prior to this, Python would have to interpret all lines of code until it reached a "return" value if the "if (self.IsOn(level)):" syntax was used.  This should yield a slight performance increase due to less interpretation time spent.

###### [ 3.0.23 ] - 2023/10/15

  * Changed SIPacket methods GetThreadId and GetProcessId to verify the returned size of their values do not exceed 32-bits.  Prior to this fix, the console viewer would report a value of zero if the values exceeded 32-bits in length.  Python frequently returns thread id's larger than 32-bits on most operating systems.  Although the value is incorrect, it is better than a zero value.  The only way to truly fix this is to expand the thread id and process id sizes in the console viewer; until then, this is the best we can do.

###### [ 3.0.22 ] - 2023/09/29

  * Set Logger.propagate = False so that our exception capture process does not forward the message on to other loggers.
  * Changed methods in SISession that support SystemLogger functionality to allow bypass of logging to the system logger.
  * Updated documentation sample code and examples.

###### [ 3.0.21 ] - 2023/09/27

  * Added SystemLogger functionality to allow logging to system logs.
  * Changed SIColors class initialiation method to accept either an integer or SIColors enum for value argument.
  * Updated documentation sample code and examples.

###### [ 3.0.20 ] - 2023/09/03

  * Changed alpha byte from 0xFF to 0x00 for all color definitions in the SIColors enum class.
  * Changed all Session.LogX method signatures to use the SIColors enum type, or an integer value in ARGB format.
  * Updated internal build processes to use Python Virtual Environment.

###### [ 3.0.19 ] - 2023/09/01

  * Minor internal naming changes to functions in various modules to conform to Python best-practice naming standards (e.g. use single underscore instead of double underscore for internal methods).

###### [ 3.0.18 ] - 2023/08/31

  * Major changes to the package!  All classes were renamed to start with an "SI" prefix, to avoid naming conflicts with other namespaces.  
  * Renamed the KnownColorValues class to SIColors.  
  * I was hesitant to do this, as it will cause breaking changes to applications that utilize the package.  It was required though, to avoid namespace conflicts with like-named modules in system / other packages.

###### [ 3.0.17 ] - 2023/07/11

  * Minor internal only changes to build process.
 
###### [ 3.0.16 ] - 2023/07/11

  * Changed Session.GetMethodName method to use inspect.stack(0) instead of inspect.stack() to improve performace.

###### [ 3.0.15 ] - 2023/06/30

  * Changed 'Development Status' to '5 - Production/Stable', and uploaded to Pypi.org site.

###### [ 3.0.14 ] - 2023/06/28

  * Changed Session class to use temporary logger to capture exception details in LogException method.

###### [ 3.0.13 ] - 2023/06/23

  * Changed Session LogAssigned method to properly format the LogMessage title value.

###### [ 3.0.12 ] - 2023/06/17

  * Changed Session.EnterMethod, LeaveMethod to include source file.
  * Added default title to Session.LogAppDomain method.
  * Added exception handling in Session.LogSystem for user name value.  It was failing on Windows WSL systems, returning some sort of permissions error.

###### [ 3.0.11 ] - 2023/06/17

  * Added *args support to Session class methods: LogDebug, LogVerbose, LogMessage, LogWarning, LogException, and LogFatal methods.

###### [ 3.0.10 ] - 2023/06/15

  * Added Session.LogPngFile, LogPngStream methods for SI Console 3.4+ support.

###### [ 3.0.9 ] - 2023/06/15

  * Changed the Session.CurrentMethodName, CurrentMethodNameClass, CurrentMethodNameClassNamespace properties to static methods.

###### [ 3.0.8 ] - 2023/06/09

  * Added InfoEvent event and RaiseInfoEvent methods to SmartInspect and Protocol classes.  This allows SmartInspect to convey informational events to interested parties.  For example, the SI Console Server banner is available, as well as when a SIConfiguration settings file is changed and reloaded if using SIConfigurationTimer class.

###### [ 3.0.7 ] - 2023/06/05

  * Documentation updates.

###### [ 3.0.6 ] - 2023/06/02

  * Documentation updates.

###### [ 3.0.5 ] - 2023/06/01

  * Fixed an issue with Session.GetMethod() not returning a method name.

###### [ 3.0.4 ] - 2023/05/31

  * Fixed an error related to using the "pack()" method that was not using the endian format characters (e.g. < >).
    This was causing packet sizes to be off on non-Windows platforms.

###### [ 3.0.2 ] - 2023/05/31

  * Added conditional import of pipeprotocol module, as named-pipes are only supported on the Windows platform.  This was causing module not found error when trying to execute on non-Windows platforms.

###### [ 3.0.0 ] - 2023/05/30

  * Version 3 initial release, ported to Python from the SmartInspect for .Net framework.

</span>