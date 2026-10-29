---
description: >-
  Plugin API reference: Daemon Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Daemon Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for Daemon plugin. ([MYSQL_DAEMON_PLUGIN](api.md#mysql_daemon_plugin))

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_daemon`](#st_mysql_daemon) | The descriptor structure, that is referred from [st_mysql_plugin](plugin_declaration.md#st_mysql_plugin). |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_DAEMON_INTERFACE_VERSION`](#mysql_daemon_interface_version)  | daemon plugins of different MySQL releases are incompatible |

---

### MYSQL_DAEMON_INTERFACE_VERSION

```cpp
#define MYSQL_DAEMON_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:782

daemon plugins of different MySQL releases are incompatible


## Class Definitions



### st_mysql_daemon

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_daemon
```

Defined in plugin.h:788

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

Defined in plugin.h:790

