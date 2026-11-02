---
description: >-
  Plugin API reference: Plugin Session-Local System Variable Macros. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin Session-Local System Variable Macros

> [`Plugin API`](plugin_api.md) / [`Plugin Declaration`](plugin_declaration.md) / [`Plugin System Variables`](plugin_sys_vars.md)

Macros for defining session-local plugin system variables.

**See also**: [Define a Session Variable](page-implementation.md#define-a-session-variable)

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_THDVAR_BOOL`](#mysql_thdvar_bool)  |  |
| [`MYSQL_THDVAR_STR`](#mysql_thdvar_str)  |  |
| [`MYSQL_THDVAR_INT`](#mysql_thdvar_int)  |  |
| [`MYSQL_THDVAR_UINT`](#mysql_thdvar_uint)  |  |
| [`MYSQL_THDVAR_LONG`](#mysql_thdvar_long)  |  |
| [`MYSQL_THDVAR_ULONG`](#mysql_thdvar_ulong)  |  |
| [`MYSQL_THDVAR_LONGLONG`](#mysql_thdvar_longlong)  |  |
| [`MYSQL_THDVAR_ULONGLONG`](#mysql_thdvar_ulonglong)  |  |
| [`MYSQL_THDVAR_ENUM`](#mysql_thdvar_enum)  |  |
| [`MYSQL_THDVAR_SET`](#mysql_thdvar_set)  |  |
| [`MYSQL_THDVAR_DOUBLE`](#mysql_thdvar_double)  |  |

---

### MYSQL_THDVAR_BOOL

```cpp
#define MYSQL_THDVAR_BOOL(name, opt, comment, check, update, def, name, opt, comment, check, update, def) DECLARE_MYSQL_THDVAR_BASIC(name, char) = { \
  PLUGIN_VAR_BOOL | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, NULL}
```

Defined in plugin.h:617

---

### MYSQL_THDVAR_STR

```cpp
#define MYSQL_THDVAR_STR(name, opt, comment, check, update, def, name, opt, comment, check, update, def) DECLARE_MYSQL_THDVAR_BASIC(name, char *) = { \
  PLUGIN_VAR_STR | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, NULL}
```

Defined in plugin.h:622

---

### MYSQL_THDVAR_INT

```cpp
#define MYSQL_THDVAR_INT(name, opt, comment, check, update, def, min, max, blk, name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, int) = { \
  PLUGIN_VAR_INT | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:627

---

### MYSQL_THDVAR_UINT

```cpp
#define MYSQL_THDVAR_UINT(name, opt, comment, check, update, def, min, max, blk, name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, unsigned int) = { \
  PLUGIN_VAR_INT | PLUGIN_VAR_THDLOCAL | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:632

---

### MYSQL_THDVAR_LONG

```cpp
#define MYSQL_THDVAR_LONG(name, opt, comment, check, update, def, min, max, blk, name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, long) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:637

---

### MYSQL_THDVAR_ULONG

```cpp
#define MYSQL_THDVAR_ULONG(name, opt, comment, check, update, def, min, max, blk, name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, unsigned long) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_THDLOCAL | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:642

---

### MYSQL_THDVAR_LONGLONG

```cpp
#define MYSQL_THDVAR_LONGLONG(name, opt, comment, check, update, def, min, max, blk, name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, long long) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:647

---

### MYSQL_THDVAR_ULONGLONG

```cpp
#define MYSQL_THDVAR_ULONGLONG(name, opt, comment, check, update, def, min, max, blk, name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, unsigned long long) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_THDLOCAL | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:652

---

### MYSQL_THDVAR_ENUM

```cpp
#define MYSQL_THDVAR_ENUM(name, opt, comment, check, update, def, typelib, name, opt, comment, check, update, def, typelib) DECLARE_MYSQL_THDVAR_TYPELIB(name, unsigned long) = { \
  PLUGIN_VAR_ENUM | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, NULL, typelib }
```

Defined in plugin.h:657

---

### MYSQL_THDVAR_SET

```cpp
#define MYSQL_THDVAR_SET(name, opt, comment, check, update, def, typelib, name, opt, comment, check, update, def, typelib) DECLARE_MYSQL_THDVAR_TYPELIB(name, unsigned long long) = { \
  PLUGIN_VAR_SET | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, NULL, typelib }
```

Defined in plugin.h:662

---

### MYSQL_THDVAR_DOUBLE

```cpp
#define MYSQL_THDVAR_DOUBLE(name, opt, comment, check, update, def, min, max, blk, name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, double) = { \
  PLUGIN_VAR_DOUBLE | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:667

