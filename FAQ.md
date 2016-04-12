

### How does Sonarr find episodes?  ###
Sonarr doesn't actively search for any episodes on its own; it uses the indexer's latest releases to find recently posted episodes. It does this using the indexer's **RSS feeds**, which typically include the last 100 uploads to the indexer. By default Sonarr will download the latest RSS feeds every 15 minutes. Because of this, Sonarr is designed to be installed on a system that is running most of the time. However, for indexers supporting 'pages', Sonarr will fetch older pages in the rss feed in an attempt to cover the gap when it has been offline for a few hours.

**Active searching** (via the indexer's API) is only done in a few situations:
* When the user clicks the _Automatic_ or _Manual Search_ buttons on a specific episode, season, or series.
* When a user adds a show using the _"Add and Search"_ button. _(New behavior as of March 2015)_

### Why didn't Sonarr grab an episode I was expecting?  ###
First, make sure you read and understand the section above called _"How does Sonarr find episodes?"_ Second, make sure at least one of your indexers has the episode you were expecting to be grabbed.

1. Click the 'Manual Search' icon next to the episode listing in Sonarr. Are there any results? If no, then either Sonarr is having trouble communicating with your indexers, or your indexers do not have the episode, or the episode is improperly named/categorized on the indexer.

2. **If there are results from step 1**, check next to them for red exclamation point icon. Hover over the icon to see why that release is not a candidate for automatic downloads. If every result has the icon, then no automatic download will occur.

3. **If there is at least one valid manual search result from step 2**, then an automatic download should have happened. If it didn't, the most likely reason is a temporary communication problem preventing an RSS Sync from your indexer. It is recommended to have several indexers set up for best results.

4. **If there is no manual result from a show, but you can find it when you browse your indexer's website** - This is a common problem that is most frequently caused by having an insufficient number of indexers. Different indexers index different content, and not all shows on your indexer may be tagged properly, which would cause Sonarr's search to fail. Having several indexers active is the best solution to this problem.


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


### Does Sonarr require a SABnzbd post-processing script to import downloaded episodes?  ###
No. Sonarr will talk to your download client to determine where the files have been downloaded and will be import them automatically automatically. [[Sorting and Renaming]]. If Sonarr and your download client are on different machines you will need to use Remote Path Mapping to link the remote path to a local one so Sonarr knows where to find the files.

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

### I see log messages for shows I don't have/don't want ###

These messages are completely normal and come from the RSS feeds that Sonarr checks to see if there are episodes you do want, usually these only appear in debug/trace logging, but in the event of an problem processing an item you may see a warning or error. Its safe to ignore the warnings/errors as well since they are for shows you don't want, in the event its for a show you want, open up a support thread on the forums.

### Seeding torrents aren't deleted automatically ###

When a torrent is still seeding Sonarr will either Copy or Hardlink the files to your library (depending on your Sonarr settings and disk configuration), when the torrent finishes seeding in your client (hits a seed ratio set in your client) Sonarr can remove the torrent from your client and ask it to delete the previously seeding files on disk, this will happen automatically if the `Remove` option is enabled under Completed Download Handling options.

### Why can't I add a new series? ###

In the event that TheTVDB is unavailable Sonarr is unable to get search results and you will be unable to add any new series by searching. You may be able to add a new series by TheTVDB ID if you know what it is, the UI explains how to add it by an ID.

### I use Sonarr on a Mac and it suddenly stopped working. What happened? ###

Most likely this is due to a MacOS bug which caused one of the Sonarr databases to be corrupted. Follow these steps to resolve:

1. In the Finder, select the Go menu, and the option **Go to Folder...**
2. Enter _~/.config/NzbDrone_ and click the **Go** button to open Sonarr's data folder
3. Move the following files to Trash: **logs.db, logs.db-journal**
4. Attempt to launch Sonarr and see if it works. If so, congrats!
5. If not, then the log DB didn't get corrupted, and it might have been the primary database. You will need to restore from backup.
6. Open the Backups folder you see and find the .zip archive with the most recent date. Decompress it. Move everything from the resulting folder into the main Sonarr data folder, over-writing any files.
7. Attempt to launch Sonarr and see if it works. If it does not work, you'll need further support in the forums or IRC channel.