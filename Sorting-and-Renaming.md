## Terminology
**Completed Download Folder:**  This is the folder where your download client places completed downloads (best if it only contains TV shows)

**Completed TV Download Folder:** Completed folder that only contains TV shows

**Drone Factory:** This needs to be the same as the Completed Download Folder (you should never use a folder that contains sorted and renamed episodes)

## SABnzbd
- Disable TV sorting (Config -> Sorting -> Series Sorting)
- Create a category for TV shows
- Configure NzbDrone to use the TV category

## NzbDrone
- The TV category for your download client (if applicable)
- The Drone Factory folder to be the same as your download client's *Completed Download Folder*/*Completed TV Download Folder* (if you're using a category with SABnzbd this needs to be the *Completed TV Download Folder* see SABnzbd's category config page for the path)

## The Import Process ##
NzbDrone does a number of checks to verify that the download is acceptable for importing, including:
- Sample file check (run time is longer than 90 seconds)
- Upgrade for existing episode file (if any)
- Not being unpack by the download client (_UNPACK_ in SABnzbd)
- Enough free space exists at the destination

Once a file has passed all those checks it is imported,  if there is an existing file it is deleted, otherwise the episode file is moved and renamed (according to your naming rules). Once the file has been moved it removes the source folder as long as it is less than 70MB in size). **If no files are imported nothing is deleted**.