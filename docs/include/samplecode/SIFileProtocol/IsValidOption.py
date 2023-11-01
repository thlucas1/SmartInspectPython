# package imports.
from smartinspectpython.siauto import *

# the following are sample SI Connections options for this protocol.

# log messages using all default options ("log.sil", no rotating).
SIAuto.Si.Connections = 'file()'

# log messages (appending) to file 'mylog.sil'.
SIAuto.Si.Connections = "file(filename=\"mylog.sil\", append=true)"

# log messages to rotating default file 'log.sil', that do not 
# exceed 16MB in size.
SIAuto.Si.Connections = "file(maxsize=\"16MB\", maxparts=5)"

# log messages to rotating default file 'log.sil', that creates a new log 
# file every week.  since maxparts is not specified, log files will continue 
# to accumulate and must be manually deleted.
SIAuto.Si.Connections = "file(rotate=weekly)"

# log messages to default file 'log.sil', in an encrypted format with a 
# password of "secret".  when opening the log file in the SI Console, you 
# will be prompted for the passphrase key.
SIAuto.Si.Connections = "file(encrypt=true, key=\"secret\")"
