# package imports.
from smartinspectpython.siauto import *

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main

# log messsages.
_logsi.LogFatal("This is a fatal error message in regular background color.")
_logsi.LogFatal("This is a fatal error message in RED background color.", SIColors.Red)
