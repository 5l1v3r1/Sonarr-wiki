## Backing up NzbDrone ##

#### Using built-in backup ####

1. Go to System: Backup in the drone UI
2. Click the Backup button
3. Download the zip after the backup is created for safe keeping

#### Using file system directly ####
1. Find the location of the AppData directory for NzbDrone
	- Via the drone UI go to System: Info
	- Defaults
		- Windows - C:\ProgramData\NzbDrone
		- Ubuntu - \home\user\\.config\NzbDrone

2. Stop NzbDrone - This will prevent the database from being corrupted
3. Copy the contents to a safe location

## Restoring from Backup ##

#### Using zip backup ####

1. Re-install NzbDrone
2. Run NzbDrone once to get the AppData directory location
3. Stop NzbDrone
4. Extract the backup
5. Delete the contents of the AppData directory
6. Restore the files extracted from the zip
7. Start NzbDrone
8. As long as the paths are the same, everything will pickup where it left off

#### Using file system backup ####
1. Re-install NzbDrone
2. Run NzbDrone once to get the AppData directory location
3. Stop NzbDrone
4. Delete the contents of the AppData directory
5. Restore from your backup
6. Start NzbDrone
7. As long as the paths are the same, everything will pickup where it left off