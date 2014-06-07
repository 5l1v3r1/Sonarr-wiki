### Completed Download Handling vs Drone Factory ###

**TODO: Pro con **

### Migration Scenarios ###

Depending on your previous configuration you may have to deal with one of the following scenarios.
The health check link will attempt to direct you to the scenario specific for your configuration.

#### Conflicting Download Client Category ####

_Your Download Client is configured to use a category which put completed downloads in the Drone Factory._

Simplest solution is to create a new category with different output path and configure NzbDrone to use that category instead.  
Do not configure that category to use a Drone Factory post-processing script.

Once that's done you're ready to enable Completed Download Handling.

#### Enable Completed Download Handling ####

Enabling Completed Download Handling is as simple as toggling the switch on the NzbDrone Settings -> Download Client page.  
However, you may run into a couple of issues depending on your previous configuration.  
Primarily the one mentioned in _"Conflicting Download Client Category"_ above. Keep an eye out for Health Check warnings.

#### Unsupported: Download Client on Different Computer ####

_As mentioned earlier, Completed Download Handling gets the file path to the download directly from the Download Client. Such a path is inaccessible from different computers and would prevent Completed Download Handling from importing the download._

The best solution to this problem is to run NzbDrone and your Download Client on the same computer.

### Keeping Completed Download Handling disabled ###

If you absolutely want to keep using the Drone Factory, enable and subsequently disable Completed Download Handling to get rid of the warning.  

### Advanced Configuration/Migration Options ###

The above scenarios were written to avoid complex choices. If you're a Power User you might want to have a couple of different options:

1. Change the Drone Factory folder to a different path. (this is actually what I did)  
   You still have to remove the Drone Factory Post-Processing script, if you previously used it.

2. Can change the output path of your existing category.  
   You still have to remove the Drone Factory Post-Processing script, if you previously used it.

3. Can simply disable the Drone Factory entirely.  
   You still have to remove the Drone Factory Post-Processing script, if you previously used it.

Not creating a new category may cause a couple of old imported downloads to show up as queued, removing them from the Download Client history resolves that.

_As you can see, a couple of choices and potential issues we tried to avoid._





















 