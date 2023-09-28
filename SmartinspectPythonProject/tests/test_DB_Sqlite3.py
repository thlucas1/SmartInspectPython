# add project drectory to python search paths for relative references
import sys
sys.path.append(".")

import sqlite3

# our package imports.
from smartinspectpython.siauto import *

# import classes used for test scenarios.
from testClassDefinitions import SIEventHandlerClass
from testSessionMethods import TestSessionMethods

print("Test Script Starting.")

# wire up smartinspect events.
SIEventHandlerClass.WireEvents(SIAuto.Si)

# set smartinspect connections, and enable logging.
SIAuto.Si.Connections = "tcp(host=192.168.1.1,port=4228,timeout=30000,reconnect=true,reconnect.interval=10s,async.enabled=false)"  # Test Async Mode
SIAuto.Si.Enabled = True

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main

# connect to the database.
conn = sqlite3.connect("./tests/testdata/TestDBSqlite.db")

## execute a query, returning a cursor.
#cursor = conn.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")

# sql to query db for table schema info.
#sql:str = "SELECT * FROM pragma_table_info('{0}');".format("Employees")
#cursor = conn.execute(sql)
#tblSchemaInfo = cursor.fetchall()

# execute a query, returning a cursor.
cursor = conn.execute("SELECT * FROM tracks_view ORDER BY album ASC, name ASC;")
_logsi.LogSqliteDbCursorData(None, None, cursor)
cursor = conn.execute("SELECT * FROM tracks_view WHERE name='xxxxxxx';")
_logsi.LogSqliteDbCursorData(None, "LogSqliteDbCursorData No Data Test", cursor)
cursor = conn.execute("SELECT * FROM MyTestTable2;")
_logsi.LogSqliteDbCursorData(None, "MyTestTable2 Data", cursor)
cursor = conn.execute("SELECT * FROM tracks;")
_logsi.LogSqliteDbCursorData(None, None, cursor)

_logsi.LogSqliteDbSchemaTables(None, conn=conn, sortByName=True)
_logsi.LogSqliteDbSchemaTables(None, conn=conn)

_logsi.LogSqliteDbSchemaIndexList(None, conn=conn, tableName="invoice_items", sortByName=True)
_logsi.LogSqliteDbSchemaIndexList(None, conn=conn, tableName="invoice_items")

_logsi.LogSqliteDbSchemaForeignKeyList(None, conn=conn, tableName="invoice_items", sortByName=True)
_logsi.LogSqliteDbSchemaForeignKeyList(None, conn=conn, tableName="invoice_items")

_logsi.LogSqliteDbSchemaTableInfo(None, conn=conn, tableName="MyTestTable2", sortByName=True)
_logsi.LogSqliteDbSchemaTableInfo(None, conn=conn, tableName="employees")
_logsi.LogSqliteDbSchemaTableInfo(None, "LogSqliteDBTableSchema sorted by Column ID", conn, "employees")
_logsi.LogSqliteDbSchemaTableInfo(None, "LogSqliteDBTableSchema sorted by Column Name", conn, "employees", True)

_logsi.LogObject(None,"Cursor Object", cursor)
_logsi.LogSqliteDbSchemaCursor(None, None, cursor)
_logsi.LogSqliteDbSchemaCursor(None, "LogSqliteCursorSchema Title", cursor)

# close db connection.
conn.close()

# print SI event counts, unwire events, and dispose of SmartInspect.
SIEventHandlerClass.PrintResults(SIAuto.Si)
SIEventHandlerClass.UnWireEvents(SIAuto.Si)
SIAuto.Si.Dispose()

print("Test Script Ended.")
