## 0.7.0.27
***
### New
* Web server will now be automatically configured if nzbdrone.exe is run as admin.
* Added the ability to auto-ignore episodes for files that are deleted, good for people that delete after watching. Option is not exposed in the UI and is disabled by default (obviously).

### Enhancements
* Episode search now verifies that an upgrade is possible before attempting a search
* History is now ignored when doing a manual episodes search.
* Added warning to NZBsRus to warn that it does not support backlog searching. (RSS Only)
* Parser now properly handles files without titles.
* Added restart warning to System config page.
* Replaced ServiceInstall.bat/ServiceUninstall.bat with exe for better support for none-admin users.

### Fixes
* Issue where automatic update would log an error when there were no updates available.