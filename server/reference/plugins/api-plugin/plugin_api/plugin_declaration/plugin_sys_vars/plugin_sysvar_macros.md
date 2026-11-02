---
description: >-
  Plugin API reference: Plugin System Variable Macros. Generated from the
  MariaDB server headers by doxygen and moxygen.
---

# Plugin System Variable Macros

> [`Plugin API`](../../) / [`Plugin Declaration`](../) / [`Plugin System Variables`](./)

Macros for defining plugin system variables.

**See also**: [Define a Global Variable](../../../page-implementation.md#define-a-global-variable)

## Macros

| Name                                                                       | Description |
| -------------------------------------------------------------------------- | ----------- |
| [`MYSQL_SYSVAR_BOOL`](plugin_sysvar_macros.md#mysql_sysvar_bool)           |             |
| [`MYSQL_SYSVAR_STR`](plugin_sysvar_macros.md#mysql_sysvar_str)             |             |
| [`MYSQL_SYSVAR_CONST_STR`](plugin_sysvar_macros.md#mysql_sysvar_const_str) |             |
| [`MYSQL_SYSVAR_INT`](plugin_sysvar_macros.md#mysql_sysvar_int)             |             |
| [`MYSQL_SYSVAR_UINT`](plugin_sysvar_macros.md#mysql_sysvar_uint)           |             |
| [`MYSQL_SYSVAR_LONG`](plugin_sysvar_macros.md#mysql_sysvar_long)           |             |
| [`MYSQL_SYSVAR_ULONG`](plugin_sysvar_macros.md#mysql_sysvar_ulong)         |             |
| [`MYSQL_SYSVAR_LONGLONG`](plugin_sysvar_macros.md#mysql_sysvar_longlong)   |             |
| [`MYSQL_SYSVAR_ULONGLONG`](plugin_sysvar_macros.md#mysql_sysvar_ulonglong) |             |
| [`MYSQL_SYSVAR_UINT64_T`](plugin_sysvar_macros.md#mysql_sysvar_uint64_t)   |             |
| [`MYSQL_SYSVAR_SIZE_T`](plugin_sysvar_macros.md#mysql_sysvar_size_t)       |             |
| [`MYSQL_SYSVAR_ENUM`](plugin_sysvar_macros.md#mysql_sysvar_enum)           |             |
| [`MYSQL_SYSVAR_SET`](plugin_sysvar_macros.md#mysql_sysvar_set)             |             |
| [`MYSQL_SYSVAR_DOUBLE`](plugin_sysvar_macros.md#mysql_sysvar_double)       |             |

***

### MYSQL\_SYSVAR\_BOOL

```cpp
#define MYSQL_SYSVAR_BOOL(name, varname, opt, comment, check, update, def, name, varname, opt, comment, check, update, def) DECLARE_MYSQL_SYSVAR_BASIC(name, char) = { \
  PLUGIN_VAR_BOOL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def}
```

Defined in plugin.h:530

***

### MYSQL\_SYSVAR\_STR

```cpp
#define MYSQL_SYSVAR_STR(name, varname, opt, comment, check, update, def, name, varname, opt, comment, check, update, def) DECLARE_MYSQL_SYSVAR_BASIC(name, char *) = { \
  PLUGIN_VAR_STR | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def}
```

Defined in plugin.h:535

***

### MYSQL\_SYSVAR\_CONST\_STR

```cpp
#define MYSQL_SYSVAR_CONST_STR(name, varname, opt, comment, check, update, def, name, varname, opt, comment, check, update, def) DECLARE_MYSQL_SYSVAR_CONST_BASIC(name, char *) = { \
  PLUGIN_VAR_STR | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def}
```

Defined in plugin.h:540

***

### MYSQL\_SYSVAR\_INT

```cpp
#define MYSQL_SYSVAR_INT(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, int) = { \
  PLUGIN_VAR_INT | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:545

***

### MYSQL\_SYSVAR\_UINT

```cpp
#define MYSQL_SYSVAR_UINT(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, unsigned int) = { \
  PLUGIN_VAR_INT | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:550

***

### MYSQL\_SYSVAR\_LONG

```cpp
#define MYSQL_SYSVAR_LONG(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, long) = { \
  PLUGIN_VAR_LONG | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:555

***

### MYSQL\_SYSVAR\_ULONG

```cpp
#define MYSQL_SYSVAR_ULONG(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, unsigned long) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:560

***

### MYSQL\_SYSVAR\_LONGLONG

```cpp
#define MYSQL_SYSVAR_LONGLONG(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, long long) = { \
  PLUGIN_VAR_LONGLONG | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:565

***

### MYSQL\_SYSVAR\_ULONGLONG

```cpp
#define MYSQL_SYSVAR_ULONGLONG(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, unsigned long long) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:570

***

### MYSQL\_SYSVAR\_UINT64\_T

```cpp
#define MYSQL_SYSVAR_UINT64_T(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, uint64_t) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:575

***

### MYSQL\_SYSVAR\_SIZE\_T

```cpp
#define MYSQL_SYSVAR_SIZE_T(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, size_t) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:586

***

### MYSQL\_SYSVAR\_ENUM

```cpp
#define MYSQL_SYSVAR_ENUM(name, varname, opt, comment, check, update, def, typelib, name, varname, opt, comment, check, update, def, typelib) DECLARE_MYSQL_SYSVAR_TYPELIB(name, unsigned long) = { \
  PLUGIN_VAR_ENUM | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, typelib }
```

Defined in plugin.h:592

***

### MYSQL\_SYSVAR\_SET

```cpp
#define MYSQL_SYSVAR_SET(name, varname, opt, comment, check, update, def, typelib, name, varname, opt, comment, check, update, def, typelib) DECLARE_MYSQL_SYSVAR_TYPELIB(name, unsigned long long) = { \
  PLUGIN_VAR_SET | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, typelib }
```

Defined in plugin.h:597

***

### MYSQL\_SYSVAR\_DOUBLE

```cpp
#define MYSQL_SYSVAR_DOUBLE(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, double) = { \
  PLUGIN_VAR_DOUBLE | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:602
