## Windows ##

### Prerequisites ###
- Get an SSL certificate with Private Key [Create self-signed Certificate](http://www.selfsignedcertificate.com/)
- [Convert PEM to PKCS#12](https://www.sslshopper.com/ssl-converter.html)
- Load the certificate in Personal store of the Local System (http://www.databasemart.com/howto/SQLoverssl/How_To_Import_Personal_Certificate_With_MMC.aspx)
- Copy the Hash/thumbprint of the certificate (http://msdn.microsoft.com/en-us/library/ms734695.aspx). Thumbprint will contain spaces. Copy thumbprint to clipboard as is. 

### Enabling SSL ###
1. Go to Settings -> General
2. Show advanced options
3. Enable SSL, set the SSL port and certificate hash (Sonarr will remove all spaces from the hash as they are not required).
4. Stop Sonarr servers or kill NzbDrone.exe or NzbDrone.Console.exe process. 
5. Ensure that server is started in **Run as Administrator ** mode which allows it regiser SSL URL and certificate with Windows.
6. Verify SSL connectivity
7. If Sonarr server is still not listening on SSL port, then follow the workaround mentioned in this [thread](http://stackoverflow.com/questions/14953132/iis-7-error-a-specified-logon-session-does-not-exist-it-may-already-have-been).

## Linux / OS X ##

### Prerequisites ###
- Windows PC. The conversion tool only works there. OpenSSL 1.0.0 and up should be able to do it, but it needs to be done without a pass phrase, currently (version 1.0.1l) this is not possible.
- SSL certificate and corresponding private key ([create self-signed certificate](http://www.selfsignedcertificate.com/)).

### Converting .key to .pvk ###

  1. Download the [PVK Conversion Tool](http://www.drh-consultancy.demon.co.uk/pvk.html) (near the bottom) and extract it.

  3. Run pvk.exe via Command Prompt:

     `pvk.exe -in yourdomain.key -topvk -nocrypt -out yourdomain.pvk`

  4. Load the certificate with `httpcfg` (comes with mono): 

     `httpcfg -add -port <SSL_PORT> -pvk yourdomain.pvk -cert yourdomain.crt`

     *Replace `<SSL_PORT>` with the SSL port you set in Sonarr.*

### Enabling SSL ###

1. Enable SSL on Settings -> General (enable advanced settings first).
2. Restart Sonarr.
3. Verify!