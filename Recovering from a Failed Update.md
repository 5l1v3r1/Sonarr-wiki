### Purpose ###

We do everything we can to prevent issues when upgrading, but they occur, this will walk you through the steps of recovering your installation.

### Determine the issue ###
The single best place to look when Sonarr won't start after an update is to check your log files, before trying to start Sonarr again, grab your log files [[Log Files]].

##### Migration Issue #####
Migration errors won't be identical, but here is an example:

````
14-2-4 18:56:49.5|Info|MigrationLogger|*** 36: update_with_quality_converters migrating ***
14-2-4 18:56:49.6|Error|MigrationLogger|SQL logic error or missing database duplicate column name: Items
While Processing: "ALTER TABLE "QualityProfiles" ADD COLUMN "Items" TEXT"
````

### Resolving the issue ###
In the event of a migration issue there is much you can do immediately, if the issue is specific to you (or there are not yet any posts), please create a post of the forums, if there are others with the same issue, then rest assured we are working on it.

### Manually upgrading ###
Grab the latest release from https://sonarr.tv - if you're running the develop version you can get the latest release here: https://download.sonarr.tv/v2/develop/latest

Install the update (.exe) or extract (.zip) the contents over your existing installation and re-run Sonarr as you normally would.