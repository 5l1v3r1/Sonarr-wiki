If you're looking to trigger a custom script in your download client to tell Sonarr when to update, you can find more details here. Scripts are added to Sonarr via the *Connect* Settings page.

### Overview ###

Sonarr can execute a custom script when new episodes are imported or a series is renamed, depending on the which action occurred the parameters will be different. Parameters are passed to the script through environment variables (allowing for more flexibility in what we send to the script and not having to worry about a particular order). In all cases the Environment Variables Sonarr sends will be prefixed with `Sonarr` and converted to lowercase, the `Series_Id` will appear as `sonarr_series_id`.

### Environment Variables ###

##### On Download/On Upgrade #####

| Environment Variable | Details |
|---|---|
| EventType | Download |
| Series_Id | Internal ID of the series |
| Series_Title | Title of the series |
| Series_Path | Full path to the series |
| Series_TvdbId | TVDB ID for the series |
| EpisodeFile_Id | Internal ID of the episode file |
| EpisodeFile_RelativePath | Path to the episode file relative to the series' path |
| EpisodeFile_Path | Full path to the episode file |
| EpisodeFile_SeasonNumber | Season number of episode |
| EpisodeFile_EpisodeNumbers | Comma separated list of episode numbers |
| EpisodeFile_EpisodeAirDates | Air date from original network |
| EpisodeFile_EpisodeAirDatesUtc | Air Date with Time in UTC |
| EpisodeFile_Quality | Quality name from Sonarr |
| EpisodeFile_QualityVersion | 1 is the default, 2 for proper, 3+ could be used for anime versions |
| EpisodeFile_ReleaseGroup | Release group, will not be set if it is unknown |
| EpisodeFile_SceneName | Original release name |
| EpisodeFile_SourcePath | Full path to the episode file that was imported |
| EpisodeFile_SourceFolder | Full path to the folder the episode file was imported from |

##### On Rename #####

| Environment Variable | Details |
|---|---|
| EventType | Rename |
| Series_Id | Internal ID of the series |
| Series_Title | Title of the series |
| Series_Path | Full path to the series |
| Series_TvdbId | TVDB ID for the series |

### Specific usage tips ###
#### PHP ####
The information from Sonarr will not be added to $_ENV as one might expect but should be included in the [$_SERVER variable](https://secure.php.net/manual/en/reserved.variables.server.php). A sample script to use this information to convert a file can be found [here](https://gist.github.com/karbowiak/7fb38d346e368edc9d1a).
#### PowerShell ####
Sample script using the Sonarr environment variables to create EDL files for all episodes is [here](https://gist.github.com/RedsGT/e1b5f28e7b5b81e1e45378151e73ba5c).  