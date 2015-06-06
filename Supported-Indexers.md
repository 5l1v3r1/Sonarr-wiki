##Usenet##

###Newznab###

Newznab is a standardized API used by many usenet indexing sites.

Several presets are available, but most require an API key to be accessible.

###Omgwtfnzbs###

Website: https://omgwtfnzbs.org/  

###Wombles###

Wombles Index is a free RSS feed that reports recent public releases. Wombles does not support (backlog) searches and thus can only be used to grab new releases as they are posted.

###Fanzub###

Website: <s>http://fanzub.com/</s>

Indexer for Japanese media (Anime) exclusively.

**NOTE:** The original Fanzub site was decommissioned March 1st, 2015. Several alternatives sites implementing the same api may be available.

##Torrents##

###Torznab###

Torznab is a wordplay on Torrent and Newznab. It uses the same structure and syntax as the Newznab API specification, but exposing torrent-specific attributes and .torrent files. Thus supports a recent rss feed AND backlog searching capabilities. The specification is not maintained and supported by the Newznab organization.
(The same api specification is shared with nZEDb)

At this point it's unlikely your favorite tracker supports this. In fact, atm there's only one. We'll update this post once we become aware of other trackers supporting it.

**Important/Disclaimer:** Many torrent trackers thrive on the community and may have rules in place that mandate site visits, karma, votes, comments and all. Please review your tracker rules and etiquette, keep your community alive.  
We're not responsible if your account is banned for disobeying rules or accruing HnRs/low-ratio.

###TorrentRssIndexer###

Generic torrent RSS feed parser.

**NOTE:** The RSS feed must contain a pubdate. The release size is recommended as well.

###BitMeTv###

Website: http://www.bitmetv.org/

**NOTE:** BitMeTv requires a cookie to be able to access the rss feed. You'll have to retrieve the cookie using your browser.
The cookie should look like:   
```"uid=123456789; pass=abcdef0123456789abcdef0123456789".```

###BroadcastheNet###

Website: https://broadcasthe.net/

###Eztv###

Website: RIP

**Warning:** do not use <s>eztv dot it</s> <s>eztv dot ch</s> or any other eztv site, those aren't owned by eztv (and eztv quit).

The entire feed is unavailable long before that.

Use the Generic Torrent RSS when we release that feature.

###IPTorrents###

Website: http://www.iptorrents.com/

###KickassTorrents###

Website: https://kickass.to/

**NOTE:** By default only verified releases will be shown, this can be changed in the KAT settings within Sonarr. If you're not seeing results for in some searches, it is likely because they are not verified results.

###Nyaa###

Website: http://www.nyaa.se/

Torrent Indexer for Japanese media (Anime) exclusively.

###Rarbg###

Website: https://rarbg.to/

###Torrentleech###

Website: http://torrentleech.org/

##Supported Features##

| Indexer         | Recent Feed | Standard | Season |  Daily  | Anime | Specials |
|-----------------|:-----------:|:--------:|:------:|:-------:|:-----:|:--------:|
| **Usenet**      |             |          |        |         |       |          |
| Newznab         |     Yes     |    Yes   |   Yes  |   Yes   |  Yes  |   Basic  |
| Fanzub          |     Yes     |     -    |    -   |    -    |  Yes  |     -    |
| Omgwtfnzbs      |     Yes     |    Yes   |   Yes  |   Yes   |   -   |   Basic  |
| Wombles         |     Yes     |     -    |    -   |    -    |   -   |     -    |
| **Torrent**     |             |          |        |         |       |          |
| Torznab         |     Yes     |    Yes   |   Yes  |   Yes   |Unknown|  Unknown |
| TorrentRss      |     Yes     |     -    |    -   |    -    |   -   |     -    |
| BitMeTv         |     Yes     |     -    |    -   |    -    |   -   |     -    |
| BroadcastheNet  |     Yes     |    Yes   |   Yes  |   Yes   |   -   |     -    |
| IPTorrents      |     Yes     |     -    |    -   |    -    |   -   |     -    |
| KickassTorrents |     Yes     |    Yes   |   Yes  |   Yes   |   -   |   Basic  |
| Nyaa            |     Yes     |     -    |    -   |    -    |  Yes  |   Basic  |
| Rarbg           |     Yes     |    Yes   |   Yes  |   Yes   |   -   |     -    |
| Torrentleech    |     Yes     |     -    |    -   |    -    |   -   |     -    |