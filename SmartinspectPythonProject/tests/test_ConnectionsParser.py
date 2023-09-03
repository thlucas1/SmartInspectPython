# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

# our package imports.
from smartinspectpython.siconnectionsparser import SIConnectionsParser
from smartinspectpython.siconnectionfoundeventargs import SIConnectionFoundEventArgs

print("Test Script Starting.\n")

def AddConnection(sender: object, args: SIConnectionFoundEventArgs):
    print("Connection Found: {0}".format(str(args)))

# create parser class and wire up events.
parser:SIConnectionsParser = SIConnectionsParser()
parser.ConnectionFoundEvent += AddConnection

parser.Parse("tcp(host=thlucasi9.netlucas.com,port=4228,timeout=30000)")                               # test single protocol
print("")
parser.Parse("tcp(host=thlucasi9.netlucas.com,port=4228,timeout=30000),file(filename=c:\\log.sil,rotate=weekly)")     # test multiple protocols
print("")
#parser.Parse("tcp(host=localhost")     # test missing closed parenthesis
#parser.Parse('tcp(host="localhost")')  # test quoted values
#parser.Parse('tcp(host="localhost"')   # test missing closed parenthesis
#parser.Parse('tcp(host="localhost),file(fileoption1=value)')   # test missing closed quotes
#parser.Parse('pipe()')
parser.Parse('pipe(pipename=smartinspect,reconnect=true,reconnect.interval=5s,async.enabled=true)')
print("")
#parser.Parse('pipe(pipename=smartinspect,reconnect=true,reconnect.interval=5s,async.enabled=false)')
parser.Parse('file(filename=\"./tests/logfiles/FileProtocol-RotateHourlyNoBuffer.sil\", rotate=hourly, maxparts=24, append=true)')
print("")
parser.Parse('file(filename=\"./tests/logfiles/FileProtocol-ENCRYPTTEST.sil\", encrypt=true, key=\"secret\", rotate=none, append=false)')
print("")
parser.Parse('mem(astext=true, indent=true)')
print("")
parser.Parse('mem(astext=true, indent=true, pattern=\"%level% [%timestamp%]: %title%\")')
print("")
parser.Parse('text(filename=\"./tests/logfiles/TextProtocol-RotateHourly.txt\", rotate=hourly, maxparts=24, indent=true, pattern=\"%level% [%timestamp%]: %title%\", append=true)')
print("")

# unwire events.
parser.ConnectionFoundEvent -= AddConnection

print("\nTest Script Ended.")
