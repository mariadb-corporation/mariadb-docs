---
description: >-
  Plugin API reference: Plugin System Variable Flags. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin System Variable Flags

> [`Plugin API`](plugin_api.md) / [`Plugin Declaration`](plugin_declaration.md) / [`Plugin System Variables`](plugin_sys_vars.md)

Flags for plugin system variables.

## Macros

| Name | Description |
|------|-------------|
| [`PLUGIN_VAR_UNSIGNED`](#plugin_var_unsigned)  | Unsigned modifier for [PLUGIN_VAR_INT](api.md#plugin_var_int), [PLUGIN_VAR_LONG](api.md#plugin_var_long), [PLUGIN_VAR_LONGLONG](api.md#plugin_var_longlong). |
| [`PLUGIN_VAR_THDLOCAL`](#plugin_var_thdlocal)  | Variable is per-connection. Do not use directly! |
| [`PLUGIN_VAR_READONLY`](#plugin_var_readonly)  | Server variable is read only |
| [`PLUGIN_VAR_NOSYSVAR`](#plugin_var_nosysvar)  | Not a server variable. Only a command line option |
| [`PLUGIN_VAR_NOCMDOPT`](#plugin_var_nocmdopt)  | Not a command line option. Only a system variable |
| [`PLUGIN_VAR_NOCMDARG`](#plugin_var_nocmdarg)  | No argument for cmd line |
| [`PLUGIN_VAR_RQCMDARG`](#plugin_var_rqcmdarg)  | Argument required for cmd line |
| [`PLUGIN_VAR_OPCMDARG`](#plugin_var_opcmdarg)  | Argument optional for cmd line |
| [`PLUGIN_VAR_DEPRECATED`](#plugin_var_deprecated)  | Server variable is deprecated |
| [`PLUGIN_VAR_MEMALLOC`](#plugin_var_memalloc)  | String needs memory allocated |

---

### PLUGIN_VAR_UNSIGNED

```cpp
#define PLUGIN_VAR_UNSIGNED 0x0080
```

Defined in plugin.h:375

Unsigned modifier for [PLUGIN_VAR_INT](api.md#plugin_var_int), [PLUGIN_VAR_LONG](api.md#plugin_var_long), [PLUGIN_VAR_LONGLONG](api.md#plugin_var_longlong).

---

### PLUGIN_VAR_THDLOCAL

```cpp
#define PLUGIN_VAR_THDLOCAL 0x0100
```

Defined in plugin.h:376

Variable is per-connection. Do not use directly!

---

### PLUGIN_VAR_READONLY

```cpp
#define PLUGIN_VAR_READONLY 0x0200
```

Defined in plugin.h:377

Server variable is read only

---

### PLUGIN_VAR_NOSYSVAR

```cpp
#define PLUGIN_VAR_NOSYSVAR 0x0400
```

Defined in plugin.h:378

Not a server variable. Only a command line option

---

### PLUGIN_VAR_NOCMDOPT

```cpp
#define PLUGIN_VAR_NOCMDOPT 0x0800
```

Defined in plugin.h:379

Not a command line option. Only a system variable

---

### PLUGIN_VAR_NOCMDARG

```cpp
#define PLUGIN_VAR_NOCMDARG 0x1000
```

Defined in plugin.h:380

No argument for cmd line

---

### PLUGIN_VAR_RQCMDARG

```cpp
#define PLUGIN_VAR_RQCMDARG 0x0000
```

Defined in plugin.h:381

Argument required for cmd line

---

### PLUGIN_VAR_OPCMDARG

```cpp
#define PLUGIN_VAR_OPCMDARG 0x2000
```

Defined in plugin.h:382

Argument optional for cmd line

---

### PLUGIN_VAR_DEPRECATED

```cpp
#define PLUGIN_VAR_DEPRECATED 0x4000
```

Defined in plugin.h:383

Server variable is deprecated

---

### PLUGIN_VAR_MEMALLOC

```cpp
#define PLUGIN_VAR_MEMALLOC 0x8000
```

Defined in plugin.h:384

String needs memory allocated

