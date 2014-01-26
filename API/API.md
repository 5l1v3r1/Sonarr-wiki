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