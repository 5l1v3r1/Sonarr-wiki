## Completed Download Handling vs Drone Factory

##### Pros:

- Doesn't scan your hard drive every minute for new downloads to complete
- Waits for files to be extracted by your download client and post-processing script run before attempting to move it (should eliminate issues with partially extract files being moved)
- Tracks downloads through post processing state (instead of showing as missing until its imported)
- Gets the file path to the download directly via the api, so the user doesn't have to configure it in drone.
- Better scene name handling. We can attach the actual scene name to database instead of the file name which can be pretty cryptic at times

##### Cons:
- Requires NzbDrone and your download client to be on the same machine (they can be on different machines as long as both drone and your download client see the exact same path (not just the same location)

## Migration Scenarios

Depending on your current configuration you may have to deal with one of the following scenarios.
The health check link will attempt to direct you to the scenario specific for your configuration.

#### Sabnzbd: Enable Completed Download Handling

Steps:

1. Create a new category with different output path and select that category in the NzbDrone SABnzbd settings page.  
   Do **not** adjust the Drone Factory Folder to use the same path.  

2. Once that's done you're ready to enable Completed Download Handling.

#### Nzbget: Conflicting Download Client Category

_Your Download Client is configured to use a category which put completed downloads in the Drone Factory._

Steps:

1. Create a new category with different output path and select that category in the NzbDrone Nzbget settings page.  
   Do **not** adjust the Drone Factory Folder to use the same path.

2. Once that's done you're ready to enable Completed Download Handling. 

#### Nzbget: Enable Completed Download Handling

_NzbDrone didn't detect any potential conflicts with your configuration. So you should be ready to enable Completed Download Handling._

Steps:

1. Enable Completed Download Handling by toggling the switch on the NzbDrone Settings -> Download Client page.  

#### Unsupported: Download Client on Different Computer

_As mentioned earlier, Completed Download Handling gets the file path to the download directly from the Download Client. Such a path is inaccessible from different computers and would prevent Completed Download Handling from importing the download._

The best solution to this problem is to run NzbDrone and your Download Client on the same computer.

_There are some advanced options to work around this limitation, but those will not be discussed here_

## Keeping Completed Download Handling disabled

If you absolutely want to keep using the Drone Factory:

1. Enable Completed Download Handling and Save.  
2. Disable Completed Download Handling and Save.  

This will permanently remove the warning.

## Advanced Configuration/Migration Options

The above scenarios were written to avoid complex choices. If you're a Power User you might want to have a couple of different options:

* Change the Drone Factory folder to a different path. (this is actually what I did)  
  You still have to remove the Drone Factory Post-Processing script, if you previously used it.

* Change the output path of your existing category.  
  You still have to remove the Drone Factory Post-Processing script, if you previously used it.

* Simply disable the Drone Factory entirely.  
  You still have to remove the Drone Factory Post-Processing script, if you previously used it.

Not creating a new category may cause a couple of old imported downloads to show up as queued, removing them from the Download Client history resolves that.

_As you can see, these are quite a number of choices and potential issues we tried to avoid by providing a couple of basic steps._





















 