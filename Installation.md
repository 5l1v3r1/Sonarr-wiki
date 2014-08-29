# Windows
1. Download the latest version of NzbDrone from [http://www.nzbdrone.com](http://www.nzbdrone.com "http://www.nzbdrone.com")
2. Extract the zip file into your target directory. Use a folder that NzbDrone process would have write access to (**DO NOT** use `C:\Program Files` or `C:\Program Files (x86)`)
3. Run `NzbDrone.exe` once as administrator to register the port and URL with Windows (Required for remote access)<sup>1</sup>
4. Manually start NzbDrone by running `Nzbdrone.exe` or `ServiceInstall.exe` to install NzbDrone as a Windows service.
5. Open [http://localhost:8989](http://localhost:8989) in your browser


<sup>1</sup> The port will be opened on the firewall (if enabled) for the private profile only, if you're connected to a domain or a public network the port will not be opened automatically, but can be done so manually.

# Linux #

### Ubuntu ###
**mono**

It is recommended that you install  mono 3.2 instead of the default that is in the Ubuntu repo, this Stack Overflow answer has the steps to do it: http://stackoverflow.com/a/13384233/882971

**Add NzbDrone's repository to your software source**
       

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC
    echo "deb http://update.nzbdrone.com/repos/apt/debian master main" | sudo tee -a /etc/apt/sources.list

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
[[CentOS 6 Installation Instructions|CentOS 6]]

### Other ###

**Install dependencies**

    mono (2.10.8+ but 3.2+ is recommended)
    mediainfo (for processing files on import)
    sqlite3 (database)

**Download**

http://update.nzbdrone.com/v2/master/mono/NzbDrone.master.tar.gz

**Extract tar.gz**

    tar xvfz NzbDrone.master.tar.gz

**Run Nzbdrone with mono (debugging enabled)**

    mono --debug NzbDrone.exe

# Docker

You can use [aostanin's Dockerfile](https://registry.hub.docker.com/u/aostanin/nzbdrone/) to quickly build your own isolated app container. It's based on the Linux instructions above.

For more info about Docker check out the [official website](https://www.docker.com).

# OS X #

**Install dependencies**

***mono***
	
    mono - (x86 required)

Download and run the Mono MRE installation

    http://www.mono-project.com/download/

***other***

mediainfo (for processing files on import) - http://mediaarea.net/en/MediaInfo/Download/Mac_OS

**Download**

http://update.nzbdrone.com/v2/master/osx/NzbDrone.master.osx.tar.gz

**Extract tar.gz**

You can do this via the command line

    tar xvfz NzbDrone.master.osx.tar.gz

or through Finder, whatever works for you

**Run Nzbdrone with mono (debugging enabled)**

1) Open Terminal
2) Run mono with debugging enabled

    mono --debug /full/path/to/extracted/NzbDrone/NzbDrone.exe