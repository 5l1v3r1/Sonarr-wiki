## POST ##

##### Summary #####
Publish a new command for NzbDrone to run

##### Parameters ######

Required:

`name (string)`

##### Returns ######

````JSON
{
  "name": "RescanSeries",
  "startedOn": "0001-01-01T00:00:00Z",
  "stateChangeTime": "2014-02-05T05:09:09.2366139Z",
  "sendUpdatesToClient": true,
  "state": "pending",
  "id": 24
}
````

## Commands ##

### RefreshSeries ###
Refresh series information from trakt and rescan disk

##### Parameters ######

Optional:

`seriesId (int)` - if not set all series will be refreshed and scanned

---

### RescanSeries ###
Refresh rescan disk for a single series

##### Parameters ######

Optional:

`seriesId (int)` - if not set all series will be scanned

---

### EpisodeSearch ###
Search for one or more episodes

##### Parameters ######

Required:

`episodeIds (int[])` - one or more episodeIds in an array

---

### SeasonSearch ###
Search for all episodes of a particular season

##### Parameters ######

Required:

`seriesId (int)`

`seasonNumber (int)`

---

### SeriesSearch ###
Search for all episodes in a series

##### Parameters ######

Required:

`seriesId (int)`

---

### DownloadedEpisodesScanCommand ###
Instruct NzbDrone to scan the DroneFactoryFolder or a folder defined by the path variable

##### Parameters ######

Optional:

`path (string)`