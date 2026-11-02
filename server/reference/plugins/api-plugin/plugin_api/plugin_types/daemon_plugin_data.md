---
description: >-
  Plugin API reference: Daemon Plugin. Generated from the MariaDB server headers
  by doxygen and moxygen.
---

# Daemon Plugin

> [`Plugin API`](../) / [`Plugin Types`](./)

API for Daemon plugin. ([MYSQL\_DAEMON\_PLUGIN](./#mysql_daemon_plugin))

## Classes

| Name                                                       | Description                                                                                                  |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [`st_mysql_daemon`](daemon_plugin_data.md#st_mysql_daemon) | The descriptor structure, that is referred from [st\_mysql\_plugin](../plugin_declaration/#st_mysql_plugin). |

## Macros

| Name                                                                                     | Description                                                 |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [`MYSQL_DAEMON_INTERFACE_VERSION`](daemon_plugin_data.md#mysql_daemon_interface_version) | daemon plugins of different MySQL releases are incompatible |

***

### MYSQL\_DAEMON\_INTERFACE\_VERSION

```cpp
#define MYSQL_DAEMON_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:782

daemon plugins of different MySQL releases are incompatible

## Class Definitions

### st\_mysql\_daemon

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_daemon
```

Defined in plugin.h:788

The descriptor structure, that is referred from [st\_mysql\_plugin](../plugin_declaration/#st_mysql_plugin).

#### Public Attributes

| Return | Name                                                           | Description |
| ------ | -------------------------------------------------------------- | ----------- |
| `int`  | [`interface_version`](daemon_plugin_data.md#interface_version) |             |

***

#### interface\_version

```cpp
int interface_version
```

Defined in plugin.h:790
