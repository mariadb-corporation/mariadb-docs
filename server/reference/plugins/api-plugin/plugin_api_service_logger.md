---
description: >-
  Plugin API reference: Logger Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Logger Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Log file with rotation implementation.

This service implements logging with possible rotation of the log files. Interface intentionally tries to be similar to FILE* related functions.

So that one can open the log with [logger_open()](api.md#logger_open), specifying the limit on the logfile size and the rotations number.

Then it's possible to write messages to the log with [logger_printf()](api.md#logger_printf) or [logger_vprintf()](api.md#logger_vprintf) functions.

As the size of the logfile grows over the specified limit, it is renamed to `logfile.1`. The former `logfile.1` becomes `logfile.2`, etc. The file `logfile.rotations` is removed.

That's how the rotation works.

The rotation can be forced with the [logger_rotate()](api.md#logger_rotate) call.

Finally the log should be closed with [logger_close()](api.md#logger_close).

> [!NOTE]
> Implementation checks the size of the log file before it starts new printf into it. So the size of the file gets over the limit when it rotates.

The access is secured with the mutex, so the log is threadsafe.

## Classes

| Name | Description |
|------|-------------|
| [`logger_service_st`](#logger_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`logger_init_mutexes`](#logger_init_mutexes)  |  |
| [`logger_open`](#logger_open)  |  |
| [`logger_close`](#logger_close)  |  |
| [`logger_rotate`](#logger_rotate)  |  |
| [`logger_vprintf`](#logger_vprintf)  |  |
| [`logger_printf`](#logger_printf)  |  |
| [`logger_write`](#logger_write)  |  |
| [`logger_sync`](#logger_sync)  |  |
| [`logger_resize_buffer`](#logger_resize_buffer)  |  |
| [`logger_set_filesize_limit`](#logger_set_filesize_limit)  |  |
| [`logger_set_rotations`](#logger_set_rotations)  |  |

---

### logger_init_mutexes

```cpp
#define logger_init_mutexes logger_service->logger_init_mutexes
```

Defined in service_logger.h:92

---

### logger_open

```cpp
#define logger_open(path, size_limit, rotations, buffer_size, path, size_limit, rotations, buffer_size) (logger_service->open(path, size_limit, rotations, buffer_size))
```

Defined in service_logger.h:93

---

### logger_close

```cpp
#define logger_close(log, log) (logger_service->close(log))
```

Defined in service_logger.h:95

---

### logger_rotate

```cpp
#define logger_rotate(log, log) (logger_service->rotate(log))
```

Defined in service_logger.h:96

---

### logger_vprintf

```cpp
#define logger_vprintf(log, fmt, argptr, log, fmt, argptr) (logger_service->\
    vprintf(log, fmt, argptr))
```

Defined in service_logger.h:97

---

### logger_printf

```cpp
#define logger_printf (*logger_service->printf)
```

Defined in service_logger.h:99

---

### logger_write

```cpp
#define logger_write(log, data, size, log, data, size) (logger_service->write(log, data, size))
```

Defined in service_logger.h:100

---

### logger_sync

```cpp
#define logger_sync(log, log) (logger_service->sync(log))
```

Defined in service_logger.h:102

---

### logger_resize_buffer

```cpp
#define logger_resize_buffer(log, new_buffer_size, log, new_buffer_size) (logger_service->resize_buffer(log, new_buffer_size))
```

Defined in service_logger.h:103

---

### logger_set_filesize_limit

```cpp
#define logger_set_filesize_limit(log, new_file_limit, log, new_file_limit) (logger_service->set_filesize_limit(log, new_file_limit))
```

Defined in service_logger.h:105

---

### logger_set_rotations

```cpp
#define logger_set_rotations(log, new_rotations, log, new_rotations) (logger_service->set_rotations(log, new_rotations))
```

Defined in service_logger.h:107

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| `struct logger_handle_st` | [`LOGGER_HANDLE`](#logger_handle)  |  |

---

### LOGGER_HANDLE

```cpp
using LOGGER_HANDLE = struct logger_handle_st
```

Defined in service_logger.h:69

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`logger_service_st`](#logger_service_st) * | [`logger_service`](#logger_service)  |  |

---

### logger_service

```cpp
struct logger_service_st * logger_service
```

Type: struct [`logger_service_st`](#logger_service_st) *

Defined in service_logger.h:88


## Class Definitions



### logger_service_st

```cpp
#include <service_logger.h>
```

```cpp
struct logger_service_st
```

Defined in service_logger.h:71

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`logger_init_mutexes`](#logger_init_mutexes-1)  |  |
| [`LOGGER_HANDLE`](api.md#logger_handle) *(* | [`open`](#open)  |  |
| `int(*` | [`close`](#close)  |  |
| `int(*` | [`vprintf`](#vprintf)  |  |
| `int(*) int(*` | [`printf`](#printf)  |  |
| `int(*) int(*) int(*` | [`write`](#write)  |  |
| `int(*` | [`rotate`](#rotate)  |  |
| `int(*` | [`sync`](#sync)  |  |
| `int(*` | [`resize_buffer`](#resize_buffer)  |  |
| `int(*` | [`set_filesize_limit`](#set_filesize_limit)  |  |
| `int(*` | [`set_rotations`](#set_rotations)  |  |

---

#### logger_init_mutexes

```cpp
void(* logger_init_mutexes)()
```

Defined in service_logger.h:72

---

#### open

```cpp
LOGGER_HANDLE *(* open)(const char *path, unsigned long long size_limit, unsigned int rotations, size_t buffer_size)
```

Defined in service_logger.h:73

---

#### close

```cpp
int(* close)(LOGGER_HANDLE *log)
```

Defined in service_logger.h:76

---

#### vprintf

```cpp
int(* vprintf)(LOGGER_HANDLE *log, const char *fmt, va_list argptr) ATTRIBUTE_FORMAT_FPTR(printf
```

Defined in service_logger.h:77

---

#### printf

```cpp
int(*) int(* printf)(LOGGER_HANDLE *log, const char *fmt,...) ATTRIBUTE_FORMAT_FPTR(printf
```

Defined in service_logger.h:79

---

#### write

```cpp
int(*) int(*) int(* write)(LOGGER_HANDLE *log, const void *data, size_t size)
```

Defined in service_logger.h:81

---

#### rotate

```cpp
int(* rotate)(LOGGER_HANDLE *log)
```

Defined in service_logger.h:82

---

#### sync

```cpp
int(* sync)(LOGGER_HANDLE *log)
```

Defined in service_logger.h:83

---

#### resize_buffer

```cpp
int(* resize_buffer)(LOGGER_HANDLE *log, size_t new_buffer_size)
```

Defined in service_logger.h:84

---

#### set_filesize_limit

```cpp
int(* set_filesize_limit)(LOGGER_HANDLE *log, unsigned long long new_file_limit)
```

Defined in service_logger.h:85

---

#### set_rotations

```cpp
int(* set_rotations)(LOGGER_HANDLE *log, unsigned int new_rotations)
```

Defined in service_logger.h:87

