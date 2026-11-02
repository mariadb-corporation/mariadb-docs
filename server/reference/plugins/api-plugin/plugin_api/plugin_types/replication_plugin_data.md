---
description: >-
  Plugin API reference: Replication Plugin. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# Replication Plugin

> [`Plugin API`](../) / [`Plugin Types`](./)

API for Replication plugin. ([MYSQL\_REPLICATION\_PLUGIN](./#mysql_replication_plugin))

## Classes

| Name                                                                | Description                   |
| ------------------------------------------------------------------- | ----------------------------- |
| [`Mysql_replication`](replication_plugin_data.md#mysql_replication) | Replication plugin descriptor |

## Macros

| Name                                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------- | ----------- |
| [`MYSQL_REPLICATION_INTERFACE_VERSION`](replication_plugin_data.md#mysql_replication_interface_version) |             |

***

### MYSQL\_REPLICATION\_INTERFACE\_VERSION

```cpp
#define MYSQL_REPLICATION_INTERFACE_VERSION 0x0200
```

Defined in plugin.h:848

## Class Definitions

### Mysql\_replication

```cpp
#include <plugin.h>
```

```cpp
struct Mysql_replication
```

Defined in plugin.h:853

Replication plugin descriptor

#### Public Attributes

| Return | Name                                                                | Description |
| ------ | ------------------------------------------------------------------- | ----------- |
| `int`  | [`interface_version`](replication_plugin_data.md#interface_version) |             |

***

#### interface\_version

```cpp
int interface_version
```

Defined in plugin.h:854
