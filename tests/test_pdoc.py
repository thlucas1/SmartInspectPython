# add project drectory to python search paths for relative references
import sys
sys.path.append(".")
sys.path.append("C:\\Users\\thluc\\AppData\\Roaming\\Python\\Python39\\site-packages")

import pdoc
from importlib import util
from smartinspectpython.siauto import *

#from pdoc import doc_pyi, doc_types, render_helpers

#modules = ['siauto', 'color']  # Public submodules are auto-imported
#context = pdoc.Context()

#modules = [pdoc.Module(mod, context=context)
#           for mod in modules]
#pdoc.link_inheritance(context)

#def recursive_htmls(mod):
#    yield mod.name, mod.html()
#    for submod in mod.submodules():
#        yield from recursive_htmls(submod)

#for mod in modules:
#    for module_name, html in recursive_htmls(mod):
#        ...  # Process




if __name__ == "__main__":

    #check to see if nmap module is installed
    find_nmap = util.find_spec("__init__.py")
    if find_nmap is None:
        print("Error")








    doc = pdoc.doc.Module(SIAuto)

    print("doc.get('Main').docstring = " + str(doc.get("Main").docstring))

    # We can override most pdoc doc attributes by just assigning to them.
    doc.get("Main").docstring = "I'm a docstring for Foo.A."

    out = pdoc.render.html_module(module=doc, all_modules={"foo": doc})

    #with open("foo.html", "w") as f:
    #    f.write(out)
