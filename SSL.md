## Windows ##

### Prerequisites ###
- SSL Cert with Private Key [Create self-signed Certificate](http://www.selfsignedcertificate.com/) then [Convert PEM to PKCS#12](https://www.sslshopper.com/ssl-converter.html)
- Certificate loaded in Personal store of Local System (http://www.databasemart.com/howto/SQLoverssl/How_To_Import_Personal_Certificate_With_MMC.aspx)
- Hash/thumbprint of the certificate (http://msdn.microsoft.com/en-us/library/ms734695.aspx)

### Enabling SSL ###
You will need to edit Sonarr's config file directly as these settings are not exposed in the UI

1. Go to Settings -> General
2. Show advanced options
3. Enable SSL, set the SSL port and certificate hash (Sonarr will remove all spaces from the hash as they are not required).
4. Restart NzbDrone.exe or NzbDrone.Console.exe as administrator so the SSL URL and certificate can be registered with Windows.
5. Verify SSL connectivity
6. Restart Sonarr in your preferred method (service, exe, console)

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