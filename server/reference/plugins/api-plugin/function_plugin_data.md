---
description: >-
  Plugin API reference: Function Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Function Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for Function plugin. ([MariaDB_FUNCTION_INTERFACE_VERSION](api.md#mariadb_function_interface_version))

This file defines the API for server plugins that manage functions.

## Classes

| Name | Description |
|------|-------------|
| [`Plugin_function`](#plugin_function) |  |

## Macros

| Name | Description |
|------|-------------|
| [`MariaDB_FUNCTION_INTERFACE_VERSION`](#mariadb_function_interface_version)  | API for function plugins. |

---

### MariaDB_FUNCTION_INTERFACE_VERSION

```cpp
#define MariaDB_FUNCTION_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin_function.h:41

API for function plugins.


## Class Definitions



### Plugin_function

```cpp
#include <plugin_function.h>
```

```cpp
class Plugin_function
```

Defined in plugin_function.h:44

#### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`Plugin_function`](#plugin_function-1) `inline` |  |
| `Create_func *` | [`create_func`](#create_func) `inline` |  |

---

#### Plugin_function

`inline`

```cpp
inline Plugin_function(Create_func * builder)
```

Defined in plugin_function.h:49

---

#### create_func

`inline`

```cpp
inline Create_func * create_func()
```

Defined in plugin_function.h:53

#### Private Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`m_interface_version`](#m_interface_version)  |  |
| `Create_func *` | [`m_builder`](#m_builder)  |  |

---

#### m_interface_version

```cpp
int m_interface_version
```

Defined in plugin_function.h:46

---

#### m_builder

```cpp
Create_func * m_builder
```

Defined in plugin_function.h:47

