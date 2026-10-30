---
description: >-
  Plugin API reference: THD Wait Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# THD Wait Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

This service provides functions for plugins and storage engines to report when they are going to sleep/stall.

Using [thd_wait_begin()](#thd_wait_begin) / [thd_wait_end()](#thd_wait_end) service is optional but recommended. Using it will improve performance as the thread pool will be more active at managing the thread workload. If [thd_wait_begin()](#thd_wait_begin) is called, [thd_wait_end()](#thd_wait_end) MUST be called immediately after waking up.

One should only report wait events that could potentially block for a long time. A mutex wait is too short of an event to report. The reason is that an event which is reported leads to a new thread starts executing a query and this has a negative impact of usage of CPU caches and thus the expected gain of starting a new thread must be higher than the expected cost of lost performance due to starting a new thread.

Good examples of events that should be reported are waiting for row locks that could easily be for many milliseconds or even seconds and the same holds true for global read locks, table locks and other meta data locks. Another event of interest is going to sleep for an extended time.

## Classes

| Name | Description |
|------|-------------|
| [`thd_wait_service_st`](#thd_wait_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_wait_begin`](#thd_wait_begin)  | Call just before a wait begins |
| [`thd_wait_end`](#thd_wait_end)  | Call just after a wait ends |

---

### thd_wait_begin

```cpp
#define thd_wait_begin(thd, wait_type, thd, wait_type) thd_wait_service->thd_wait_begin_func(thd, wait_type)
```

Defined in service_thd_wait.h:91

Call just before a wait begins 
This is used by the threadpool to have better knowledge of which threads that currently are actively running on CPUs. When a thread reports that it's going to sleep/stall, the threadpool scheduler is free to start another thread in the pool most likely. The expected wait time is simply an indication of how long the wait is expected to become, the real wait time could be very different.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | Thread object. Use NULL if the thd is NOT known. |
| `wait_type` |  | Type of wait: one of [thd_wait_type](#thd_wait_type) |
| `thd` |  | Thread object. Use NULL if the thd is NOT known. |
| `wait_type` |  | Type of wait: one of [thd_wait_type](#thd_wait_type) |

---

### thd_wait_end

```cpp
#define thd_wait_end(thd, thd) thd_wait_service->thd_wait_end_func(thd)
```

Defined in service_thd_wait.h:97

Call just after a wait ends

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | Thread object. Use NULL if the thd is NOT known. |
| `thd` |  | Thread object. Use NULL if the thd is NOT known. |

## Enumerations

| Name | Description |
|------|-------------|
| [`_thd_wait_type_e`](#thd_wait_type_e)  |  |

---

### _thd_wait_type_e

```cpp
enum _thd_wait_type_e
```

Defined in service_thd_wait.h:57

| Value | Description |
|-------|-------------|
| `THD_WAIT_SLEEP` | sleep |
| `THD_WAIT_DISKIO` | Medium wait (e.g. for disk io) |
| `THD_WAIT_ROW_LOCK` | Large wait (e.g. for locked row/table) |
| `THD_WAIT_GLOBAL_LOCK` |  |
| `THD_WAIT_META_DATA_LOCK` |  |
| `THD_WAIT_TABLE_LOCK` |  |
| `THD_WAIT_USER_LOCK` |  |
| `THD_WAIT_BINLOG` |  |
| `THD_WAIT_GROUP_COMMIT` |  |
| `THD_WAIT_SYNC` |  |
| `THD_WAIT_NET` |  |
| `THD_WAIT_LAST` |  |
## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| enum [`_thd_wait_type_e`](#thd_wait_type_e) | [`thd_wait_type`](#thd_wait_type)  |  |

---

### thd_wait_type

```cpp
using thd_wait_type = enum _thd_wait_type_e
```

Type: enum [`_thd_wait_type_e`](#thd_wait_type_e)

Defined in service_thd_wait.h:70

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_wait_service_st`](#thd_wait_service_st) * | [`thd_wait_service`](#thd_wait_service)  |  |

---

### thd_wait_service

```cpp
struct thd_wait_service_st * thd_wait_service
```

Type: struct [`thd_wait_service_st`](#thd_wait_service_st) *

Defined in service_thd_wait.h:75


## Class Definitions



### thd_wait_service_st

```cpp
#include <service_thd_wait.h>
```

```cpp
struct thd_wait_service_st
```

Defined in service_thd_wait.h:72

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`thd_wait_begin_func`](#thd_wait_begin_func)  |  |
| `void(*` | [`thd_wait_end_func`](#thd_wait_end_func)  |  |

---

#### thd_wait_begin_func

```cpp
void(* thd_wait_begin_func)(MYSQL_THD, int)
```

Defined in service_thd_wait.h:73

---

#### thd_wait_end_func

```cpp
void(* thd_wait_end_func)(MYSQL_THD)
```

Defined in service_thd_wait.h:74

