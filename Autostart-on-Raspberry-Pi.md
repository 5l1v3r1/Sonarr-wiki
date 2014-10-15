### Upstart script for Raspberry Pi
Using Upstart allows for more advanced features, such as start/stop and automatic restart if it would crash.

Install Upstart

    sudo apt-get install upstart

**Create the NzbDrone Upstart config file**
       
    sudo nano /etc/init/nzbdrone.conf

**Paste in the following code, changing the username (right click if using terminal)**
```bash
#author "HTPCGuides.com"
#description "Upstart Script to run Nzbdrone as a service on Ubuntu/Debian

#Set username for the process. Should probably be what you use for logging in
setuid pi
setgid pi

#Set mono directory
env MONO=/usr/bin/mono
#Set Nzbdrone directory
env DIR=/opt/NzbDrone

start on runlevel [2345]
stop on runlevel [016]

respawn

exec $MONO $DIR/NzbDrone.exe

```

Press <kbd>Ctrl</kbd>+<kbd>X</kbd> then <kbd>y</kbd> to save.

**Start NzbDrone**

	sudo start nzbdrone
