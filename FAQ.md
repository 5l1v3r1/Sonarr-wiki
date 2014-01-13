### Does NzbDrone require a SABnzbd post-processing script to import downloaded episodes?  ###
No. as long as you set the Drone Factory path `Settings > Download Client > Drone Factory` to the folder where sab downloads your TV Shows everything will be imported automatically. [[Sorting and Renaming]]

### How does NzbDrone find episodes?  ###
NzbDrone doesn't actively search for any episodes on its own, it uses the indexer's latest releases to find recently posted episodes. Typically the indexer returns the last 100 releases, which isn't much, so be wary if you shut your system down for an extended period of time you might miss some newly release episodes. also, sometimes older episodes are re-posted and might get downloaded if you haven't ignored them. Missing episodes are not actively searched for (missing is anything that aired prior to the current time), unless that episode has not yet been posted (aired recently) or is re-posted you will need to manually search for them.

### Why can't NzbDrone see my files on a remote server?  ###
This can be for various reasons, but the most common is, NzbDrone is running as a service, which causes one of two things:

1.  NzbDrone runs under the SYSTEM account by default which doesn't have access to protected remote file shares.
	
	**Solutions:**
	- Run NzbDrone's service as another user that has access to that share [How to change a service's user account](http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/sys_srv_logon_user.mspx?mfr=true)
	- Run NzbDrone.exe using the Startup Folder
	


2. You're using a mapped network drive (not a UNC path)
	
	**Solutions:**
	- Change your paths to UNC paths (\\server\share)
	- Run NzbDrone.exe via the Startup Folder 


### How does NzbDrone handle scene numbering issues (American Dad!, etc)? ###
NzbDrone relies on [TheXEM](TheXEM "http://thexem.de/"), a community driven site that lets users create mappings of shows that the scene (the people that post the files) and TheTVDB (which typically follows the network's numbering). There are a number of shows on there already, but its easy to add another and typically the changes are accepted within a couple days (if they're correct).

### Why can't NzbDrone import episode files for series X? / Why can't NzbDrone find releases for series X? ###
NzbDrone relies on being able to match titles, often the scene posts episodes using different titles, eg *CSI: Crime Scene Investigation* as just *CSI* so NzbDrone can't match the names without some help. NzbDrone maintains a list of problematic series which lets us solve this issue. To request a new mapping:

1. Make sure it hasn't already been requested. [Requested Mappings](https://docs.google.com/spreadsheet/ccc?key=0Atcf2VZ47O8tdGdQN1ZTbjFRanhFSTBlU0xhbzhuMGc#gid=0) 
2. Make a new request here: [Scene Mapping Request Form]( https://docs.google.com/forms/d/15S6FKZf5dDXOThH4Gkp3QCNtS9Q-AmxIiOpEBJJxi-o/viewform)

*Typically these are added the next day, if I'm available earlier and asked nicely in IRC I can expedite the*m

### Why can't I add a new show to NzbDrone, its on TheTVDB? ###
NzbDrone use [trakt](http://trakt.tv/) for series/episode information and images (fanart, banners, images). Here are some reasons why you might not be able to find your show:

1. Trakt doesn't like special characters to be used when searching for series through the API. Try your search without special characters. [Also vote on this issue so they can get it fixed](http://support.trakt.tv/forums/188762-general/suggestions/4199849-searching-for-shows-with-special-characters).
2. The series hasn't been added to trakt yet, follow their [guide](http://support.trakt.tv/knowledgebase/articles/151225-how-do-i-add-a-new-tv-show-to-trakt) to get it added. 

### I see that feature/bug X was fixed, why can't I see it?  ###
NzbDrone consists of two main branches of code, master and develop, master is released periodically, when the develop branch is stable and develop is for pre-release testing and people willing to live on the edge, if you want to help out testing or want more information on the two branches, please see: [[Release-Branches]]
When a feature is marked as Done (complete) it means its been fixed in develop, it won't be until the next release to the master branch after the feature is marked as Done that it will appear for most users.

### Episode Progress - How is it calculated?  ###
There are two parts to the episode count, one being the number of episodes (Episode Count) and the other being the number of episodes with files (Episode File Count), each one uses slightly different logic to give you the overall progress for a series or season.

- Episode Count
	- Episode has already aired AND is monitored OR
	- Episode has a file
- Episode File Count
	- Episode has a file

If a series has 10 episodes that have all aired and you don't have any files for them you would have 0/10 episodes, if you unmonitored all the episodes in that series you would have 0/0 and if you got all the episodes for that series, regardless of if the episodes are monitored or not, you would have 10/10 episodes.

### I got a pop-up that said config.xml was corrupt, what now?  ###
NzbDrone was unable to read your config file on start-up as it became corrupted somehow. In order to get NzbDrone back online, you will need to delete `C:\ProgramData\NzbDrone\Config.xml` (Windows), once deleted start NzbDrone and it will start on the default port (8989), you should now re-configure any settings you configured on the General Settings page.

### How do I access NzbDrone from another computer?  ###
By default NzbDrone doesn't listen to requests from all systems (when not run as administrator), it will only listen on localhost, this is due to how the Web Server NzbDrone uses integrates with Windows (this also applies for current alternatives). If NzbDrone is run as an administrator it will correctly register itself with Windows as well as open the Firewall port so it can be accessed from other systems on your network. Running as admin only needs to happen once (if you change the port it will need to be re-run).