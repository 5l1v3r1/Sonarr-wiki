##Introduction##

Since version 2.0.0.3000 Sonarr supports a Newznab-like api dubbed **Torznab**.  
This api offers a standardized recent/search api for both tv and movies (of which Sonarr only uses tv).  

Obviously, Torznab is only implemented on a limited number of torrent trackers, but that will change and when it does Sonarr will be ready for it.  
The purpose of this wiki page is to describe the differences with Newznab and some recommendations to implement a custom proxy/indexer.

**Note:** If your torrent tracker is based on a generic tracker software, please coordinate to get the api implemented in the generic base code so everyone can benefit and to avoid double work.   
It's also imperative to think about how to integrate this in your existing karma/bonus system to keep your users engaged in your community.

##Differences with Newznab##

Torznab extends on Newznab on a couple of points to make it more useful. However, it is in principle backward compatible.

###Torznab queries###

Newznab defines the query params `q,rid,season,ep` for `t=tvsearch` and `q` for `t=search`, however not all sites support tvrage ids, and therefore would have to be queries with the q= param.
Torznab implementations should return the supported query params in their `t=caps` response. (more on `caps` later)
Implementations should also take care in returning appropriate responses when a query includes an unsupported newznab parameter, for example, if rid is not supported, return an empty result set.
This is to remain backward compatibility with clients that do not query the caps.

~~Newznab does not define `tvdbid=` and `imdbid=`, but implementors are recommended to support these if possible.~~
The latest Newznab version support `tvdbid=` and `tvmazeid=` as well. That newznab version also uses the `supportedParams` mentioned later, and supports specifying multiple id parameters simultaneously (of which only one needs to match).

```
t=tvsearch:
   Newznab query params: q,rid,season,ep
   Torznab query params: tvdbid
t=search:
   Newznab query params: q
t=movie:
   Newznab query params: q
   Torznab query params: imdbid
```

Examples:
```
?t=tvsearch&cat=..,..&rid=..&season=1&episode=1
?t=tvsearch&cat=..,..&q=..&season=1&episode=1

?t=tvsearch&cat=..,..&rid=..&season=2016&ep=12/20
?t=tvsearch&cat=..,..&q=..&season=2016&ep=12/20

?t=search&cat=..,..&q=Anime+Title+123
?t=search&cat=..,..&q=Fantastic+Series+With+Episode+Title+For+Special
```

###Torznab caps endpoint###

The mode `t=caps` is supposed to return the capabilities and categories of the newznab/torznab indexer.
Implementing this mode is mandatory.

The caps response for torznab is mostly the same as newznab, except for a few points:

The `searching` element is normally used to specify what kind of modes (`tvsearch`,`search`,`movie`) the api supports. But torznab adds an optional `supportedParams` attribute allowing the api to specify which query params are supported.
If the `supportedParams` attribute is not found, then it defaults to the original newznab params as specified earlier.

Many torrent sites have their own categories starting at '1', it's recommended NOT to map these 1 to 1 on newznab categories but instead add 100000 to the number.
That way it falls in the site specific range and does not interfere with the original newznab categories.
The api should then alias all site-specific categories in one of the original newznab category.
For example, if you have category 10 as Blu-Ray 1080p TV, then releases in that category would use the torznab api cats 100010,5040,5000 (Site-specific, TV/HD, TV).
Any query that includes any of those numbers in the `cat=` parameter would return those releases as results.
Of course it's also allowed to omit the site-specific categories entirely, and map only on newznab categories.

Example `t=caps` response:
```
      <?xml version="1.0" encoding="UTF-8"?>
         <caps>
            <!-- server information -->
            <server version="1.0" title="site" strapline="..."
             email="info@site.com" url="http://servername.com/" image="http://servername.com/theme/black/images/banner.jpg"/>

            <limits max="100" default="50"/>

            <registration available="yes" open="yes" />

            <searching>
               <search available="yes" supportedParams="q" />
               <tv-search available="yes" supportedParams="q,rid,season,ep" />
               <movie-search available="no" supportedParams="q" />
            </searching>

            <!-- supported categories -->
            <categories>
               <category id="1000" name="Console">
                  <subcat id="1010" name="NDS"/>
                  <subcat id="1020" name="PSP"/>
               </category>
               <category id="2000" name="Movies">
                  <subcat id="2010" name="Foreign"/>
               </category>

               <!-- site specific categories -->
               <category id="100001" name="MotoGP"       description="Latest MotoGP stuff"/>
               <category id="100002" name="Fifa 2010"    description="Fifa 2010 world cup">
                  <subcat id="100003" name="Fifa 2010 HD" description="HD stuff"/>
                  <subcat id="100004" name="Fifa 2010 SD" description="SD stuff"/>
               </category>
               <!-- etc.. -->
            </categories>
         </caps>
      </xml>
```


###Torznab results###
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
| imdb                 | integer | id for imdb.com                                |
| bannerurl            | url     | Url to a banner image                          |
| **infohash**         | string  | Torrent infohash                               |
|  magneturl           | url     | Magnet uri. Not relevant for private trackers. |
| **seeders**          | integer | Number of active seeders. Omit if unknown!     |
| leechers             | integer | Number of active non-seeders. Omit if unknown! |
| **peers**            | integer | Number of active peers (seeders+leechers).     |
| seedtype             | string  | **TBD** Specifies which seed criteria must be met. Was going for 'ratio,seedtime,both' but afaik it's always 'either' |
| **minimumratio**     | double  | Specifies the minimum ratio the torrent client must seed this torrent. |
| **minimumseedtime**  | integer | Specifies the minimum number of seconds the torrent client must actively seed the torrent. |

###Minimum ratio/seedtime###

These two attributes are included to allow a torrent tracker to specify the seeding requirements on a per torrent basis.     
These values should be set to the long term requirements for the torrent. So if it's freeleech for a decade, you can set minimumratio to 0.0, but if it's only for a day, keep it at 1.0. (0.0 is a bit drastic, but you get the point)  
The idea is that if one of the two criteria is satisfied, the torrent client can put the torrent at a lower priority or stop seeding entirely.

Specifying one or both of these attributes is recommended, because it allows future clients to appropriately adjust the seeding configuration of the torrent client.

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