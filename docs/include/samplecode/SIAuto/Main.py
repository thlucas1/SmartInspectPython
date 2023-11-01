# package imports.
from smartinspectpython.siauto import *

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main
    
# log some messages and data.
_logsi.LogSystem(SILevel.Debug)
_logsi.LogDebug("This is a Debug message.")
_logsi.LogMessage("This is a Message.")
_logsi.LogWarning("You have been warned!")
_logsi.LogError("Danger Will Robinson!")
