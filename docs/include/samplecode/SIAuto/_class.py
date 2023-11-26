# package imports.
from smartinspectpython.siauto import *

#############################################################################
# Use the following for 1-time initialization code:
#############################################################################

# load SmartInspect settings from a configuration settings file.
siConfigPath:str = "./smartinspect.cfg"
SIAuto.Si.LoadConfiguration(siConfigPath)

# start monitoring the configuration file for changes, and reload it when it changes.
siConfigTask:SIConfigurationTimer = SIConfigurationTimer(SIAuto.Si, siConfigPath)

#############################################################################
# Use the following in main (or classes) in your project:
#############################################################################

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main
    
# log some messages and data.
_logsi.LogSystem(SILevel.Debug)
_logsi.LogDebug("This is a Debug message.")
_logsi.LogMessage("This is a Message.")
_logsi.LogWarning("You have been warned!")
_logsi.LogError("Danger Will Robinson!")
