# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

# external package imports.
import logging
import logging.handlers
import os

# our package imports.
from smartinspectpython.siauto import *

# import classes used for test scenarios.
from testClassDefinitions import SIEventHandlerClass
from testSessionMethods import TestSessionMethods

# data used by various tests.
exedir = os.path.dirname(sys.argv[0])
testdataPfx:str = exedir + "/testdata/"
logfilePath:str = exedir + "/logfiles/"
argsVar1:str="Argument 1 Value"
argsVar2:int=1000

# wire up smartinspect events.
SIEventHandlerClass.WireEvents(SIAuto.Si)

# set smartinspect connections, and enable logging.
SIAuto.Si.Connections = "tcp(host=localhost,port=4228,timeout=30000)"
SIAuto.Si.Enabled = True

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main

for level in SILevel:

    if (level == SILevel.Control):
        continue

    # reset counters for next test.
    SIEventHandlerClass.ResetCounters(_logsi.Parent)
    
    # get system logging level based on smartinspect logging level.
    # NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40, CRITICAL=50
    sysLoglevel:str = level.name.upper()
    if level == SILevel.Fatal:
        sysLoglevel = "CRITICAL"
    elif level == SILevel.Message:
        sysLoglevel = "INFO"
    elif level == SILevel.Verbose:
        sysLoglevel = "DEBUG"
    elif level == SILevel.Warning:
        sysLoglevel = "WARN"

    # configure system logging (to file).
    handler = logging.handlers.WatchedFileHandler(logfilePath+"test_SystemLogger_Output_{0}.log".format(level.name))
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    handler.setFormatter(formatter)
    _LOGGER = logging.getLogger()
    _LOGGER.setLevel(sysLoglevel)
    _LOGGER.addHandler(handler)

    # add system logging to smartinspect logger.
    _logsi.SystemLogger = _LOGGER

    # test all session methods, using specified logging level.
    # note that we will just change the Parent.Level value for this.
    # the Parent.Default and SISession.Level are set to Debug, in the
    # event that configuration file contains other values.  this
    # makes for a 1-to-1 comparison between level test runs.
    _logsi.Parent.Level = level
    _logsi.Parent.DefaultLevel = SILevel.Debug
    _logsi.Level = SILevel.Debug
    TestSessionMethods.TestAllMethods(_logsi)

    # print SI event counts.
    SIEventHandlerClass.PrintResults(_logsi.Parent)

    print("Test was Successful!")

# print SI event counts, unwire events, and dispose of SmartInspect.
SIEventHandlerClass.PrintResults(SIAuto.Si)
SIEventHandlerClass.UnWireEvents(SIAuto.Si)
SIAuto.Si.Dispose()
