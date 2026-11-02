---
description: >-
  Plugin API reference: Audit Class: Table. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# Audit Class: Table

> [`Plugin API`](../../) / [`Plugin Types`](../) / [`Audit Plugin`](./)

LOCK occurs when a connection "locks" (this does not necessarily mean a table lock and also happens for row-locking engines) the table at the beginning of a statement. This event is generated at the beginning of every statement for every affected table, unless there's a LOCK TABLES statement in effect (in which case it is generated once for LOCK TABLES and then is suppressed until the tables are unlocked).

CREATE/DROP/RENAME occur when a table is created, dropped, or renamed.

## Classes

| Name                                                          | Description |
| ------------------------------------------------------------- | ----------- |
| [`mysql_event_table`](audit_table_class.md#mysql_event_table) |             |

## Macros

| Name                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [`MYSQL_AUDIT_TABLE_CLASS`](audit_table_class.md#mysql_audit_table_class)         |             |
| [`MYSQL_AUDIT_TABLE_CLASSMASK`](audit_table_class.md#mysql_audit_table_classmask) |             |
| [`MYSQL_AUDIT_TABLE_LOCK`](audit_table_class.md#mysql_audit_table_lock)           |             |
| [`MYSQL_AUDIT_TABLE_CREATE`](audit_table_class.md#mysql_audit_table_create)       |             |
| [`MYSQL_AUDIT_TABLE_DROP`](audit_table_class.md#mysql_audit_table_drop)           |             |
| [`MYSQL_AUDIT_TABLE_RENAME`](audit_table_class.md#mysql_audit_table_rename)       |             |
| [`MYSQL_AUDIT_TABLE_ALTER`](audit_table_class.md#mysql_audit_table_alter)         |             |

***

### MYSQL\_AUDIT\_TABLE\_CLASS

```cpp
#define MYSQL_AUDIT_TABLE_CLASS 15
```

Defined in plugin\_audit.h:145

***

### MYSQL\_AUDIT\_TABLE\_CLASSMASK

```cpp
#define MYSQL_AUDIT_TABLE_CLASSMASK (1 << MYSQL_AUDIT_TABLE_CLASS)
```

Defined in plugin\_audit.h:146

***

### MYSQL\_AUDIT\_TABLE\_LOCK

```cpp
#define MYSQL_AUDIT_TABLE_LOCK 0
```

Defined in plugin\_audit.h:147

***

### MYSQL\_AUDIT\_TABLE\_CREATE

```cpp
#define MYSQL_AUDIT_TABLE_CREATE 1
```

Defined in plugin\_audit.h:148

***

### MYSQL\_AUDIT\_TABLE\_DROP

```cpp
#define MYSQL_AUDIT_TABLE_DROP 2
```

Defined in plugin\_audit.h:149

***

### MYSQL\_AUDIT\_TABLE\_RENAME

```cpp
#define MYSQL_AUDIT_TABLE_RENAME 3
```

Defined in plugin\_audit.h:150

***

### MYSQL\_AUDIT\_TABLE\_ALTER

```cpp
#define MYSQL_AUDIT_TABLE_ALTER 4
```

Defined in plugin\_audit.h:151

## Class Definitions

### mysql\_event\_table

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_table
```

Defined in plugin\_audit.h:153

#### Public Attributes

| Return                                                                                                                                       | Name                                                    | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------- |
| `unsigned int`                                                                                                                               | [`event_subclass`](audit_table_class.md#event_subclass) |             |
| `unsigned long`                                                                                                                              | [`thread_id`](audit_table_class.md#thread_id)           |             |
| `const char *`                                                                                                                               | [`user`](audit_table_class.md#user)                     |             |
| `const char *`                                                                                                                               | [`priv_user`](audit_table_class.md#priv_user)           |             |
| `const char *`                                                                                                                               | [`priv_host`](audit_table_class.md#priv_host)           |             |
| `const char *`                                                                                                                               | [`external_user`](audit_table_class.md#external_user)   |             |
| `const char *`                                                                                                                               | [`proxy_user`](audit_table_class.md#proxy_user)         |             |
| `const char *`                                                                                                                               | [`host`](audit_table_class.md#host)                     |             |
| `const char *`                                                                                                                               | [`ip`](audit_table_class.md#ip)                         |             |
| `unsigned int`                                                                                                                               | [`port`](audit_table_class.md#port)                     |             |
| [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string) | [`database`](audit_table_class.md#database)             |             |
| [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string) | [`table`](audit_table_class.md#table)                   |             |
| [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string) | [`new_database`](audit_table_class.md#new_database)     |             |
| [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string) | [`new_table`](audit_table_class.md#new_table)           |             |
| `int`                                                                                                                                        | [`read_only`](audit_table_class.md#read_only)           |             |
| `unsigned long long`                                                                                                                         | [`query_id`](audit_table_class.md#query_id)             |             |

***

#### event\_subclass

```cpp
unsigned int event_subclass
```

Defined in plugin\_audit.h:155

***

#### thread\_id

```cpp
unsigned long thread_id
```

Defined in plugin\_audit.h:156

***

#### user

```cpp
const char * user
```

Defined in plugin\_audit.h:157

***

#### priv\_user

```cpp
const char * priv_user
```

Defined in plugin\_audit.h:158

***

#### priv\_host

```cpp
const char * priv_host
```

Defined in plugin\_audit.h:159

***

#### external\_user

```cpp
const char * external_user
```

Defined in plugin\_audit.h:160

***

#### proxy\_user

```cpp
const char * proxy_user
```

Defined in plugin\_audit.h:161

***

#### host

```cpp
const char * host
```

Defined in plugin\_audit.h:162

***

#### ip

```cpp
const char * ip
```

Defined in plugin\_audit.h:163

***

#### port

```cpp
unsigned int port
```

Defined in plugin\_audit.h:164

***

#### database

```cpp
MYSQL_CONST_LEX_STRING database
```

Type: [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string)

Defined in plugin\_audit.h:165

***

#### table

```cpp
MYSQL_CONST_LEX_STRING table
```

Type: [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string)

Defined in plugin\_audit.h:166

***

#### new\_database

```cpp
MYSQL_CONST_LEX_STRING new_database
```

Type: [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string)

Defined in plugin\_audit.h:168

***

#### new\_table

```cpp
MYSQL_CONST_LEX_STRING new_table
```

Type: [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string)

Defined in plugin\_audit.h:169

***

#### read\_only

```cpp
int read_only
```

Defined in plugin\_audit.h:171

***

#### query\_id

```cpp
unsigned long long query_id
```

Defined in plugin\_audit.h:173
