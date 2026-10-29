---
description: >-
  Plugin API reference: Audit Class: General. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Audit Class: General

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md) / [`Audit Plugin`](audit_plugin_data.md)

LOG events occurs before emitting to the general query log. ERROR events occur before transmitting errors to the user. RESULT events occur after transmitting a resultset to the user. STATUS events occur after transmitting a resultset or errors to the user.

## Classes

| Name | Description |
|------|-------------|
| [`mysql_event_general`](#mysql_event_general) |  |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_AUDIT_GENERAL_CLASS`](#mysql_audit_general_class)  |  |
| [`MYSQL_AUDIT_GENERAL_CLASSMASK`](#mysql_audit_general_classmask)  |  |
| [`MYSQL_AUDIT_GENERAL_LOG`](#mysql_audit_general_log)  |  |
| [`MYSQL_AUDIT_GENERAL_ERROR`](#mysql_audit_general_error)  |  |
| [`MYSQL_AUDIT_GENERAL_RESULT`](#mysql_audit_general_result)  |  |
| [`MYSQL_AUDIT_GENERAL_STATUS`](#mysql_audit_general_status)  |  |
| [`MYSQL_AUDIT_GENERAL_WARNING`](#mysql_audit_general_warning)  |  |

---

### MYSQL_AUDIT_GENERAL_CLASS

```cpp
#define MYSQL_AUDIT_GENERAL_CLASS 0
```

Defined in plugin_audit.h:50

---

### MYSQL_AUDIT_GENERAL_CLASSMASK

```cpp
#define MYSQL_AUDIT_GENERAL_CLASSMASK (1 << MYSQL_AUDIT_GENERAL_CLASS)
```

Defined in plugin_audit.h:51

---

### MYSQL_AUDIT_GENERAL_LOG

```cpp
#define MYSQL_AUDIT_GENERAL_LOG 0
```

Defined in plugin_audit.h:52

---

### MYSQL_AUDIT_GENERAL_ERROR

```cpp
#define MYSQL_AUDIT_GENERAL_ERROR 1
```

Defined in plugin_audit.h:53

---

### MYSQL_AUDIT_GENERAL_RESULT

```cpp
#define MYSQL_AUDIT_GENERAL_RESULT 2
```

Defined in plugin_audit.h:54

---

### MYSQL_AUDIT_GENERAL_STATUS

```cpp
#define MYSQL_AUDIT_GENERAL_STATUS 3
```

Defined in plugin_audit.h:55

---

### MYSQL_AUDIT_GENERAL_WARNING

```cpp
#define MYSQL_AUDIT_GENERAL_WARNING 4
```

Defined in plugin_audit.h:56


## Class Definitions



### mysql_event_general

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_general
```

Defined in plugin_audit.h:58

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned int` | [`event_subclass`](#event_subclass)  |  |
| `int` | [`general_error_code`](#general_error_code)  |  |
| `unsigned long` | [`general_thread_id`](#general_thread_id)  |  |
| `const char *` | [`general_user`](#general_user)  |  |
| `unsigned int` | [`general_user_length`](#general_user_length)  |  |
| `const char *` | [`general_command`](#general_command)  |  |
| `unsigned int` | [`general_command_length`](#general_command_length)  |  |
| `const char *` | [`general_query`](#general_query)  |  |
| `unsigned int` | [`general_query_length`](#general_query_length)  |  |
| `const struct charset_info_st *` | [`general_charset`](#general_charset)  |  |
| `unsigned long long` | [`general_time`](#general_time)  |  |
| `unsigned long long` | [`general_rows`](#general_rows)  |  |
| `unsigned long long` | [`query_id`](#query_id)  |  |
| `unsigned int` | [`port`](#port)  |  |
| [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string) | [`database`](#database)  |  |
| `unsigned long long` | [`general_time_microseconds`](#general_time_microseconds)  |  |

---

#### event_subclass

```cpp
unsigned int event_subclass
```

Defined in plugin_audit.h:60

---

#### general_error_code

```cpp
int general_error_code
```

Defined in plugin_audit.h:61

---

#### general_thread_id

```cpp
unsigned long general_thread_id
```

Defined in plugin_audit.h:62

---

#### general_user

```cpp
const char * general_user
```

Defined in plugin_audit.h:63

---

#### general_user_length

```cpp
unsigned int general_user_length
```

Defined in plugin_audit.h:64

---

#### general_command

```cpp
const char * general_command
```

Defined in plugin_audit.h:65

---

#### general_command_length

```cpp
unsigned int general_command_length
```

Defined in plugin_audit.h:66

---

#### general_query

```cpp
const char * general_query
```

Defined in plugin_audit.h:67

---

#### general_query_length

```cpp
unsigned int general_query_length
```

Defined in plugin_audit.h:68

---

#### general_charset

```cpp
const struct charset_info_st * general_charset
```

Defined in plugin_audit.h:69

---

#### general_time

```cpp
unsigned long long general_time
```

Defined in plugin_audit.h:70

---

#### general_rows

```cpp
unsigned long long general_rows
```

Defined in plugin_audit.h:71

---

#### query_id

```cpp
unsigned long long query_id
```

Defined in plugin_audit.h:73

---

#### port

```cpp
unsigned int port
```

Defined in plugin_audit.h:75

---

#### database

```cpp
MYSQL_CONST_LEX_STRING database
```

Type: [`MYSQL_CONST_LEX_STRING`](api.md#mysql_const_lex_string)

Defined in plugin_audit.h:76

---

#### general_time_microseconds

```cpp
unsigned long long general_time_microseconds
```

Defined in plugin_audit.h:84

