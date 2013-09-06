#### Does NzbDrone require a SABnzbd post-processing script to import downloaded episodes?  ####
No. as long as you set the Drone Factory path `Settings > Download Client > Drone Factory` to the folder where sab downloads your TV Shows everything will be imported automatically. [[Sorting and Renaming]]

#### How does NzbDrone find new episodes?  ####
NzbDrone doesn't actively search for any episodes on its own, it uses RSS feed to find recently posted episodes (sometimes older episodes are posted). Typically the indexer returns the last 100 releases, which isn't much, so be wary if you shut your system down for an extended period of time you might miss some newly release episodes.

#### Why can't NzbDrone see my files on a remote server?  ####
This can be for various reasons, but the most common is, NzbDrone is running as a service, which causes one of two things:

	1. The remote server requires authentication and NzbDrone runs under the SYSTEM account by default so it doesn't know what the credentials are for that share.
	
		Solutions:
		- Run NzbDrone's service as another user that has connected to that share 
		- Run NzbDrone.exe via the Startup Folder
	2. You're using a mapped network drive (not a UNC path)
	
		Solutions:
		- Change your paths to UNC paths (\\server\share)
		- Run NzbDrone.exe via the Startup Folder 


#### How does NzbDrone handle scene numbering issues (American Dad!, etc)? ####
NzbDrone relies on TheXEM (http://thexem.de/), a community driven site that lets users create mappings of shows that the scene (the people that post the files) and TheTVDB (which typically follows the network's numbering). There are a number of shows on there already, but its easy to add another and typically the changes are accepted within a couple days (if they're correct).

#### Why can't NzbDrone import episode files for series X? ####
NzbDrone relies on being able to parse the series title of the post into something it knows about, during that process it removes special characters and spaces and converts the name to lower case, for example: *CSI: Crime Scene Investigation* would be *csicrimesceneinvestigation* often the scene posts episodes as just *CSI* so NzbDrone can't match the names without some help. NzbDrone maintains a list of problematic series which lets us solve the issue for everyone at once. To request a new mapping:

1. Make sure it hasn't already been requested: https://docs.google.com/spreadsheet/ccc?key=0Atcf2VZ47O8tdGdQN1ZTbjFRanhFSTBlU0xhbzhuMGc#gid=0
2. Make a new request here: https://docs.google.com/forms/d/15S6FKZf5dDXOThH4Gkp3QCNtS9Q-AmxIiOpEBJJxi-o/viewform
3. Typically these are added the next day, if I'm available earlier and asked nicely in IRC I can expedite them

#### Why can't I add a new show to NzbDrone, its on TheTVDB? ####
NzbDrone use trakt.tv for series/episode information and for images (fanart, banners, images) and there are two reasons why you may not be able to add it:

1. Trakt doesn't like special characters to be used when searching for series through the API (which NzbDrone uses), so try without special characters and vote on this feature to fix it on their side: http://support.trakt.tv/forums/188762-general/suggestions/4199849-searching-for-shows-with-special-characters
2. The series hasn't been added to trakt yet, follow their guide to get it added: http://support.trakt.tv/knowledgebase/articles/151225-how-do-i-add-a-new-tv-show-to-trakt-

#### I see that feature/bug X was fixed, why can't I see it?  ####
NzbDrone consists of two main branches of code, master and develop, master is released periodically, when the develop branch is stable and develop is for pre-release testing and people willing to live on the edge, if you want to help out testing or want more information on the two branches, please see: [[Release-Branches]]
When a feature is marked as Done (complete) it means its been fixed in develop, it won't be until the next release to the master branch after the feature is marked as Done that it will appear for most users.

#### Episode Progress - How is it calculated?  ####
There are two parts to the episode count, one being the number of episodes (Episode Count) and the other being the number of episodes with files (Episode File Count), each one uses slightly different logic to give you the overall progress for a series or season.

- Episode Count
	- Episode has already aired AND is monitored OR
	- Episode has a file
- Episode File Count
	- Episode has a file

If a series has 10 episodes that have all aired and you don't have any files for them you would have 0/10 episodes, if you unmonitored all the episodes in that series you would have 0/0 and if you got all the episodes for that series, regardless of if the episodes are monitored or not, you would have 10/10 episodes. 