---
description: >-
  Plugin API reference: Plugin System Variable Types. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# Plugin System Variable Types

> [`Plugin API`](../../) / [`Plugin Declaration`](../) / [`Plugin System Variables`](./)

A list of the plugin system variable types.

For each data type there's a corresponding C++ native data type and a macro to define the system variable of that type in [Plugin System Variable Macros](plugin_sysvar_macros.md) (for global variables) or [Plugin Session-Local System Variable Macros](plugin_thdvar_macros.md) (for session-local variables).

**See also**: [Plugin System Variables Implementation](../../../page-implementation.md#plugin-system-variables-implementation)

## Macros

| Name                                                                | Description                                                                                                |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [`PLUGIN_VAR_BOOL`](plugin_sysvar_types.md#plugin_var_bool)         | [my\_bool](../../#my_bool). **See also**: [MYSQL\_SYSVAR\_BOOL](plugin_sysvar_macros.md#mysql_sysvar_bool) |
| [`PLUGIN_VAR_INT`](plugin_sysvar_types.md#plugin_var_int)           | `int`. **See also**: [MYSQL\_SYSVAR\_INT](plugin_sysvar_macros.md#mysql_sysvar_int)                        |
| [`PLUGIN_VAR_LONG`](plugin_sysvar_types.md#plugin_var_long)         | `long`. **See also**: [MYSQL\_SYSVAR\_LONG](plugin_sysvar_macros.md#mysql_sysvar_long)                     |
| [`PLUGIN_VAR_LONGLONG`](plugin_sysvar_types.md#plugin_var_longlong) | `long long`. **See also**: [MYSQL\_SYSVAR\_LONGLONG](plugin_sysvar_macros.md#mysql_sysvar_longlong)        |
| [`PLUGIN_VAR_STR`](plugin_sysvar_types.md#plugin_var_str)           | `char*`. **See also**: [MYSQL\_SYSVAR\_STR](plugin_sysvar_macros.md#mysql_sysvar_str)                      |
| [`PLUGIN_VAR_ENUM`](plugin_sysvar_types.md#plugin_var_enum)         | `unsigned long`. **See also**: [MYSQL\_SYSVAR\_ENUM](plugin_sysvar_macros.md#mysql_sysvar_enum)            |
| [`PLUGIN_VAR_SET`](plugin_sysvar_types.md#plugin_var_set)           | `unsigned long long`. **See also**: [MYSQL\_SYSVAR\_SET](plugin_sysvar_macros.md#mysql_sysvar_set)         |
| [`PLUGIN_VAR_DOUBLE`](plugin_sysvar_types.md#plugin_var_double)     | `double`. **See also**: [MYSQL\_SYSVAR\_DOUBLE](plugin_sysvar_macros.md#mysql_sysvar_double)               |

***

### PLUGIN\_VAR\_BOOL

```cpp
#define PLUGIN_VAR_BOOL 0x0001
```

Defined in plugin.h:353

[my\_bool](../../#my_bool). **See also**: [MYSQL\_SYSVAR\_BOOL](plugin_sysvar_macros.md#mysql_sysvar_bool)

***

### PLUGIN\_VAR\_INT

```cpp
#define PLUGIN_VAR_INT 0x0002
```

Defined in plugin.h:354

`int`. **See also**: [MYSQL\_SYSVAR\_INT](plugin_sysvar_macros.md#mysql_sysvar_int)

***

### PLUGIN\_VAR\_LONG

```cpp
#define PLUGIN_VAR_LONG 0x0003
```

Defined in plugin.h:355

`long`. **See also**: [MYSQL\_SYSVAR\_LONG](plugin_sysvar_macros.md#mysql_sysvar_long)

***

### PLUGIN\_VAR\_LONGLONG

```cpp
#define PLUGIN_VAR_LONGLONG 0x0004
```

Defined in plugin.h:356

`long long`. **See also**: [MYSQL\_SYSVAR\_LONGLONG](plugin_sysvar_macros.md#mysql_sysvar_longlong)

***

### PLUGIN\_VAR\_STR

```cpp
#define PLUGIN_VAR_STR 0x0005
```

Defined in plugin.h:357

`char*`. **See also**: [MYSQL\_SYSVAR\_STR](plugin_sysvar_macros.md#mysql_sysvar_str)

***

### PLUGIN\_VAR\_ENUM

```cpp
#define PLUGIN_VAR_ENUM 0x0006
```

Defined in plugin.h:358

`unsigned long`. **See also**: [MYSQL\_SYSVAR\_ENUM](plugin_sysvar_macros.md#mysql_sysvar_enum)

***

### PLUGIN\_VAR\_SET

```cpp
#define PLUGIN_VAR_SET 0x0007
```

Defined in plugin.h:359

`unsigned long long`. **See also**: [MYSQL\_SYSVAR\_SET](plugin_sysvar_macros.md#mysql_sysvar_set)

***

### PLUGIN\_VAR\_DOUBLE

```cpp
#define PLUGIN_VAR_DOUBLE 0x0008
```

Defined in plugin.h:360

`double`. **See also**: [MYSQL\_SYSVAR\_DOUBLE](plugin_sysvar_macros.md#mysql_sysvar_double)
