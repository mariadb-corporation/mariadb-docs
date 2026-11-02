---
description: >-
  Plugin API reference: Print Check Msg Service. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# Print Check Msg Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

This service provides functions to write messages for check or repair

## Classes

| Name                                                                                             | Description |
| ------------------------------------------------------------------------------------------------ | ----------- |
| [`print_check_msg_service_st`](plugin_api_service_print_check_msg.md#print_check_msg_service_st) |             |

## Macros

| Name                                                                       | Description |
| -------------------------------------------------------------------------- | ----------- |
| [`print_check_msg`](plugin_api_service_print_check_msg.md#print_check_msg) |             |

***

### print\_check\_msg

```cpp
#define print_check_msg(thd, db_name, table_name, op, msg_type, message, print_to_log, thd, db_name, table_name, op, msg_type, message, print_to_log) print_check_msg_service->print_check_msg(thd, db_name, table_name, op, msg_type, message, print_to_log)
```

Defined in service\_print\_check\_msg.h:41

## Variables

| Return                                                                                                     | Name                                                                                       | Description |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------- |
| struct [`print_check_msg_service_st`](plugin_api_service_print_check_msg.md#print_check_msg_service_st) \* | [`print_check_msg_service`](plugin_api_service_print_check_msg.md#print_check_msg_service) |             |

***

### print\_check\_msg\_service

```cpp
struct print_check_msg_service_st * print_check_msg_service
```

Type: struct [`print_check_msg_service_st`](plugin_api_service_print_check_msg.md#print_check_msg_service_st) \*

Defined in service\_print\_check\_msg.h:38

## Class Definitions

### print\_check\_msg\_service\_st

```cpp
#include <service_print_check_msg.h>
```

```cpp
struct print_check_msg_service_st
```

Defined in service\_print\_check\_msg.h:34

#### Public Attributes

| Return   | Name                                                                         | Description |
| -------- | ---------------------------------------------------------------------------- | ----------- |
| `void(*` | [`print_check_msg`](plugin_api_service_print_check_msg.md#print_check_msg-1) |             |

***

#### print\_check\_msg

```cpp
void(* print_check_msg)(MYSQL_THD thd, const char *db_name, const char *table_name, const char *op, const char *msg_type, const char *message, my_bool print_to_log)
```

Defined in service\_print\_check\_msg.h:35
