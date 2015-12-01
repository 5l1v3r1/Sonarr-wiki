## GET ##

##### Summary #####
Returns all episodes for the given series

##### Parameters ######

`seriesId (int)`

##### Returns JsonArray ######

````JSON
[
  {
    "seriesId": 1,
    "episodeFileId": 0,
    "seasonNumber": 1,
    "episodeNumber": 1,
    "title": "Mole Hunt",
    "airDate": "2009-09-17",
    "airDateUtc": "2009-09-18T02:00:00Z",
    "overview": "Archer is in trouble with his Mother and the Comptroller because his expense account is way out of proportion to his actual expenses. So he creates the idea that a Mole has breached ISIS and he needs to get into the mainframe to hunt him down (so he can cover his tracks!). All this leads to a surprising ending.",
    "hasFile": false,
    "monitored": true,
    "sceneEpisodeNumber": 0,
    "sceneSeasonNumber": 0,
    "tvDbEpisodeId": 0,
    "absoluteEpisodeNumber": 1,
    "id": 1
  }
]
````

## GET/{id} ##

##### Summary #####
Returns the episode with the matching id

##### Parameters ######

`id (int)`

##### Returns ######

````JSON
{
  "seriesId": 1,
  "episodeFileId": 0,
  "seasonNumber": 1,
  "episodeNumber": 1,
  "title": "Mole Hunt",
  "airDate": "2009-09-17",
  "airDateUtc": "2009-09-18T02:00:00Z",
  "overview": "Archer is in trouble with his Mother and the Comptroller because his expense account is way out of proportion to his actual expenses. So he creates the idea that a Mole has breached ISIS and he needs to get into the mainframe to hunt him down (so he can cover his tracks!). All this leads to a surprising ending.",
  "hasFile": false,
  "monitored": true,
  "sceneEpisodeNumber": 0,
  "sceneSeasonNumber": 0,
  "tvDbEpisodeId": 0,
  "absoluteEpisodeNumber": 1,
  "downloading": false,
  "id": 1
}
````

## PUT ##

##### Summary #####
Update the given episodes, currently only monitored is changed, all other modifications are ignored.

##### Parameters ######

Required:
All parameters (you should perform a GET/{id} and submit the full body with the changes, as other values may be editable in the future.

##### Returns ######

````JSON
{
  "seriesId": 1,
  "episodeFileId": 0,
  "seasonNumber": 1,
  "episodeNumber": 1,
  "title": "Mole Hunt",
  "airDate": "2009-09-17",
  "airDateUtc": "2009-09-18T02:00:00Z",
  "overview": "Archer is in trouble with his Mother and the Comptroller because his expense account is way out of proportion to his actual expenses. So he creates the idea that a Mole has breached ISIS and he needs to get into the mainframe to hunt him down (so he can cover his tracks!). All this leads to a surprising ending.",
  "hasFile": false,
  "monitored": false,
  "sceneEpisodeNumber": 0,
  "sceneSeasonNumber": 0,
  "tvDbEpisodeId": 0,
  "absoluteEpisodeNumber": 1,
  "downloading": false,
  "id": 1
}
````