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