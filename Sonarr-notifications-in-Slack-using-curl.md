I use Slack for my notifications. You can do this easily with the custom script connection already implemented. My solution will work pretty much out of the box on POSIX type OS with curl installed.

So it is simple to setup on any Linux or OS X machine.

If you are running Sonarr on Windows there may be a  way with Cygwin / bash / curl but I'd look for a cleaner solution.

## Setup a Slack Webhook intergration

Setup a webhook integration for your slack team here:

https://my.slack.com/services/new/incoming-webhook/

After you make the webhook it will give you a "Webhook URL" that looks something like this:

    https://hooks.slack.com/TXXXXX/BXXXXX/XXXXXXXXXX
    
## Create a bash script with curl command

Next create a new bash script with this code:

    #!/bin/bash
    curl -X POST --data-urlencode "payload={\"username\": \"Sonarr\", \"icon_emoji\": \":ghost:\", \"text\": \"$sonarr_eventtype: $sonarr_series_title S$sonarr_episodefile_seasonnumber E$sonarr_episodefile_episodenumbers ($sonarr_episodefile_quality)}" $1

I put mine in `~/scripts/sonarr/` and named it `slack.sh`

* You can edit the icon_emoji filed and match any emoji you have in slack, I added a custom one for sonarr.
* You can change up the text filed in the curl command to be whatever you want. You can insert any variable provided by Sonarr custom script by pre-pending it with `$sonarr_` and making everything lowercase. A complete list of variables can be found here. https://github.com/Sonarr/Sonarr/wiki/Custom-Post-Processing-Scripts

Now set the permissions so it can be executed by everyone, you can modify this if you know what user Sonarr runs under on your system.

    > chmod a+x ~/scripts/sonarr/slack.sh

## Create custom script connection in Sonarr

From the Sonarr web interface go to Settings -> Connect

Add a Custom Script connection

    Name: Slack
    Path: <put full path to slack.sh here>
    Arguments: <put your SLack Webhook URL here>
    
Example:

    Name: Slack
    Path: /Users/nzb/scripts/sonarr/slack.sh
    Arguments: https://hooks.slack.com/TXXXXX/BXXXXX/XXXXXXXXXX

Set your notification preferences and save.