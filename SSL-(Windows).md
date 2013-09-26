## Prerequisites ##
- SSL Cert with Private Key [(Create self-signed Certificate)](http://www.selfsignedcertificate.com/) then [(Convert PEM to PKCS#12)](https://www.sslshopper.com/ssl-converter.html)
- Cert loaded in Personal store of Local System

## Enabling SSL ##
You will need to edit NzbDrone's config file directly as these settings are not exposed in the UI

1. Shutdown NzbDrone
2. Open `C:\ProgramData\NzbDrone\config.xml`
3. Add/Change the following settings
	- `<SslPort>` - Default 9898
	- `<EnableSsl>` - default false
	- `<SslCertHash>` - this is the thumbnail/hash of the SSL certificate with all spaces removed (ie: 
`123456f6790a35f4b017b55d09e28f7ebe001bd`)
4. Run NzbDrone.exe or NzbDrone.Console.exe as administrator (so the SSL URL and Certificate can be registered with Windows).
5. Verify SSL connectivity
6. Restart NzbDrone in your preferred method (service, exe, console)