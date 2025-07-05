# InnoDB Temporary Tablespaces

When the user creates a temporary table using the [CREATE TEMPORARY TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement and the engine is set as InnoDB, MariaDB creates a temporary tablespace file. When the table is not compressed, MariaDB writes to a shared temporary tablespace as defined by the [innodb\_temp\_data\_file\_path](../innodb-system-variables.md#innodb_temp_data_file_path) system variable. MariaDB does not allow the creation of ROW\_FORMAT=COMPRESSED temporary tables. All temporary tables will be uncompressed. MariaDB deletes temporary tablespaces when the server shuts down gracefully and is recreated when it starts again. It cannot be placed on a raw device.

Internal temporary tablespaces, (that is, temporary tables that cannot be kept in memory) use either Aria or MyISAM, depending on the [aria\_used\_for\_temp\_tables](../../aria/aria-system-variables.md#aria_used_for_temp_tables) system variable. You can set the default storage engine for user-created temporary tables using the [default\_tmp\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_tmp_storage_engine) system variable.

Prior to [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102), temporary tablespaces existed as part of the InnoDB [system](innodb-system-tablespaces.md) tablespace or were file-per-table depending on the configuration of the [innodb\_file\_per\_table](../innodb-system-variables.md#innodb_file_per_table) system variable.

## Syntax for the value of the innodb\_temp\_data\_file\_path variable

The options for [innodb\_temp\_data\_file\_path](../innodb-system-variables.md#innodb_temp_data_file_path) is one path or a set of paths, separated by ';'.

The syntax for each path is:

```
path:size[:autoextend][:max:size][:autoshrink]
```

`size` can have extensions 'G' (Gigabytes), 'M' (Megabytes) or 'K' (Kilobytes). If no extension is given, then megabytes is assumed.

* The first `size` argument is the initial size of the temporary table space.
* `autoextend` means that the file size will automatically increase if needed.
* `max` can be used to limit the total size of the temporary file if `autoextend` is used.
* `autoshrink` means that the file will shrink to original size when possible.

Only the last path can have the `autoextend` , `max` and `autoshrink` options.

## Sizing Temporary Tablespaces

In order to size temporary tablespaces, use the [innodb\_temp\_data\_file\_path](../innodb-system-variables.md#innodb_temp_data_file_path) system variable. This system variable can be specified as a command-line argument to [mysqld](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
innodb_temp_data_file_path=ibtmp1:32M:autoextend
```

This system variable's syntax is the same as the [innodb\_data\_file\_path](../innodb-system-variables.md#innodb_data_file_path) system variable. That is, a file name, size and option. By default, it writes a 12MB autoextending file to `ibtmp1` in the data directory.

To increase the size of the temporary tablespace, you can add a path to an additional tablespace file to the value of the [innodb\_temp\_data\_file\_path](../innodb-system-variables.md#innodb_temp_data_file_path) system variable. Providing additional paths allows you to spread the temporary tablespace between multiple tablespace files. The last file can have the `autoextend` attribute, which ensures that you won't run out of space. For example:

```
[mariadb]
...
innodb_temp_data_file_path=ibtmp1:32M;ibtmp2:32M:autoextend
```

Unlike normal tablespaces, temporary tablespaces are deleted when you stop MariaDB. To shrink temporary tablespaces to their minimum sizes, restart the server.

## Shrinking the Tablespace

**MariaDB starting with** [**11.3**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113)

From [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes), the temporary tablespace can be shrunk by setting [innodb\_truncate\_temporary\_tablespace\_now](../innodb-system-variables.md#innodb_truncate_temporary_tablespace_now) to ON:

```
SET GLOBAL innodb_truncate_temporary_tablespace_now=1;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
