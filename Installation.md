# Windows
1. Download the latest version of NzbDrone from [http://www.nzbdrone.com](http://www.nzbdrone.com "http://www.nzbdrone.com")
2. Extract the zip file into your target directory. Use a folder that NzbDrone process would have write access to (Don't use `C:\Program Files` or `C:\Program Files (x86)`)
3. Manually start NzbDrone by running `Nzbdrone.exe` or `ServiceInstall.exe` to install NzbDrone as a Windows service.


# Linux

### Ubuntu/Debian
**Add NzbDrone's repository to your software source**
       
    sudo add-apt-repository 'deb http://update.nzbdrone.com/repos/apt/debian develop main'

**Install/Update NzbDrone**
	
	sudo apt-get update
	sudo apt-get install nzbdrone 

**Start NzbDrone**

	mono /opt/NzbDrone/NzbDrone.exe

# Windows
1. Download the latest version of NzbDrone from [http://www.nzbdrone.com](http://www.nzbdrone.com "http://www.nzbdrone.com")
2. Extract the zip file into your target directory. Use a folder that NzbDrone process would have write access to (Don't use `C:\Program Files` or `C:\Program Files (x86)`)
3. Manually start NzbDrone by running `Nzbdrone.exe` or `ServiceInstall.exe` to install NzbDrone as a Windows service.


# Linux

### Ubuntu/Debian
**Add NzbDrone's repository to your software source**
       
    sudo add-apt-repository 'deb http://update.nzbdrone.com/repos/apt/debian develop main'

**Install/Update NzbDrone**
	
	sudo apt-get update
	sudo apt-get install nzbdrone 

**Start NzbDrone**

	mono /opt/NzbDrone/NzbDrone.exe

**Automatically Start NzbDrone**

[https://github.com/NzbDrone/NzbDrone/wiki/Making-NZBDrone-autostart-on-Linux-(Ubuntu-Debian-Tested)#method-1-recommended-upstart-ubuntudebian-based-distros](https://github.com/NzbDrone/NzbDrone/wiki/Making-NZBDrone-autostart-on-Linux-(Ubuntu-Debian-Tested)#method-1-recommended-upstart-ubuntudebian-based-distros)