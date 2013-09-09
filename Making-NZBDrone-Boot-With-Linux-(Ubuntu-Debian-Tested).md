### Upstart (Ubuntu/Debian based distros)
Using Upstart allows for more advanced features, such as start/stop and automatic restart if it would crash.

**Create the NzbDrone Upstart config file**
       
    sudo nano /etc/init/nzbdrone.conf

**Paste in the following code, changing the username (right click if using terminal)**
```bash
author "Simon Tallmyr - Nosscire"
description "Upstart Script to run NzbDrone as a service on Ubuntu/Debian based systems, as well as others"

#Set username for the process. Should probably be what you use for logging in
setuid yourusername

#This is the install directory. If you installed using a deb package or the NzbDrone Repository you do not need to change this
env DIR=/opt/NzbDrone

setgid nogroup
start on runlevel [2345]
stop on runlevel [016]

expect fork
respawn

script
   mono $DIR/NzbDrone.exe
end script
```

Press `ctrl+x` then `y` to save.

**Start NzbDrone**

	sudo start nzbdrone


###RC.Local
**Please Note: This is not the most elegant solution but it works**
***


This Guide is to help those who would like to use linux to run NZBDrone at time of writing this there is not "Install As Service" option like with the Windows Build so this needs to be done until a better alternative is found i have personally tested it so you should have no issues if you do please post in the NZBDrone Forums (http://forums.nzbdrone.com/) and someone will try and help you.

**First **
make sure NzbDrone is installed you can go here to find out how to do that https://github.com/NzbDrone/NzbDrone/wiki/Installation

Next I created a .sh or batch file to automate the process of type "sudo mono /opt/NzbDrone/NzbDrone.exe"
Here is a link to the batch file so it saves you all from having to do this even though it was easy if you open in a text editor you will see

**Batch File:** (Just Hit Download to grab it)
http://goo.gl/4c8yWg

Next there are two ways of doing this 

**Method One:**

is using rc.local you do this by opening a terminal windows and typing (without quotes) "sudo nano /etc/rc.local" (or if easier you can use a text editor like gedit, pluma, leafpad whatever you have just replace the nano part with what you want

Once this is open go to the bottom and just above where it says "exit 0" type the following for eg.

/bin/sh /home/server/Desktop/NzbDrone.sh

mine was saved to my desktop on my linux machine you will need to edit this to wherever you put the NzbDrone.sh file you downloaded above but remember to keep the /bin/sh first then a space then the rest

**Method Two:** (With Screenshots)

Go to your menu and find the application to set startup items this may be called many things mine was called Session And Startup

http://i.imgur.com/qqw8ghT.png

Once this is open i went to Application AutoStart there i clicked on the add button

http://i.imgur.com/FqVFXEQ.png

Next i added the following which you will notice is the same as the one in Method One "/bin/sh /home/server/Desktop/NzbDrone.sh"

http://i.imgur.com/8gokS5j.png

after that i gave it a name and then pressed "Ok" and then "Close" i then did a reboot of the system 

on reboot i did notice it took a couple more seconds to login this is because this is setting that command to run at login but once logged in i opened my browser and went to http://localhost:8989 and voila it started


I cannot guarantee this will work but it seems to be working for me i am Linux newbie and this took me a while to figure out so hopefully by posting here it will help someone else avoid the trouble i went through 