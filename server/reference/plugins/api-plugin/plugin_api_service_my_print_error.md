---
description: >-
  Plugin API reference: My Print Error Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# My Print Error Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

This service provides functions for plugins to report errors to client (without client, the errors are written to the error log).

## Classes

| Name | Description |
|------|-------------|
| [`my_print_error_service_st`](#my_print_error_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`ME_ERROR_LOG`](#me_error_log)  |  |
| [`ME_ERROR_LOG_ONLY`](#me_error_log_only)  |  |
| [`ME_NOTE`](#me_note)  |  |
| [`ME_WARNING`](#me_warning)  |  |
| [`ME_FATAL`](#me_fatal)  |  |
| [`my_error`](#my_error)  |  |
| [`my_printf_error`](#my_printf_error)  |  |
| [`my_printv_error`](#my_printv_error)  |  |

---

### ME_ERROR_LOG

```cpp
#define ME_ERROR_LOG 64 /* Write the message to the error log */
```

Defined in service_my_print_error.h:43

---

### ME_ERROR_LOG_ONLY

```cpp
#define ME_ERROR_LOG_ONLY 128 /* Write the error message to error log only */
```

Defined in service_my_print_error.h:44

---

### ME_NOTE

```cpp
#define ME_NOTE 1024 /* Not an error, just a note */
```

Defined in service_my_print_error.h:45

---

### ME_WARNING

```cpp
#define ME_WARNING 2048 /* Not an error, just a warning */
```

Defined in service_my_print_error.h:46

---

### ME_FATAL

```cpp
#define ME_FATAL 4096 /* Fatal statement error */
```

Defined in service_my_print_error.h:47

---

### my_error

```cpp
#define my_error my_print_error_service->my_error_func
```

Defined in service_my_print_error.h:61

---

### my_printf_error

```cpp
#define my_printf_error my_print_error_service->my_printf_error_func
```

Defined in service_my_print_error.h:62

---

### my_printv_error

```cpp
#define my_printv_error(A, B, C, D, A, B, C, D) my_print_error_service->my_printv_error_func(A,B,C,D)
```

Defined in service_my_print_error.h:63

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`my_print_error_service_st`](#my_print_error_service_st) * | [`my_print_error_service`](#my_print_error_service)  |  |

---

### my_print_error_service

```cpp
struct my_print_error_service_st * my_print_error_service
```

Type: struct [`my_print_error_service_st`](#my_print_error_service_st) *

Defined in service_my_print_error.h:57


## Class Definitions



### my_print_error_service_st

```cpp
#include <service_my_print_error.h>
```

```cpp
struct my_print_error_service_st
```

Defined in service_my_print_error.h:49

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`my_error_func`](#my_error_func)  |  |
| `void(*` | [`my_printf_error_func`](#my_printf_error_func)  |  |
| `void(*) void(*` | [`my_printv_error_func`](#my_printv_error_func)  |  |

---

#### my_error_func

```cpp
void(* my_error_func)(unsigned int nr, unsigned long MyFlags,...)
```

Defined in service_my_print_error.h:50

---

#### my_printf_error_func

```cpp
void(* my_printf_error_func)(unsigned int nr, const char *fmt, unsigned long MyFlags,...) ATTRIBUTE_FORMAT_FPTR(printf
```

Defined in service_my_print_error.h:51

---

#### my_printv_error_func

```cpp
void(*) void(* my_printv_error_func)(unsigned int error, const char *format, unsigned long MyFlags, va_list ap) ATTRIBUTE_FORMAT_FPTR(printf
```

Defined in service_my_print_error.h:54

