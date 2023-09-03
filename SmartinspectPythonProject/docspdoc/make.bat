@echo off
echo Build PDoc Documentation Script starting.

rem set python path so source files can be found.
set PYTHONPATH=C:\Users\thluc\source\repos\SmartinspectPython\SmartinspectPythonProject\;C:\Users\thluc\source\repos\SmartinspectPython\SmartinspectPythonProject\smartinspectpython


echo Changing working directory to package docspdoc folder.
cd C:\Users\thluc\source\repos\SmartinspectPython\SmartinspectPythonProject\docspdoc


echo Setting build environment variables via buildEnv.py ...
FOR /F "delims=|" %%G IN ('"python.exe .\buildEnv.py"') DO SET "%%G"
echo.
echo Build Environment variables ...
echo - BUILDENV_PACKAGENAME = %BUILDENV_PACKAGENAME%
echo - BUILDENV_PACKAGEVERSION = %BUILDENV_PACKAGEVERSION%
echo - BUILDENV_PDOC_BRAND_ICON_URL = %BUILDENV_PDOC_BRAND_ICON_URL%
echo - BUILDENV_PDOC_BRAND_ICON_URL_SRC = %BUILDENV_PDOC_BRAND_ICON_URL_SRC%
echo - BUILDENV_PDOC_BRAND_ICON_URL_TITLE = %BUILDENV_PDOC_BRAND_ICON_URL_TITLE%


echo Cleaning up the PDoc Documentation output folder.
del /Q .\build\smartinspectpython\*.*
del /Q .\build\*.*


echo Copying include files to PDoc output folder.
mkdir .\build\smartinspectpython
copy .\include\*.js .\build
copy .\include\*.ico .\build
copy .\include\*.ico .\build\smartinspectpython


echo Changing working directory to package source folder.
cd C:\Users\thluc\source\repos\SmartinspectPython\SmartinspectPythonProject\smartinspectpython


echo Building PDoc Documentation ...
rem can also add custom footer text with this option:  --footer-text "This is some footer text" 
echo.
pdoc -o ..\docspdoc\build -d google --no-show-source --no-math --no-mermaid --search -t ..\docspdoc\templates\darkmode __init__ siargumentnullexception.py siargumentoutofrangeexception.py siauto.py sibinarycontext.py sibinaryformatter.py sibinaryviewercontext.py sicolor.py siconfiguration.py siconfigurationtimer.py siconnectionfoundeventargs.py siconnectionsbuilder.py siconnectionsparser.py siconst.py sicontrolcommand.py sicontrolcommandeventargs.py sicontrolcommandtype.py sicryptostreamwriter.py sidataviewercontext.py sienumcomparable.py sierroreventargs.py sifilehelper.py sifileprotocol.py sifilerotate.py sifilerotater.py sifiltereventargs.py siformatter.py sigraphicid.py sigraphicviewercontext.py siinfoeventargs.py siinspectorviewercontext.py siinvalidconnectionsexception.py silevel.py silistviewercontext.py siloadconfigurationexception.py siloadconnectionsexception.py silogentry.py silogentryeventargs.py silogentrytype.py silogheader.py silookuptable.py simemoryprotocol.py siobjectrenderer.py sioptionfoundeventargs.py sioptionsparser.py sipacket.py sipacketqueue.py sipacketqueueitem.py sipackettype.py sipatternparser.py sipipehandle.py sipipeprotocol.py sipipestream.py siprocessflow.py siprocessfloweventargs.py siprocessflowtype.py siprotocol.py siprotocolcommand.py siprotocolexception.py siprotocolfactory.py siprotocolvariables.py sischeduler.py sischeduleraction.py sischedulercommand.py sischedulerqueue.py sischedulerqueueitem.py sisession.py sisessiondefaults.py sisessionmanager.py sisourceid.py sisourceviewercontext.py sitableviewercontext.py sitcpprotocol.py sitextcontext.py sitextformatter.py sitextprotocol.py sitoken.py sitokenfactory.py siutils.py sivaluelistviewercontext.py siviewercontext.py siviewerid.py siwatch.py siwatcheventargs.py siwatchtype.py siwebviewercontext.py smartinspect.py smartinspectexception.py 


echo.
echo Changing working directory to package project folder.
cd C:\Users\thluc\source\repos\SmartinspectPython\SmartinspectPythonProject


echo Build PDoc Documentation Script completed.
