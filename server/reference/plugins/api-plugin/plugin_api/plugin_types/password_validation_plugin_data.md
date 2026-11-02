---
description: >-
  Plugin API reference: Password Validation Plugin. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# Password Validation Plugin

> [`Plugin API`](../) / [`Plugin Types`](./)

Password validation plugin API ([MariaDB\_PASSWORD\_VALIDATION\_INTERFACE\_VERSION](password_validation_plugin_data.md#mariadb_password_validation_interface_version))

This file defines the API for server plugins that perform password validation.

## Classes

| Name                                                                                                  | Description                           |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------- |
| [`st_mariadb_password_validation`](password_validation_plugin_data.md#st_mariadb_password_validation) | Password validation plugin descriptor |

## Macros

| Name                                                                                                                                | Description |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [`MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION`](password_validation_plugin_data.md#mariadb_password_validation_interface_version) |             |

***

### MariaDB\_PASSWORD\_VALIDATION\_INTERFACE\_VERSION

```cpp
#define MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION 0x0101
```

Defined in plugin\_password\_validation.h:43

## Class Definitions

### st\_mariadb\_password\_validation

```cpp
#include <plugin_password_validation.h>
```

```cpp
struct st_mariadb_password_validation
```

Defined in plugin\_password\_validation.h:48

Password validation plugin descriptor

#### Public Attributes

| Return  | Name                                                                        | Description                                                                                                                      |
| ------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `int`   | [`interface_version`](password_validation_plugin_data.md#interface_version) | version plugin uses                                                                                                              |
| `int(*` | [`validate_password`](password_validation_plugin_data.md#validate_password) | Function provided by the plugin which should perform password validation and return 0 if the password has passed the validation. |

***

#### interface\_version

```cpp
int interface_version
```

Defined in plugin\_password\_validation.h:50

version plugin uses

***

#### validate\_password

```cpp
int(* validate_password)(const MYSQL_CONST_LEX_STRING *username, const MYSQL_CONST_LEX_STRING *password, const MYSQL_CONST_LEX_STRING *hostname)
```

Defined in plugin\_password\_validation.h:55

Function provided by the plugin which should perform password validation and return 0 if the password has passed the validation.
