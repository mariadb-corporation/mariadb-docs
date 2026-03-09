---
hidden: true
---

# Upgrading from MySQL to MariaDB

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/tWsl3iOmmAdATPgw6nAL/" %}

For all practical purposes, you can view MariaDB as an upgrade of MySQL:

* Before upgrading, please [check if there are any known incompatibilities](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-compatibility) between your MySQL release and the MariaDB release you want to move to.
* In particular, note that the JSON type in MariaDB is a LONGTEXT, while in MySQL it's a binary type. See [Making MariaDB understand MySQL JSON](https://mariadb.org/making-mariadb-understand-mysql-json/).
* If you are using MySQL 8.0 or above, you have to use mysqldump to move your database to MariaDB.
* For upgrading from very old MySQL versions, see Upgrading to MariaDB from MySQL 5.0 (or older version).
* Within the same base version (for example MySQL 5.5 -> MariaDB 5.5, MySQL 5.6 -> [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) and MySQL 5.7 -> [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)) you can in most cases just uninstall MySQL and install MariaDB and you are good to go. There is no need to dump and restore databases. As with any upgrade, we recommend making a backup of your data beforehand.
* You should run mariadb-upgrade (as you would with `mysql_upgrade` in MySQL) to finish the upgrade. This is needed to ensure that your mysql privilege and event tables are updated with the new fields MariaDB uses. Note that if you use a MariaDB package, `mariadb-upgrade` is usually run automatically.
* All your old clients and connectors (PHP, Perl, Python, Java, etc.) will work unchanged (no need to recompile). This works because MariaDB and MySQL use the same client protocol and the client libraries are binary compatible. You can also use your old MySQL connector packages with MariaDB if you want.

### Upgrading from MySQL 5.6 or MySQL 5.7

#### Prerequisites

Check the values of the following server variables:

* innodb\_file\_per\_table
* innodb\_fast\_shutdown

```sql
SELECT @@Innodb_file_per_table,@@Innodb_fast_shutdown\G
```

innodb\_file\_per\_table should be 1. This is the default setting for MySQL and MariaDB. If not, one should use mysqldump for migration as some of the following recommendations will not work.

innodb\_fast\_shutdown should be 0 (at least on the migrated server during shutdown, to ensure that a full shutdown is done when taking server down). This is required when upgrading between major versions of both MySQL and MariaDB as the format of the undo or redo files can change between major versions. This variable can be set just before doing the shutdown.

If your distribution allows it, install the MariaDB packages or the MariaDB tar distribution on the database server. Do not start MariaDB yet! This will decrease the downtime while doing the migration.

#### MySQL `caching_sha256_password` Authentication

MariaDB does not support the `caching_sha256_password` authentication protocol (which is cumbersome and not secure for in-house attacks, since clear-text passwords are available inside the server). Still, we're considering implementing it for MySQL compatibility; see [MDEV-9804](https://jira.mariadb.org/browse/MDEV-9804) / Implement a `caching_sha256_password` plugin.

You can check which MySQL users are using SHA-256 or `caching_sha256_password` by executing:

```sql
SELECT user, plugin FROM mysql.user WHERE plugin LIKE "%sha%";
```

You can change the user to use a protocol compatible with both MySQL and MariaDB with:

```sql
ALTER USER user_name IDENTIFIED WITH mysql_native_password BY  'new_password';
```

#### JSON

MariaDB stores JSON differently than MySQL. Normally you do not have to do anything when migrating JSON data, except if you are using replication or Galera. If this is the case, then you should convert your `JSON` columns to `TEXT` to ensure that all data is stored identically in MySQL and MariaDB:

* If you are using `JSON` columns and want to upgrade to MariaDB, use the mysql\_json plugin to automatically convert MySQL `JSON` to `TEXT`.
* Alternatively, you need to either convert them to `TEXT` or use mysqldump to copy these tables to MariaDB.

Check if you have tables that use the MySQL `JSON` type:

```sql
SELECT table_schema, table_name FROM information_schema.COLUMNS 
WHERE data_type="JSON";
```

You can convert the JSON column to text with:

```sql
ALTER TABLE table_name MODIFY json_column LONGTEXT;
```

#### XA

When doing a backup, ensure that there are no active XA transactions in the backup, as these transactions needs to be committed/rolled back before the migration.

#### Encryption and Compression

Encryption and compression are very different in MySQL and MariaDB.

Encrypted/compressed tables need to be de-encrypted/de-compressed before starting the conversion, and then encrypted/compressed again afterwards.

Detect compressed tables:

```sql
SELECT table_name, create_options FROM information_schema.TABLES WHERE
create_options LIKE "%comp%";
```

#### Config Files

