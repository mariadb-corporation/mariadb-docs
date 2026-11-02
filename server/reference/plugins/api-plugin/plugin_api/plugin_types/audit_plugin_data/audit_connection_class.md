---
description: >-
  Plugin API reference: Audit Class: Connection. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# Audit Class: Connection

> [`Plugin API`](../../) / [`Plugin Types`](../) / [`Audit Plugin`](./)

CONNECT occurs after authentication phase is completed. DISCONNECT occurs after connection is terminated. CHANGE\_USER occurs after COM\_CHANGE\_USER RPC is completed.

## Classes

| Name                                                                         | Description |
| ---------------------------------------------------------------------------- | ----------- |
| [`mysql_event_connection`](audit_connection_class.md#mysql_event_connection) |             |

## Macros

| Name                                                                                                 | Description |
| ---------------------------------------------------------------------------------------------------- | ----------- |
| [`MYSQL_AUDIT_CONNECTION_CLASS`](audit_connection_class.md#mysql_audit_connection_class)             |             |
| [`MYSQL_AUDIT_CONNECTION_CLASSMASK`](audit_connection_class.md#mysql_audit_connection_classmask)     |             |
| [`MYSQL_AUDIT_CONNECTION_CONNECT`](audit_connection_class.md#mysql_audit_connection_connect)         |             |
| [`MYSQL_AUDIT_CONNECTION_DISCONNECT`](audit_connection_class.md#mysql_audit_connection_disconnect)   |             |
| [`MYSQL_AUDIT_CONNECTION_CHANGE_USER`](audit_connection_class.md#mysql_audit_connection_change_user) |             |

***

### MYSQL\_AUDIT\_CONNECTION\_CLASS

```cpp
#define MYSQL_AUDIT_CONNECTION_CLASS 1
```

Defined in plugin\_audit.h:98

***

### MYSQL\_AUDIT\_CONNECTION\_CLASSMASK

```cpp
#define MYSQL_AUDIT_CONNECTION_CLASSMASK (1 << MYSQL_AUDIT_CONNECTION_CLASS)
```

Defined in plugin\_audit.h:99

***

### MYSQL\_AUDIT\_CONNECTION\_CONNECT

```cpp
#define MYSQL_AUDIT_CONNECTION_CONNECT 0
```

Defined in plugin\_audit.h:100

***

### MYSQL\_AUDIT\_CONNECTION\_DISCONNECT

```cpp
#define MYSQL_AUDIT_CONNECTION_DISCONNECT 1
```

Defined in plugin\_audit.h:101

***

### MYSQL\_AUDIT\_CONNECTION\_CHANGE\_USER

```cpp
#define MYSQL_AUDIT_CONNECTION_CHANGE_USER 2
```

Defined in plugin\_audit.h:102

## Class Definitions

### mysql\_event\_connection

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_connection
```

Defined in plugin\_audit.h:104

#### Public Attributes

| Return                                                                                                                                       | Name                                                                     | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------- |
| `unsigned int`                                                                                                                               | [`event_subclass`](audit_connection_class.md#event_subclass)             |             |
| `int`                                                                                                                                        | [`status`](audit_connection_class.md#status)                             |             |
| `unsigned long`                                                                                                                              | [`thread_id`](audit_connection_class.md#thread_id)                       |             |
| `const char *`                                                                                                                               | [`user`](audit_connection_class.md#user)                                 |             |
| `unsigned int`                                                                                                                               | [`user_length`](audit_connection_class.md#user_length)                   |             |
| `const char *`                                                                                                                               | [`priv_user`](audit_connection_class.md#priv_user)                       |             |
| `unsigned int`                                                                                                                               | [`priv_user_length`](audit_connection_class.md#priv_user_length)         |             |
| `const char *`                                                                                                                               | [`external_user`](audit_connection_class.md#external_user)               |             |
| `unsigned int`                                                                                                                               | [`external_user_length`](audit_connection_class.md#external_user_length) |             |
| `const char *`                                                                                                                               | [`proxy_user`](audit_connection_class.md#proxy_user)                     |             |
| `unsigned int`                                                                                                                               | [`proxy_user_length`](audit_connection_class.md#proxy_user_length)       |             |
| `const char *`                                                                                                                               | [`host`](audit_connection_class.md#host)                                 |             |
| `unsigned int`                                                                                                                               | [`host_length`](audit_connection_class.md#host_length)                   |             |
| `const char *`                                                                                                                               | [`ip`](audit_connection_class.md#ip)                                     |             |
| `unsigned int`                                                                                                                               | [`ip_length`](audit_connection_class.md#ip_length)                       |             |
| `unsigned int`                                                                                                                               | [`port`](audit_connection_class.md#port)                                 |             |
| [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string) | [`database`](audit_connection_class.md#database)                         |             |
| `const char *`                                                                                                                               | [`tls_version`](audit_connection_class.md#tls_version)                   |             |
| `unsigned int`                                                                                                                               | [`tls_version_length`](audit_connection_class.md#tls_version_length)     |             |

***

#### event\_subclass

```cpp
unsigned int event_subclass
```

Defined in plugin\_audit.h:106

***

#### status

```cpp
int status
```

Defined in plugin\_audit.h:107

***

#### thread\_id

```cpp
unsigned long thread_id
```

Defined in plugin\_audit.h:108

***

#### user

```cpp
const char * user
```

Defined in plugin\_audit.h:109

***

#### user\_length

```cpp
unsigned int user_length
```

Defined in plugin\_audit.h:110

***

#### priv\_user

```cpp
const char * priv_user
```

Defined in plugin\_audit.h:111

***

#### priv\_user\_length

```cpp
unsigned int priv_user_length
```

Defined in plugin\_audit.h:112

***

#### external\_user

```cpp
const char * external_user
```

Defined in plugin\_audit.h:113

***

#### external\_user\_length

```cpp
unsigned int external_user_length
```

Defined in plugin\_audit.h:114

***

#### proxy\_user

```cpp
const char * proxy_user
```

Defined in plugin\_audit.h:115

***

#### proxy\_user\_length

```cpp
unsigned int proxy_user_length
```

Defined in plugin\_audit.h:116

***

#### host

```cpp
const char * host
```

Defined in plugin\_audit.h:117

***

#### host\_length

```cpp
unsigned int host_length
```

Defined in plugin\_audit.h:118

***

#### ip

```cpp
const char * ip
```

Defined in plugin\_audit.h:119

***

#### ip\_length

```cpp
unsigned int ip_length
```

Defined in plugin\_audit.h:120

***

#### port

```cpp
unsigned int port
```

Defined in plugin\_audit.h:121

***

#### database

```cpp
MYSQL_CONST_LEX_STRING database
```

Type: [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string)

Defined in plugin\_audit.h:122

***

#### tls\_version

```cpp
const char * tls_version
```

Defined in plugin\_audit.h:124

***

#### tls\_version\_length

```cpp
unsigned int tls_version_length
```

Defined in plugin\_audit.h:125
