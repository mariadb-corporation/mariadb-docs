---
description: >-
  Plugin API reference: THD Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# THD Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Access to the current thd

This service provides functions for plugins and storage engines to access current thd.

## Classes

| Name | Description |
|------|-------------|
| [`thd_service_st`](#thd_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`get_current_thd`](#get_current_thd)  | Current session (thd) accessor |

---

### get_current_thd

```cpp
#define get_current_thd() thd_service->get_current_thd()
```

Defined in service_thd.h:49

Current session (thd) accessor 
#### Returns
pointer to current thd

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_service_st`](#thd_service_st) * | [`thd_service`](#thd_service)  |  |

---

### thd_service

```cpp
struct thd_service_st * thd_service
```

Type: struct [`thd_service_st`](#thd_service_st) *

Defined in service_thd.h:42


## Class Definitions



### thd_service_st

```cpp
#include <service_thd.h>
```

```cpp
struct thd_service_st
```

Defined in service_thd.h:40

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`MYSQL_THD`](api.md#mysql_thd)(* | [`get_current_thd`](#get_current_thd-1)  |  |

---

#### get_current_thd

```cpp
MYSQL_THD(* get_current_thd)(void)
```

Defined in service_thd.h:41

