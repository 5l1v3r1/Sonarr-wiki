# Windows
1. Download the latest version of Sonarr from [https://sonarr.tv](https://sonarr.tv "https://sonarr.tv")
* Extract the zip file into your target directory. Use a folder that Sonarr process would have write access to (**DO NOT** use `C:\Program Files` or `C:\Program Files (x86)`)
* Run `NzbDrone.exe` once as administrator to register the port and URL with Windows (Required for remote access)<sup>1</sup>
* Manually start Sonarr by running `Nzbdrone.exe` or `ServiceInstall.exe` to install Sonarr as a Windows service.
* Open [http://localhost:8989](http://localhost:8989) in your browser


<sup>1</sup> The port will be opened on the firewall (if enabled) for the private profile only, if you're connected to a domain or a public network the port will not be opened automatically, but can be done so manually.

# OS X #
1. Download latest version of Sonarr's OSX package from [https://download.sonarr.tv/v2/master/2 latest/NzbDrone.master.osx.zip](http://download.sonarr.tv/v2/master/latest/NzbDrone.master.osx.zip)
* Open the archive and drag the Sonarr icon to your Application folder.
* Open Sonarr from your application folder
* You should now be able to access Sonarr at [http://localhost:8989](http://localhost:8989) 


# Linux #

### Debian/Ubuntu ###

**mono**

mono 3.10 is included for x86/x64 in our repo (mirrored from Xamarin's), for other platforms you may have to compile it yourself: http://www.lovesmesomecode.com/20130719-compiling-mono-3-in-ubuntu/

**Add Sonarr's repository to your software source**
       

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC
    echo "deb http://apt.sonarr.tv/ master main" | sudo tee /etc/apt/sources.list.d/sonarr.list

*If you have issues with the repo being https you can install the `apt-transport-https` package or switch to http*

**Install/Update Sonarr**
	
	sudo apt-get update
	sudo apt-get install nzbdrone 

**Start Sonarr**

	mono /opt/NzbDrone/NzbDrone.exe

**Open Browser**

	http://localhost:8989

**Automatically Start Sonarr**

[[Autostart on Linux]]

### CentOS / Fedora / RHEL ###
[[CentOS 6 Installation Instructions|CentOS 6]]<br />
[[Fedora Installation|Fedora 20]]
### Raspberry Pi ###
[Install Nzbdrone Raspberry Pi on Raspbian](http://www.htpcguides.com/install-sonarr-raspberry-pi-mono-310/)
### FreeNAS / FreeBSD ###
[[FreeNAS Installation Instructions|FreeNAS Installation]]
### Other ###
**Install dependencies**

    mono (3.6+ but 3.10+ is recommended)
    mediainfo (for processing files on import)
    sqlite3 (database)

**Download**

http://update.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz

**Extract tar.gz**

    tar xvfz NzbDrone.master.tar.gz

**Run Nzbdrone with mono (debugging enabled)**

    mono --debug NzbDrone.exe

# Docker

There is a Docker image available that lets you update within the container as well as install from the develop branch.  [tuxeh/sonarr](https://registry.hub.docker.com/u/tuxeh/sonarr/)

For more info about Docker check out the [official website](https://www.docker.com).

# Synology #

**(1)** Add the SynoCommunity repo to your Synology device:

* Log into your NAS as administrator and go to `Main Menu` -> `Package Center` -> `Settings` -> `Package Sources`
* Click `Add`, type `SynoCommunity` as Name and `http://packages.synocommunity.com/` as Location and then press `OK` to validate.
* Also, click `Beta` and then checkmark the option labeled: `Yes, I want beta versions!` and press `OK`

**(2)** Click on the `Community` tab in Package Center and you will find Sonarr listed there.

**NOTE:** You must install Mono first (also found in the Synocommunity repo.)