## What is a profile ##
A profile controls what file qualities you want for a series, it lets you decide whether or not you want SDTV or HDTV only and if you eventually want episodes in DVD or Bluray. Sonarr ships with a few default profiles, but you're able to edit and create your own to match your preferences. Sonarr uses your profile when considering a release for grabbing.

![Profile editor from Sonarr v2.0.0.3258](http://i.imgur.com/CxLB3lW.png)
## What makes a profile? ##

A profile is a ranked list of qualities, along with a 'cutoff' quality.

#### Allowed ####
An allowed quality is one that is acceptable for Sonarr to download. If the box next to a quality is checked, that quality is allowed.

#### Cutoff ####

Select the cutoff ranking from the dropdown menu. This ranking is corresponding to an entry in 'Qualities' ranking selected below.

Once a file on your disk meets or exceeds this cutoff ranking, Sonarr will stop looking for upgrades to your existing file.

#### Qualities (Ranking) ####

Drag the qualities so that they are arranged with your most-desired quality at the top of the list, and your least-desired quality at the bottom of the list. _Advanced settings must be shown to reorder the qualities._

Sonarr will download any allowed quality, and continue to upgrade the file on your disk if a new release is found that is higher ranked within your profile.


## Examples ##
In all examples the preference for quality is top down (qualities higher in the list are more preferred).

### SDTV ###
Default SDTV profile.

##### Allowed #####
DVD  
SDTV

###### Cutoff ######
SDTV

##### Scenario 1 #####
No existing file exists. When Sonarr finds a release for this episode it will accept either SDTV or DVD, any other quality is rejected.

##### Scenario 2 #####
Existing file is SDTV. If a DVD release is found it will be rejected because the cutoff has already been met.

##### Scenario 3 #####
No existing files exists. A search is performed and both SDTV and DVD are available, Sonarr will grab the DVD release because it is the best allowed quality.


### HDTV 720p ###
Default HDTV 720p profile.

##### Allowed #####
Bluray 720p  
WEBDL 720p  
HDTV 720p

###### Cutoff ######
WEBDL 720p  


##### Scenario 1 #####
No existing file exists. if Sonarr finds a WEBDL 720p release it would grab it.

##### Scenario 2 #####
Existing file exists at HDTV 720p. If a Bluray720p release is found it will be grabbed because the cutoff has not been met

##### Scenario 3 #####
Existing file exists at WEBDL 720p. If a Bluray720p release is found it will not be grabbed because the cutoff has been met.

## Advanced Examples ##
These examples show the power of a quality profile that has had the quality orders adjusted, they should only be used if you understand the pros and cons of this action.

### HDTV with DVD archive ###
Want to watch in HDTV 720p the first time, but want to save disk space when archiving the file for later watching.

##### Allowed #####
DVD  
HDTV 720p

###### Cutoff ######
DVD


##### Scenario 1 #####
No existing file exists. HDTV 720p release found and grabbed.

##### Scenario 2 #####
Existing file exists at HDTV 720p. DVD release is available and is grabbed because it is more desired than the HDTV 720p release.

##### Scenario 3 #####
No existing file exists. Episode is searched and both HDTV 720p and DVD are available, DVD release is grabbed because it is preferred.