* Create configuration files for MariaDB that match the MySQL cluster option files.
* There are some configuration options that differ. See [System Variable Differences between MariaDB and MySQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/system-variable-differences-between-mariadb-and-mysql).
* You can use `[mariadb]` or `[mariadb-x.y.z]` (for the specific version) in the current config files for MariaDB-specific options.
* You can also place MySQL-specific options inside a `[mysqld-5.7]` section. This includes all options that use mysql-specific directories for logging or replication (on other words, paths with `mysql` as part of the path).
* With a combination of these, it's easy to create a config file that will work with both MariaDB and MySQL, no matter what options are present.
* See also [MDEV-32745](https://jira.mariadb.org/browse/MDEV-32745) for an upcoming tool to automatically detect incompatible options.

**Audit plugin**

* MariaDB does not have the `audit_log_plugin`. Rather, MariaDB uses the `server_audit` plugin, which takes different options.

#### Common Steps

* Perform all the prerequisite steps (SHA-256) on the MySQL Server.
* If replication is used, do these steps also on the primary.
* Take a backup.
* Install the MariaB packages or MariaDB tar distribution.
* Change the `my.cnf` file to work with both MariaDB and MySQL.
* When MariaDB is installed, test your configuration files with\
  `mariadbd --help --verbose > /tmp/log 2>&1`\
  which will display all unsupported config options. It's also possible to use the script at [MDEV-32745](https://jira.mariadb.org/browse/MDEV-32745) to find all unsupported options.
* Check the log for `ERROR` and change the configuration files if needed.

#### Sample Steps for Single Instance MySQL Server

In the shell:

```bash
shell> mysql --user=root ...##
```

In MySQL:

```sql
SET @@global.innodb_fast_shutdown=0;
quit
```

* Take down the node with `mysqladmin shutdown` or `sudo service mysqld stop`:

```bash
shell> mysqladmin --user=root shutdown
```

* Drop the MySQL packages:

```bash
shell> yum -y remove Percona-Server*
```

or

```bash
shell> rpm -q -a | grep Percona | xargs rpm -e --nodeps
```

or

```bash
shell> rpm -q -a | grep -i mysql | xargs rpm -e --nodeps
```

* This can also be done later if you have both MySQL and MariaDB installed at the same time.
* Remove the unsupported `auditlog` (only relevant with Percona server):

```bash
shell> mv /etc/my.cnf.d/auditlog.cnf /etc/my.cnf.d/auditlog.cnf-backup
```

* Install MariaDB if not already installed from the [download site](https://mariadb.org/download/)
* Using the repo is recommended, or

```bash
shell> yum install MariaDB-server MariaDB-client
```

* Start mariadbd on the node data

```bash
systemctl start mariadb.service
```

* If the service does not start, check the error file. Remove all unsupported options from the config files and try again.
* Run mariadb-upgrade:

```bash
mariadb-upgrade
```

* If there were problems with a plugin that does not work or is not supported, you can disable it with:

```bash
mariadb mysql
```

* Then, from the MariaDB client:

```sql
SELECT * FROM mysql.plugin
```

* And then for each unsupported plugin:

```sql
UNINSTALL PLUGIN IF EXISTS #plugin_name#;
```

* Test your new server.
* As long as you do not create new tables or alter tables, it should be possible to go back to MySQL by dropping all tables in the 'mysql' database:

```sql
SET @@global.innodb_fast_shutdown=0;
SHUTDOWN
```

* Start MySQL server with `--skip-grants`.
* Install the backup of the 'mysql' database with:

```bash
shell> mysql mysql < /tmp/mysql-dump.txt
shell> mysqladmin flush-privileges
```

#### MySQL replication setup

In case of replication you can either convert one of the existing nodes directly to MariaDB or create a new node, convert that to MariaDB and then delete the old MySQL node after testing.

* Do all the "Prerequisite steps" on the to-be-converted node.
* Follow the Single instance MySQL server instructions for the node.
* Start MariaDB as a replica to MySQL.
* Test that the new node works as expected.
* Note that a MariaDB replica will work with replication positions, not with MySQL GTID.
* Repeat with all other nodes.
* Switch one of the MariaDB nodes to be the primary.
* Convert the old primary according to the above instructions.
* Add the old primary as a replica.

### Upgrading on Windows

On Windows, you should not uninstall MySQL and then install MariaDB. This would not work, because the existing database will not be found.

Instead, install MariaDB and use the upgrade wizard which is part of installer package and is launched by MSI installer. Or use `mysql_upgrade_service <service_name>` on the command line.

### Upgrading my.cnf

All the options in your original MySQL my.cnf file should work fine for MariaDB.

However, as MariaDB has more features than MySQL, there are a few things that you should consider changing in your `my.cnf` file.

* MariaDB uses the Aria storage engine by default for internal temporary files, instead of MyISAM. If you have a lot of temporary files, you should add and set aria-pagecache-buffer-size to the same value as you have for key-buffer-size.
* If you don't use MyISAM tables, you can set key-buffer-size to a very low value, like 64K.
* If you have a LOT of connections (> 100) that mostly run short running queries, you should consider using the thread pool. For example using : thread\_handling=pool-of-threads and thread\_pool\_size=128 could give a notable performance boost in this case. Where the `thread_pool_size` should be about `2 * number of cores on your machine`.

### Other Things to Consider

* MariaDB has LGPL versions of the [C Connector](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) and [Java Client](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j). If you are shipping an application that supports MariaDB or MySQL, you should consider using these!
* You should consider trying out the MyRocks storage engine or some of the other new storage engines that MariaDB provides.

### See Also

* MariaDB has a lot of [new features](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-features) that you should know about.
* [MariaDB versus MySQL - Compatibility](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-compatibility)
* Migrating to MariaDB
* You can find general upgrading informations on the MariaDB installation page.
* There is a Screencast for upgrading MySQL to MariaDB.
* Upgrading to MariaDB in Debian 9

<sub>_This page is licensed: This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

<sub>_This page is licensed: This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
