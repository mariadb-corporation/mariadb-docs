---
description: >-
  Plugin API reference: Audit Class: General. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# Audit Class: General

> [`Plugin API`](../../) / [`Plugin Types`](../) / [`Audit Plugin`](./)

LOG events occurs before emitting to the general query log. ERROR events occur before transmitting errors to the user. RESULT events occur after transmitting a resultset to the user. STATUS events occur after transmitting a resultset or errors to the user.

## Classes

| Name                                                                | Description |
| ------------------------------------------------------------------- | ----------- |
| [`mysql_event_general`](audit_general_class.md#mysql_event_general) |             |

## Macros

| Name                                                                                    | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [`MYSQL_AUDIT_GENERAL_CLASS`](audit_general_class.md#mysql_audit_general_class)         |             |
| [`MYSQL_AUDIT_GENERAL_CLASSMASK`](audit_general_class.md#mysql_audit_general_classmask) |             |
| [`MYSQL_AUDIT_GENERAL_LOG`](audit_general_class.md#mysql_audit_general_log)             |             |
| [`MYSQL_AUDIT_GENERAL_ERROR`](audit_general_class.md#mysql_audit_general_error)         |             |
| [`MYSQL_AUDIT_GENERAL_RESULT`](audit_general_class.md#mysql_audit_general_result)       |             |
| [`MYSQL_AUDIT_GENERAL_STATUS`](audit_general_class.md#mysql_audit_general_status)       |             |
| [`MYSQL_AUDIT_GENERAL_WARNING`](audit_general_class.md#mysql_audit_general_warning)     |             |

***

### MYSQL\_AUDIT\_GENERAL\_CLASS

```cpp
#define MYSQL_AUDIT_GENERAL_CLASS 0
```

Defined in plugin\_audit.h:50

***

### MYSQL\_AUDIT\_GENERAL\_CLASSMASK

```cpp
#define MYSQL_AUDIT_GENERAL_CLASSMASK (1 << MYSQL_AUDIT_GENERAL_CLASS)
```

Defined in plugin\_audit.h:51

***

### MYSQL\_AUDIT\_GENERAL\_LOG

```cpp
#define MYSQL_AUDIT_GENERAL_LOG 0
```

Defined in plugin\_audit.h:52

***

### MYSQL\_AUDIT\_GENERAL\_ERROR

```cpp
#define MYSQL_AUDIT_GENERAL_ERROR 1
```

Defined in plugin\_audit.h:53

***

### MYSQL\_AUDIT\_GENERAL\_RESULT

```cpp
#define MYSQL_AUDIT_GENERAL_RESULT 2
```

Defined in plugin\_audit.h:54

***

### MYSQL\_AUDIT\_GENERAL\_STATUS

```cpp
#define MYSQL_AUDIT_GENERAL_STATUS 3
```

Defined in plugin\_audit.h:55

***

### MYSQL\_AUDIT\_GENERAL\_WARNING

```cpp
#define MYSQL_AUDIT_GENERAL_WARNING 4
```

Defined in plugin\_audit.h:56

## Class Definitions

### mysql\_event\_general

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_general
```

Defined in plugin\_audit.h:58

#### Public Attributes

| Return                                                                                                                                       | Name                                                                            | Description |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------- |
| `unsigned int`                                                                                                                               | [`event_subclass`](audit_general_class.md#event_subclass)                       |             |
| `int`                                                                                                                                        | [`general_error_code`](audit_general_class.md#general_error_code)               |             |
| `unsigned long`                                                                                                                              | [`general_thread_id`](audit_general_class.md#general_thread_id)                 |             |
| `const char *`                                                                                                                               | [`general_user`](audit_general_class.md#general_user)                           |             |
| `unsigned int`                                                                                                                               | [`general_user_length`](audit_general_class.md#general_user_length)             |             |
| `const char *`                                                                                                                               | [`general_command`](audit_general_class.md#general_command)                     |             |
| `unsigned int`                                                                                                                               | [`general_command_length`](audit_general_class.md#general_command_length)       |             |
| `const char *`                                                                                                                               | [`general_query`](audit_general_class.md#general_query)                         |             |
| `unsigned int`                                                                                                                               | [`general_query_length`](audit_general_class.md#general_query_length)           |             |
| `const struct charset_info_st *`                                                                                                             | [`general_charset`](audit_general_class.md#general_charset)                     |             |
| `unsigned long long`                                                                                                                         | [`general_time`](audit_general_class.md#general_time)                           |             |
| `unsigned long long`                                                                                                                         | [`general_rows`](audit_general_class.md#general_rows)                           |             |
| `unsigned long long`                                                                                                                         | [`query_id`](audit_general_class.md#query_id)                                   |             |
| `unsigned int`                                                                                                                               | [`port`](audit_general_class.md#port)                                           |             |
| [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string) | [`database`](audit_general_class.md#database)                                   |             |
| `unsigned long long`                                                                                                                         | [`general_time_microseconds`](audit_general_class.md#general_time_microseconds) |             |

***

#### event\_subclass

```cpp
unsigned int event_subclass
```

Defined in plugin\_audit.h:60

***

#### general\_error\_code

```cpp
int general_error_code
```

Defined in plugin\_audit.h:61

***

#### general\_thread\_id

```cpp
unsigned long general_thread_id
```

Defined in plugin\_audit.h:62

***

#### general\_user

```cpp
const char * general_user
```

Defined in plugin\_audit.h:63

***

#### general\_user\_length

```cpp
unsigned int general_user_length
```

Defined in plugin\_audit.h:64

***

#### general\_command

```cpp
const char * general_command
```

Defined in plugin\_audit.h:65

***

#### general\_command\_length

```cpp
unsigned int general_command_length
```

Defined in plugin\_audit.h:66

***

#### general\_query

```cpp
const char * general_query
```

Defined in plugin\_audit.h:67

***

#### general\_query\_length

```cpp
unsigned int general_query_length
```

Defined in plugin\_audit.h:68

***

#### general\_charset

```cpp
const struct charset_info_st * general_charset
```

Defined in plugin\_audit.h:69

***

#### general\_time

```cpp
unsigned long long general_time
```

Defined in plugin\_audit.h:70

***

#### general\_rows

```cpp
unsigned long long general_rows
```

Defined in plugin\_audit.h:71

***

#### query\_id

```cpp
unsigned long long query_id
```

Defined in plugin\_audit.h:73

***

#### port

```cpp
unsigned int port
```

Defined in plugin\_audit.h:75

***

#### database

```cpp
MYSQL_CONST_LEX_STRING database
```

Type: [`MYSQL_CONST_LEX_STRING`](../../plugin_api_services_for_plugins/plugin_api_services/plugin_api_service_thd_alloc.md#mysql_const_lex_string)

Defined in plugin\_audit.h:76

***

#### general\_time\_microseconds

```cpp
unsigned long long general_time_microseconds
```

Defined in plugin\_audit.h:84
