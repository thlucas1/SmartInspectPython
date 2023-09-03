# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

import inspect

# import classes used for test scenarios.
from testClassDefinitions import InstanceGetMembersTestClass

def PrintInstanceData(title:str, data, excludeBuiltIns:bool=False, excludeInternals:bool=True) -> None:
    """ 
    Prints inspect.getmember data.
    """
    print('\n###############################################################################')
    print(title + ':')
    for name, data in data:
        if (excludeBuiltIns) and (str(data).find('<built-in method') != -1):
            continue
        if (excludeInternals) and (name.startswith('__')):
            continue
        print(' - %s :' % name, repr(data))


print("Test Script Starting.")

# good reference doc on inspect.getmembers:
#   http://pymotw.com/2/inspect/

oInstance:InstanceGetMembersTestClass = InstanceGetMembersTestClass("parm string value", True)

# return ALL methods and properties of the class:
rsltAll = inspect.getmembers(oInstance, None)
PrintInstanceData("All", rsltAll)
PrintInstanceData("All (exclude builtins)", rsltAll, True)

# return only methods of the class:
#rsltMethods = inspect.getmembers(oInstance, predicate=inspect.ismethod)
#PrintInstanceData("rsltMethods", rsltMethods)

# other types of returned info:
PrintInstanceData("isfunction", inspect.getmembers(oInstance, predicate=inspect.isfunction))       # functions (appears to be @staticmethod only items)
PrintInstanceData("ismethod  ", inspect.getmembers(oInstance, predicate=inspect.ismethod))         # methods (methods, but no @staticmethod items)
PrintInstanceData("isroutine ", inspect.getmembers(oInstance, predicate=inspect.isroutine))        # combination if isfunction and ismethod items  ** use for Methods reflection!
PrintInstanceData("isabstract", inspect.getmembers(oInstance, predicate=inspect.isabstract))       # abstract base classes
PrintInstanceData("isclass   ", inspect.getmembers(oInstance, predicate=inspect.isclass))          # classes
PrintInstanceData("isbuiltin ", inspect.getmembers(oInstance, predicate=inspect.isbuiltin))        # builtin function or method
PrintInstanceData("iscode    ", inspect.getmembers(oInstance, predicate=inspect.iscode))           # code objects
PrintInstanceData("ismodule  ", inspect.getmembers(oInstance, predicate=inspect.ismodule))         # module objects
PrintInstanceData("isgetset  ", inspect.getmembers(oInstance, predicate=inspect.isgetsetdescriptor))    # getset descriptors

properties = inspect.getmembers(type(oInstance), lambda o: isinstance(o, property)) # get all properties decorated with "@property"
PrintInstanceData("Properties", properties)

methods = inspect.getmembers(oInstance, inspect.ismethod)                           # get all public and private methods ()
PrintInstanceData("Methods", methods)

print("Test Script Ended.")
