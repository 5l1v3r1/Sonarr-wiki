## URL ##

All API endpoints are based off of `/api` if you access Sonarr via `http://localhost:8989` the API root would be `http://localhost:8989/api`


## Authentication ##

All requests made to the api endpoint require API Key authentication using the X-Api-Key header or using the apikey query string.

### API Key ###

- Can be accessed and reset via Settings -> General
- Stored in Config.xml
- alpha-numeric (lower case)

## Dates & Times ##

- All dates/timestamps are ISO-8601 formatted in UTC `2014-01-27T01:30:00Z`
- Episodes (and episode based endpoints, missing & calendar) also include the airdate in the original timezone for display purposes
- Date parameters should be ISO-8601 UTC dates to ensure proper handling by Sonarr

## Content Type ##

- All POST/PUT requests require all parameters to be JSON encoded in the body, unless otherwise noted.
- All GET requests will return a JSON encoded response

## Endpoints ##

- [[Calendar]]
- [[Command]]
- [[Diskspace]]
- [[Episode]]
- [[EpisodeFile]]
- [[History]]
- [[Missing]]
- [[Queue]]
- [[QualityProfile]]
- [[Release]]
- [[Rootfolder]]
- [[Series]]
- [[Series-Lookup]]
- [[System-Status]]
