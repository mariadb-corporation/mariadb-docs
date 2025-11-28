# What to Do if MariaDB Doesn't Start

There could be many reasons that MariaDB fails to start. This page will help troubleshoot some of the more common reasons and provide solutions.

If you have tried everything here and still need help, you can ask for help on IRC or on the forums - see [Where to find other MariaDB users and developers](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/joining-the-community) - or ask a question at the [Starting and Stopping MariaDB](./) page.

## The Error Log and the Data Directory

The reason for the failure will almost certainly be written in the [error log](../server-monitoring-logs/error-log.md) and, if you are starting MariaDB manually, to the console. By default, the error log is named _host-name_.err and is written to the data directory.

Common Locations:

* /var/log/
* /var/log/mysql
* C:\Program Files\MariaDB x.y\data (x.y refers to the version number)
* C:\Program Files (x86)\MariaDB x.y\data (32bit version on 64bit Windows)

It's also possible that the error log has been explicitly written to another location. This is often done by changing the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) or [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) system variables in an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). See the [Option Files](what-to-do-if-mariadb-doesnt-start.md#option-files) below for more information about that.

A quick way to get the values of these system variables is to execute the following commands:

```
mariadbd --help --verbose | grep 'log-error' | tail -1
mariadbd --help --verbose | grep 'datadir' | tail -1
```

## Option Files

Another kind of file to consider when troubleshooting is [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). The default option file is called `my.cnf`. Option files contain configuration options, such as the location of the data directory mentioned above. If you're unsure where the option file is located, see [Configuring MariaDB with Option Files: Default Option File Locations](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#default-option-file-locations) for information on the default locations.

You can check which configuration options MariaDB server will use from its option files by executing the following command:

```
mariadbd --print-defaults
```

You can also check by executing the following command:

```
my_print_defaults --mysqld
```

See [Configuring MariaDB with Option Files: Checking Program Options](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#checking-program-options) for more information on checking configuration options.

### Invalid Option or Option Value

Another potential reason for a startup failure is that an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) contains an invalid option or an invalid option value. In those cases, the [error log](../server-monitoring-logs/error-log.md) should contain an error similar to this:

```
140514 12:19:37 [ERROR] /usr/local/mysql/bin/mariadbd: unknown variable 'option=value'
```

This is more likely to happen when you upgrade to a new version of MariaDB. In most cases, the [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) from the old version of MariaDB will work just fine with the new version. However, occasionally, options are removed in new versions of MariaDB, or the valid values for options are changed in new versions of MariaDB. Therefore, it's possible for an [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) to stop working after an upgrade.

Also, remember that option names are case sensitive.

Examine the specifics of the error. Possible fixes are usually one of the following:

* If the option is completely invalid, then remove it from the [option file](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).
* If the option's name has changed, then fix the name.
* If the option's valid values have changed, then change the option's value to a valid one.
* If the problem is caused by a simple typo, then fix the typo.

## Can't Open Privilege Tables

It is possible to see errors similar to the following:

```
System error 1067 has occurred.
Fatal error: Can't open privilege tables: Table 'mysql.host' doesn't exist
```

