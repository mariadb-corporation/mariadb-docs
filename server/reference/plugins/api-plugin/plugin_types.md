---
description: >-
  Plugin API reference: Plugin Types. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin Types

> [`Plugin API`](plugin_api.md)

The available plugin APIs (types).

## Groups

| Name | Description |
|------|-------------|
| [`Daemon Plugin`](daemon_plugin_data.md) | API for Daemon plugin. ([MYSQL_DAEMON_PLUGIN](api.md#mysql_daemon_plugin)) |
| [`Information Schema Plugin`](information_schema_plugin_data.md) | API for I_S plugin. ([MYSQL_INFORMATION_SCHEMA_PLUGIN](api.md#mysql_information_schema_plugin)) |
| [`Storage Engine Plugin`](storage_engine_plugin_data.md) | API for Storage Engine plugin. ([MYSQL_STORAGE_ENGINE_PLUGIN](api.md#mysql_storage_engine_plugin)) |
| [`Replication Plugin`](replication_plugin_data.md) | API for Replication plugin. ([MYSQL_REPLICATION_PLUGIN](api.md#mysql_replication_plugin)) |
| [`Audit Plugin`](audit_plugin_data.md) | API for Audit plugin. ([MYSQL_AUDIT_PLUGIN](api.md#mysql_audit_plugin)) |
| [`Authentication Plugin`](authentication_plugin.md) | API for Authentication plugin. ([MYSQL_AUTHENTICATION_PLUGIN](api.md#mysql_authentication_plugin)) |
| [`Data Type Plugin`](data_type_plugin.md) | API for data type plugins. ([MariaDB_DATA_TYPE_PLUGIN](api.md#mariadb_data_type_plugin)) |
| [`Encryption Plugin`](encryption_plugin_data.md) | API for Encryption plugin. ([MariaDB_ENCRYPTION_PLUGIN](api.md#mariadb_encryption_plugin)) |
| [`Full-Text Parser Plugin`](ftparser_plugin_data.md) | API for Full-text parser plugin. ([MYSQL_FTPARSER_PLUGIN](api.md#mysql_ftparser_plugin)) |
| [`Function Plugin`](function_plugin_data.md) | API for Function plugin. ([MariaDB_FUNCTION_INTERFACE_VERSION](api.md#mariadb_function_interface_version)) |
| [`Password Validation Plugin`](password_validation_plugin_data.md) | Password validation plugin API ([MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION](api.md#mariadb_password_validation_interface_version)) |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_UDF_PLUGIN`](#mysql_udf_plugin)  | not implemented <br/> |
| [`MYSQL_STORAGE_ENGINE_PLUGIN`](#mysql_storage_engine_plugin)  | Storage engine plugin <br/> |
| [`MYSQL_FTPARSER_PLUGIN`](#mysql_ftparser_plugin)  | Full-text parser plugin <br/> |
| [`MYSQL_DAEMON_PLUGIN`](#mysql_daemon_plugin)  | Daemon plugin <br/> |
| [`MYSQL_INFORMATION_SCHEMA_PLUGIN`](#mysql_information_schema_plugin)  | Information schema plugin |
| [`MYSQL_AUDIT_PLUGIN`](#mysql_audit_plugin)  | Audit plugin <br/> |
| [`MYSQL_REPLICATION_PLUGIN`](#mysql_replication_plugin)  | Replication plugin <br/> |
| [`MYSQL_AUTHENTICATION_PLUGIN`](#mysql_authentication_plugin)  | Authentication plugin <br/> |
| [`MYSQL_MAX_PLUGIN_TYPE_NUM`](#mysql_max_plugin_type_num)  |  |
| [`MariaDB_PASSWORD_VALIDATION_PLUGIN`](#mariadb_password_validation_plugin)  | Client and server password validation Encryption and key management plugins |
| [`MariaDB_ENCRYPTION_PLUGIN`](#mariadb_encryption_plugin)  | Plugins for SQL data storage types |
| [`MariaDB_DATA_TYPE_PLUGIN`](#mariadb_data_type_plugin)  | Plugins for new native SQL functions |
| [`MariaDB_FUNCTION_PLUGIN`](#mariadb_function_plugin)  |  |

---

### MYSQL_UDF_PLUGIN

```cpp
#define MYSQL_UDF_PLUGIN 0
```

Defined in plugin.h:127

not implemented <br/>

---

### MYSQL_STORAGE_ENGINE_PLUGIN

```cpp
#define MYSQL_STORAGE_ENGINE_PLUGIN 1
```

Defined in plugin.h:128

Storage engine plugin <br/>

---

### MYSQL_FTPARSER_PLUGIN

```cpp
#define MYSQL_FTPARSER_PLUGIN 2
```

Defined in plugin.h:129

Full-text parser plugin <br/>

---

### MYSQL_DAEMON_PLUGIN

```cpp
#define MYSQL_DAEMON_PLUGIN 3
```

Defined in plugin.h:130

Daemon plugin <br/>

---

### MYSQL_INFORMATION_SCHEMA_PLUGIN

```cpp
#define MYSQL_INFORMATION_SCHEMA_PLUGIN 4
```

Defined in plugin.h:131

Information schema plugin

---

### MYSQL_AUDIT_PLUGIN

```cpp
#define MYSQL_AUDIT_PLUGIN 5
```

Defined in plugin.h:132

Audit plugin <br/>

---

### MYSQL_REPLICATION_PLUGIN

```cpp
#define MYSQL_REPLICATION_PLUGIN 6
```

Defined in plugin.h:133

Replication plugin <br/>

---

### MYSQL_AUTHENTICATION_PLUGIN

```cpp
#define MYSQL_AUTHENTICATION_PLUGIN 7
```

Defined in plugin.h:134

Authentication plugin <br/>

---

### MYSQL_MAX_PLUGIN_TYPE_NUM

```cpp
#define MYSQL_MAX_PLUGIN_TYPE_NUM 12
```

Defined in plugin.h:135

---

### MariaDB_PASSWORD_VALIDATION_PLUGIN

```cpp
#define MariaDB_PASSWORD_VALIDATION_PLUGIN 8
```

Defined in plugin.h:139

Client and server password validation Encryption and key management plugins

---

### MariaDB_ENCRYPTION_PLUGIN

```cpp
#define MariaDB_ENCRYPTION_PLUGIN 9
```

Defined in plugin.h:141

Plugins for SQL data storage types

---

### MariaDB_DATA_TYPE_PLUGIN

```cpp
#define MariaDB_DATA_TYPE_PLUGIN 10
```

Defined in plugin.h:143

Plugins for new native SQL functions

---

### MariaDB_FUNCTION_PLUGIN

```cpp
#define MariaDB_FUNCTION_PLUGIN 11
```

Defined in plugin.h:145

