---
description: >-
  Plugin API reference: My Print Error Service. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# My Print Error Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

This service provides functions for plugins to report errors to client (without client, the errors are written to the error log).

## Classes

| Name                                                                                          | Description |
| --------------------------------------------------------------------------------------------- | ----------- |
| [`my_print_error_service_st`](plugin_api_service_my_print_error.md#my_print_error_service_st) |             |

## Macros

| Name                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [`ME_ERROR_LOG`](plugin_api_service_my_print_error.md#me_error_log)           |             |
| [`ME_ERROR_LOG_ONLY`](plugin_api_service_my_print_error.md#me_error_log_only) |             |
| [`ME_NOTE`](plugin_api_service_my_print_error.md#me_note)                     |             |
| [`ME_WARNING`](plugin_api_service_my_print_error.md#me_warning)               |             |
| [`ME_FATAL`](plugin_api_service_my_print_error.md#me_fatal)                   |             |
| [`my_error`](plugin_api_service_my_print_error.md#my_error)                   |             |
| [`my_printf_error`](plugin_api_service_my_print_error.md#my_printf_error)     |             |
| [`my_printv_error`](plugin_api_service_my_print_error.md#my_printv_error)     |             |

***

### ME\_ERROR\_LOG

```cpp
#define ME_ERROR_LOG 64 /* Write the message to the error log */
```

Defined in service\_my\_print\_error.h:43

***

### ME\_ERROR\_LOG\_ONLY

```cpp
#define ME_ERROR_LOG_ONLY 128 /* Write the error message to error log only */
```

Defined in service\_my\_print\_error.h:44

***

### ME\_NOTE

```cpp
#define ME_NOTE 1024 /* Not an error, just a note */
```

Defined in service\_my\_print\_error.h:45

***

### ME\_WARNING

```cpp
#define ME_WARNING 2048 /* Not an error, just a warning */
```

Defined in service\_my\_print\_error.h:46

***

### ME\_FATAL

```cpp
#define ME_FATAL 4096 /* Fatal statement error */
```

Defined in service\_my\_print\_error.h:47

***

### my\_error

```cpp
#define my_error my_print_error_service->my_error_func
```

Defined in service\_my\_print\_error.h:61

***

### my\_printf\_error

```cpp
#define my_printf_error my_print_error_service->my_printf_error_func
```

Defined in service\_my\_print\_error.h:62

***

### my\_printv\_error

```cpp
#define my_printv_error(A, B, C, D, A, B, C, D) my_print_error_service->my_printv_error_func(A,B,C,D)
```

Defined in service\_my\_print\_error.h:63

## Variables

| Return                                                                                                  | Name                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------- |
| struct [`my_print_error_service_st`](plugin_api_service_my_print_error.md#my_print_error_service_st) \* | [`my_print_error_service`](plugin_api_service_my_print_error.md#my_print_error_service) |             |

***

### my\_print\_error\_service

```cpp
struct my_print_error_service_st * my_print_error_service
```

Type: struct [`my_print_error_service_st`](plugin_api_service_my_print_error.md#my_print_error_service_st) \*

Defined in service\_my\_print\_error.h:57

## Class Definitions

### my\_print\_error\_service\_st

```cpp
#include <service_my_print_error.h>
```

```cpp
struct my_print_error_service_st
```

Defined in service\_my\_print\_error.h:49

#### Public Attributes

| Return           | Name                                                                                | Description |
| ---------------- | ----------------------------------------------------------------------------------- | ----------- |
| `void(*`         | [`my_error_func`](plugin_api_service_my_print_error.md#my_error_func)               |             |
| `void(*`         | [`my_printf_error_func`](plugin_api_service_my_print_error.md#my_printf_error_func) |             |
| `void(*) void(*` | [`my_printv_error_func`](plugin_api_service_my_print_error.md#my_printv_error_func) |             |

***

#### my\_error\_func

```cpp
void(* my_error_func)(unsigned int nr, unsigned long MyFlags,...)
```

Defined in service\_my\_print\_error.h:50

***

#### my\_printf\_error\_func

```cpp
void(* my_printf_error_func)(unsigned int nr, const char *fmt, unsigned long MyFlags,...) ATTRIBUTE_FORMAT_FPTR(printf
```

Defined in service\_my\_print\_error.h:51

***

#### my\_printv\_error\_func

```cpp
void(*) void(* my_printv_error_func)(unsigned int error, const char *format, unsigned long MyFlags, va_list ap) ATTRIBUTE_FORMAT_FPTR(printf
```

Defined in service\_my\_print\_error.h:54
