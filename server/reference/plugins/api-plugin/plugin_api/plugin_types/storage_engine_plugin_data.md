---
description: >-
  Plugin API reference: Storage Engine Plugin. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# Storage Engine Plugin

> [`Plugin API`](../) / [`Plugin Types`](./)

API for Storage Engine plugin. ([MYSQL\_STORAGE\_ENGINE\_PLUGIN](./#mysql_storage_engine_plugin))

## Classes

| Name                                                                               | Description                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`st_mysql_xid`](storage_engine_plugin_data.md#st_mysql_xid)                       | struct [st\_mysql\_xid](storage_engine_plugin_data.md#st_mysql_xid) is binary compatible with the XID structure as in the X/Open CAE Specification, Distributed Transaction Processing: The XA Specification, X/Open Company Ltd., 1991. [http://www.opengroup.org/bookstore/catalog/c193.htm](http://www.opengroup.org/bookstore/catalog/c193.htm) |
| [`st_mysql_storage_engine`](storage_engine_plugin_data.md#st_mysql_storage_engine) | The real API is in the sql/handler.h Here we define only the descriptor structure, that is referred from [st\_mysql\_plugin](../plugin_declaration/#st_mysql_plugin).                                                                                                                                                                               |

## Macros

| Name                                                                                                     | Description                                                  |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| [`MYSQL_XIDDATASIZE`](storage_engine_plugin_data.md#mysql_xiddatasize)                                   |                                                              |
| [`MYSQL_HANDLERTON_INTERFACE_VERSION`](storage_engine_plugin_data.md#mysql_handlerton_interface_version) | storage engines of different MySQL releases are incompatible |

***

### MYSQL\_XIDDATASIZE

```cpp
#define MYSQL_XIDDATASIZE 128
```

Defined in plugin.h:87

***

### MYSQL\_HANDLERTON\_INTERFACE\_VERSION

```cpp
#define MYSQL_HANDLERTON_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:825

storage engines of different MySQL releases are incompatible

## Typedefs

| Return                                                              | Name                                                   | Description |
| ------------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| struct [`st_mysql_xid`](storage_engine_plugin_data.md#st_mysql_xid) | [`MYSQL_XID`](storage_engine_plugin_data.md#mysql_xid) |             |

***

### MYSQL\_XID

```cpp
using MYSQL_XID = struct st_mysql_xid
```

Type: struct [`st_mysql_xid`](storage_engine_plugin_data.md#st_mysql_xid)

Defined in plugin.h:102

## Class Definitions

### st\_mysql\_xid

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_xid
```

Defined in plugin.h:96

struct [st\_mysql\_xid](storage_engine_plugin_data.md#st_mysql_xid) is binary compatible with the XID structure as in the X/Open CAE Specification, Distributed Transaction Processing: The XA Specification, X/Open Company Ltd., 1991. [http://www.opengroup.org/bookstore/catalog/c193.htm](http://www.opengroup.org/bookstore/catalog/c193.htm)

**See also**: XID in sql/handler.h

#### Public Attributes

| Return | Name                                                         | Description |
| ------ | ------------------------------------------------------------ | ----------- |
| `long` | [`formatID`](storage_engine_plugin_data.md#formatid)         |             |
| `long` | [`gtrid_length`](storage_engine_plugin_data.md#gtrid_length) |             |
| `long` | [`bqual_length`](storage_engine_plugin_data.md#bqual_length) |             |
| `char` | [`data`](storage_engine_plugin_data.md#data)                 |             |

***

#### formatID

```cpp
long formatID
```

Defined in plugin.h:97

***

#### gtrid\_length

```cpp
long gtrid_length
```

Defined in plugin.h:98

***

#### bqual\_length

```cpp
long bqual_length
```

Defined in plugin.h:99

***

#### data

```cpp
char data[MYSQL_XIDDATASIZE]
```

Defined in plugin.h:100

### st\_mysql\_storage\_engine

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_storage_engine
```

Defined in plugin.h:833

The real API is in the sql/handler.h Here we define only the descriptor structure, that is referred from [st\_mysql\_plugin](../plugin_declaration/#st_mysql_plugin).

#### Public Attributes

| Return | Name                                                                   | Description |
| ------ | ---------------------------------------------------------------------- | ----------- |
| `int`  | [`interface_version`](storage_engine_plugin_data.md#interface_version) |             |

***

#### interface\_version

```cpp
int interface_version
```

Defined in plugin.h:835
