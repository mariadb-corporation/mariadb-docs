---
description: >-
  Plugin API reference: THD MDL Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# THD MDL Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

Access to the metadata locks.

This service provides functions for plugins and storage engines to access metadata locks.

## Classes

| Name                                                                     | Description |
| ------------------------------------------------------------------------ | ----------- |
| [`thd_mdl_service_st`](plugin_api_service_thd_mdl.md#thd_mdl_service_st) |             |

## Macros

| Name                                                               | Description           |
| ------------------------------------------------------------------ | --------------------- |
| [`thd_mdl_context`](plugin_api_service_thd_mdl.md#thd_mdl_context) | MDL\_context accessor |

***

### thd\_mdl\_context

```cpp
#define thd_mdl_context(thd, thd) thd_mdl_service->thd_mdl_context(thd)
```

Defined in service\_thd\_mdl.h:49

MDL\_context accessor

#### Returns

pointer to thd->mdl\_context

#### Parameters

| Parameter | Type | Description         |
| --------- | ---- | ------------------- |
| `thd`     |      | the current session |
| `thd`     |      | the current session |

## Variables

| Return                                                                             | Name                                                               | Description |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------- |
| struct [`thd_mdl_service_st`](plugin_api_service_thd_mdl.md#thd_mdl_service_st) \* | [`thd_mdl_service`](plugin_api_service_thd_mdl.md#thd_mdl_service) |             |

***

### thd\_mdl\_service

```cpp
struct thd_mdl_service_st * thd_mdl_service
```

Type: struct [`thd_mdl_service_st`](plugin_api_service_thd_mdl.md#thd_mdl_service_st) \*

Defined in service\_thd\_mdl.h:41

## Class Definitions

### thd\_mdl\_service\_st

```cpp
#include <service_thd_mdl.h>
```

```cpp
struct thd_mdl_service_st
```

Defined in service\_thd\_mdl.h:39

#### Public Attributes

| Return     | Name                                                                 | Description |
| ---------- | -------------------------------------------------------------------- | ----------- |
| `void *(*` | [`thd_mdl_context`](plugin_api_service_thd_mdl.md#thd_mdl_context-1) |             |

***

#### thd\_mdl\_context

```cpp
void *(* thd_mdl_context)(MYSQL_THD)
```

Defined in service\_thd\_mdl.h:40
