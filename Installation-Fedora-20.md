The following instructions are for installing Sonarr on Fedora 20.  The same method should work on Fedora 15-19 and RHEL 7 however I have not tested those environments.

For system v init based versions of Fedora (anything prior to 15), reference the [[CentOS 6]] guide.

Works on Fedora 21, however I suspect they will update the mono package for that distribution (check http://download.opensuse.org/repositories/home:/tpokorra:/mono/ for the repository.  At time of writing Fedora 21 had not yet been released.).  

Automatic/scary install script at the end.

### Install Sonarr

All commands run as root sudo -s if necessary.

**Add a non-root user (optional, but very recommended)**
```bash
groupadd sonarr
adduser -g sonarr -m -c "Sonarr User" -s /sbin/nologin  sonarr
```
Note that after install configuration options will be stored in /home/sonarr/.config/NzbDrone/.  You may use another user if you prefer, just be sure to change the options below.

**Verify selinux status**
	
```bash
getenforce
```
A common step that gets missed, since Sonarr doesn't have an selinux exception, we need to either disable selinux or set it to permissive mode.  If the command returns Permissive or disabled continue to the next step.
<br />  
If it is set to enforcing, you need to edit /etc/selinux/config and modify "SELINUX=enforcing" to read "SELINUX=permissive".
Then run:

```bash
setenforce Permissive
```

**Install Mono repository**

CentOS 7, Fedora 19, and derivatives
Add the Mono Project GPG signing key and the package repository in a root shell with:

```bash 
rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
yum-config-manager --add-repo http://download.mono-project.com/repo/centos/
```

Run a package upgrade to upgrade existing packages to the latest available. Then install Mono as described in the Usage section.

Users of CentOS or RHEL (or similar distributions) may need to add the EPEL repository to their system to satisfy all dependencies.

**Install prerequisites**
    
I set a symbolic link for mono, this step is optional. If you have applications that rely on the earlier version, skip the link creation step.

```bash
yum install mediainfo libzen libmediainfo curl gettext mono-opt mono-opt-devel sqlite.x86_64
ln -s /opt/mono/bin/mono /usr/bin/mono
```

**Download and extract Sonarr**
    
```bash
wget http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz
tar -xvf ~/NzbDrone.master.tar.gz -C /opt/
```

**Set Program directory ownership**
```bash
chown -R sonarr:sonarr /opt/NzbDrone
```


### Create Sonarr systemd Service and firewall rules

**Create systemd service file**
```bash
cat > sonarr.service << EOF
[Unit]
Description=Sonarr Daemon
After=syslog.target network.target

[Service]
User=sonarr
Group=sonarr

Type=simple
ExecStart=/opt/mono/bin/mono /opt/NzbDrone/NzbDrone.exe -nobrowser -data /opt/NzbDrone
TimeoutStopSec=20

[Install]
WantedBy=multi-user.target
EOF
mv sonarr.service /usr/lib/systemd/system/
```

**Add Sonarr to startup**

```bash
systemctl enable sonarr.service
```

**Start Sonarr service**

Start sonarr via systemd and verify status.
    
```bash
systemctl start sonarr.service
systemctl status sonarr.service
```
	
**Add a firewall rule**
    
```bash
cat > sonarr.xml << EOF
<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>sonarr</short>
  <description>Sonarr Download Service</description>
  <port protocol="tcp" port="8989"/>
</service>
EOF
mv sonarr.xml /etc/firewalld/services/
firewall-cmd --permanent --add-service sonarr
firewall-cmd --reload
```

**Open a web browser**
Open a web broswer and navigate to http://server:8989
	
## Automatic Install Script
Use at your own risk.
```bash
#!/bin/bash

groupadd sonarr
adduser -g sonarr -m -c "Sonarr User" -s /sbin/nologin  sonarr
wget -4 -O /etc/yum.repos.d/mono.repo http://download.opensuse.org/repositories/home:/tpokorra:/mono/Fedora_20/home:tpokorra:mono.repo
yum install mediainfo libzen libmediainfo curl gettext mono-opt mono-opt-devel sqlite.x86_64
ln -s /opt/mono/bin/mono /usr/bin/mono
wget http://download.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz
tar -xvf ~/NzbDrone.master.tar.gz -C /opt/
chown -R sonarr:sonarr /opt/NzbDrone
cat > sonarr.service << EOF
[Unit]
Description=Sonarr Daemon
After=syslog.target network.target

[Service]
User=sonarr
Group=sonarr

Type=simple
ExecStart=/opt/mono/bin/mono /opt/NzbDrone/NzbDrone.exe -nobrowser -data /opt/NzbDrone
TimeoutStopSec=20

[Install]
WantedBy=multi-user.target
EOF
mv sonarr.service /usr/lib/systemd/system/
systemctl enable sonarr.service
systemctl start sonarr.service
systemctl status sonarr.service
cat > sonarr.xml << EOF
<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>sonarr</short>
  <description>Sonarr Download Service</description>
  <port protocol="tcp" port="8989"/>
</service>
EOF
mv sonarr.xml /etc/firewalld/services/
firewall-cmd --permanent --add-service sonarr && firewall-cmd --reload

 ```