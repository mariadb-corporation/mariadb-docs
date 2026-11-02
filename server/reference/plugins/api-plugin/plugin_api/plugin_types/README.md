---
description: >-
  Plugin API reference: Plugin Types. Generated from the MariaDB server headers
  by doxygen and moxygen.
---

# Plugin Types

> [`Plugin API`](../)

The available plugin APIs (types).

## Groups

| Name                                                               | Description                                                                                                                                                            |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Daemon Plugin`](daemon_plugin_data.md)                           | API for Daemon plugin. ([MYSQL\_DAEMON\_PLUGIN](./#mysql_daemon_plugin))                                                                                               |
| [`Information Schema Plugin`](information_schema_plugin_data.md)   | API for I\_S plugin. ([MYSQL\_INFORMATION\_SCHEMA\_PLUGIN](./#mysql_information_schema_plugin))                                                                        |
| [`Storage Engine Plugin`](storage_engine_plugin_data.md)           | API for Storage Engine plugin. ([MYSQL\_STORAGE\_ENGINE\_PLUGIN](./#mysql_storage_engine_plugin))                                                                      |
| [`Replication Plugin`](replication_plugin_data.md)                 | API for Replication plugin. ([MYSQL\_REPLICATION\_PLUGIN](./#mysql_replication_plugin))                                                                                |
| [`Audit Plugin`](audit_plugin_data/)                               | API for Audit plugin. ([MYSQL\_AUDIT\_PLUGIN](./#mysql_audit_plugin))                                                                                                  |
| [`Authentication Plugin`](authentication_plugin/)                  | API for Authentication plugin. ([MYSQL\_AUTHENTICATION\_PLUGIN](./#mysql_authentication_plugin))                                                                       |
| [`Data Type Plugin`](data_type_plugin.md)                          | API for data type plugins. ([MariaDB\_DATA\_TYPE\_PLUGIN](./#mariadb_data_type_plugin))                                                                                |
| [`Encryption Plugin`](encryption_plugin_data.md)                   | API for Encryption plugin. ([MariaDB\_ENCRYPTION\_PLUGIN](./#mariadb_encryption_plugin))                                                                               |
| [`Full-Text Parser Plugin`](ftparser_plugin_data.md)               | API for Full-text parser plugin. ([MYSQL\_FTPARSER\_PLUGIN](./#mysql_ftparser_plugin))                                                                                 |
| [`Function Plugin`](function_plugin_data.md)                       | API for Function plugin. ([MariaDB\_FUNCTION\_INTERFACE\_VERSION](function_plugin_data.md#mariadb_function_interface_version))                                         |
| [`Password Validation Plugin`](password_validation_plugin_data.md) | Password validation plugin API ([MariaDB\_PASSWORD\_VALIDATION\_INTERFACE\_VERSION](password_validation_plugin_data.md#mariadb_password_validation_interface_version)) |

## Macros

| Name                                                                          | Description                                                                 |
| ----------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [`MYSQL_UDF_PLUGIN`](./#mysql_udf_plugin)                                     | <p>not implemented<br></p>                                                  |
| [`MYSQL_STORAGE_ENGINE_PLUGIN`](./#mysql_storage_engine_plugin)               | <p>Storage engine plugin<br></p>                                            |
| [`MYSQL_FTPARSER_PLUGIN`](./#mysql_ftparser_plugin)                           | <p>Full-text parser plugin<br></p>                                          |
| [`MYSQL_DAEMON_PLUGIN`](./#mysql_daemon_plugin)                               | <p>Daemon plugin<br></p>                                                    |
| [`MYSQL_INFORMATION_SCHEMA_PLUGIN`](./#mysql_information_schema_plugin)       | Information schema plugin                                                   |
| [`MYSQL_AUDIT_PLUGIN`](./#mysql_audit_plugin)                                 | <p>Audit plugin<br></p>                                                     |
| [`MYSQL_REPLICATION_PLUGIN`](./#mysql_replication_plugin)                     | <p>Replication plugin<br></p>                                               |
| [`MYSQL_AUTHENTICATION_PLUGIN`](./#mysql_authentication_plugin)               | <p>Authentication plugin<br></p>                                            |
| [`MYSQL_MAX_PLUGIN_TYPE_NUM`](./#mysql_max_plugin_type_num)                   |                                                                             |
| [`MariaDB_PASSWORD_VALIDATION_PLUGIN`](./#mariadb_password_validation_plugin) | Client and server password validation Encryption and key management plugins |
| [`MariaDB_ENCRYPTION_PLUGIN`](./#mariadb_encryption_plugin)                   | Plugins for SQL data storage types                                          |
| [`MariaDB_DATA_TYPE_PLUGIN`](./#mariadb_data_type_plugin)                     | Plugins for new native SQL functions                                        |
| [`MariaDB_FUNCTION_PLUGIN`](./#mariadb_function_plugin)                       |                                                                             |

***

### MYSQL\_UDF\_PLUGIN

```cpp
#define MYSQL_UDF_PLUGIN 0
```

Defined in plugin.h:127

not implemented<br>

***

### MYSQL\_STORAGE\_ENGINE\_PLUGIN

```cpp
#define MYSQL_STORAGE_ENGINE_PLUGIN 1
```

Defined in plugin.h:128

Storage engine plugin<br>

***

### MYSQL\_FTPARSER\_PLUGIN

```cpp
#define MYSQL_FTPARSER_PLUGIN 2
```

Defined in plugin.h:129

Full-text parser plugin<br>

***

### MYSQL\_DAEMON\_PLUGIN

```cpp
#define MYSQL_DAEMON_PLUGIN 3
```

Defined in plugin.h:130

Daemon plugin<br>

***

### MYSQL\_INFORMATION\_SCHEMA\_PLUGIN

```cpp
#define MYSQL_INFORMATION_SCHEMA_PLUGIN 4
```

Defined in plugin.h:131

Information schema plugin

***

### MYSQL\_AUDIT\_PLUGIN

```cpp
#define MYSQL_AUDIT_PLUGIN 5
```

Defined in plugin.h:132

Audit plugin<br>

***

### MYSQL\_REPLICATION\_PLUGIN

```cpp
#define MYSQL_REPLICATION_PLUGIN 6
```

Defined in plugin.h:133

Replication plugin<br>

***

### MYSQL\_AUTHENTICATION\_PLUGIN

```cpp
#define MYSQL_AUTHENTICATION_PLUGIN 7
```

Defined in plugin.h:134

Authentication plugin<br>

***

### MYSQL\_MAX\_PLUGIN\_TYPE\_NUM

```cpp
#define MYSQL_MAX_PLUGIN_TYPE_NUM 12
```

Defined in plugin.h:135

***

### MariaDB\_PASSWORD\_VALIDATION\_PLUGIN

```cpp
#define MariaDB_PASSWORD_VALIDATION_PLUGIN 8
```

Defined in plugin.h:139

Client and server password validation Encryption and key management plugins

***

### MariaDB\_ENCRYPTION\_PLUGIN

```cpp
#define MariaDB_ENCRYPTION_PLUGIN 9
```

Defined in plugin.h:141

Plugins for SQL data storage types

***

### MariaDB\_DATA\_TYPE\_PLUGIN

```cpp
#define MariaDB_DATA_TYPE_PLUGIN 10
```

Defined in plugin.h:143

Plugins for new native SQL functions

***

### MariaDB\_FUNCTION\_PLUGIN

```cpp
#define MariaDB_FUNCTION_PLUGIN 11
```

Defined in plugin.h:145
