---
description: >-
  Plugin API reference: THD RND Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# THD RND Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

Access to the thd-local random number generator.

It's preferable over the global one, because concurrent threads can generate random numbers without fighting each other over the access to the shared rnd state.

## Classes

| Name                                                                     | Description |
| ------------------------------------------------------------------------ | ----------- |
| [`thd_rnd_service_st`](plugin_api_service_thd_rnd.md#thd_rnd_service_st) |             |

## Macros

| Name                                                                                     | Description                                                         |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [`thd_rnd`](plugin_api_service_thd_rnd.md#thd_rnd)                                       |                                                                     |
| [`thd_create_random_password`](plugin_api_service_thd_rnd.md#thd_create_random_password) | Generate string of printable random characters of requested length. |

***

### thd\_rnd

```cpp
#define thd_rnd(thd, thd) thd_rnd_service->thd_rnd_ptr(thd)
```

Defined in service\_thd\_rnd.h:52

***

### thd\_create\_random\_password

```cpp
#define thd_create_random_password(thd, to, length, thd, to, length) thd_rnd_service->thd_c_r_p_ptr(thd,to,length)
```

Defined in service\_thd\_rnd.h:61

Generate string of printable random characters of requested length.

#### Parameters

| Parameter | Type | Description                                                                                          |
| --------- | ---- | ---------------------------------------------------------------------------------------------------- |
| `thd`     |      | User thread connection handle                                                                        |
| `to`      |      | Buffer for generation; must be at least length+1 bytes long; result string is always null-terminated |
| `length`  |      | How many random characters to put in buffer                                                          |
| `thd`     |      | User thread connection handle                                                                        |
| `to`      |      | Buffer for generation; must be at least length+1 bytes long; result string is always null-terminated |
| `length`  |      | How many random characters to put in buffer                                                          |

## Variables

| Return                                                                             | Name                                                               | Description |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------- |
| struct [`thd_rnd_service_st`](plugin_api_service_thd_rnd.md#thd_rnd_service_st) \* | [`thd_rnd_service`](plugin_api_service_thd_rnd.md#thd_rnd_service) |             |

***

### thd\_rnd\_service

```cpp
struct thd_rnd_service_st * thd_rnd_service
```

Type: struct [`thd_rnd_service_st`](plugin_api_service_thd_rnd.md#thd_rnd_service_st) \*

Defined in service\_thd\_rnd.h:49

## Class Definitions

### thd\_rnd\_service\_st

```cpp
#include <service_thd_rnd.h>
```

```cpp
struct thd_rnd_service_st
```

Defined in service\_thd\_rnd.h:46

#### Public Attributes

| Return     | Name                                                           | Description |
| ---------- | -------------------------------------------------------------- | ----------- |
| `double(*` | [`thd_rnd_ptr`](plugin_api_service_thd_rnd.md#thd_rnd_ptr)     |             |
| `void(*`   | [`thd_c_r_p_ptr`](plugin_api_service_thd_rnd.md#thd_c_r_p_ptr) |             |

***

#### thd\_rnd\_ptr

```cpp
double(* thd_rnd_ptr)(MYSQL_THD thd)
```

Defined in service\_thd\_rnd.h:47

***

#### thd\_c\_r\_p\_ptr

```cpp
void(* thd_c_r_p_ptr)(MYSQL_THD thd, char *to, size_t length)
```

Defined in service\_thd\_rnd.h:48
