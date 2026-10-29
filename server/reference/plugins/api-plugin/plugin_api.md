---
description: >-
  Plugin API reference: Plugin API. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin API

The Plugin API is a set of interfaces for handling plugins.

## Groups

| Name | Description |
|------|-------------|
| [`Plugin Types`](plugin_types.md) | The available plugin APIs (types). |
| [`Plugin Declaration`](plugin_declaration.md) | How to declare a plugin to the server. |
| [`Services for Plugins`](plugin_api_services_for_plugins.md) | Plugins calling back into the server. |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_THD`](#mysql_thd)  |  |

---

### MYSQL_THD

```cpp
#define MYSQL_THD THD*
```

Defined in plugin.h:66

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| `char` | [`my_bool`](#my_bool)  |  |

---

### my_bool

```cpp
using my_bool = char
```

Defined in plugin.h:72

