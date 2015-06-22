Installing Sonarr on FreeBSD isn't hard, but does require several commands.  If you aren't familiar with Unix or Linux, this guide should hopefully be enough to get you up and running.  This guide was adapted from the original FreeNAS 9.2.1.9 guide, and tested under FreeBSD 10.1-RELEASE.

First thing you'll need to do is create a new jail in FreeNAS, just the default settings, give it a name and create.

Next you'll need to get a command line shell into that jail.  There are 2 options for this. Either SSH into your FreeNAS box, run 'jls' to find your jail #, and then 'jexec # csh' OR you can shell into your jail via the jails tab in the FreeNAS GUI (find the little button at the bottom that looks like a command prompt). Either way you need to be sitting at a shell for your jail. The next steps are commands to run.

```
mv /usr/local/etc/pkg.conf /usr/local/etc/pkg.conf.backup
pkg install mono mediainfo sqlite3
cd
fetch http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz
tar -xzvf NzbDrone.master.tar.gz
ee /etc/rc.d/run_drone
```

Ok at this point you now have a text editor open, you'll want to copy and the paste the following line into the editor and then continue with the commands:

`/usr/local/bin/mono /root/NzbDrone/NzbDrone.exe --nobrowser &`

* Hit Esc, Enter, Enter to leave editor and save changes.

`chmod 555 /etc/rc.d/run_drone`

At this point Sonarr is installed, and we have it set to start with the Jail.  So go ahead and stop, and then start the jail in FreeNAS GUI. Hit up http://jail-ip:8989 Should be good to go.

If you are wondering what is going on in the commands, here's a brief rundown. FreeNAS 9.2 may have an older version of pkg installed. By moving the configuration file, it will heal itself and just work™. Then we install mono, mediainfo, sqlite3 and all their required dependencies, including perl.  Next up is Sonarr itself.  Grab the files and extract, simple enough.  Lastly we need to get Sonarr launching at boot, so we make a small script in rc.d which gets run at boot.

Unix experts will see that this is very hacky and insecure, especially as everything is running as root and listening on all IPs by default, although this should be fine in a jail.  You are welcome to clean this up a bit, I was optimizing for ease of installation more than anything.