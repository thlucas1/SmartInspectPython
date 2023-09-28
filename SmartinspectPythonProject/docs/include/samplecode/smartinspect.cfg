; smartinspect.cfg

; SmartInspect Logging Configuration General settings.
; - "Enabled" parameter to turn logging on (True) or off (False).
; - "Level" parameter to control the logging level (Debug|Verbose|Message|Warning|Error).
; - "AppName" parameter to control the application name.
Enabled = False 
Level = Verbose
DefaultLevel = Debug
AppName = My Application Name

; SmartInspect Logging Configuration Output settings.
; - Log to SmartInspect Console Viewer running on the specified network address.
Connections = tcp(host=localhost, port=4228, timeout=5000, reconnect=true, reconnect.interval=10s, async.enabled=true)
; - Log to a file:
;Connections = "file(filename=\"./tests/logfiles/logfile.log\", rotate=hourly, maxparts=24, append=true)"
; - Log to an encrypted file:
;Connections = "file(filename=\"./tests/logfiles/logfileEncrypted.sil\", encrypt=true, key=""1234567890123456"", rotate=hourly, maxparts=14, append=true)"
        
; set defaults for new sessions
; note that session defaults do not apply to the SIAuto.Main session, since
; this session was already added before a configuration file can be loaded. 
; session defaults only apply to newly added sessions and do not affect existing sessions.
SessionDefaults.Active = True
SessionDefaults.Level = Message
SessionDefaults.ColorBG = 0xFFFFFF

; configure some individual session properties.
; note that this does not add the session to the sessionmanager; it simply
; sets the property values IF the session name already exists.
Session.Main.Active = True
Session.Main.ColorBG = 0xFFFFFF
