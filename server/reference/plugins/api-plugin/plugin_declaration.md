---
description: >-
  Plugin API reference: Plugin Declaration. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Plugin Declaration

> [`Plugin API`](plugin_api.md)

How to declare a plugin to the server.

Macros for beginning and ending plugin declarations. Between [maria_declare_plugin](#maria_declare_plugin) and [maria_declare_plugin_end](#maria_declare_plugin_end) there should be a [st_maria_plugin](#st_maria_plugin) struct for each plugin to be declared.

## Groups

| Name | Description |
|------|-------------|
| [`Plugin License`](plugin_license.md) | The allowable licenses for plugins |
| [`Plugin Maturity`](plugin_maturity.md) | The allowable code maturity levels for plugins |
| [`Plugin Status Variables`](plugin_status_vars.md) |  |
| [`Plugin Flags`](plugin_flags.md) | Constants for plugin flags. |
| [`Plugin System Variables`](plugin_sys_vars.md) | Declarations for server variables and command line options. |

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_plugin`](#st_mysql_plugin) | Plugin description structure. |
| [`st_maria_plugin`](#st_maria_plugin) | MariaDB extension for plugins declaration structure. |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_DLLEXPORT`](#mysql_dllexport)  | Declaration macros for MySQL plugins. |
| [`MYSQL_PLUGIN_EXPORT`](#mysql_plugin_export)  | Implementation independent macro for MySQL plugins. |
| [`MYSQL_PLUGIN_INTERFACE_VERSION`](#mysql_plugin_interface_version)  | MySQL plugin interface version |
| [`MARIA_PLUGIN_INTERFACE_VERSION`](#maria_plugin_interface_version)  | MariaDB plugin interface version |
| [`__MYSQL_DECLARE_PLUGIN`](#mysql_declare_plugin)  |  |
| [`MARIA_DECLARE_PLUGIN__`](#maria_declare_plugin)  |  |
| [`mysql_declare_plugin`](#mysql_declare_plugin)  |  |
| [`maria_declare_plugin`](#maria_declare_plugin)  |  |
| [`mysql_declare_plugin_end`](#mysql_declare_plugin_end)  |  |
| [`maria_declare_plugin_end`](#maria_declare_plugin_end)  |  |

---

### MYSQL_DLLEXPORT

```cpp
#define MYSQL_DLLEXPORT
```

Defined in plugin.h:45

Declaration macros for MySQL plugins.

On Windows, exports from DLL need to be declared Also, plugin needs to be declared as extern "C" because MSVC unlike other compilers, uses C++ mangling for variables not only for functions.

---

### MYSQL_PLUGIN_EXPORT

```cpp
#define MYSQL_PLUGIN_EXPORT extern "C" MYSQL_DLLEXPORT
```

Defined in plugin.h:58

Implementation independent macro for MySQL plugins.

---

### MYSQL_PLUGIN_INTERFACE_VERSION

```cpp
#define MYSQL_PLUGIN_INTERFACE_VERSION 0x0105
```

Defined in plugin.h:115

MySQL plugin interface version

---

### MARIA_PLUGIN_INTERFACE_VERSION

```cpp
#define MARIA_PLUGIN_INTERFACE_VERSION 0x0110
```

Defined in plugin.h:118

MariaDB plugin interface version

---

### __MYSQL_DECLARE_PLUGIN

```cpp
#define __MYSQL_DECLARE_PLUGIN(NAME, VERSION, PSIZE, DECLS, NAME, VERSION, PSIZE, DECLS) MYSQL_PLUGIN_EXPORT int _mysql_plugin_interface_version_;                     \
int _mysql_plugin_interface_version_= MYSQL_PLUGIN_INTERFACE_VERSION;         \
MYSQL_PLUGIN_EXPORT int _mysql_sizeof_struct_st_plugin_;                      \
int _mysql_sizeof_struct_st_plugin_= sizeof(struct st_mysql_plugin);          \
MYSQL_PLUGIN_EXPORT struct st_mysql_plugin _mysql_plugin_declarations_[];     \
struct st_mysql_plugin _mysql_plugin_declarations_[]= {
```

Defined in plugin.h:207

---

### MARIA_DECLARE_PLUGIN__

```cpp
#define MARIA_DECLARE_PLUGIN__(NAME, VERSION, PSIZE, DECLS, NAME, VERSION, PSIZE, DECLS) MYSQL_PLUGIN_EXPORT int _maria_plugin_interface_version_;                      \
int _maria_plugin_interface_version_= MARIA_PLUGIN_INTERFACE_VERSION;          \
MYSQL_PLUGIN_EXPORT int _maria_sizeof_struct_st_plugin_;                       \
int _maria_sizeof_struct_st_plugin_= sizeof(struct st_maria_plugin);           \
MYSQL_PLUGIN_EXPORT struct st_maria_plugin _maria_plugin_declarations_[];      \
struct st_maria_plugin _maria_plugin_declarations_[]= {
```

Defined in plugin.h:215

---

### mysql_declare_plugin

```cpp
#define mysql_declare_plugin(NAME, NAME) __MYSQL_DECLARE_PLUGIN(NAME, \
                 builtin_ ## NAME ## _plugin_interface_version, \
                 builtin_ ## NAME ## _sizeof_struct_st_plugin, \
                 builtin_ ## NAME ## _plugin)
```

Defined in plugin.h:225

---

### maria_declare_plugin

```cpp
#define maria_declare_plugin(NAME, NAME) MARIA_DECLARE_PLUGIN__(NAME, \
                 builtin_maria_ ## NAME ## _plugin_interface_version, \
                 builtin_maria_ ## NAME ## _sizeof_struct_st_plugin, \
                 builtin_maria_ ## NAME ## _plugin)
```

Defined in plugin.h:231

---

### mysql_declare_plugin_end

```cpp
#define mysql_declare_plugin_end ,{0,0,0,0,0,0,0,0,0,0,0,0,0}}
```

Defined in plugin.h:237

---

### maria_declare_plugin_end

```cpp
#define maria_declare_plugin_end ,{0,0,0,0,0,0,0,0,0,0,0,0,0}}
```

Defined in plugin.h:238

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| `void *` | [`MYSQL_PLUGIN`](#mysql_plugin)  | Opaque type for a plugin handle. |

---

### MYSQL_PLUGIN

```cpp
using MYSQL_PLUGIN = void *
```

Defined in plugin.h:78

Opaque type for a plugin handle.


## Class Definitions



### st_mysql_plugin

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_plugin
```

Defined in plugin.h:715

Plugin description structure.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`type`](#type)  | the plugin type (a MYSQL_XXX_PLUGIN value) <br/> |
| `void *` | [`info`](#info)  | pointer to type-specific plugin descriptor <br/> |
| `const char *` | [`name`](#name)  | plugin name <br/> |
| `const char *` | [`author`](#author)  | plugin author (for I_S.PLUGINS) <br/> |
| `const char *` | [`descr`](#descr)  | general descriptive text (for I_S.PLUGINS) <br/> |
| `int` | [`license`](#license)  | the plugin license (PLUGIN_LICENSE_XXX) <br/> |
| `int(*` | [`init`](#init)  | The function to invoke when plugin is loaded. Plugin initialisation done here should defer any ALTER TABLE queries to after the ddl recovery is done, in the signal_ddl_recovery_done() callback called by ha_signal_ddl_recovery_done(). |
| `int(*` | [`deinit`](#deinit)  | the function to invoke when plugin is unloaded |
| `unsigned int` | [`version`](#version)  | plugin version (for I_S.PLUGINS) <br/> |
| struct [`st_mysql_show_var`](plugin_status_vars.md#st_mysql_show_var) * | [`status_vars`](#status_vars)  |  |
| `struct st_mysql_sys_var **` | [`system_vars`](#system_vars)  |  |
| `void *` | [`__reserved1`](#reserved1)  | reserved for dependency checking <br/> |
| `unsigned long` | [`flags`](#flags)  | flags for plugin |

---

#### type

```cpp
int type
```

Defined in plugin.h:717

the plugin type (a MYSQL_XXX_PLUGIN value) <br/>

---

#### info

```cpp
void * info
```

Defined in plugin.h:718

pointer to type-specific plugin descriptor <br/>

---

#### name

```cpp
const char * name
```

Defined in plugin.h:719

plugin name <br/>

---

#### author

```cpp
const char * author
```

Defined in plugin.h:720

plugin author (for I_S.PLUGINS) <br/>

---

#### descr

```cpp
const char * descr
```

Defined in plugin.h:721

general descriptive text (for I_S.PLUGINS) <br/>

---

#### license

```cpp
int license
```

Defined in plugin.h:722

the plugin license (PLUGIN_LICENSE_XXX) <br/>

---

#### init

```cpp
int(* init)(void *)
```

Defined in plugin.h:729

The function to invoke when plugin is loaded. Plugin initialisation done here should defer any ALTER TABLE queries to after the ddl recovery is done, in the signal_ddl_recovery_done() callback called by ha_signal_ddl_recovery_done().

---

#### deinit

```cpp
int(* deinit)(void *)
```

Defined in plugin.h:730

the function to invoke when plugin is unloaded

---

#### version

```cpp
unsigned int version
```

Defined in plugin.h:731

plugin version (for I_S.PLUGINS) <br/>

---

#### status_vars

```cpp
struct st_mysql_show_var * status_vars
```

Type: struct [`st_mysql_show_var`](plugin_status_vars.md#st_mysql_show_var) *

Defined in plugin.h:732

---

#### system_vars

```cpp
struct st_mysql_sys_var ** system_vars
```

Defined in plugin.h:733

---

#### __reserved1

```cpp
void * __reserved1
```

Defined in plugin.h:734

reserved for dependency checking <br/>

---

#### flags

```cpp
unsigned long flags
```

Defined in plugin.h:735

flags for plugin



### st_maria_plugin

```cpp
#include <plugin.h>
```

```cpp
struct st_maria_plugin
```

Defined in plugin.h:746

MariaDB extension for plugins declaration structure.

It also copies current MySQL plugin fields to have more independency in plugins extension

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`type`](#type-1)  | the plugin type (a MYSQL_XXX_PLUGIN value) <br/> |
| `void *` | [`info`](#info-1)  | pointer to type-specific plugin descriptor <br/> |
| `const char *` | [`name`](#name-1)  | plugin name <br/> |
| `const char *` | [`author`](#author-1)  | plugin author (for SHOW PLUGINS) <br/> |
| `const char *` | [`descr`](#descr-1)  | general descriptive text (for SHOW PLUGINS ) |
| `int` | [`license`](#license-1)  | the plugin license (PLUGIN_LICENSE_XXX) <br/> |
| `int(*` | [`init`](#init-1)  | The function to invoke when plugin is loaded. Plugin initialisation done here should defer any ALTER TABLE queries to after the ddl recovery is done, in the signal_ddl_recovery_done() callback called by ha_signal_ddl_recovery_done(). |
| `int(*` | [`deinit`](#deinit-1)  | the function to invoke when plugin is unloaded |
| `unsigned int` | [`version`](#version-1)  | plugin version (for SHOW PLUGINS) <br/> |
| struct [`st_mysql_show_var`](plugin_status_vars.md#st_mysql_show_var) * | [`status_vars`](#status_vars-1)  |  |
| `struct st_mysql_sys_var **` | [`system_vars`](#system_vars-1)  |  |
| `const char *` | [`version_info`](#version_info)  | plugin version string |
| `unsigned int` | [`maturity`](#maturity)  | MariaDB_PLUGIN_MATURITY_XXX |

---

#### type

```cpp
int type
```

Defined in plugin.h:748

the plugin type (a MYSQL_XXX_PLUGIN value) <br/>

---

#### info

```cpp
void * info
```

Defined in plugin.h:749

pointer to type-specific plugin descriptor <br/>

---

#### name

```cpp
const char * name
```

Defined in plugin.h:750

plugin name <br/>

---

#### author

```cpp
const char * author
```

Defined in plugin.h:751

plugin author (for SHOW PLUGINS) <br/>

---

#### descr

```cpp
const char * descr
```

Defined in plugin.h:752

general descriptive text (for SHOW PLUGINS )

---

#### license

```cpp
int license
```

Defined in plugin.h:753

the plugin license (PLUGIN_LICENSE_XXX) <br/>

---

#### init

```cpp
int(* init)(void *)
```

Defined in plugin.h:760

The function to invoke when plugin is loaded. Plugin initialisation done here should defer any ALTER TABLE queries to after the ddl recovery is done, in the signal_ddl_recovery_done() callback called by ha_signal_ddl_recovery_done().

---

#### deinit

```cpp
int(* deinit)(void *)
```

Defined in plugin.h:761

the function to invoke when plugin is unloaded

---

#### version

```cpp
unsigned int version
```

Defined in plugin.h:762

plugin version (for SHOW PLUGINS) <br/>

---

#### status_vars

```cpp
struct st_mysql_show_var * status_vars
```

Type: struct [`st_mysql_show_var`](plugin_status_vars.md#st_mysql_show_var) *

Defined in plugin.h:763

---

#### system_vars

```cpp
struct st_mysql_sys_var ** system_vars
```

Defined in plugin.h:764

---

#### version_info

```cpp
const char * version_info
```

Defined in plugin.h:765

plugin version string

---

#### maturity

```cpp
unsigned int maturity
```

Defined in plugin.h:766

MariaDB_PLUGIN_MATURITY_XXX

