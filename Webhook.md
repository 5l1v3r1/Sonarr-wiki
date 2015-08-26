If you're looking to notify a web service to indicate when Sonarr has done things, you can find more details here: 

### Overview ###

Sonarr can notify a web service using `POST` or `PUT` when new episodes are imported, renamed, or grabbed.

Parameters are passed to the web service as a JSON body

### Example Payload ###

##### On Download/On Upgrade #####

```json
{
    "EventType": "Download",
    "Series": {
        "Id": 2,
        "Title": "Gravity Falls",
        "Path": "C:\\Temp\\sonarr\\Gravity Falls",
        "TvdbId": 259972
    },
    "EpisodeFile": {
        "Id": 2,
        "FullPath": "C:\\Temp\\sonarr\\Gravity Falls\\Season 2\\Gravity Falls - S02E14 - The Stanchurian Candidate HDTV-720p.mkv",
        "RelativePath": "Season 2\\Gravity Falls - S02E14 - The Stanchurian Candidate HDTV-720p.mkv",
        "SeasonNumber": 2,
        "Episodes": [
            {
                "AirDate": "2015-08-24",
                "AirDateUtc": "2015-08-25T01:30:00Z",
                "EpisodeNumber": 14
            }
        ],
        "Quality": "HDTV-720p",
        "QualityVersion": "1",
        "ReleaseGroup": "",
        "SceneName": ""
    },
    "Episode": {
        "AirDate": "2015-08-24",
        "AirDateUtc": "2015-08-25T01:30:00Z",
        "EpisodeNumber": 14
    }
}
```

##### On Grab #####

```json
{
    "EventType": "Grab",
    "Series": {
        "Id": 2,
        "Title": "Gravity Falls",
        "Path": "C:\\Temp\\sonarr\\Gravity Falls",
        "TvdbId": 259972
    },
    "EpisodeFile": null,
    "Episode": {
        "AirDate": "2015-08-24",
        "AirDateUtc": "2015-08-25T01:30:00Z",
        "EpisodeNumber": 14
    }
}
```

##### On Rename #####

```json
{
    "EventType": "Rename",
    "Series": {
        "Id": 2,
        "Title": "Gravity Falls",
        "Path": "C:\\Temp\\sonarr\\Gravity Falls",
        "TvdbId": 259972
    },
    "EpisodeFile": null,
    "Episode": null
}
```