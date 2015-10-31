The easiest way (when using Sonarr.app) is using `Login Items`, available in System Preferences, alternatively you can use the steps below.

Create a plist with these contents, changing the path to NzbDrone.exe as required:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>KeepAlive</key>
    <dict>
      <key>SuccessfulExit</key>
      <false />
    </dict>
    <key>Label</key>
    <string>nzbdrone.job</string>
    <key>ProgramArguments</key>
    <array>
      <string>mono</string>
      <string>--debug</string>
      <string>/Applications/Sonarr.app/Contents/MacOS/NzbDrone.exe</string>
    </array>
    <key>RunAtLoad</key>
    <true />
    <key>AbandonProcessGroup</key>
    <true />
  </dict>
</plist>
```

Save the plist to `~/Library/LaunchAgents/nzbdrone.plist`

Execute these commands in the terminal

```
cd ~/Library/LaunchAgents
launchctl load nzbdrone.plist
launchctl start nzbdrone.job
```