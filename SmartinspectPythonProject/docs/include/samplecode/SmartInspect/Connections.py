# package imports.
from smartinspectpython.siauto import *

# log messages to default file 'log.sil'.
SIAuto.Si.Connections = 'file()'

# log messages to file 'mylog.sil'.
SIAuto.Si.Connections = "file(filename=""mylog.sil"", append=true)"

# log messages to default file "log.sil", as well as to the SmartInspect 
# Console viewer running on localhost.
SIAuto.Si.Connections = "file(append=true), tcp(host=""localhost"")"

# log messages to default file "log.sil", as well as to file "anotherlog.sil".
SIAuto.Si.Connections = "file(), file(filename=""anotherlog.sil"")"
