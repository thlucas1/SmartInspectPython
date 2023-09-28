# package imports.
from smartinspectpython.siauto import *

# the following are sample SI Connections options for this protocol.

# log messages to SI Console using all default options (pipename=smartinspect).
SIAuto.Si.Connections = "pipe()"

# log messages to SI Console using pipe name "sipipe", with asyncronous send enabled.
SIAuto.Si.Connections = "pipe(pipename=sipipe,reconnect=true,reconnect.interval=10s,async.enabled=true)"
