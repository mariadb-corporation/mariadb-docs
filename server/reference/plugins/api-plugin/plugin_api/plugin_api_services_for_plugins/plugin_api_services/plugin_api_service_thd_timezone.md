---
description: >-
  Plugin API reference: THD Timezone Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# THD Timezone Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

THD timezone handling for plugin(s)

This service provides functions to convert between my\_time\_t and MYSQL\_TIME taking into account the current value of the `time_zone` session variable.

The values of the my\_time\_t type are in Unix timestamp format, i.e. the number of seconds since `1970-01-01 00:00:00 UTC`.

The values of the MYSQL\_TIME type are in the current time zone, according to `thd->variables.time_zone`.

If the [MYSQL\_THD](../../#mysql_thd) parameter is NULL, then `global_system_variables.time_zone` is used for conversion.

## Classes

| Name                                                                                    | Description |
| --------------------------------------------------------------------------------------- | ----------- |
| [`thd_timezone_service_st`](plugin_api_service_thd_timezone.md#thd_timezone_service_st) |             |

## Macros

| Name                                                                            | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [`thd_TIME_to_gmt_sec`](plugin_api_service_thd_timezone.md#thd_time_to_gmt_sec) |             |
| [`thd_gmt_sec_to_TIME`](plugin_api_service_thd_timezone.md#thd_gmt_sec_to_time) |             |
| [`thd_TIME_to_str`](plugin_api_service_thd_timezone.md#thd_time_to_str)         |             |

***

### thd\_TIME\_to\_gmt\_sec

```cpp
#define thd_TIME_to_gmt_sec(thd, ltime, errcode, thd, ltime, errcode) (thd_timezone_service->thd_TIME_to_gmt_sec((thd), (ltime), (errcode)))
```

Defined in service\_thd\_timezone.h:67

***

### thd\_gmt\_sec\_to\_TIME

```cpp
#define thd_gmt_sec_to_TIME(thd, ltime, t, thd, ltime, t) (thd_timezone_service->thd_gmt_sec_to_TIME((thd), (ltime), (t)))
```

Defined in service\_thd\_timezone.h:70

***

### thd\_TIME\_to\_str

```cpp
#define thd_TIME_to_str(thd, ltime, format, buf, buf_len, thd, ltime, format, buf, buf_len) (thd_timezone_service->thd_TIME_to_str((thd), (ltime), (format), (buf), (buf_len)))
```

Defined in service\_thd\_timezone.h:73

## Variables

| Return                                                                                            | Name                                                                              | Description |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------- |
| struct [`thd_timezone_service_st`](plugin_api_service_thd_timezone.md#thd_timezone_service_st) \* | [`thd_timezone_service`](plugin_api_service_thd_timezone.md#thd_timezone_service) |             |

***

### thd\_timezone\_service

```cpp
struct thd_timezone_service_st * thd_timezone_service
```

Type: struct [`thd_timezone_service_st`](plugin_api_service_thd_timezone.md#thd_timezone_service_st) \*

Defined in service\_thd\_timezone.h:63

## Class Definitions

### thd\_timezone\_service\_st

```cpp
#include <service_thd_timezone.h>
```

```cpp
struct thd_timezone_service_st
```

Defined in service\_thd\_timezone.h:59

#### Public Attributes

| Return        | Name                                                                              | Description |
| ------------- | --------------------------------------------------------------------------------- | ----------- |
| `my_time_t(*` | [`thd_TIME_to_gmt_sec`](plugin_api_service_thd_timezone.md#thd_time_to_gmt_sec-1) |             |
| `void(*`      | [`thd_gmt_sec_to_TIME`](plugin_api_service_thd_timezone.md#thd_gmt_sec_to_time-1) |             |
| `void(*`      | [`thd_TIME_to_str`](plugin_api_service_thd_timezone.md#thd_time_to_str-1)         |             |

***

#### thd\_TIME\_to\_gmt\_sec

```cpp
my_time_t(* thd_TIME_to_gmt_sec)(MYSQL_THD thd, const MYSQL_TIME *ltime, unsigned int *errcode)
```

Defined in service\_thd\_timezone.h:60

***

#### thd\_gmt\_sec\_to\_TIME

```cpp
void(* thd_gmt_sec_to_TIME)(MYSQL_THD thd, MYSQL_TIME *ltime, my_time_t t)
```

Defined in service\_thd\_timezone.h:61

***

#### thd\_TIME\_to\_str

```cpp
void(* thd_TIME_to_str)(MYSQL_THD thd, const MYSQL_TIME *ltime, const char *format, char *buf, unsigned int buf_len)
```

Defined in service\_thd\_timezone.h:62
