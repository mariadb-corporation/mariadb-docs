---
description: >-
  This page explains the InnoDB system tablespace (ibdata1), which stores the
  data dictionary, doublewrite buffer, and undo logs, and how to resize it.
---

# InnoDB System Tablespaces

When InnoDB needs to store general information relating to the system as a whole, rather than a specific table, the specific file it writes to is the system tablespace. By default, this is the `ibdata1` file located in the data directory, (as defined by either the [datadir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) or [innodb\_data\_home\_dir](../innodb-system-variables.md#innodb_data_home_dir) system variables). InnoDB uses the system tablespace to store the data dictionary, change buffer, and undo logs.

You can define the system tablespace filename or filenames, size and other options by setting the [innodb\_data\_file\_path](../innodb-system-variables.md#innodb_data_file_path) system variable. This system variable can be specified as a command-line argument to [mariadbd](../../../../server-management/starting-and-stopping-mariadb/mariadbd.md) or it can be specified in a relevant server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
innodb_data_file_path=ibdata1:50M:autoextend
```

This system variable defaults to the file `ibdata1`, and it defaults to a minimum size of `12M`, and it defaults with the `autoextend` attribute enabled.

## Changing Sizes

InnoDB defaults to allocating 12M to the `ibdata1` file for the system tablespace. While this is sufficient for most use cases, it may not be for all. You may find after using MariaDB for a while that the allocation is too small for the system tablespace or it grows too large for your disk. Fortunately, you can adjust this size as need later.

### Increasing the Size

When setting the [innodb\_data\_file\_path](../innodb-system-variables.md#innodb_data_file_path) system variable, you can define a size for each file given. In cases where you need a larger system tablespace, add the `autoextend` option to the last value.

```
[mariadb]
...
innodb_data_file_path=ibdata1:12M;ibdata2:50M:autoextend
```

Under this configuration, when the last system tablespace grows beyond the size allocation, InnoDB increases the size of the file by increments. To control the allocation increment, set the [innodb\_autoextend\_increment](../innodb-system-variables.md#innodb_autoextend_increment) system variable.

### Decreasing the Size

**MariaDB starting with** [**11.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/what-is-mariadb-112)

From [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.0), when MariaDB starts up, unused InnoDB tablespace can be reclaimed, reducing the file size ([MDEV-14795](https://jira.mariadb.org/browse/MDEV-14795)). This is disabled by default and is enabled by adding the `:autoshrink` attribute to the [innodb\_data\_file\_path](../innodb-system-variables.md#innodb_data_file_path) system variable, e.g.:

```
[mariadb]
...
innodb_data_file_path=ibdata1:12M;ibdata2:50M:autoextend:autoshrink
```

Alternatively, starting with [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.3), the shrinking can be set to happen during a slow shutdown (e.g. after `SET GLOBAL innodb_fast_shutdown=0`) ([MDEV-32452](https://jira.mariadb.org/browse/MDEV-32452)).\
Technically, how this works is:

1. Find the last used extent in the system tablespace by iterating through the BITMAP in the extent descriptor page.
2. Check whether the tablespace is being used within fixed size, and if the last used extent is less than the fixed size, then set the desired target size to fixed size.
3. Flush all pages belonging to the system tablespace in flush list.
4. Truncate the truncated pages from FSP\_FREE and FSP\_FREE\_FRAG list.
5. Reset the bitmap in descriptor pages for the truncated pages.
6. Update the FSP\_SIZE and FSP\_FREE\_LIMIT in header page.
7. In case of multiple files, calculate the truncated last file size and do the truncation in last file.

**MariaDB until** [**11.2.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.0)

In cases where the InnoDB system tablespace has grown too large, before [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/what-is-mariadb-112), the process to reduce it in size is a little more complicated than increasing the size. MariaDB does not allow you to remove data from the tablespace file itself. Instead you need to delete the tablespace files themselves, then restore the database from backups.\
The backup utility [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) produces backup files containing the SQL statements needed to recreate the database. As a result, it restores a database with the bare minimum data rather than any additional information that might have built up in the tablespace file.\
Use mariadb-dump to backup all of your InnoDB database tables, including the system tables in the `mysql` database that use InnoDB. You can find out what they are using the Information Schema.

```sql
SELECT TABLE_NAME FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'mysql' AND ENGINE = 'InnoDB';
```

If you only use InnoDB, you may find it easier to back up all databases and tables.

```
$ mariadb-dump -u root -p --all-databases > full-backup.sql
```

Then stop the MariaDB Server and remove the InnoDB tablespace files. In the data directory or the InnoDB data home directory, delete all the `ibdata` and `ib_log` files as well as any file with an `.ibd` or `.frm` extension.\
Once this is done, restart the server and import the dump file:

```
$ mysql -u root -p < full-backup.sql
```

## Using Raw Disk Partitions

Instead of having InnoDB write to the file system, you can set it to use raw disk partitions. On Windows and some Linux distributions, this allows you to perform non-buffered I/O without the file system overhead. Note that in many use cases this may not actually improve performance. Run tests to verify if there are any real gains for your application usage.

To enable a raw disk partition, first start MariaDB with the `newraw` option set on the tablespace:

```
[mariadb]
...
innodb_data_file_path=/dev/sdc:10Gnewraw
```

When the MariaDB Server starts, it initializes the partition. Don't create or change any data, (any data written to InnoDB at this stage are lost on restart). Once the server has successful started, stop it then edit the configuration file again, changing the `newraw` keyword to `raw`.

```
[mariadb]
...
innodb_data_file_path=/dev/sdc:10Graw
```

When you start MariaDB again, it'll read and write InnoDB data to the given disk partition instead of the file system.

### Raw Disk Partitions on Windows

When defining a raw disk partition for InnoDB on the Windows operating system, use the same procedure as defined above, but when defining the path for the [innodb\_data\_file\_path](../innodb-system-variables.md#innodb_data_file_path) system variable, use `./` at the start:

```
[mariadb]
...
innodb_data_file_path=//./E::10Graw
```

The given path is synonymous with the Windows syntax for accessing the physical drive.

## System Tables within the InnoDB System Tablespace

InnoDB creates some system tables within the InnoDB System Tablespace:

* `SYS_DATAFILES`
* `SYS_FOREIGN`
* `SYS_FOREIGN_COLS`
* `SYS_TABLESPACES`
* `SYS_VIRTUAL`
* `SYS_ZIP_DICT`
* `SYS_ZIP_DICT_COLS`

These tables cannot be queried. However, you might see references to them in some places, such as in the [INNODB\_SYS\_TABLES](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table in the [information\_schema](../../../../reference/system-tables/information-schema/information-schema-tables/) database.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
