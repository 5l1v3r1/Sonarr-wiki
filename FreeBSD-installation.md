Installing Sonarr on FreeBSD isn't hard, but does require several commands.  If you aren't familiar with Unix or Linux, this guide should hopefully be enough to get you up and running.  This guide was tested under FreeBSD 10.1-RELEASE.

If you want to do this safely, install and run it inside a [FreeBSD jail](https://www.freebsd.org/doc/handbook/jails.html).

```
mv /usr/local/etc/pkg.conf /usr/local/etc/pkg.conf.backup
pkg install mono mediainfo sqlite3
cd
fetch http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz
tar -xzvf NzbDrone.master.tar.gz
ee /etc/rc.d/run_drone
```

At this point you have a text editor open. Copy and the paste the following line into the editor:

`/usr/local/bin/mono /root/NzbDrone/NzbDrone.exe --nobrowser &`

* Hit Esc, Enter, Enter to leave editor and save changes.

`chmod 555 /etc/rc.d/run_drone`

At this point Sonarr is installed, and we have it set to start on boot. You can execute run_drone, reboot the system or restart the jail if installed into one.

If you are wondering what is going on in the commands, here's a brief rundown. FreeBSD may have an older version of pkg installed and by moving the configuration file, it will heal itself and just work. Although this should not be necessary on newer versions of FreeBSD. Then we install mono, mediainfo, sqlite3 and all their required dependencies, including perl.  Next up is Sonarr itself.  Grab the files and extract, simple enough.  Lastly we need to get Sonarr launching at boot, so we make a small script in rc.d which gets run at boot.

Unix experts will see that this is very hacky and insecure, especially as everything is running as root and listening on all IPs by default, so it's a really good idea to put this inside a jail.