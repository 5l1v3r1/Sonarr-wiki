# Autostart on Debian using init.d script

The instructions for Ubuntu/Debian did not seem to work for Debian very well, and the pid got lost whenever Sonarr was restarted via the web-ui, so I've included a working script here init.d script here. You'll need to have already created an nzbdrone user.

**Create and edit the nzbdrone init.d script**
       
    sudo vim /etc/init.d/nzbdrone

**Paste the following, changing applicable variables**       
````bash
        
#! /bin/sh
### BEGIN INIT INFO
# Provides:          NzbDrone
# Required-Start:    $local_fs $network $remote_fs
# Required-Stop:     $local_fs $network $remote_fs
# Should-Start:      $NetworkManager
# Should-Stop:       $NetworkManager
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts instance of Sonarr
# Description:       starts instance of Sonarr using start-stop-daemon
### END INIT INFO
    
############### EDIT ME ##################
# path to app
APP_PATH=/opt/NzbDrone
   
# user
RUN_AS=nzbdrone
    
# path to mono bin
DAEMON=/usr/bin/mono

# options for mono
DAEMON_OPTS=" "

# Path to store PID file
PID_PATH=/var/run/nzbdrone
############### END EDIT ME ##################

PID_FILE=${PID_PATH}/nzbdrone.pid
EXENAME=`basename ${APP_PATH}/NzbDrone.exe`
DESC=`basename ${APP_PATH}/NzbDrone.exe .exe`
NZBDRONE_PID=`ps auxf | grep $EXENAME | grep -v grep | awk '{print $2}'`

test -x $DAEMON || { echo "$DAEMON must be executable."; exit 1; }
    
set -e

if [ ! -e ${PID_PATH} ]; then
    mkdir ${PID_PATH}
fi

echo $NZBDRONE_PID > $PID_FILE
    
case "$1" in
start)
    if [ -z "${NZBDRONE_PID}" ]; then
        echo "Starting $DESC"
        rm -rf ${PID_PATH:?} || return 1
        install -d --mode=0755 -o $RUN_AS $PID_PATH || return 1
        start-stop-daemon -d $APP_PATH -c $RUN_AS --start --background --pidfile $PID_FILE --exec $DAEMON -- $DAEMON_OPTS $EXENAME
    else
        echo "${DESC} already running."
    fi
    ;;
stop)
    echo "Stopping $DESC"
    echo $NZBDRONE_PID > $PID_FILE
    start-stop-daemon --stop --pidfile $PID_FILE --retry 15
    ;;

restart|force-reload)
    echo "Restarting $DESC"
    start-stop-daemon --stop --pidfile $PID_FILE --retry 15
    start-stop-daemon -d $APP_PATH -c $RUN_AS --start --background --pidfile $PID_FILE --exec $DAEMON -- $DAEMON_OPTS $EXENAME
    ;;
*)
     echo "Usage: `basename $0` {start|stop|restart|force-reload}" >&2    
     exit 1
    ;;   
    
esac

exit 0
````    

**Make it executable**

	sudo chmod +x nzbdrone

**Update rc.d**

	sudo update-rc.d nzbdrone defaults

**Start Sonarr**

	sudo service nzbdrone start
