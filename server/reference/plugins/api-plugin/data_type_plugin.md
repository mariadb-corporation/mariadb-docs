---
description: >-
  Plugin API reference: Data Type Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Data Type Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for data type plugins. ([MariaDB_DATA_TYPE_PLUGIN](api.md#mariadb_data_type_plugin))

## Classes

| Name | Description |
|------|-------------|
| [`st_mariadb_data_type`](#st_mariadb_data_type) | Data type plugin descriptor |

## Macros

| Name | Description |
|------|-------------|
| [`MariaDB_DATA_TYPE_INTERFACE_VERSION`](#mariadb_data_type_interface_version)  | Data type plugin interface version |

---

### MariaDB_DATA_TYPE_INTERFACE_VERSION

```cpp
#define MariaDB_DATA_TYPE_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin_data_type.h:40

Data type plugin interface version


## Class Definitions



### st_mariadb_data_type

```cpp
#include <plugin_data_type.h>
```

```cpp
struct st_mariadb_data_type
```

Defined in plugin_data_type.h:46

Data type plugin descriptor

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version)  |  |
| `class Type_handler *` | [`type_handler`](#type_handler)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in plugin_data_type.h:48

---

#### type_handler

```cpp
class Type_handler * type_handler
```

Defined in plugin_data_type.h:49

