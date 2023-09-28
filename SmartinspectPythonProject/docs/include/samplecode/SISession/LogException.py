# package imports.
from smartinspectpython.siauto import *

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main

try:
    
    _logsi.LogMessage("Forcing a divide by zero error ...")
    1/0   # force an exception
    _logsi.LogMessage("You should not see this message due to the above exception.")
    
except Exception as ex:
    
    # log exceptions.
    _logsi.LogException("*** Caught exception!", ex)
    _logsi.LogException(None, ex)
