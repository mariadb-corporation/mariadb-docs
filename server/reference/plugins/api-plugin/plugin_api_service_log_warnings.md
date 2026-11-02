---
description: >-
  Plugin API reference: Log Warnings Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Log Warnings Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

This service provides access to the log warning level for the current session.

## Classes

| Name | Description |
|------|-------------|
| [`thd_log_warnings_service_st`](#thd_log_warnings_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_log_warnings`](#thd_log_warnings)  | Log warnings accessor |

---

### thd_log_warnings

```cpp
#define thd_log_warnings(thd, thd) thd_log_warnings_service->thd_log_warnings(thd)
```

Defined in service_log_warnings.h:48

Log warnings accessor 
#### Returns
the value of thd->log_warnings

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | the current session |
| `thd` |  | the current session |

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_log_warnings_service_st`](#thd_log_warnings_service_st) * | [`thd_log_warnings_service`](#thd_log_warnings_service)  |  |

---

### thd_log_warnings_service

```cpp
struct thd_log_warnings_service_st * thd_log_warnings_service
```

Type: struct [`thd_log_warnings_service_st`](#thd_log_warnings_service_st) *

Defined in service_log_warnings.h:40


## Class Definitions



### thd_log_warnings_service_st

```cpp
#include <service_log_warnings.h>
```

```cpp
struct thd_log_warnings_service_st
```

Defined in service_log_warnings.h:38

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void *(*` | [`thd_log_warnings`](#thd_log_warnings-1)  |  |

---

#### thd_log_warnings

```cpp
void *(* thd_log_warnings)(MYSQL_THD)
```

Defined in service_log_warnings.h:39

