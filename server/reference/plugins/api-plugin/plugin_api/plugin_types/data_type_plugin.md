---
description: >-
  Plugin API reference: Data Type Plugin. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# Data Type Plugin

> [`Plugin API`](../) / [`Plugin Types`](./)

API for data type plugins. ([MariaDB\_DATA\_TYPE\_PLUGIN](./#mariadb_data_type_plugin))

## Classes

| Name                                                               | Description                 |
| ------------------------------------------------------------------ | --------------------------- |
| [`st_mariadb_data_type`](data_type_plugin.md#st_mariadb_data_type) | Data type plugin descriptor |

## Macros

| Name                                                                                             | Description                        |
| ------------------------------------------------------------------------------------------------ | ---------------------------------- |
| [`MariaDB_DATA_TYPE_INTERFACE_VERSION`](data_type_plugin.md#mariadb_data_type_interface_version) | Data type plugin interface version |

***

### MariaDB\_DATA\_TYPE\_INTERFACE\_VERSION

```cpp
#define MariaDB_DATA_TYPE_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin\_data\_type.h:40

Data type plugin interface version

## Class Definitions

### st\_mariadb\_data\_type

```cpp
#include <plugin_data_type.h>
```

```cpp
struct st_mariadb_data_type
```

Defined in plugin\_data\_type.h:46

Data type plugin descriptor

#### Public Attributes

| Return                 | Name                                                         | Description |
| ---------------------- | ------------------------------------------------------------ | ----------- |
| `int`                  | [`interface_version`](data_type_plugin.md#interface_version) |             |
| `class Type_handler *` | [`type_handler`](data_type_plugin.md#type_handler)           |             |

***

#### interface\_version

```cpp
int interface_version
```

Defined in plugin\_data\_type.h:48

***

#### type\_handler

```cpp
class Type_handler * type_handler
```

Defined in plugin\_data\_type.h:49
