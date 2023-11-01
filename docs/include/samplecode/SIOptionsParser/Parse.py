# package imports.
from smartinspectpython.sioptionsparser import SIOptionsParser
from smartinspectpython.sioptionfoundeventargs import SIOptionFoundEventArgs

print("Test Script Starting.\n")

def AddOption(sender:object, args:SIOptionFoundEventArgs):
    print("Protocol Option Found: {0}".format(str(args)))

# create parser class and wire up events.
parser:SIOptionsParser = SIOptionsParser()
parser.OptionFoundEvent += AddOption

parser.Parse("tcp", 'host=localhost, port=4228, timeout=30000, reconnect=true, reconnect.interval=10s, async.enabled=false')
print("")
parser.Parse("tcp", "host=thlucasi9.netlucas.com,port=4228,timeout=30000")
print("")
parser.Parse("pipe", "pipename=smartinspect,reconnect=true,reconnect.interval=5s,async.enabled=true")
print("")
parser.Parse("file", "filename=\"./tests/logfiles/FileProtocol-RotateHourly.sil\", rotate=hourly, maxparts=24, append=true")
print("")
parser.Parse("file", "filename=\"./tests/logfiles/FileProtocol-ENCRYPTTEST.sil\", encrypt=true, key=\"secret\", rotate=none, append=false")
print("")
parser.Parse("mem", "astext=true, indent=true")
print("")
parser.Parse("mem", "astext=true, indent=true, pattern=\"%level% [%timestamp%]: %title%\"")
print("")
parser.Parse("text", "filename=\"./tests/logfiles/TextProtocol-RotateHourly.txt\", rotate=hourly, maxparts=24, indent=true, pattern=\"%level% [%timestamp%]: %title%\", append=true")
print("")

# unwire events.
parser.OptionFoundEvent -= AddOption

print("/nTest Script Ended.")
