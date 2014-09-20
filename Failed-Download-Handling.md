Failed Download Handling is compatible with SABnzbd and NZBGet.

There are a couple components that make up the failed download handling process:

1) Check SABnzbd Queue and History for failed downloads

a. Queue - Encrypted (passworded) as detected by SAB
b. History - Failed, whatever the reason, not enough to repair or extraction failed

When drone finds a failed download it starts processing them and does a few things:

1. Adds a failed event to drone's history
2. Removes the failed download from SAB to free space (opt out)
3. Starts searching for a replacement file (opt out)

2) Blacklisting
Allows automatic skipping of nzbs when they fail, this means that nzb will not be automatically downloaded by drone ever again (You can still force the download via a manual search).

There are 3 advanced options (on Download Client) that control the behavior of failed downloading in drone, at this time, they are all on by default.

Enable - Turns the checking of SAB and the blacklist functionality on or off
Redownload - Controls whether or not drone will search for the same episode after a failure
Remove - Whether or not the download should automatically be removed from SAB when the failure is detected