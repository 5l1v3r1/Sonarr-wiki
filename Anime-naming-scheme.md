#Anime naming scheme

Renaming your files, of course, depends on your personal preference. Many users though wonder about how they can make their anime work with Kodi or Plex. While usual tv gets released by the scene in a perfectly parsable way for your htpc, anime does not. The solution is simple though, just rename your anime to tvdb-style.

**{Series.CleanTitle}.S{season:00}E{episode:00}.{absolute:000}.{Quality.Full}-{Release.Group}**

The above renaming scheme is an example that will let your anime have almost the same style as episodes of regular tv. Let's analyze and see why this naming scheme is good for you.

>**{Series.CleanTitle}.S{season:00}E{episode:00}**.{absolute:000}.{Quality.Full}-{Release.Group}
>
>This is the part that the Kodi/Plex scraper is interested in. It will be able to parse it like any regular tv show.
>
>*****
>
>{Series.CleanTitle}.S{season:00}E{episode:00}.**{absolute:000}**.{Quality.Full}-{Release.Group}
>
>This part isn't really obvious. Why would you need the absolute number in there? It's for forward compatibility. If you ever want to rename your anime to another style or if tvdb changes seasons and you want to fix the resulting wrong season/episode number, you would do it based on this absolute number. Having this will save you many headaches in the future.
>
>*****
>
>{Series.CleanTitle}.S{season:00}E{episode:00}.{absolute:000}.**{Quality.Full}**-{Release.Group}
>
>This part is for forward compatibility also. If something goes wrong with your library or you lose your database, you want Sonarr to be able to rescrape the quality of your files.
>
>*****
>
>{Series.CleanTitle}.S{season:00}E{episode:00}.{absolute:000}.{Quality.Full}-**{Release.Group}**
>
>The same goes for group. If you have a file, with the group in the end like this, Sonarr will be able to detect the group (not through the dronefactory. The dronefactory expects anime scene style) when this show is in your library.

Feel free to modify this naming scheme to your personal preference or take comfort on knowing that the scheme, as described here, is well tested.

One more note. If you ever want to rename your files to exactly their original state, you can use AniDB O'Matic for that. It's a tool that hooks directly into the info on anidb and parses your files by hash. It can then rename to the original name as stored at anidb. Be warned though. The hashing may take a very long time.

### Anime Manual Import Issue ###

Per the forum post [here] (https://forums.sonarr.tv/t/sonarr-not-finding-all-files/8618/4), Sonarr currently has trouble parsing absolute episode numbers over 100, since it then treats the first digit as a season with the following two digits as the episode number.  The current workaround for this issue is to add any release group name in brackets at the beginning of the file name.

Example:
* Bad absolute file name: Show.234.Episode.Name.mkv
* Modified file name: [DND] Show.234.Episode.Name.mkv