## Backing up NzbDrone ##

1. Find the location of the AppData directory for NzbDrone
	- Via the WebUI go to System: Info
	- Defaults
		- Windows - C:\ProgramData\NzbDrone
		- Ubuntu - \home\user\\.config\NzbDrone

2. Stop NzbDrone - Not mandatory, but will prevent write locks
3. Copy the contents to a safe location

## Restoring from Backup ##

1. Re-install NzbDrone
2. Run NzbDrone once to get the AppData directory location
3. Stop NzbDrone
4. Delete the contents of the AppData directory (the one created in step 2)
5. Restore from your backup
6. Start NzbDrone
7. As long as the paths are the same, everything will pickup where it left off