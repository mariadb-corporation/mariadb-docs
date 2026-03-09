# Backup and Restore for MariaDB ColumnStore 1.1.0

## Backup and Restore for MariaDB ColumnStore 1.1.0

## Backup and Restore Package

The Backup and Restore is part of the MariaDB ColumnStore Tools package. It can be downloaded here: [tools-ax](https://mariadb.com/downloads/mariadb-ax/tools-ax)

## Installing MariaDB ColumnStore Tools Package

The package is available as `rpm`, `deb`, and `binary`. Follow the instructions to install the associated package:

### RPM

```bash
rpm -ivh mariadb-columnstore-tools-x.x.x-x.rpm
```

### DEB

```bash
dpkg -i mariadb-columnstore-tools-x.x.x-x.deb
```

### BINARY

```bash
tar zxvf  mariadb-columnstore-tools-x.x.x-x.tar.gz
```

## Backup Overview

The high level steps involved in performing a full backup of MariaDB ColumnStore are:

* Suspend write activity on the system.
* Backup the MariaDB Server data files.
* Backup the ColumnStore data files.
* Resume write activity on the system.

## ColumnStore Backup

In MariaDB ColumnStore 1.1.0, the `columnstoreBackup` tool is available to automate the backup/restore across MariaDB ColumnStore nodes.

{% hint style="info" %}
`columnstoreBackup` tool is only for ColumnStore data backups. Other engines may not be fully backed up and data could be lost when restoring.
{% endhint %}

#### Backup Setup

To run `columnstoreBackup` you'll need to setup a backup server with `passwordless ssh login` available for the user account that installed MariaDB ColumnStore. (Default: root). It will need passwordless ssh login to all MariaDB ColumnStore Modules.

Copy the executable [columnstoreBackup](https://mariadb.com/downloads/mariadb-ax/tools-ax) onto the backup server. Create a target directory on the backup server to store the files. This directory will need to have enough space to store all ColumnStore data files.\
Example:

```sql
Backup Executable: /home/user/columnstoreBackup
Backup Data Directory: /home/user/columnstoreBackupData/
```

There is an optional `columnstoreBackup.config` file that when placed in the same directory as the `columnstoreBackup` executable will allow you to configure an incremental backup option that uses the `rsync` link-dest option to enable incremental backups. These are stored in backup.1 thru backup.\[n-1] from newest to oldest. The `columnstoreBackup.config` file should only contain a single line:

```sql
NUMBER_BACKUPS=[n]
```

Where "n" is the number of incremental backups to store. (Default: 3)

#### Running columnstoreBackup

columnstoreBackup must be run as root user either logging in as root or via the sudo command.

```sql
Usage: [sudo] ./columnstoreBackup [options] activeParentOAM backupServerLocation

activeParentOAM           IP address of ColumnStore server
                             (Active parent OAM module on multi-node install)
backupServerLocation      Path to the directory for storing backup files.

OPTIONS:
-h,--help         Prints help and exits.
-v,--verbose      Print more verbose execution details.
-d,--dry-run      Dry run and executes rsync dry run with stats.
-z,--compress     Utilize the compression option for rsync.
-n [value]        Maximum number parallel rsync commands. (Default: 5)
--user=[user]     Change the user performing remote sessions. (Default: root)

--install-dir=[PATH]  Change the install directory of ColumnStore.
                          Default: /usr/local/mariadb/columnstore
```

Example:

```sql
Running from the directory /home/user/:

sudo ./columnstoreBackup -zv 192.168.1.2 home/user/columnstoreBackupData
```

This will execute a backup for the system with a parent OAM module located at 192.168.1.2 and store all backup files inside the directory located at `home/user/columnstoreBackupData`. Option v will print out a more verbose logging of commands executed and option z will let rsync utilize the compression option for file transfers.

#### Backup Logging

Logging is output to the console as well as to a columnstoreBackup.log that is located in the directory columnstoreBackup is executed. This will contain some extra details on some issues. Log rotation is left to the user for handling.

#### Backup Return Codes

```sql
0 - success
1 - command line parameter or config file issue detected
2 - missing rsync or xmllint
3 - detected issue with disk space
4 - detected bad configuration file settings
5 - rsync command failed with an error
255 - could not connect via passwordless ssh
```

#### Backup Operation Notes

columnstoreBackup will create the following directories inside the Backup Data Directory:

```sql
backup.[1-n] (n incremental backups)
cnf (my.cnf and my.cnf.d)
pm[moduleID]dbroot[DBRootID] (pm1dbroot1 contains PM data from dbroot 1 on pm 1)
um[moduleID] (NOTE: When UM/PM are combined on nodes UM1 is the mysql/db directory for PM1)
```

These directories are created if they do not exist and can be created prior to execution by the user.

The columnstoreBackup option -n \[value] limits the number parallel rsync commands executed at a given time. The default 5 means up to 5 DBRoots will kick off rysnc commands to various PMs and the backup system will wait until all are complete and verified successful. At this time it will kick off another 5 DBRoots. The progress indicator should reflect the percentage of total completion and not individual rysnc commands. This value can be set higher via the -n command but if the number of DBRoots present in the system is large enough there may be a performance hit on system processing or network bandwidth limitations.

## ColumnStore Restore

The `columnstoreRestore` tool is designed to be run on the system storing the backups. This automates restoring from backups created by the `columnstoreBackup` tool.

#### Restore Setup

To run `columnstoreRestore` you'll need to setup a backup server with `passwordless ssh login` available for the user account that installed MariaDB ColumnStore. (Default: root)

`columnstoreRestore` must be run as root or with `sudo`.

`columnstoreRestore` expects MariaDB Columnstore to be shut down in a fresh install state.

Take the following steps to prepare system for columnstoreRestore:

* On the active parent OAM module execute the command

```sql
mcsadmin shutdownsystem y
```

* Run on all PM modules:

```sql
rm -rf [INSTALL_DIR]/data*/000.dir
rm -rf [INSTALL_DIR]/data1/systemFiles/dbrm/*
```

* Run on all UM or combo PM front-end nodes

```sql
cd [INSTALL_DIR]/mysql/db 
delete all directories except:
calpontsys
infinidb_querystats
infinidb_infinidb_vtable
mysql
performance_schema
test
```

* On the active parent OAM module execute the command

```sql
[INSTALL_DIR]/bin/clearShm
```

* On the backup system run columnstoreRestore script

#### Running columnstoreRestore

columnstoreRestore must be run as root user either logging in as root or via the `sudo` command.

```sql
Usage: ./columnstoreRestore [options] backupServerLocation restoreServerPM1

restoreServerPM1          IP address of ColumnStore server
                             (Assumes PM1 = Active Parent OAM Module)
backupServerLocation      Path to the directory for storing backup files.

OPTIONS:
-h,--help         Print this message and exit.
-v,--verbose      Print more verbose execution details.
-d,--dry-run      Dry run and executes rsync dry run with stats.
-z,--compress     Utilize the compression option for rsync.
-n [value]        Maximum number parallel rsync commands. (Default: 5).
--user=[user]     Change the user performing remote sessions. (Default: root)

--install-dir=[PATH]  Change the install directory of ColumnStore.
                          Default: /usr/local/mariadb/columnstore
```

EXAMPLE:\
Running from the directory /home/user/ with the `columnstoreBackupData` directory created in the columnstoreBackup example above:

```sql
sudo ./columnstoreRestore -zv home/user/columnstoreBackupData 192.168.1.100
```

This will execute a restore for the MariaDB ColumnStore system with a parent OAM module located at 192.168.1.100 from the directory located at home/user/columnstoreBackupData. Option v will print out a more verbose logging of commands executed, and option z will let rsync utilize the compression option for file transfers.

#### Restore Logging

Logging is output to the console as well as to a columnstoreRestore.log that is located in the directory columnstoreRestore is executed. This will contain some extra details on some issues. Log rotation is left to the user for handling.

#### Restore Return Codes

```sql
0 - success
1 - command line parameter or config file issue detected
2 - missing rsync or xmllint
3 - detected issue with disk space
4 - detected bad configuration file settings
5 - rsync command failed with an error
255 - could not connect via passwordless ssh
```

#### Restore Operation Notes

columnstoreRestore will create a `restoreConfig` directory inside the `backupServerLocation` defined at the command line. This is just meant to store a copy of the restored systems version and configuration file for verification the restore is possible.

The columnstoreRestore option -n \[value] limits the number parallel `rsync` commands executed at a given time. The default 5 means up to 5 DBRoots will kick off `rysnc` commands to various PMs, and the backup system will wait until all are complete and verified successful. At this time, it will kick off another 5 DBRoots. The progress indicator should reflect the percentage of total completion and not individual `rysnc` commands. This value can be set higher via the -n command, but if the number of DBRoots present in the system is large enough there may be a performance hit on system processing or network bandwidth limitations.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
