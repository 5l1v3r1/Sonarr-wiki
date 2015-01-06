Installing Sonarr on FreeNAS isn't hard, but does require several commands.  If you aren't familiar with Unix or Linux, this guide should hopefully be enough to get you up and running.  This guide was made using FreeNAS 9.2.1.9.

First thing you'll need to do is create a new jail in FreeNAS, just the default settings, give it a name and create.

Next you'll need to get a command line shell into that jail.  There are 2 options for this. Either SSH into your FreeNAS box, run 'jls' to find your jail #, and then 'jexec # csh' OR you can shell into your jail via the jails tab in the FreeNAS GUI (find the little button at the bottom that looks like a command prompt). Either way you need to be sitting at a shell for your jail. The next steps are commands to run.

```
mv /usr/local/etc/pkg.conf /usr/local/etc/pkg.conf.backup
pkg install nano
pkg install mono
pkg install mediainfo
cd
fetch http://www.sqlite.org/2014/sqlite-autoconf-3080704.tar.gz
tar -xzvf sqlite-autoconf-3080704.tar.gz
cd sqlite-autoconf-3080704
set CPPFLAGS="-DSQLITE_ENABLE_COLUMN_METADATA"
./configure CFLAGS=-DSQLITE_ENABLE_COLUMN_METADATA
make
make install
cd
fetch http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz
tar -xzvf NzbDrone.master.tar.gz
nano /etc/rc.d/run_drone
```

Ok at this point you now have a text editor open, you'll want to copy and the paste the following line into the editor and then continue with the commands:

`/usr/local/bin/mono /root/NzbDrone/NzbDrone.exe --nobrowser &`

* Hit Ctrl+X and then hit the 'Y' key.

`chmod 555 /etc/rc.d/run_drone`

At this point Sonarr is installed, and we have it set to start with the Jail.  So go ahead and stop, and then start the jail in FreeNAS GUI. Hit up http://jail-ip:8989 Should be good to go.

If you are wondering what is going on in the commands, here's a brief rundown. FreeNAS 9.2 may have an older version of pkg installed. By moving the configuration file, it will heal itself and just work™. Then we install nano, mono, wget and mediainfo.  Nano is optional, it's just an wasy to use text editor so it made instructions easier, but you could use vi.  Next we install SQLite, problem is that the repo that pkg install uses has an outdated SQLite, and we need a special flag during compilation.  So we grab the source, extract, set the flags, configure, compile, and install.  Next up is Sonarr itself.  Grab the files and extract, simple enough.  Lastly we need to get Sonarr launching at boot, so we make a small script in rc.d which gets run at boot.

Unix experts will see that this is kinda hacky and insecure, especially as everything is running as root.  You are welcome to clean this up a bit, I was optimizing for ease of installation more than anything.