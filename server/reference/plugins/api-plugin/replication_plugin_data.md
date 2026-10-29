---
description: >-
  Plugin API reference: Replication Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Replication Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for Replication plugin. ([MYSQL_REPLICATION_PLUGIN](api.md#mysql_replication_plugin))

## Classes

| Name | Description |
|------|-------------|
| [`Mysql_replication`](#mysql_replication) | Replication plugin descriptor |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_REPLICATION_INTERFACE_VERSION`](#mysql_replication_interface_version)  |  |

---

### MYSQL_REPLICATION_INTERFACE_VERSION

```cpp
#define MYSQL_REPLICATION_INTERFACE_VERSION 0x0200
```

Defined in plugin.h:848


## Class Definitions



### Mysql_replication

```cpp
#include <plugin.h>
```

```cpp
struct Mysql_replication
```

Defined in plugin.h:853

Replication plugin descriptor

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in plugin.h:854

