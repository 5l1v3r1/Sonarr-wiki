## Series ##

If a series is monitored then the episodes in that series can be grabbed, depending on their monitored state. If a series is not monitored then no episodes in that series will be grabbed.

Series' can be be set as monitored from the following locations in Sonarr:

- Series Details
	- Use the bookmark icon to the left of the the title.
- Series Editor
	- Select one or more series and use the drop down before pressing save.
- Season Pass
	- Use the bookmark icon to the left of the title.

## Season ##
	
Unmonitoring a season will unmonitor the episodes in that season, both current and future. If a season is unmonitored then the episodes within that season can still be marked as monitored. These episode will not be blocked in the same way as when a series is unmonitored.

A season's monitored state can be toggled from the following locations within Sonarr:

- Series Details
	- Use the bookmark icon to the left of the season header
- Season Pass
	- Quickly toggle one or more seasons, expand the series to control seasons individually

## Episode ##

If you came here looking for an answer why Sonarr does not automatically search for missing episodes, please view the [FAQ](https://github.com/Sonarr/Sonarr/wiki/FAQ#why-doesnt-nzbdrone-automatically-search-for-missing-episodes).


If an episode is not monitored then it will not be grabbed, regardless of the monitored state of the series. If an episode is monitored and the series is not, it will be considered unmonitored.

An episode's monitored state can be toggled from the following locations within Sonarr:

- Series Details
	- Use the bookmark icon next to the episode number on the left side
- Episode Details Modal (popup)
	- Use the bookmark icon to the left of the modal header
		- Can be toggled from any location that opens the episode details modal