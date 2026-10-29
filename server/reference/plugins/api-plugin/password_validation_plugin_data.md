---
description: >-
  Plugin API reference: Password Validation Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Password Validation Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

Password validation plugin API ([MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION](api.md#mariadb_password_validation_interface_version))

This file defines the API for server plugins that perform password validation.

## Classes

| Name | Description |
|------|-------------|
| [`st_mariadb_password_validation`](#st_mariadb_password_validation) | Password validation plugin descriptor |

## Macros

| Name | Description |
|------|-------------|
| [`MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION`](#mariadb_password_validation_interface_version)  |  |

---

### MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION

```cpp
#define MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION 0x0101
```

Defined in plugin_password_validation.h:43


## Class Definitions



### st_mariadb_password_validation

```cpp
#include <plugin_password_validation.h>
```

```cpp
struct st_mariadb_password_validation
```

Defined in plugin_password_validation.h:48

Password validation plugin descriptor

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version)  | version plugin uses |
| `int(*` | [`validate_password`](#validate_password)  | Function provided by the plugin which should perform password validation and return 0 if the password has passed the validation. |

---

#### interface_version

```cpp
int interface_version
```

Defined in plugin_password_validation.h:50

version plugin uses

---

#### validate_password

```cpp
int(* validate_password)(const MYSQL_CONST_LEX_STRING *username, const MYSQL_CONST_LEX_STRING *password, const MYSQL_CONST_LEX_STRING *hostname)
```

Defined in plugin_password_validation.h:55

Function provided by the plugin which should perform password validation and return 0 if the password has passed the validation.

