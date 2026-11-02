---
description: >-
  Plugin API reference: THD Error Context Service. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# THD Error Context Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

Error context service to access the statement diagnostics area.

This service provides access to the statement diagnostics area:

* error message
* error number
* row for warning (e.g. for multi-row INSERT statements)

## Classes

| Name                                                                                                   | Description |
| ------------------------------------------------------------------------------------------------------ | ----------- |
| [`thd_error_context_service_st`](plugin_api_service_thd_error_context.md#thd_error_context_service_st) |             |

## Macros

| Name                                                                                                             | Description                                                                                    |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [`thd_get_error_message`](plugin_api_service_thd_error_context.md#thd_get_error_message)                         | Return error message                                                                           |
| [`thd_get_error_number`](plugin_api_service_thd_error_context.md#thd_get_error_number)                           | Return error number                                                                            |
| [`thd_get_error_row`](plugin_api_service_thd_error_context.md#thd_get_error_row)                                 | Return the current row number (i.e. in a multiple INSERT statement)                            |
| [`thd_inc_error_row`](plugin_api_service_thd_error_context.md#thd_inc_error_row)                                 | Increment the current row number                                                               |
| [`thd_get_error_context_description`](plugin_api_service_thd_error_context.md#thd_get_error_context_description) | Return a text description of a thread, its security context (user,host) and the current query. |

***

### thd\_get\_error\_message

```cpp
#define thd_get_error_message(thd, thd) (thd_error_context_service->thd_get_error_message_func((thd)))
```

Defined in service\_thd\_error\_context.h:59

Return error message

#### Returns

error text

#### Parameters

| Parameter | Type | Description                   |
| --------- | ---- | ----------------------------- |
| `thd`     |      | user thread connection handle |
| `thd`     |      | user thread connection handle |

***

### thd\_get\_error\_number

```cpp
#define thd_get_error_number(thd, thd) (thd_error_context_service->thd_get_error_number_func((thd)))
```

Defined in service\_thd\_error\_context.h:66

Return error number

#### Returns

error number

#### Parameters

| Parameter | Type | Description                   |
| --------- | ---- | ----------------------------- |
| `thd`     |      | user thread connection handle |
| `thd`     |      | user thread connection handle |

***

### thd\_get\_error\_row

```cpp
#define thd_get_error_row(thd, thd) (thd_error_context_service->thd_get_error_row_func((thd)))
```

Defined in service\_thd\_error\_context.h:73

Return the current row number (i.e. in a multiple INSERT statement)

#### Returns

row number

#### Parameters

| Parameter | Type | Description                   |
| --------- | ---- | ----------------------------- |
| `thd`     |      | user thread connection handle |
| `thd`     |      | user thread connection handle |

***

### thd\_inc\_error\_row

```cpp
#define thd_inc_error_row(thd, thd) (thd_error_context_service->thd_inc_error_row_func((thd)))
```

Defined in service\_thd\_error\_context.h:79

Increment the current row number

#### Parameters

| Parameter | Type | Description                   |
| --------- | ---- | ----------------------------- |
| `thd`     |      | user thread connection handle |
| `thd`     |      | user thread connection handle |

***

### thd\_get\_error\_context\_description

```cpp
#define thd_get_error_context_description(thd, buffer, length, max_query_length, thd, buffer, length, max_query_length) (thd_error_context_service->thd_get_error_context_description_func((thd), \
                                                                (buffer), \
                                                                (length), \
                                                                (max_query_length)))
```

Defined in service\_thd\_error\_context.h:85

Return a text description of a thread, its security context (user,host) and the current query.

## Variables

| Return                                                                                                           | Name                                                                                             | Description |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------- |
| struct [`thd_error_context_service_st`](plugin_api_service_thd_error_context.md#thd_error_context_service_st) \* | [`thd_error_context_service`](plugin_api_service_thd_error_context.md#thd_error_context_service) |             |

***

### thd\_error\_context\_service

```cpp
struct thd_error_context_service_st * thd_error_context_service
```

Type: struct [`thd_error_context_service_st`](plugin_api_service_thd_error_context.md#thd_error_context_service_st) \*

Defined in service\_thd\_error\_context.h:51

## Class Definitions

### thd\_error\_context\_service\_st

```cpp
#include <service_thd_error_context.h>
```

```cpp
struct thd_error_context_service_st
```

Defined in service\_thd\_error\_context.h:42

#### Public Attributes

| Return            | Name                                                                                                                       | Description |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `const char *(*`  | [`thd_get_error_message_func`](plugin_api_service_thd_error_context.md#thd_get_error_message_func)                         |             |
| `unsigned int(*`  | [`thd_get_error_number_func`](plugin_api_service_thd_error_context.md#thd_get_error_number_func)                           |             |
| `unsigned long(*` | [`thd_get_error_row_func`](plugin_api_service_thd_error_context.md#thd_get_error_row_func)                                 |             |
| `void(*`          | [`thd_inc_error_row_func`](plugin_api_service_thd_error_context.md#thd_inc_error_row_func)                                 |             |
| `char *(*`        | [`thd_get_error_context_description_func`](plugin_api_service_thd_error_context.md#thd_get_error_context_description_func) |             |

***

#### thd\_get\_error\_message\_func

```cpp
const char *(* thd_get_error_message_func)(const MYSQL_THD thd)
```

Defined in service\_thd\_error\_context.h:43

***

#### thd\_get\_error\_number\_func

```cpp
unsigned int(* thd_get_error_number_func)(const MYSQL_THD thd)
```

Defined in service\_thd\_error\_context.h:44

***

#### thd\_get\_error\_row\_func

```cpp
unsigned long(* thd_get_error_row_func)(const MYSQL_THD thd)
```

Defined in service\_thd\_error\_context.h:45

***

#### thd\_inc\_error\_row\_func

```cpp
void(* thd_inc_error_row_func)(MYSQL_THD thd)
```

Defined in service\_thd\_error\_context.h:46

***

#### thd\_get\_error\_context\_description\_func

```cpp
char *(* thd_get_error_context_description_func)(MYSQL_THD thd, char *buffer, unsigned int length, unsigned int max_query_length)
```

Defined in service\_thd\_error\_context.h:47
