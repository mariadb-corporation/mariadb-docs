---
description: >-
  Plugin API reference: THD Error Context Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# THD Error Context Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Error context service to access the statement diagnostics area.

This service provides access to the statement diagnostics area:

* error message
* error number
* row for warning (e.g. for multi-row INSERT statements)

## Classes

| Name | Description |
|------|-------------|
| [`thd_error_context_service_st`](#thd_error_context_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_get_error_message`](#thd_get_error_message)  | Return error message |
| [`thd_get_error_number`](#thd_get_error_number)  | Return error number |
| [`thd_get_error_row`](#thd_get_error_row)  | Return the current row number (i.e. in a multiple INSERT statement) |
| [`thd_inc_error_row`](#thd_inc_error_row)  | Increment the current row number |
| [`thd_get_error_context_description`](#thd_get_error_context_description)  | Return a text description of a thread, its security context (user,host) and the current query. |

---

### thd_get_error_message

```cpp
#define thd_get_error_message(thd, thd) (thd_error_context_service->thd_get_error_message_func((thd)))
```

Defined in service_thd_error_context.h:59

Return error message 
#### Returns
error text

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `thd` |  | user thread connection handle |

---

### thd_get_error_number

```cpp
#define thd_get_error_number(thd, thd) (thd_error_context_service->thd_get_error_number_func((thd)))
```

Defined in service_thd_error_context.h:66

Return error number 
#### Returns
error number

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `thd` |  | user thread connection handle |

---

### thd_get_error_row

```cpp
#define thd_get_error_row(thd, thd) (thd_error_context_service->thd_get_error_row_func((thd)))
```

Defined in service_thd_error_context.h:73

Return the current row number (i.e. in a multiple INSERT statement) 
#### Returns
row number

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `thd` |  | user thread connection handle |

---

### thd_inc_error_row

```cpp
#define thd_inc_error_row(thd, thd) (thd_error_context_service->thd_inc_error_row_func((thd)))
```

Defined in service_thd_error_context.h:79

Increment the current row number

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `thd` |  | user thread connection handle |

---

### thd_get_error_context_description

```cpp
#define thd_get_error_context_description(thd, buffer, length, max_query_length, thd, buffer, length, max_query_length) (thd_error_context_service->thd_get_error_context_description_func((thd), \
                                                                (buffer), \
                                                                (length), \
                                                                (max_query_length)))
```

Defined in service_thd_error_context.h:85

Return a text description of a thread, its security context (user,host) and the current query.

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_error_context_service_st`](#thd_error_context_service_st) * | [`thd_error_context_service`](#thd_error_context_service)  |  |

---

### thd_error_context_service

```cpp
struct thd_error_context_service_st * thd_error_context_service
```

Type: struct [`thd_error_context_service_st`](#thd_error_context_service_st) *

Defined in service_thd_error_context.h:51


## Class Definitions



### thd_error_context_service_st

```cpp
#include <service_thd_error_context.h>
```

```cpp
struct thd_error_context_service_st
```

Defined in service_thd_error_context.h:42

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const char *(*` | [`thd_get_error_message_func`](#thd_get_error_message_func)  |  |
| `unsigned int(*` | [`thd_get_error_number_func`](#thd_get_error_number_func)  |  |
| `unsigned long(*` | [`thd_get_error_row_func`](#thd_get_error_row_func)  |  |
| `void(*` | [`thd_inc_error_row_func`](#thd_inc_error_row_func)  |  |
| `char *(*` | [`thd_get_error_context_description_func`](#thd_get_error_context_description_func)  |  |

---

#### thd_get_error_message_func

```cpp
const char *(* thd_get_error_message_func)(const MYSQL_THD thd)
```

Defined in service_thd_error_context.h:43

---

#### thd_get_error_number_func

```cpp
unsigned int(* thd_get_error_number_func)(const MYSQL_THD thd)
```

Defined in service_thd_error_context.h:44

---

#### thd_get_error_row_func

```cpp
unsigned long(* thd_get_error_row_func)(const MYSQL_THD thd)
```

Defined in service_thd_error_context.h:45

---

#### thd_inc_error_row_func

```cpp
void(* thd_inc_error_row_func)(MYSQL_THD thd)
```

Defined in service_thd_error_context.h:46

---

#### thd_get_error_context_description_func

```cpp
char *(* thd_get_error_context_description_func)(MYSQL_THD thd, char *buffer, unsigned int length, unsigned int max_query_length)
```

Defined in service_thd_error_context.h:47

