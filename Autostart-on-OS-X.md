Create a plist with these contents, changing the path to NzbDrone.exe as required:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
        <key>Label</key>
        <string>nzbdrone.job</string>
        <key>ProgramArguments</key>
        <array>
                <string>mono</string>
                <string>--debug</string>
                <string>/Applications/NzbDrone/NzbDrone.exe</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>AbandonProcessGroup</key>
        <true/>
        <key>Disabled</key>
        <true/>
</dict>
</plist>
```

Save the plist to `~/Library/LauncherAgents/nzbdrone.plist`

Execute these commands in the terminal

```
cd ~/Library/LaunchAgents
launchctl load nzbdrone.plist
launchctl start nzbdrone.job
```