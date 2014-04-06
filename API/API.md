## URL ##

All API endpoints are based off of `/api` if you access drone via `http://localhost:8989` the API root would be `http://localhost:8989/api`


## Authentication ##

All requests made to the api endpoint require API Key authentication using the X-Api-Key header.

### API Key ###

- Can be accessed and reset via Settings -> General
- Stored in Config.xml
- alpha-numeric (lower case)

## Dates & Times ##

- All dates/timestamps are ISO-8601 formatted in UTC `2014-01-27T01:30:00Z`
- Episodes (and episode based endpoints, missing & calendar) also include the airdate in the original timezone for display purposes
- Date parameters should be ISO-8601 UTC dates to ensure proper handling by drone


