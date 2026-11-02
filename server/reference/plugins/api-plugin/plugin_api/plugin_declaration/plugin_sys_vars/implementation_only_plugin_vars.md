---
description: >-
  Plugin API reference: Implementation-Only Code for Plugin System Variables.
  Generated from the MariaDB server headers by doxygen and moxygen.
---

# Implementation-Only Code for Plugin System Variables

> [`Plugin API`](../../) / [`Plugin Declaration`](../) / [`Plugin System Variables`](./)

The following declarations are utilities to implement plugin system variables API. Do not use directly in plugin code.

## Macros

| Name                                                                                                      | Description |
| --------------------------------------------------------------------------------------------------------- | ----------- |
| [`PLUGIN_VAR_MASK`](implementation_only_plugin_vars.md#plugin_var_mask)                                   |             |
| [`MYSQL_PLUGIN_VAR_HEADER`](implementation_only_plugin_vars.md#mysql_plugin_var_header)                   |             |
| [`MYSQL_SYSVAR_NAME`](implementation_only_plugin_vars.md#mysql_sysvar_name)                               |             |
| [`MYSQL_SYSVAR`](implementation_only_plugin_vars.md#mysql_sysvar)                                         |             |
| [`DECLARE_MYSQL_SYSVAR_BASIC`](implementation_only_plugin_vars.md#declare_mysql_sysvar_basic)             |             |
| [`DECLARE_MYSQL_SYSVAR_CONST_BASIC`](implementation_only_plugin_vars.md#declare_mysql_sysvar_const_basic) |             |
| [`DECLARE_MYSQL_SYSVAR_SIMPLE`](implementation_only_plugin_vars.md#declare_mysql_sysvar_simple)           |             |
| [`DECLARE_MYSQL_SYSVAR_TYPELIB`](implementation_only_plugin_vars.md#declare_mysql_sysvar_typelib)         |             |
| [`DECLARE_THDVAR_FUNC`](implementation_only_plugin_vars.md#declare_thdvar_func)                           |             |
| [`DECLARE_MYSQL_THDVAR_BASIC`](implementation_only_plugin_vars.md#declare_mysql_thdvar_basic)             |             |
| [`DECLARE_MYSQL_THDVAR_SIMPLE`](implementation_only_plugin_vars.md#declare_mysql_thdvar_simple)           |             |
| [`DECLARE_MYSQL_THDVAR_TYPELIB`](implementation_only_plugin_vars.md#declare_mysql_thdvar_typelib)         |             |

***

### PLUGIN\_VAR\_MASK

```cpp
#define PLUGIN_VAR_MASK (PLUGIN_VAR_READONLY | PLUGIN_VAR_NOSYSVAR | \
         PLUGIN_VAR_NOCMDOPT | PLUGIN_VAR_NOCMDARG | \
         PLUGIN_VAR_OPCMDARG | PLUGIN_VAR_RQCMDARG | \
         PLUGIN_VAR_DEPRECATED | PLUGIN_VAR_MEMALLOC)
```

Defined in plugin.h:444

***

### MYSQL\_PLUGIN\_VAR\_HEADER

```cpp
#define MYSQL_PLUGIN_VAR_HEADER int flags;                    \
  const char *name;             \
  const char *comment;          \
  mysql_var_check_func check;   \
  mysql_var_update_func update
```

Defined in plugin.h:450

***

### MYSQL\_SYSVAR\_NAME

```cpp
#define MYSQL_SYSVAR_NAME(name, name) mysql_sysvar_ ## name
```

Defined in plugin.h:457

***

### MYSQL\_SYSVAR

```cpp
#define MYSQL_SYSVAR(name, name) ((struct st_mysql_sys_var *)&(MYSQL_SYSVAR_NAME(name)))
```

Defined in plugin.h:458

***

### DECLARE\_MYSQL\_SYSVAR\_BASIC

```cpp
#define DECLARE_MYSQL_SYSVAR_BASIC(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  type *value;                  \
  const type def_val;                 \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:469

***

### DECLARE\_MYSQL\_SYSVAR\_CONST\_BASIC

```cpp
#define DECLARE_MYSQL_SYSVAR_CONST_BASIC(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  const type *value;                  \
  const type def_val;                 \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:475

***

### DECLARE\_MYSQL\_SYSVAR\_SIMPLE

```cpp
#define DECLARE_MYSQL_SYSVAR_SIMPLE(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  type *value; type def_val;    \
  type min_val; type max_val;   \
  type blk_sz;                  \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:481

***

### DECLARE\_MYSQL\_SYSVAR\_TYPELIB

```cpp
#define DECLARE_MYSQL_SYSVAR_TYPELIB(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  type *value; type def_val;    \
  TYPELIB *typelib;             \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:488

***

### DECLARE\_THDVAR\_FUNC

```cpp
#define DECLARE_THDVAR_FUNC(type, type) type *(*resolve)(MYSQL_THD thd, int offset)
```

Defined in plugin.h:494

***

### DECLARE\_MYSQL\_THDVAR\_BASIC

```cpp
#define DECLARE_MYSQL_THDVAR_BASIC(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  int offset;                   \
  const type def_val;           \
  DECLARE_THDVAR_FUNC(type);    \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:497

***

### DECLARE\_MYSQL\_THDVAR\_SIMPLE

```cpp
#define DECLARE_MYSQL_THDVAR_SIMPLE(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  int offset;                   \
  type def_val; type min_val;   \
  type max_val; type blk_sz;    \
  DECLARE_THDVAR_FUNC(type);    \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:504

***

### DECLARE\_MYSQL\_THDVAR\_TYPELIB

```cpp
#define DECLARE_MYSQL_THDVAR_TYPELIB(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  int offset;                   \
  const type def_val;           \
  DECLARE_THDVAR_FUNC(type);    \
  TYPELIB *typelib;             \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:512
