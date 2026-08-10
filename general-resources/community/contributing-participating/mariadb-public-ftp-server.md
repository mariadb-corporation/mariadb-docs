# MariaDB Public FTP Server

MariaDB provides a secure [FTP](http://en.wikipedia.org/wiki/File_Transfer_Protocol), [SFTP](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) and [WebDAV](https://en.wikipedia.org/wiki/WebDAV) server where you can upload files to be used by MariaDB developers, for example table structures and data for bug reports.

The folder tree consists of:

* The **public** folder for files that the MariaDB developers want to give the public access to (patches, samples etc).
* The **private** folder for uploads. Files uploaded there can only be accessed by MariaDB developers. You will not be able to see your upload and this folder does not allow downloads. This is done to protect any sensitive information which may be in test results, mysqld & core files. Upload those into this folder.
* The **secret** folder is for private downloads. Files in this folder are not visible so you will need the complete filename to successfully download a file from this folder.

To share files with MariaDB developers, upload it into the **private** directory with either:

* SFTP client (**scp**), enter 'anonymous' as the password:

```bash
scp MDEV-XXXXX.tgz anonymous@ftp.mariadb.org:private/
(anonymous@ftp.mariadb.org) Password: 
MDEV-XXXXX.tgz                                                          100%  152KB 218.8KB/s   00:00    
scp: remote fsetstat: Permission denied
```

You can ignore the 'fsetstat: Permission denied' error.

* WebDAV client (**curl**):

```bash
curl -T MDEV-XXXXX.tgz -u anonymous:anonymous https://webdav.mariadb.org/private/MDEV-XXXXX.tgz
Created
```

* FTP client (**lftp**); enter 'anonymous' as the password:

```bash
lftp -u anonymous -e 'put  MDEV-XXXXX.tgz' ftp://ftp.mariadb.org/private/
Password: 
cd ok, cwd=/private                                            
put: Access failed: 550 Issue during transfer: network error: error transferring data: read tcp
[...] read: connection reset by peer (MDEV-XXXXX.tgz)
```

You can ignore the 'network error'.

**Note for MariaDB developers**: please request your access to the SFTP service if not already at ftp@mariadb.org (provide public SSH key and username). You will then be able to access the service with:

```bash
sftp user@ftp.mariadb.org
```

or with HTTPS at [https://ftp.mariadb.org](https://ftp.mariadb.org/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
