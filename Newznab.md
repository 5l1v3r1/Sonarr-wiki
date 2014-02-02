## Errors ##

These are some of the common errors you may see when adding an indexer

### The underlying connection was closed: An unexpected error occurred on a send. ###

This is caused by the indexer using a SSL protocol not supported by .net 4.5, to resolve this you will need to install .net 4.5, which is available on Vista/Server 2008 and above (if you're on XP/Server 2003 its time to upgrade).

### Error getting response stream (Write: The authentication or decryption has failed.): SendFailure ###

This is caused by the indexer using a new certificate authority that is not trusted by mono 2.10. The solution is to upgrade to mono 3.x, on Ubuntu this can be done via this method: http://stackoverflow.com/a/13384233/882971 We recommend upgrading to mono 3.x to fix a number of bugs and add support for .net 4.5 features.