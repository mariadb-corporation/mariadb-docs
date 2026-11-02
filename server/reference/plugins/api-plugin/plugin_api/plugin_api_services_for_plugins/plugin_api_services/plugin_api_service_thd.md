---
description: >-
  Plugin API reference: THD Service. Generated from the MariaDB server headers
  by doxygen and moxygen.
---

# THD Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

Access to the current thd

This service provides functions for plugins and storage engines to access current thd.

## Classes

| Name                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [`thd_service_st`](plugin_api_service_thd.md#thd_service_st) |             |

## Macros

| Name                                                           | Description                    |
| -------------------------------------------------------------- | ------------------------------ |
| [`get_current_thd`](plugin_api_service_thd.md#get_current_thd) | Current session (thd) accessor |

***

### get\_current\_thd

```cpp
#define get_current_thd() thd_service->get_current_thd()
```

Defined in service\_thd.h:49

Current session (thd) accessor

#### Returns

pointer to current thd

## Variables

| Return                                                                 | Name                                                   | Description |
| ---------------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| struct [`thd_service_st`](plugin_api_service_thd.md#thd_service_st) \* | [`thd_service`](plugin_api_service_thd.md#thd_service) |             |

***

### thd\_service

```cpp
struct thd_service_st * thd_service
```

Type: struct [`thd_service_st`](plugin_api_service_thd.md#thd_service_st) \*

Defined in service\_thd.h:42

## Class Definitions

### thd\_service\_st

```cpp
#include <service_thd.h>
```

```cpp
struct thd_service_st
```

Defined in service\_thd.h:40

#### Public Attributes

| Return                             | Name                                                             | Description |
| ---------------------------------- | ---------------------------------------------------------------- | ----------- |
| [`MYSQL_THD`](../../#mysql_thd)(\* | [`get_current_thd`](plugin_api_service_thd.md#get_current_thd-1) |             |

***

#### get\_current\_thd

```cpp
MYSQL_THD(* get_current_thd)(void)
```

Defined in service\_thd.h:41
