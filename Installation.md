# Windows
1. Download the latest version of NzbDrone from [http://www.sonarr.tv](http://www.sonarr.tv "http://www.sonarr.tv")
2. Extract the zip file into your target directory. Use a folder that NzbDrone process would have write access to (**DO NOT** use `C:\Program Files` or `C:\Program Files (x86)`)
3. Run `NzbDrone.exe` once as administrator to register the port and URL with Windows (Required for remote access)<sup>1</sup>
4. Manually start NzbDrone by running `Nzbdrone.exe` or `ServiceInstall.exe` to install NzbDrone as a Windows service.
5. Open [http://localhost:8989](http://localhost:8989) in your browser


<sup>1</sup> The port will be opened on the firewall (if enabled) for the private profile only, if you're connected to a domain or a public network the port will not be opened automatically, but can be done so manually.

# Linux #

### Debian/Ubuntu ###

**mono**

mono 3.10 is included for x86/x64 in our repo (mirrored from Xamarin's), for other platforms you may have to compile it yourself: http://www.lovesmesomecode.com/20130719-compiling-mono-3-in-ubuntu/

**Add NzbDrone's repository to your software source**
       

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC
    echo "deb https://apt.sonarr.tv/ master main" | sudo tee -a /etc/apt/sources.list

*If you have issues with the repo being https you can install the `apt-transport-https` package or switch to http*

**Install/Update NzbDrone**
	
	sudo apt-get update
	sudo apt-get install nzbdrone 

**Start NzbDrone**

	mono /opt/NzbDrone/NzbDrone.exe

**Open Browser**

	http://localhost:8989

**Automatically Start NzbDrone**

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

# OS X #
[Install Nzbdrone OSX Screenshot Guide](http://www.htpcguides.com/install-nzbdrone-osx/)

**Install dependencies**

***mono***
	
    mono - (x86 required)

Download and run the Mono MRE installation

    http://www.mono-project.com/download/

**Do not `brew install mono`.**

***other***

mediainfo (for processing files on import) - http://mediaarea.net/en/MediaInfo/Download/Mac_OS

**Download**

http://update.sonarr.tv/v2/master/osx/NzbDrone.master.osx.tar.gz

**Extract tar.gz**

You can do this via the command line

    tar xvfz NzbDrone.master.osx.tar.gz

or through Finder, whatever works for you

**Run Nzbdrone with mono (debugging enabled)**

1) Open Terminal
2) Run mono with debugging enabled

    mono --debug /full/path/to/extracted/NzbDrone/NzbDrone.exe  

# Synology #

**(1)** Add the SynoCommunity repo to your Synology device:

* Log into your NAS as administrator and go to `Main Menu` ? `Package Center` ? `Settings` ? `Package Sources`
* Click `Add`, type `SynoCommunity` as Name and `http://packages.synocommunity.com/` as Location and then press `OK` to validate.
* Also, click `Beta` and then checkmark the option labeled: `Yes, I want beta versions!` and press `OK`

**(2)** Click on the `Community` tab in Package Center and you will find Sonarr.
**NOTE:** You must install Mono first