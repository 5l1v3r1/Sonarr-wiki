**Endpoint: "/series"**

## GET ##

##### Summary #####
Returns all series in your collection

##### Parameters ######

*None*

##### Returns JsonArray ######

```JSON
[
  {
    "title": "Archer (2009)",
    "seasonCount": 5,
    "episodeCount": 47,
    "episodeFileCount": 47,
    "status": "continuing",
    "overview": "At ISIS, an international spy agency, global crises are merely opportunities for its highly trained employees to confuse, undermine, betray and royally screw each other. At the center of it all is suave master spy Sterling Archer, whose less-than-masculine code name is \"Duchess.\" Archer works with his domineering mother Malory, who is also his boss. Drama revolves around Archer's ex-girlfriend, Agent Lana Kane and her new boyfriend, ISIS comptroller Cyril Figgis, as well as Malory's lovesick secretary, Cheryl.",
    "nextAiring": "2014-01-21T03:00:00Z",
    "network": "FX",
    "airTime": "7:00pm",
    "images": [
      {
        "coverType": "banner",
        "url": "/MediaCover/7/banner.jpg?lastWrite=635114443841234311"
      },
      {
        "coverType": "poster",
        "url": "/MediaCover/7/poster.jpg?lastWrite=635114443843262329"
      },
      {
        "coverType": "fanart",
        "url": "/MediaCover/7/fanart.jpg?lastWrite=635114443844822347"
      }
    ],
    "seasons": [
      {
        "seasonNumber": 5,
        "monitored": true
      },
      {
        "seasonNumber": 4,
        "monitored": true
      },
      {
        "seasonNumber": 3,
        "monitored": true
      },
      {
        "seasonNumber": 2,
        "monitored": true
      },
      {
        "seasonNumber": 1,
        "monitored": true
      },
      {
        "seasonNumber": 0,
        "monitored": false
      }
    ],
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
    "lastInfoSync": "2014-01-17T05:10:23.253208Z",
    "seriesType": "standard",
    "cleanTitle": "archer2009",
    "imdbId": "tt1486217",
    "titleSlug": "archer-2009",
    "id": 1
  }
]
```

## GET/{id} ##

##### Summary #####
Returns the series with the matching ID or 404 if no matching series is found

##### Parameters ######

`id (int)`

##### Returns JsonObject ######

````JSON
{
  "title": "Archer (2009)",
  "seasonCount": 5,
  "episodeCount": 47,
  "episodeFileCount": 47,
  "status": "continuing",
  "overview": "At ISIS, an international spy agency, global crises are merely opportunities for its highly trained employees to confuse, undermine, betray and royally screw each other. At the center of it all is suave master spy Sterling Archer, whose less-than-masculine code name is \"Duchess.\" Archer works with his domineering mother Malory, who is also his boss. Drama revolves around Archer's ex-girlfriend, Agent Lana Kane and her new boyfriend, ISIS comptroller Cyril Figgis, as well as Malory's lovesick secretary, Cheryl.",
  "nextAiring": "2014-01-21T03:00:00Z",
  "network": "FX",
  "airTime": "7:00pm",
  "images": [
    {
      "coverType": "banner",
      "url": "/MediaCover/7/banner.jpg?lastWrite=635114443841234311"
    },
    {
      "coverType": "poster",
      "url": "/MediaCover/7/poster.jpg?lastWrite=635114443843262329"
    },
    {
      "coverType": "fanart",
      "url": "/MediaCover/7/fanart.jpg?lastWrite=635114443844822347"
    }
  ],
  "seasons": [
    {
      "seasonNumber": 5,
      "monitored": true
    },
    {
      "seasonNumber": 4,
      "monitored": true
    },
    {
      "seasonNumber": 3,
      "monitored": true
    },
    {
      "seasonNumber": 2,
      "monitored": true
    },
    {
      "seasonNumber": 1,
      "monitored": true
    },
    {
      "seasonNumber": 0,
      "monitored": false
    }
  ],
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
  "lastInfoSync": "2014-01-17T05:10:23.253208Z",
  "seriesType": "standard",
  "cleanTitle": "archer2009",
  "imdbId": "tt1486217",
  "titleSlug": "archer-2009",
  "id": 1
}
````

