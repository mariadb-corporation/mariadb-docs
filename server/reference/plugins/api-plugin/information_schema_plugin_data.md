---
description: >-
  Plugin API reference: Information Schema Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Information Schema Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for I_S plugin. ([MYSQL_INFORMATION_SCHEMA_PLUGIN](api.md#mysql_information_schema_plugin))

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_information_schema`](#st_mysql_information_schema) | The descriptor structure, that is referred from [st_mysql_plugin](plugin_declaration.md#st_mysql_plugin). |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_INFORMATION_SCHEMA_INTERFACE_VERSION`](#mysql_information_schema_interface_version)  | information schema plugins of different MySQL releases are incompatible |

---

### MYSQL_INFORMATION_SCHEMA_INTERFACE_VERSION

```cpp
#define MYSQL_INFORMATION_SCHEMA_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:803

information schema plugins of different MySQL releases are incompatible


## Class Definitions



### st_mysql_information_schema

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_information_schema
```

Defined in plugin.h:809

The descriptor structure, that is referred from [st_mysql_plugin](plugin_declaration.md#st_mysql_plugin).

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in plugin.h:811

