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
Sonarr uses rolling log files, each one limited to 1MB in size. The current log file is always `nzbdrone.txt`, for the the other files `nzbdrone.0.txt` is the next newest (the higher the number the older it is). When Info logging is enabled (default) there will be 6 log files in total, when debug or trace logging is enabled there will be 51 files.