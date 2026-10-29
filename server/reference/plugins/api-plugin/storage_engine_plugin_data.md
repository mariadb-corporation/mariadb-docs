---
description: >-
  Plugin API reference: Storage Engine Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Storage Engine Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for Storage Engine plugin. ([MYSQL_STORAGE_ENGINE_PLUGIN](api.md#mysql_storage_engine_plugin))

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_xid`](#st_mysql_xid) | struct [st_mysql_xid](#st_mysql_xid) is binary compatible with the XID structure as in the X/Open CAE Specification, Distributed Transaction Processing: The XA Specification, X/Open Company Ltd., 1991. [http://www.opengroup.org/bookstore/catalog/c193.htm](http://www.opengroup.org/bookstore/catalog/c193.htm) |
| [`st_mysql_storage_engine`](#st_mysql_storage_engine) | The real API is in the sql/handler.h Here we define only the descriptor structure, that is referred from [st_mysql_plugin](plugin_declaration.md#st_mysql_plugin). |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_XIDDATASIZE`](#mysql_xiddatasize)  |  |
| [`MYSQL_HANDLERTON_INTERFACE_VERSION`](#mysql_handlerton_interface_version)  | storage engines of different MySQL releases are incompatible |

---

### MYSQL_XIDDATASIZE

```cpp
#define MYSQL_XIDDATASIZE 128
```

Defined in plugin.h:87

---

### MYSQL_HANDLERTON_INTERFACE_VERSION

```cpp
#define MYSQL_HANDLERTON_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:825

storage engines of different MySQL releases are incompatible

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| struct [`st_mysql_xid`](#st_mysql_xid) | [`MYSQL_XID`](#mysql_xid)  |  |

---

### MYSQL_XID

```cpp
using MYSQL_XID = struct st_mysql_xid
```

Type: struct [`st_mysql_xid`](#st_mysql_xid)

Defined in plugin.h:102


## Class Definitions



### st_mysql_xid

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_xid
```

Defined in plugin.h:96

struct [st_mysql_xid](#st_mysql_xid) is binary compatible with the XID structure as in the X/Open CAE Specification, Distributed Transaction Processing: The XA Specification, X/Open Company Ltd., 1991. [http://www.opengroup.org/bookstore/catalog/c193.htm](http://www.opengroup.org/bookstore/catalog/c193.htm)

**See also**: XID in sql/handler.h

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `long` | [`formatID`](#formatid)  |  |
| `long` | [`gtrid_length`](#gtrid_length)  |  |
| `long` | [`bqual_length`](#bqual_length)  |  |
| `char` | [`data`](#data)  |  |

---

#### formatID

```cpp
long formatID
```

Defined in plugin.h:97

---

#### gtrid_length

```cpp
long gtrid_length
```

Defined in plugin.h:98

---

#### bqual_length

```cpp
long bqual_length
```

Defined in plugin.h:99

---

#### data

```cpp
char data[MYSQL_XIDDATASIZE]
```

Defined in plugin.h:100



### st_mysql_storage_engine

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_storage_engine
```

Defined in plugin.h:833

The real API is in the sql/handler.h Here we define only the descriptor structure, that is referred from [st_mysql_plugin](plugin_declaration.md#st_mysql_plugin).

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in plugin.h:835

