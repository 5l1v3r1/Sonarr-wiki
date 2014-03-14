**WARNING** Only follow these instructions if you understand the risks of doing so and know how to write and enable a post processing script in your download client

## Disable Drone Factory Folder Scanning ##

You can disable drone factory folder scanning via the advanced setting "Drone Factory Interval" on the download client settings page, by setting it to zero.

## Post Processing Script ##

You can configure your download client to run a script to send a command to NzbDrone's API instructing it to run a scan on the drone factory folder.

The script will need to send a POST with a JSON body as described here: [Command](Command#downloadedepisodesscancommand)

## Example Scripts ##

#### curl ####
````
curl http://localhost:8989/api/command -X POST -d '{"name": "downloadedepisodesscan"}' --header "X-Api-Key:YOUR_API_KEY_GOES_HERE"
````

#### PowerShell ####
````
$url = "http://8989/api/command"
$json = "{ ""name"": ""downloadedepisodesscan"" }"

Write-Host "Publishing update $version ($branch) to: $url"
Invoke-RestMethod -Uri $url -Method Post -Body $json -Headers @{"X-Api-Key"="YOUR_API_KEY_GOES_HERE"}
````
