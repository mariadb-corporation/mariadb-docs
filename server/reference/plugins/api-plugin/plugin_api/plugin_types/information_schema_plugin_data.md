---
description: >-
  Plugin API reference: Information Schema Plugin. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# Information Schema Plugin

> [`Plugin API`](../) / [`Plugin Types`](./)

API for I\_S plugin. ([MYSQL\_INFORMATION\_SCHEMA\_PLUGIN](./#mysql_information_schema_plugin))

## Classes

| Name                                                                                           | Description                                                                                                  |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [`st_mysql_information_schema`](information_schema_plugin_data.md#st_mysql_information_schema) | The descriptor structure, that is referred from [st\_mysql\_plugin](../plugin_declaration/#st_mysql_plugin). |

## Macros

| Name                                                                                                                         | Description                                                             |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [`MYSQL_INFORMATION_SCHEMA_INTERFACE_VERSION`](information_schema_plugin_data.md#mysql_information_schema_interface_version) | information schema plugins of different MySQL releases are incompatible |

***

### MYSQL\_INFORMATION\_SCHEMA\_INTERFACE\_VERSION

```cpp
#define MYSQL_INFORMATION_SCHEMA_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:803

information schema plugins of different MySQL releases are incompatible

## Class Definitions

### st\_mysql\_information\_schema

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_information_schema
```

Defined in plugin.h:809

The descriptor structure, that is referred from [st\_mysql\_plugin](../plugin_declaration/#st_mysql_plugin).

#### Public Attributes

| Return | Name                                                                       | Description |
| ------ | -------------------------------------------------------------------------- | ----------- |
| `int`  | [`interface_version`](information_schema_plugin_data.md#interface_version) |             |

***

#### interface\_version

```cpp
int interface_version
```

Defined in plugin.h:811
