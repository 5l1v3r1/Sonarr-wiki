If you're looking to trigger a custom script in your download client to tell Sonarr when to update, you can find more details here: 

### Overview ###

Sonarr can execute a custom script when new episodes are imported or a series is renamed, depending on the which action occurred the parameters will be different. Parameters are passed to the script through environment variables (allowing for more flexibility in what we send to the script and not having to worry about a particular order). In all cases the Environment Variables Sonarr sends will be prefixed with `Sonarr` so, the `EventType` Sonarr sends would be `Sonarr.EventType`.

### Environment Variables ###

##### On Download/On Upgrade #####

| Environment Variable | Details |
|---|---|
| EventType | Download |
| Series.Id | Internal ID of the series |
| Series.Title | Title of the series |
| Series.Path | Full path to the series |
| Series.TvdbId | TVDB ID for the series |
| EpisodeFile.Id | Internal ID of the episode file |
| EpisodeFile.RelativePath | Path to the episode file relative to the series' path |
| EpisodeFile.Path | Full path to the episode file |
| EpisodeFile.SeasonNumber | Season number of episode |
| EpisodeFile.EpisodeNumbers | Comma separated list of episode numbers |
| EpisodeFile.EpisodeAirDates | Air date from original network |
| EpisodeFile.EpisodeAirDatesUtc | Air Date with Time in UTC |
| EpisodeFile.Quality | Quality name from Sonarr |
| EpisodeFile.QualityVersion | 1 is the default, 2 for proper, 3+ could be used for anime versions |
| EpisodeFile.ReleaseGroup | Release group, will not be set if it is unknown |
| EpisodeFile.SceneName | Original release name |

##### On Rename #####

| Environment Variable | Details |
|---|---|
| EventType | Rename |
| Series.Id | Internal ID of the series |
| Series.Title | Title of the series |
| Series.Path | Full path to the series |
| Series.TvdbId | TVDB ID for the series |

### Specific usage tips ###
#### PHP ####
The information from Sonarr will not be added to $_ENV as one might expect but should be included in the [$_SERVER variable](https://secure.php.net/manual/en/reserved.variables.server.php). A sample script to use this information to convert a file can be found [here](https://gist.github.com/karbowiak/7fb38d346e368edc9d1a).