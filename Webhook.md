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
    "Episodes": [
        {
            "Id": 67,
            "EpisodeNumber": 14,
            "SeasonNumber": 2,
            "Title": "The Stanchurian Candidate",
            "AirDate": "2015-08-24",
            "AirDateUtc": "2015-08-25T01:30:00Z",
            "Quality": "HDTV-720p",
            "QualityVersion": 1,
            "ReleaseGroup": null,
            "SceneName": null
        }
    ]
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
    "Episodes": [
        {
            "Id": 67,
            "EpisodeNumber": 14,
            "SeasonNumber": 2,
            "Title": "The Stanchurian Candidate",
            "AirDate": "2015-08-24",
            "AirDateUtc": "2015-08-25T01:30:00Z",
            "Quality": "WEBDL-1080p",
            "QualityVersion": 1,
            "ReleaseGroup": "iT00NZ",
            "SceneName": null
        }
    ]
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
    "Episode": null
}
```


##### Sample/Example Apps/Usage ####

[Hubot Integration](https://github.com/halkeye/hubot-sonarr/)