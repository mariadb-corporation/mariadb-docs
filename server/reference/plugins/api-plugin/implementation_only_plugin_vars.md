---
description: >-
  Plugin API reference: Implementation-Only Code for Plugin System Variables. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Implementation-Only Code for Plugin System Variables

> [`Plugin API`](plugin_api.md) / [`Plugin Declaration`](plugin_declaration.md) / [`Plugin System Variables`](plugin_sys_vars.md)

The following declarations are utilities to implement plugin system variables API. Do not use directly in plugin code.

## Macros

| Name | Description |
|------|-------------|
| [`PLUGIN_VAR_MASK`](#plugin_var_mask)  |  |
| [`MYSQL_PLUGIN_VAR_HEADER`](#mysql_plugin_var_header)  |  |
| [`MYSQL_SYSVAR_NAME`](#mysql_sysvar_name)  |  |
| [`MYSQL_SYSVAR`](#mysql_sysvar)  |  |
| [`DECLARE_MYSQL_SYSVAR_BASIC`](#declare_mysql_sysvar_basic)  |  |
| [`DECLARE_MYSQL_SYSVAR_CONST_BASIC`](#declare_mysql_sysvar_const_basic)  |  |
| [`DECLARE_MYSQL_SYSVAR_SIMPLE`](#declare_mysql_sysvar_simple)  |  |
| [`DECLARE_MYSQL_SYSVAR_TYPELIB`](#declare_mysql_sysvar_typelib)  |  |
| [`DECLARE_THDVAR_FUNC`](#declare_thdvar_func)  |  |
| [`DECLARE_MYSQL_THDVAR_BASIC`](#declare_mysql_thdvar_basic)  |  |
| [`DECLARE_MYSQL_THDVAR_SIMPLE`](#declare_mysql_thdvar_simple)  |  |
| [`DECLARE_MYSQL_THDVAR_TYPELIB`](#declare_mysql_thdvar_typelib)  |  |

---

### PLUGIN_VAR_MASK

```cpp
#define PLUGIN_VAR_MASK (PLUGIN_VAR_READONLY | PLUGIN_VAR_NOSYSVAR | \
         PLUGIN_VAR_NOCMDOPT | PLUGIN_VAR_NOCMDARG | \
         PLUGIN_VAR_OPCMDARG | PLUGIN_VAR_RQCMDARG | \
         PLUGIN_VAR_DEPRECATED | PLUGIN_VAR_MEMALLOC)
```

Defined in plugin.h:444

---

### MYSQL_PLUGIN_VAR_HEADER

```cpp
#define MYSQL_PLUGIN_VAR_HEADER int flags;                    \
  const char *name;             \
  const char *comment;          \
  mysql_var_check_func check;   \
  mysql_var_update_func update
```

Defined in plugin.h:450

---

### MYSQL_SYSVAR_NAME

```cpp
#define MYSQL_SYSVAR_NAME(name, name) mysql_sysvar_ ## name
```

Defined in plugin.h:457

---

### MYSQL_SYSVAR

```cpp
#define MYSQL_SYSVAR(name, name) ((struct st_mysql_sys_var *)&(MYSQL_SYSVAR_NAME(name)))
```

Defined in plugin.h:458

---

### DECLARE_MYSQL_SYSVAR_BASIC

```cpp
#define DECLARE_MYSQL_SYSVAR_BASIC(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  type *value;                  \
  const type def_val;                 \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:469

---

### DECLARE_MYSQL_SYSVAR_CONST_BASIC

```cpp
#define DECLARE_MYSQL_SYSVAR_CONST_BASIC(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  const type *value;                  \
  const type def_val;                 \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:475

---

### DECLARE_MYSQL_SYSVAR_SIMPLE

```cpp
#define DECLARE_MYSQL_SYSVAR_SIMPLE(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  type *value; type def_val;    \
  type min_val; type max_val;   \
  type blk_sz;                  \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:481

---

### DECLARE_MYSQL_SYSVAR_TYPELIB

```cpp
#define DECLARE_MYSQL_SYSVAR_TYPELIB(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  type *value; type def_val;    \
  TYPELIB *typelib;             \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:488

---

### DECLARE_THDVAR_FUNC

```cpp
#define DECLARE_THDVAR_FUNC(type, type) type *(*resolve)(MYSQL_THD thd, int offset)
```

Defined in plugin.h:494

---

### DECLARE_MYSQL_THDVAR_BASIC

```cpp
#define DECLARE_MYSQL_THDVAR_BASIC(name, type, name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  int offset;                   \
  const type def_val;           \
  DECLARE_THDVAR_FUNC(type);    \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:497

---

### DECLARE_MYSQL_THDVAR_SIMPLE

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

---

### DECLARE_MYSQL_THDVAR_TYPELIB

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

