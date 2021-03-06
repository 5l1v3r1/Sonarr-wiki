## GET ##

##### Parameters #####

Required:
`episodeId (int)`

##### Response #####
```JSON
[
{
	"guid": "a5a4a6a7-f7c9-4ff0-b3c4-b8dea9ed965b",
    "quality": {
      "quality": {
        "id": 4,
        "name": "HDTV-720p"
      },
      "proper": false
    },
    "age": 0,
    "size": 0,
    "indexer": "Wombles",
    "releaseGroup": "YesTV",
    "title": "The.Devils.Ride.S03E01.720p.HDTV.x264-YesTV",
    "fullSeason": false,
    "sceneSource": false,
    "seasonNumber": 3,
    "language": "english",
    "seriesTitle": "devilsride",
    "episodeNumbers": [
      1
    ],
    "approved": false,
    "tvRageId": 0,
    "rejections": [
      "Unknown Series"
    ],
    "publishDate": "2014-02-10T00:00:00Z",
    "downloadUrl": "http://www.newshost.co.za/nzb/5a6/The.Devils.Ride.S03E01.720p.HDTV.x264-YesTV.nzb",
    "downloadAllowed": true
  }
]
```



## POST ##

##### Summary #####
Adds a previously searched release to the download client, if the release is still in Sonarr's search cache (30 minute cache). If the release is not found in the cache Sonarr will return a 404.

##### Parameters #####
`guid (string)`

##### Returns JsonObject ######

```JSON
[
{
	"guid": "a5a4a6a7-f7c9-4ff0-b3c4-b8dea9ed965b",
    "quality": {
      "quality": {
        "id": 4,
        "name": "HDTV-720p"
      },
      "proper": false
    },
    "age": 0,
    "size": 0,
    "indexer": "Wombles",
    "releaseGroup": "YesTV",
    "title": "The.Devils.Ride.S03E01.720p.HDTV.x264-YesTV",
    "fullSeason": false,
    "sceneSource": false,
    "seasonNumber": 3,
    "language": "english",
    "seriesTitle": "devilsride",
    "episodeNumbers": [
      1
    ],
    "approved": false,
    "tvRageId": 0,
    "rejections": [
      "Unknown Series"
    ],
    "publishDate": "2014-02-10T00:00:00Z",
    "downloadUrl": "http://www.newshost.co.za/nzb/5a6/The.Devils.Ride.S03E01.720p.HDTV.x264-YesTV.nzb",
    "downloadAllowed": true
  }
]
```