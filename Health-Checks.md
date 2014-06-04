This page contains a list of health checks errors.
These health checks are periodically performed performed by drone and on certain events. The resulting warnings and errors are listed here to give advice on how to resolve them.

### System warnings ###

#### Mono version is less than 3.2, upgrade for improved stability ####

NzbDrone is written in .Net and requires Mono to run. Versions of 3.2 and above resolved various stability issues we experienced in the past.
Updating to at least version 3.2 is therefore highly recommended.

#### New update is available ####

Rejoice, the developers have released a new update. This generally means awesome new features and squashed piles of bugs (right?).
Apparently you don't have Auto-Updating enabled, so you'll have to figure out how to update on your platform.
Pressing the Install button on the System -> Updates page is probably a good starting point.
But while you're at it, read the change log to find out what the relevant changes were.

_(This warning will not appear if your current version is less than 14 days old)_

#### Unable to update, running from write-protected folder ####

This means NzbDrone will be unable to update itself. You'll have to update drone manually.

### Download Clients ###

#### No download client is available ####

A properly configured and enabled download client is required for NzbDrone to be able to download media.
Since NzbDrone supports different download clients, you should determine which best matches your requirements.
If you already have a download client installed, you should configure NzbDrone to use it and create a category. See Settings -> Download Client.

#### Unable to communicate with download client ####

NzbDrone was unable to communicate with the configured download client. Please verify if the download client is operational and double check the url. This could also indicate an authentication error.

#### Enable Completed Download Handling or configure Drone factory ####

NzbDrone requires Completed Download Handling or a properly configured Drone Factory to be able to import files that were downloaded by the download client. It is recommended to enable Completed Download Handling.

_(Completed Download Handling is enabled by default for new users.)_

### Drone Factory ###

#### Drone factory folder does not exist ####

If you configure NzbDrone to use a Drone Factory the specified folder must exist. Please ensure that it indeed exists, or disable the Drone Factory.

_(You might want to consider using Completed Download Handling since it provides better compatibility for the unpacking and post-processing logic of various download clients.)_

#### Unable to write to drone factory folder ####

You configured NzbDrone to use a Drone Factory, however NzbDrone was unable to creates a test file, this indicates permission issues.
Please verify that the user NzbDrone runs under has the appropriate permissions.

### Completed/Failed Download Handling ###

#### Completed Download Handling is disabled ####

_(This warning is only generated for existing users before when the Completed Download Handling feature was implemented. This feature is disabled by default to ensure the system continued to operate as expected for current configurations.)_

It's recommended to switch to Completed Download Handling since it provides better compatibility for the unpacking and post-processing logic of various download clients.
With it, drone will only import a download once the download client reports it as ready.

If you don't wish to enable Completed Download Handling at all and wants to remove the warning. You can enable and then disable Completed Download Handling. This obviously isn't recommended.

If you wish to enable Completed Download Handling you should verify the following:
* **Warning**: Completed Download Handling only works properly if the download client and NzbDrone are on the same machine since it gets the path to be imported directly from the download client.
* If you added a post-processing script to Sabnzbd/NzbGet to notify NzbDrone that it should scan the Drone Factory. You _SHOULD_ disable this script to prevent conflicts.
* Completed Download Handling and the Drone Factory cannot be configured for the same directory. If Completed Download Handling detects a download resides in the Drone Factory it will be ignored. (again to prevent conflicts)  
   You should reconfigure NzbDrone to use a different Drone Factory Folder or disable it altogether.  
   Alternatively you can change the output folder for the Category, as long as that output folder is not a subdirectory of the Drone Factory Folder.

Both Completed Download Handling and the Drone Factory logic generates Import Events in history while importing files. However, only Completed Download Handling associates this Import event with a Download Client history item.
If Completed Download Handling was enabled recently, your download client may still contain history items that were already imported but do not have a history event with the same unique id.
NzbDrone attempts to resolve this issue automatically, occassionally drone may be unable to make that association and cause a 'Completed' download to be listed in the History -> Queue table forever.
The easiest way to resolve this is to clear your Download Client history, or only those individual items. Alternatively you can rename the category.

#### Download Client has history items in Drone Factory conflicting with Completed Download Handling ####

The Download Client put finished downloads inside the Drone Factory even though Completed Download Handling is configured.
This could potentially cause both Completed Download Handling and the Drone Factory logic to import the same download simultaneously.
To avoid conflicts NzbDrone will ignore those downloads during it's Completed Download Handling logic, leaving it to be handled by the Drone Factory.
This is a suboptimal situation since this effectively disabled Completed Download Handling.

You should configure the Drone Factory to use a different folder.   
_**TODO: Reword**_

### Indexers ###

#### No indexers are enabled ####

NzbDrone requires indexers to be able to discover new releases.
Please read the wiki on instructions how to add indexers.

#### Enabled indexers do not support searching ####

None of the indexers you have enabled support searching. This means NzbDrone will only be able to find new releases via the RSS feeds. But searching for episodes (either Automatic Search or Manual Search) will never return any results.
Obviously, the only way to remedy it is to add another indexer.

### Series Folders ###

#### Missing root folder ####

_**TODO**_
