# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

# our package imports.
#from smartinspectpython.siauto import *
from smartinspectpython.siauto import SIAuto, SILevel, SISession, SIConfigurationTimer, SIColors

print("Test Script Starting.\n")

NUM_ENTRIES:int = 6000

import threading

# Function to simulate a task
def print_numbers():

    # load SmartInspect settings from a configuration settings file.
    siConfigPath: str = "./tests/testdata/smartinspect_encrypted.cfg"
    SIAuto.Si.LoadConfiguration(siConfigPath)

    # start monitoring the configuration file for changes, and reload it when it changes.
    # this will check the file for changes every 60 seconds.
    #siConfig:SIConfigurationTimer = SIConfigurationTimer(SIAuto.Si, siConfigPath)

    # get smartinspect logger reference; create a new session for this module name.
    _logsi:SISession = SIAuto.Si.GetSession(__name__)
    if (_logsi == None):
        _logsi = SIAuto.Si.AddSession(__name__, True)
    _logsi.LogVerbose("siThreadTest - See \"%s\" Watch Counter for results" % threading.current_thread().name)
    _logsi.LogAppDomain(SILevel.Verbose)
    _logsi.LogSystem(SILevel.Verbose)

    for i in range(1, NUM_ENTRIES):
        _logsi.LogValue(SILevel.Debug, "print_numbers - %s" % threading.current_thread().name , i)
        _logsi.IncCounter(SILevel.Debug, threading.current_thread().name)


# Create threads
thread1 = threading.Thread(target=print_numbers, name="siTestThread1")
thread2 = threading.Thread(target=print_numbers, name="siTestThread2")
thread3 = threading.Thread(target=print_numbers, name="siTestThread3")
thread4 = threading.Thread(target=print_numbers, name="siTestThread4")
thread5 = threading.Thread(target=print_numbers, name="siTestThread5")
thread6 = threading.Thread(target=print_numbers, name="siTestThread6")
thread7 = threading.Thread(target=print_numbers, name="siTestThread7")
thread8 = threading.Thread(target=print_numbers, name="siTestThread8")
thread9 = threading.Thread(target=print_numbers, name="siTestThread9")

# # Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()

# # Wait for both threads to complete
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
