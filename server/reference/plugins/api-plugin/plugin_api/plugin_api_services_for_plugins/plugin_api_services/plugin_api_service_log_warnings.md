---
description: >-
  Plugin API reference: Log Warnings Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# Log Warnings Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

This service provides access to the log warning level for the current session.

## Classes

| Name                                                                                            | Description |
| ----------------------------------------------------------------------------------------------- | ----------- |
| [`thd_log_warnings_service_st`](plugin_api_service_log_warnings.md#thd_log_warnings_service_st) |             |

## Macros

| Name                                                                      | Description           |
| ------------------------------------------------------------------------- | --------------------- |
| [`thd_log_warnings`](plugin_api_service_log_warnings.md#thd_log_warnings) | Log warnings accessor |

***

### thd\_log\_warnings

```cpp
#define thd_log_warnings(thd, thd) thd_log_warnings_service->thd_log_warnings(thd)
```

Defined in service\_log\_warnings.h:48

Log warnings accessor

#### Returns

the value of thd->log\_warnings

#### Parameters

| Parameter | Type | Description         |
| --------- | ---- | ------------------- |
| `thd`     |      | the current session |
| `thd`     |      | the current session |

## Variables

| Return                                                                                                    | Name                                                                                      | Description |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------- |
| struct [`thd_log_warnings_service_st`](plugin_api_service_log_warnings.md#thd_log_warnings_service_st) \* | [`thd_log_warnings_service`](plugin_api_service_log_warnings.md#thd_log_warnings_service) |             |

***

### thd\_log\_warnings\_service

```cpp
struct thd_log_warnings_service_st * thd_log_warnings_service
```

Type: struct [`thd_log_warnings_service_st`](plugin_api_service_log_warnings.md#thd_log_warnings_service_st) \*

Defined in service\_log\_warnings.h:40

## Class Definitions

### thd\_log\_warnings\_service\_st

```cpp
#include <service_log_warnings.h>
```

```cpp
struct thd_log_warnings_service_st
```

Defined in service\_log\_warnings.h:38

#### Public Attributes

| Return     | Name                                                                        | Description |
| ---------- | --------------------------------------------------------------------------- | ----------- |
| `void *(*` | [`thd_log_warnings`](plugin_api_service_log_warnings.md#thd_log_warnings-1) |             |

***

#### thd\_log\_warnings

```cpp
void *(* thd_log_warnings)(MYSQL_THD)
```

Defined in service\_log\_warnings.h:39
