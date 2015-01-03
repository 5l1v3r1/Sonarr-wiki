These are guidelines that should help determine the appropriate log level and method when logging events.

## Levels ##

### Fatal ###
Sonarr has failed completely, or will be operating in a diminished state.


### Error ###
Sonarr was preventing from doing something and the user may need to take action to correct it (Unable to connect to an external service), Sonarr will be unable to operate normally.


### Warning ###
Sonarr was unable to perform an action, but the result doesn't prevent Sonarr from operating normally.


### Info ###
Informational messages, to let the user know something normal/good has happened.


### Debug ###
Use for debugging purposes, more information than most users will be con concerned with.


### Trace ###
System level messages, or when logged information is not required for normal debugging.


## Progress ##
Sends logging messages to the UI when jobs are running (searching, updating information, etc), used to tell the user something is happening in the background, without having to look at log files.


## Cleansed ##
Use to clean log messages before logging, currently it will clean API keys from messages before the message is saved. 