## POST ##

##### Summary #####
Adds a new series to your collection

##### Parameters ######

NOTE: if you do not add the required params, then the series wont function. some of these without the others can indeed make a "series". But it wont function properly in nzbdrone. 

Required:
`tvdbId (int)`
`title (string)`
`qualityProfileId (int)`
`titleSlug (string)`
`seasons (array)` - See GET output for format

`path (string)` - full path to the series on disk
*or*
`rootFolderPath (string)` - full path will be created by combining the rootFolderPath with the series title

Optional:
`tvRageId (int)`
`seasonFolder (bool)`
`monitored (bool)`

##### Returns JsonObject ######

````JSON
{
    "title": "Archer (2009)",
    "seasons": [
      {
        "seasonNumber": 5,
        "monitored": true
      },
      {
        "seasonNumber": 4,
        "monitored": true
      },
      {
        "seasonNumber": 3,
        "monitored": true
      },
      {
        "seasonNumber": 2,
        "monitored": true
      },
      {
        "seasonNumber": 1,
        "monitored": true
      },
      {
        "seasonNumber": 0,
        "monitored": false
      }
    ],
    "path": "T:\\Archer (2009)",
    "qualityProfileId": 1,
    "seasonFolder": true,
    "monitored": true,
    "tvdbId": 110381,
    "tvRageId": 23354,
    "cleanTitle": "archer2009",
    "imdbId": "tt1486217",
    "titleSlug": "archer-2009",
    "id": 1
  }
````

## PUT ##

##### Summary #####
Update an existing series

##### Parameters ######

Required:
All parameters (you should perform a GET/{id} and submit the full body with the changes

##### Returns JsonObject ######

````JSON
{
  "title": "Archer (2009)",
  "seasonCount": 5,
  "episodeCount": 47,
  "episodeFileCount": 47,
  "status": "continuing",
  "overview": "At ISIS, an international spy agency, global crises are merely opportunities for its highly trained employees to confuse, undermine, betray and royally screw each other. At the center of it all is suave master spy Sterling Archer, whose less-than-masculine code name is \"Duchess.\" Archer works with his domineering mother Malory, who is also his boss. Drama revolves around Archer's ex-girlfriend, Agent Lana Kane and her new boyfriend, ISIS comptroller Cyril Figgis, as well as Malory's lovesick secretary, Cheryl.",
  "nextAiring": "2014-01-21T03:00:00Z",
  "network": "FX",
  "airTime": "7:00pm",
  "images": [
    {
      "coverType": "banner",
      "url": "/MediaCover/7/banner.jpg?lastWrite=635114443841234311"
    },
    {
      "coverType": "poster",
      "url": "/MediaCover/7/poster.jpg?lastWrite=635114443843262329"
    },
    {
      "coverType": "fanart",
      "url": "/MediaCover/7/fanart.jpg?lastWrite=635114443844822347"
    }
  ],
  "seasons": [
    {
      "seasonNumber": 5,
      "monitored": true
    },
    {
      "seasonNumber": 4,
      "monitored": true
    },
    {
      "seasonNumber": 3,
      "monitored": true
    },
    {
      "seasonNumber": 2,
      "monitored": true
    },
    {
      "seasonNumber": 1,
      "monitored": true
    },
    {
      "seasonNumber": 0,
      "monitored": false
    }
  ],
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
  "lastInfoSync": "2014-01-17T05:10:23.253208Z",
  "seriesType": "standard",
  "cleanTitle": "archer2009",
  "imdbId": "tt1486217",
  "titleSlug": "archer-2009",
  "id": 1
}
````

## DELETE/{id} ##

##### Summary #####
Delete the series with the given ID

##### Parameters ######

Required:
`id (int)`

Optional:
`deleteFiles (bool)` - if true the series folder and all files will be deleted when the series is deleted

##### Returns JsonObject ######
````JSON
{}
````