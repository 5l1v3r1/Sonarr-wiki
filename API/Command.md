## GET ##

`api/command`
`api/command/{id}`

##### Summary #####
Queries the status of a previously started command, or all currently started commands.

##### Parameters ######

Optional route {id}:

`id (int)` Unique ID of the command

##### Returns ######

For `api/command`   
Array of json objects   

For `api/command/{id}`
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

## POST ##

##### Summary #####
Publish a new command for Sonarr to run. These commands are executed asynchronously; use GET to retrieve the current status.

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

### DownloadedEpisodesScan ###
Instruct Sonarr to scan the DroneFactoryFolder or a folder defined by the path variable.    
Each file and folder in the DroneFactoryFolder is interpreted as separate download.   

But a folder specified by the path variable is assumed to be a single download (job) and the folder name should be the release name.

The downloadClientId can be used to support this API endpoint in conjunction with Completed Download Handling, so Sonarr knows that a particular download has already been imported.

##### Parameters ######

Optional:

`path (string)`,   
`downloadClientId (string)` (nzoid for sabnzbd, special 'drone' attribute value for nzbget, uppercase infohash for torrents)

---

### RssSync ###
Instruct Sonarr to perform an RSS sync with all enabled indexers

##### Parameters ######

None

---

### RenameFiles ###
Instruct Sonarr to rename the list of files provided.

##### Parameters ######

`files (int[])` (List of File IDs to rename)

---

### RenameSeries ###
Instruct Sonarr to rename all files in the provided series.

##### Parameters ######

`seriesIds (int[])` (List of Series IDs to rename)