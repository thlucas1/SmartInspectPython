<h1 class="modulename">
SmartInspect Python3 Library
</h1>

# Overview
This API provides Python code execution tracing and diagnostics support via the SmartInspect library.
More information on SmartInspect can be found here: <a href="https://code-partners.com/offerings/smartinspect/" target="_blank">https://code-partners.com/offerings/smartinspect/</a>

Warning: Enabling diagnostics tracing could significantly impact application performance, depending on the logging level.
For example, a DEBUG logging level will generate a significant amount of trace data compared to an ERROR logging level.

Diagnostic data can be captured in various ways: Real-Time Console, File, Memory, or Text.  Diagnostic data is buffered in a message list, and sent by a separate worker thread.  This approach ensures that performance impact of the diagnosed application is minimal while diagnostics are enabled.
          
Diagnostics tracing options can be set via an application configuration settings file.

The Real-Time Console method of sending diagnostic data is the ideal way to diagnose applications that utilize services, such as ASP.NET or Windows Services.  For real-time monitoring, diagnostics trace data is sent from your application to the SmartInspect Console viewer over the TCP/IP network.  The SmartInspect Console can be started on the same machine where your application is running, or on a different machine that is accessible via the TCP/IP network.

# Documentation
* Documentation is located in the package library under the 'docs' folder; use the index.html as your starting point. 

# Requirements
* Python 3.4 or greater (not tested with Python 2).
* pycryptodome package - used for log file encryption support.
* pywin32 package - for named-pipe support (Windows platform only - use `pip install pywin32` to install manually).

# Dependencies
* SmartInspect Redistributable Console, Version 3.3+.

    The Console Viewer is required to view SmartInspect Log (.sil) formatted files, as well capture packets via the SITcpProtocol or SIPipeProtocol connections. 
    The Console Viewer (aka Redistributable Console) can be downloaded here: <a href="https://code-partners.com/offerings/smartinspect/releases/" target="_blank">https://code-partners.com/offerings/smartinspect/releases/</a>

# Quick-Start Sample Code

The following code snippets will get you started with establishing a connection to a logging Console or file.
Please refer to the `smartinspectpython.sisession.SISession` class for all of the various "Logx" methods to log data.

<em>Example 1 - Logging via tcp to a running SmartInspect Console on localhost</em>
``` python
# our package imports.
from smartinspectpython.siauto import *

# set smartinspect connections, and enable logging.
SIAuto.Si.Connections = "tcp(host=localhost,port=4228,timeout=5000)"
SIAuto.Si.Enabled = True    # enable logging

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main
_logsi.Level = SILevel.Debug   # set Message level logging

# log some test messages.
_logsi.LogSystem(SILevel.Debug, "System Information on application startup")
_logsi.LogMessage("Hello World has started")
```
<br/>

<em>Example 2 - Logging to rotating hourly log files in SmartInspect Console format</em>
``` python
# our package imports.
from smartinspectpython.siauto import *

# set smartinspect connections, and enable logging.
# this will keep 24 log files, that rotate every hour.
SIAuto.Si.Connections = "file(filename=\".\\logfiles\\AppLog.sil\", rotate=hourly, maxparts=24, append=true)"
SIAuto.Si.Enabled = True    # enable logging

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main
_logsi.Level = SILevel.Debug   # set Message level logging

# log some test messages.
_logsi.LogSystem(SILevel.Debug, "System Information on application startup")
_logsi.LogMessage("Hello World has started")
```
<br/>

<em>Example 3 - Logging to rotating hourly log files in Plain Text format</em>
``` python
# our package imports.
from smartinspectpython.siauto import *

# set smartinspect connections, and enable logging.
# this will keep 24 log files, that rotate every hour.
SIAuto.Si.Connections = "text(filename=\".\\logfiles\\AppLog.txt\", rotate=hourly, maxparts=24, append=true)"
SIAuto.Si.Enabled = True    # enable logging

# get smartinspect logger reference.
_logsi:SISession = SIAuto.Main
_logsi.Level = SILevel.Debug   # set Message level logging

# log some test messages.
_logsi.LogSystem(SILevel.Debug, "System Information on application startup")
_logsi.LogMessage("Hello World has started")
```

# Licensing
This project is licensed under the terms of the MIT End-User License Agreement (EULA) license.
