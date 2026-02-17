# Percona XtraBackup Overview

{% hint style="danger" %}
Percona XtraBackup is **not supported** in MariaDB. mariadb-backup is the recommended backup method to use instead of Percona XtraBackup. See [Percona XtraBackup Overview: Compatibility with MariaDB](percona-xtrabackup-overview.md#compatibility-with-mariadb) for more information.
{% endhint %}

Percona XtraBackup is an open source tool for performing hot backups of MariaDB, MySQL and Percona Server databases. Percona XtraBackup can perform compressed, incremental and streaming backups. It was designed to back up [XtraDB/InnoDB](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-xtradb-tables/) tables but can also back up other [storage engines](../../../server-usage/storage-engines/storage-engines-storage-engines-overview.md).

[mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) is a fork of Percona XtraBackup designed to work with encrypted and compressed tables and other MariaDB enhancements. There are many bug fixes, such as [MDEV-13807](https://jira.mariadb.org/browse/MDEV-13807), and some unsafe or redundant options have been removed. [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) is the recommended backup method for MariaDB servers.

## Installing Percona XtraBackup

### Installing with a Package Manager

Percona XtraBackup can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from a repository that has it.

You can also configure your package manager to install it from Percona's repository by following the instructions in their documentation:

* [Installing Percona XtraBackup 2.3](https://www.percona.com/doc/percona-xtrabackup/2.3/installation.html)
* [Installing Percona XtraBackup 2.4](https://www.percona.com/doc/percona-xtrabackup/2.4/installation.html)

#### Installing with yum/dnf

On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's\
repository using [yum](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum.md) or [dnf](https://en.wikipedia.org/wiki/DNF_\(software\)). Starting with RHEL 8 and Fedora 22, `yum` has been replaced by `dnf`, which is the next major version of `yum`. However, `yum` commands still work on many systems that use `dnf`. For example, to install Percona XtraBackup 2.3:

```
sudo yum install percona-xtrabackup
```

And to install Percona XtraBackup 2.4:

```
sudo yum install percona-xtrabackup-24
```

#### Installing with apt-get

On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant [DEB package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md) from MariaDB's\
repository using [apt-get](https://wiki.debian.org/apt-get). For example, to install Percona XtraBackup 2.3:

```
sudo apt-get install percona-xtrabackup
```

And to install Percona XtraBackup 2.4:

```
sudo apt-get install percona-xtrabackup-24
```

#### Installing with zypper

On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's repository using [zypper](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md). For example, to install Percona XtraBackup 2.3:

```
sudo zypper install percona-xtrabackup
```

And to install Percona XtraBackup 2.4:

```
sudo zypper install percona-xtrabackup-24
```

## Using Percona XtraBackup

The command to use `xtrabackup` and the general syntax is:

```
xtrabackup <options>
```

or:

```
innobackupex <options>
```

### Options

Options supported by Percona XtraBackup can be found on Percona's documentation.

`xtrabackup` options:

* [xtrabackup options - Percona XtraBackup 2.3](https://www.percona.com/doc/percona-xtrabackup/2.3/xtrabackup_bin/xbk_option_reference.html)
* [xtrabackup options - Percona XtraBackup 2.4](https://www.percona.com/doc/percona-xtrabackup/2.4/xtrabackup_bin/xbk_option_reference.html)

`innobackupex` options:

* [innobackupex options - Percona XtraBackup 2.3](https://www.percona.com/doc/percona-xtrabackup/2.3/innobackupex/innobackupex_option_reference.html)
* [innobackupex options - Percona XtraBackup 2.4](https://www.percona.com/doc/percona-xtrabackup/2.4/innobackupex/innobackupex_option_reference.html)

### Option Files

In addition to reading options from the command line, Percona XtraBackup can also read options from [option files](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

The following options relate to how MariaDB/MySQL command line tools handles option files. They must be given as the first argument on the command line:

| Option                  | Description                                      |
| ----------------------- | ------------------------------------------------ |
| --print-defaults        | Print the program argument list and exit.        |
| --no-defaults           | Don't read default options from any option file. |
| --defaults-file=#       | Only read default options from the given file #. |
| --defaults-extra-file=# | Read this file after the global files are read.  |

#### Server Option Groups

Percona XtraBackup reads server options from the following [option groups](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group         | Description                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| \[xtrabackup] | Options read by [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) and Percona XtraBackup. |
| \[mysqld]     | Options read by mysqld, which includes both MariaDB Server and MySQL Server.                                                                 |

#### Client Option Groups

Percona XtraBackup reads client options from the following [option groups](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group         | Description                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \[xtrabackup] | Options read by [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) and Percona XtraBackup.           |
| \[client]     | Options read by all MariaDB and MySQL [client programs](../../mariadb-client/), which includes both MariaDB and MySQL clients. For example, mysqldump. |

### Authentication and Privileges

Percona XtraBackup needs to authenticate with the database server when it performs a backup operation (i.e. when the `--backup` option is specified). The user account that performs the backup needs to have the `RELOAD` , `PROCESS`, `LOCK TABLES` and `REPLICATION CLIENT` [global privileges](../../../reference/sql-statements/account-management-sql-statements/grant.md#global-privileges) on the database server. For example:

```
CREATE USER 'xtrabackup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'xtrabackup'@'localhost';
```

The user account information can be specified with the `-user` and `--password` command line options. For example:

```
$ xtrabackup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=xtrabackup --password=mypassword
```

The user account information can also be specified in a supported [client option group](percona-xtrabackup-overview.md#client-option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[xtrabackup]
user=xtrabackup
password=mypassword
```

Percona XtraBackup does not need to authenticate with the database server when preparing or restoring a backup.

### File System Permissions

Percona XtraBackup has to read MariaDB's files from the file system. Therefore, when you run Percona XtraBackup as a specific operating system user, you should ensure that user account has sufficient permissions to read those files.

If you are using Linux and if you installed MariaDB with a package manager, then MariaDB's files will probably be owned by the `mysql` user and the `mysql` group.

## Compatibility with MariaDB

### Compatibility with [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) and Later

{% hint style="success" %}
In [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) and later, [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) is the recommended backup method to use instead of Percona XtraBackup.
{% endhint %}

In [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) and later, Percona XtraBackup is not supported.

This limitation is being tracked by Percona XtraBackup bug [PXB-1550](https://jira.percona.com/browse/PXB-1550). However, it does not appear that there are plans to fix it.

### Compatibility with [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

{% hint style="success" %}
In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) is the recommended backup method to use instead of Percona XtraBackup.
{% endhint %}

In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), Percona XtraBackup 2.4 is supported in some cases if [InnoDB page compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md) is not used, and if [data at rest encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md) is not used, and if [innodb\_page\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_page_size) is set to `16k`.

However, users should be aware that problems are likely due to the MySQL 5.7 undo log format incompatibility bug that was fixed in [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.2) in [MDEV-12289](https://jira.mariadb.org/browse/MDEV-12289). Due to this bug, backups prepared with Percona XtraBackup 2.4 may fail to recover some transactions. Only if you ran the server with the setting [innodb\_undo\_logs](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs)=1 this would not be a problem. Percona XtraBackup 2.4 may also fail to work entirely with [MariaDB 10.2.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.19) and later if [innodb\_safe\_truncate=ON](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_safe_truncate) is set due to changes in the redo log format introduced by [MDEV-14717](https://jira.mariadb.org/browse/MDEV-14717). In that case, you may see the following error:

```
InnoDB: Unsupported redo log format. The redo log was created with MariaDB 10.2.19. Please follow the instructions at http://dev.mysql.com/doc/refman/5.7/en/upgrading-downgrading.html
```

### Compatibility with [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1)

{% hint style="success" %}
In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) is the recommended backup method to use instead of Percona XtraBackup.
{% endhint %}

In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), Percona XtraBackup 2.3 is supported if [InnoDB page compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md) is not used, and if [data at rest encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md) is not used, and if [innodb\_page\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_page_size) is set to `16k`.

### Compatibility with [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0) and Before

In [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0) and before, Percona XtraBackup 2.3 is supported.

## Using Percona XtraBackup for Galera SSTs

The `xtrabackup-v2` SST method uses the [Percona XtraBackup](./) utility for performing SSTs. See [xtrabackup-v2 SST method](https://mariadb.com/kb/en/) for more information.

## See Also

* [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md)
* [mysqldump](../mysqldump.md)
* [Percona XtraBackup documentation](https://www.percona.com/doc/percona-xtrabackup/)
* [Percona JIRA](https://jira.percona.com/secure/Dashboard.jspa)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
