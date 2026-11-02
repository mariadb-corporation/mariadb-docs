---
description: >-
  Plugin API reference: THD Autoinc Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# THD Autoinc Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

Access to the auto\_increment related system variables.

This service is used by plugins that need to know the current values of the auto\_increment\_offset and auto\_increment\_increment system variables for a given thread. This service provides access to the auto\_increment related system variables:

* `@@auto_increment_offset`
* `@@auto_increment_increment`

## Classes

| Name                                                                                 | Description |
| ------------------------------------------------------------------------------------ | ----------- |
| [`thd_autoinc_service_st`](plugin_api_service_thd_autoinc.md#thd_autoinc_service_st) |             |

## Macros

| Name                                                                   | Description                           |
| ---------------------------------------------------------------------- | ------------------------------------- |
| [`thd_get_autoinc`](plugin_api_service_thd_autoinc.md#thd_get_autoinc) | Return autoincrement system variables |

***

### thd\_get\_autoinc

```cpp
#define thd_get_autoinc(thd, off, inc, thd, off, inc) (thd_autoinc_service->thd_get_autoinc_func((thd), (off), (inc)))
```

Defined in service\_thd\_autoinc.h:55

Return autoincrement system variables

#### Parameters

| Parameter | Type | Description                                      |
| --------- | ---- | ------------------------------------------------ |
| `thd`     |      | user thread connection handle                    |
| `off`     |      | the value of @SESSION.auto\_increment\_offset    |
| `inc`     |      | the value of @SESSION.auto\_increment\_increment |
| `thd`     |      | user thread connection handle                    |
| `off`     |      | the value of @SESSION.auto\_increment\_offset    |
| `inc`     |      | the value of @SESSION.auto\_increment\_increment |

## Variables

| Return                                                                                         | Name                                                                           | Description |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------- |
| struct [`thd_autoinc_service_st`](plugin_api_service_thd_autoinc.md#thd_autoinc_service_st) \* | [`thd_autoinc_service`](plugin_api_service_thd_autoinc.md#thd_autoinc_service) |             |

***

### thd\_autoinc\_service

```cpp
struct thd_autoinc_service_st * thd_autoinc_service
```

Type: struct [`thd_autoinc_service_st`](plugin_api_service_thd_autoinc.md#thd_autoinc_service_st) \*

Defined in service\_thd\_autoinc.h:46

## Class Definitions

### thd\_autoinc\_service\_st

```cpp
#include <service_thd_autoinc.h>
```

```cpp
struct thd_autoinc_service_st
```

Defined in service\_thd\_autoinc.h:43

#### Public Attributes

| Return   | Name                                                                             | Description |
| -------- | -------------------------------------------------------------------------------- | ----------- |
| `void(*` | [`thd_get_autoinc_func`](plugin_api_service_thd_autoinc.md#thd_get_autoinc_func) |             |

***

#### thd\_get\_autoinc\_func

```cpp
void(* thd_get_autoinc_func)(const MYSQL_THD thd, unsigned long *off, unsigned long *inc)
```

Defined in service\_thd\_autoinc.h:44
