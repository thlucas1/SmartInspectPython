# package imports.
from smartinspectpython.siutils import Event

# Define the class that will be raising events:
class MyFileWatcher:
    def __init__(self):
        self.fileChanged = Event()      # define event

    def watchFiles(self):
        source_path = "foo"
        self.fileChanged(source_path)   # fire event

def log_file_change(source_path):       # event handler 1
    print("%r changed." % (source_path,))

def log_file_change2(source_path):      # event handler 2
    print("%r changed!" % (source_path,))

# Define the code that will be handling raised events.
watcher              = MyFileWatcher()
watcher.fileChanged += log_file_change2
watcher.fileChanged += log_file_change
watcher.fileChanged -= log_file_change2
watcher.watchFiles()
