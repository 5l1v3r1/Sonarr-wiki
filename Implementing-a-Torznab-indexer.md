##Introduction##

Since version 2.0.0.3000 Sonarr supports a Newznab-like api dubbed **Torznab**.  
This api offers a standardized recent/search api for both tv and movies (of which Sonarr only uses tv).  

Obviously, Torznab is only implemented on one torrent tracker, but that will change and when it does Sonarr will be ready for it.  
The purpose of this wiki page is to describe the differences with Newznab and some recommendations to implement a custom proxy/indexer.

**Note:** If your torrent tracker is based on a generic tracker software, please coordinate to get the api implemented in the generic base code so everyone can benefit and to avoid double work.

##Differences with Newznab##

First and foremost: Torznab indexers should return application/x-bittorrent as enclosure type:   
```
<enclosure url="https://yoursite.com/download.php?torrent=123&amp;passkey=123456"   
           length="1460985071" type="application/x-bittorrent" />
```

Torznab defines a couple of attributes using the ```xmlns:torznab="http://torznab.com/schemas/2015/feed"``` xml namespace.   
I'm keeping the list in the reference linked below, but here is a table with the torrent-specific stuff:   
```<torznab:attr name="seeders" value="1"/>```

All these attributes are optional, the bold ones are recommended.

| Name                 | Type    | Description                                    |
|:---------------------|:--------|:-----------------------------------------------|
| type                 | string  | series,movie,music,book (if unknown just omit) |
| tvdbid               | integer | id for thetvdb.com                             |
| **rageid**           | integer | id for tvrage.com                              |
| bannerurl            | url     | Url to a banner image                          |
| **infohash**         | string  | Torrent infohash                               |
|  magneturl           | url     | Magnet uri. Not relevant for private trackers. |
| **seeders**          | integer | Number of active seeders. Omit if unknown!     |
| leechers             | integer | Number of active non-seeders. Omit if unknown! |
| **peers**            | integer | Number of active peers (seeders+leechers).     |
| seedtype             | string  | **TBD** Specifies which seed criteria must be met was going for 'ratio,seedtime,both' but afaik it's always 'either' |
| **minimumratio**     | double  | Specifies the minimum ratio the torrent client must seed at for this torrent. |
| **minimumseedtime**  | integer | Specifies the minimum number of seconds the torrent client must've actively seeded the torrent. |

###Minimum ratio/seedtime###

These two attributes are included to allow a torrent tracker to specify the seeding requirements on a per torrent basis.     
These values should be set to the long term requirements for the torrent. So if it's freeleech for a decade, you can set minimumratio to 0.0, but if it's only for a day, keep it at 1.0.  
The idea is that if one of the two criteria is satisfied, the torrent client can put the torrent at a lower priority or stop seeding entirely.

Specifying one or both of these attributes is recommended, because it allows future clients to appropriately adjust the seeding configuration of the torrent client.

##Recommended query params##

Incomplete list of what should be supported.

```
?t=tvsearch&cat=..,..&rid=..&season=1&episode=1
?t=tvsearch&cat=..,..&q=..&season=1&episode=1

?t=tvsearch&cat=..,..&rid=..&season=2016&episode=12/20
?t=tvsearch&cat=..,..&q=..&season=2016&episode=12/20

?t=search&cat=..,..&q=Anime+Title+123
?t=search&cat=..,..&q=Fantastic+Series+With+Episode+Title+For+Special
```

##Hints and gotta's##

- Make sure your api properly handles the ```Accept``` and ```Content-Type``` http headers. Rss should have one of these mime-types ```application/rss+xml, text/rss+xml, text/xml```. Whatever you do, do _not_ use ```text/html```.
- Double check enclosure url, size and type.
- Triple check any caching mechanism you have to make sure you're not serving stale or incorrect data.
- Make sure that filter options you do not support return no results. Eg. if you don't support the 'q=' wildcard search, make sure you don't return any result if that query param is supplied.
- Return the appropriate newznab errors on apilimits and such.
- Support the ```offset=``` paging option.
- Ensure you have a ```<guid>...</guid>``` item in your rss results.
- Implement the ```t=caps``` endpoint, feel free to put it behind an apikey check. It provides useful information about which categories you support.

##Some References##
Newznab specification:  http://newznab.readthedocs.org/en/latest/misc/api/  
nZEDb specification: https://github.com/nZEDb/nZEDb/blob/master/docs/newznab_api_specification.txt  
Torznab xml attributes: https://github.com/Sonarr/Sonarr/blob/develop/schemas/torznab.xsd   
Specific example: https://github.com/Sonarr/Sonarr/blob/develop/src/NzbDrone.Core.Test/Files/RSS/torznab_hdaccess_net.xml   