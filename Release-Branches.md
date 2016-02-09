- **master (Default/Stable):** It has been tested by users on develop branch and it's not known to have any major issues.


- **develop (Nightly):** The bleeding edge. Released as soon as code is committed and passed all automated tests, this build may have not been used by us or other users. There is no guarantee that it will even run in some cases. ***Use this branch only if you know what you are doing and are willing to get your hands dirty to recover a failed update.***

## How to change your branch ##

#### For Built-In Updater ####

1. Go to Settings and then the General tab and show advanced settings (use the toggle by the save button).

2. Under the Development section change the branch name to `develop`

3. Save

_This will not install the bits from that branch immediately, it will happen during the next update._

#### For Ubuntu/Debian aptitude/apt-get ####

You probably should update your sources.list file too if you installed using aptitude/apt-get:

    deb http://apt.sonarr.tv/ develop main

## Installing a newer version ##

1. Go to System and then the Updates tab

2. Newer versions that are not yet installed will have an update button next to them, clicking that button will install the update.

## Can I switch from develop back to master?##
We don't recommend manually switching back to master, since other branches are commonly running newer code which might not be compatible with the older code in master.
We have plans to mitigate this in the future.