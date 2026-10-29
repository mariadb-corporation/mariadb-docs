---
description: >-
  Plugin API reference: Plugin Status Variables. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin Status Variables

> [`Plugin API`](plugin_api.md) / [`Plugin Declaration`](plugin_declaration.md)

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_show_var`](#st_mysql_show_var) | Structure representing a SHOW STATUS variable in a plugin. |

## Macros

| Name | Description |
|------|-------------|
| [`SHOW_INT`](#show_int)  | Backward compatibility mapping to [SHOW_UINT](#enum_mysql_show_type) |
| [`SHOW_LONG`](#show_long)  | Backward compatibility mapping to [SHOW_ULONG](#enum_mysql_show_type) |
| [`SHOW_LONGLONG`](#show_longlong)  | Backward compatibility mapping to [SHOW_ULONGLONG](#enum_mysql_show_type) |
| [`SHOW_VAR_FUNC_BUFF_SIZE`](#show_var_func_buff_size)  |  |

---

### SHOW_INT

```cpp
#define SHOW_INT SHOW_UINT
```

Defined in plugin.h:272

Backward compatibility mapping to [SHOW_UINT](#enum_mysql_show_type)

---

### SHOW_LONG

```cpp
#define SHOW_LONG SHOW_ULONG
```

Defined in plugin.h:274

Backward compatibility mapping to [SHOW_ULONG](#enum_mysql_show_type)

---

### SHOW_LONGLONG

```cpp
#define SHOW_LONGLONG SHOW_ULONGLONG
```

Defined in plugin.h:276

Backward compatibility mapping to [SHOW_ULONGLONG](#enum_mysql_show_type)

---

### SHOW_VAR_FUNC_BUFF_SIZE

```cpp
#define SHOW_VAR_FUNC_BUFF_SIZE (256 * sizeof(void*))
```

Defined in plugin.h:298

## Enumerations

| Name | Description |
|------|-------------|
| [`enum_mysql_show_type`](#enum_mysql_show_type)  | declarations for SHOW STATUS support in plugins |
| [`enum_var_type`](#enum_var_type)  | SHOW STATUS scope |

---

### enum_mysql_show_type

```cpp
enum enum_mysql_show_type
```

Defined in plugin.h:251

declarations for SHOW STATUS support in plugins

| Value | Description |
|-------|-------------|
| `SHOW_UNDEF` | Internal only! |
| `SHOW_BOOL` | [my_bool](plugin_api.md#my_bool) |
| `SHOW_UINT` | `unsigned int` |
| `SHOW_ULONG` | `unsigned long` |
| `SHOW_ULONGLONG` | `unsigned long long` |
| `SHOW_CHAR` | `char *` |
| `SHOW_CHAR_PTR` | `char **` |
| `SHOW_ARRAY` | SHOW_VAR [] |
| `SHOW_FUNC` | **See also**: SHOW_FUNC_ENTRY |
| `SHOW_DOUBLE` | `double` |
| `SHOW_SINT` | `int` |
| `SHOW_SLONG` | `long` |
| `SHOW_SLONGLONG` | `long long` |
| `SHOW_SIMPLE_FUNC` | [mysql_show_var_func](#mysql_show_var_func) * |
| `SHOW_SIZE_T` | `size_t` |
| `SHOW_always_last` | Internal only! |

---

### enum_var_type

```cpp
enum enum_var_type
```

Defined in plugin.h:279

SHOW STATUS scope

| Value | Description |
|-------|-------------|
| `SHOW_OPT_DEFAULT` | Internal only! |
| `SHOW_OPT_SESSION` | Session scope |
| `SHOW_OPT_GLOBAL` | Global scope |
| `SHOW_OPT_SESSION_NO_LOCK` | Session scope without locking |
## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`mysql_show_var_func`](#mysql_show_var_func)  |  |

---

### mysql_show_var_func

```cpp
using mysql_show_var_func = int(*
```

Defined in plugin.h:299

## Functions

| Return | Name | Description |
|--------|------|-------------|
| struct [`st_mysql_show_var`](#st_mysql_show_var) | [`SHOW_FUNC_ENTRY`](#show_func_entry) `static` `inline` |  |

---

### SHOW_FUNC_ENTRY

`static` `inline`

```cpp
static inline struct st_mysql_show_var SHOW_FUNC_ENTRY(const char * name, mysql_show_var_func func_arg, const char * name, mysql_show_var_func func_arg)
```

Defined in plugin.h:303


## Class Definitions



### st_mysql_show_var

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_show_var
```

Defined in plugin.h:290

Structure representing a SHOW STATUS variable in a plugin.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const char *` | [`name`](#name)  |  |
| `void *` | [`value`](#value)  |  |
| enum [`enum_mysql_show_type`](#enum_mysql_show_type) | [`type`](#type)  |  |

---

#### name

```cpp
const char * name
```

Defined in plugin.h:291

---

#### value

```cpp
void * value
```

Defined in plugin.h:292

---

#### type

```cpp
enum enum_mysql_show_type type
```

Type: enum [`enum_mysql_show_type`](#enum_mysql_show_type)

Defined in plugin.h:293

