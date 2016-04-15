## Windows

### Prerequisites

- SSL certificate with Private Key [Create self-signed Certificate](http://www.selfsignedcertificate.com/) or [generate your own](#generate-a-self-signed-certificate)
- [Convert PEM to PKCS#12](https://www.sslshopper.com/ssl-converter.html)
- Load the certificate in Personal store of the Local System (http://www.databasemart.com/howto/SQLoverssl/How_To_Import_Personal_Certificate_With_MMC.aspx)
- Copy the Hash/thumbprint of the certificate (http://msdn.microsoft.com/en-us/library/ms734695.aspx). Thumbprint will contain spaces. Copy thumbprint to clipboard as is. 


### Enabling SSL in Sonarr
1. Go to Settings -> General
2. Show advanced options
3. Enable SSL, set the SSL port and certificate hash (Sonarr will remove all spaces from the hash as they are not required).
4. Stop Sonarr, either through the UI or by stopping the service or killing the NzbDrone.exe or NzbDrone.Console.exe process. 
5. Ensure that server is started in **Run as Administrator ** mode which allows it register SSL URL and certificate with Windows.
6. Verify SSL connectivity
7. If Sonarr server is still not listening on SSL port, then follow the workaround mentioned in this [thread](http://stackoverflow.com/questions/14953132/iis-7-error-a-specified-logon-session-does-not-exist-it-may-already-have-been).


## Linux / OS X

### Limitations

At this time newer SSL technologies are not supported by mono and some browsers do not support the older technologies mono uses (for good reason), which means the steps below may not help you achieve SSL connectivity to Sonarr. A surefire way is to setup an nginx (or Apache) reverse proxy and use it for SSL offloading.

### Prerequisites

- SSL certificate with Private Key [Create self-signed Certificate](http://www.selfsignedcertificate.com/) or [generate your own](#generate-a-self-signed-certificate)
- `.pvk` certificate, this can be done by converting a `.key` and `.cert`
- *Windows PC/VM*. The conversion tool only works there. OpenSSL 1.0.0 and up should be able to do it, but it needs to be done without a pass phrase, currently (version 1.0.1l) this is not possible.

### Converting key/cert to pvk

  1. Download the [PVK Conversion Tool](http://www.drh-consultancy.demon.co.uk/pvk.html) (near the bottom) and extract it.

  3. Run pvk.exe via Command Prompt:

     `pvk.exe -in yourdomain.key -topvk -nocrypt -out yourdomain.pvk`

### Synology Only
_If you're not running Sonarr on a Synology, skip these steps_

1. Place the SSL certificate **and** converted key in `pvk` format in `/volume1/@appstore/nzbdrone/var/`
2. Load the certificate with `httpcfg` (comes with mono) as `nzbdrone`, the user that runs Sonarr: 

  `su nzbdrone -c "/volume1/@appstore/mono/bin/httpcfg -add -port <SSL_PORT> -pvk yourdomain.pvk -cert yourdomain.cert"`

  *Replace `<SSL_PORT>` with the SSL port you set in Sonarr.*
3. Skip the importing step below as the pvk and cert have already been imported

### Importing
1. Load the certificate with `httpcfg` (comes with mono) with the user that runs Sonarr: 

  `httpcfg -add -port <SSL_PORT> -pvk yourdomain.pvk -cert yourdomain.cert`

   *Replace `<SSL_PORT>` with the SSL port you set in Sonarr.*

### Enabling SSL in Sonarr
1. Go to Settings -> General
2. Show advanced options
3. Enable SSL, set the SSL port
4. Save
5. Verify


## Generate a Self-signed Certificate ##

`openssl genrsa -out yourdomain.key 2048`
`openssl req -new -x509 -key yourdomain.key -out yourdomain.cert -days 3650 -subj /CN=yourdomain`