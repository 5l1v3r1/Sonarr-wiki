This page contains a list of health checks errors.
These health checks are periodically performed performed by Sonarr and on certain events. The resulting warnings and errors are listed here to give advice on how to resolve them.

### System warnings ###

#### Mono version is less than 3.2, upgrade for improved stability ####

Sonarr is written in .Net and requires Mono to run. Versions of 3.2 and above resolved various stability issues we experienced in the past.
Updating to at least version 3.2 is therefore highly recommended.

#### New update is available ####

Rejoice, the developers have released a new update. This generally means awesome new features and squashed piles of bugs (right?).
Apparently you don't have Auto-Updating enabled, so you'll have to figure out how to update on your platform.
Pressing the Install button on the System -> Updates page is probably a good starting point.
But while you're at it, read the change log to find out what the relevant changes were.

_(This warning will not appear if your current version is less than 14 days old)_

#### Cannot install update because startup folder is not writable by the user ####

This means Sonarr will be unable to update itself. You'll have to update Sonarr manually or set the permissions on Sonarr's Startup directory (the installation directory) to allow Sonarr to update itself.

#### Updating will not be possible to prevent deleting AppData on Update ####

Sonarr detected that AppData folder for your Operating System is located inside the directory that contains the Sonarr binaries. Normally it would be ```C:\ProgramData``` for Windows and, ```~/.config``` for linux.   
Please look at System -> Info to see the current AppData & Startup directories.

This means Sonarr will be unable to update itself without risking data-loss.

If you're on linux, you'll probably have to change the home directory for the user that is running Sonarr and copy the current contents of the ```~/.config/Sonarr``` directory to preserve your database.

### Download Clients ###

#### No download client is available ####

A properly configured and enabled download client is required for Sonarr to be able to download media.
Since Sonarr supports different download clients, you should determine which best matches your requirements.
If you already have a download client installed, you should configure Sonarr to use it and create a category. See Settings -> Download Client.

#### Unable to communicate with download client ####

Sonarr was unable to communicate with the configured download client. Please verify if the download client is operational and double check the url. This could also indicate an authentication error.

#### Enable Completed Download Handling or configure Drone Factory ####

Sonarr requires Completed Download Handling or a properly configured Drone Factory to be able to import files that were downloaded by the download client. It is recommended to enable Completed Download Handling.

_(Completed Download Handling is enabled by default for new users.)_

### Drone Factory ###

#### Drone Factory folder does not exist ####

If you configure Sonarr to use a Drone Factory the specified folder must exist. Please ensure that it indeed exists, or disable the Drone Factory.

_(You might want to consider using Completed Download Handling since it provides better compatibility for the unpacking and post-processing logic of various download clients.)_

#### Unable to write to Drone Factory folder ####

You configured Sonarr to use a Drone Factory, however Sonarr was unable to creates a test file, this indicates permission issues.
Please verify that the user Sonarr runs under has the appropriate permissions.

### Completed/Failed Download Handling ###

#### Completed Download Handling is disabled ####

_(This warning is only generated for existing users before when the Completed Download Handling feature was implemented. This feature is disabled by default to ensure the system continued to operate as expected for current configurations.)_

It's recommended to switch to Completed Download Handling since it provides better compatibility for the unpacking and post-processing logic of various download clients.
With it, Sonarr will only import a download once the download client reports it as ready.

If you don't wish to enable Completed Download Handling at all and wants to remove the warning. You can enable and then disable Completed Download Handling. This obviously isn't recommended.

If you wish to enable Completed Download Handling you should verify the following:
* **Warning**: Completed Download Handling only works properly if the download client and Sonarr are on the same machine since it gets the path to be imported directly from the download client.
* If you added a post-processing script to Sabnzbd/NzbGet to notify Sonarr that it should scan the Drone Factory. You _SHOULD_ disable this script to prevent conflicts.
* Completed Download Handling and the Drone Factory cannot be configured for the same directory. If Completed Download Handling detects a download resides in the Drone Factory it will be ignored. (again to prevent conflicts)  
   You should reconfigure Sonarr to use a different Drone Factory Folder or disable it altogether.  
   Alternatively you can change the output folder for the Category, as long as that output folder is not a subdirectory of the Drone Factory Folder.

Both Completed Download Handling and the Drone Factory logic generates Import Events in history while importing files. However, only Completed Download Handling associates this Import event with a Download Client history item.
If Completed Download Handling was enabled recently, your download client may still contain history items that were already imported but do not have a history event with the same unique id.
Sonarr attempts to resolve this issue automatically, occassionally Sonarr may be unable to make that association and cause a 'Completed' download to be listed in the History -> Queue table forever.
The easiest way to resolve this is to clear your Download Client history, or only those individual items. Alternatively you can rename the category.

#### Download Client has history items in Drone Factory conflicting with Completed Download Handling ####

The Download Client put finished downloads inside the Drone Factory even though Completed Download Handling is configured.
This could potentially cause both Completed Download Handling and the Drone Factory logic to import the same download simultaneously.
To avoid conflicts Sonarr will ignore those downloads during it's Completed Download Handling logic, leaving it to be handled by the Drone Factory.
This is a suboptimal situation since this effectively disabled Completed Download Handling.

Resolution: Configure the Drone Factory to use a different folder.

_**TODO: Reword**_

### Indexers ###

#### No indexers are enabled ####

Sonarr requires indexers to be able to discover new releases.
Please read the wiki on instructions how to add indexers.

#### Enabled indexers do not support searching ####

None of the indexers you have enabled support searching. This means Sonarr will only be able to find new releases via the RSS feeds. But searching for episodes (either Automatic Search or Manual Search) will never return any results.
Obviously, the only way to remedy it is to add another indexer.

#### Indexers are unavailable due to failures ####

Errors occurs while Sonarr tried to use one of your indexers. To limit retries, Sonarr will not use the indexer for an increasing amount of time (up to 24h).   
This mechanism is triggered if Sonarr was unable to get a response from the indexer (could be dns, connection, authentication or indexer issue), or unable to fetch the nzb/torrent file from the indexer. Please inspect the logs to determine what kind of error causes the problem.   

You can prevent the warning by disabling the affected indexer.

Run the Test on the indexer to force Sonarr to recheck the indexer, please note that the Health Check warning will not always disappear immediately.

### Series Folders ###

#### Missing root folder ####

_**TODO**_

This message may appear if a previous root folder is no longer used. To remove old root folders:

1. Begin adding a new Series by searching for a name, but do not submit
2. In the 'Path' dropdown, select 'Add a different path'
3. Click the cross at the end of a row to remove the unused path 

The message will continue to appear until all series have their root folder updated to the new root folder. To change the root folder for other series, visit the series editor.