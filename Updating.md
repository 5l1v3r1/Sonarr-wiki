## General ##

**Branch** - You can change the branch Sonarr will use to update, see [[Release Branches]] for more information.

## Windows ##

Windows has automatic updates without making any changes.

## Linux/OS X ##

Both Linux and OS X now have the ability to update directly from the UI or automatically, but it is not enabled by default.

### Options ###
**Automatic** - Enable automatic updating, please test the update process manually to ensure it will work for your setup before enabling

**Mechanism**
    - **Built-in** - Use Sonarr's own updater
    - **Script** - Use a custom external script to update Sonarr, it will need to take care of stopping and starting Sonarr during the update process

**Script** - Visible only when *Mechanism* is set to *Script* - Path to update script


### Update Process ###
Sonarr will download the update file, verify its integrity and extract it to a temporary location and call the chosen method. The update process will be be run under the same user that Sonarr is run under, it will need permissions to update the Sonarr files as well as stop/start Sonarr.

#### Built-in ####
The built-in method will backup Sonarr files and settings, stop Sonarr, update the installation and Start Sonarr, if your system will not handle the stopping of Sonarr and will attempt to restart it automatically it may be best to use a script instead. In the event of failure the previous version of Sonarr will be restarted.


#### Script ####
The script should handle the the same as the built-in updater, if you need to handle stopping and starting services (upstart/launchd/etc) you will need to do that here.