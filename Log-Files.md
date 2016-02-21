### Location ###
The location of the log files depends on the OS, but is in Sonarr's AppData directory, you can check the location of the AppData directory on the System Info page.

##### Windows #####
`C:\ProgramData\NzbDrone\logs`

##### Ubuntu #####
`/home/<user>/.config/NzbDrone/logs`

##### OS X #####
`/Users/<user>/.config/NzbDrone/logs`

##### Synology #####
`/usr/local/nzbdrone/var/.config/NzbDrone`

##### QNAP #####
`/share/MD0_DATA/homes/admin/.config/NzbDrone/logs`

### Trace/Debug Logs ###
You can enable Trace or Debug logging in Settings on the General tab. Sonarr does not need to restarted for the change to take effect. This change only effects the log files, not the logging database.

### Clearing Logs ###
You can clear log files and the logs database directly from the UI, under System -> Logs -> Files and System -> Logs respectively.

### Multiple Log Files ###
Sonarr uses rolling log files, each one limited to 1MB in size. The current log file is always `sonarr.txt`, for the the other files `sonarr.0.txt` is the next newest (the higher the number the older it is) up to 6 log files total. This log file contains fatal,error,warn and info entries.   
When Debug log level is enabled, additional `sonarr.debug.txt` rolling log files will be present, up to 51 files. This log files contains fatal,error,warn,info and debug entries. It usually covers a 40h period.   
When Trace log level is enabled, additional `sonarr.trace.txt` rolling log files will be present, up to 51 files. This log files contains fatal,error,warn,info,debug and trace entries. Due to trace verbosity it only covers a couple of hours.