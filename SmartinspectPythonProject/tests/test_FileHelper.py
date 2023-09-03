# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

from datetime import datetime

# our package imports.
from smartinspectpython.sifilehelper import SIFileHelper

print("Test Script Starting.\n")

# test begin
print("Testing SIFileHelper methods ...")
#fileDate:datetime = SIFileHelper.GetFileDate("C:\\logfile-hourly.txt", "C:\\logfile-hourly-2023-05-22-00-49-55.txt")
fileDate:datetime = SIFileHelper.GetFileDate("C:\\logfile-hourly.txt", "C:\\logfile-hourly-2023-05-22-00-49-55.txt")
print("C:\\logfile-hourly-2023-05-22-00-49-55.txt - Log Date={0}".format(fileDate))
#fileDateBad:datetime = SIFileHelper.GetFileDate("C:\\logfile-hourly.txt", "C:\\logfile-hourly-2023-A5-22-00-49-55.txt")
#files1:list[str] = SIFileHelper.__GetFiles("C:\\C3\\v11\\Source\\C3.Diagnostics\\TestResults\\C3.Diagnostics.TestCS-TextProtocol-RotateHourly.txt")
#firstlogfile:str = SIFileHelper.__FindFileName("C:\\C3\\v11\\Source\\C3.Diagnostics\\TestResults\\C3.Diagnostics.TestCS-TextProtocol-RotateHourly.txt")
#newlogfile:str = SIFileHelper.__ExpandFileName("C:\\C3\\v11\\Source\\C3.Diagnostics\\TestResults\\C3.Diagnostics.TestCS-TextProtocol-RotateHourly.txt")
# test end

print("\nTest Script Ended.")