If errors like this occur, then critical [system tables](../../reference/system-tables/) are either missing or are in the wrong location. The above error is quite common after an upgrade if the [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) set the [basedir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#basedir) or datadir to a non-standard location, but the new server is using the default location. Therefore, make sure that the basedir and datadir variables are correctly set.

If you're unsure where the option file is located, see Configuring MariaDB with Option Files: Default Option File Locations for information on the default locations.

If the [system tables](../../reference/system-tables/) really do not exist, then you may need to create them with [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md). See [Installing System Tables (mariadb-install-db)](../install-and-upgrade-mariadb/installing-mariadb/installing-system-tables-mariadb-install-db/) for more information.

## Can't Create Test File

One of the first tests on startup is to check whether MariaDB can write to the data directory. When this fails, it will log an error like this:

```
May 13 10:24:28 mariadb3 mariadbd[19221]: 2019-05-13 10:24:28 0 [Warning] Can't create test file /usr/local/data/mariadb/mariadb3.lower-test
May 13 10:24:28 mariadb3 maridbd[19221]: 2019-05-13 10:24:28 0 [ERROR] Aborting
```

This is usually a permission error on the directory in which this file is being written. Ensure that the entire [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) is owned by the user running `mariadbd`, usually `mysql`. Ensure that directories have the "x" (execute) directory permissions for the owner. Ensure that all the parent directories of the datadir upwards have "x" (execute) permissions for all (`user`, `group`, and `other`).

Once this is checked, look at the [systemd](what-to-do-if-mariadb-doesnt-start.md#systemd) and [SELinux](what-to-do-if-mariadb-doesnt-start.md#selinux) documentation below, or [AppArmor](what-to-do-if-mariadb-doesnt-start.md#AppArmorl).

## Can't Lock Aria Control File

On starting MariaDB, the `aria_log_control` file is locked. If a lock cannot be obtained, it will log an error like this:

```
2023-05-01 16:27:03 0 [ERROR] mariadbd: Can't lock aria control file '/var/lib/mysql/aria_log_control' for exclusive use, error: 11. Will retry for 30 seconds
```

This almost always happens because there is already an existing MariaDB service running on this data directory. Recommend aborting this startup and looking closely for the other MariaDB instance.

A less likely case is that file locking is not available, which might occur on an NFS-mounted data directory without proper locking support.

## Unable to lock ./ibdata1 error 11

Like the above for the Aria Control File, this is attempting to exclusively lock the `ibdata1` InnoDB system tablespace. Error 11 corresponds to the system error "OS error code 11: Resource temporarily unavailable," meaning the lock cannot be created.

```
2023-05-01 16:27:34 0 [ERROR] InnoDB: Unable to lock ./ibdata1 error: 11
2023-05-01 16:27:34 0 [Note] InnoDB: Check that you do not already have another mariadbd process using the same InnoDB data or log files.
2023-05-01 16:27:34 0 [ERROR] InnoDB: Plugin initialization aborted with error Generic error
2023-05-01 16:27:35 0 [Note] InnoDB: Starting shutdown...
```

Like the above, this is an indication that a second MariaDB instance is already running on the data directory.

## InnoDB

[InnoDB](../../server-usage/storage-engines/innodb/) is probably the MariaDB component that most frequently causes a crash. In the error log, lines containing InnoDB messages generally start with "InnoDB:".

### Cannot Allocate Memory for the InnoDB Buffer Pool

In a typical installation on a dedicated server, at least 70% of your memory should be assigned to the [InnoDB buffer pool](../../server-usage/storage-engines/innodb/innodb-buffer-pool.md); sometimes it can even reach 85%. But be very careful: don't assign to the buffer pool more memory than it can allocate. If it cannot allocate memory, InnoDB will use the disk's swap area, which is very bad for performance. If swapping is disabled or the swap area is not big enough, InnoDB will crash. In this case, MariaDB will probably try to restart several times, and each time it will log a message like this:

```
140124 17:29:01 InnoDB: Fatal error: cannot allocate memory for the buffer pool
```

In that case, you will need to add more memory to your server/VM or decrease the value of the [innodb\_buffer\_pool\_size](../../server-usage/storage-engines/innodb/innodb-system-variables.md) variable.

Remember that the buffer pool will slightly exceed that limit. Also, remember that MariaDB also needs to allocate memory for other storage engines and several per-connection buffers. The operating system also needs memory.

### InnoDB Table Corruption

By default, InnoDB deliberately crashes the server when it detects table corruption. The reason for this behavior is preventing corruption propagation. However, in some situations, server availability is more important than data integrity. For this reason, we can avoid these crashes by changing the value of [innodb\_corrupt\_table\_action](../../server-usage/storage-engines/innodb/innodb-system-variables.md) to 'warn'.

If InnoDB crashes the server after detecting data corruption, it writes a detailed message in the error log. The first lines are similar to the following:

```
InnoDB: Database page corruption on disk or a failed
InnoDB: file read of page 7.
InnoDB: You may have to recover from a backup.
```

Generally, it is still possible to recover most of the corrupted data. To do so, restart the server in [InnoDB recovery mode](../../server-usage/storage-engines/innodb/innodb-troubleshooting/innodb-recovery-modes.md) and try to extract the data that you want to backup. You can save them in a CSV file or in a non-InnoDB table. Then, restart the server in normal mode and restore the data.

## MyISAM

Most tables in the [mysql](../../reference/system-tables/the-mysql-database-tables/) database are MyISAM tables. These tables are necessary for MariaDB to properly work or even start.

A MariaDB crash could cause system table corruption. With the default settings, MariaDB will simply not start if the system tables are corrupted. With [myisam\_recover\_options](../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options), we can force MyISAM to repair damaged tables.

## systemd

If you are using [systemd](systemd.md), then there are a few relevant notes about startup failures:

* If MariaDB is configured to access files under `/home`, `/root`, or `/run/user`, then the default systemd unit file will prevent access to these directories with a `Permission Denied` error. This happens because the unit file sets [ProtectHome=true](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#ProtectHome=). See [Systemd: Configuring Access to Home Directories](systemd.md#configuring-access-to-home-directories) for information on how to work around this.
* The default systemd unit file also sets [ProtectSystem=full](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#ProtectSystem=), which places restrictions on writing to a few other directories. Overwriting this with `ProtectSystem=off` in the same way as above will restore access to these directories.
* If MariaDB takes longer than 90 seconds to start, then the default systemd unit file will cause it to fail with an error. This happens because the default value for the [TimeoutStartSec](https://www.freedesktop.org/software/systemd/man/systemd.service.html#TimeoutStartSec=) option is 90 seconds. See [Systemd: Configuring the Systemd Service Timeout](systemd.md#configuring-the-systemd-service-timeout) for information on how to work around this.
* The systemd journal may also contain useful information about startup failures. See [Systemd: Systemd Journal](systemd.md#systemd-journal) for more information.

See [systemd](systemd.md) documentation for further information on systemd configuration.

## SELinux

[Security-Enhanced Linux (SELinux)](https://selinuxproject.org/page/Main_Page) is a Linux kernel module that provides a framework for configuring a [mandatory access control (MAC)](https://en.wikipedia.org/wiki/Mandatory_access_control) system for many resources on the system. It is enabled by default on some Linux distributions, including RHEL, CentOS, Fedora, and other similar Linux distributions. SELinux prevents programs from accessing files, directories, or ports unless it is configured to access those resources.

You might need to troubleshoot SELinux-related issues in cases such as:

* MariaDB is using a non-default port.
* MariaDB is reading from or writing to some files (datadir, log files, option files, etc.) located at non-default paths.
* MariaDB is using a plugin that requires access to resources that default installations do not use.

Setting SELinux state to `permissive` is a common way to investigate what is going wrong while allowing MariaDB to function normally. `permissive` is supposed to produce a log entry every time it should block a resource access, without actually blocking it. However, [there are situations](https://danwalsh.livejournal.com/67855.html) when SELinux blocks resource accesses even in `permissive` mode.

See [SELinux](../../security/securing-mariadb/selinux.md) for more information.

## AppArmor

Add the following to `/etc/apparmor.d/tunables/alias` if you have moved the datadir:

```
alias /var/lib/mysql/ -> /data/mariadb/,
```

The restart AppArmor:

```
sudo systemctl restart apparmor
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
