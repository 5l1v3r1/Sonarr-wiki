## Backing up Sonarr ##

#### Using built-in backup ####

1. Go to System: Backup in the Sonarr UI
2. Click the Backup button
3. Download the zip after the backup is created for safe keeping

#### Using file system directly ####
1. Find the location of the AppData directory for Sonarr
	- Via the Sonarr UI go to System: Info
	- Defaults
		- Windows - 'C:\ProgramData\NzbDrone'
		- OS X - '/Users/\<user\>/.config/NzbDrone'
		- Ubuntu - '/home/\<user\>/.config/NzbDrone'
		- Synology - '/usr/local/nzbdrone/var/.config/NzbDrone'

2. Stop Sonarr - This will prevent the database from being corrupted
3. Copy the contents to a safe location

## Restoring from Backup ##

#### Using zip backup ####

1. Re-install Sonarr
2. Run Sonarr once to get the AppData directory location
3. Stop Sonarr
4. Extract the backup
5. Delete the contents of the AppData directory
6. Restore the files extracted from the zip
7. Start Sonarr
8. As long as the paths are the same, everything will pickup where it left off

#### Using file system backup ####
1. Re-install Sonarr
2. Run Sonarr once to get the AppData directory location
3. Stop Sonarr
4. Delete the contents of the AppData directory
5. Restore from your backup
6. Start Sonarr
7. As long as the paths are the same, everything will pickup where it left off

### Restore for Synology NAS ###
**CAUTION: Restoring on a Synology requires knowledge of Linux and Root SSH access to the Synology Device.**  

1. Re-install Sonarr  
2. Run Sonarr once to get the AppData directory location  
3. Stop Sonarr  
4. Connect to the Synology NAS through SSH and login as root  
5. execute the following commands

    ```
    rm -r /usr/local/nzbdrone/var/.config/NzbDrone/nzbdrone.db-*
    cp -f /tmp/nzbdrone_backup/. /usr/local/nzbdrone/var/.config/NzbDrone/
    ```

6. Start Sonarr  