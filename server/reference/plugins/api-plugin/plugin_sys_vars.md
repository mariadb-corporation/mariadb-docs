---
description: >-
  Plugin API reference: Plugin System Variables. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin System Variables

> [`Plugin API`](plugin_api.md) / [`Plugin Declaration`](plugin_declaration.md)

Declarations for server variables and command line options.

**See also**: [Plugin System Variables Implementation](page-implementation.md#plugin-system-variables-implementation)

## Groups

| Name | Description |
|------|-------------|
| [`Plugin System Variable Types`](plugin_sysvar_types.md) | A list of the plugin system variable types. |
| [`Plugin System Variable Flags`](plugin_sysvar_flags.md) | Flags for plugin system variables. |
| [`Implementation-Only Code for Plugin System Variables`](implementation_only_plugin_vars.md) | The following declarations are utilities to implement plugin system variables API. Do not use directly in plugin code. |
| [`Plugin System Variable Macros`](plugin_sysvar_macros.md) | Macros for defining plugin system variables. |
| [`Plugin Session-Local System Variable Macros`](plugin_thdvar_macros.md) | Macros for defining session-local plugin system variables. |

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_value`](#st_mysql_value) | [st_mysql_value](#st_mysql_value) Reading values API. |

## Macros

| Name | Description |
|------|-------------|
| [`SYSVAR`](#sysvar)  | System variable value reference macro. |
| [`THDVAR`](#thdvar)  | Access per-thread plugin system variable values. |
| [`MYSQL_VALUE_TYPE_STRING`](#mysql_value_type_string)  |  |
| [`MYSQL_VALUE_TYPE_REAL`](#mysql_value_type_real)  |  |
| [`MYSQL_VALUE_TYPE_INT`](#mysql_value_type_int)  |  |

---

### SYSVAR

```cpp
#define SYSVAR(name, name) (*(MYSQL_SYSVAR_NAME(name).value))
```

Defined in plugin.h:691

System variable value reference macro.

Macro to reference plugin system variable global value.

Example use 
```cpp
int value = SYSVAR(my_system_variable);
...
SYSVAR(my_system_variable) = 12;
```

**See also**: st_mysql_sys_var and [Plugin System Variables Implementation](page-implementation.md#plugin-system-variables-implementation)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` |  | The name of the plugin system variable. |
| `name` |  | The name of the plugin system variable. |

---

### THDVAR

```cpp
#define THDVAR(thd, name, thd, name) (*(MYSQL_SYSVAR_NAME(name).resolve(thd, MYSQL_SYSVAR_NAME(name).offset)))
```

Defined in plugin.h:705

Access per-thread plugin system variable values.

Used to reference the session system variable values.

#### Returns
Reference to the corresponding plugin system variable's value.

**See also**: [Define a Session Variable](page-implementation.md#define-a-session-variable)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | The session handle. If thd is NULL, the global value is accessed. |
| `name` |  | The name of the plugin system variable. |
| `thd` |  | The session handle. If thd is NULL, the global value is accessed. |
| `name` |  | The name of the plugin system variable. |

---

### MYSQL_VALUE_TYPE_STRING

```cpp
#define MYSQL_VALUE_TYPE_STRING 0
```

Defined in plugin.h:864

---

### MYSQL_VALUE_TYPE_REAL

```cpp
#define MYSQL_VALUE_TYPE_REAL 1
```

Defined in plugin.h:865

---

### MYSQL_VALUE_TYPE_INT

```cpp
#define MYSQL_VALUE_TYPE_INT 2
```

Defined in plugin.h:866

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`mysql_var_check_func`](#mysql_var_check_func)  | This function should parse the user provided value and store in the provided temporary storage any data as required by the update func. There is sufficient space in the temporary storage to store a double. Note that the update func may not be called if any other error occurs so any memory allocated should be thread-local so that it may be freed automatically at the end of the statement. |
| `void(*` | [`mysql_var_update_func`](#mysql_var_update_func)  | This function should use the validated value stored in the temporary store `save` and persist it in the provided pointer to the dynamic variable. For example, strings may require memory to be allocated. |

---

### mysql_var_check_func

```cpp
using mysql_var_check_func = int(*
```

Defined in plugin.h:413

This function should parse the user provided value and store in the provided temporary storage any data as required by the update func. There is sufficient space in the temporary storage to store a double. Note that the update func may not be called if any other error occurs so any memory allocated should be thread-local so that it may be freed automatically at the end of the statement.

> [!WARNING]
> If this callback is supplied, it *MUST* store the new value into `save`, so that [mysql_var_update_func](#mysql_var_update_func) can pick it up later. The server will not do it on its own in addition to calling the callback.

**See also**: [Check and Update Callbacks](page-implementation.md#check-and-update-callbacks)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | thread handle |
| `var` |  | dynamic variable being altered |
| `save` |  | pointer to temporary storage. Valid across check and update functions. |
| `value` |  | user provided value |
| `thd` |  | thread handle |
| `var` |  | dynamic variable being altered |
| `save` |  | pointer to temporary storage. Valid across check and update functions. |
| `value` |  | user provided value |

#### Return Values

| Value | Description |
|-------|-------------|
| `0` | user provided value is OK and the update func may be called. |
| `any` | other value indicates error. |

---

### mysql_var_update_func

```cpp
using mysql_var_update_func = void(*
```

Defined in plugin.h:432

This function should use the validated value stored in the temporary store `save` and persist it in the provided pointer to the dynamic variable. For example, strings may require memory to be allocated.

> [!WARNING]
> If this callback is supplied, it *MUST* store the actual value from `save` to `var_ptr`. The server will not do it on its own in addition to calling the callback.

**See also**: [Check and Update Callbacks](page-implementation.md#check-and-update-callbacks)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | thread handle |
| `var` |  | dynamic variable being altered |
| `var_ptr` |  | pointer to dynamic variable |
| `save` |  | pointer to temporary storage. Valid across check and update functions. |
| `thd` |  | thread handle |
| `var` |  | dynamic variable being altered |
| `var_ptr` |  | pointer to dynamic variable |
| `save` |  | pointer to temporary storage. Valid across check and update functions. |


## Class Definitions



### st_mysql_value

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_value
```

Defined in plugin.h:880

[st_mysql_value](#st_mysql_value) Reading values API.

Used by server variables framework to parse user-provided values.

Will be used for arguments when implementing UDFs.

Note that [val_str()](#val_str) returns a string in temporary memory that will be freed at the end of statement. Copy the string if you need it to persist.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`value_type`](#value_type)  |  |
| `const char *(*` | [`val_str`](#val_str)  |  |
| `int(*` | [`val_real`](#val_real)  |  |
| `int(*` | [`val_int`](#val_int)  |  |
| `int(*` | [`is_unsigned`](#is_unsigned)  |  |

---

#### value_type

```cpp
int(* value_type)(struct st_mysql_value *)
```

Defined in plugin.h:882

---

#### val_str

```cpp
const char *(* val_str)(struct st_mysql_value *, char *buffer, int *length)
```

Defined in plugin.h:883

---

#### val_real

```cpp
int(* val_real)(struct st_mysql_value *, double *realbuf)
```

Defined in plugin.h:884

---

#### val_int

```cpp
int(* val_int)(struct st_mysql_value *, long long *intbuf)
```

Defined in plugin.h:885

---

#### is_unsigned

```cpp
int(* is_unsigned)(struct st_mysql_value *)
```

Defined in plugin.h:886

