The following instructions are for installing Sonarr on CentOS 7.

Please note these were the steps taken by an experienced user.

*If you don't feel like fighting SELinux
<pre>setenforce 0</pre>
**And ensure it stays that way
***vi /etc/selinux/config
***change enforced to disabled

*Install some repos and packages
<pre>
yum install epel-release yum-utils -y
rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
yum-config-manager --add-repo http://download.mono-project.com/repo/centos/
yum install mediainfo libzen libmediainfo curl gettext mono-core mono-devel sqlite.x86_64 -y
</pre>
*Add a user for sonarr to use
<pre>useradd sonarr -s /sbin/nologin</pre>
*Download, extract and move sonarr
<pre>
wget http://update.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz
tar -xvf ~/NzbDrone.master.tar.gz -C /opt/
rm -f NzbDrone.master.tar.gz
mv /opt/NzbDrone /opt/sonarr
</pre>
*Change ownership of the install directory
<pre>chown -R sonarr:sonarr /opt/sonarr</pre>

*Create your systemd unit file
<pre>
cat > sonarr.service << EOF
[Unit]
Description=Sonarr Daemon
After=syslog.target network.target

[Service]
User=sonarr
Group=sonarr

Type=simple
ExecStart=/usr/bin/mono /opt/sonarr/NzbDrone.exe -nobrowser -data /opt/sonarr
TimeoutStopSec=20

[Install]
WantedBy=multi-user.target
EOF
</pre>
*Now move the unit file to the proper location
<pre>mv sonarr.service /usr/lib/systemd/system/</pre>

*Add firewall exceptions if the firewall is enabled
<pre>
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
</pre>
*enable sonarr to run on startup, and start!
<pre>
systemctl enable sonarr.service
systemctl start sonarr.service
</pre>