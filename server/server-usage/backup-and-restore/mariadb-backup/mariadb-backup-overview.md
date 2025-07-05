# mariadb-backup Overview

{% include "../../../.gitbook/includes/mariadb-backup-was-previous....md" %}

**mariadb-backup** is an open source tool provided by MariaDB for performing physical online backups of InnoDB, Aria and MyISAM tables. For InnoDB, “hot online” backups are possible. It was originally forked from Percona XtraBackup 2.3.8. It is available on Linux and Windows.

This tool provides a production-quality, nearly non-blocking method for performing full backups on running systems. While partial backups with mariadb-backup are technically possible, they require many steps and cannot be restored directly onto existing servers containing other data.

#### Supported Features

`mariadb-backup` supports all of the main features of Percona XtraBackup 2.3.8, plus:

* Backup/Restore of tables using Data-at-Rest Encryption.
* Backup/Restore of tables using InnoDB Page Compression.
* [mariadb-backup SST method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method) with Galera Cluster.
* Microsoft Windows support.
* Backup/Restore of tables using the MyRocks storage engine. See [Files Backed up by mariadb-backup: MyRocks Data Files](files-backed-up-by-mariadb-backup.md#myrocks-data-files) for more information.

**Supported Features in MariaDB Enterprise Backup**

{% tabs %}
{% tab title="Current" %}
MariaDB Backup supports some additional features, such as:

* Minimizes locks during the backup to permit more concurrency and to enable faster backups.
  * This relies on the usage of `BACKUP STAGE` commands and DDL logging.
  * This includes no locking during the copy phase of `ALTER TABLE` statements, which tends to be the longest phase of these statements.
* Provides optimal backup support for all storage engines that store things on local disk.
{% endtab %}

{% tab title="< 10.11.8" %}
MariaDB Backup does **not** support some additional features.
{% endtab %}
{% endtabs %}

#### Differences Compared to Percona XtraBackup

* Percona XtraBackup requires more locks to run than MariaDB. In addition, any running ALTER TABLE will block Percona XtraBackup until it completes.
* Percona XtraBackup copies its InnoDB redo log files to the file `xtrabackup_logfile`, while mariadb-backup uses the file ib\_logfile0.
* Percona XtraBackup's [libgcrypt-based encryption of backups](https://www.percona.com/doc/percona-xtrabackup/2.3/backup_scenarios/encrypted_backup.html) is not supported by mariadb-backup.
* There is no symbolic link from `mariadb-backup` to [innobackupex](https://www.percona.com/doc/percona-xtrabackup/2.3/innobackupex/innobackupex_option_reference.html), as there is for [xtrabackup](https://www.percona.com/doc/percona-xtrabackup/2.3/xtrabackup_bin/xbk_option_reference.html). Instead, `mariadb-backup` has the --innobackupex command-line option to enable innobackupex-compatible options.
* The [--compact](https://www.percona.com/doc/percona-xtrabackup/2.3/xtrabackup_bin/xbk_option_reference.html#cmdoption-xtrabackup-compact) and [--rebuild\_indexes](https://www.percona.com/doc/percona-xtrabackup/2.3/xtrabackup_bin/xbk_option_reference.html#cmdoption-xtrabackup-rebuild-indexes) options are not supported.
* Support for [--stream=tar](https://www.percona.com/doc/percona-xtrabackup/2.3/howtos/recipes_ibkx_stream.html) was removed from `mariadb-backup` in [MariaDB 10.1.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10124-release-notes).
* The [xbstream](https://www.percona.com/doc/percona-xtrabackup/2.3/xbstream/xbstream.html) utility has been renamed to `mbstream`. However, to select this output format when creating a backup, `mariadb-backup`'s [--stream](mariadb-backup-options.md#stream) option still expects the `xbstream` value.
* `mariadb-backup` does not support [lockless binlog](https://www.percona.com/doc/percona-xtrabackup/2.3/advanced/lockless_bin-log.html).

**Difference in Versioning Schemes**

Each Percona XtraBackup release has two version numbers--the Percona XtraBackup version number and the version number of the MySQL Server release that it is based on. For example:

```bash
xtrabackup version 2.2.8 based on MySQL server 5.6.22
```

Each mariadb-backup release only has one version number, and it is the same as the version number of the MariaDB Server release that it is based on. For example:

```bash
mariadb-backup based on MariaDB server 10.2.15-MariaDB Linux (x86_64)
```

See [Compatibility of mariadb-backup Releases with MariaDB Server Releases](mariadb-backup-overview.md#compatibility-of-mariadb-backup-releases-with-mariadb-server-releases) for more information on mariadb-backup versions.

## Installing `mariadb-backup`

### Installing on Linux

The `mariadb-backup` executable is included in binary tarballs on Linux.

### **Installing with a Package Manager**

mariadb-backup can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from one of the MariaDB repositories.

You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the MariaDB Package Repository setup script.

You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md).

**Installing with yum/dnf**

On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant RPM package from MariaDB's repository using yum or [dnf](https://en.wikipedia.org/wiki/DNF_\(software\)). Starting with RHEL 8 and Fedora 22, `yum` has been replaced by `dnf`, which is the next major version of `yum`. However, `yum` commands still work on many systems that use `dnf`. For example:

```bash
sudo yum install MariaDB-backup
```

**Installing with apt-get**

On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant DEB package from MariaDB's\
repository using [apt-get](https://wiki.debian.org/apt-get). For example:

```bash
sudo apt-get install mariadb-backup
```

**Installing with zypper**

On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant RPM package from MariaDB's repository using zypper. For example:

```bash
sudo zypper install MariaDB-backup
```

### Installing on Windows

The `mariadb-backup` executable is included in MSI and ZIP packages on Windows.

When using the [Windows MSI installer](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows.md), `mariadb-backup` can be installed by selecting _Backup utilities_:

<figure><img src="../../../.gitbook/assets/mariadb_backup_windows.png" alt=""><figcaption><p>MariaDB MSI Installer showing the Backup utilites install option</p></figcaption></figure>

## Using mariadb-backup

The command to use `mariadb-backup` and the general syntax is:

```bash
mariadb-backup <options>
```

For in-depth explanations on how to use `mariadb-backup`, see:

* [Full Backup and Restore with mariadb-backup](full-backup-and-restore-with-mariadb-backup.md)
* [Incremental Backup and Restore with mariadb-backup](incremental-backup-and-restore-with-mariadb-backup.md)
* [Partial Backup and Restore with mariadb-backup](partial-backup-and-restore-with-mariadb-backup.md)
* [Restoring Individual Tables and Partitions with mariadb-backup](restoring-individual-tables-and-partitions-with-mariadb-backup.md)
* [Setting up a Replica with mariadb-backup](setting-up-a-replica-with-mariadb-backup.md)
* [Using Encryption and Compression Tools With mariadb-backup](using-encryption-and-compression-tools-with-mariadb-backup.md)

### Options

Options supported by mariadb-backup can be found on the [mariadb-backup Options](mariadb-backup-options.md) page.

{% hint style="warning" %}
`mariadb-backup` will currently silently ignore unknown command-line options, so be extra careful about accidentally including typos in options or accidentally using options from later `mariadb-backup` versions. The reason for this is that `mariadb-backup` currently treats command-line options and options from [option files](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) equivalently. When it reads from these [option files](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), it has to read a lot of options from the server option groups read by [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md). However, `mariadb-backup` does not know about many of the options that it normally reads in these option groups. If `mariadb-backup` raised an error or warning when it encountered an unknown option, then this process would generate a large amount of log messages under normal use. Therefore, `mariadb-backup` is designed to silently ignore the unknown options instead. See [MDEV-18215](https://jira.mariadb.org/browse/MDEV-18215) about that.
{% endhint %}

#### Option Files

In addition to reading options from the command-line, mariadb-backup can also read options from option files.

The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:

| Option                      | Description                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------- |
| `--print-defaults`          | Print the program argument list and exit.                                           |
| `--no-defaults`             | Don't read default options from any option file.                                    |
| `--defaults-file=#`         | Only read default options from the given option file.                               |
| `--defaults-extra-file=#`   | Read this file after the global files are read.                                     |
| `--defaults-group-suffix=#` | In addition to the default option groups, also read option groups with this suffix. |

#### **Server Option Groups**

mariadb-backup reads server options from the following [option groups](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `[mariadb-backup]` | Options read by `mariadb-backup`. Available starting with [MariaDB 10.1.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes) and [MariaDB 10.2.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10213-release-notes).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `[mariadb-backup]` | Options read by `mariadb-backup`. Available starting with [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes) and [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1054-release-notes).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `[xtrabackup]`     | Options read by `mariadb-backup` and Percona XtraBackup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `[server]`         | Options read by MariaDB Server. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                                                                                                                                                                   |
| `[mysqld]`         | Options read by `mariadbd`, which includes both MariaDB Server and MySQL Server (where it is called `mysqld`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `[mysqld-X.Y]`     | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example: `[mysqld-10.4]`. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                                                                  |
| `[mariadb]`        | Options read by MariaDB Server. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                                                                                                                                                                   |
| `[mariadb-X.Y]`    | Options read by a specific version of MariaDB Server. For example: `[mariadb-10.4]`. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                                                                                                              |
| `[mariadbd]`       | Options read by MariaDB Server. Available starting with [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes) and [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1054-release-notes).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `[mariadbd-X.Y]`   | Options read by a specific version of MariaDB Server. For example: `[mariadbd-10.4]`. Available starting with [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes) and [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1054-release-notes).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `[client-server]`  | Options read by all MariaDB client programs and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                          |
| `[galera]`         | Options read by MariaDB Server, but only if it is compiled with Galera Cluster support. In MariaDB 10.1 and later, all builds on Linux are compiled with Galera Cluster support. When using one of these builds, options from this option group are read even if the Galera Cluster functionality is not enabled. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes) on systems compiled with Galera Cluster support. |

#### **Client Option Groups**

mariadb-backup reads client options from the following option groups from option files:

| Group              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[mariadb-backup]` | Options read by mariadb-backup. Available starting with [MariaDB 10.1.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes) and [MariaDB 10.2.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10213-release-notes).                                                                                                                                                                                                                                                                                                                                |
| `[mariadb-backup]` | Options read by mariadb-backup. Available starting with [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes) and [MariaDB 10.5.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1054-release-notes)                                                                                                                                                                                                                                                                                                                                                              |
| `[xtrabackup]`     | Options read by mariadb-backup and Percona XtraBackup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `[client]`         | Options read by all MariaDB and MySQL client programs, which includes both MariaDB and MySQL clients. For example, mysqldump.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `[client-server]`  | Options read by all MariaDB client programs and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes). |
| `[client-mariadb]` | Options read by all MariaDB client programs. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                             |

### Authentication and Privileges

`mariadb-backup` needs to authenticate with the database server when it performs a backup operation (i.e. when the [--backup ](mariadb-backup-options.md#backup)option is specified). For most use cases, the user account that performs the backup needs to have the following global privileges on the database server.

{% tabs %}
{% tab title="MariaDB 10.5 and Later" %}
In 10.5 and later the required privileges are:

```sql
CREATE USER 'mariadb-backup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR ON *.* TO 'mariadb-backup'@'localhost';
```
{% endtab %}

{% tab title="MairaDB 10.4 and Earlier" %}
Prior to 10.5, the required privileges are:

```sql
CREATE USER 'mariadb-backup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'mariadb-backup'@'localhost';
```
{% endtab %}
{% endtabs %}

If your database server is also using the [MyRocks storage engine](../../storage-engines/myrocks/), then the user account that performs the backup will also need the `SUPER` [global privilege](../../../reference/sql-statements/account-management-sql-statements/grant.md#global-privileges). This is because `mariadb-backup` creates a checkpoint of this data by setting the [rocksdb\_create\_checkpoint](../../storage-engines/myrocks/myrocks-system-variables.md#rocksdb_create_checkpoint) system variable, which requires this privilege. See [MDEV-20577](https://jira.mariadb.org/browse/MDEV-20577) for more information.

`CONNECTION ADMIN` is also required where [--kill-long-queries-timeout](mariadb-backup-options.md#kill-long-queries-timeout) is greater than `0`, and [--no-lock](mariadb-backup-options.md#no-lock) isn't applied in order to [KILL](../../../reference/sql-statements/administrative-sql-statements/kill.md) queries. Prior to 10.5 a `SUPER` privilege is required instead of `CONNECTION ADMIN`.

`REPLICA MONITOR` (or alias `SLAVE MONITOR`) is also required where [--galera-info](mariadb-backup-options.md#galera-info) or [--slave-info](mariadb-backup-options.md#slave-info) is specified.

To use the [--history](mariadb-backup-options.md#history) option, the backup user also needs to have the following privileges granted:

```sql
GRANT CREATE, INSERT ON mysql.mariadb_backup_history TO 'mariadb-backup'@'localhost';
```

Prior to MariaDB 10.11, the necessary permissions to use [--history](mariadb-backup-options.md#history) were:

```sql
GRANT CREATE, INSERT ON PERCONA_SCHEMA.* TO 'mariadb-backup'@'localhost';
```

If you're upgrading from an older version and you want to use the new default table without losing your backup history, you can move and rename the current table in this way:

```sql
RENAME TABLE PERCONA_SCHEMA.xtrabackup_history TO mysql.mariadb_backup_history;
```

The user account information can be specified with the [--user](mariadb-backup-options.md#user) and [--password](mariadb-backup-options.md#p-password) command-line options. For example:

```bash
mariadb-backup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

The user account information can also be specified in a supported [client option group](mariadb-backup-overview.md#client-option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```bash
[mariadb-backup]
user=mariadb-backup
password=mypassword
```

`mariadb-backup` does not need to authenticate with the database server when preparing or restoring a backup.

#### File System Permissions

`mariadb-backup` has to read MariaDB's files from the file system. Therefore, when you run `mariadb-backup` as a specific operating system user, you should ensure that user account has sufficient permissions to read those files.

If you are using Linux and if you installed MariaDB with a package manager, then MariaDB's files will probably be owned by the `mysql` user and the `mysql` group.

#### Using `mariadb-backup` with Data-at-Rest Encryption

`mariadb-backup` supports [Data-at-Rest Encryption](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/).

mariadb-backup will query the server to determine which [key management and encryption plugin](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) is being used, and then it will load that plugin itself, which means that `mariadb-backup` needs to be able to load the key management and encryption plugin's shared library.

mariadb-backup will also query the server to determine which [encryption keys](../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys) it needs to use.

In other words, `mariadb-backup` is able to figure out a lot of encryption-related information on its own, so normally one doesn't need to provide any extra options to backup or restore encrypted tables.

`mariadb-backup` backs up encrypted and unencrypted tables as they are on the original server. If a table is encrypted, then the table will remain encrypted in the backup. Similarly, if a table is unencrypted, then the table will remain unencrypted in the backup.

The primary reason that mariadb-backup needs to be able to encrypt and decrypt data is that it needs to apply [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) records to make the data consistent when the backup is prepared. As a consequence, mariadb-backup does not perform many encryption or decryption operations when the backup is initially taken. MariaDB performs more encryption and decryption operations when the backup is prepared. This means that some encryption-related problems (such as using the wrong encryption keys) may not become apparent until the backup is prepared.

#### Using `mariadb-backup` for Galera SSTs

The `mariadb-backup` SST method uses the `mariadb-backup` utility for performing SSTs. See [mariadb-backup SST method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method) for more information.

### Files Backed up by `mariadb-backup`

`mariadb-backup` backs up many different files in order to perform its backup operation. See [Files Backed up by mariadb-backup](files-backed-up-by-mariadb-backup.md) for a list of these files.

### Files Created by `mariadb-backup`

`mariadb-backup` creates several different types of files during the backup and prepare phases. See [Files Created by mariadb-backup](mariadb-backup-overview.md#files-created-by-mariadb-backup) for a list of these files.

### Binary logs

`mariadb-backup` can store the binary log position in the backup. See [--binlog-info](mariadb-backup-options.md#binlog-info). This can be used for point-in-time recovery and to use the backup to setup a slave with the correct binlog position.

## Known Issues

### Unsupported Server Option Groups

Prior to [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes), `mariadb-backup` doesn't read server options from all option groups supported by the server. In those versions, it only looks for server options in the following server option groups:

| Group              | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[xtrabackup]`     | Options read by Percona XtraBackup and `mariadb-backup`.                                                                                                                                                                                                                                                                                                                                                          |
| `[mariadb-backup]` | Options read by Percona XtraBackup and `mariadb-backup`. Available starting with [MariaDB 10.1.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes) and [MariaDB 10.2.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10213-release-notes). |
| `[mysqld]`         | Options read by [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd.md), which includes both MariaDB Server and MySQL Server (where it is called `mysqld`).                                                                                                                                                                                                                              |

Those versions do not read server options from the following option groups supported by the server:

| Group             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `[server]`        | Options read by MariaDB Server. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                                                                                                                                                                   |
| `[mysqld-X.Y]`    | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example: `[mysqld-5.5]`. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                                                                   |
| `[mariadb]`       | Options read by MariaDB Server. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                                                                                                                                                                   |
| `[mariadb-X.Y]`   | Options read by a specific version of MariaDB Server. For example: `[mariadb-10.3]`. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                                                                                                              |
| `[client-server]` | Options read by all MariaDB client programs and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes).                                                                                                                                                                                          |
| `[galera]`        | Options read by MariaDB Server, but only if it is compiled with Galera Cluster support. In MariaDB 10.1 and later, all builds on Linux are compiled with Galera Cluster support. When using one of these builds, options from this option group are read even if the Galera Cluster functionality is not enabled. Available starting with [MariaDB 10.1.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10138-release-notes), [MariaDB 10.2.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10222-release-notes), and [MariaDB 10.3.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10313-release-notes) on systems compiled with Galera Cluster support. |

See [MDEV-18347](https://jira.mariadb.org/browse/MDEV-18347) for more information.

### No Default Datadir

Prior to [MariaDB 10.1.36](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10136-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes), and [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), if you were performing a [--copy-back](mariadb-backup-options.md#copy-back) operation, and if you did not explicitly specify a value for the [--datadir](mariadb-backup-options.md#h-datadir) option either on the command line or one of the supported server option groups in an option file, then `mariadb-backup` would not default to the server's default `datadir`. Instead, `mariadb-backup` would fail with an error. For example:

```bash
Error: datadir must be specified.
```

The solution is to explicitly specify a value for the [--datadir](mariadb-backup-options.md#h-datadir) option either on the command line or in one of the supported server option groups in an option file. For example:

```bash
[mysqld]
datadir=/var/lib/mysql
```

In [MariaDB 10.1.36](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10136-release-notes), [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes), and [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes) and later, mariadb-backup will default to the server's default `datadir` value.

See [MDEV-12956](https://jira.mariadb.org/browse/MDEV-12956) for more information.

### Concurrent DDL and Backup Issues

Prior to [MariaDB 10.2.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10219-release-notes) and [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), if concurrent DDL was executed while the backup was taken, then that could cause various kinds of problems to occur.

One example is that if DDL caused any tablespace IDs to change (such as [TRUNCATE TABLE](../../../reference/sql-statements/table-statements/truncate-table.md) or [RENAME TABLE](../../../reference/sql-statements/data-definition/rename-table.md)), then that could cause the effected tables to be inconsistent in the backup. In this scenario, you might see errors about mismatched tablespace IDs when the backup is prepared.

For example, the errors might look like this:

```
2018-12-07 07:49:32 7f51b3184820  InnoDB: Error: table 'DB1/TAB_TEMP'
InnoDB: in InnoDB data dictionary has tablespace id 1355633,
InnoDB: but a tablespace with that id does not exist. There is
InnoDB: a tablespace of name DB1/TAB_TEMP and id 1354713, though. Have
InnoDB: you deleted or moved .ibd files?
InnoDB: Please refer to
InnoDB: http://dev.mysql.com/doc/refman/5.6/en/innodb-troubleshooting-datadict.html
InnoDB: for how to resolve the issue.
```

Or they might look like this:

```
2018-07-12 21:24:14 139666981324672 [Note] InnoDB: Ignoring data file 'db1/tab1.ibd' with space ID 200485, since the redo log references db1/tab1.ibd with space ID 200484.
```

Some of the problems related to concurrent DDL are described below.

Problems solved by setting [--lock-ddl-per-table](mariadb-backup-options.md#lock-ddl-per-table) (`mariadb-backup` command-line option added in [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1029-release-notes)):

* If a table is dropped during the backup, then it might still exists after the backup is prepared.
* If a table exists when the backup starts, but it is dropped before the backup copies it, then the tablespace file can't be copied, so the backup would fail.

Problems solved by setting [--innodb\_log\_optimize\_ddl=OFF](../../storage-engines/innodb/innodb-system-variables.md#innodb_log_optimize_ddl) (MariaDB Server system variable added in [MariaDB 10.2.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10217-release-notes) and removed in 10.6.0):

*   If the backup noticed concurrent DDL, then it might fail with

    ```
    ALTER TABLE or OPTIMIZE TABLE was executed during backup
    ```

Problems solved by [--innodb\_safe\_truncate=ON](../../storage-engines/innodb/innodb-system-variables.md#innodb_safe_truncate) (MariaDB Server system variable in [MariaDB 10.2.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10219-release-notes) and removed in 10.3.0):

* If a table is created during the backup, then it might not exist in the backup after prepare.
* If a table is renamed during the backup after the tablespace file was copied, then the table may not exist after the backup is prepared.
* If a table is dropped and created under the same name during the backup after the tablespace file was copied, then the table will have the wrong tablespace ID when the backup is prepared.

Note that, with the removal of `innodb_log_optimize_ddl` and `innodb_safe_truncate`, the above problems were definitely solved.

Problems solved by other bug fixes:

* If [--lock-ddl-per-table](mariadb-backup-options.md#lock-ddl-per-table) is used and if a table is concurrently being dropped or renamed, then mariadb-backup can fail to acquire the MDL lock.

These problems are only fixed in MariaDB 10.2 and later, so it is not recommended to execute concurrent DDL when using `mariadb-backup` with MariaDB 10.1.

See [MDEV-13563](https://jira.mariadb.org/browse/MDEV-13563), [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564), [MDEV-16809](https://jira.mariadb.org/browse/MDEV-16809), and [MDEV-16791](https://jira.mariadb.org/browse/MDEV-16791) for more information.

### Manual Restore with Pre-existing InnoDB Redo Log files

Prior to [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10210-release-notes), `mariadb-backup` users could run into issues if they restored a backup by manually copying the files from the backup into the datadir while the directory still contained pre-existing [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) files. The backup itself did not contain InnoDB redo log files with the traditional `ib_logfileN` file names, so the pre-existing log files would remain in the datadir. If the server were started with these pre-existing log files, then it could perform crash recovery with them, which could cause the database to become inconsistent or corrupt.

In these MariaDB versions, this problem could be avoided by not restoring the backup by manually copying the files and instead restoring the backup by using `mariadb-backup` and providing the [--copy-back](mariadb-backup-options.md#copy-back) option, since `mariadb-backup` deletes pre-existing InnoDB redo log files from the datadir during the restore process.

In [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10210-release-notes) and later, `mariadb-backup` prevents this issue by creating an empty [InnoDB redo log](../../storage-engines/innodb/innodb-redo-log.md) file called `ib_logfile0` as part of the [--prepare](mariadb-backup-options.md#prepare) stage. That way, if the backup is manually restored, any pre-existing InnoDB redo log files would get overwritten by the empty one.

See [MDEV-13311](https://jira.mariadb.org/browse/MDEV-13311) for more information.

### Too Many Open Files

If `mariadb-backup` uses more file descriptors than the system is configured to allow, then users can see errors like the following:

```
2019-02-12 09:48:38 7ffff7fdb820  InnoDB: Operating system error number 23 in a file operation.
InnoDB: Error number 23 means 'Too many open files in system'.
InnoDB: Some operating system error numbers are described at
InnoDB: http://dev.mysql.com/doc/refman/5.6/en/operating-system-error-codes.html
InnoDB: Error: could not open single-table tablespace file ./db1/tab1.ibd
InnoDB: We do not continue the crash recovery, because the table may become
InnoDB: corrupt if we cannot apply the log records in the InnoDB log to it.
InnoDB: To fix the problem and start mysqld:
InnoDB: 1) If there is a permission problem in the file and mysqld cannot
InnoDB: open the file, you should modify the permissions.
InnoDB: 2) If the table is not needed, or you can restore it from a backup,
InnoDB: then you can remove the .ibd file, and InnoDB will do a normal
InnoDB: crash recovery and ignore that table.
InnoDB: 3) If the file system or the disk is broken, and you cannot remove
InnoDB: the .ibd file, you can set innodb_force_recovery > 0 in my.cnf
InnoDB: and force InnoDB to continue crash recovery here.
```

Prior to [MariaDB 10.1.39](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10139-release-notes), [MariaDB 10.2.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10224-release-notes), and [MariaDB 10.3.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10314-release-notes), `mariadb-backup` would actually ignore the error and continue the backup. In some of those cases, `mariadb-backup` would even report a successful completion of the backup to the user. In later versions, `mariadb-backup` will properly throw an error and abort when this error is encountered. See [MDEV-19060](https://jira.mariadb.org/browse/MDEV-19060) for more information.

When this error is encountered, one solution is to explicitly specify a value for the [--open-files-limit](mariadb-backup-options.md#open-files-limit) option either on the command line or in one of the supported [server option group](mariadb-backup-overview.md#server-option-groups)s in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```bash
[mariadb-backup]
open_files_limit=65535
```

An alternative solution is to set the soft and hard limits for the user account that runs `mariadb-backup` by adding new limits to [/etc/security/limits.conf](https://linux.die.net/man/5/limits.conf). For example, if `mariadb-backup` is run by the `mysql` user, then you could add lines like the following:

```
mysql soft nofile 65535
mysql hard nofile 65535
```

After the system is rebooted, the above configuration should set new open file limits for the `mysql` user, and the user's `ulimit` output should look like the following:

```bash
ulimit -Sn
65535
ulimit -Hn
65535
```

### Versions

| mariadb-backup/Server Version                                                                                                                                                                                                                                                                                                                                              | Maturity |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10210-release-notes)+, [MariaDB 10.1.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10126-release-notes)+ | Stable   |
| [MariaDB 10.2.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1027-release-notes)+, [MariaDB 10.1.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10125-release-notes)    | Beta     |
| [MariaDB 10.1.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10123-release-notes)                                                                                                                                                                                        | Alpha    |

## See Also

* [mariadb-dump/mysqldump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md)
* [How to backup with MariaDB](https://www.youtube.com/watch?v=xB4ImmmzXqU) (video)
* [MariaDB point-in-time recovery](https://www.youtube.com/watch?v=ezHmnNmmcDo) (video)
* [mariadb-backup and Restic](https://www.youtube.com/watch?v=b-KFj8GfvzE) (video)
* [Percona Xtrabackup 2.3 documentation](https://www.percona.com/doc/percona-xtrabackup/2.3/index.html/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
