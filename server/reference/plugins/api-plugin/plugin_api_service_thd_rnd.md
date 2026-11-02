---
description: >-
  Plugin API reference: THD RND Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# THD RND Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Access to the thd-local random number generator.

It's preferable over the global one, because concurrent threads can generate random numbers without fighting each other over the access to the shared rnd state.

## Classes

| Name | Description |
|------|-------------|
| [`thd_rnd_service_st`](#thd_rnd_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_rnd`](#thd_rnd)  |  |
| [`thd_create_random_password`](#thd_create_random_password)  | Generate string of printable random characters of requested length. |

---

### thd_rnd

```cpp
#define thd_rnd(thd, thd) thd_rnd_service->thd_rnd_ptr(thd)
```

Defined in service_thd_rnd.h:52

---

### thd_create_random_password

```cpp
#define thd_create_random_password(thd, to, length, thd, to, length) thd_rnd_service->thd_c_r_p_ptr(thd,to,length)
```

Defined in service_thd_rnd.h:61

Generate string of printable random characters of requested length.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | User thread connection handle |
| `to` |  | Buffer for generation; must be at least length+1 bytes long; result string is always null-terminated |
| `length` |  | How many random characters to put in buffer |
| `thd` |  | User thread connection handle |
| `to` |  | Buffer for generation; must be at least length+1 bytes long; result string is always null-terminated |
| `length` |  | How many random characters to put in buffer |

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_rnd_service_st`](#thd_rnd_service_st) * | [`thd_rnd_service`](#thd_rnd_service)  |  |

---

### thd_rnd_service

```cpp
struct thd_rnd_service_st * thd_rnd_service
```

Type: struct [`thd_rnd_service_st`](#thd_rnd_service_st) *

Defined in service_thd_rnd.h:49


## Class Definitions



### thd_rnd_service_st

```cpp
#include <service_thd_rnd.h>
```

```cpp
struct thd_rnd_service_st
```

Defined in service_thd_rnd.h:46

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `double(*` | [`thd_rnd_ptr`](#thd_rnd_ptr)  |  |
| `void(*` | [`thd_c_r_p_ptr`](#thd_c_r_p_ptr)  |  |

---

#### thd_rnd_ptr

```cpp
double(* thd_rnd_ptr)(MYSQL_THD thd)
```

Defined in service_thd_rnd.h:47

---

#### thd_c_r_p_ptr

```cpp
void(* thd_c_r_p_ptr)(MYSQL_THD thd, char *to, size_t length)
```

Defined in service_thd_rnd.h:48

