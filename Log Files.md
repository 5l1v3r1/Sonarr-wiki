### Location ###
The location of the log files depends on the OS, but is in Sonarr's AppData directory, you can check the location of the AppData directory on the System Info page.

##### Windows #####
`C:\ProgramData\NzbDrone\logs`

##### Ubuntu #####
`/home/<user>/.config/NzbDrone/logs`


### Trace/Debug Logs ###
You can enable Trace or Debug logging in Settings on the General tab. Sonarr does not need to restarted for the change to take effect. This change only effects the log files, not the logging database.


### Clearing Logs ###
You can clear log files and the logs database directly from the UI, under System -> Logs -> Files and System -> Logs respectively.