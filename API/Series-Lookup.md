**Endpoint: "/series/lookup"**

## GET ##

##### Summary #####
Searches for new shows on trakt

##### Parameters ######

Required:
`term` - query string for the search (Use `tvdb:12345` to lookup TVDB ID 12345)

eg: localhost/api/Series/lookup?term=The%20Blacklist

##### Returns Array ######

```JSON
[
  {
    "title": "The Blacklist",
    "seasonCount": 1,
    "episodeCount": 0,
    "episodeFileCount": 0,
    "status": "continuing",
    "overview": "Raymond \"Red\" Reddington, one of the FBI's most wanted fugitives, surrenders in person at FBI Headquarters in Washington, D.C. He claims that he and the FBI have the same interests: bringing down dangerous criminals and terrorists. Reddington will co-operate, but insists that he will speak only to Elizabeth Keen, a rookie FBI profiler. Keen questions Reddington's sudden interest in her, though he claims that Keen is very special. After the FBI brings down a terrorist he provided information on, Reddington reveals that the terrorist is only just the first of many. In the last two decades, he's made a list of criminals and terrorists he believes the FBI cannot find because they did not know they exist and that they matter the most. Reddington calls it \"The Blacklist\".",
    "network": "NBC",
    "images": [
      {
        "coverType": "banner",
        "url": "http://slurm.trakt.us/images/banners/23288.8.jpg"
      },
      {
        "coverType": "poster",
        "url": "http://slurm.trakt.us/images/posters/23288.8-300.jpg"
      },
      {
        "coverType": "fanart",
        "url": "http://slurm.trakt.us/images/fanart/23288.8.jpg"
      }
    ],
    "remotePoster": "http://slurm.trakt.us/images/posters/23288.8-300.jpg",
    "seasons": [
      {
        "seasonNumber": 1,
        "monitored": false
      },
      {
        "seasonNumber": 0,
        "monitored": false
      }
    ],
    "year": 2013,
    "qualityProfileId": 0,
    "seasonFolder": false,
    "monitored": false,
    "useSceneNumbering": false,
    "runtime": 60,
    "tvdbId": 266189,
    "tvRageId": 35048,
    "seriesType": "standard",
    "cleanTitle": "blacklist",
    "imdbId": "tt2741602",
    "titleSlug": "the-blacklist"
  }
]
```