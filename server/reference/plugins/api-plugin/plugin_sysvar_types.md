---
description: >-
  Plugin API reference: Plugin System Variable Types. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin System Variable Types

> [`Plugin API`](plugin_api.md) / [`Plugin Declaration`](plugin_declaration.md) / [`Plugin System Variables`](plugin_sys_vars.md)

A list of the plugin system variable types.

For each data type there's a corresponding C++ native data type and a macro to define the system variable of that type in [Plugin System Variable Macros](plugin_sysvar_macros.md) (for global variables) or [Plugin Session-Local System Variable Macros](plugin_thdvar_macros.md) (for session-local variables).

**See also**: [Plugin System Variables Implementation](page-implementation.md#plugin-system-variables-implementation)

## Macros

| Name | Description |
|------|-------------|
| [`PLUGIN_VAR_BOOL`](#plugin_var_bool)  | [my_bool](api.md#my_bool). **See also**: [MYSQL_SYSVAR_BOOL](api.md#mysql_sysvar_bool) |
| [`PLUGIN_VAR_INT`](#plugin_var_int)  | `int`. **See also**: [MYSQL_SYSVAR_INT](api.md#mysql_sysvar_int) |
| [`PLUGIN_VAR_LONG`](#plugin_var_long)  | `long`. **See also**: [MYSQL_SYSVAR_LONG](api.md#mysql_sysvar_long) |
| [`PLUGIN_VAR_LONGLONG`](#plugin_var_longlong)  | `long long`. **See also**: [MYSQL_SYSVAR_LONGLONG](api.md#mysql_sysvar_longlong) |
| [`PLUGIN_VAR_STR`](#plugin_var_str)  | `char*`. **See also**: [MYSQL_SYSVAR_STR](api.md#mysql_sysvar_str) |
| [`PLUGIN_VAR_ENUM`](#plugin_var_enum)  | `unsigned long`. **See also**: [MYSQL_SYSVAR_ENUM](api.md#mysql_sysvar_enum) |
| [`PLUGIN_VAR_SET`](#plugin_var_set)  | `unsigned long long`. **See also**: [MYSQL_SYSVAR_SET](api.md#mysql_sysvar_set) |
| [`PLUGIN_VAR_DOUBLE`](#plugin_var_double)  | `double`. **See also**: [MYSQL_SYSVAR_DOUBLE](api.md#mysql_sysvar_double) |

---

### PLUGIN_VAR_BOOL

```cpp
#define PLUGIN_VAR_BOOL 0x0001
```

Defined in plugin.h:353

[my_bool](api.md#my_bool). **See also**: [MYSQL_SYSVAR_BOOL](api.md#mysql_sysvar_bool)

---

### PLUGIN_VAR_INT

```cpp
#define PLUGIN_VAR_INT 0x0002
```

Defined in plugin.h:354

`int`. **See also**: [MYSQL_SYSVAR_INT](api.md#mysql_sysvar_int)

---

### PLUGIN_VAR_LONG

```cpp
#define PLUGIN_VAR_LONG 0x0003
```

Defined in plugin.h:355

`long`. **See also**: [MYSQL_SYSVAR_LONG](api.md#mysql_sysvar_long)

---

### PLUGIN_VAR_LONGLONG

```cpp
#define PLUGIN_VAR_LONGLONG 0x0004
```

Defined in plugin.h:356

`long long`. **See also**: [MYSQL_SYSVAR_LONGLONG](api.md#mysql_sysvar_longlong)

---

### PLUGIN_VAR_STR

```cpp
#define PLUGIN_VAR_STR 0x0005
```

Defined in plugin.h:357

`char*`. **See also**: [MYSQL_SYSVAR_STR](api.md#mysql_sysvar_str)

---

### PLUGIN_VAR_ENUM

```cpp
#define PLUGIN_VAR_ENUM 0x0006
```

Defined in plugin.h:358

`unsigned long`. **See also**: [MYSQL_SYSVAR_ENUM](api.md#mysql_sysvar_enum)

---

### PLUGIN_VAR_SET

```cpp
#define PLUGIN_VAR_SET 0x0007
```

Defined in plugin.h:359

`unsigned long long`. **See also**: [MYSQL_SYSVAR_SET](api.md#mysql_sysvar_set)

---

### PLUGIN_VAR_DOUBLE

```cpp
#define PLUGIN_VAR_DOUBLE 0x0008
```

Defined in plugin.h:360

`double`. **See also**: [MYSQL_SYSVAR_DOUBLE](api.md#mysql_sysvar_double)

