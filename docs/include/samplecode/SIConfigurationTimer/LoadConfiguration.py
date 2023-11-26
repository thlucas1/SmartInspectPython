# package imports.
from smartinspectpython.siauto import *

# load SmartInspect settings from a configuration settings file.
siConfigPath:str = "./smartinspect.cfg"
SIAuto.Si.LoadConfiguration(siConfigPath)

# start monitoring the configuration file for changes, and reload it when it changes.
siConfigTask:SIConfigurationTimer = SIConfigurationTimer(SIAuto.Si, siConfigPath)

# get smartinspect logger reference.
logsi:SISession = SIAuto.Main
