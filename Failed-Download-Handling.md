Failed Download Handling is compatible with SABnzbd and NZBGet.

There are a couple components that make up the failed download handling process:

1) **Check Downloader**:

a. Queue - Check your downloader's queue for password-protected (encrypted) releases
b. History - Check your downloader's history for failure (eg. not enough to repair, or extraction failed)

When Sonarr finds a failed download it starts processing them and does a few things:

1. Adds a failed event to Sonarr's history
2. Removes the failed download from Download Client to free space and clear downloaded files (optional)
3. Starts searching for a replacement file (optional)

2) **Blacklisting**
Allows automatic skipping of nzbs when they fail, this means that nzb will not be automatically downloaded by Sonarr ever again (You can still force the download via a manual search).

There are 2 advanced options (on 'Download Client' settings page) that control the behavior of failed downloading in Sonarr, at this time, they are all on by default.

* Redownload - Controls whether or not Sonarr will search for the same episode after a failure
* Remove - Whether or not the download should automatically be removed from Download Client when the failure is detected