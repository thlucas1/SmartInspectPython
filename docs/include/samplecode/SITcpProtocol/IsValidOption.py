# package imports.
from smartinspectpython.siauto import *

# the following are sample SI Connections options for this protocol.

# log messages using all default options (localhost, port 4228, 30s timeout).
SIAuto.Si.Connections = "tcp()"

# log messages using localhost, port 4228, 30s timeout, asynchronous processing.
SIAuto.Si.Connections = "tcp(host=localhost,port=4228,timeout=30000,reconnect=true,reconnect.interval=10s,async.enabled=true)"

# log messages using another server, port 4228, 30s timeout, asynchronous processing.
SIAuto.Si.Connections = "tcp(host=myserver.example.com,port=4228,timeout=30000,reconnect=true,reconnect.interval=10s,async.enabled=true)"
