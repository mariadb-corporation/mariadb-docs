---
description: >-
  Plugin API reference: Function Plugin. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# Function Plugin

> [`Plugin API`](../) / [`Plugin Types`](./)

API for Function plugin. ([MariaDB\_FUNCTION\_INTERFACE\_VERSION](function_plugin_data.md#mariadb_function_interface_version))

This file defines the API for server plugins that manage functions.

## Classes

| Name                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [`Plugin_function`](function_plugin_data.md#plugin_function) |             |

## Macros

| Name                                                                                               | Description               |
| -------------------------------------------------------------------------------------------------- | ------------------------- |
| [`MariaDB_FUNCTION_INTERFACE_VERSION`](function_plugin_data.md#mariadb_function_interface_version) | API for function plugins. |

***

### MariaDB\_FUNCTION\_INTERFACE\_VERSION

```cpp
#define MariaDB_FUNCTION_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin\_function.h:41

API for function plugins.

## Class Definitions

### Plugin\_function

```cpp
#include <plugin_function.h>
```

```cpp
class Plugin_function
```

Defined in plugin\_function.h:44

#### Public Methods

| Return          | Name                                                                    | Description |
| --------------- | ----------------------------------------------------------------------- | ----------- |
|                 | [`Plugin_function`](function_plugin_data.md#plugin_function-1) `inline` |             |
| `Create_func *` | [`create_func`](function_plugin_data.md#create_func) `inline`           |             |

***

#### Plugin\_function

`inline`

```cpp
inline Plugin_function(Create_func * builder)
```

Defined in plugin\_function.h:49

***

#### create\_func

`inline`

```cpp
inline Create_func * create_func()
```

Defined in plugin\_function.h:53

#### Private Attributes

| Return          | Name                                                                 | Description |
| --------------- | -------------------------------------------------------------------- | ----------- |
| `int`           | [`m_interface_version`](function_plugin_data.md#m_interface_version) |             |
| `Create_func *` | [`m_builder`](function_plugin_data.md#m_builder)                     |             |

***

#### m\_interface\_version

```cpp
int m_interface_version
```

Defined in plugin\_function.h:46

***

#### m\_builder

```cpp
Create_func * m_builder
```

Defined in plugin\_function.h:47
