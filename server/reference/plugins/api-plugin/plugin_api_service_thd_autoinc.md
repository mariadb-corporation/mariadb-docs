---
description: >-
  Plugin API reference: THD Autoinc Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# THD Autoinc Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Access to the auto_increment related system variables.

This service is used by plugins that need to know the current values of the auto_increment_offset and auto_increment_increment system variables for a given thread. This service provides access to the auto_increment related system variables:

* `@@auto_increment_offset`
* `@@auto_increment_increment`

## Classes

| Name | Description |
|------|-------------|
| [`thd_autoinc_service_st`](#thd_autoinc_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_get_autoinc`](#thd_get_autoinc)  | Return autoincrement system variables |

---

### thd_get_autoinc

```cpp
#define thd_get_autoinc(thd, off, inc, thd, off, inc) (thd_autoinc_service->thd_get_autoinc_func((thd), (off), (inc)))
```

Defined in service_thd_autoinc.h:55

Return autoincrement system variables

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `off` |  | the value of @SESSION.auto_increment_offset |
| `inc` |  | the value of @SESSION.auto_increment_increment |
| `thd` |  | user thread connection handle |
| `off` |  | the value of @SESSION.auto_increment_offset |
| `inc` |  | the value of @SESSION.auto_increment_increment |

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_autoinc_service_st`](#thd_autoinc_service_st) * | [`thd_autoinc_service`](#thd_autoinc_service)  |  |

---

### thd_autoinc_service

```cpp
struct thd_autoinc_service_st * thd_autoinc_service
```

Type: struct [`thd_autoinc_service_st`](#thd_autoinc_service_st) *

Defined in service_thd_autoinc.h:46


## Class Definitions



### thd_autoinc_service_st

```cpp
#include <service_thd_autoinc.h>
```

```cpp
struct thd_autoinc_service_st
```

Defined in service_thd_autoinc.h:43

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`thd_get_autoinc_func`](#thd_get_autoinc_func)  |  |

---

#### thd_get_autoinc_func

```cpp
void(* thd_get_autoinc_func)(const MYSQL_THD thd, unsigned long *off, unsigned long *inc)
```

Defined in service_thd_autoinc.h:44

