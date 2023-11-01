# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

# our package imports.
from smartinspectpython.sitokenfactory import SITokenFactory
from smartinspectpython.sitoken import SIToken

print("Test Script Starting.\n")

token1:SIToken = SITokenFactory.GetToken("%session%")
print("token1 = {0}".format(str(token1)))
token2:SIToken = SITokenFactory.GetToken("%timestamp{HH:mm:ss.fff}%")
print("token2 = {0}".format(str(token2)))
token3:SIToken = SITokenFactory.GetToken("%level,8%")
print("token3 = {0}".format(str(token3)))
token4:SIToken = SITokenFactory.GetToken("%title%")  # indent=true
print("token4 = {0}".format(str(token4)))

print("\nTest Script Ended.")
