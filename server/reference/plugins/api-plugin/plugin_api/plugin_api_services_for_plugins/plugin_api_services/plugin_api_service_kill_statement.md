---
description: >-
  Plugin API reference: KILL Statement Service. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# KILL Statement Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

This service provides functions that allow plugins to support the KILL statement.

In MySQL support for the KILL statement is cooperative. The KILL statement only sets a "killed" flag. This function returns the value of that flag. A thread should check it often, especially inside time-consuming loops, and gracefully abort the operation if it is non-zero.

## Classes

| Name                                                                                          | Description |
| --------------------------------------------------------------------------------------------- | ----------- |
| [`kill_statement_service_st`](plugin_api_service_kill_statement.md#kill_statement_service_st) |             |

## Macros

| Name                                                                    | Description                                                |
| ----------------------------------------------------------------------- | ---------------------------------------------------------- |
| [`thd_killed`](plugin_api_service_kill_statement.md#thd_killed)         | Backward compatibility helper                              |
| [`thd_kill_level`](plugin_api_service_kill_statement.md#thd_kill_level) | Check if a KILL statement was issued for the given thread. |

***

### thd\_killed

```cpp
#define thd_killed(THD, THD) (thd_kill_level(THD) == THD_ABORT_ASAP)
```

Defined in service\_kill\_statement.h:62

Backward compatibility helper

#### Parameters

| Parameter | Type | Description   |
| --------- | ---- | ------------- |
| `THD`     |      | thread handle |
| `THD`     |      | thread handle |

#### Return Values

| Value | Description                                      |
| ----- | ------------------------------------------------ |
| `0`   | No KILL statement was issued, continue normally  |
| `1`   | There was a KILL statement, abort the execution. |

***

### thd\_kill\_level

```cpp
#define thd_kill_level(THD, THD) thd_kill_statement_service->thd_kill_level_func(THD)
```

Defined in service\_kill\_statement.h:73

Check if a KILL statement was issued for the given thread.

#### Returns

[thd\_kill\_levels](plugin_api_service_kill_statement.md#thd_kill_levels) values

#### Parameters

| Parameter | Type | Description   |
| --------- | ---- | ------------- |
| `THD`     |      | thread handle |
| `THD`     |      | thread handle |

## Enumerations

| Name                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [`thd_kill_levels`](plugin_api_service_kill_statement.md#thd_kill_levels) |             |

***

### thd\_kill\_levels

```cpp
enum thd_kill_levels
```

Defined in service\_kill\_statement.h:45

| Value               | Description                                       |
| ------------------- | ------------------------------------------------- |
| `THD_IS_NOT_KILLED` |                                                   |
| `THD_ABORT_SOFTLY`  | abort when possible, don't leave tables corrupted |
| `THD_ABORT_ASAP`    | abort asap                                        |

## Variables

| Return                                                                                                  | Name                                                                                            | Description |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| struct [`kill_statement_service_st`](plugin_api_service_kill_statement.md#kill_statement_service_st) \* | [`thd_kill_statement_service`](plugin_api_service_kill_statement.md#thd_kill_statement_service) |             |

***

### thd\_kill\_statement\_service

```cpp
struct kill_statement_service_st * thd_kill_statement_service
```

Type: struct [`kill_statement_service_st`](plugin_api_service_kill_statement.md#kill_statement_service_st) \*

Defined in service\_kill\_statement.h:53

## Class Definitions

### kill\_statement\_service\_st

```cpp
#include <service_kill_statement.h>
```

```cpp
struct kill_statement_service_st
```

Defined in service\_kill\_statement.h:51

#### Public Attributes

| Return                                                                            | Name                                                                              | Description |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------- |
| enum [`thd_kill_levels`](plugin_api_service_kill_statement.md#thd_kill_levels)(\* | [`thd_kill_level_func`](plugin_api_service_kill_statement.md#thd_kill_level_func) |             |

***

#### thd\_kill\_level\_func

```cpp
enum thd_kill_levels(* thd_kill_level_func)(const MYSQL_THD)
```

Defined in service\_kill\_statement.h:1
