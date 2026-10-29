---
description: >-
  Plugin API reference: Client Plugin API. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Client Plugin API

API for plugins that work on the client side

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_client_plugin`](#st_mysql_client_plugin) |  |
| [`st_mysql_client_plugin_AUTHENTICATION`](#st_mysql_client_plugin_authentication) |  |

## Macros

| Name | Description |
|------|-------------|
| [`ORDINARY_QUESTION`](#ordinary_question)  | first byte of the question string is the question "type". It can be an "ordinary" or a "password" question. The last bit set marks a last question in the authentication exchange. |
| [`LAST_QUESTION`](#last_question)  |  |
| [`PASSWORD_QUESTION`](#password_question)  |  |
| [`LAST_PASSWORD`](#last_password)  |  |
| [`MYSQL_PLUGIN_EXPORT_C`](#mysql_plugin_export_c)  |  |
| [`MYSQL_PLUGIN_EXPORT`](#mysql_plugin_export)  |  |
| [`C_MODE_START`](#c_mode_start)  |  |
| [`C_MODE_END`](#c_mode_end)  |  |
| [`MYSQL_CLIENT_reserved1`](#mysql_client_reserved1)  |  |
| [`MYSQL_CLIENT_reserved2`](#mysql_client_reserved2)  |  |
| [`MYSQL_CLIENT_AUTHENTICATION_PLUGIN`](#mysql_client_authentication_plugin)  |  |
| [`MYSQL_CLIENT_AUTHENTICATION_PLUGIN_INTERFACE_VERSION`](#mysql_client_authentication_plugin_interface_version)  |  |
| [`MYSQL_CLIENT_MAX_PLUGINS`](#mysql_client_max_plugins)  |  |
| [`mysql_declare_client_plugin`](#mysql_declare_client_plugin)  |  |
| [`mysql_end_client_plugin`](#mysql_end_client_plugin)  |  |
| [`MYSQL_CLIENT_PLUGIN_HEADER`](#mysql_client_plugin_header)  |  |

---

### ORDINARY_QUESTION

```cpp
#define ORDINARY_QUESTION "\2"
```

Defined in auth_dialog_client.h:57

first byte of the question string is the question "type". It can be an "ordinary" or a "password" question. The last bit set marks a last question in the authentication exchange.

---

### LAST_QUESTION

```cpp
#define LAST_QUESTION "\3"
```

Defined in auth_dialog_client.h:58

---

### PASSWORD_QUESTION

```cpp
#define PASSWORD_QUESTION "\4"
```

Defined in auth_dialog_client.h:59

---

### LAST_PASSWORD

```cpp
#define LAST_PASSWORD "\5"
```

Defined in auth_dialog_client.h:60

---

### MYSQL_PLUGIN_EXPORT_C

```cpp
#define MYSQL_PLUGIN_EXPORT_C
```

Defined in client_plugin.h:42

---

### MYSQL_PLUGIN_EXPORT

```cpp
#define MYSQL_PLUGIN_EXPORT extern "C" MYSQL_PLUGIN_EXPORT_C
```

Defined in client_plugin.h:45

---

### C_MODE_START

```cpp
#define C_MODE_START extern "C" {
```

Defined in client_plugin.h:46

---

### C_MODE_END

```cpp
#define C_MODE_END }
```

Defined in client_plugin.h:47

---

### MYSQL_CLIENT_reserved1

```cpp
#define MYSQL_CLIENT_reserved1 0
```

Defined in client_plugin.h:60

---

### MYSQL_CLIENT_reserved2

```cpp
#define MYSQL_CLIENT_reserved2 1
```

Defined in client_plugin.h:61

---

### MYSQL_CLIENT_AUTHENTICATION_PLUGIN

```cpp
#define MYSQL_CLIENT_AUTHENTICATION_PLUGIN 2
```

Defined in client_plugin.h:62

---

### MYSQL_CLIENT_AUTHENTICATION_PLUGIN_INTERFACE_VERSION

```cpp
#define MYSQL_CLIENT_AUTHENTICATION_PLUGIN_INTERFACE_VERSION 0x0101
```

Defined in client_plugin.h:64

---

### MYSQL_CLIENT_MAX_PLUGINS

```cpp
#define MYSQL_CLIENT_MAX_PLUGINS 3
```

Defined in client_plugin.h:66

---

### mysql_declare_client_plugin

```cpp
#define mysql_declare_client_plugin(X, X) C_MODE_STARTMYSQL_PLUGIN_EXPORT_C         \
        struct st_mysql_client_plugin_ ## X        \
        _mysql_client_plugin_declaration_ = {   \
          MYSQL_CLIENT_ ## X ## _PLUGIN,        \
          MYSQL_CLIENT_ ## X ## _PLUGIN_INTERFACE_VERSION,
```

Defined in client_plugin.h:68

---

### mysql_end_client_plugin

```cpp
#define mysql_end_client_plugin }; C_MODE_END
```

Defined in client_plugin.h:74

---

### MYSQL_CLIENT_PLUGIN_HEADER

```cpp
#define MYSQL_CLIENT_PLUGIN_HEADER int type;                                             \
  unsigned int interface_version;                       \
  const char *name;                                     \
  const char *author;                                   \
  const char *desc;                                     \
  unsigned int version[3];                              \
  const char *license;                                  \
  void *mysql_api;                                      \
  int (*init)(char *, size_t, int, va_list);            \
  int (*deinit)();                                      \
  int (*options)(const char *option, const void *);
```

Defined in client_plugin.h:77

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| `char *(*` | [`mysql_authentication_dialog_ask_t`](#mysql_authentication_dialog_ask_t)  | type of the mysql_authentication_dialog_ask function |

---

### mysql_authentication_dialog_ask_t

```cpp
using mysql_authentication_dialog_ask_t = char *(*
```

Defined in auth_dialog_client.h:49

type of the mysql_authentication_dialog_ask function

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql` |  | mysql |
| `type` |  | type of the input 1 - ordinary string input 2 - password string |
| `prompt` |  | prompt |
| `buf` |  | a buffer to store the use input |
| `buf_len` |  | the length of the buffer |
| `mysql` |  | mysql |
| `type` |  | type of the input 1 - ordinary string input 2 - password string |
| `prompt` |  | prompt |
| `buf` |  | a buffer to store the use input |
| `buf_len` |  | the length of the buffer |

#### Return Values

| Value | Description |
|-------|-------------|
| `a` | pointer to the user input string. It may be equal to 'buf' or to 'mysql->password'. In all other cases it is assumed to be an allocated string, and the "dialog" plugin will free() it. |

## Functions

| Return | Name | Description |
|--------|------|-------------|
| struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | [`mysql_load_plugin`](#mysql_load_plugin)  | loads a plugin and initializes it |
| struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | [`mysql_load_plugin_v`](#mysql_load_plugin_v)  | loads a plugin and initializes it, taking va_list as an argument |
| struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | [`mysql_client_find_plugin`](#mysql_client_find_plugin)  | finds an already loaded plugin by name, or loads it, if necessary |
| struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | [`mysql_client_register_plugin`](#mysql_client_register_plugin)  | adds a plugin structure to the list of loaded plugins |
| `int` | [`mysql_plugin_options`](#mysql_plugin_options)  | set plugin options |

---

### mysql_load_plugin

```cpp
struct st_mysql_client_plugin * mysql_load_plugin(struct st_mysql * mysql, const char * name, int type, int argc, ..., struct st_mysql * mysql, const char * name, int type, int argc, ...)
```

Defined in client_plugin.h:125

loads a plugin and initializes it

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql` | `struct st_mysql *` | MYSQL structure. |
| `name` | `const char *` | a name of the plugin to load |
| `type` | `int` | type of plugin that should be loaded, -1 to disable type check |
| `argc` | `int` | number of arguments to pass to the plugin initialization function |
| `mysql` | `struct st_mysql *` | MYSQL structure. |
| `name` | `const char *` | a name of the plugin to load |
| `type` | `int` | type of plugin that should be loaded, -1 to disable type check |
| `argc` | `int` | number of arguments to pass to the plugin initialization function |

#### Return Values

| Value | Description |
|-------|-------------|
| `a` | pointer to the loaded plugin, or NULL in case of a failure |

---

### mysql_load_plugin_v

```cpp
struct st_mysql_client_plugin * mysql_load_plugin_v(struct st_mysql * mysql, const char * name, int type, int argc, va_list args, struct st_mysql * mysql, const char * name, int type, int argc, va_list args)
```

Defined in client_plugin.h:145

loads a plugin and initializes it, taking va_list as an argument

This is the same as mysql_load_plugin, but take va_list instead of a list of arguments.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql` | `struct st_mysql *` | MYSQL structure. |
| `name` | `const char *` | a name of the plugin to load |
| `type` | `int` | type of plugin that should be loaded, -1 to disable type check |
| `argc` | `int` | number of arguments to pass to the plugin initialization function |
| `args` | `va_list` | arguments for the plugin initialization function |
| `mysql` | `struct st_mysql *` | MYSQL structure. |
| `name` | `const char *` | a name of the plugin to load |
| `type` | `int` | type of plugin that should be loaded, -1 to disable type check |
| `argc` | `int` | number of arguments to pass to the plugin initialization function |
| `args` | `va_list` | arguments for the plugin initialization function |

#### Return Values

| Value | Description |
|-------|-------------|
| `a` | pointer to the loaded plugin, or NULL in case of a failure |

---

### mysql_client_find_plugin

```cpp
struct st_mysql_client_plugin * mysql_client_find_plugin(struct st_mysql * mysql, const char * name, int type, struct st_mysql * mysql, const char * name, int type)
```

Defined in client_plugin.h:159

finds an already loaded plugin by name, or loads it, if necessary

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql` | `struct st_mysql *` | MYSQL structure. |
| `name` | `const char *` | a name of the plugin to load |
| `type` | `int` | type of plugin that should be loaded |
| `mysql` | `struct st_mysql *` | MYSQL structure. |
| `name` | `const char *` | a name of the plugin to load |
| `type` | `int` | type of plugin that should be loaded |

#### Return Values

| Value | Description |
|-------|-------------|
| `a` | pointer to the plugin, or NULL in case of a failure |

---

### mysql_client_register_plugin

```cpp
struct st_mysql_client_plugin * mysql_client_register_plugin(struct st_mysql * mysql, struct st_mysql_client_plugin * plugin, struct st_mysql * mysql, struct st_mysql_client_plugin * plugin)
```

Defined in client_plugin.h:176

adds a plugin structure to the list of loaded plugins

This is useful if an application has the necessary functionality (for example, a special load data handler) statically linked into the application binary. It can use this function to register the plugin directly, avoiding the need to factor it out into a shared object.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql` | `struct st_mysql *` | MYSQL structure. It is only used for error reporting |
| `plugin` | struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | an [st_mysql_client_plugin](#st_mysql_client_plugin) structure to register |
| `mysql` | `struct st_mysql *` | MYSQL structure. It is only used for error reporting |
| `plugin` | struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | an [st_mysql_client_plugin](#st_mysql_client_plugin) structure to register |

#### Return Values

| Value | Description |
|-------|-------------|
| `a` | pointer to the plugin, or NULL in case of a failure |

---

### mysql_plugin_options

```cpp
int mysql_plugin_options(struct st_mysql_client_plugin * plugin, const char * option, const void * value, struct st_mysql_client_plugin * plugin, const char * option, const void * value)
```

Defined in client_plugin.h:191

set plugin options

Can be used to set extra options and affect behavior for a plugin. This function may be called multiple times to set several options

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `plugin` | struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | an [st_mysql_client_plugin](#st_mysql_client_plugin) structure |
| `option` | `const char *` | a string which specifies the option to set |
| `value` | `const void *` | value for the option. |
| `plugin` | struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | an [st_mysql_client_plugin](#st_mysql_client_plugin) structure |
| `option` | `const char *` | a string which specifies the option to set |
| `value` | `const void *` | value for the option. |

#### Return Values

| Value | Description |
|-------|-------------|
| `0` | on success, 1 in case of failure |


## Class Definitions



### st_mysql_client_plugin

```cpp
#include <client_plugin.h>
```

```cpp
struct st_mysql_client_plugin
```

Defined in client_plugin.h:90



### st_mysql_client_plugin_AUTHENTICATION

```cpp
#include <client_plugin.h>
```

```cpp
struct st_mysql_client_plugin_AUTHENTICATION
```

Defined in client_plugin.h:100

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`MYSQL_CLIENT_PLUGIN_HEADER`](api.md#mysql_client_plugin_header) int(* | [`authenticate_user`](#authenticate_user)  |  |
| `int(*` | [`hash_password_bin`](#hash_password_bin)  |  |

---

#### authenticate_user

```cpp
MYSQL_CLIENT_PLUGIN_HEADER int(* authenticate_user)(MYSQL_PLUGIN_VIO *vio, struct st_mysql *mysql)
```

Defined in client_plugin.h:103

---

#### hash_password_bin

```cpp
int(* hash_password_bin)(struct st_mysql *mysql, unsigned char *hash, size_t *hash_length)
```

Defined in client_plugin.h:104

