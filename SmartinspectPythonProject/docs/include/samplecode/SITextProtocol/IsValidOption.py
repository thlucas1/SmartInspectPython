# package imports.
from smartinspectpython.siauto import *

# the following are sample SI Connections options for this protocol.

# log messages using all default options ("log.sil", no indent).
SIAuto.Si.Connections = "text()"

# log messages using all default options ("log.sil", no indent).
SIAuto.Si.Connections = "text(filename=\"log.txt\")"

# log messages (appending) to file 'mylog.txt'.
SIAuto.Si.Connections = "text(filename=\"mylog.txt\", append=true)"

# log messages to rotating log file 'mylog.txt', that creates a new log 
# file every week.  since maxparts is not specified, log files will continue 
# to accumulate and must be manually deleted.
SIAuto.Si.Connections = "text(filename=\"mylog.txt\", append=true, rotate=weekly"

# log messages to rotating log file 'mylog.txt', that creates a new log 
# file every week; keep only 7 log files, automatically deleting outdated files.
SIAuto.Si.Connections = "text(filename=\"mylog.txt\", append=true, rotate=weekly, maxparts=7)"

# log messages to file "mylog.txt" using a custom pattern.
SIAuto.Si.Connections = "text(filename=\"mylog.txt\", append=true, pattern=\"%level% [%timestamp%]: %title%\")"

# log messages to rotating default file 'mylog.txt', that do not 
# exceed 16MB in size.
SIAuto.Si.Connections = "text(maxsize=\"16MB\")"
