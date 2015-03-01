### Does Sonarr require a SABnzbd post-processing script to import downloaded episodes?  ###
No. As long as you set the Drone Factory path `Settings > Download Client > Drone Factory` to the folder where sab downloads your TV Shows everything will be imported automatically. [[Sorting and Renaming]]

### How does Sonarr find episodes?  ###
Sonarr doesn't actively search for any episodes on its own, it uses the indexer's latest releases to find recently posted episodes. Typically the indexer returns the last 100 releases, which isn't much, so be wary if you shut your system down for an extended period of time you might miss some newly release episodes. also, sometimes older episodes are re-posted and might get downloaded if you haven't ignored them. Missing episodes are not actively searched for (missing is anything that aired prior to the current time), unless that episode has not yet been posted (aired recently) or is re-posted you will need to manually search for them. If Sonarr is shut down for a period of time (more than 1 hour), it will attempt to search for recently aired episodes that have not been grabbed or imported yet, this is the only case where Sonarr will search for a missing episode without user interaction.

### Why can't Sonarr see my files on a remote server?  ###
This can be for various reasons, but the most common is, Sonarr is running as a service, which causes one of two things:

1.  Sonarr runs under the SYSTEM account by default which doesn't have access to protected remote file shares.
	
	**Solutions:**
	- Run Sonarr's service as another user that has access to that share [How to change a service's user account](http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/sys_srv_logon_user.mspx?mfr=true)
	- Run NzbDrone.exe using the Startup Folder
	


2. You're using a mapped network drive (not a UNC path)
	
	**Solutions:**
	- Change your paths to UNC paths (\\\\server\share)
	- Run NzbDrone.exe via the Startup Folder 


### How does Sonarr handle scene numbering issues (American Dad!, etc)? ###
Sonarr relies on [TheXEM](TheXEM "http://thexem.de/"), a community driven site that lets users create mappings of shows that the scene (the people that post the files) and TheTVDB (which typically follows the network's numbering). There are a number of shows on there already, but its easy to add another and typically the changes are accepted within a couple days (if they're correct).

### Why can't Sonarr import episode files for series X? / Why can't Sonarr find releases for series X? ###
Sonarr relies on being able to match titles, often the scene posts episodes using different titles, eg *CSI: Crime Scene Investigation* as just *CSI* so Sonarr can't match the names without some help. Sonarr maintains a list of problematic series which lets us solve this issue. To request a new mapping:

1. Make sure it hasn't already been requested. [Requested Mappings](https://docs.google.com/spreadsheet/ccc?key=0Atcf2VZ47O8tdGdQN1ZTbjFRanhFSTBlU0xhbzhuMGc#gid=0) 
2. Make a new request here: [Scene Mapping Request Form]( https://docs.google.com/forms/d/15S6FKZf5dDXOThH4Gkp3QCNtS9Q-AmxIiOpEBJJxi-o/viewform)

*Typically these are added within 1-2 days*

### Sonarr grabbed a release, why can't it import it? ###
The reason it was able to grab the release in the first place was because the indexer returned the tv rage ID for the series and Sonarr was able to match it to that, but that ID is not available during import, so it fails.

### I see that feature/bug X was fixed, why can't I see it?  ###
Sonarr consists of two main branches of code, master and develop, master is released periodically, when the develop branch is stable and develop is for pre-release testing and people willing to live on the edge, if you want to help out testing or want more information on the two branches, please see: [[Release-Branches]]
When a feature is marked as In Develop it will only be available to users running the develop branch, once its been move to Live (in master) it is officially released.

### Episode Progress - How is it calculated?  ###
There are two parts to the episode count, one being the number of episodes (Episode Count) and the other being the number of episodes with files (Episode File Count), each one uses slightly different logic to give you the overall progress for a series or season.

- Episode Count
	- Episode has already aired AND is monitored OR
	- Episode has a file
- Episode File Count
	- Episode has a file

If a series has 10 episodes that have all aired and you don't have any files for them you would have 0/10 episodes, if you unmonitored all the episodes in that series you would have 0/0 and if you got all the episodes for that series, regardless of if the episodes are monitored or not, you would have 10/10 episodes.

### I got a pop-up that said config.xml was corrupt, what now?  ###
Sonarr was unable to read your config file on start-up as it became corrupted somehow. In order to get Sonarr back online, you will need to delete `C:\ProgramData\Sonarr\Config.xml` (Windows), once deleted start Sonarr and it will start on the default port (8989), you should now re-configure any settings you configured on the General Settings page.

### How do I access Sonarr from another computer?  ###
By default Sonarr doesn't listen to requests from all systems (when not run as administrator), it will only listen on localhost, this is due to how the Web Server Sonarr uses integrates with Windows (this also applies for current alternatives). If Sonarr is run as an administrator it will correctly register itself with Windows as well as open the Firewall port so it can be accessed from other systems on your network. Running as admin only needs to happen once (if you change the port it will need to be re-run).

### Why doesn't Sonarr automatically search for missing episodes? ###
There are two times when we would want to have missing episodes searched for, when a new series with existing aired episodes is added and when Sonarr has been offline and unable to find episodes as it normally would. Endlessly searching for episodes that have aired that are missing is a waste of resources, both in terms of local processing power and on the indexers and in our experience catches users off guard, wasting bandwidth.

In v1 of Sonarr we had an opt in backlog search option, often people would turn it on and then get a bunch of old episodes and ask us why, we also had indexers ask why they saw an increase in API calls, which was due to the backlog searching.

In v2 we sat back and thought about it and realized the benefit is not really there, we could try to throttle the searching, but that just draws it out and still does the same thing; hammer the indexer with useless requests. If the episode wasn't there the last time the search was performed, why would it be there now? It would be if it was reposted, but if it was reposted, the automatic process that gets new episodes would see it was posted and act on it.

### I am getting an error: Invalid Newznab URL entered. ###
First make sure you're using the correct URL (with https if applicable), such as: `http://indexer.com`, not `https://indexer.com/api`. If you're still having issues please see [[Newznab]]

### I am getting an error: Database disk image is malformed. ###
This means your sqlite database that stores most of the information for Sonarr is corrupt. There is an excellent guide here to copy the contents from the corrupt database into a new one: http://techblog.dorogin.com/2011/05/sqliteexception-database-disk-image-is.html

### Why does Sonarr refresh series information so frequently? ###

Sonarr refreshes series and episode information in addition to rescanning the disk for files every 12 hours. This might seem aggressive, but is a very important process. The data refresh from trakt is important, because new episode information is synced down, air dates, number of episodes, status (continuing/ended). Even shows that aren't airing are being updated with new information.

The disk scan is less important, but is used to check for new files that weren't sorted by Sonarr and detect deleted files.

The most time consuming portion is the information refresh (assuming reasonable disk access speed), larger shows take longer due to the number of episodes to process.

### Why is there a number above Activity? ###

This number shows the count of episodes in your download client's queue and the last 30 items in its history that have not yet been imported. If the number is blue it is operating normally and should import episodes when they complete. Yellow means there is a warning on one of the episodes. Red means there has been an error. In the case of yellow (warning) and red (error), you will need to look at the queue under Activity to see what the issue is (hover over the icon to get more details).

You need to remove the item from your download client's queue or history to remove them from Sonarr's queue.