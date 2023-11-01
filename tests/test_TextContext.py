# add project drectory to python search paths for relative references
import sys
sys.path.append("..")
#sys.path.append(".")

# our package imports.
from smartinspectpython.sitextcontext import SITextContext
from smartinspectpython.siviewerid import SIViewerId

print("Test Script Starting.\n")
print("Testing TextContext methods ...")

tc:SITextContext = SITextContext(SIViewerId.PythonSource)
tc.LoadFromFile("C:\\Users\\thluc\\source\\repos\\SmartinspectPython\\SmartinspectPythonProject\\tests\\test_configuration.py")
tc.AppendLine("This is an Appended Line with no LF or CR at the end.")
tc.AppendLine("This is an Appended Line with LF at the end.\n")
tc.AppendLine("This is an Appended Line with CRLF at the end.\r\n")
tc.AppendText("This is Appended Text line 1.\nThis is Appended Text line 2.\n")
print("SITextContext Data:\n" + str(tc.ViewerData))

data = tc.ViewerData.read()
print("data=" + str(data))

print("\nTest Script Ended.")
