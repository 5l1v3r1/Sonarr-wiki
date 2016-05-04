The following instructions are for installing Sonarr on CentOS 7.

Please note these were the steps taken by an experienced user.

*If you don't feel like fighting SELinux

    setenforce 0

*And to ensure it stays that way

    vi /etc/selinux/config
    Find the value enforcing, and change to disabled

*Install some repos and packages

    yum install epel-release yum-utils -y
    rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
    yum-config-manager --add-repo http://download.mono-project.com/repo/centos/
    yum install mediainfo libzen libmediainfo curl gettext mono-core mono-devel sqlite.x86_64 -y

*Add a user for sonarr to use

    useradd sonarr -s /sbin/nologin

*Download, extract and move sonarr

    wget http://update.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz
    tar -xvf ~/NzbDrone.master.tar.gz -C /opt/
    rm -f NzbDrone.master.tar.gz
    mv /opt/NzbDrone /opt/sonarr

*Change ownership of the install directory

    chown -R sonarr:sonarr /opt/sonarr

*Create your systemd unit file

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



*Now move the unit file to the proper location

    mv sonarr.service /usr/lib/systemd/system/

*Add firewall exceptions if the firewall is enabled

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

*Enable sonarr to run on startup, and start!

    systemctl enable sonarr.service
    systemctl start sonarr.service
