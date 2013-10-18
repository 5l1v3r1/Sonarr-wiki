# Windows
1. Download the latest version of NzbDrone from [http://www.nzbdrone.com](http://www.nzbdrone.com "http://www.nzbdrone.com")
2. Extract the zip file into your target directory. Use a folder that NzbDrone process would have write access to (Don't use `C:\Program Files` or `C:\Program Files (x86)`)
3. Manually start NzbDrone by running `Nzbdrone.exe` or `ServiceInstall.exe` to install NzbDrone as a Windows service.


# Linux

### Ubuntu/Debian
**Add NzbDrone's repository to your software source**
       
    echo "deb http://update.nzbdrone.com/repos/apt/debian develop main" | sudo tee -a /etc/apt/sources.list

**Install/Update NzbDrone**
	
	sudo apt-get update
	sudo apt-get install nzbdrone 

**Start NzbDrone**

	mono /opt/NzbDrone/NzbDrone.exe

**Automatically Start NzbDrone**

[[Autostart on Linux]]