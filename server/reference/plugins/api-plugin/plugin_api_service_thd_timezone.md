---
description: >-
  Plugin API reference: THD Timezone Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# THD Timezone Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

THD timezone handling for plugin(s)

This service provides functions to convert between my_time_t and MYSQL_TIME taking into account the current value of the `time_zone` session variable.

The values of the my_time_t type are in Unix timestamp format, i.e. the number of seconds since `1970-01-01 00:00:00 UTC`.

The values of the MYSQL_TIME type are in the current time zone, according to `thd->variables.time_zone`.

If the [MYSQL_THD](api.md#mysql_thd) parameter is NULL, then `global_system_variables.time_zone` is used for conversion.

## Classes

| Name | Description |
|------|-------------|
| [`thd_timezone_service_st`](#thd_timezone_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_TIME_to_gmt_sec`](#thd_time_to_gmt_sec)  |  |
| [`thd_gmt_sec_to_TIME`](#thd_gmt_sec_to_time)  |  |
| [`thd_TIME_to_str`](#thd_time_to_str)  |  |

---

### thd_TIME_to_gmt_sec

```cpp
#define thd_TIME_to_gmt_sec(thd, ltime, errcode, thd, ltime, errcode) (thd_timezone_service->thd_TIME_to_gmt_sec((thd), (ltime), (errcode)))
```

Defined in service_thd_timezone.h:67

---

### thd_gmt_sec_to_TIME

```cpp
#define thd_gmt_sec_to_TIME(thd, ltime, t, thd, ltime, t) (thd_timezone_service->thd_gmt_sec_to_TIME((thd), (ltime), (t)))
```

Defined in service_thd_timezone.h:70

---

### thd_TIME_to_str

```cpp
#define thd_TIME_to_str(thd, ltime, format, buf, buf_len, thd, ltime, format, buf, buf_len) (thd_timezone_service->thd_TIME_to_str((thd), (ltime), (format), (buf), (buf_len)))
```

Defined in service_thd_timezone.h:73

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_timezone_service_st`](#thd_timezone_service_st) * | [`thd_timezone_service`](#thd_timezone_service)  |  |

---

### thd_timezone_service

```cpp
struct thd_timezone_service_st * thd_timezone_service
```

Type: struct [`thd_timezone_service_st`](#thd_timezone_service_st) *

Defined in service_thd_timezone.h:63


## Class Definitions



### thd_timezone_service_st

```cpp
#include <service_thd_timezone.h>
```

```cpp
struct thd_timezone_service_st
```

Defined in service_thd_timezone.h:59

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `my_time_t(*` | [`thd_TIME_to_gmt_sec`](#thd_time_to_gmt_sec-1)  |  |
| `void(*` | [`thd_gmt_sec_to_TIME`](#thd_gmt_sec_to_time-1)  |  |
| `void(*` | [`thd_TIME_to_str`](#thd_time_to_str-1)  |  |

---

#### thd_TIME_to_gmt_sec

```cpp
my_time_t(* thd_TIME_to_gmt_sec)(MYSQL_THD thd, const MYSQL_TIME *ltime, unsigned int *errcode)
```

Defined in service_thd_timezone.h:60

---

#### thd_gmt_sec_to_TIME

```cpp
void(* thd_gmt_sec_to_TIME)(MYSQL_THD thd, MYSQL_TIME *ltime, my_time_t t)
```

Defined in service_thd_timezone.h:61

---

#### thd_TIME_to_str

```cpp
void(* thd_TIME_to_str)(MYSQL_THD thd, const MYSQL_TIME *ltime, const char *format, char *buf, unsigned int buf_len)
```

Defined in service_thd_timezone.h:62

