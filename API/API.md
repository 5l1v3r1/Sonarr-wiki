## URL ##

All API endpoints are based off of `/api` if you access drone via `http://localhost:8989` the API root would be `http://localhost:8989/api`


## Authentication ##

All requests made from a system other than localhost require authentication, either an API Key or Basic Authentication is supported, although it is recommended to use the API Key. Basic auth may be disabled on the API in a future version.

API Key uses the X-Api-Key header for authentication.

### API Key ###

- Recommended
- Found in Config.xml
- alpha-numeric (lower case)

### Basic Auth ###

- Not recommended
- Username & Password

## Dates & Times ##

- All dates/timestamps are ISO-8601 formatted in UTC `2014-01-27T01:30:00Z`
- Episodes (and episode based endpoints, missing & calendar) also include the airdate in the original timezone for display purposes
- Date parameters should be ISO-8601 UTC dates to ensure proper handling by drone


