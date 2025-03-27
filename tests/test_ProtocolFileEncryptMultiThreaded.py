# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

# our package imports.
#from smartinspectpython.siauto import *

print("Test Script Starting.\n")

try:

    from smartinspectpython.siauto import SIAuto, SILevel, SISession, SIConfigurationTimer, SIColors

    # load SmartInspect settings from a configuration settings file.
    siConfigPath: str = "./tests/testdata/smartinspect_encrypted.cfg"
    SIAuto.Si.LoadConfiguration(siConfigPath)

    # start monitoring the configuration file for changes, and reload it when it changes.
    # this will check the file for changes every 60 seconds.
    siConfig:SIConfigurationTimer = SIConfigurationTimer(SIAuto.Si, siConfigPath)

    # get smartinspect logger reference; create a new session for this module name.
    _logsi:SISession = SIAuto.Si.GetSession(__name__)
    if (_logsi == None):
        _logsi = SIAuto.Si.AddSession(__name__, True)
    _logsi.LogSeparator(SILevel.Error)
    _logsi.LogVerbose("__init__.py HAS SpotifyPlus: initialization")
    _logsi.LogAppDomain(SILevel.Verbose)
    _logsi.LogSystem(SILevel.Verbose)

except Exception as ex:

    print(str(ex))
    #_LOGGER.warning("HAS SpotifyPlus could not init SmartInspect debugging! %s", str(ex))

NUM_ENTRIES:int = 80000

import threading
import time

# Function to simulate a task
def print_numbers1():
    for i in range(1, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers 1", i)

# Function to simulate another task
def print_numbers2():
    for i in range(2, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers 2", i)

# Function to simulate another task
def print_numbers3():
    for i in range(1, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers 3", i)

# Function to simulate another task
def print_numbers4():
    for i in range(1, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers 4", i)

# Function to simulate another task
def print_numbers5():
    for i in range(1, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers 5", i)

# Function to simulate another task
def print_numbers6():
    for i in range(1, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers 6", i)

# Function to simulate another task
def print_numbers7():
    for i in range(1, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers 7", i)

# Function to simulate another task
def print_numbers8():
    for i in range(1, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers 8", i)

# Function to simulate another task
def print_numbers9():
    for i in range(1, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers 9", i)

# Create threads
thread1 = threading.Thread(target=print_numbers1, name="thread1")
thread2 = threading.Thread(target=print_numbers2, name="thread2")
thread3 = threading.Thread(target=print_numbers3, name="thread3")
thread4 = threading.Thread(target=print_numbers4, name="thread4")
thread5 = threading.Thread(target=print_numbers5, name="thread5")
thread6 = threading.Thread(target=print_numbers6, name="thread6")
thread7 = threading.Thread(target=print_numbers7, name="thread7")
thread8 = threading.Thread(target=print_numbers8, name="thread8")
thread9 = threading.Thread(target=print_numbers9, name="thread9")

# Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()

# Wait for both threads to complete
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()

SIAuto.Si.Dispose()

print("\nTest Script Ended.")
