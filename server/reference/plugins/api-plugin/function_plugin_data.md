---
description: >-
  Plugin API reference: Function Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Function Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for Function plugin. ([MariaDB_FUNCTION_INTERFACE_VERSION](#mariadb_function_interface_version))

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

Defined in plugin_function.h:50

API for function plugins.

An aggregate function's Create_func must create an Item_sum_plugin descendant. Aggregate implementations consume rows in add_row() and use aggregation_arg() to read values, including values replayed by DISTINCT. FILTER (WHERE ...) is applied by the server: add_row() and remove_row() see only passing rows. DISTINCT does not guarantee replay order; order-sensitive implementations must override supports_distinct() to return false. Aggregates can implement supports_removal() and remove_row() for moving window frames, and val_native() to preserve a pluggable result type.


## Class Definitions



### Plugin_function

```cpp
#include <plugin_function.h>
```

```cpp
class Plugin_function
```

Defined in plugin_function.h:53

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

Defined in plugin_function.h:58

---

#### create_func

`inline`

```cpp
inline Create_func * create_func()
```

Defined in plugin_function.h:62

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

Defined in plugin_function.h:55

---

#### m_builder

```cpp
Create_func * m_builder
```

Defined in plugin_function.h:56

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
