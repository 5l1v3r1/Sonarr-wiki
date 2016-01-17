**Completed Download Handling** is how Sonarr imports media from your download client to your series folders. It replaced an older system called the **Drone Factory** in early 2015. Most setups should exclusively use Completed Download Handling.

#### How Completed Download Handling Works

1. Sonarr will send a download request to your client, and associate it with a label or category name that you have configured in the download client settings. The default is 'tv'.
2. Sonarr will monitor your download clients active downloads that use that category name. It monitors this via your download client's API. 
3. When the download is completed, Sonarr will know the final file location as reported by your download client. This file location can be almost anywhere, as long as it is somewhere separate from your media folder. It also should not be the same as your Drone Factory folder, if you still use that system. Something like *C:\Downloads\Completed\TV* works well.
4. Sonarr will scan that completed file location for video files. It will parse the video file name to match it to a show, season, and episode. If it can do that, it will rename the file according to your specifications, and move it to the TV Series folder.
5. Leftover files from the download will be sent to your trash or recycling.

If you download using a BitTorrent client, the process is slightly different:
- Completed files are left in their original location to allow you to seed. When files are imported to your Series folder Sonarr by default will copy the video file, which uses twice the disk space. An advanced option to hardlink can be enabled (*Settings > Media Management > Importing*) which will attempt to hardlink the media to your Series folder. A hardlink will allow not use any additional disk space. If the hardlink creation fails, Sonarr will fall back to the default behavior and copy the file.
- If the "Completed Download Handling - Remove" option is enabled in Sonarr's settings, Sonarr will delete the original file and torrent from your client, but **only** if the client reports that seeding is complete and torrent is stopped. 


#### Completed Download Handling vs Drone Factory

##### Pros:

- Doesn't scan your hard drive every minute for new downloads to complete
- Waits for files to be extracted by your download client and post-processing script run before attempting to move it (should eliminate issues with partially extract files being moved)
- Tracks downloads through post processing state (instead of showing as missing until its imported)
- Gets the file path to the download directly via the api, so the user doesn't have to configure it in Sonarr.
- Better scene name handling. We can attach the actual scene name to database instead of the file name which can be pretty cryptic at times

##### Cons:
- Requires Sonarr and your download client to be on the same machine or the remote file system mounted locally and remapped in Sonarr with Remote Path Mapping.

#### Migrating to Completed Download Handling from Drone Factory

Depending on your current configuration you may have to deal with one of the following scenarios.
The health check link will attempt to direct you to the scenario specific for your configuration.

###### Sabnzbd: Enable Completed Download Handling

Steps:

1. Create a new category with different output path and select that category in the Sonarr SABnzbd settings page.  
   Do **not** adjust the Drone Factory Folder to use the same path.  

2. Once that's done you're ready to enable Completed Download Handling.

###### Nzbget: Conflicting Download Client Category

_Your Download Client is configured to use a category which put completed downloads in the Drone Factory._

Steps:

1. Create a new category with different output path and select that category in the Sonarr Nzbget settings page.  
   Do **not** adjust the Drone Factory Folder to use the same path.

2. Once that's done you're ready to enable Completed Download Handling. 

###### Nzbget: Enable Completed Download Handling

_Sonarr didn't detect any potential conflicts with your configuration. So you should be ready to enable Completed Download Handling._

Steps:

1. Enable Completed Download Handling by toggling the switch on the Sonarr Settings -> Download Client page.  

###### Unsupported: Download Client on Different Computer

_As mentioned earlier, Completed Download Handling gets the file path to the download directly from the Download Client. Such a path is inaccessible from different computers and would prevent Completed Download Handling from importing the download._

The best solution to this problem is to run Sonarr and your Download Client on the same computer.

_There are some advanced options to work around this limitation, but those will not be discussed here_

##### Keeping Completed Download Handling disabled

If you absolutely want to keep using the Drone Factory:

1. Enable Completed Download Handling and Save.  
2. Disable Completed Download Handling and Save.  

This will permanently remove the warning.

##### Advanced Configuration/Migration Options

The above scenarios were written to avoid complex choices. If you're a Power User you might want to have a couple of different options:

* Change the Drone Factory folder to a different path. (this is actually what I did)  
  You still have to remove the Drone Factory Post-Processing script, if you previously used it.

* Change the output path of your existing category.  
  You still have to remove the Drone Factory Post-Processing script, if you previously used it.

* Simply disable the Drone Factory entirely.  
  You still have to remove the Drone Factory Post-Processing script, if you previously used it.

Not creating a new category may cause a couple of old imported downloads to show up as queued, removing them from the Download Client history resolves that.

_As you can see, these are quite a number of choices and potential issues we tried to avoid by providing a couple of basic steps._





















 