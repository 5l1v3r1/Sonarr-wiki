If you're looking to notify a web service to indicate when Sonarr has done things, you can find more details here: 

### Overview ###

Sonarr can notify a webservice using POST or PUT when new episodes are imported, a series is renamed, or new files are grabbed.

Parameters are passed to the webservice using a JSON body

### Example Outputs ###

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
        "Id": 1,
        "FullPath": "C:\\Temp\\sonarr\\Gravity Falls\\Season 2\\Gravity Falls - S02E14 - The Stanchurian Candidate.mkv",
        "RelativePath": "Season 2\\Gravity Falls - S02E14 - The Stanchurian Candidate.mkv",
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
    "Episode": null
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