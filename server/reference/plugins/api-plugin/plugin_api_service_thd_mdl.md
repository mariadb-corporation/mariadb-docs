---
description: >-
  Plugin API reference: THD MDL Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# THD MDL Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Access to the metadata locks.

This service provides functions for plugins and storage engines to access metadata locks.

## Classes

| Name | Description |
|------|-------------|
| [`thd_mdl_service_st`](#thd_mdl_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_mdl_context`](#thd_mdl_context)  | MDL_context accessor |

---

### thd_mdl_context

```cpp
#define thd_mdl_context(thd, thd) thd_mdl_service->thd_mdl_context(thd)
```

Defined in service_thd_mdl.h:49

MDL_context accessor 
#### Returns
pointer to thd->mdl_context

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | the current session |
| `thd` |  | the current session |

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_mdl_service_st`](#thd_mdl_service_st) * | [`thd_mdl_service`](#thd_mdl_service)  |  |

---

### thd_mdl_service

```cpp
struct thd_mdl_service_st * thd_mdl_service
```

Type: struct [`thd_mdl_service_st`](#thd_mdl_service_st) *

Defined in service_thd_mdl.h:41


## Class Definitions



### thd_mdl_service_st

```cpp
#include <service_thd_mdl.h>
```

```cpp
struct thd_mdl_service_st
```

Defined in service_thd_mdl.h:39

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void *(*` | [`thd_mdl_context`](#thd_mdl_context-1)  |  |

---

#### thd_mdl_context

```cpp
void *(* thd_mdl_context)(MYSQL_THD)
```

Defined in service_thd_mdl.h:40

