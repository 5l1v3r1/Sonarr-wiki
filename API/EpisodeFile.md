## GET ##

##### Summary #####
Returns all episode files for the given series

##### Parameters ######

Required:

`seriesId (int)`

##### Returns JsonArray ######

````JSON
[
    {
        "seriesId": 1,
        "seasonNumber": 1,
        "path": "C:\\Test\Breaking Bad\\Season 01\\Breaking Bad - S01E01 - Pilot [Bluray 720p].mkv",
        "size": 2183157756,
        "dateAdded": "2013-05-29T10:42:05.1335301Z",
        "sceneName": "",
        "quality": {
            "quality": {
                "id": 1,
                "name": "Bluray 720p"
            },
            "proper": false
        },
        "id": 1
    }
]
````

## GET/{id} ##

##### Summary #####
Returns the episode file with the matching id

##### Parameters ######

Required:

`id (int)`

##### Returns ######

````JSON
{
    "seriesId": 1,
    "seasonNumber": 1,
    "path": "C:\\Test\Breaking Bad\\Season 01\\Breaking Bad - S01E01 - Pilot [Bluray 720p].mkv",
    "size": 2183157756,
    "dateAdded": "2013-05-29T10:42:05.1335301Z",
    "sceneName": "",
    "quality": {
        "quality": {
            "id": 1,
            "name": "Bluray 720p"
        },
        "proper": false
    },
    "id": 1
}
````

## DELETE ##

##### Summary #####
Delete the given episode file

##### Parameters ######

Required:

`id (int)`

##### Returns ######

````JSON
{}
````