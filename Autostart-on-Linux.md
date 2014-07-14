# Autostart on Debian using init.d script

The instructions for Ubuntu/Debian did not seem to work for Debian very well, and the pid got lost whenever NzbDrone was restarted via the web-ui, so I've included my working script here init.d script here.

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
    # Short-Description: starts instance of NzbDrone
    # Description:       starts instance of NzbDrone using start-stop-daemon
    ### END INIT INFO
    
    ############### EDIT ME ##################
    # path to app
    APP_PATH=/home/nzbdrone/NzbDrone
    
    # user
    RUN_AS=nzbdrone
    
    # path to mono bin
    DAEMON=/usr/bin/mono
    
    # Path to store PID file
    PID_FILE=/var/run/nzbdrone/nzbdrone.pid
    PID_PATH=$(dirname $PID_FILE)
    
    # script name
    NAME=nzbdrone
    
    # app name
    DESC=NzbDrone
    
    # startup args
    EXENAME="NzbDrone.exe"
    DAEMON_OPTS=" "$EXENAME
    
    ############### END EDIT ME ##################
    
    NZBDRONE_PID=`ps auxf | grep NzbDrone.exe | grep -v grep | awk '{print $2}'`
    
    test -x $DAEMON || exit 0
    
    set -e
    
    echo $NZBDRONE_PID > $PID_FILE
    
    case "$1" in
      start)
            if [ -z "${NZBDRONE_PID}" ]; then
                    echo "Starting $DESC"
                    rm -rf $PID_PATH || return 1
                    install -d --mode=0755 -o $RUN_AS $PID_PATH || return 1
                    start-stop-daemon -d $APP_PATH -c $RUN_AS --start --background --pidfile $PID_FILE --exec     $DAEMON -- $DAEMON_OPTS
            else
                    echo "NzbDrone already running."
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
            start-stop-daemon -d $APP_PATH -c $RUN_AS --start --background --pidfile $PID_FILE --exec $DAEMON     -- $DAEMON_OPTS
            ;;
      *)
            N=/etc/init.d/$NAME
            echo "Usage: $N {start|stop|restart|force-reload}" >&2    
            exit 1
            ;;   
    
    esac
    
    exit 0
````    
    

**Update rc.d**

	sudo update-rc.d

**Start NzbDrone**

	sudo service nzbdrone start
