# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

# our package imports.
from smartinspectpython.siconfiguration import SIConfiguration
from smartinspectpython.sicolor import SIColor

print("Test Script Starting.\n")

config:SIConfiguration = SIConfiguration()
config.Parse("MyKey=MyValue")
print("Key Count=" + str(config.Count))
config.Parse("MyKey2=MyValue")
print("Key Count=" + str(config.Count))

config.LoadFromFile("C:\\Users\\thluc\\source\\repos\\SmartinspectPython\\SmartinspectPythonProject\\tests\\test_configuration.settings.txt")
print("File Key Count=" + str(config.Count))

oCol:SIColor = config.ReadColor("sessiondefaults.color", SIColor.FromArgb(0,1,2,3))
print (oCol)

print("\nTest Script Ended.")
