## GET ##

##### Summary #####
Gets history (grabs/failures/completed).

##### Parameters ######

Required:
`page (int)` - 1-indexed
`pageSize (int)`
`sortKey (string)` - `series.title` or `date`
`sortDir (direction)` - `asc` or `desc`

##### Returns ######

````JSON
{
  "page": 1,
  "pageSize": 15,
  "sortKey": "date",
  "sortDirection": "descending",
  "totalRecords": 100, //Use to disable paging when additional results are not available
  "records": [
    {
      "episodeId": 100,
      "seriesId": 1,
      "sourceTitle": "archer.2009.s05e02.hdtv.x264-killers",
      "quality": {
        "quality": {
          "id": 1,
          "name": "SDTV",
          "weight": 1
        },
        "proper": false
      },
      "date": "2014-01-21T03:54:47.5479441Z",
      "eventType": "downloadFolderImported",
      "data": {
        "droppedPath": "D:\\Completed\\Unsorted TV\\Archer.2009.S05E02.HDTV.x264-KILLERS\\archer.2009.s05e02.hdtv.x264-killers.mp4",
        "importedPath": "T:\\Archer (2009)\\Season 05\\Archer (2009) - S05E02 - Archer Vice- A Kiss While Dying [SDTV].mp4"
      },
      "episode": {
        "seriesId": 7,
        "episodeFileId": 14359,
        "seasonNumber": 5,
        "episodeNumber": 2,
        "title": "Archer Vice: A Kiss While Dying",
        "airDate": "2014-01-20",
        "airDateUtc": "2014-01-21T03:00:00Z",
        "overview": "Archer, Pam and Lana travel to Miami to visit some old friends. It's a fondue party!",
        "hasFile": true,
        "monitored": true,
        "sceneEpisodeNumber": 0,
        "sceneSeasonNumber": 0,
        "tvDbEpisodeId": 0,
        "downloading": false,
        "id": 20985
      },
      "series": {
        "title": "Archer (2009)",
        "seasonCount": 0,
        "episodeCount": 0,
        "episodeFileCount": 0,
        "status": "continuing",
        "overview": "At ISIS, an international spy agency, global crises are merely opportunities for its highly trained employees to confuse, undermine, betray and royally screw each other. At the center of it all is suave master spy Sterling Archer, whose less-than-masculine code name is \"Duchess.\" Archer works with his domineering mother Malory, who is also his boss. Drama revolves around Archer's ex-girlfriend, Agent Lana Kane and her new boyfriend, ISIS comptroller Cyril Figgis, as well as Malory's lovesick secretary, Cheryl.",
        "network": "FX",
        "airTime": "7:00pm",
        "images": [],
        "seasons": [],
        "year": 0,
        "path": "T:\\Archer (2009)",
        "qualityProfileId": 1,
        "seasonFolder": true,
        "monitored": true,
        "useSceneNumbering": false,
        "runtime": 30,
        "tvdbId": 110381,
        "tvRageId": 23354,
        "firstAired": "2009-09-18T02:00:00Z",
        "lastInfoSync": "2014-01-26T19:24:53.0106115Z",
        "seriesType": "standard",
        "cleanTitle": "archer2009",
        "imdbId": "tt1486217",
        "titleSlug": "archer-2009",
        "id": 7
      },
      "id": 3331
    },
    {
      "episodeId": 100,
      "seriesId": 1,
      "sourceTitle": "Archer.2009.S05E02.HDTV.x264-KILLERS",
      "quality": {
        "quality": {
          "id": 1,
          "name": "SDTV",
          "weight": 1
        },
        "proper": false
      },
      "date": "2014-01-21T03:53:44.7999213Z",
      "eventType": "grabbed",
      "data": {
        "indexer": "Nzbs.org",
        "nzbInfoUrl": "http://nzbs.org/details/eab47be5f459b9136a45cf779683d13c",
        "releaseGroup": "KILLERS",
        "age": "0",
        "downloadClient": "SabnzbdClient",
        "downloadClientId": "SABnzbd_nzo_bdmnfn"
      },
      "episode": {
        "seriesId": 7,
        "episodeFileId": 14359,
        "seasonNumber": 5,
        "episodeNumber": 2,
        "title": "Archer Vice: A Kiss While Dying",
        "airDate": "2014-01-20",
        "airDateUtc": "2014-01-21T03:00:00Z",
        "overview": "Archer, Pam and Lana travel to Miami to visit some old friends. It's a fondue party!",
        "hasFile": true,
        "monitored": true,
        "sceneEpisodeNumber": 0,
        "sceneSeasonNumber": 0,
        "tvDbEpisodeId": 0,
        "downloading": false,
        "id": 20985
      },
      "series": {
        "title": "Archer (2009)",
        "seasonCount": 0,
        "episodeCount": 0,
        "episodeFileCount": 0,
        "status": "continuing",
        "overview": "At ISIS, an international spy agency, global crises are merely opportunities for its highly trained employees to confuse, undermine, betray and royally screw each other. At the center of it all is suave master spy Sterling Archer, whose less-than-masculine code name is \"Duchess.\" Archer works with his domineering mother Malory, who is also his boss. Drama revolves around Archer's ex-girlfriend, Agent Lana Kane and her new boyfriend, ISIS comptroller Cyril Figgis, as well as Malory's lovesick secretary, Cheryl.",
        "network": "FX",
        "airTime": "7:00pm",
        "images": [],
        "seasons": [],
        "year": 0,
        "path": "T:\\Archer (2009)",
        "qualityProfileId": 1,
        "seasonFolder": true,
        "monitored": true,
        "useSceneNumbering": false,
        "runtime": 30,
        "tvdbId": 110381,
        "tvRageId": 23354,
        "firstAired": "2009-09-18T02:00:00Z",
        "lastInfoSync": "2014-01-26T19:24:53.0106115Z",
        "seriesType": "standard",
        "cleanTitle": "archer2009",
        "imdbId": "tt1486217",
        "titleSlug": "archer-2009",
        "id": 7
      },
      "id": 3330
    },
  ]
}
````