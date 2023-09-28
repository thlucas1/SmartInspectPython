# package imports.
from smartinspectpython.siauto import *

# the following are sample SI Connections options for this protocol.

# log messages using all default options (binary log, no indent).
SIAuto.Si.Connections = "mem()"

# log messages using max packet queue size of 8 MB.
SIAuto.Si.Connections = "mem(maxsize=\"8MB\")"

# log messages using text instead of binary.
SIAuto.Si.Connections = "mem(astext=true)"

# log messages using indented text and a custom pattern.
SIAuto.Si.Connections = "mem(astext=true, indent=true, pattern=\"%level% [%timestamp%]: %title%\")"
