---
description: >-
  Plugin API reference: Audit Class: Table. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Audit Class: Table

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md) / [`Audit Plugin`](audit_plugin_data.md)

LOCK occurs when a connection "locks" (this does not necessarily mean a table lock and also happens for row-locking engines) the table at the beginning of a statement. This event is generated at the beginning of every statement for every affected table, unless there's a LOCK TABLES statement in effect (in which case it is generated once for LOCK TABLES and then is suppressed until the tables are unlocked).

CREATE/DROP/RENAME occur when a table is created, dropped, or renamed.

## Classes

| Name | Description |
|------|-------------|
| [`mysql_event_table`](#mysql_event_table) |  |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_AUDIT_TABLE_CLASS`](#mysql_audit_table_class)  |  |
| [`MYSQL_AUDIT_TABLE_CLASSMASK`](#mysql_audit_table_classmask)  |  |
| [`MYSQL_AUDIT_TABLE_LOCK`](#mysql_audit_table_lock)  |  |
| [`MYSQL_AUDIT_TABLE_CREATE`](#mysql_audit_table_create)  |  |
| [`MYSQL_AUDIT_TABLE_DROP`](#mysql_audit_table_drop)  |  |
| [`MYSQL_AUDIT_TABLE_RENAME`](#mysql_audit_table_rename)  |  |
| [`MYSQL_AUDIT_TABLE_ALTER`](#mysql_audit_table_alter)  |  |

---

### MYSQL_AUDIT_TABLE_CLASS

```cpp
#define MYSQL_AUDIT_TABLE_CLASS 15
```

Defined in plugin_audit.h:145

---

### MYSQL_AUDIT_TABLE_CLASSMASK

```cpp
#define MYSQL_AUDIT_TABLE_CLASSMASK (1 << MYSQL_AUDIT_TABLE_CLASS)
```

Defined in plugin_audit.h:146

---

### MYSQL_AUDIT_TABLE_LOCK

```cpp
#define MYSQL_AUDIT_TABLE_LOCK 0
```

Defined in plugin_audit.h:147

---

### MYSQL_AUDIT_TABLE_CREATE

```cpp
#define MYSQL_AUDIT_TABLE_CREATE 1
```

Defined in plugin_audit.h:148

---

### MYSQL_AUDIT_TABLE_DROP

```cpp
#define MYSQL_AUDIT_TABLE_DROP 2
```

Defined in plugin_audit.h:149

---

### MYSQL_AUDIT_TABLE_RENAME

```cpp
#define MYSQL_AUDIT_TABLE_RENAME 3
```

Defined in plugin_audit.h:150

---

### MYSQL_AUDIT_TABLE_ALTER

```cpp
#define MYSQL_AUDIT_TABLE_ALTER 4
```

Defined in plugin_audit.h:151


## Class Definitions



### mysql_event_table

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_table
```

Defined in plugin_audit.h:153

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned int` | [`event_subclass`](#event_subclass)  |  |
| `unsigned long` | [`thread_id`](#thread_id)  |  |
| `const char *` | [`user`](#user)  |  |
| `const char *` | [`priv_user`](#priv_user)  |  |
| `const char *` | [`priv_host`](#priv_host)  |  |
| `const char *` | [`external_user`](#external_user)  |  |
| `const char *` | [`proxy_user`](#proxy_user)  |  |
| `const char *` | [`host`](#host)  |  |
| `const char *` | [`ip`](#ip)  |  |
| `unsigned int` | [`port`](#port)  |  |
| [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string) | [`database`](#database)  |  |
| [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string) | [`table`](#table)  |  |
| [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string) | [`new_database`](#new_database)  |  |
| [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string) | [`new_table`](#new_table)  |  |
| `int` | [`read_only`](#read_only)  |  |
| `unsigned long long` | [`query_id`](#query_id)  |  |

---

#### event_subclass

```cpp
unsigned int event_subclass
```

Defined in plugin_audit.h:155

---

#### thread_id

```cpp
unsigned long thread_id
```

Defined in plugin_audit.h:156

---

#### user

```cpp
const char * user
```

Defined in plugin_audit.h:157

---

#### priv_user

```cpp
const char * priv_user
```

Defined in plugin_audit.h:158

---

#### priv_host

```cpp
const char * priv_host
```

Defined in plugin_audit.h:159

---

#### external_user

```cpp
const char * external_user
```

Defined in plugin_audit.h:160

---

#### proxy_user

```cpp
const char * proxy_user
```

Defined in plugin_audit.h:161

---

#### host

```cpp
const char * host
```

Defined in plugin_audit.h:162

---

#### ip

```cpp
const char * ip
```

Defined in plugin_audit.h:163

---

#### port

```cpp
unsigned int port
```

Defined in plugin_audit.h:164

---

#### database

```cpp
MYSQL_CONST_LEX_STRING database
```

Type: [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string)

Defined in plugin_audit.h:165

---

#### table

```cpp
MYSQL_CONST_LEX_STRING table
```

Type: [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string)

Defined in plugin_audit.h:166

---

#### new_database

```cpp
MYSQL_CONST_LEX_STRING new_database
```

Type: [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string)

Defined in plugin_audit.h:168

---

#### new_table

```cpp
MYSQL_CONST_LEX_STRING new_table
```

Type: [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string)

Defined in plugin_audit.h:169

---

#### read_only

```cpp
int read_only
```

Defined in plugin_audit.h:171

---

#### query_id

```cpp
unsigned long long query_id
```

Defined in plugin_audit.h:173

