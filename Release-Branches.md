- **master (Default):** Stable branch. It has been used by users on develop branch and it's not known to have any major issues.


- **develop:** The bleeding edge. Released as soon as code is committed and passed all automated tests, this build has not been used by us or users. There is no guarantee that it will even run in some cases. 

	*Use this branch only if you know what you are doing and are willing to get your hands dirty to recover a failed update.*

## How to change your branch ##

1. Go to Settings and then the General tab and show advanced settings (use the toggle by the save button).

2. Under the Development section change the branch name to `develop`

3. Save

### For Ubuntu/Debian ###

You probably should update your sources.list file too if you installed using aptitude/apt-get:

    deb http://update.nzbdrone.com/repos/apt/debian develop main

## Checking the release notes/changes ##

1. Go to System and then the Updates tab

2. The last 5 updates for that branch are shown here


## Installing a newer version ##

1. Go to System and then the Updates tab

2. Newer versions that are not yet installed will have an update button next to them, clicking that button will install the update.