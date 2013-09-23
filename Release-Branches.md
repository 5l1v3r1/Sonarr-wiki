- **master (Default):** Stable branch. It has been used by users on develop branch and it's not known to have any major issues.


- **develop:** The bleeding edge. Released as soon as code is committed and passed all automated tests, this build has not been used by us or users. There is no guarantee that it will even run in some cases. 

	*Use this branch only if you know what you are doing and are willing to get your hands dirty to recover a failed update.*

 




## How to change your branch ##

In order to change your update branch you will need to make a small configuration change:

Use your XML editor of choice to edit `C:\ProgramData\NzbDrone\config.xml` and set it to branch of your choosing
 

```xml
<Config>
   <Branch>master</Branch>
</Config>
```

**Once you make this change you will need to restart NzbDrone for it to take effect.**