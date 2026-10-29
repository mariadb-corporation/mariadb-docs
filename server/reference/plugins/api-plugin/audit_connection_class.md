---
description: >-
  Plugin API reference: Audit Class: Connection. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Audit Class: Connection

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md) / [`Audit Plugin`](audit_plugin_data.md)

CONNECT occurs after authentication phase is completed. DISCONNECT occurs after connection is terminated. CHANGE_USER occurs after COM_CHANGE_USER RPC is completed.

## Classes

| Name | Description |
|------|-------------|
| [`mysql_event_connection`](#mysql_event_connection) |  |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_AUDIT_CONNECTION_CLASS`](#mysql_audit_connection_class)  |  |
| [`MYSQL_AUDIT_CONNECTION_CLASSMASK`](#mysql_audit_connection_classmask)  |  |
| [`MYSQL_AUDIT_CONNECTION_CONNECT`](#mysql_audit_connection_connect)  |  |
| [`MYSQL_AUDIT_CONNECTION_DISCONNECT`](#mysql_audit_connection_disconnect)  |  |
| [`MYSQL_AUDIT_CONNECTION_CHANGE_USER`](#mysql_audit_connection_change_user)  |  |

---

### MYSQL_AUDIT_CONNECTION_CLASS

```cpp
#define MYSQL_AUDIT_CONNECTION_CLASS 1
```

Defined in plugin_audit.h:98

---

### MYSQL_AUDIT_CONNECTION_CLASSMASK

```cpp
#define MYSQL_AUDIT_CONNECTION_CLASSMASK (1 << MYSQL_AUDIT_CONNECTION_CLASS)
```

Defined in plugin_audit.h:99

---

### MYSQL_AUDIT_CONNECTION_CONNECT

```cpp
#define MYSQL_AUDIT_CONNECTION_CONNECT 0
```

Defined in plugin_audit.h:100

---

### MYSQL_AUDIT_CONNECTION_DISCONNECT

```cpp
#define MYSQL_AUDIT_CONNECTION_DISCONNECT 1
```

Defined in plugin_audit.h:101

---

### MYSQL_AUDIT_CONNECTION_CHANGE_USER

```cpp
#define MYSQL_AUDIT_CONNECTION_CHANGE_USER 2
```

Defined in plugin_audit.h:102


## Class Definitions



### mysql_event_connection

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_connection
```

Defined in plugin_audit.h:104

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned int` | [`event_subclass`](#event_subclass)  |  |
| `int` | [`status`](#status)  |  |
| `unsigned long` | [`thread_id`](#thread_id)  |  |
| `const char *` | [`user`](#user)  |  |
| `unsigned int` | [`user_length`](#user_length)  |  |
| `const char *` | [`priv_user`](#priv_user)  |  |
| `unsigned int` | [`priv_user_length`](#priv_user_length)  |  |
| `const char *` | [`external_user`](#external_user)  |  |
| `unsigned int` | [`external_user_length`](#external_user_length)  |  |
| `const char *` | [`proxy_user`](#proxy_user)  |  |
| `unsigned int` | [`proxy_user_length`](#proxy_user_length)  |  |
| `const char *` | [`host`](#host)  |  |
| `unsigned int` | [`host_length`](#host_length)  |  |
| `const char *` | [`ip`](#ip)  |  |
| `unsigned int` | [`ip_length`](#ip_length)  |  |
| `unsigned int` | [`port`](#port)  |  |
| [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string) | [`database`](#database)  |  |
| `const char *` | [`tls_version`](#tls_version)  |  |
| `unsigned int` | [`tls_version_length`](#tls_version_length)  |  |

---

#### event_subclass

```cpp
unsigned int event_subclass
```

Defined in plugin_audit.h:106

---

#### status

```cpp
int status
```

Defined in plugin_audit.h:107

---

#### thread_id

```cpp
unsigned long thread_id
```

Defined in plugin_audit.h:108

---

#### user

```cpp
const char * user
```

Defined in plugin_audit.h:109

---

#### user_length

```cpp
unsigned int user_length
```

Defined in plugin_audit.h:110

---

#### priv_user

```cpp
const char * priv_user
```

Defined in plugin_audit.h:111

---

#### priv_user_length

```cpp
unsigned int priv_user_length
```

Defined in plugin_audit.h:112

---

#### external_user

```cpp
const char * external_user
```

Defined in plugin_audit.h:113

---

#### external_user_length

```cpp
unsigned int external_user_length
```

Defined in plugin_audit.h:114

---

#### proxy_user

```cpp
const char * proxy_user
```

Defined in plugin_audit.h:115

---

#### proxy_user_length

```cpp
unsigned int proxy_user_length
```

Defined in plugin_audit.h:116

---

#### host

```cpp
const char * host
```

Defined in plugin_audit.h:117

---

#### host_length

```cpp
unsigned int host_length
```

Defined in plugin_audit.h:118

---

#### ip

```cpp
const char * ip
```

Defined in plugin_audit.h:119

---

#### ip_length

```cpp
unsigned int ip_length
```

Defined in plugin_audit.h:120

---

#### port

```cpp
unsigned int port
```

Defined in plugin_audit.h:121

---

#### database

```cpp
MYSQL_CONST_LEX_STRING database
```

Type: [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string)

Defined in plugin_audit.h:122

---

#### tls_version

```cpp
const char * tls_version
```

Defined in plugin_audit.h:124

---

#### tls_version_length

```cpp
unsigned int tls_version_length
```

Defined in plugin_audit.h:125

