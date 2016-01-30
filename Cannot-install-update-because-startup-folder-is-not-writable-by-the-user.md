Check the folder permissions. Can your user read/write the folder? The default startup folder when installed under Ubuntu 14.04 is /opt/NzbDrone/ but you can verify that by browsing to the System/Status page in Sonarr.

If the user doesn't have write access, the simple solution is to make your user the owner of the startup folder. Where **_user_** equals the account that runs Sonarr, run this command:

`sudo chown -hR user /opt/NzbDrone/`