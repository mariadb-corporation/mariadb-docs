---
description: >-
  Plugin API reference: Plugin System Variable Macros. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin System Variable Macros

> [`Plugin API`](plugin_api.md) / [`Plugin Declaration`](plugin_declaration.md) / [`Plugin System Variables`](plugin_sys_vars.md)

Macros for defining plugin system variables.

**See also**: [Define a Global Variable](page-implementation.md#define-a-global-variable)

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_SYSVAR_BOOL`](#mysql_sysvar_bool)  |  |
| [`MYSQL_SYSVAR_STR`](#mysql_sysvar_str)  |  |
| [`MYSQL_SYSVAR_CONST_STR`](#mysql_sysvar_const_str)  |  |
| [`MYSQL_SYSVAR_INT`](#mysql_sysvar_int)  |  |
| [`MYSQL_SYSVAR_UINT`](#mysql_sysvar_uint)  |  |
| [`MYSQL_SYSVAR_LONG`](#mysql_sysvar_long)  |  |
| [`MYSQL_SYSVAR_ULONG`](#mysql_sysvar_ulong)  |  |
| [`MYSQL_SYSVAR_LONGLONG`](#mysql_sysvar_longlong)  |  |
| [`MYSQL_SYSVAR_ULONGLONG`](#mysql_sysvar_ulonglong)  |  |
| [`MYSQL_SYSVAR_UINT64_T`](#mysql_sysvar_uint64_t)  |  |
| [`MYSQL_SYSVAR_SIZE_T`](#mysql_sysvar_size_t)  |  |
| [`MYSQL_SYSVAR_ENUM`](#mysql_sysvar_enum)  |  |
| [`MYSQL_SYSVAR_SET`](#mysql_sysvar_set)  |  |
| [`MYSQL_SYSVAR_DOUBLE`](#mysql_sysvar_double)  |  |

---

### MYSQL_SYSVAR_BOOL

```cpp
#define MYSQL_SYSVAR_BOOL(name, varname, opt, comment, check, update, def, name, varname, opt, comment, check, update, def) DECLARE_MYSQL_SYSVAR_BASIC(name, char) = { \
  PLUGIN_VAR_BOOL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def}
```

Defined in plugin.h:530

---

### MYSQL_SYSVAR_STR

```cpp
#define MYSQL_SYSVAR_STR(name, varname, opt, comment, check, update, def, name, varname, opt, comment, check, update, def) DECLARE_MYSQL_SYSVAR_BASIC(name, char *) = { \
  PLUGIN_VAR_STR | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def}
```

Defined in plugin.h:535

---

### MYSQL_SYSVAR_CONST_STR

```cpp
#define MYSQL_SYSVAR_CONST_STR(name, varname, opt, comment, check, update, def, name, varname, opt, comment, check, update, def) DECLARE_MYSQL_SYSVAR_CONST_BASIC(name, char *) = { \
  PLUGIN_VAR_STR | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def}
```

Defined in plugin.h:540

---

### MYSQL_SYSVAR_INT

```cpp
#define MYSQL_SYSVAR_INT(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, int) = { \
  PLUGIN_VAR_INT | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:545

---

### MYSQL_SYSVAR_UINT

```cpp
#define MYSQL_SYSVAR_UINT(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, unsigned int) = { \
  PLUGIN_VAR_INT | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:550

---

### MYSQL_SYSVAR_LONG

```cpp
#define MYSQL_SYSVAR_LONG(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, long) = { \
  PLUGIN_VAR_LONG | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:555

---

### MYSQL_SYSVAR_ULONG

```cpp
#define MYSQL_SYSVAR_ULONG(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, unsigned long) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:560

---

### MYSQL_SYSVAR_LONGLONG

```cpp
#define MYSQL_SYSVAR_LONGLONG(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, long long) = { \
  PLUGIN_VAR_LONGLONG | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:565

---

### MYSQL_SYSVAR_ULONGLONG

```cpp
#define MYSQL_SYSVAR_ULONGLONG(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, unsigned long long) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:570

---

### MYSQL_SYSVAR_UINT64_T

```cpp
#define MYSQL_SYSVAR_UINT64_T(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, uint64_t) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:575

---

### MYSQL_SYSVAR_SIZE_T

```cpp
#define MYSQL_SYSVAR_SIZE_T(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, size_t) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:586

---

### MYSQL_SYSVAR_ENUM

```cpp
#define MYSQL_SYSVAR_ENUM(name, varname, opt, comment, check, update, def, typelib, name, varname, opt, comment, check, update, def, typelib) DECLARE_MYSQL_SYSVAR_TYPELIB(name, unsigned long) = { \
  PLUGIN_VAR_ENUM | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, typelib }
```

Defined in plugin.h:592

---

### MYSQL_SYSVAR_SET

```cpp
#define MYSQL_SYSVAR_SET(name, varname, opt, comment, check, update, def, typelib, name, varname, opt, comment, check, update, def, typelib) DECLARE_MYSQL_SYSVAR_TYPELIB(name, unsigned long long) = { \
  PLUGIN_VAR_SET | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, typelib }
```

Defined in plugin.h:597

---

### MYSQL_SYSVAR_DOUBLE

```cpp
#define MYSQL_SYSVAR_DOUBLE(name, varname, opt, comment, check, update, def, min, max, blk, name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, double) = { \
  PLUGIN_VAR_DOUBLE | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:602

