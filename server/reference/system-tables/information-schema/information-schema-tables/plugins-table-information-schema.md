---
description: >-
  The Information Schema PLUGINS table contains information about server
  plugins, including their status, type, and library paths.
---

# Information Schema PLUGINS Table

The [Information Schema](../) `PLUGINS` table contains information about [server plugins](../../../plugins/).

It contains the following columns:

| Column                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PLUGIN\_NAME             | Name of the plugin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PLUGIN\_VERSION          | Version from the plugin's general type descriptor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PLUGIN\_STATUS           | Plugin status, one of ACTIVE, INACTIVE, DISABLED or DELETED.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PLUGIN\_TYPE             | Plugin type; STORAGE ENGINE, INFORMATION\_SCHEMA, AUTHENTICATION, REPLICATION, DAEMON or AUDIT.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PLUGIN\_TYPE\_VERSION    | Version from the plugin's type-specific descriptor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PLUGIN\_LIBRARY          | Plugin's shared object file name, located in the directory specified by the [plugin\_dir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir) system variable, and used by the [INSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) and [UNINSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) statements. NULL if the plugin is complied in and cannot be uninstalled. |
| PLUGIN\_LIBRARY\_VERSION | Version from the plugin's API interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PLUGIN\_AUTHOR           | Author of the plugin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PLUGIN\_DESCRIPTION      | Description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PLUGIN\_LICENSE          | Plugin's licence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| LOAD\_OPTION             | How the plugin was loaded; one of OFF, ON, FORCE or FORCE\_PLUS\_PERMANENT. See [Installing Plugins](../../../plugins/plugin-overview.md#installing-plugins).                                                                                                                                                                                                                                                                                                                                                                                              |
| PLUGIN\_MATURITY         | Plugin's maturity level; one of Unknown, Experimental, Alpha, Beta,'Gamma, and Stable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PLUGIN\_AUTH\_VERSION    | Plugin's version as determined by the plugin author. An example would be '0.99 beta 1'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

It provides a superset of the information shown by the [SHOW PLUGINS](../../../sql-statements/administrative-sql-statements/show/show-plugins.md) statement. For specific information about storage engines (a particular type of plugins), see the [information\_schema.ENGINES](information-schema-engines-table.md) table and the [SHOW ENGINES](../../../sql-statements/administrative-sql-statements/show/show-engines.md) statement.

This table provides a subset of the Information Schema [information\_schema.ALL\_PLUGINS](all-plugins-table-information-schema.md) table, which contains all available plugins, installed or not.

The table is not a standard Information Schema table, and is a MariaDB extension.

#### Examples

The easiest way to get basic information on plugins is with [SHOW PLUGINS](../../../sql-statements/administrative-sql-statements/show/show-plugins.md):

```sql
SHOW PLUGINS;

+----------------------------+----------+--------------------+-------------+---------+
| Name                       | Status   | Type               | Library     | License |
+----------------------------+----------+--------------------+-------------+---------+
| binlog                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| mysql_native_password      | ACTIVE   | AUTHENTICATION     | NULL        | GPL     |
| mysql_old_password         | ACTIVE   | AUTHENTICATION     | NULL        | GPL     |
| MRG_MyISAM                 | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| MyISAM                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| CSV                        | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| MEMORY                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| FEDERATED                  | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| PERFORMANCE_SCHEMA         | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| Aria                       | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| InnoDB                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| INNODB_TRX                 | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_LOCKS               | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_LOCK_WAITS          | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_CMP                 | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_CMP_RESET           | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_CMPMEM              | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_CMPMEM_RESET        | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_BUFFER_PAGE         | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_BUFFER_PAGE_LRU     | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_BUFFER_POOL_STATS   | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_METRICS             | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_FT_DEFAULT_STOPWORD | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_FT_INSERTED         | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_FT_DELETED          | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_FT_BEING_DELETED    | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_FT_CONFIG           | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_FT_INDEX_CACHE      | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_FT_INDEX_TABLE      | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_SYS_TABLES          | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_SYS_TABLESTATS      | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_SYS_INDEXES         | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_SYS_COLUMNS         | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_SYS_FIELDS          | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_SYS_FOREIGN         | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| INNODB_SYS_FOREIGN_COLS    | ACTIVE   | INFORMATION SCHEMA | NULL        | GPL     |
| SPHINX                     | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| ARCHIVE                    | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| BLACKHOLE                  | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| FEEDBACK                   | DISABLED | INFORMATION SCHEMA | NULL        | GPL     |
| partition                  | ACTIVE   | STORAGE ENGINE     | NULL        | GPL     |
| pam                        | ACTIVE   | AUTHENTICATION     | auth_pam.so | GPL     |
+----------------------------+----------+--------------------+-------------+---------+
```

```sql
SELECT LOAD_OPTION 
FROM INFORMATION_SCHEMA.PLUGINS 
WHERE PLUGIN_NAME LIKE 'tokudb';
Empty SET
```

The equivalent [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md) query would be:

```sql
SELECT PLUGIN_NAME, PLUGIN_STATUS, 
PLUGIN_TYPE, PLUGIN_LIBRARY, PLUGIN_LICENSE
FROM INFORMATION_SCHEMA.PLUGINS;
```

Other [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md) queries can be used to see additional information. For example:

```sql
SELECT PLUGIN_NAME, PLUGIN_DESCRIPTION, 
PLUGIN_MATURITY, PLUGIN_AUTH_VERSION
FROM INFORMATION_SCHEMA.PLUGINS
WHERE PLUGIN_TYPE='STORAGE ENGINE'
ORDER BY PLUGIN_MATURITY \G

*************************** 1. row ***************************
        PLUGIN_NAME: FEDERATED
 PLUGIN_DESCRIPTION: FederatedX pluggable storage engine
    PLUGIN_MATURITY: Beta
PLUGIN_AUTH_VERSION: 2.1
*************************** 2. row ***************************
        PLUGIN_NAME: Aria
 PLUGIN_DESCRIPTION: Crash-safe tables with MyISAM heritage
    PLUGIN_MATURITY: Gamma
PLUGIN_AUTH_VERSION: 1.5
*************************** 3. row ***************************
        PLUGIN_NAME: PERFORMANCE_SCHEMA
 PLUGIN_DESCRIPTION: Performance Schema
    PLUGIN_MATURITY: Gamma
PLUGIN_AUTH_VERSION: 0.1
*************************** 4. row ***************************
        PLUGIN_NAME: binlog
 PLUGIN_DESCRIPTION: This is a pseudo storage engine to represent the binlog in a transaction
    PLUGIN_MATURITY: Stable
PLUGIN_AUTH_VERSION: 1.0
*************************** 5. row ***************************
        PLUGIN_NAME: MEMORY
 PLUGIN_DESCRIPTION: Hash based, stored in memory, useful for temporary tables
    PLUGIN_MATURITY: Stable
PLUGIN_AUTH_VERSION: 1.0
*************************** 6. row ***************************
        PLUGIN_NAME: MyISAM
 PLUGIN_DESCRIPTION: MyISAM storage engine
    PLUGIN_MATURITY: Stable
PLUGIN_AUTH_VERSION: 1.0
*************************** 7. row ***************************
        PLUGIN_NAME: MRG_MyISAM
 PLUGIN_DESCRIPTION: Collection of identical MyISAM tables
    PLUGIN_MATURITY: Stable
PLUGIN_AUTH_VERSION: 1.0
*************************** 8. row ***************************
        PLUGIN_NAME: CSV
 PLUGIN_DESCRIPTION: CSV storage engine
    PLUGIN_MATURITY: Stable
PLUGIN_AUTH_VERSION: 1.0
*************************** 9. row ***************************
        PLUGIN_NAME: InnoDB
 PLUGIN_DESCRIPTION: Supports transactions, row-level locking, and foreign keys
    PLUGIN_MATURITY: Stable
PLUGIN_AUTH_VERSION: 1.2.5
*************************** 10. row ***************************
        PLUGIN_NAME: BLACKHOLE
 PLUGIN_DESCRIPTION: /dev/null storage engine (anything you write to it disappears)
    PLUGIN_MATURITY: Stable
PLUGIN_AUTH_VERSION: 1.0
*************************** 11. row ***************************
        PLUGIN_NAME: ARCHIVE
 PLUGIN_DESCRIPTION: Archive storage engine
    PLUGIN_MATURITY: Stable
PLUGIN_AUTH_VERSION: 1.0
*************************** 12. row ***************************
        PLUGIN_NAME: partition
 PLUGIN_DESCRIPTION: Partition Storage Engine Helper
    PLUGIN_MATURITY: Stable
PLUGIN_AUTH_VERSION: 1.0
```

Check if a given plugin is available:

```sql
SELECT LOAD_OPTION 
FROM INFORMATION_SCHEMA.PLUGINS 
WHERE PLUGIN_NAME LIKE 'tokudb';
Empty SET
```

Show authentication plugins:

```sql
SELECT PLUGIN_NAME, LOAD_OPTION 
FROM INFORMATION_SCHEMA.PLUGINS 
WHERE PLUGIN_TYPE LIKE 'authentication' \G

*************************** 1. row ***************************
PLUGIN_NAME: mysql_native_password
LOAD_OPTION: FORCE
*************************** 2. row ***************************
PLUGIN_NAME: mysql_old_password
LOAD_OPTION: FORCE
```

## See Also

* [List of Plugins](../../../plugins/information-on-plugins/list-of-plugins.md)
* [Plugin Overview](../../../plugins/plugin-overview.md)
* [SHOW PLUGINS](../../../sql-statements/administrative-sql-statements/show/show-plugins.md)
* [INSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)
* [INSTALL SONAME](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)
* [UNINSTALL PLUGIN](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)
* [UNINSTALL SONAME](../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
