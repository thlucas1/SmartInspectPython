import os, sys, os.path as path
from inspect import getsourcefile
python_path = os.environ['PYTHONPATH'].split(os.pathsep)
current_working_dir = os.getcwd()
current_absolute_source = path.abspath(getsourcefile(lambda:0))
current_absolute_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
current_absolute_dir_parent = current_absolute_dir[:current_absolute_dir.rfind(path.sep)]
print("Environment Setup (test_configuration_in_src.py):")
print("- PYTHONPATH:      " + os.environ['PYTHONPATH'])
print("- CURRENT_WRK_DIR: " + os.getcwd())
print("- ABSOLUTE_SRC:    " + current_absolute_source)
print("- ABSOLUTE_DIR:    " + current_absolute_dir)
print("- ABSOLUTE_PARENT: " + current_absolute_dir_parent)
print("- SYS.PATH:        " + ';'.join(sys.path))
print("")

#from .smartinspect import *
from .smartinspect.siconfiguration import SIConfiguration
from .smartinspect.sicolor import SIColor

print("Test Script Starting.")

config: SIConfiguration = SIConfiguration()
config.Parse("MyKey=MyValue")
print("Key Count=" + str(config.Count))
config.Parse("MyKey2=MyValue")
print("Key Count=" + str(config.Count))

config.LoadFromFile("C:\\Users\\thluc\\source\\repos\\SmartinspectPython\\SmartinspectPythonProject\\src\\test_configuration.settings")
print("File Key Count=" + str(config.Count))

oCol:SIColor = config.ReadColor("sessiondefaults.color", SIColor.FromArgb(1,2,3))
print (oCol)

print("Test Script Ended.")

