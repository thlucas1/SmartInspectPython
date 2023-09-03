# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

import time

# our package imports.
from smartinspectpython.siauto import *

# import classes used for test scenarios.
from testClassDefinitions import SIEventHandlerClass

print("Test Script Starting.\n")

# wire up smartinspect events.
SIEventHandlerClass.WireEvents(SIAuto.Si)

# load SmartInspect settings from a configuration settings file.
configPath:str = "./tests/test_configuration.settings.txt"
print("Loading SmartInspect settings from configuration settings file:\n{0}\n".format(configPath))
SIAuto.Si.LoadConfiguration(configPath)

# start monitoring the configuration file for changes, and reload it when it changes.
# this will check the file for changes every 5 seconds.
config:SIConfigurationTimer = SIConfigurationTimer(SIAuto.Si, configPath, 2)
print("Monitoring SmartInspect configuration settings for changes.")

# get smartinspect logger reference.
logsi:SISession = SIAuto.Main
SIAuto.Si.AddSession('NewSession1', True)

# keep logging messages every second for 300 seconds.
# while it is running, change the configuration file "level" value
# and watch the Si Console to see if changes were applied.
for i in range(30):
    time.sleep(1)
    logsi.LogDebug("This is a test Debug message (current Level=\"{0}\").".format(str(logsi.Parent.Level)))
    logsi.LogVerbose("This is a test Verbose message (current Level=\"{0}\").".format(str(logsi.Parent.Level)))
    logsi.LogMessage("This is a test Message message (current Level=\"{0}\").".format(str(logsi.Parent.Level)))
    logsi.LogWarning("This is a test Warning message (current Level=\"{0}\").".format(str(logsi.Parent.Level)))
    logsi.LogError("This is a test Error message (current Level=\"{0}\").".format(str(logsi.Parent.Level)))
    logsi.LogFatal("This is a test Fatal message (current Level=\"{0}\").".format(str(logsi.Parent.Level)))

    logsi1:SISession = SIAuto.Si.GetSession("NewSession1")
    if (logsi1 != None):
        logsi1.LogMessage("LOGSI1 - This is a test Message message (current Level=\"{0}\").".format(str(logsi1.Parent.Level)))


# stop configuration file monitoring for changes.
#config.Stop()

print("\nTest Script Ended.")
