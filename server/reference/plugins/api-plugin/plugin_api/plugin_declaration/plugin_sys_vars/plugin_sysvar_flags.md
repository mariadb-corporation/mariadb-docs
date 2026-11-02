---
description: >-
  Plugin API reference: Plugin System Variable Flags. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# Plugin System Variable Flags

> [`Plugin API`](../../) / [`Plugin Declaration`](../) / [`Plugin System Variables`](./)

Flags for plugin system variables.

## Macros

| Name                                                                    | Description                                                                                                                                                                                                        |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`PLUGIN_VAR_UNSIGNED`](plugin_sysvar_flags.md#plugin_var_unsigned)     | Unsigned modifier for [PLUGIN\_VAR\_INT](plugin_sysvar_types.md#plugin_var_int), [PLUGIN\_VAR\_LONG](plugin_sysvar_types.md#plugin_var_long), [PLUGIN\_VAR\_LONGLONG](plugin_sysvar_types.md#plugin_var_longlong). |
| [`PLUGIN_VAR_THDLOCAL`](plugin_sysvar_flags.md#plugin_var_thdlocal)     | Variable is per-connection. Do not use directly!                                                                                                                                                                   |
| [`PLUGIN_VAR_READONLY`](plugin_sysvar_flags.md#plugin_var_readonly)     | Server variable is read only                                                                                                                                                                                       |
| [`PLUGIN_VAR_NOSYSVAR`](plugin_sysvar_flags.md#plugin_var_nosysvar)     | Not a server variable. Only a command line option                                                                                                                                                                  |
| [`PLUGIN_VAR_NOCMDOPT`](plugin_sysvar_flags.md#plugin_var_nocmdopt)     | Not a command line option. Only a system variable                                                                                                                                                                  |
| [`PLUGIN_VAR_NOCMDARG`](plugin_sysvar_flags.md#plugin_var_nocmdarg)     | No argument for cmd line                                                                                                                                                                                           |
| [`PLUGIN_VAR_RQCMDARG`](plugin_sysvar_flags.md#plugin_var_rqcmdarg)     | Argument required for cmd line                                                                                                                                                                                     |
| [`PLUGIN_VAR_OPCMDARG`](plugin_sysvar_flags.md#plugin_var_opcmdarg)     | Argument optional for cmd line                                                                                                                                                                                     |
| [`PLUGIN_VAR_DEPRECATED`](plugin_sysvar_flags.md#plugin_var_deprecated) | Server variable is deprecated                                                                                                                                                                                      |
| [`PLUGIN_VAR_MEMALLOC`](plugin_sysvar_flags.md#plugin_var_memalloc)     | String needs memory allocated                                                                                                                                                                                      |

***

### PLUGIN\_VAR\_UNSIGNED

```cpp
#define PLUGIN_VAR_UNSIGNED 0x0080
```

Defined in plugin.h:375

Unsigned modifier for [PLUGIN\_VAR\_INT](plugin_sysvar_types.md#plugin_var_int), [PLUGIN\_VAR\_LONG](plugin_sysvar_types.md#plugin_var_long), [PLUGIN\_VAR\_LONGLONG](plugin_sysvar_types.md#plugin_var_longlong).

***

### PLUGIN\_VAR\_THDLOCAL

```cpp
#define PLUGIN_VAR_THDLOCAL 0x0100
```

Defined in plugin.h:376

Variable is per-connection. Do not use directly!

***

### PLUGIN\_VAR\_READONLY

```cpp
#define PLUGIN_VAR_READONLY 0x0200
```

Defined in plugin.h:377

Server variable is read only

***

### PLUGIN\_VAR\_NOSYSVAR

```cpp
#define PLUGIN_VAR_NOSYSVAR 0x0400
```

Defined in plugin.h:378

Not a server variable. Only a command line option

***

### PLUGIN\_VAR\_NOCMDOPT

```cpp
#define PLUGIN_VAR_NOCMDOPT 0x0800
```

Defined in plugin.h:379

Not a command line option. Only a system variable

***

### PLUGIN\_VAR\_NOCMDARG

```cpp
#define PLUGIN_VAR_NOCMDARG 0x1000
```

Defined in plugin.h:380

No argument for cmd line

***

### PLUGIN\_VAR\_RQCMDARG

```cpp
#define PLUGIN_VAR_RQCMDARG 0x0000
```

Defined in plugin.h:381

Argument required for cmd line

***

### PLUGIN\_VAR\_OPCMDARG

```cpp
#define PLUGIN_VAR_OPCMDARG 0x2000
```

Defined in plugin.h:382

Argument optional for cmd line

***

### PLUGIN\_VAR\_DEPRECATED

```cpp
#define PLUGIN_VAR_DEPRECATED 0x4000
```

Defined in plugin.h:383

Server variable is deprecated

***

### PLUGIN\_VAR\_MEMALLOC

```cpp
#define PLUGIN_VAR_MEMALLOC 0x8000
```

Defined in plugin.h:384

String needs memory allocated
