# Change Log

All notable changes to this project are listed here.
Detailed changes are listed in the module where the change was made.

Change are listed in reverse chronological order (newest to oldest).

<span class="changelog">

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