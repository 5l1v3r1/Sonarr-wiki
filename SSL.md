## Windows ##

### Prerequisites ###
- SSL Cert with Private Key [Create self-signed Certificate](http://www.selfsignedcertificate.com/) then [Convert PEM to PKCS#12](https://www.sslshopper.com/ssl-converter.html)
- Cert loaded in Personal store of Local System (http://www.databasemart.com/howto/SQLoverssl/How_To_Import_Personal_Certificate_With_MMC.aspx)
- Thumbprint of the certificate (http://msdn.microsoft.com/en-us/library/ms734695.aspx)

### Enabling SSL ###
You will need to edit NzbDrone's config file directly as these settings are not exposed in the UI

1. Go to Settings -> General
2. Show advanced options
3. Enable SSL, set the SSL port and Certificate Hash (make sure all spaces are removed from the Certificate hash, before and after.
4. Restart NzbDrone.exe or NzbDrone.Console.exe as administrator (so the SSL URL and Certificate can be registered with Windows).
5. Verify SSL connectivity
6. Restart NzbDrone in your preferred method (service, exe, console)

## Linux ##

### Prerequisites ###
- Windows PC (Conversion tool only works there currently, OpenSSL should be able to do it, but it needs to be done without a pass phrase)
- SSL Cert with Private Key [(Create self-signed Certificate)](http://www.selfsignedcertificate.com/) then 	- Convert .key to .pvk
 
 		1. Download Win32 binary - http://www.drh-consultancy.demon.co.uk/pvk.html
 		2. Extract Zip
 		3. Run pvk.exe with the following options: pvk -in yourdomain.key -topvk -nocrypt -out yourdomain.pvk
- Load cert with httpcfg (comes with mono): httpcfg -add -port 9898 -pvk yourdomain.pvk -cert yourdomain.crt

### Enabling SSL ###

1. Enable SSL on Settings -> General
2. Restart NzbDrone
3. Verify!