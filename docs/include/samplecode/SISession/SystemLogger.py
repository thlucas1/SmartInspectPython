# package imports.
from smartinspectpython.siauto import *

# set smartinspect connections, and enable logging.
SIAuto.Si.Connections = "tcp(host=localhost,port=4228,timeout=30000)"
SIAuto.Si.Enabled = True

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main

# configure system logging (to file).
import logging
import logging.handlers
import os
exedir = os.path.dirname(sys.argv[0])
logfilePath:str = exedir + "/logfiles/"
handler = logging.handlers.WatchedFileHandler(logfilePath+"test_SystemLogger_Output.log")
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
_LOGGER = logging.getLogger()
_LOGGER.setLevel("INFO")
_LOGGER.addHandler(handler)

# get smartinspect logger reference, and add system logging.
_logsi:SISession = SIAuto.Main
_logsi.SystemLogger = _LOGGER

# data used by various tests.
argsVar1:str="Argument 1 Value"
argsVar2:int=1000

# log some messages of different logging levels.
# note that the "LogDebug" messages will not appear in the system logging file due to "INFO" system logging level.
_logsi.LogDebug("This is a debug message.  It will not be displayed if Level=Verbose or above.")
_logsi.LogDebug("This is a debug message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Verbose or above.", argsVar1, argsVar2)
_logsi.LogVerbose("This is a verbose message.  It will not be displayed if Level=Message or above.")
_logsi.LogVerbose("This is a verbose message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Message or above.", argsVar1, argsVar2)
_logsi.LogMessage("This is a message.  It will not be displayed if Level=Warning or above.")
_logsi.LogMessage("This is a message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Warning or above.", argsVar1, argsVar2)
_logsi.LogWarning("This is a warning message.  It will not be displayed if Level=Error or above.")
_logsi.LogWarning("This is a warning message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Error or above.", argsVar1, argsVar2)
_logsi.LogError("This is a error message.  It will not be displayed if Level=Fatal or above.")
_logsi.LogError("This is a error message with *args: str1='%s', int2=%i.  It will not be displayed if Level=Fatal or above.", argsVar1, argsVar2)
_logsi.LogFatal("This is a fatal error message.")
_logsi.LogFatal("This is a fatal error message with *args: str1='%s', int2=%i.", argsVar1, argsVar2)

# log an exception.
try:

    raise Exception("This is a forced exception used to test the LogException method.")

except Exception as ex:

    _logsi.LogException("LogException - with Custom title, exception details in SI Console viewer area.", ex)
    _logsi.LogException(None, ex)
