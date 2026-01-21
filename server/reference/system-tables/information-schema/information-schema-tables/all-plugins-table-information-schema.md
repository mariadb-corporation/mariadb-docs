---
description: >-
  The Information Schema ALL_PLUGINS table contains information about server
  plugins, whether installed or not, providing a superset of SHOW PLUGINS
  SONAME.
---

# Information Schema ALL\_PLUGINS Table

## Description

The [Information Schema](../) `ALL_PLUGINS` table contains information about [server plugins](../../../plugins/), whether installed or not.

It contains the following columns:

| Column                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PLUGIN\_NAME             | Name of the plugin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PLUGIN\_VERSION          | Version from the plugin's general type descriptor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PLUGIN\_STATUS           | Plugin status, one of ACTIVE, INACTIVE, DISABLED, DELETED or NOT INSTALLED.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
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

It provides a superset of the information shown by the [SHOW PLUGINS SONAME](../../../sql-statements/administrative-sql-statements/show/show-plugins-soname.md) statement, as well as the [information\_schema.PLUGINS](plugins-table-information-schema.md) table. For specific information about storage engines (a particular type of plugin), see the [Information Schema ENGINES table](information-schema-engines-table.md) and the [SHOW ENGINES](../../../sql-statements/administrative-sql-statements/show/show-engines.md) statement.

The table is not a standard Information Schema table, and is a MariaDB extension.

## Example

```sql
SELECT * FROM information_schema.all_plugins\G
*************************** 1. row ***************************
           PLUGIN_NAME: binlog
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: STORAGE ENGINE
   PLUGIN_TYPE_VERSION: 100314.0
        PLUGIN_LIBRARY: NULL
PLUGIN_LIBRARY_VERSION: NULL
         PLUGIN_AUTHOR: MySQL AB
    PLUGIN_DESCRIPTION: This is a pseudo storage engine to represent the binlog in a transaction
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: FORCE
       PLUGIN_MATURITY: Stable
   PLUGIN_AUTH_VERSION: 1.0
*************************** 2. row ***************************
           PLUGIN_NAME: mysql_native_password
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: AUTHENTICATION
   PLUGIN_TYPE_VERSION: 2.1
        PLUGIN_LIBRARY: NULL
PLUGIN_LIBRARY_VERSION: NULL
         PLUGIN_AUTHOR: R.J.Silk, Sergei Golubchik
    PLUGIN_DESCRIPTION: Native MySQL authentication
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: FORCE
       PLUGIN_MATURITY: Stable
   PLUGIN_AUTH_VERSION: 1.0
*************************** 3. row ***************************
           PLUGIN_NAME: mysql_old_password
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: AUTHENTICATION
   PLUGIN_TYPE_VERSION: 2.1
        PLUGIN_LIBRARY: NULL
PLUGIN_LIBRARY_VERSION: NULL
         PLUGIN_AUTHOR: R.J.Silk, Sergei Golubchik
    PLUGIN_DESCRIPTION: Old MySQL-4.0 authentication
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: FORCE
       PLUGIN_MATURITY: Stable
   PLUGIN_AUTH_VERSION: 1.0
...
*************************** 104. row ***************************
           PLUGIN_NAME: WSREP_MEMBERSHIP
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: NOT INSTALLED
           PLUGIN_TYPE: INFORMATION SCHEMA
   PLUGIN_TYPE_VERSION: 100314.0
        PLUGIN_LIBRARY: wsrep_info.so
PLUGIN_LIBRARY_VERSION: 1.13
         PLUGIN_AUTHOR: Nirbhay Choubey
    PLUGIN_DESCRIPTION: Information about group members
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: OFF
       PLUGIN_MATURITY: Stable
   PLUGIN_AUTH_VERSION: 1.0
*************************** 105. row ***************************
           PLUGIN_NAME: WSREP_STATUS
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: NOT INSTALLED
           PLUGIN_TYPE: INFORMATION SCHEMA
   PLUGIN_TYPE_VERSION: 100314.0
        PLUGIN_LIBRARY: wsrep_info.so
PLUGIN_LIBRARY_VERSION: 1.13
         PLUGIN_AUTHOR: Nirbhay Choubey
    PLUGIN_DESCRIPTION: Group view information
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: OFF
       PLUGIN_MATURITY: Stable
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
