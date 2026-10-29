---
description: >-
  Every generated Plugin API class, macro, typedef, and function on one page, including the plugin services and the audit, authentication, and encryption plugin interfaces.
---

# API Reference

## Groups

| Name | Description |
|------|-------------|
| [`Plugin API`](plugin_api.md) | The Plugin API is a set of interfaces for handling plugins. |
| [`Client Plugin API`](plugin_client_api.md) | API for plugins that work on the client side |

## Macros

---

### psi_likely

```cpp
#define psi_likely(A, A) unlikely(A)
```

Defined in psi/psi.h:52

---

### psi_unlikely

```cpp
#define psi_unlikely(A, A) likely(A)
```

Defined in psi/psi.h:53

---

### PSI_SCHEMA_NAME_LEN

```cpp
#define PSI_SCHEMA_NAME_LEN (64 * 3)
```

Defined in psi/psi.h:1200

---

### PSI_DYNAMIC_CALL

```cpp
#define PSI_DYNAMIC_CALL(M, M) PSI_server->M
```

Defined in psi/psi.h:3030

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

### MYSQL_THD

```cpp
#define MYSQL_THD THD*
```

Defined in plugin.h:66

---

### MYSQL_XIDDATASIZE

```cpp
#define MYSQL_XIDDATASIZE 128
```

Defined in plugin.h:87

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

### MYSQL_UDF_PLUGIN

```cpp
#define MYSQL_UDF_PLUGIN 0
```

Defined in plugin.h:127

not implemented <br/>

---

### MYSQL_STORAGE_ENGINE_PLUGIN

```cpp
#define MYSQL_STORAGE_ENGINE_PLUGIN 1
```

Defined in plugin.h:128

Storage engine plugin <br/>

---

### MYSQL_FTPARSER_PLUGIN

```cpp
#define MYSQL_FTPARSER_PLUGIN 2
```

Defined in plugin.h:129

Full-text parser plugin <br/>

---

### MYSQL_DAEMON_PLUGIN

```cpp
#define MYSQL_DAEMON_PLUGIN 3
```

Defined in plugin.h:130

Daemon plugin <br/>

---

### MYSQL_INFORMATION_SCHEMA_PLUGIN

```cpp
#define MYSQL_INFORMATION_SCHEMA_PLUGIN 4
```

Defined in plugin.h:131

Information schema plugin

---

### MYSQL_AUDIT_PLUGIN

```cpp
#define MYSQL_AUDIT_PLUGIN 5
```

Defined in plugin.h:132

Audit plugin <br/>

---

### MYSQL_REPLICATION_PLUGIN

```cpp
#define MYSQL_REPLICATION_PLUGIN 6
```

Defined in plugin.h:133

Replication plugin <br/>

---

### MYSQL_AUTHENTICATION_PLUGIN

```cpp
#define MYSQL_AUTHENTICATION_PLUGIN 7
```

Defined in plugin.h:134

Authentication plugin <br/>

---

### MYSQL_MAX_PLUGIN_TYPE_NUM

```cpp
#define MYSQL_MAX_PLUGIN_TYPE_NUM 12
```

Defined in plugin.h:135

---

### MariaDB_PASSWORD_VALIDATION_PLUGIN

```cpp
#define MariaDB_PASSWORD_VALIDATION_PLUGIN 8
```

Defined in plugin.h:139

Client and server password validation Encryption and key management plugins

---

### MariaDB_ENCRYPTION_PLUGIN

```cpp
#define MariaDB_ENCRYPTION_PLUGIN 9
```

Defined in plugin.h:141

Plugins for SQL data storage types

---

### MariaDB_DATA_TYPE_PLUGIN

```cpp
#define MariaDB_DATA_TYPE_PLUGIN 10
```

Defined in plugin.h:143

Plugins for new native SQL functions

---

### MariaDB_FUNCTION_PLUGIN

```cpp
#define MariaDB_FUNCTION_PLUGIN 11
```

Defined in plugin.h:145

---

### PLUGIN_LICENSE_PROPRIETARY

```cpp
#define PLUGIN_LICENSE_PROPRIETARY 0
```

Defined in plugin.h:156

---

### PLUGIN_LICENSE_GPL

```cpp
#define PLUGIN_LICENSE_GPL 1
```

Defined in plugin.h:157

---

### PLUGIN_LICENSE_BSD

```cpp
#define PLUGIN_LICENSE_BSD 2
```

Defined in plugin.h:158

---

### PLUGIN_LICENSE_PROPRIETARY_STRING

```cpp
#define PLUGIN_LICENSE_PROPRIETARY_STRING "PROPRIETARY"
```

Defined in plugin.h:160

---

### PLUGIN_LICENSE_GPL_STRING

```cpp
#define PLUGIN_LICENSE_GPL_STRING "GPL"
```

Defined in plugin.h:161

---

### PLUGIN_LICENSE_BSD_STRING

```cpp
#define PLUGIN_LICENSE_BSD_STRING "BSD"
```

Defined in plugin.h:162

---

### MariaDB_PLUGIN_MATURITY_UNKNOWN

```cpp
#define MariaDB_PLUGIN_MATURITY_UNKNOWN 0
```

Defined in plugin.h:173

---

### MariaDB_PLUGIN_MATURITY_EXPERIMENTAL

```cpp
#define MariaDB_PLUGIN_MATURITY_EXPERIMENTAL 1
```

Defined in plugin.h:174

---

### MariaDB_PLUGIN_MATURITY_ALPHA

```cpp
#define MariaDB_PLUGIN_MATURITY_ALPHA 2
```

Defined in plugin.h:175

---

### MariaDB_PLUGIN_MATURITY_BETA

```cpp
#define MariaDB_PLUGIN_MATURITY_BETA 3
```

Defined in plugin.h:176

---

### MariaDB_PLUGIN_MATURITY_GAMMA

```cpp
#define MariaDB_PLUGIN_MATURITY_GAMMA 4
```

Defined in plugin.h:177

---

### MariaDB_PLUGIN_MATURITY_STABLE

```cpp
#define MariaDB_PLUGIN_MATURITY_STABLE 5
```

Defined in plugin.h:178

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

---

### SHOW_INT

```cpp
#define SHOW_INT SHOW_UINT
```

Defined in plugin.h:272

Backward compatibility mapping to [SHOW_UINT](plugin_status_vars.md#enum_mysql_show_type)

---

### SHOW_LONG

```cpp
#define SHOW_LONG SHOW_ULONG
```

Defined in plugin.h:274

Backward compatibility mapping to [SHOW_ULONG](plugin_status_vars.md#enum_mysql_show_type)

---

### SHOW_LONGLONG

```cpp
#define SHOW_LONGLONG SHOW_ULONGLONG
```

Defined in plugin.h:276

Backward compatibility mapping to [SHOW_ULONGLONG](plugin_status_vars.md#enum_mysql_show_type)

---

### SHOW_VAR_FUNC_BUFF_SIZE

```cpp
#define SHOW_VAR_FUNC_BUFF_SIZE (256 * sizeof(void*))
```

Defined in plugin.h:298

---

### PLUGIN_OPT_NO_INSTALL

```cpp
#define PLUGIN_OPT_NO_INSTALL 1UL
```

Defined in plugin.h:323

Unused

---

### PLUGIN_OPT_NO_UNINSTALL

```cpp
#define PLUGIN_OPT_NO_UNINSTALL 2UL
```

Defined in plugin.h:324

Unused

---

### PLUGIN_VAR_BOOL

```cpp
#define PLUGIN_VAR_BOOL 0x0001
```

Defined in plugin.h:353

[my_bool](#my_bool). **See also**: [MYSQL_SYSVAR_BOOL](#mysql_sysvar_bool)

---

### PLUGIN_VAR_INT

```cpp
#define PLUGIN_VAR_INT 0x0002
```

Defined in plugin.h:354

`int`. **See also**: [MYSQL_SYSVAR_INT](#mysql_sysvar_int)

---

### PLUGIN_VAR_LONG

```cpp
#define PLUGIN_VAR_LONG 0x0003
```

Defined in plugin.h:355

`long`. **See also**: [MYSQL_SYSVAR_LONG](#mysql_sysvar_long)

---

### PLUGIN_VAR_LONGLONG

```cpp
#define PLUGIN_VAR_LONGLONG 0x0004
```

Defined in plugin.h:356

`long long`. **See also**: [MYSQL_SYSVAR_LONGLONG](#mysql_sysvar_longlong)

---

### PLUGIN_VAR_STR

```cpp
#define PLUGIN_VAR_STR 0x0005
```

Defined in plugin.h:357

`char*`. **See also**: [MYSQL_SYSVAR_STR](#mysql_sysvar_str)

---

### PLUGIN_VAR_ENUM

```cpp
#define PLUGIN_VAR_ENUM 0x0006
```

Defined in plugin.h:358

`unsigned long`. **See also**: [MYSQL_SYSVAR_ENUM](#mysql_sysvar_enum)

---

### PLUGIN_VAR_SET

```cpp
#define PLUGIN_VAR_SET 0x0007
```

Defined in plugin.h:359

`unsigned long long`. **See also**: [MYSQL_SYSVAR_SET](#mysql_sysvar_set)

---

### PLUGIN_VAR_DOUBLE

```cpp
#define PLUGIN_VAR_DOUBLE 0x0008
```

Defined in plugin.h:360

`double`. **See also**: [MYSQL_SYSVAR_DOUBLE](#mysql_sysvar_double)

---

### PLUGIN_VAR_UNSIGNED

```cpp
#define PLUGIN_VAR_UNSIGNED 0x0080
```

Defined in plugin.h:375

Unsigned modifier for [PLUGIN_VAR_INT](#plugin_var_int), [PLUGIN_VAR_LONG](#plugin_var_long), [PLUGIN_VAR_LONGLONG](#plugin_var_longlong).

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

### MYSQL_DAEMON_INTERFACE_VERSION

```cpp
#define MYSQL_DAEMON_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:782

daemon plugins of different MySQL releases are incompatible

---

### MYSQL_INFORMATION_SCHEMA_INTERFACE_VERSION

```cpp
#define MYSQL_INFORMATION_SCHEMA_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:803

information schema plugins of different MySQL releases are incompatible

---

### MYSQL_HANDLERTON_INTERFACE_VERSION

```cpp
#define MYSQL_HANDLERTON_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:825

storage engines of different MySQL releases are incompatible

---

### MYSQL_REPLICATION_INTERFACE_VERSION

```cpp
#define MYSQL_REPLICATION_INTERFACE_VERSION 0x0200
```

Defined in plugin.h:848

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

---

### PSI_PS_CALL

```cpp
#define PSI_PS_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_ps.h:41

---

### MYSQL_CREATE_PS

```cpp
#define MYSQL_CREATE_PS(IDENTITY, ID, LOCKER, NAME, NAME_LENGTH, IDENTITY, ID, LOCKER, NAME, NAME_LENGTH) NULL
```

Defined in psi/mysql_ps.h:56

---

### MYSQL_EXECUTE_PS

```cpp
#define MYSQL_EXECUTE_PS(LOCKER, PREPARED_STMT, LOCKER, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql_ps.h:58

---

### MYSQL_DESTROY_PS

```cpp
#define MYSQL_DESTROY_PS(PREPARED_STMT, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql_ps.h:60

---

### MYSQL_REPREPARE_PS

```cpp
#define MYSQL_REPREPARE_PS(PREPARED_STMT, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql_ps.h:62

---

### MYSQL_SET_PS_TEXT

```cpp
#define MYSQL_SET_PS_TEXT(PREPARED_STMT, SQLTEXT, SQLTEXT_LENGTH, PREPARED_STMT, SQLTEXT, SQLTEXT_LENGTH) do {} while (0)
```

Defined in psi/mysql_ps.h:64

---

### PSI_SP_CALL

```cpp
#define PSI_SP_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_sp.h:41

---

### MYSQL_START_SP

```cpp
#define MYSQL_START_SP(STATE, SP_SHARE, STATE, SP_SHARE) NULL
```

Defined in psi/mysql_sp.h:48

---

### MYSQL_END_SP

```cpp
#define MYSQL_END_SP(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql_sp.h:57

---

### MYSQL_DROP_SP

```cpp
#define MYSQL_DROP_SP(OT, SN, SNL, ON, ONL, OT, SN, SNL, ON, ONL) do {} while (0)
```

Defined in psi/mysql_sp.h:65

---

### MYSQL_GET_SP_SHARE

```cpp
#define MYSQL_GET_SP_SHARE(OT, SN, SNL, ON, ONL, OT, SN, SNL, ON, ONL) NULL
```

Defined in psi/mysql_sp.h:73

---

### PSI_INSTRUMENT_ME

```cpp
#define PSI_INSTRUMENT_ME 0
```

Defined in psi/psi_base.h:47

---

### PSI_INSTRUMENT_MEM

```cpp
#define PSI_INSTRUMENT_MEM ((PSI_memory_key)0)
```

Defined in psi/psi_base.h:48

---

### PSI_NOT_INSTRUMENTED

```cpp
#define PSI_NOT_INSTRUMENTED 0
```

Defined in psi/psi_base.h:50

---

### PSI_FLAG_GLOBAL

```cpp
#define PSI_FLAG_GLOBAL (1 << 0)
```

Defined in psi/psi_base.h:57

Global flag. This flag indicate that an instrumentation point is a global variable, or a singleton.

---

### PSI_FLAG_MUTABLE

```cpp
#define PSI_FLAG_MUTABLE (1 << 1)
```

Defined in psi/psi_base.h:64

Mutable flag. This flag indicate that an instrumentation point is a general placeholder, that can mutate into a more specific instrumentation point.

---

### PSI_FLAG_THREAD

```cpp
#define PSI_FLAG_THREAD (1 << 2)
```

Defined in psi/psi_base.h:66

---

### PSI_FLAG_STAGE_PROGRESS

```cpp
#define PSI_FLAG_STAGE_PROGRESS (1 << 3)
```

Defined in psi/psi_base.h:73

Stage progress flag. This flag apply to the stage instruments only. It indicates the instrumentation provides progress data.

---

### PSI_RWLOCK_FLAG_SX

```cpp
#define PSI_RWLOCK_FLAG_SX (1 << 4)
```

Defined in psi/psi_base.h:79

Shared Exclusive flag. Indicates that rwlock support the shared exclusive state.

---

### PSI_FLAG_TRANSFER

```cpp
#define PSI_FLAG_TRANSFER (1 << 5)
```

Defined in psi/psi_base.h:86

Transferable flag. This flag indicate that an instrumented object can be created by a thread and destroyed by another thread.

---

### PSI_FLAG_VOLATILITY_SESSION

```cpp
#define PSI_FLAG_VOLATILITY_SESSION (1 << 6)
```

Defined in psi/psi_base.h:94

Volatility flag. This flag indicate that an instrumented object has a volatility (life cycle) comparable to the volatility of a session.

---

### PSI_FLAG_THREAD_SYSTEM

```cpp
#define PSI_FLAG_THREAD_SYSTEM (1 << 9)
```

Defined in psi/psi_base.h:100

System thread flag. Indicates that the instrumented object exists on a system thread.

---

### PSI_CALL_start_metadata_wait

```cpp
#define PSI_CALL_start_metadata_wait(A, B, C, D, A, B, C, D) 0
```

Defined in psi/mysql_mdl.h:52

---

### PSI_CALL_end_metadata_wait

```cpp
#define PSI_CALL_end_metadata_wait(A, B, A, B) do { } while(0)
```

Defined in psi/mysql_mdl.h:53

---

### PSI_CALL_create_metadata_lock

```cpp
#define PSI_CALL_create_metadata_lock(A, B, C, D, E, F, G, A, B, C, D, E, F, G) 0
```

Defined in psi/mysql_mdl.h:54

---

### PSI_CALL_set_metadata_lock_status

```cpp
#define PSI_CALL_set_metadata_lock_status(A, B, A, B) do {} while(0)
```

Defined in psi/mysql_mdl.h:55

---

### PSI_CALL_destroy_metadata_lock

```cpp
#define PSI_CALL_destroy_metadata_lock(A, A) do {} while(0)
```

Defined in psi/mysql_mdl.h:56

---

### mysql_mdl_create

```cpp
#define mysql_mdl_create(I, K, T, D, S, F, L, I, K, T, D, S, F, L) NULL
```

Defined in psi/mysql_mdl.h:75

Instrumented metadata lock creation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `I` |  | Metadata lock identity |
| `K` |  | Metadata key |
| `T` |  | Metadata lock type |
| `D` |  | Metadata lock duration |
| `S` |  | Metadata lock status |
| `F` |  | request source file |
| `L` |  | request source line |
| `I` |  | Metadata lock identity |
| `K` |  | Metadata key |
| `T` |  | Metadata lock type |
| `D` |  | Metadata lock duration |
| `S` |  | Metadata lock status |
| `F` |  | request source file |
| `L` |  | request source line |

---

### mysql_mdl_set_status

```cpp
#define mysql_mdl_set_status(L, S, L, S) do {} while (0)
```

Defined in psi/mysql_mdl.h:82

---

### mysql_mdl_destroy

```cpp
#define mysql_mdl_destroy(M, M) do {} while (0)
```

Defined in psi/mysql_mdl.h:96

Instrumented metadata lock destruction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `M` |  | Metadata lock |
| `M` |  | Metadata lock |

---

### PSI_FILE_CALL

```cpp
#define PSI_FILE_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_file.h:58

---

### mysql_file_register

```cpp
#define mysql_file_register(P1, P2, P3, P1, P2, P3) inline_mysql_file_register(P1, P2, P3)
```

Defined in psi/mysql_file.h:65

File registration.

---

### mysql_file_fgets

```cpp
#define mysql_file_fgets(P1, P2, F, P1, P2, F) inline_mysql_file_fgets(P1, P2, F)
```

Defined in psi/mysql_file.h:77

Instrumented fgets. `mysql_file_fgets` is a replacement for `fgets`.

---

### mysql_file_fgetc

```cpp
#define mysql_file_fgetc(F, F) inline_mysql_file_fgetc(F)
```

Defined in psi/mysql_file.h:89

Instrumented fgetc. `mysql_file_fgetc` is a replacement for `fgetc`.

---

### mysql_file_fputs

```cpp
#define mysql_file_fputs(P1, F, P1, F) inline_mysql_file_fputs(P1, F)
```

Defined in psi/mysql_file.h:101

Instrumented fputs. `mysql_file_fputs` is a replacement for `fputs`.

---

### mysql_file_fputc

```cpp
#define mysql_file_fputc(P1, F, P1, F) inline_mysql_file_fputc(P1, F)
```

Defined in psi/mysql_file.h:114

Instrumented fputc. `mysql_file_fputc` is a replacement for `fputc`.

---

### mysql_file_fprintf

```cpp
#define mysql_file_fprintf inline_mysql_file_fprintf
```

Defined in psi/mysql_file.h:123

Instrumented fprintf. `mysql_file_fprintf` is a replacement for `fprintf`.

---

### mysql_file_vfprintf

```cpp
#define mysql_file_vfprintf(F, P1, P2, F, P1, P2) inline_mysql_file_vfprintf(F, P1, P2)
```

Defined in psi/mysql_file.h:134

Instrumented vfprintf. `mysql_file_vfprintf` is a replacement for `vfprintf`.

---

### mysql_file_fflush

```cpp
#define mysql_file_fflush(F, F) inline_mysql_file_fflush(F)
```

Defined in psi/mysql_file.h:147

Instrumented fflush. `mysql_file_fflush` is a replacement for `fflush`.

---

### mysql_file_feof

```cpp
#define mysql_file_feof(F, F) inline_mysql_file_feof(F)
```

Defined in psi/mysql_file.h:156

Instrumented feof. `mysql_file_feof` is a replacement for `feof`.

---

### mysql_file_fstat

```cpp
#define mysql_file_fstat(FN, S, FL, FN, S, FL) inline_mysql_file_fstat(FN, S, FL)
```

Defined in psi/mysql_file.h:167

Instrumented fstat. `mysql_file_fstat` is a replacement for `my_fstat`.

---

### mysql_file_stat

```cpp
#define mysql_file_stat(K, FN, S, FL, K, FN, S, FL) inline_mysql_file_stat(FN, S, FL)
```

Defined in psi/mysql_file.h:180

Instrumented stat. `mysql_file_stat` is a replacement for `my_stat`.

---

### mysql_file_chsize

```cpp
#define mysql_file_chsize(F, P1, P2, P3, F, P1, P2, P3) inline_mysql_file_chsize(F, P1, P2, P3)
```

Defined in psi/mysql_file.h:193

Instrumented chsize. `mysql_file_chsize` is a replacement for `my_chsize`.

---

### mysql_file_fopen

```cpp
#define mysql_file_fopen(K, N, F1, F2, K, N, F1, F2) inline_mysql_file_fopen(N, F1, F2)
```

Defined in psi/mysql_file.h:206

Instrumented fopen. `mysql_file_fopen` is a replacement for `my_fopen`.

---

### mysql_file_fclose

```cpp
#define mysql_file_fclose(FD, FL, FD, FL) inline_mysql_file_fclose(FD, FL)
```

Defined in psi/mysql_file.h:226

Instrumented fclose. `mysql_file_fclose` is a replacement for `my_fclose`. Without the instrumentation, this call will have the same behavior as the undocumented and possibly platform specific my_fclose(NULL, ...) behavior. With the instrumentation, mysql_fclose(NULL, ...) will safely return 0, which is an extension compared to my_fclose and is therefore compliant. mysql_fclose is on purpose *not* implementing 
```cpp
assert(file != NULL) 
```
, since doing so could introduce regressions.

---

### mysql_file_fread

```cpp
#define mysql_file_fread(FD, P1, P2, P3, FD, P1, P2, P3) inline_mysql_file_fread(FD, P1, P2, P3)
```

Defined in psi/mysql_file.h:239

Instrumented fread. `mysql_file_fread` is a replacement for `my_fread`.

---

### mysql_file_fwrite

```cpp
#define mysql_file_fwrite(FD, P1, P2, P3, FD, P1, P2, P3) inline_mysql_file_fwrite(FD, P1, P2, P3)
```

Defined in psi/mysql_file.h:252

Instrumented fwrite. `mysql_file_fwrite` is a replacement for `my_fwrite`.

---

### mysql_file_fseek

```cpp
#define mysql_file_fseek(FD, P, W, F, FD, P, W, F) inline_mysql_file_fseek(FD, P, W, F)
```

Defined in psi/mysql_file.h:265

Instrumented fseek. `mysql_file_fseek` is a replacement for `my_fseek`.

---

### mysql_file_ftell

```cpp
#define mysql_file_ftell(FD, F, FD, F) inline_mysql_file_ftell(FD, F)
```

Defined in psi/mysql_file.h:278

Instrumented ftell. `mysql_file_ftell` is a replacement for `my_ftell`.

---

### mysql_file_create

```cpp
#define mysql_file_create(K, N, F1, F2, F3, K, N, F1, F2, F3) inline_mysql_file_create(N, F1, F2, F3)
```

Defined in psi/mysql_file.h:291

Instrumented create. `mysql_file_create` is a replacement for `my_create`.

---

### mysql_file_create_temp

```cpp
#define mysql_file_create_temp(K, T, D, P, M, F, K, T, D, P, M, F) inline_mysql_file_create_temp(T, D, P, M, F)
```

Defined in psi/mysql_file.h:304

Instrumented create_temp_file. `mysql_file_create_temp` is a replacement for `create_temp_file`.

---

### mysql_file_open

```cpp
#define mysql_file_open(K, N, F1, F2, K, N, F1, F2) inline_mysql_file_open(N, F1, F2)
```

Defined in psi/mysql_file.h:317

Instrumented open. `mysql_file_open` is a replacement for `my_open`.

---

### mysql_file_close

```cpp
#define mysql_file_close(FD, F, FD, F) inline_mysql_file_close(FD, F)
```

Defined in psi/mysql_file.h:330

Instrumented close. `mysql_file_close` is a replacement for `my_close`.

---

### mysql_file_read

```cpp
#define mysql_file_read(FD, B, S, F, FD, B, S, F) inline_mysql_file_read(FD, B, S, F)
```

Defined in psi/mysql_file.h:343

Instrumented read. `mysql_read` is a replacement for `my_read`.

---

### mysql_file_write

```cpp
#define mysql_file_write(FD, B, S, F, FD, B, S, F) inline_mysql_file_write(FD, B, S, F)
```

Defined in psi/mysql_file.h:356

Instrumented write. `mysql_file_write` is a replacement for `my_write`.

---

### mysql_file_pread

```cpp
#define mysql_file_pread(FD, B, S, O, F, FD, B, S, O, F) inline_mysql_file_pread(FD, B, S, O, F)
```

Defined in psi/mysql_file.h:369

Instrumented pread. `mysql_pread` is a replacement for `my_pread`.

---

### mysql_file_pwrite

```cpp
#define mysql_file_pwrite(FD, B, S, O, F, FD, B, S, O, F) inline_mysql_file_pwrite(FD, B, S, O, F)
```

Defined in psi/mysql_file.h:382

Instrumented pwrite. `mysql_file_pwrite` is a replacement for `my_pwrite`.

---

### mysql_file_seek

```cpp
#define mysql_file_seek(FD, P, W, F, FD, P, W, F) inline_mysql_file_seek(FD, P, W, F)
```

Defined in psi/mysql_file.h:395

Instrumented seek. `mysql_file_seek` is a replacement for `my_seek`.

---

### mysql_file_tell

```cpp
#define mysql_file_tell(FD, F, FD, F) inline_mysql_file_tell(FD, F)
```

Defined in psi/mysql_file.h:408

Instrumented tell. `mysql_file_tell` is a replacement for `my_tell`.

---

### mysql_file_delete

```cpp
#define mysql_file_delete(K, P1, P2, K, P1, P2) inline_mysql_file_delete(P1, P2)
```

Defined in psi/mysql_file.h:421

Instrumented delete. `mysql_file_delete` is a replacement for `my_delete`.

---

### mysql_file_rename

```cpp
#define mysql_file_rename(K, P1, P2, P3, K, P1, P2, P3) inline_mysql_file_rename(P1, P2, P3)
```

Defined in psi/mysql_file.h:434

Instrumented rename. `mysql_file_rename` is a replacement for `my_rename`.

---

### mysql_file_create_with_symlink

```cpp
#define mysql_file_create_with_symlink(K, P1, P2, P3, P4, P5, K, P1, P2, P3, P4, P5) inline_mysql_file_create_with_symlink(P1, P2, P3, P4, P5)
```

Defined in psi/mysql_file.h:449

Instrumented create with symbolic link. `mysql_file_create_with_symlink` is a replacement for `my_create_with_symlink`.

---

### mysql_file_delete_with_symlink

```cpp
#define mysql_file_delete_with_symlink(K, P1, P2, P3, K, P1, P2, P3) inline_mysql_file_delete_with_symlink(P1, P2, P3)
```

Defined in psi/mysql_file.h:463

Instrumented delete with symbolic link. `mysql_file_delete_with_symlink` is a replacement for `my_handler_delete_with_symlink`.

---

### mysql_file_rename_with_symlink

```cpp
#define mysql_file_rename_with_symlink(K, P1, P2, P3, K, P1, P2, P3) inline_mysql_file_rename_with_symlink(P1, P2, P3)
```

Defined in psi/mysql_file.h:477

Instrumented rename with symbolic link. `mysql_file_rename_with_symlink` is a replacement for `my_rename_with_symlink`.

---

### mysql_file_sync

```cpp
#define mysql_file_sync(P1, P2, P1, P2) inline_mysql_file_sync(P1, P2)
```

Defined in psi/mysql_file.h:490

Instrumented file sync. `mysql_file_sync` is a replacement for `my_sync`.

---

### PSI_IDLE_CALL

```cpp
#define PSI_IDLE_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_idle.h:39

---

### MYSQL_START_IDLE_WAIT

```cpp
#define MYSQL_START_IDLE_WAIT(LOCKER, STATE, LOCKER, STATE) do {} while (0)
```

Defined in psi/mysql_idle.h:54

Instrumentation helper for table io_waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_IDLE_WAIT](#mysql_end_idle_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |

---

### MYSQL_END_IDLE_WAIT

```cpp
#define MYSQL_END_IDLE_WAIT(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql_idle.h:69

Instrumentation helper for idle waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_IDLE_WAIT](#mysql_start_idle_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `LOCKER` |  | the locker |

---

### MYSQL_AUTHENTICATION_INTERFACE_VERSION

```cpp
#define MYSQL_AUTHENTICATION_INTERFACE_VERSION 0x0203
```

Defined in plugin_auth.h:37

---

### PASSWORD_USED_NO

```cpp
#define PASSWORD_USED_NO 0
```

Defined in plugin_auth.h:50

---

### PASSWORD_USED_YES

```cpp
#define PASSWORD_USED_YES 1
```

Defined in plugin_auth.h:51

---

### PASSWORD_USED_NO_MENTION

```cpp
#define PASSWORD_USED_NO_MENTION 2
```

Defined in plugin_auth.h:52

---

### PSI_STAGE_CALL

```cpp
#define PSI_STAGE_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_stage.h:38

---

### mysql_stage_register

```cpp
#define mysql_stage_register(P1, P2, P3, P1, P2, P3) do {} while (0)
```

Defined in psi/mysql_stage.h:49

Stage registration.

---

### MYSQL_SET_STAGE

```cpp
#define MYSQL_SET_STAGE(K, F, L, K, F, L) NULL
```

Defined in psi/mysql_stage.h:67

Set the current stage. Use this API when the file and line is passed from the caller. 
#### Returns
the current stage progress

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | the stage key |
| `F` |  | the source file name |
| `L` |  | the source file line |
| `K` |  | the stage key |
| `F` |  | the source file name |
| `L` |  | the source file line |

---

### mysql_set_stage

```cpp
#define mysql_set_stage(K, K) NULL
```

Defined in psi/mysql_stage.h:81

Set the current stage. 
#### Returns
the current stage progress

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | the stage key |
| `K` |  | the stage key |

---

### mysql_end_stage

```cpp
#define mysql_end_stage() do {} while (0)
```

Defined in psi/mysql_stage.h:93

End the last stage

---

### mysql_stage_set_work_completed

```cpp
#define mysql_stage_set_work_completed(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql_stage.h:129

---

### mysql_stage_get_work_completed

```cpp
#define mysql_stage_get_work_completed(P1, P1) do {} while (0)
```

Defined in psi/mysql_stage.h:132

---

### mysql_stage_inc_work_completed

```cpp
#define mysql_stage_inc_work_completed(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql_stage.h:140

---

### mysql_stage_set_work_estimated

```cpp
#define mysql_stage_set_work_estimated(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql_stage.h:151

---

### mysql_stage_get_work_estimated

```cpp
#define mysql_stage_get_work_estimated(P1, P1) do {} while (0)
```

Defined in psi/mysql_stage.h:154

---

### PSI_TABLE_CALL

```cpp
#define PSI_TABLE_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_table.h:39

---

### MYSQL_UNBIND_TABLE

```cpp
#define MYSQL_UNBIND_TABLE(handler, handler) do { } while(0)
```

Defined in psi/mysql_table.h:53

---

### PSI_CALL_unbind_table

```cpp
#define PSI_CALL_unbind_table(A1, A1) do { } while(0)
```

Defined in psi/mysql_table.h:55

---

### PSI_CALL_rebind_table

```cpp
#define PSI_CALL_rebind_table(A1, A2, A3, A1, A2, A3) NULL
```

Defined in psi/mysql_table.h:56

---

### PSI_CALL_close_table

```cpp
#define PSI_CALL_close_table(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_table.h:57

---

### PSI_CALL_open_table

```cpp
#define PSI_CALL_open_table(A1, A2, A1, A2) NULL
```

Defined in psi/mysql_table.h:58

---

### PSI_CALL_get_table_share

```cpp
#define PSI_CALL_get_table_share(A1, A2, A1, A2) NULL
```

Defined in psi/mysql_table.h:59

---

### PSI_CALL_release_table_share

```cpp
#define PSI_CALL_release_table_share(A1, A1) do { } while(0)
```

Defined in psi/mysql_table.h:60

---

### PSI_CALL_drop_table_share

```cpp
#define PSI_CALL_drop_table_share(A1, A2, A3, A4, A5, A1, A2, A3, A4, A5) do { } while(0)
```

Defined in psi/mysql_table.h:61

---

### MYSQL_TABLE_WAIT_VARIABLES

```cpp
#define MYSQL_TABLE_WAIT_VARIABLES(LOCKER, STATE, LOCKER, STATE)
```

Defined in psi/mysql_table.h:81

Instrumentation helper for table waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: MYSQL_START_TABLE_IO_WAIT. 

**See also**: MYSQL_END_TABLE_IO_WAIT. 

**See also**: [MYSQL_START_TABLE_LOCK_WAIT](#mysql_start_table_lock_wait). 

**See also**: [MYSQL_END_TABLE_LOCK_WAIT](#mysql_end_table_lock_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |

---

### MYSQL_START_TABLE_LOCK_WAIT

```cpp
#define MYSQL_START_TABLE_LOCK_WAIT(LOCKER, STATE, PSI, OP, FLAGS, LOCKER, STATE, PSI, OP, FLAGS) do {} while (0)
```

Defined in psi/mysql_table.h:100

Instrumentation helper for table lock waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_TABLE_LOCK_WAIT](#mysql_end_table_lock_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `PSI` |  | the instrumented table |
| `OP` |  | the table operation to be performed |
| `FLAGS` |  | per table operation flags. |
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `PSI` |  | the instrumented table |
| `OP` |  | the table operation to be performed |
| `FLAGS` |  | per table operation flags. |

---

### MYSQL_END_TABLE_LOCK_WAIT

```cpp
#define MYSQL_END_TABLE_LOCK_WAIT(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql_table.h:115

Instrumentation helper for table lock waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_TABLE_LOCK_WAIT](#mysql_start_table_lock_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `LOCKER` |  | the locker |

---

### MYSQL_UNLOCK_TABLE

```cpp
#define MYSQL_UNLOCK_TABLE(T, T) do {} while (0)
```

Defined in psi/mysql_table.h:123

---

### MY_GLOBAL_INCLUDED

```cpp
#define MY_GLOBAL_INCLUDED
```

Defined in psi/psi_abi_v2.h:36

---

### USE_PSI_1

```cpp
#define USE_PSI_1
```

Defined in psi/psi_abi_v1.h:34

---

### HAVE_PSI_INTERFACE

```cpp
#define HAVE_PSI_INTERFACE
```

Defined in psi/psi_abi_v2.h:35

---

### MY_GLOBAL_INCLUDED

```cpp
#define MY_GLOBAL_INCLUDED
```

Defined in psi/psi_abi_v2.h:36

---

### USE_PSI_2

```cpp
#define USE_PSI_2
```

Defined in psi/psi_abi_v2.h:34

---

### HAVE_PSI_INTERFACE

```cpp
#define HAVE_PSI_INTERFACE
```

Defined in psi/psi_abi_v2.h:35

---

### MY_GLOBAL_INCLUDED

```cpp
#define MY_GLOBAL_INCLUDED
```

Defined in psi/psi_abi_v2.h:36

---

### MY_MD5_HASH_SIZE

```cpp
#define MY_MD5_HASH_SIZE 16 /* Hash size in bytes */
```

Defined in service_md5.h:40

---

### my_md5

```cpp
#define my_md5(A, B, C, A, B, C) my_md5_service->my_md5_type(A,B,C)
```

Defined in service_md5.h:53

---

### my_md5_multi

```cpp
#define my_md5_multi my_md5_service->my_md5_multi_type
```

Defined in service_md5.h:54

---

### my_md5_context_size

```cpp
#define my_md5_context_size() my_md5_service->my_md5_context_size_type()
```

Defined in service_md5.h:55

---

### my_md5_init

```cpp
#define my_md5_init(A, A) my_md5_service->my_md5_init_type(A)
```

Defined in service_md5.h:56

---

### my_md5_input

```cpp
#define my_md5_input(A, B, C, A, B, C) my_md5_service->my_md5_input_type(A,B,C)
```

Defined in service_md5.h:57

---

### my_md5_result

```cpp
#define my_md5_result(A, B, A, B) my_md5_service->my_md5_result_type(A,B)
```

Defined in service_md5.h:58

---

### mysql_init

```cpp
#define mysql_init(mysql, mysql) sql_service->mysql_init_func(mysql)
```

Defined in service_sql.h:90

---

### mysql_real_connect_local

```cpp
#define mysql_real_connect_local(mysql, mysql) sql_service->mysql_real_connect_local_func(mysql)
```

Defined in service_sql.h:91

---

### mysql_real_connect

```cpp
#define mysql_real_connect(mysql, host, user, password, db, port, socket, flags, mysql, host, user, password, db, port, socket, flags) sql_service->mysql_real_connect_func(mysql,host,user,password,db,port,socket,flags)
```

Defined in service_sql.h:92

---

### mysql_errno

```cpp
#define mysql_errno(mysql, mysql) sql_service->mysql_errno_func(mysql)
```

Defined in service_sql.h:94

---

### mysql_error

```cpp
#define mysql_error(mysql, mysql) sql_service->mysql_error_func(mysql)
```

Defined in service_sql.h:95

---

### mysql_real_query

```cpp
#define mysql_real_query sql_service->mysql_real_query_func
```

Defined in service_sql.h:96

---

### mysql_affected_rows

```cpp
#define mysql_affected_rows(mysql, mysql) sql_service->mysql_affected_rows_func(mysql)
```

Defined in service_sql.h:97

---

### mysql_num_rows

```cpp
#define mysql_num_rows(result, result) sql_service->mysql_num_rows_func(result)
```

Defined in service_sql.h:98

---

### mysql_store_result

```cpp
#define mysql_store_result(mysql, mysql) sql_service->mysql_store_result_func(mysql)
```

Defined in service_sql.h:99

---

### mysql_free_result

```cpp
#define mysql_free_result(result, result) sql_service->mysql_free_result_func(result)
```

Defined in service_sql.h:100

---

### mysql_fetch_row

```cpp
#define mysql_fetch_row(result, result) sql_service->mysql_fetch_row_func(result)
```

Defined in service_sql.h:101

---

### mysql_close

```cpp
#define mysql_close(mysql, mysql) sql_service->mysql_close_func(mysql)
```

Defined in service_sql.h:102

---

### mysql_options

```cpp
#define mysql_options(mysql, option, arg, mysql, option, arg) sql_service->mysql_options_func(mysql,option,arg)
```

Defined in service_sql.h:103

---

### mysql_fetch_lengths

```cpp
#define mysql_fetch_lengths(result, result) sql_service->mysql_fetch_lengths_func(result)
```

Defined in service_sql.h:104

---

### mysql_set_character_set

```cpp
#define mysql_set_character_set(mysql, cs_name, mysql, cs_name) sql_service->mysql_set_character_set_func(mysql,cs_name)
```

Defined in service_sql.h:105

---

### mysql_num_fields

```cpp
#define mysql_num_fields(result, result) sql_service->mysql_num_fields_func(result)
```

Defined in service_sql.h:106

---

### mysql_select_db

```cpp
#define mysql_select_db(mysql, db, mysql, db) sql_service->mysql_select_db_func(mysql,db)
```

Defined in service_sql.h:107

---

### mysql_use_result

```cpp
#define mysql_use_result(mysql, mysql) sql_service->mysql_use_result_func(mysql)
```

Defined in service_sql.h:108

---

### mysql_fetch_fields

```cpp
#define mysql_fetch_fields(result, result) sql_service->mysql_fetch_fields_func(result)
```

Defined in service_sql.h:109

---

### mysql_real_escape_string

```cpp
#define mysql_real_escape_string(mysql, to, from, length, mysql, to, from, length) sql_service->mysql_real_escape_string_func(mysql,to,from,length)
```

Defined in service_sql.h:110

---

### mysql_ssl_set

```cpp
#define mysql_ssl_set(mysql, key, cert, ca, capath, cipher, mysql, key, cert, ca, capath, cipher) sql_service->mysql_ssl_set_func(mysql,key,cert,ca,capath,cipher)
```

Defined in service_sql.h:111

---

### get_current_thd

```cpp
#define get_current_thd() thd_service->get_current_thd()
```

Defined in service_thd.h:49

Current session (thd) accessor 
#### Returns
pointer to current thd

---

### MYSQL_AUDIT_CLASS_MASK_SIZE

```cpp
#define MYSQL_AUDIT_CLASS_MASK_SIZE 1
```

Defined in plugin_audit.h:34

---

### MYSQL_AUDIT_INTERFACE_VERSION

```cpp
#define MYSQL_AUDIT_INTERFACE_VERSION 0x0304
```

Defined in plugin_audit.h:36

---

### MYSQL_AUDIT_GENERAL_CLASS

```cpp
#define MYSQL_AUDIT_GENERAL_CLASS 0
```

Defined in plugin_audit.h:50

---

### MYSQL_AUDIT_GENERAL_CLASSMASK

```cpp
#define MYSQL_AUDIT_GENERAL_CLASSMASK (1 << MYSQL_AUDIT_GENERAL_CLASS)
```

Defined in plugin_audit.h:51

---

### MYSQL_AUDIT_GENERAL_LOG

```cpp
#define MYSQL_AUDIT_GENERAL_LOG 0
```

Defined in plugin_audit.h:52

---

### MYSQL_AUDIT_GENERAL_ERROR

```cpp
#define MYSQL_AUDIT_GENERAL_ERROR 1
```

Defined in plugin_audit.h:53

---

### MYSQL_AUDIT_GENERAL_RESULT

```cpp
#define MYSQL_AUDIT_GENERAL_RESULT 2
```

Defined in plugin_audit.h:54

---

### MYSQL_AUDIT_GENERAL_STATUS

```cpp
#define MYSQL_AUDIT_GENERAL_STATUS 3
```

Defined in plugin_audit.h:55

---

### MYSQL_AUDIT_GENERAL_WARNING

```cpp
#define MYSQL_AUDIT_GENERAL_WARNING 4
```

Defined in plugin_audit.h:56

---

### MYSQL_AUDIT_CONNECTION_CLASS

```cpp
#define MYSQL_AUDIT_CONNECTION_CLASS 1
```

Defined in plugin_audit.h:98

---

### MYSQL_AUDIT_CONNECTION_CLASSMASK

```cpp
#define MYSQL_AUDIT_CONNECTION_CLASSMASK (1 << MYSQL_AUDIT_CONNECTION_CLASS)
```

Defined in plugin_audit.h:99

---

### MYSQL_AUDIT_CONNECTION_CONNECT

```cpp
#define MYSQL_AUDIT_CONNECTION_CONNECT 0
```

Defined in plugin_audit.h:100

---

### MYSQL_AUDIT_CONNECTION_DISCONNECT

```cpp
#define MYSQL_AUDIT_CONNECTION_DISCONNECT 1
```

Defined in plugin_audit.h:101

---

### MYSQL_AUDIT_CONNECTION_CHANGE_USER

```cpp
#define MYSQL_AUDIT_CONNECTION_CHANGE_USER 2
```

Defined in plugin_audit.h:102

---

### MYSQL_AUDIT_TABLE_CLASS

```cpp
#define MYSQL_AUDIT_TABLE_CLASS 15
```

Defined in plugin_audit.h:145

---

### MYSQL_AUDIT_TABLE_CLASSMASK

```cpp
#define MYSQL_AUDIT_TABLE_CLASSMASK (1 << MYSQL_AUDIT_TABLE_CLASS)
```

Defined in plugin_audit.h:146

---

### MYSQL_AUDIT_TABLE_LOCK

```cpp
#define MYSQL_AUDIT_TABLE_LOCK 0
```

Defined in plugin_audit.h:147

---

### MYSQL_AUDIT_TABLE_CREATE

```cpp
#define MYSQL_AUDIT_TABLE_CREATE 1
```

Defined in plugin_audit.h:148

---

### MYSQL_AUDIT_TABLE_DROP

```cpp
#define MYSQL_AUDIT_TABLE_DROP 2
```

Defined in plugin_audit.h:149

---

### MYSQL_AUDIT_TABLE_RENAME

```cpp
#define MYSQL_AUDIT_TABLE_RENAME 3
```

Defined in plugin_audit.h:150

---

### MYSQL_AUDIT_TABLE_ALTER

```cpp
#define MYSQL_AUDIT_TABLE_ALTER 4
```

Defined in plugin_audit.h:151

---

### MYSQL_MEMORY_H

```cpp
#define MYSQL_MEMORY_H
```

Defined in psi/mysql_memory.h:34

---

### PSI_CALL_memory_alloc

```cpp
#define PSI_CALL_memory_alloc(A1, A2, A3, A1, A2, A3) 0
```

Defined in psi/mysql_memory.h:44

---

### PSI_CALL_memory_free

```cpp
#define PSI_CALL_memory_free(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql_memory.h:45

---

### PSI_CALL_memory_realloc

```cpp
#define PSI_CALL_memory_realloc(A1, A2, A3, A4, A1, A2, A3, A4) 0
```

Defined in psi/mysql_memory.h:46

---

### PSI_CALL_register_memory

```cpp
#define PSI_CALL_register_memory(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql_memory.h:47

---

### PSI_MEMORY_CALL

```cpp
#define PSI_MEMORY_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_memory.h:51

---

### mysql_memory_register

```cpp
#define mysql_memory_register(P1, P2, P3, P1, P2, P3) inline_mysql_memory_register(P1, P2, P3)
```

Defined in psi/mysql_memory.h:58

Memory registration.

---

### SOCKBUF_T

```cpp
#define SOCKBUF_T void
```

Defined in psi/mysql_socket.h:53

---

### PSI_SOCKET_CALL

```cpp
#define PSI_SOCKET_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_socket.h:59

---

### mysql_socket_register

```cpp
#define mysql_socket_register(P1, P2, P3, P1, P2, P3) inline_mysql_socket_register(P1, P2, P3)
```

Defined in psi/mysql_socket.h:67

Socket registration.

---

### MYSQL_INVALID_SOCKET

```cpp
#define MYSQL_INVALID_SOCKET mysql_socket_invalid()
```

Defined in psi/mysql_socket.h:109

MYSQL_SOCKET initial value.

---

### MYSQL_SOCKET_WAIT_VARIABLES

```cpp
#define MYSQL_SOCKET_WAIT_VARIABLES(LOCKER, STATE, LOCKER, STATE) struct PSI_socket_locker* LOCKER; \
    PSI_socket_locker_state STATE;
```

Defined in psi/mysql_socket.h:204

Instrumentation helper for socket waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: [MYSQL_START_SOCKET_WAIT](#mysql_start_socket_wait). 

**See also**: [MYSQL_END_SOCKET_WAIT](#mysql_end_socket_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | locker |
| `STATE` |  | locker state |
| `LOCKER` |  | locker |
| `STATE` |  | locker state |

---

### MYSQL_START_SOCKET_WAIT

```cpp
#define MYSQL_START_SOCKET_WAIT(LOCKER, STATE, SOCKET, OP, COUNT, LOCKER, STATE, SOCKET, OP, COUNT) LOCKER= inline_mysql_start_socket_wait(STATE, SOCKET, OP, COUNT,\
                                           __FILE__, __LINE__)
```

Defined in psi/mysql_socket.h:223

Instrumentation helper for socket waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_SOCKET_WAIT](#mysql_end_socket_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | locker |
| `STATE` |  | locker state |
| `SOCKET` |  | instrumented socket |
| `OP` |  | The socket operation to be performed |
| `COUNT` |  | bytes to be written/read |
| `LOCKER` |  | locker |
| `STATE` |  | locker state |
| `SOCKET` |  | instrumented socket |
| `OP` |  | The socket operation to be performed |
| `COUNT` |  | bytes to be written/read |

---

### MYSQL_END_SOCKET_WAIT

```cpp
#define MYSQL_END_SOCKET_WAIT(LOCKER, COUNT, LOCKER, COUNT) inline_mysql_end_socket_wait(LOCKER, COUNT)
```

Defined in psi/mysql_socket.h:240

Instrumentation helper for socket waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_SOCKET_WAIT](#mysql_start_socket_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | locker |
| `COUNT` |  | actual bytes written/read, or -1 |
| `LOCKER` |  | locker |
| `COUNT` |  | actual bytes written/read, or -1 |

---

### MYSQL_SOCKET_SET_STATE

```cpp
#define MYSQL_SOCKET_SET_STATE(SOCKET, STATE, SOCKET, STATE) inline_mysql_socket_set_state(SOCKET, STATE)
```

Defined in psi/mysql_socket.h:255

Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI_socket_state

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `SOCKET` |  | the instrumented socket |
| `STATE` |  | the new state |
| `SOCKET` |  | the instrumented socket |
| `STATE` |  | the new state |

---

### mysql_socket_fd

```cpp
#define mysql_socket_fd(K, F, K, F) inline_mysql_socket_fd(K, F)
```

Defined in psi/mysql_socket.h:319

Create a socket. `mysql_socket_fd` is a replacement for `socket`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | PSI_socket_key for this instrumented socket |
| `F` |  | File descriptor |
| `K` |  | PSI_socket_key for this instrumented socket |
| `F` |  | File descriptor |

---

### mysql_socket_socket

```cpp
#define mysql_socket_socket(K, D, T, P, K, D, T, P) inline_mysql_socket_socket(K, D, T, P)
```

Defined in psi/mysql_socket.h:337

Create a socket. `mysql_socket_socket` is a replacement for `socket`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | PSI_socket_key for this instrumented socket |
| `D` |  | Socket domain |
| `T` |  | Protocol type |
| `P` |  | Transport protocol |
| `K` |  | PSI_socket_key for this instrumented socket |
| `D` |  | Socket domain |
| `T` |  | Protocol type |
| `P` |  | Transport protocol |

---

### mysql_socket_bind

```cpp
#define mysql_socket_bind(FD, AP, L, FD, AP, L) inline_mysql_socket_bind(__FILE__, __LINE__, FD, AP, L)
```

Defined in psi/mysql_socket.h:353

Bind a socket to a local port number and IP address `mysql_socket_bind` is a replacement for `bind`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to local port number and IP address in sockaddr structure |
| `L` |  | Length of sockaddr structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to local port number and IP address in sockaddr structure |
| `L` |  | Length of sockaddr structure |

---

### mysql_socket_getsockname

```cpp
#define mysql_socket_getsockname(FD, AP, LP, FD, AP, LP) inline_mysql_socket_getsockname(__FILE__, __LINE__, FD, AP, LP)
```

Defined in psi/mysql_socket.h:369

Return port number and IP address of the local host `mysql_socket_getsockname` is a replacement for `getsockname`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to returned address of local host in `sockaddr` structure |
| `LP` |  | Pointer to length of `sockaddr` structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to returned address of local host in `sockaddr` structure |
| `LP` |  | Pointer to length of `sockaddr` structure |

---

### mysql_socket_connect

```cpp
#define mysql_socket_connect(FD, AP, L, FD, AP, L) inline_mysql_socket_connect(__FILE__, __LINE__, FD, AP, L)
```

Defined in psi/mysql_socket.h:385

Establish a connection to a remote host. `mysql_socket_connect` is a replacement for `connect`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to target address in sockaddr structure |
| `L` |  | Length of sockaddr structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to target address in sockaddr structure |
| `L` |  | Length of sockaddr structure |

---

### mysql_socket_getpeername

```cpp
#define mysql_socket_getpeername(FD, AP, LP, FD, AP, LP) inline_mysql_socket_getpeername(__FILE__, __LINE__, FD, AP, LP)
```

Defined in psi/mysql_socket.h:401

Get port number and IP address of remote host that a socket is connected to. `mysql_socket_getpeername` is a replacement for `getpeername`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `AP` |  | Pointer to returned address of remote host in sockaddr structure |
| `LP` |  | Pointer to length of sockaddr structure |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `AP` |  | Pointer to returned address of remote host in sockaddr structure |
| `LP` |  | Pointer to length of sockaddr structure |

---

### mysql_socket_send

```cpp
#define mysql_socket_send(FD, B, N, FL, FD, B, N, FL) inline_mysql_socket_send(__FILE__, __LINE__, FD, B, N, FL)
```

Defined in psi/mysql_socket.h:418

Send data from the buffer, B, to a connected socket. `mysql_socket_send` is a replacement for `send`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `B` |  | Buffer to send |
| `N` |  | Number of bytes to send |
| `FL` |  | Control flags |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `B` |  | Buffer to send |
| `N` |  | Number of bytes to send |
| `FL` |  | Control flags |

---

### mysql_socket_recv

```cpp
#define mysql_socket_recv(FD, B, N, FL, FD, B, N, FL) inline_mysql_socket_recv(__FILE__, __LINE__, FD, B, N, FL)
```

Defined in psi/mysql_socket.h:435

Receive data from a connected socket. `mysql_socket_recv` is a replacement for `recv`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `B` |  | Buffer to receive to |
| `N` |  | Maximum bytes to receive |
| `FL` |  | Control flags |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `B` |  | Buffer to receive to |
| `N` |  | Maximum bytes to receive |
| `FL` |  | Control flags |

---

### mysql_socket_sendto

```cpp
#define mysql_socket_sendto(FD, B, N, FL, AP, L, FD, B, N, FL, AP, L) inline_mysql_socket_sendto(__FILE__, __LINE__, FD, B, N, FL, AP, L)
```

Defined in psi/mysql_socket.h:454

Send data to a socket at the specified address. `mysql_socket_sendto` is a replacement for `sendto`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `B` |  | Buffer to send |
| `N` |  | Number of bytes to send |
| `FL` |  | Control flags |
| `AP` |  | Pointer to destination sockaddr structure |
| `L` |  | Size of sockaddr structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `B` |  | Buffer to send |
| `N` |  | Number of bytes to send |
| `FL` |  | Control flags |
| `AP` |  | Pointer to destination sockaddr structure |
| `L` |  | Size of sockaddr structure |

---

### mysql_socket_recvfrom

```cpp
#define mysql_socket_recvfrom(FD, B, N, FL, AP, LP, FD, B, N, FL, AP, LP) inline_mysql_socket_recvfrom(__FILE__, __LINE__, FD, B, N, FL, AP, LP)
```

Defined in psi/mysql_socket.h:473

Receive data from a socket and return source address information `mysql_socket_recvfrom` is a replacement for `recvfrom`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `B` |  | Buffer to receive to |
| `N` |  | Maximum bytes to receive |
| `FL` |  | Control flags |
| `AP` |  | Pointer to source address in sockaddr_storage structure |
| `LP` |  | Size of sockaddr_storage structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `B` |  | Buffer to receive to |
| `N` |  | Maximum bytes to receive |
| `FL` |  | Control flags |
| `AP` |  | Pointer to source address in sockaddr_storage structure |
| `LP` |  | Size of sockaddr_storage structure |

---

### mysql_socket_getsockopt

```cpp
#define mysql_socket_getsockopt(FD, LV, ON, OP, OL, FD, LV, ON, OP, OL) inline_mysql_socket_getsockopt(__FILE__, __LINE__, FD, LV, ON, OP, OL)
```

Defined in psi/mysql_socket.h:491

Get a socket option for the specified socket. `mysql_socket_getsockopt` is a replacement for `getsockopt`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `LV` |  | Protocol level |
| `ON` |  | Option to query |
| `OP` |  | Buffer which will contain the value for the requested option |
| `OL` |  | Pointer to length of OP |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `LV` |  | Protocol level |
| `ON` |  | Option to query |
| `OP` |  | Buffer which will contain the value for the requested option |
| `OL` |  | Pointer to length of OP |

---

### mysql_socket_setsockopt

```cpp
#define mysql_socket_setsockopt(FD, LV, ON, OP, OL, FD, LV, ON, OP, OL) inline_mysql_socket_setsockopt(__FILE__, __LINE__, FD, LV, ON, OP, OL)
```

Defined in psi/mysql_socket.h:509

Set a socket option for the specified socket. `mysql_socket_setsockopt` is a replacement for `setsockopt`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `LV` |  | Protocol level |
| `ON` |  | Option to modify |
| `OP` |  | Buffer containing the value for the specified option |
| `OL` |  | Pointer to length of OP |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `LV` |  | Protocol level |
| `ON` |  | Option to modify |
| `OP` |  | Buffer containing the value for the specified option |
| `OL` |  | Pointer to length of OP |

---

### mysql_sock_set_nonblocking

```cpp
#define mysql_sock_set_nonblocking(FD, FD) inline_mysql_sock_set_nonblocking(__FILE__, __LINE__, FD)
```

Defined in psi/mysql_socket.h:522

Set socket to non-blocking.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | instrumented socket descriptor |
| `FD` |  | instrumented socket descriptor |

---

### mysql_socket_listen

```cpp
#define mysql_socket_listen(FD, N, FD, N) inline_mysql_socket_listen(__FILE__, __LINE__, FD, N)
```

Defined in psi/mysql_socket.h:537

Set socket state to listen for an incoming connection. `mysql_socket_listen` is a replacement for `listen`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor, bound and connected |
| `N` |  | Maximum number of pending connections allowed. |
| `FD` |  | Instrumented socket descriptor, bound and connected |
| `N` |  | Maximum number of pending connections allowed. |

---

### mysql_socket_accept

```cpp
#define mysql_socket_accept(K, FD, AP, LP, K, FD, AP, LP) inline_mysql_socket_accept(__FILE__, __LINE__, K, FD, AP, LP)
```

Defined in psi/mysql_socket.h:554

Accept a connection from any remote host; TCP only. `mysql_socket_accept` is a replacement for `accept`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | PSI_socket_key for this instrumented socket |
| `FD` |  | Instrumented socket descriptor, bound and placed in a listen state |
| `AP` |  | Pointer to sockaddr structure with returned IP address and port of connected host |
| `LP` |  | Pointer to length of valid information in AP |
| `K` |  | PSI_socket_key for this instrumented socket |
| `FD` |  | Instrumented socket descriptor, bound and placed in a listen state |
| `AP` |  | Pointer to sockaddr structure with returned IP address and port of connected host |
| `LP` |  | Pointer to length of valid information in AP |

---

### mysql_socket_close

```cpp
#define mysql_socket_close(FD, FD) inline_mysql_socket_close(__FILE__, __LINE__, FD)
```

Defined in psi/mysql_socket.h:568

Close a socket and sever any connections. `mysql_socket_close` is a replacement for `close`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |

---

### mysql_socket_shutdown

```cpp
#define mysql_socket_shutdown(FD, H, FD, H) inline_mysql_socket_shutdown(__FILE__, __LINE__, FD, H)
```

Defined in psi/mysql_socket.h:583

Disable receives and/or sends on a socket. `mysql_socket_shutdown` is a replacement for `shutdown`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `H` |  | Specifies which operations to shutdown |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `H` |  | Specifies which operations to shutdown |

---

### PSI_MUTEX_CALL

```cpp
#define PSI_MUTEX_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_thread.h:79

---

### PSI_RWLOCK_CALL

```cpp
#define PSI_RWLOCK_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_thread.h:83

---

### PSI_COND_CALL

```cpp
#define PSI_COND_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_thread.h:87

---

### PSI_THREAD_CALL

```cpp
#define PSI_THREAD_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_thread.h:91

---

### PSI_CALL_delete_current_thread

```cpp
#define PSI_CALL_delete_current_thread() do { } while(0)
```

Defined in psi/mysql_thread.h:111

---

### PSI_CALL_get_thread

```cpp
#define PSI_CALL_get_thread() NULL
```

Defined in psi/mysql_thread.h:112

---

### PSI_CALL_new_thread

```cpp
#define PSI_CALL_new_thread(A1, A2, A3, A1, A2, A3) NULL
```

Defined in psi/mysql_thread.h:113

---

### PSI_CALL_register_thread

```cpp
#define PSI_CALL_register_thread(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql_thread.h:114

---

### PSI_CALL_set_thread

```cpp
#define PSI_CALL_set_thread(A1, A1) do { } while(0)
```

Defined in psi/mysql_thread.h:115

---

### PSI_CALL_set_thread_THD

```cpp
#define PSI_CALL_set_thread_THD(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:116

---

### PSI_CALL_set_thread_connect_attrs

```cpp
#define PSI_CALL_set_thread_connect_attrs(A1, A2, A3, A1, A2, A3) 0
```

Defined in psi/mysql_thread.h:117

---

### PSI_CALL_set_thread_db

```cpp
#define PSI_CALL_set_thread_db(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:118

---

### PSI_CALL_set_thread_id

```cpp
#define PSI_CALL_set_thread_id(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:119

---

### PSI_CALL_set_thread_os_id

```cpp
#define PSI_CALL_set_thread_os_id(A1, A1) do { } while(0)
```

Defined in psi/mysql_thread.h:120

---

### PSI_CALL_set_thread_info

```cpp
#define PSI_CALL_set_thread_info(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:121

---

### PSI_CALL_set_thread_start_time

```cpp
#define PSI_CALL_set_thread_start_time(A1, A1) do { } while(0)
```

Defined in psi/mysql_thread.h:122

---

### PSI_CALL_set_thread_account

```cpp
#define PSI_CALL_set_thread_account(A1, A2, A3, A4, A1, A2, A3, A4) do { } while(0)
```

Defined in psi/mysql_thread.h:123

---

### PSI_CALL_spawn_thread

```cpp
#define PSI_CALL_spawn_thread(A1, A2, A3, A4, A5, A1, A2, A3, A4, A5) 0
```

Defined in psi/mysql_thread.h:124

---

### PSI_CALL_set_connection_type

```cpp
#define PSI_CALL_set_connection_type(A, A) do { } while(0)
```

Defined in psi/mysql_thread.h:125

---

### mysql_mutex_is_owner

```cpp
#define mysql_mutex_is_owner(M, M) safe_mutex_is_owner(&(M)->m_mutex)
```

Defined in psi/mysql_thread.h:266

---

### mysql_mutex_assert_owner

```cpp
#define mysql_mutex_assert_owner(M, M) safe_mutex_assert_owner(&(M)->m_mutex)
```

Defined in psi/mysql_thread.h:273

Wrapper, to use safe_mutex_assert_owner with instrumented mutexes. `mysql_mutex_assert_owner` is a drop-in replacement for `safe_mutex_assert_owner`.

---

### mysql_mutex_assert_not_owner

```cpp
#define mysql_mutex_assert_not_owner(M, M) safe_mutex_assert_not_owner(&(M)->m_mutex)
```

Defined in psi/mysql_thread.h:282

Wrapper, to use safe_mutex_assert_not_owner with instrumented mutexes. `mysql_mutex_assert_not_owner` is a drop-in replacement for `safe_mutex_assert_not_owner`.

---

### mysql_mutex_setflags

```cpp
#define mysql_mutex_setflags(M, F, M, F) safe_mutex_setflags(&(M)->m_mutex, (F))
```

Defined in psi/mysql_thread.h:285

---

### mysql_prlock_assert_write_owner

```cpp
#define mysql_prlock_assert_write_owner(M, M) rw_pr_lock_assert_write_owner(&(M)->m_prlock)
```

Defined in psi/mysql_thread.h:293

Drop-in replacement for `rw_pr_lock_assert_write_owner`.

---

### mysql_prlock_assert_not_write_owner

```cpp
#define mysql_prlock_assert_not_write_owner(M, M) rw_pr_lock_assert_not_write_owner(&(M)->m_prlock)
```

Defined in psi/mysql_thread.h:301

Drop-in replacement for `rw_pr_lock_assert_not_write_owner`.

---

### mysql_mutex_register

```cpp
#define mysql_mutex_register(P1, P2, P3, P1, P2, P3) inline_mysql_mutex_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:308

Mutex registration.

---

### mysql_mutex_init

```cpp
#define mysql_mutex_init(K, M, A, K, M, A) inline_mysql_mutex_init(M, A)
```

Defined in psi/mysql_thread.h:333

Instrumented mutex_init. `mysql_mutex_init` is a replacement for `pthread_mutex_init`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_mutex_key for this instrumented mutex |
| `M` |  | The mutex to initialize |
| `A` |  | Mutex attributes |
| `K` |  | The PSI_mutex_key for this instrumented mutex |
| `M` |  | The mutex to initialize |
| `A` |  | Mutex attributes |

---

### mysql_mutex_destroy

```cpp
#define mysql_mutex_destroy(M, M) inline_mysql_mutex_destroy(M)
```

Defined in psi/mysql_thread.h:348

Instrumented mutex_destroy. `mysql_mutex_destroy` is a drop-in replacement for `pthread_mutex_destroy`.

---

### mysql_mutex_lock

```cpp
#define mysql_mutex_lock(M, M) inline_mysql_mutex_lock(M)
```

Defined in psi/mysql_thread.h:363

Instrumented mutex_lock. `mysql_mutex_lock` is a drop-in replacement for `pthread_mutex_lock`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `M` |  | The mutex to lock |
| `M` |  | The mutex to lock |

---

### mysql_mutex_trylock

```cpp
#define mysql_mutex_trylock(M, M) inline_mysql_mutex_trylock(M)
```

Defined in psi/mysql_thread.h:378

Instrumented mutex_lock. `mysql_mutex_trylock` is a drop-in replacement for `pthread_mutex_trylock`.

---

### mysql_mutex_unlock

```cpp
#define mysql_mutex_unlock(M, M) inline_mysql_mutex_unlock(M)
```

Defined in psi/mysql_thread.h:391

Instrumented mutex_unlock. `mysql_mutex_unlock` is a drop-in replacement for `pthread_mutex_unlock`.

---

### mysql_rwlock_register

```cpp
#define mysql_rwlock_register(P1, P2, P3, P1, P2, P3) inline_mysql_rwlock_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:399

Rwlock registration.

---

### mysql_rwlock_init

```cpp
#define mysql_rwlock_init(K, RW, K, RW) inline_mysql_rwlock_init(RW)
```

Defined in psi/mysql_thread.h:413

Instrumented rwlock_init. `mysql_rwlock_init` is a replacement for `pthread_rwlock_init`. Note that pthread_rwlockattr_t is not supported in MySQL.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_rwlock_key for this instrumented rwlock |
| `RW` |  | The rwlock to initialize |
| `K` |  | The PSI_rwlock_key for this instrumented rwlock |
| `RW` |  | The rwlock to initialize |

---

### mysql_prlock_init

```cpp
#define mysql_prlock_init(K, RW, K, RW) inline_mysql_prlock_init(RW)
```

Defined in psi/mysql_thread.h:426

Instrumented rw_pr_init. `mysql_prlock_init` is a replacement for `rw_pr_init`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_rwlock_key for this instrumented prlock |
| `RW` |  | The prlock to initialize |
| `K` |  | The PSI_rwlock_key for this instrumented prlock |
| `RW` |  | The prlock to initialize |

---

### mysql_rwlock_destroy

```cpp
#define mysql_rwlock_destroy(RW, RW) inline_mysql_rwlock_destroy(RW)
```

Defined in psi/mysql_thread.h:435

Instrumented rwlock_destroy. `mysql_rwlock_destroy` is a drop-in replacement for `pthread_rwlock_destroy`.

---

### mysql_prlock_destroy

```cpp
#define mysql_prlock_destroy(RW, RW) inline_mysql_prlock_destroy(RW)
```

Defined in psi/mysql_thread.h:443

Instrumented rw_pr_destroy. `mysql_prlock_destroy` is a drop-in replacement for `rw_pr_destroy`.

---

### mysql_rwlock_rdlock

```cpp
#define mysql_rwlock_rdlock(RW, RW) inline_mysql_rwlock_rdlock(RW)
```

Defined in psi/mysql_thread.h:455

Instrumented rwlock_rdlock. `mysql_rwlock_rdlock` is a drop-in replacement for `pthread_rwlock_rdlock`.

---

### mysql_prlock_rdlock

```cpp
#define mysql_prlock_rdlock(RW, RW) inline_mysql_prlock_rdlock(RW)
```

Defined in psi/mysql_thread.h:469

Instrumented rw_pr_rdlock. `mysql_prlock_rdlock` is a drop-in replacement for `rw_pr_rdlock`.

---

### mysql_rwlock_wrlock

```cpp
#define mysql_rwlock_wrlock(RW, RW) inline_mysql_rwlock_wrlock(RW)
```

Defined in psi/mysql_thread.h:483

Instrumented rwlock_wrlock. `mysql_rwlock_wrlock` is a drop-in replacement for `pthread_rwlock_wrlock`.

---

### mysql_prlock_wrlock

```cpp
#define mysql_prlock_wrlock(RW, RW) inline_mysql_prlock_wrlock(RW)
```

Defined in psi/mysql_thread.h:497

Instrumented rw_pr_wrlock. `mysql_prlock_wrlock` is a drop-in replacement for `rw_pr_wrlock`.

---

### mysql_rwlock_tryrdlock

```cpp
#define mysql_rwlock_tryrdlock(RW, RW) inline_mysql_rwlock_tryrdlock(RW)
```

Defined in psi/mysql_thread.h:511

Instrumented rwlock_tryrdlock. `mysql_rwlock_tryrdlock` is a drop-in replacement for `pthread_rwlock_tryrdlock`.

---

### mysql_rwlock_trywrlock

```cpp
#define mysql_rwlock_trywrlock(RW, RW) inline_mysql_rwlock_trywrlock(RW)
```

Defined in psi/mysql_thread.h:525

Instrumented rwlock_trywrlock. `mysql_rwlock_trywrlock` is a drop-in replacement for `pthread_rwlock_trywrlock`.

---

### mysql_rwlock_unlock

```cpp
#define mysql_rwlock_unlock(RW, RW) inline_mysql_rwlock_unlock(RW)
```

Defined in psi/mysql_thread.h:535

Instrumented rwlock_unlock. `mysql_rwlock_unlock` is a drop-in replacement for `pthread_rwlock_unlock`.

---

### mysql_prlock_unlock

```cpp
#define mysql_prlock_unlock(RW, RW) inline_mysql_prlock_unlock(RW)
```

Defined in psi/mysql_thread.h:543

Instrumented rw_pr_unlock. `mysql_prlock_unlock` is a drop-in replacement for `rw_pr_unlock`.

---

### mysql_cond_register

```cpp
#define mysql_cond_register(P1, P2, P3, P1, P2, P3) inline_mysql_cond_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:549

Cond registration.

---

### mysql_cond_init

```cpp
#define mysql_cond_init(K, C, A, K, C, A) inline_mysql_cond_init(C, A)
```

Defined in psi/mysql_thread.h:563

Instrumented cond_init. `mysql_cond_init` is a replacement for `pthread_cond_init`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_cond_key for this instrumented cond |
| `C` |  | The cond to initialize |
| `A` |  | Condition attributes |
| `K` |  | The PSI_cond_key for this instrumented cond |
| `C` |  | The cond to initialize |
| `A` |  | Condition attributes |

---

### mysql_cond_destroy

```cpp
#define mysql_cond_destroy(C, C) inline_mysql_cond_destroy(C)
```

Defined in psi/mysql_thread.h:571

Instrumented cond_destroy. `mysql_cond_destroy` is a drop-in replacement for `pthread_cond_destroy`.

---

### mysql_cond_wait

```cpp
#define mysql_cond_wait(C, M, C, M) inline_mysql_cond_wait(C, M)
```

Defined in psi/mysql_thread.h:582

Instrumented cond_wait. `mysql_cond_wait` is a drop-in replacement for `pthread_cond_wait`.

---

### mysql_cond_timedwait

```cpp
#define mysql_cond_timedwait(C, M, W, C, M, W) inline_mysql_cond_timedwait(C, M, W)
```

Defined in psi/mysql_thread.h:596

Instrumented cond_timedwait. `mysql_cond_timedwait` is a drop-in replacement for `pthread_cond_timedwait`.

---

### mysql_cond_signal

```cpp
#define mysql_cond_signal(C, C) inline_mysql_cond_signal(C)
```

Defined in psi/mysql_thread.h:605

Instrumented cond_signal. `mysql_cond_signal` is a drop-in replacement for `pthread_cond_signal`.

---

### mysql_cond_broadcast

```cpp
#define mysql_cond_broadcast(C, C) inline_mysql_cond_broadcast(C)
```

Defined in psi/mysql_thread.h:613

Instrumented cond_broadcast. `mysql_cond_broadcast` is a drop-in replacement for `pthread_cond_broadcast`.

---

### mysql_thread_register

```cpp
#define mysql_thread_register(P1, P2, P3, P1, P2, P3) inline_mysql_thread_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:619

Thread registration.

---

### mysql_thread_create

```cpp
#define mysql_thread_create(K, P1, P2, P3, P4, K, P1, P2, P3, P4) pthread_create(P1, P2, P3, P4)
```

Defined in psi/mysql_thread.h:643

Instrumented pthread_create. This function creates both the thread instrumentation and a thread. `mysql_thread_create` is a replacement for `pthread_create`. The parameter P4 (or, if it is NULL, P1) will be used as the instrumented thread "identity". Providing a P1 / P4 parameter with a different value for each call will on average improve performances, since this thread identity value is used internally to randomize access to data and prevent contention. This is optional, and the improvement is not guaranteed, only statistical.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | The PSI_thread_key for this instrumented thread |
| `P1` |  | pthread_create parameter 1 |
| `P2` |  | pthread_create parameter 2 |
| `P3` |  | pthread_create parameter 3 |
| `P4` |  | pthread_create parameter 4 |
| `K` |  | The PSI_thread_key for this instrumented thread |
| `P1` |  | pthread_create parameter 1 |
| `P2` |  | pthread_create parameter 2 |
| `P3` |  | pthread_create parameter 3 |
| `P4` |  | pthread_create parameter 4 |

---

### mysql_thread_set_psi_id

```cpp
#define mysql_thread_set_psi_id(I, I) do {} while (0)
```

Defined in psi/mysql_thread.h:655

Set the thread identifier for the instrumentation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `I` |  | The thread identifier |
| `I` |  | The thread identifier |

---

### mysql_thread_set_psi_THD

```cpp
#define mysql_thread_set_psi_THD(T, T) do {} while (0)
```

Defined in psi/mysql_thread.h:666

Set the thread sql session for the instrumentation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `T` |  | The thread identifier |
| `T` |  | The thread identifier |

---

### json_type

```cpp
#define json_type json_service->json_type
```

Defined in service_json.h:93

---

### json_get_array_item

```cpp
#define json_get_array_item json_service->json_get_array_item
```

Defined in service_json.h:94

---

### json_get_object_key

```cpp
#define json_get_object_key json_service->json_get_object_key
```

Defined in service_json.h:95

---

### json_get_object_nkey

```cpp
#define json_get_object_nkey json_service->json_get_object_nkey
```

Defined in service_json.h:96

---

### json_escape_string

```cpp
#define json_escape_string json_service->json_escape_string
```

Defined in service_json.h:97

---

### json_unescape_json

```cpp
#define json_unescape_json json_service->json_unescape_json
```

Defined in service_json.h:98

---

### MY_SHA1_HASH_SIZE

```cpp
#define MY_SHA1_HASH_SIZE 20 /* Hash size in bytes */
```

Defined in service_sha1.h:41

---

### my_sha1

```cpp
#define my_sha1(digest, buf, len, digest, buf, len) my_sha1_service->my_sha1_type(digest, buf, len)
```

Defined in service_sha1.h:54

---

### my_sha1_multi

```cpp
#define my_sha1_multi my_sha1_service->my_sha1_multi_type
```

Defined in service_sha1.h:55

---

### my_sha1_context_size

```cpp
#define my_sha1_context_size() my_sha1_service->my_sha1_context_size_type()
```

Defined in service_sha1.h:56

---

### my_sha1_init

```cpp
#define my_sha1_init(context, context) my_sha1_service->my_sha1_init_type(context)
```

Defined in service_sha1.h:57

---

### my_sha1_input

```cpp
#define my_sha1_input(context, buf, len, context, buf, len) my_sha1_service->my_sha1_input_type(context, buf, len)
```

Defined in service_sha1.h:58

---

### my_sha1_result

```cpp
#define my_sha1_result(context, digest, context, digest) my_sha1_service->my_sha1_result_type(context, digest)
```

Defined in service_sha1.h:59

---

### my_sha224

```cpp
#define my_sha224(digest, buf, len, digest, buf, len) my_sha2_service->my_sha224_type(digest, buf, len)
```

Defined in service_sha2.h:75

---

### my_sha224_multi

```cpp
#define my_sha224_multi my_sha2_service->my_sha224_multi_type
```

Defined in service_sha2.h:76

---

### my_sha224_context_size

```cpp
#define my_sha224_context_size() my_sha2_service->my_sha224_context_size_type()
```

Defined in service_sha2.h:77

---

### my_sha224_init

```cpp
#define my_sha224_init(context, context) my_sha2_service->my_sha224_init_type(context)
```

Defined in service_sha2.h:78

---

### my_sha224_input

```cpp
#define my_sha224_input(context, buf, len, context, buf, len) my_sha2_service->my_sha224_input_type(context, buf, len)
```

Defined in service_sha2.h:79

---

### my_sha224_result

```cpp
#define my_sha224_result(context, digest, context, digest) my_sha2_service->my_sha224_result_type(context, digest)
```

Defined in service_sha2.h:80

---

### my_sha256

```cpp
#define my_sha256(digest, buf, len, digest, buf, len) my_sha2_service->my_sha256_type(digest, buf, len)
```

Defined in service_sha2.h:82

---

### my_sha256_multi

```cpp
#define my_sha256_multi my_sha2_service->my_sha256_multi_type
```

Defined in service_sha2.h:83

---

### my_sha256_context_size

```cpp
#define my_sha256_context_size() my_sha2_service->my_sha256_context_size_type()
```

Defined in service_sha2.h:84

---

### my_sha256_init

```cpp
#define my_sha256_init(context, context) my_sha2_service->my_sha256_init_type(context)
```

Defined in service_sha2.h:85

---

### my_sha256_input

```cpp
#define my_sha256_input(context, buf, len, context, buf, len) my_sha2_service->my_sha256_input_type(context, buf, len)
```

Defined in service_sha2.h:86

---

### my_sha256_result

```cpp
#define my_sha256_result(context, digest, context, digest) my_sha2_service->my_sha256_result_type(context, digest)
```

Defined in service_sha2.h:87

---

### my_sha384

```cpp
#define my_sha384(digest, buf, len, digest, buf, len) my_sha2_service->my_sha384_type(digest, buf, len)
```

Defined in service_sha2.h:89

---

### my_sha384_multi

```cpp
#define my_sha384_multi my_sha2_service->my_sha384_multi_type
```

Defined in service_sha2.h:90

---

### my_sha384_context_size

```cpp
#define my_sha384_context_size() my_sha2_service->my_sha384_context_size_type()
```

Defined in service_sha2.h:91

---

### my_sha384_init

```cpp
#define my_sha384_init(context, context) my_sha2_service->my_sha384_init_type(context)
```

Defined in service_sha2.h:92

---

### my_sha384_input

```cpp
#define my_sha384_input(context, buf, len, context, buf, len) my_sha2_service->my_sha384_input_type(context, buf, len)
```

Defined in service_sha2.h:93

---

### my_sha384_result

```cpp
#define my_sha384_result(context, digest, context, digest) my_sha2_service->my_sha384_result_type(context, digest)
```

Defined in service_sha2.h:94

---

### my_sha512

```cpp
#define my_sha512(digest, buf, len, digest, buf, len) my_sha2_service->my_sha512_type(digest, buf, len)
```

Defined in service_sha2.h:96

---

### my_sha512_multi

```cpp
#define my_sha512_multi my_sha2_service->my_sha512_multi_type
```

Defined in service_sha2.h:97

---

### my_sha512_context_size

```cpp
#define my_sha512_context_size() my_sha2_service->my_sha512_context_size_type()
```

Defined in service_sha2.h:98

---

### my_sha512_init

```cpp
#define my_sha512_init(context, context) my_sha2_service->my_sha512_init_type(context)
```

Defined in service_sha2.h:99

---

### my_sha512_input

```cpp
#define my_sha512_input(context, buf, len, context, buf, len) my_sha2_service->my_sha512_input_type(context, buf, len)
```

Defined in service_sha2.h:100

---

### my_sha512_result

```cpp
#define my_sha512_result(context, digest, context, digest) my_sha2_service->my_sha512_result_type(context, digest)
```

Defined in service_sha2.h:101

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

---

### WSREP_ASSERT_INNODB_TRX

```cpp
#define WSREP_ASSERT_INNODB_TRX 1
```

Defined in service_wsrep.h:46

The bits in the bitmask for disabling temporarily some asserts

---

### MYSQL_SERVICE_WSREP_DYNAMIC_INCLUDED

```cpp
#define MYSQL_SERVICE_WSREP_DYNAMIC_INCLUDED
```

Defined in service_wsrep.h:116

---

### get_wsrep_recovery

```cpp
#define get_wsrep_recovery() wsrep_service->get_wsrep_recovery_func()
```

Defined in service_wsrep.h:117

---

### wsrep_consistency_check

```cpp
#define wsrep_consistency_check(thd, thd) wsrep_service->wsrep_consistency_check_func(thd)
```

Defined in service_wsrep.h:118

---

### wsrep_is_wsrep_xid

```cpp
#define wsrep_is_wsrep_xid(xid, xid) wsrep_service->wsrep_is_wsrep_xid_func(xid)
```

Defined in service_wsrep.h:119

---

### wsrep_xid_seqno

```cpp
#define wsrep_xid_seqno(xid, xid) wsrep_service->wsrep_xid_seqno_func(xid)
```

Defined in service_wsrep.h:120

---

### wsrep_xid_uuid

```cpp
#define wsrep_xid_uuid(xid, xid) wsrep_service->wsrep_xid_uuid_func(xid)
```

Defined in service_wsrep.h:121

---

### wsrep_on

```cpp
#define wsrep_on(thd, thd) (thd) && WSREP_ON && wsrep_service->wsrep_on_func(thd)
```

Defined in service_wsrep.h:126

Return true if wsrep is enabled for a thd. This means that wsrep is enabled globally and the thd has wsrep on

---

### wsrep_prepare_key_for_innodb

```cpp
#define wsrep_prepare_key_for_innodb(A, B, C, D, E, F, G, A, B, C, D, E, F, G) wsrep_service->wsrep_prepare_key_for_innodb_func(A,B,C,D,E,F,G)
```

Defined in service_wsrep.h:127

---

### wsrep_thd_LOCK

```cpp
#define wsrep_thd_LOCK(thd, thd) wsrep_service->wsrep_thd_LOCK_func(thd)
```

Defined in service_wsrep.h:129

Lock thd wsrep lock

---

### wsrep_thd_TRYLOCK

```cpp
#define wsrep_thd_TRYLOCK(thd, thd) wsrep_service->wsrep_thd_TRYLOCK_func(thd)
```

Defined in service_wsrep.h:134

Try thd wsrep lock. 
#### Returns
non-zero if lock could not be taken.

---

### wsrep_thd_UNLOCK

```cpp
#define wsrep_thd_UNLOCK(thd, thd) wsrep_service->wsrep_thd_UNLOCK_func(thd)
```

Defined in service_wsrep.h:136

Unlock thd wsrep lock

---

### wsrep_thd_kill_LOCK

```cpp
#define wsrep_thd_kill_LOCK(thd, thd) wsrep_service->wsrep_thd_kill_LOCK_func(thd)
```

Defined in service_wsrep.h:137

---

### wsrep_thd_kill_UNLOCK

```cpp
#define wsrep_thd_kill_UNLOCK(thd, thd) wsrep_service->wsrep_thd_kill_UNLOCK_func(thd)
```

Defined in service_wsrep.h:138

---

### wsrep_thd_query

```cpp
#define wsrep_thd_query(thd, thd) wsrep_service->wsrep_thd_query_func(thd)
```

Defined in service_wsrep.h:139

---

### wsrep_thd_retry_counter

```cpp
#define wsrep_thd_retry_counter(thd, thd) wsrep_service->wsrep_thd_retry_counter_func(thd)
```

Defined in service_wsrep.h:140

---

### wsrep_thd_ignore_table

```cpp
#define wsrep_thd_ignore_table(thd, thd) wsrep_service->wsrep_thd_ignore_table_func(thd)
```

Defined in service_wsrep.h:141

---

### wsrep_thd_trx_seqno

```cpp
#define wsrep_thd_trx_seqno(thd, thd) wsrep_service->wsrep_thd_trx_seqno_func(thd)
```

Defined in service_wsrep.h:142

---

### wsrep_set_data_home_dir

```cpp
#define wsrep_set_data_home_dir(A, A) wsrep_service->wsrep_set_data_home_dir_func(A)
```

Defined in service_wsrep.h:143

---

### wsrep_thd_is_BF

```cpp
#define wsrep_thd_is_BF(thd, sync, thd, sync) wsrep_service->wsrep_thd_is_BF_func(thd,sync)
```

Defined in service_wsrep.h:145

#### Return Values

| Value | Description |
|-------|-------------|
| `true` | if thd is in BF mode, either high_priority or TOI |

---

### wsrep_thd_is_aborting

```cpp
#define wsrep_thd_is_aborting(thd, thd) wsrep_service->wsrep_thd_is_aborting_func(thd)
```

Defined in service_wsrep.h:146

---

### wsrep_thd_in_rollback_func

```cpp
#define wsrep_thd_in_rollback_func(thd, thd) wsrep_service->wsrep_thd_in_rollback_func(thd)
```

Defined in service_wsrep.h:148

#### Return Values

| Value | Description |
|-------|-------------|
| `true` | if thd is in rollback |

---

### wsrep_thd_is_local

```cpp
#define wsrep_thd_is_local(thd, thd) wsrep_service->wsrep_thd_is_local_func(thd)
```

Defined in service_wsrep.h:150

#### Return Values

| Value | Description |
|-------|-------------|
| `true` | if thd is in replicating mode |

---

### wsrep_thd_self_abort

```cpp
#define wsrep_thd_self_abort(thd, thd) wsrep_service->wsrep_thd_self_abort_func(thd)
```

Defined in service_wsrep.h:152

Mark thd own transaction as aborted

---

### wsrep_thd_append_key

```cpp
#define wsrep_thd_append_key(thd, key, nkeys, key_type, thd, key, nkeys, key_type) wsrep_service->wsrep_thd_append_key_func(thd,key,nkeys,key_type)
```

Defined in service_wsrep.h:153

---

### wsrep_thd_append_table_key

```cpp
#define wsrep_thd_append_table_key(thd, db, table, key, thd, db, table, key) wsrep_service->wsrep_thd_append_table_key_func(thd,db,table,key)
```

Defined in service_wsrep.h:154

---

### wsrep_thd_is_local_transaction

```cpp
#define wsrep_thd_is_local_transaction(thd, thd) wsrep_service->wsrep_thd_is_local_transaction_func(thd)
```

Defined in service_wsrep.h:155

---

### wsrep_thd_client_state_str

```cpp
#define wsrep_thd_client_state_str(thd, thd) wsrep_service->wsrep_thd_client_state_str_func(thd)
```

Defined in service_wsrep.h:157

#### Returns
thd client state string

---

### wsrep_thd_client_mode_str

```cpp
#define wsrep_thd_client_mode_str(thd, thd) wsrep_service->wsrep_thd_client_mode_str_func(thd)
```

Defined in service_wsrep.h:159

#### Returns
thd client mode string

---

### wsrep_thd_transaction_state_str

```cpp
#define wsrep_thd_transaction_state_str(thd, thd) wsrep_service->wsrep_thd_transaction_state_str_func(thd)
```

Defined in service_wsrep.h:161

#### Returns
thd transaction state string

---

### wsrep_thd_transaction_id

```cpp
#define wsrep_thd_transaction_id(thd, thd) wsrep_service->wsrep_thd_transaction_id_func(thd)
```

Defined in service_wsrep.h:163

#### Returns
current transaction id

---

### wsrep_thd_bf_abort

```cpp
#define wsrep_thd_bf_abort(bf_thd, victim_thd, signal, bf_thd, victim_thd, signal) wsrep_service->wsrep_thd_bf_abort_func(bf_thd,victim_thd,signal)
```

Defined in service_wsrep.h:165

Mark victim_thd transaction as aborted

---

### wsrep_thd_order_before

```cpp
#define wsrep_thd_order_before(left, right, left, right) wsrep_service->wsrep_thd_order_before_func(left,right)
```

Defined in service_wsrep.h:166

---

### wsrep_handle_SR_rollback

```cpp
#define wsrep_handle_SR_rollback(BF_thd, victim_thd, BF_thd, victim_thd) wsrep_service->wsrep_handle_SR_rollback_func(BF_thd,victim_thd)
```

Defined in service_wsrep.h:167

---

### wsrep_thd_skip_locking

```cpp
#define wsrep_thd_skip_locking(thd, thd) wsrep_service->wsrep_thd_skip_locking_func(thd)
```

Defined in service_wsrep.h:168

---

### wsrep_get_sr_table_name

```cpp
#define wsrep_get_sr_table_name() wsrep_service->wsrep_get_sr_table_name_func()
```

Defined in service_wsrep.h:169

---

### wsrep_get_debug

```cpp
#define wsrep_get_debug() wsrep_service->wsrep_get_debug_func()
```

Defined in service_wsrep.h:170

---

### wsrep_commit_ordered

```cpp
#define wsrep_commit_ordered(thd, thd) wsrep_service->wsrep_commit_ordered_func(thd)
```

Defined in service_wsrep.h:171

---

### wsrep_thd_is_applying

```cpp
#define wsrep_thd_is_applying(thd, thd) wsrep_service->wsrep_thd_is_applying_func(thd)
```

Defined in service_wsrep.h:176

#### Returns
true if thd is in high priority mode

---

### wsrep_OSU_method_get

```cpp
#define wsrep_OSU_method_get(thd, thd) wsrep_service->wsrep_OSU_method_get_func(thd)
```

Defined in service_wsrep.h:177

---

### wsrep_thd_has_ignored_error

```cpp
#define wsrep_thd_has_ignored_error(thd, thd) wsrep_service->wsrep_thd_has_ignored_error_func(thd)
```

Defined in service_wsrep.h:178

---

### wsrep_thd_set_ignored_error

```cpp
#define wsrep_thd_set_ignored_error(thd, val, thd, val) wsrep_service->wsrep_thd_set_ignored_error_func(thd,val)
```

Defined in service_wsrep.h:179

---

### wsrep_report_bf_lock_wait

```cpp
#define wsrep_report_bf_lock_wait(thd, trx_id, thd, trx_id) wsrep_service->wsrep_report_bf_lock_wait_func(thd,trx_id)
```

Defined in service_wsrep.h:180

---

### wsrep_thd_set_PA_unsafe

```cpp
#define wsrep_thd_set_PA_unsafe(thd, thd) wsrep_service->wsrep_thd_set_wsrep_PA_unsafe_func(thd)
```

Defined in service_wsrep.h:181

---

### wsrep_get_domain_id

```cpp
#define wsrep_get_domain_id() wsrep_service->wsrep_get_domain_id_func()
```

Defined in service_wsrep.h:182

---

### MY_BASE64_DECODE_ALLOW_MULTIPLE_CHUNKS

```cpp
#define MY_BASE64_DECODE_ALLOW_MULTIPLE_CHUNKS 1
```

Defined in service_base64.h:45

---

### my_base64_needed_encoded_length

```cpp
#define my_base64_needed_encoded_length(A, A) base64_service->base64_needed_encoded_length_ptr(A)
```

Defined in service_base64.h:59

---

### my_base64_encode_max_arg_length

```cpp
#define my_base64_encode_max_arg_length() base64_service->base64_encode_max_arg_length_ptr()
```

Defined in service_base64.h:60

---

### my_base64_needed_decoded_length

```cpp
#define my_base64_needed_decoded_length(A, A) base64_service->base64_needed_decoded_length_ptr(A)
```

Defined in service_base64.h:61

---

### my_base64_decode_max_arg_length

```cpp
#define my_base64_decode_max_arg_length() base64_service->base64_decode_max_arg_length_ptr()
```

Defined in service_base64.h:62

---

### my_base64_encode

```cpp
#define my_base64_encode(A, B, C, A, B, C) base64_service->base64_encode_ptr(A,B,C)
```

Defined in service_base64.h:63

---

### my_base64_decode

```cpp
#define my_base64_decode(A, B, C, D, E, A, B, C, D, E) base64_service->base64_decode_ptr(A,B,C,D,E)
```

Defined in service_base64.h:64

---

### logger_init_mutexes

```cpp
#define logger_init_mutexes logger_service->logger_init_mutexes
```

Defined in service_logger.h:92

---

### logger_open

```cpp
#define logger_open(path, size_limit, rotations, buffer_size, path, size_limit, rotations, buffer_size) (logger_service->open(path, size_limit, rotations, buffer_size))
```

Defined in service_logger.h:93

---

### logger_close

```cpp
#define logger_close(log, log) (logger_service->close(log))
```

Defined in service_logger.h:95

---

### logger_rotate

```cpp
#define logger_rotate(log, log) (logger_service->rotate(log))
```

Defined in service_logger.h:96

---

### logger_vprintf

```cpp
#define logger_vprintf(log, fmt, argptr, log, fmt, argptr) (logger_service->\
    vprintf(log, fmt, argptr))
```

Defined in service_logger.h:97

---

### logger_printf

```cpp
#define logger_printf (*logger_service->printf)
```

Defined in service_logger.h:99

---

### logger_write

```cpp
#define logger_write(log, data, size, log, data, size) (logger_service->write(log, data, size))
```

Defined in service_logger.h:100

---

### logger_sync

```cpp
#define logger_sync(log, log) (logger_service->sync(log))
```

Defined in service_logger.h:102

---

### logger_resize_buffer

```cpp
#define logger_resize_buffer(log, new_buffer_size, log, new_buffer_size) (logger_service->resize_buffer(log, new_buffer_size))
```

Defined in service_logger.h:103

---

### logger_set_filesize_limit

```cpp
#define logger_set_filesize_limit(log, new_file_limit, log, new_file_limit) (logger_service->set_filesize_limit(log, new_file_limit))
```

Defined in service_logger.h:105

---

### logger_set_rotations

```cpp
#define logger_set_rotations(log, new_rotations, log, new_rotations) (logger_service->set_rotations(log, new_rotations))
```

Defined in service_logger.h:107

---

### MYSQL_FTPARSER_INTERFACE_VERSION

```cpp
#define MYSQL_FTPARSER_INTERFACE_VERSION 0x0100
```

Defined in plugin_ftparser.h:31

---

### MYSQL_FTFLAGS_NEED_COPY

```cpp
#define MYSQL_FTFLAGS_NEED_COPY 1
```

Defined in plugin_ftparser.h:159

Needs a copy flag.

The following flag means that buffer with a string (document, word) may be overwritten by the caller before the end of the parsing (that is before [st_mysql_ftparser::deinit()](ftparser_plugin_data.md#deinit) call). If one needs the string to survive between two successive calls of the parsing function, she needs to save a copy of it. The flag may be set by MySQL before calling [st_mysql_ftparser::parse()](ftparser_plugin_data.md#parse), or it may be set by a plugin before calling [st_mysql_ftparser_param::mysql_parse()](ftparser_plugin_data.md#mysql_parse) or [st_mysql_ftparser_param::mysql_add_word()](ftparser_plugin_data.md#mysql_add_word).

---

### MariaDB_FUNCTION_INTERFACE_VERSION

```cpp
#define MariaDB_FUNCTION_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin_function.h:41

API for function plugins.

---

### PSI_STATEMENT_CALL

```cpp
#define PSI_STATEMENT_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_statement.h:44

---

### PSI_DIGEST_CALL

```cpp
#define PSI_DIGEST_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_statement.h:48

---

### mysql_statement_register

```cpp
#define mysql_statement_register(P1, P2, P3, P1, P2, P3) do {} while (0)
```

Defined in psi/mysql_statement.h:59

Statement registration.

---

### MYSQL_DIGEST_START

```cpp
#define MYSQL_DIGEST_START(LOCKER, LOCKER) NULL
```

Defined in psi/mysql_statement.h:67

---

### MYSQL_DIGEST_END

```cpp
#define MYSQL_DIGEST_END(LOCKER, DIGEST, LOCKER, DIGEST) do {} while (0)
```

Defined in psi/mysql_statement.h:75

---

### MYSQL_START_STATEMENT

```cpp
#define MYSQL_START_STATEMENT(STATE, K, DB, DB_LEN, CS, SPS, STATE, K, DB, DB_LEN, CS, SPS) NULL
```

Defined in psi/mysql_statement.h:83

---

### MYSQL_REFINE_STATEMENT

```cpp
#define MYSQL_REFINE_STATEMENT(LOCKER, K, LOCKER, K) NULL
```

Defined in psi/mysql_statement.h:91

---

### MYSQL_SET_STATEMENT_TEXT

```cpp
#define MYSQL_SET_STATEMENT_TEXT(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql_statement.h:99

---

### MYSQL_SET_STATEMENT_LOCK_TIME

```cpp
#define MYSQL_SET_STATEMENT_LOCK_TIME(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_statement.h:107

---

### MYSQL_SET_STATEMENT_ROWS_SENT

```cpp
#define MYSQL_SET_STATEMENT_ROWS_SENT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_statement.h:115

---

### MYSQL_SET_STATEMENT_ROWS_EXAMINED

```cpp
#define MYSQL_SET_STATEMENT_ROWS_EXAMINED(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_statement.h:123

---

### MYSQL_END_STATEMENT

```cpp
#define MYSQL_END_STATEMENT(LOCKER, DA, LOCKER, DA) do {} while (0)
```

Defined in psi/mysql_statement.h:131

---

### thd_mdl_context

```cpp
#define thd_mdl_context(thd, thd) thd_mdl_service->thd_mdl_context(thd)
```

Defined in service_thd_mdl.h:49

MDL_context accessor 
#### Returns
pointer to thd->mdl_context

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | the current session |
| `thd` |  | the current session |

---

### thd_rnd

```cpp
#define thd_rnd(thd, thd) thd_rnd_service->thd_rnd_ptr(thd)
```

Defined in service_thd_rnd.h:52

---

### thd_create_random_password

```cpp
#define thd_create_random_password(thd, to, length, thd, to, length) thd_rnd_service->thd_c_r_p_ptr(thd,to,length)
```

Defined in service_thd_rnd.h:61

Generate string of printable random characters of requested length.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | User thread connection handle |
| `to` |  | Buffer for generation; must be at least length+1 bytes long; result string is always null-terminated |
| `length` |  | How many random characters to put in buffer |
| `thd` |  | User thread connection handle |
| `to` |  | Buffer for generation; must be at least length+1 bytes long; result string is always null-terminated |
| `length` |  | How many random characters to put in buffer |

---

### MariaDB_DATA_TYPE_INTERFACE_VERSION

```cpp
#define MariaDB_DATA_TYPE_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin_data_type.h:40

Data type plugin interface version

---

### MariaDB_ENCRYPTION_INTERFACE_VERSION

```cpp
#define MariaDB_ENCRYPTION_INTERFACE_VERSION 0x0300
```

Defined in plugin_encryption.h:52

---

### PSI_TRANSACTION_CALL

```cpp
#define PSI_TRANSACTION_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_transaction.h:40

---

### MYSQL_START_TRANSACTION

```cpp
#define MYSQL_START_TRANSACTION(STATE, XID, TRXID, ISO, RO, AC, STATE, XID, TRXID, ISO, RO, AC) 0
```

Defined in psi/mysql_transaction.h:47

---

### MYSQL_SET_TRANSACTION_GTID

```cpp
#define MYSQL_SET_TRANSACTION_GTID(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql_transaction.h:55

---

### MYSQL_SET_TRANSACTION_XID

```cpp
#define MYSQL_SET_TRANSACTION_XID(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql_transaction.h:63

---

### MYSQL_SET_TRANSACTION_XA_STATE

```cpp
#define MYSQL_SET_TRANSACTION_XA_STATE(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:71

---

### MYSQL_SET_TRANSACTION_TRXID

```cpp
#define MYSQL_SET_TRANSACTION_TRXID(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:79

---

### MYSQL_INC_TRANSACTION_SAVEPOINTS

```cpp
#define MYSQL_INC_TRANSACTION_SAVEPOINTS(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:87

---

### MYSQL_INC_TRANSACTION_ROLLBACK_TO_SAVEPOINT

```cpp
#define MYSQL_INC_TRANSACTION_ROLLBACK_TO_SAVEPOINT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:95

---

### MYSQL_INC_TRANSACTION_RELEASE_SAVEPOINT

```cpp
#define MYSQL_INC_TRANSACTION_RELEASE_SAVEPOINT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:103

---

### MYSQL_ROLLBACK_TRANSACTION

```cpp
#define MYSQL_ROLLBACK_TRANSACTION(LOCKER, LOCKER) do { } while(0)
```

Defined in psi/mysql_transaction.h:111

---

### MYSQL_COMMIT_TRANSACTION

```cpp
#define MYSQL_COMMIT_TRANSACTION(LOCKER, LOCKER) do { } while(0)
```

Defined in psi/mysql_transaction.h:119

---

### MY_AES_OK

```cpp
#define MY_AES_OK 0
```

Defined in service_my_crypt.h:43

---

### MY_AES_BAD_DATA

```cpp
#define MY_AES_BAD_DATA -100
```

Defined in service_my_crypt.h:44

---

### MY_AES_OPENSSL_ERROR

```cpp
#define MY_AES_OPENSSL_ERROR -101
```

Defined in service_my_crypt.h:45

---

### MY_AES_BAD_KEYSIZE

```cpp
#define MY_AES_BAD_KEYSIZE -102
```

Defined in service_my_crypt.h:46

---

### MY_AES_BLOCK_SIZE

```cpp
#define MY_AES_BLOCK_SIZE 16
```

Defined in service_my_crypt.h:49

---

### MY_AES_MAX_KEY_LENGTH

```cpp
#define MY_AES_MAX_KEY_LENGTH 32
```

Defined in service_my_crypt.h:52

---

### MY_AES_CTX_SIZE

```cpp
#define MY_AES_CTX_SIZE 1040
```

Defined in service_my_crypt.h:54

---

### my_aes_crypt_init

```cpp
#define my_aes_crypt_init(A, B, C, D, E, F, G, A, B, C, D, E, F, G) my_crypt_service->my_aes_crypt_init(A,B,C,D,E,F,G)
```

Defined in service_my_crypt.h:90

---

### my_aes_crypt_update

```cpp
#define my_aes_crypt_update(A, B, C, D, E, A, B, C, D, E) my_crypt_service->my_aes_crypt_update(A,B,C,D,E)
```

Defined in service_my_crypt.h:93

---

### my_aes_crypt_finish

```cpp
#define my_aes_crypt_finish(A, B, C, A, B, C) my_crypt_service->my_aes_crypt_finish(A,B,C)
```

Defined in service_my_crypt.h:96

---

### my_aes_crypt

```cpp
#define my_aes_crypt(A, B, C, D, E, F, G, H, I, J, A, B, C, D, E, F, G, H, I, J) my_crypt_service->my_aes_crypt(A,B,C,D,E,F,G,H,I,J)
```

Defined in service_my_crypt.h:99

---

### my_aes_get_size

```cpp
#define my_aes_get_size(A, B, A, B) my_crypt_service->my_aes_get_size(A,B)
```

Defined in service_my_crypt.h:102

---

### my_aes_ctx_size

```cpp
#define my_aes_ctx_size(A, A) my_crypt_service->my_aes_ctx_size(A)
```

Defined in service_my_crypt.h:105

---

### my_random_bytes

```cpp
#define my_random_bytes(A, B, A, B) my_crypt_service->my_random_bytes(A,B)
```

Defined in service_my_crypt.h:108

---

### my_bytes_to_key

```cpp
#define my_bytes_to_key(A, B, C, D, E, F, G, A, B, C, D, E, F, G) my_crypt_service->my_bytes_to_key(A,B,C,D,E,F,G)
```

Defined in service_my_crypt.h:111

---

### thd_wait_begin

```cpp
#define thd_wait_begin(thd, wait_type, thd, wait_type) thd_wait_service->thd_wait_begin_func(thd, wait_type)
```

Defined in service_thd_wait.h:91

Call just before a wait begins 
This is used by the threadpool to have better knowledge of which threads that currently are actively running on CPUs. When a thread reports that it's going to sleep/stall, the threadpool scheduler is free to start another thread in the pool most likely. The expected wait time is simply an indication of how long the wait is expected to become, the real wait time could be very different.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | Thread object. Use NULL if the thd is NOT known. |
| `wait_type` |  | Type of wait: one of [thd_wait_type](#thd_wait_type) |
| `thd` |  | Thread object. Use NULL if the thd is NOT known. |
| `wait_type` |  | Type of wait: one of [thd_wait_type](#thd_wait_type) |

---

### thd_wait_end

```cpp
#define thd_wait_end(thd, thd) thd_wait_service->thd_wait_end_func(thd)
```

Defined in service_thd_wait.h:97

Call just after a wait ends

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | Thread object. Use NULL if the thd is NOT known. |
| `thd` |  | Thread object. Use NULL if the thd is NOT known. |

---

### ENCRYPTION_KEY_VERSION_INVALID

```cpp
#define ENCRYPTION_KEY_VERSION_INVALID (~(unsigned int)0)
```

Defined in service_encryption.h:48

---

### ENCRYPTION_KEY_NOT_ENCRYPTED

```cpp
#define ENCRYPTION_KEY_NOT_ENCRYPTED (0)
```

Defined in service_encryption.h:49

---

### ENCRYPTION_KEY_SYSTEM_DATA

```cpp
#define ENCRYPTION_KEY_SYSTEM_DATA 1
```

Defined in service_encryption.h:51

---

### ENCRYPTION_KEY_TEMPORARY_DATA

```cpp
#define ENCRYPTION_KEY_TEMPORARY_DATA 2
```

Defined in service_encryption.h:52

---

### ENCRYPTION_KEY_BUFFER_TOO_SMALL

```cpp
#define ENCRYPTION_KEY_BUFFER_TOO_SMALL (100)
```

Defined in service_encryption.h:55

---

### ENCRYPTION_FLAG_DECRYPT

```cpp
#define ENCRYPTION_FLAG_DECRYPT 0
```

Defined in service_encryption.h:57

---

### ENCRYPTION_FLAG_ENCRYPT

```cpp
#define ENCRYPTION_FLAG_ENCRYPT 1
```

Defined in service_encryption.h:58

---

### ENCRYPTION_FLAG_NOPAD

```cpp
#define ENCRYPTION_FLAG_NOPAD 2
```

Defined in service_encryption.h:59

---

### encryption_key_get_latest_version

```cpp
#define encryption_key_get_latest_version(KI, KI) encryption_service->encryption_key_get_latest_version_func(KI)
```

Defined in service_encryption.h:80

---

### encryption_key_get

```cpp
#define encryption_key_get(KI, KV, K, S, KI, KV, K, S) encryption_service->encryption_key_get_func((KI),(KV),(K),(S))
```

Defined in service_encryption.h:81

---

### encryption_ctx_size

```cpp
#define encryption_ctx_size(KI, KV, KI, KV) encryption_service->encryption_ctx_size_func((KI),(KV))
```

Defined in service_encryption.h:82

---

### encryption_ctx_init

```cpp
#define encryption_ctx_init(CTX, K, KL, IV, IVL, F, KI, KV, CTX, K, KL, IV, IVL, F, KI, KV) encryption_service->encryption_ctx_init_func((CTX),(K),(KL),(IV),(IVL),(F),(KI),(KV))
```

Defined in service_encryption.h:83

---

### encryption_ctx_update

```cpp
#define encryption_ctx_update(CTX, S, SL, D, DL, CTX, S, SL, D, DL) encryption_service->encryption_ctx_update_func((CTX),(S),(SL),(D),(DL))
```

Defined in service_encryption.h:84

---

### encryption_ctx_finish

```cpp
#define encryption_ctx_finish(CTX, D, DL, CTX, D, DL) encryption_service->encryption_ctx_finish_func((CTX),(D),(DL))
```

Defined in service_encryption.h:85

---

### encryption_encrypted_length

```cpp
#define encryption_encrypted_length(SL, KI, KV, SL, KI, KV) encryption_service->encryption_encrypted_length_func((SL),(KI),(KV))
```

Defined in service_encryption.h:86

---

### thd_alloc

```cpp
#define thd_alloc(thd, size, thd, size) (thd_alloc_service->thd_alloc_func((thd), (size)))
```

Defined in service_thd_alloc.h:95

Allocate memory in the connection's local memory pool

When properly used in place of `my_malloc()`, this can significantly improve concurrency. Don't use this or related functions to allocate large chunks of memory. Use for temporary storage only. The memory will be freed automatically at the end of the statement; no explicit code is required to prevent memory leaks.

---

### thd_calloc

```cpp
#define thd_calloc(thd, size, thd, size) (thd_alloc_service->thd_calloc_func((thd), (size)))
```

Defined in service_thd_alloc.h:99

**See also**: [thd_alloc()](#thd_alloc)

---

### thd_strdup

```cpp
#define thd_strdup(thd, str, thd, str) (thd_alloc_service->thd_strdup_func((thd), (str)))
```

Defined in service_thd_alloc.h:103

**See also**: [thd_alloc()](#thd_alloc)

---

### thd_strmake

```cpp
#define thd_strmake(thd, str, size, thd, str, size) (thd_alloc_service->thd_strmake_func((thd), (str), (size)))
```

Defined in service_thd_alloc.h:107

**See also**: [thd_alloc()](#thd_alloc)

---

### thd_memdup

```cpp
#define thd_memdup(thd, str, size, thd, str, size) (thd_alloc_service->thd_memdup_func((thd), (str), (size)))
```

Defined in service_thd_alloc.h:112

**See also**: [thd_alloc()](#thd_alloc)

---

### thd_make_lex_string

```cpp
#define thd_make_lex_string(thd, lex_str, str, size, allocate_lex_string, thd, lex_str, str, size, allocate_lex_string) (thd_alloc_service->thd_make_lex_string_func((thd), (lex_str), (str), \
                                               (size), (allocate_lex_string)))
```

Defined in service_thd_alloc.h:127

Create a LEX_STRING in this connection's local memory pool

#### Returns
NULL on failure, or pointer to the LEX_STRING object

**See also**: [thd_alloc()](#thd_alloc)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `lex_str` |  | pointer to LEX_STRING object to be initialized |
| `str` |  | initializer to be copied into lex_str |
| `size` |  | length of str, in bytes |
| `allocate_lex_string` |  | flag: if TRUE, allocate new LEX_STRING object, instead of using lex_str value |
| `thd` |  | user thread connection handle |
| `lex_str` |  | pointer to LEX_STRING object to be initialized |
| `str` |  | initializer to be copied into lex_str |
| `size` |  | length of str, in bytes |
| `allocate_lex_string` |  | flag: if TRUE, allocate new LEX_STRING object, instead of using lex_str value |

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

### MYSQL_USERNAME_LENGTH

```cpp
#define MYSQL_USERNAME_LENGTH 512
```

Defined in plugin_auth_common.h:37

the max allowed length for a user name

---

### CR_AUTH_PLUGIN_ERROR

```cpp
#define CR_AUTH_PLUGIN_ERROR 3
```

Defined in plugin_auth_common.h:50

Authentication failed, plugin internal error. An error occurred in the authentication plugin itself. These errors are reported in table performance_schema.host_cache, column COUNT_AUTH_PLUGIN_ERRORS.

---

### CR_AUTH_HANDSHAKE

```cpp
#define CR_AUTH_HANDSHAKE 2
```

Defined in plugin_auth_common.h:57

Authentication failed, client server handshake. An error occurred during the client server handshake. These errors are reported in table performance_schema.host_cache, column COUNT_HANDSHAKE_ERRORS.

---

### CR_AUTH_USER_CREDENTIALS

```cpp
#define CR_AUTH_USER_CREDENTIALS 1
```

Defined in plugin_auth_common.h:64

Authentication failed, user credentials. For example, wrong passwords. These errors are reported in table performance_schema.host_cache, column COUNT_AUTHENTICATION_ERRORS.

---

### CR_ERROR

```cpp
#define CR_ERROR 0
```

Defined in plugin_auth_common.h:75

Authentication failed. Additionally, all other CR_xxx values (libmysql error code) can be used too.

The client plugin may set the error code and the error message directly in the MYSQL structure and return CR_ERROR. If a CR_xxx specific error code was returned, an error message in the MYSQL structure will be overwritten. If CR_ERROR is returned without setting the error in MYSQL, CR_UNKNOWN_ERROR will be user.

---

### CR_OK

```cpp
#define CR_OK -1
```

Defined in plugin_auth_common.h:83

Authentication (client part) was successful. It does not mean that the authentication as a whole was successful, usually it only means that the client was able to send the user name and the password to the server. If CR_OK is returned, the libmysql reads the next packet expecting it to be one of OK, ERROR, or CHANGE_PLUGIN packets.

---

### CR_OK_HANDSHAKE_COMPLETE

```cpp
#define CR_OK_HANDSHAKE_COMPLETE -2
```

Defined in plugin_auth_common.h:98

Authentication was successful. It means that the client has done its part successfully and also that a plugin has read the last packet (one of OK, ERROR, CHANGE_PLUGIN). In this case, libmysql will not read a packet from the server, but it will use the data at mysql->net.read_pos.

A plugin may return this value if the number of roundtrips in the authentication protocol is not known in advance, and the client plugin needs to read one packet more to determine if the authentication is finished or not.

Server plugins should not return this value.

---

### DEBUG_SYNC

```cpp
#define DEBUG_SYNC(thd, name, thd, name) do { } while(0)
```

Defined in service_debug_sync.h:357

---

### DEBUG_SYNC_C_IF_THD

```cpp
#define DEBUG_SYNC_C_IF_THD(thd, _sync_point_name_, thd, _sync_point_name_) do { } while(0)
```

Defined in service_debug_sync.h:358

---

### DEBUG_SYNC_C

```cpp
#define DEBUG_SYNC_C(name, name) DEBUG_SYNC(nullptr, name)
```

Defined in service_debug_sync.h:363

---

### my_snprintf

```cpp
#define my_snprintf(to, n, fmt, to, n, fmt) my_snprintf_service->my_snprintf_type
```

Defined in service_my_snprintf.h:120

A portable, limited vsnprintf() implementation, with some extra features.

#### Returns
a number of bytes written to a buffer *excluding* terminating '\0'

> [!NOTE]
> The syntax of a format string is generally the same: 
> ```
> %[<flag>][<length>][.<precision>][<size modifier>]<format>[<format extension>]
> ```
>  where everything but the `format` is optional.

Two one-character `flags` are recognized:

* '0' has the standard zero-padding semantics;
* '-' is parsed, but silently ignored;

Both `length` and `precision` are the same as in the standard. They can be specified as integers, or as '*' to consume an int argument.

`size modifier` can be 'l', 'll', or 'z'.

Supported `format`s are `s` (null pointer is accepted, printed as "(null)"), `c`, `d`, `i`, `u`, `x`, `X`, `o`, `p` (works as "0x%x"), `f`, and `g`.

The `$n` syntax for positional arguments is supported.

Format extensions:

* Format 'sQ' quotes the string with "\`" (backtick)s similar to "%s", but also "escapes" existing backticks in the string to '\`\`' as in SQL ''''.
* Format 'sB' treats the argument as a byte sequence. It reads and prints exactly `precision` bytes without terminating on any `\0`s in the sequence. The default `precision` when it's unspecified is not defined.
* Format 'sT' replaces the end of the printed string with "..." if it was truncated.
* Format 'sS' is a synonym for 's'. It's an escape that avoid consuming the following plain char as one of the above extension suffixes. Example: "Data Class: %sSType"
* Format 'iE' treats the argument as an errno number. It prints this number, a space, then its corresponding error message in double quotes. In other words: 
```cpp
printf("%iE", n) === printf("%i \"%sT\"", n, strerror(n))
```
* Format 'dE' has no effect. Therefore, to escape 'iE', use 'dE' instead.

Unrecognized and multiple suffixes are not parsed; for example, both "%sTQ" and "%iQ" will suffix with a literal 'Q'.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `to` |  | A buffer to store the result in |
| `n` |  | Store up to n-1 characters, followed by an end 0 |
| `fmt` |  | printf-like format string |
| `to` |  | A buffer to store the result in |
| `n` |  | Store up to n-1 characters, followed by an end 0 |
| `fmt` |  | printf-like format string |

---

### my_vsnprintf

```cpp
#define my_vsnprintf my_snprintf_service->my_vsnprintf_type
```

Defined in service_my_snprintf.h:121

---

### thd_get_autoinc

```cpp
#define thd_get_autoinc(thd, off, inc, thd, off, inc) (thd_autoinc_service->thd_get_autoinc_func((thd), (off), (inc)))
```

Defined in service_thd_autoinc.h:55

Return autoincrement system variables

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `off` |  | the value of @SESSION.auto_increment_offset |
| `inc` |  | the value of @SESSION.auto_increment_increment |
| `thd` |  | user thread connection handle |
| `off` |  | the value of @SESSION.auto_increment_offset |
| `inc` |  | the value of @SESSION.auto_increment_increment |

---

### thd_log_warnings

```cpp
#define thd_log_warnings(thd, thd) thd_log_warnings_service->thd_log_warnings(thd)
```

Defined in service_log_warnings.h:48

Log warnings accessor 
#### Returns
the value of thd->log_warnings

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | the current session |
| `thd` |  | the current session |

---

### thd_TIME_to_gmt_sec

```cpp
#define thd_TIME_to_gmt_sec(thd, ltime, errcode, thd, ltime, errcode) (thd_timezone_service->thd_TIME_to_gmt_sec((thd), (ltime), (errcode)))
```

Defined in service_thd_timezone.h:67

---

### thd_gmt_sec_to_TIME

```cpp
#define thd_gmt_sec_to_TIME(thd, ltime, t, thd, ltime, t) (thd_timezone_service->thd_gmt_sec_to_TIME((thd), (ltime), (t)))
```

Defined in service_thd_timezone.h:70

---

### thd_TIME_to_str

```cpp
#define thd_TIME_to_str(thd, ltime, format, buf, buf_len, thd, ltime, format, buf, buf_len) (thd_timezone_service->thd_TIME_to_str((thd), (ltime), (format), (buf), (buf_len)))
```

Defined in service_thd_timezone.h:73

---

### thd_key_create_from_var

```cpp
#define thd_key_create_from_var(K, V, K, V) do { *(K)= MYSQL_SYSVAR_NAME(V).offset; } while(0)
```

Defined in service_thd_specifics.h:81

---

### thd_key_create

```cpp
#define thd_key_create(key, key) (thd_specifics_service->thd_key_create_func(key))
```

Defined in service_thd_specifics.h:90

create THD specific storage 
#### Returns
0 on success else errno is returned

---

### thd_key_delete

```cpp
#define thd_key_delete(key, key) (thd_specifics_service->thd_key_delete_func(key))
```

Defined in service_thd_specifics.h:94

delete THD specific storage

---

### thd_getspecific

```cpp
#define thd_getspecific(thd, key, thd, key) (thd_specifics_service->thd_getspecific_func(thd, key))
```

Defined in service_thd_specifics.h:102

get thd specific storage

* first time this is called from a thread it will return 0
* this call is thread-safe in that different threads may call this simultaneously if operating on different THDs.
* this call acquires no mutexes and is implemented as an array lookup

---

### thd_setspecific

```cpp
#define thd_setspecific(thd, key, value, thd, key, value) (thd_specifics_service->thd_setspecific_func(thd, key, value))
```

Defined in service_thd_specifics.h:110

set thd specific storage

* first time this is called from a thread it will return 0
* this call is thread-safe in that different threads may call this simultaneously if operating on different THDs.
* this call acquires no mutexes and is implemented as an array lookup

---

### thd_killed

```cpp
#define thd_killed(THD, THD) (thd_kill_level(THD) == THD_ABORT_ASAP)
```

Defined in service_kill_statement.h:62

Backward compatibility helper

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `THD` |  | thread handle |
| `THD` |  | thread handle |

#### Return Values

| Value | Description |
|-------|-------------|
| `0` | No KILL statement was issued, continue normally |
| `1` | There was a KILL statement, abort the execution. |

---

### thd_kill_level

```cpp
#define thd_kill_level(THD, THD) thd_kill_statement_service->thd_kill_level_func(THD)
```

Defined in service_kill_statement.h:73

Check if a KILL statement was issued for the given thread.

#### Returns
[thd_kill_levels](#thd_kill_levels) values

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `THD` |  | thread handle |
| `THD` |  | thread handle |

---

### ME_ERROR_LOG

```cpp
#define ME_ERROR_LOG 64 /* Write the message to the error log */
```

Defined in service_my_print_error.h:43

---

### ME_ERROR_LOG_ONLY

```cpp
#define ME_ERROR_LOG_ONLY 128 /* Write the error message to error log only */
```

Defined in service_my_print_error.h:44

---

### ME_NOTE

```cpp
#define ME_NOTE 1024 /* Not an error, just a note */
```

Defined in service_my_print_error.h:45

---

### ME_WARNING

```cpp
#define ME_WARNING 2048 /* Not an error, just a warning */
```

Defined in service_my_print_error.h:46

---

### ME_FATAL

```cpp
#define ME_FATAL 4096 /* Fatal statement error */
```

Defined in service_my_print_error.h:47

---

### my_error

```cpp
#define my_error my_print_error_service->my_error_func
```

Defined in service_my_print_error.h:61

---

### my_printf_error

```cpp
#define my_printf_error my_print_error_service->my_printf_error_func
```

Defined in service_my_print_error.h:62

---

### my_printv_error

```cpp
#define my_printv_error(A, B, C, D, A, B, C, D) my_print_error_service->my_printv_error_func(A,B,C,D)
```

Defined in service_my_print_error.h:63

---

### thd_proc_info

```cpp
#define thd_proc_info(thd, msg, thd, msg) set_thd_proc_info(thd, msg, \
                                                   __func__, __FILE__, __LINE__)
```

Defined in service_progress_report.h:44

---

### thd_progress_init

```cpp
#define thd_progress_init(thd, max_stage, thd, max_stage) (progress_report_service->thd_progress_init_func((thd),(max_stage)))
```

Defined in service_progress_report.h:62

---

### thd_progress_report

```cpp
#define thd_progress_report(thd, progress, max_progress, thd, progress, max_progress) (progress_report_service->thd_progress_report_func((thd), (progress), (max_progress)))
```

Defined in service_progress_report.h:63

---

### thd_progress_next_stage

```cpp
#define thd_progress_next_stage(thd, thd) (progress_report_service->thd_progress_next_stage_func(thd))
```

Defined in service_progress_report.h:64

---

### thd_progress_end

```cpp
#define thd_progress_end(thd, thd) (progress_report_service->thd_progress_end_func(thd))
```

Defined in service_progress_report.h:65

---

### set_thd_proc_info

```cpp
#define set_thd_proc_info(thd, info, func, file, line, thd, info, func, file, line) (progress_report_service->set_thd_proc_info_func((thd),(info),(func),(file),(line)))
```

Defined in service_progress_report.h:66

---

### print_check_msg

```cpp
#define print_check_msg(thd, db_name, table_name, op, msg_type, message, print_to_log, thd, db_name, table_name, op, msg_type, message, print_to_log) print_check_msg_service->print_check_msg(thd, db_name, table_name, op, msg_type, message, print_to_log)
```

Defined in service_print_check_msg.h:41

---

### ENCRYPTION_SCHEME_KEY_INVALID

```cpp
#define ENCRYPTION_SCHEME_KEY_INVALID -1
```

Defined in service_encryption_scheme.h:74

---

### ENCRYPTION_SCHEME_BLOCK_LENGTH

```cpp
#define ENCRYPTION_SCHEME_BLOCK_LENGTH 16
```

Defined in service_encryption_scheme.h:75

---

### encryption_scheme_encrypt

```cpp
#define encryption_scheme_encrypt(S, SL, D, DL, SCH, KV, I32, J32, I64, S, SL, D, DL, SCH, KV, I32, J32, I64) encryption_scheme_service->encryption_scheme_encrypt_func(S,SL,D,DL,SCH,KV,I32,J32,I64)
```

Defined in service_encryption_scheme.h:109

---

### encryption_scheme_decrypt

```cpp
#define encryption_scheme_decrypt(S, SL, D, DL, SCH, KV, I32, J32, I64, S, SL, D, DL, SCH, KV, I32, J32, I64) encryption_scheme_service->encryption_scheme_decrypt_func(S,SL,D,DL,SCH,KV,I32,J32,I64)
```

Defined in service_encryption_scheme.h:110

---

### MYSQL_SERVICE_ENCRYPTION_SCHEME_INCLUDED

```cpp
#define MYSQL_SERVICE_ENCRYPTION_SCHEME_INCLUDED
```

Defined in service_encryption_scheme.h:132

---

### MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION

```cpp
#define MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION 0x0101
```

Defined in plugin_password_validation.h:43

---

### thd_get_error_message

```cpp
#define thd_get_error_message(thd, thd) (thd_error_context_service->thd_get_error_message_func((thd)))
```

Defined in service_thd_error_context.h:59

Return error message 
#### Returns
error text

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `thd` |  | user thread connection handle |

---

### thd_get_error_number

```cpp
#define thd_get_error_number(thd, thd) (thd_error_context_service->thd_get_error_number_func((thd)))
```

Defined in service_thd_error_context.h:66

Return error number 
#### Returns
error number

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `thd` |  | user thread connection handle |

---

### thd_get_error_row

```cpp
#define thd_get_error_row(thd, thd) (thd_error_context_service->thd_get_error_row_func((thd)))
```

Defined in service_thd_error_context.h:73

Return the current row number (i.e. in a multiple INSERT statement) 
#### Returns
row number

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `thd` |  | user thread connection handle |

---

### thd_inc_error_row

```cpp
#define thd_inc_error_row(thd, thd) (thd_error_context_service->thd_inc_error_row_func((thd)))
```

Defined in service_thd_error_context.h:79

Increment the current row number

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `thd` |  | user thread connection handle |

---

### thd_get_error_context_description

```cpp
#define thd_get_error_context_description(thd, buffer, length, max_query_length, thd, buffer, length, max_query_length) (thd_error_context_service->thd_get_error_context_description_func((thd), \
                                                                (buffer), \
                                                                (length), \
                                                                (max_query_length)))
```

Defined in service_thd_error_context.h:85

Return a text description of a thread, its security context (user,host) and the current query.

## Enumerations

---

### PSI_table_io_operation

```cpp
enum PSI_table_io_operation
```

Defined in psi/psi.h:243

IO operation performed on an instrumented table.

| Value | Description |
|-------|-------------|
| `PSI_TABLE_FETCH_ROW` | Row fetch. |
| `PSI_TABLE_WRITE_ROW` | Row write. |
| `PSI_TABLE_UPDATE_ROW` | Row update. |
| `PSI_TABLE_DELETE_ROW` | Row delete. |

---

### enum_mysql_show_type

```cpp
enum enum_mysql_show_type
```

Defined in plugin.h:251

declarations for SHOW STATUS support in plugins

| Value | Description |
|-------|-------------|
| `SHOW_UNDEF` | Internal only! |
| `SHOW_BOOL` | [my_bool](#my_bool) |
| `SHOW_UINT` | `unsigned int` |
| `SHOW_ULONG` | `unsigned long` |
| `SHOW_ULONGLONG` | `unsigned long long` |
| `SHOW_CHAR` | `char *` |
| `SHOW_CHAR_PTR` | `char **` |
| `SHOW_ARRAY` | SHOW_VAR [] |
| `SHOW_FUNC` | **See also**: SHOW_FUNC_ENTRY |
| `SHOW_DOUBLE` | `double` |
| `SHOW_SINT` | `int` |
| `SHOW_SLONG` | `long` |
| `SHOW_SLONGLONG` | `long long` |
| `SHOW_SIMPLE_FUNC` | [mysql_show_var_func](#mysql_show_var_func) * |
| `SHOW_SIZE_T` | `size_t` |
| `SHOW_always_last` | Internal only! |

---

### enum_var_type

```cpp
enum enum_var_type
```

Defined in plugin.h:279

SHOW STATUS scope

| Value | Description |
|-------|-------------|
| `SHOW_OPT_DEFAULT` | Internal only! |
| `SHOW_OPT_SESSION` | Session scope |
| `SHOW_OPT_GLOBAL` | Global scope |
| `SHOW_OPT_SESSION_NO_LOCK` | Session scope without locking |

---

### json_types

```cpp
enum json_types
```

Defined in service_json.h:59

| Value | Description |
|-------|-------------|
| `JSV_BAD_JSON` |  |
| `JSV_NOTHING` |  |
| `JSV_OBJECT` |  |
| `JSV_ARRAY` |  |
| `JSV_STRING` |  |
| `JSV_NUMBER` |  |
| `JSV_TRUE` |  |
| `JSV_FALSE` |  |
| `JSV_NULL` |  |

---

### Wsrep_service_key_type

```cpp
enum Wsrep_service_key_type
```

Defined in service_wsrep.h:36

| Value | Description |
|-------|-------------|
| `WSREP_SERVICE_KEY_SHARED` |  |
| `WSREP_SERVICE_KEY_REFERENCE` |  |
| `WSREP_SERVICE_KEY_UPDATE` |  |
| `WSREP_SERVICE_KEY_EXCLUSIVE` |  |

---

### enum_ftparser_mode

```cpp
enum enum_ftparser_mode
```

Defined in plugin_ftparser.h:34

Parsing modes. Set in [MYSQL_FTPARSER_PARAM::mode](ftparser_plugin_data.md#mode)

| Value | Description |
|-------|-------------|
| `MYSQL_FTPARSER_SIMPLE_MODE` | Fast and simple mode. |
| `MYSQL_FTPARSER_WITH_STOPWORDS` | Parse with stopwords mode. |
| `MYSQL_FTPARSER_FULL_BOOLEAN_INFO` | Parse in boolean mode. |

---

### enum_ft_token_type

```cpp
enum enum_ft_token_type
```

Defined in plugin_ftparser.h:82

Token types for boolean mode searching

Used for the type member of MYSQL_FTPARSER_BOOLEAN_INFO struct.

| Value | Description |
|-------|-------------|
| `FT_TOKEN_EOF` | End of data. |
| `FT_TOKEN_WORD` | Regular word. |
| `FT_TOKEN_LEFT_PAREN` | Left parenthesis (start of group/sub-expression). |
| `FT_TOKEN_RIGHT_PAREN` | Right parenthesis (end of group/sub-expression). |
| `FT_TOKEN_STOPWORD` | Stopword. |

---

### my_aes_mode

```cpp
enum my_aes_mode
```

Defined in service_my_crypt.h:56

| Value | Description |
|-------|-------------|
| `MY_AES_ECB` |  |
| `MY_AES_CBC` |  |

---

### my_digest

```cpp
enum my_digest
```

Defined in service_my_crypt.h:66

| Value | Description |
|-------|-------------|
| `MY_DIGEST_SHA1` |  |
| `MY_DIGEST_SHA224` |  |
| `MY_DIGEST_SHA256` |  |
| `MY_DIGEST_SHA384` |  |
| `MY_DIGEST_SHA512` |  |

---

### _thd_wait_type_e

```cpp
enum _thd_wait_type_e
```

Defined in service_thd_wait.h:57

| Value | Description |
|-------|-------------|
| `THD_WAIT_SLEEP` | sleep |
| `THD_WAIT_DISKIO` | Medium wait (e.g. for disk io) |
| `THD_WAIT_ROW_LOCK` | Large wait (e.g. for locked row/table) |
| `THD_WAIT_GLOBAL_LOCK` |  |
| `THD_WAIT_META_DATA_LOCK` |  |
| `THD_WAIT_TABLE_LOCK` |  |
| `THD_WAIT_USER_LOCK` |  |
| `THD_WAIT_BINLOG` |  |
| `THD_WAIT_GROUP_COMMIT` |  |
| `THD_WAIT_SYNC` |  |
| `THD_WAIT_NET` |  |
| `THD_WAIT_LAST` |  |

---

### thd_kill_levels

```cpp
enum thd_kill_levels
```

Defined in service_kill_statement.h:45

| Value | Description |
|-------|-------------|
| `THD_IS_NOT_KILLED` |  |
| `THD_ABORT_SOFTLY` | abort when possible, don't leave tables corrupted |
| `THD_ABORT_ASAP` | abort asap |
## Typedefs

---

### MDL_key

```cpp
using MDL_key = struct MDL_key
```

Type: struct [`MDL_key`](#mdl_key)

Defined in psi/psi.h:75

---

### opaque_mdl_type

```cpp
using opaque_mdl_type = int
```

Defined in psi/psi.h:78

**See also**: enum_mdl_type.

---

### opaque_mdl_duration

```cpp
using opaque_mdl_duration = int
```

Defined in psi/psi.h:81

**See also**: enum_mdl_duration.

---

### opaque_mdl_status

```cpp
using opaque_mdl_status = int
```

Defined in psi/psi.h:84

**See also**: MDL_wait::enum_wait_status.

---

### opaque_vio_type

```cpp
using opaque_vio_type = int
```

Defined in psi/psi.h:87

**See also**: enum_vio_type.

---

### PSI_mutex

```cpp
using PSI_mutex = struct PSI_mutex
```

Type: struct [`PSI_mutex`](#psi_mutex)

Defined in psi/psi.h:117

---

### PSI_rwlock

```cpp
using PSI_rwlock = struct PSI_rwlock
```

Type: struct [`PSI_rwlock`](#psi_rwlock)

Defined in psi/psi.h:124

---

### PSI_cond

```cpp
using PSI_cond = struct PSI_cond
```

Type: struct [`PSI_cond`](#psi_cond)

Defined in psi/psi.h:131

---

### PSI_table_share

```cpp
using PSI_table_share = struct PSI_table_share
```

Type: struct [`PSI_table_share`](#psi_table_share)

Defined in psi/psi.h:138

---

### PSI_table

```cpp
using PSI_table = struct PSI_table
```

Type: struct [`PSI_table`](#psi_table)

Defined in psi/psi.h:145

---

### PSI_thread

```cpp
using PSI_thread = struct PSI_thread
```

Type: struct [`PSI_thread`](#psi_thread)

Defined in psi/psi.h:152

---

### PSI_file

```cpp
using PSI_file = struct PSI_file
```

Type: struct [`PSI_file`](#psi_file)

Defined in psi/psi.h:159

---

### PSI_socket

```cpp
using PSI_socket = struct PSI_socket
```

Type: struct [`PSI_socket`](#psi_socket)

Defined in psi/psi.h:166

---

### PSI_prepared_stmt

```cpp
using PSI_prepared_stmt = struct PSI_prepared_stmt
```

Type: struct [`PSI_prepared_stmt`](#psi_prepared_stmt)

Defined in psi/psi.h:173

---

### PSI_table_locker

```cpp
using PSI_table_locker = struct PSI_table_locker
```

Type: struct [`PSI_table_locker`](#psi_table_locker)

Defined in psi/psi.h:180

---

### PSI_statement_locker

```cpp
using PSI_statement_locker = struct PSI_statement_locker
```

Type: struct [`PSI_statement_locker`](#psi_statement_locker)

Defined in psi/psi.h:187

---

### PSI_transaction_locker

```cpp
using PSI_transaction_locker = struct PSI_transaction_locker
```

Type: struct [`PSI_transaction_locker`](#psi_transaction_locker)

Defined in psi/psi.h:194

---

### PSI_idle_locker

```cpp
using PSI_idle_locker = struct PSI_idle_locker
```

Type: struct [`PSI_idle_locker`](#psi_idle_locker)

Defined in psi/psi.h:201

---

### PSI_digest_locker

```cpp
using PSI_digest_locker = struct PSI_digest_locker
```

Type: struct [`PSI_digest_locker`](#psi_digest_locker)

Defined in psi/psi.h:208

---

### PSI_sp_share

```cpp
using PSI_sp_share = struct PSI_sp_share
```

Type: struct [`PSI_sp_share`](#psi_sp_share)

Defined in psi/psi.h:215

---

### PSI_sp_locker

```cpp
using PSI_sp_locker = struct PSI_sp_locker
```

Type: struct [`PSI_sp_locker`](#psi_sp_locker)

Defined in psi/psi.h:222

---

### PSI_metadata_lock

```cpp
using PSI_metadata_lock = struct PSI_metadata_lock
```

Type: struct [`PSI_metadata_lock`](#psi_metadata_lock)

Defined in psi/psi.h:229

---

### PSI_stage_progress

```cpp
using PSI_stage_progress = struct PSI_stage_progress
```

Type: struct [`PSI_stage_progress`](Instrumentation_interface.md#psi_stage_progress-1)

Defined in psi/psi.h:240

---

### PSI_table_io_operation

```cpp
using PSI_table_io_operation = enum PSI_table_io_operation
```

Type: enum [`PSI_table_io_operation`](#psi_table_io_operation)

Defined in psi/psi.h:254

---

### PSI_table_locker_state

```cpp
using PSI_table_locker_state = struct PSI_table_locker_state
```

Type: struct [`PSI_table_locker_state`](Instrumentation_interface.md#psi_table_locker_state-1)

Defined in psi/psi.h:292

---

### PSI_bootstrap

```cpp
using PSI_bootstrap = struct PSI_bootstrap
```

Type: struct [`PSI_bootstrap`](Instrumentation_interface.md#psi_bootstrap-1)

Defined in psi/psi.h:312

---

### PSI_mutex_key

```cpp
using PSI_mutex_key = unsigned int
```

Defined in psi/psi.h:794

Instrumented mutex key. To instrument a mutex, a mutex key must be obtained using `register_mutex`. Using a zero key always disable the instrumentation.

---

### PSI_rwlock_key

```cpp
using PSI_rwlock_key = unsigned int
```

Defined in psi/psi.h:802

Instrumented rwlock key. To instrument a rwlock, a rwlock key must be obtained using `register_rwlock`. Using a zero key always disable the instrumentation.

---

### PSI_cond_key

```cpp
using PSI_cond_key = unsigned int
```

Defined in psi/psi.h:810

Instrumented cond key. To instrument a condition, a condition key must be obtained using `register_cond`. Using a zero key always disable the instrumentation.

---

### PSI_thread_key

```cpp
using PSI_thread_key = unsigned int
```

Defined in psi/psi.h:818

Instrumented thread key. To instrument a thread, a thread key must be obtained using `register_thread`. Using a zero key always disable the instrumentation.

---

### PSI_file_key

```cpp
using PSI_file_key = unsigned int
```

Defined in psi/psi.h:825

Instrumented file key. To instrument a file, a file key must be obtained using `register_file`. Using a zero key always disable the instrumentation.

---

### PSI_stage_key

```cpp
using PSI_stage_key = unsigned int
```

Defined in psi/psi.h:832

Instrumented stage key. To instrument a stage, a stage key must be obtained using `register_stage`. Using a zero key always disable the instrumentation.

---

### PSI_statement_key

```cpp
using PSI_statement_key = unsigned int
```

Defined in psi/psi.h:839

Instrumented statement key. To instrument a statement, a statement key must be obtained using `register_statement`. Using a zero key always disable the instrumentation.

---

### PSI_socket_key

```cpp
using PSI_socket_key = unsigned int
```

Defined in psi/psi.h:846

Instrumented socket key. To instrument a socket, a socket key must be obtained using `register_socket`. Using a zero key always disable the instrumentation.

---

### PSI_mutex_info_v1

```cpp
using PSI_mutex_info_v1 = struct PSI_mutex_info_v1
```

Type: struct [`PSI_mutex_info_v1`](Group_PSI_v1.md#psi_mutex_info_v1-1)

Defined in psi/psi.h:877

---

### PSI_rwlock_info_v1

```cpp
using PSI_rwlock_info_v1 = struct PSI_rwlock_info_v1
```

Type: struct [`PSI_rwlock_info_v1`](Group_PSI_v1.md#psi_rwlock_info_v1-1)

Defined in psi/psi.h:900

---

### PSI_cond_info_v1

```cpp
using PSI_cond_info_v1 = struct PSI_cond_info_v1
```

Type: struct [`PSI_cond_info_v1`](Group_PSI_v1.md#psi_cond_info_v1-1)

Defined in psi/psi.h:923

---

### PSI_thread_info_v1

```cpp
using PSI_thread_info_v1 = struct PSI_thread_info_v1
```

Type: struct [`PSI_thread_info_v1`](Group_PSI_v1.md#psi_thread_info_v1-1)

Defined in psi/psi.h:946

---

### PSI_file_info_v1

```cpp
using PSI_file_info_v1 = struct PSI_file_info_v1
```

Type: struct [`PSI_file_info_v1`](Group_PSI_v1.md#psi_file_info_v1-1)

Defined in psi/psi.h:969

---

### PSI_stage_info_v1

```cpp
using PSI_stage_info_v1 = struct PSI_stage_info_v1
```

Type: struct [`PSI_stage_info_v1`](Group_PSI_v1.md#psi_stage_info_v1-1)

Defined in psi/psi.h:985

---

### PSI_statement_info_v1

```cpp
using PSI_statement_info_v1 = struct PSI_statement_info_v1
```

Type: struct [`PSI_statement_info_v1`](Group_PSI_v1.md#psi_statement_info_v1-1)

Defined in psi/psi.h:1001

---

### PSI_socket_info_v1

```cpp
using PSI_socket_info_v1 = struct PSI_socket_info_v1
```

Type: struct [`PSI_socket_info_v1`](Group_PSI_v1.md#psi_socket_info_v1-1)

Defined in psi/psi.h:1024

---

### PSI_idle_locker_state_v1

```cpp
using PSI_idle_locker_state_v1 = struct PSI_idle_locker_state_v1
```

Type: struct [`PSI_idle_locker_state_v1`](Group_PSI_v1.md#psi_idle_locker_state_v1-1)

Defined in psi/psi.h:1048

---

### PSI_mutex_locker_state_v1

```cpp
using PSI_mutex_locker_state_v1 = struct PSI_mutex_locker_state_v1
```

Type: struct [`PSI_mutex_locker_state_v1`](Group_PSI_v1.md#psi_mutex_locker_state_v1-1)

Defined in psi/psi.h:1076

---

### PSI_rwlock_locker_state_v1

```cpp
using PSI_rwlock_locker_state_v1 = struct PSI_rwlock_locker_state_v1
```

Type: struct [`PSI_rwlock_locker_state_v1`](Group_PSI_v1.md#psi_rwlock_locker_state_v1-1)

Defined in psi/psi.h:1105

---

### PSI_cond_locker_state_v1

```cpp
using PSI_cond_locker_state_v1 = struct PSI_cond_locker_state_v1
```

Type: struct [`PSI_cond_locker_state_v1`](Group_PSI_v1.md#psi_cond_locker_state_v1-1)

Defined in psi/psi.h:1135

---

### PSI_file_locker_state_v1

```cpp
using PSI_file_locker_state_v1 = struct PSI_file_locker_state_v1
```

Type: struct [`PSI_file_locker_state_v1`](Group_PSI_v1.md#psi_file_locker_state_v1-1)

Defined in psi/psi.h:1171

---

### PSI_metadata_locker_state_v1

```cpp
using PSI_metadata_locker_state_v1 = struct PSI_metadata_locker_state_v1
```

Type: struct [`PSI_metadata_locker_state_v1`](Group_PSI_v1.md#psi_metadata_locker_state_v1-1)

Defined in psi/psi.h:1197

---

### PSI_statement_locker_state_v1

```cpp
using PSI_statement_locker_state_v1 = struct PSI_statement_locker_state_v1
```

Type: struct [`PSI_statement_locker_state_v1`](Group_PSI_v1.md#psi_statement_locker_state_v1-1)

Defined in psi/psi.h:1273

---

### PSI_transaction_locker_state_v1

```cpp
using PSI_transaction_locker_state_v1 = struct PSI_transaction_locker_state_v1
```

Type: struct [`PSI_transaction_locker_state_v1`](Group_PSI_v1.md#psi_transaction_locker_state_v1-1)

Defined in psi/psi.h:1313

---

### PSI_socket_locker_state_v1

```cpp
using PSI_socket_locker_state_v1 = struct PSI_socket_locker_state_v1
```

Type: struct [`PSI_socket_locker_state_v1`](Group_PSI_v1.md#psi_socket_locker_state_v1-1)

Defined in psi/psi.h:1347

---

### PSI_sp_locker_state_v1

```cpp
using PSI_sp_locker_state_v1 = struct PSI_sp_locker_state_v1
```

Type: struct [`PSI_sp_locker_state_v1`](Group_PSI_v1.md#psi_sp_locker_state_v1-1)

Defined in psi/psi.h:1362

---

### register_mutex_v1_t

```cpp
using register_mutex_v1_t = void(*
```

Defined in psi/psi.h:1372

Mutex registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of mutex info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of mutex info to register |
| `count` |  | the size of the info array |

---

### register_rwlock_v1_t

```cpp
using register_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1381

Rwlock registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of rwlock info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of rwlock info to register |
| `count` |  | the size of the info array |

---

### register_cond_v1_t

```cpp
using register_cond_v1_t = void(*
```

Defined in psi/psi.h:1390

Cond registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of cond info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of cond info to register |
| `count` |  | the size of the info array |

---

### register_thread_v1_t

```cpp
using register_thread_v1_t = void(*
```

Defined in psi/psi.h:1399

Thread registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of thread info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of thread info to register |
| `count` |  | the size of the info array |

---

### register_file_v1_t

```cpp
using register_file_v1_t = void(*
```

Defined in psi/psi.h:1408

File registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of file info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of file info to register |
| `count` |  | the size of the info array |

---

### register_stage_v1_t

```cpp
using register_stage_v1_t = void(*
```

Defined in psi/psi.h:1417

Stage registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name |
| `info` |  | an array of stage info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name |
| `info` |  | an array of stage info to register |
| `count` |  | the size of the info array |

---

### register_statement_v1_t

```cpp
using register_statement_v1_t = void(*
```

Defined in psi/psi.h:1426

Statement registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name |
| `info` |  | an array of stage info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name |
| `info` |  | an array of stage info to register |
| `count` |  | the size of the info array |

---

### register_socket_v1_t

```cpp
using register_socket_v1_t = void(*
```

Defined in psi/psi.h:1435

Socket registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of socket info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of socket info to register |
| `count` |  | the size of the info array |

---

### init_mutex_v1_t

```cpp
using init_mutex_v1_t = struct PSI_mutex *(*
```

Defined in psi/psi.h:1435

Mutex instrumentation initialisation API. 
#### Returns
an instrumented mutex

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered mutex key |
| `identity` |  | the address of the mutex itself |
| `key` |  | the registered mutex key |
| `identity` |  | the address of the mutex itself |

---

### destroy_mutex_v1_t

```cpp
using destroy_mutex_v1_t = void(*
```

Defined in psi/psi.h:1451

Mutex instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mutex` |  | the mutex to destroy |
| `mutex` |  | the mutex to destroy |

---

### init_rwlock_v1_t

```cpp
using init_rwlock_v1_t = struct PSI_rwlock *(*
```

Defined in psi/psi.h:1451

Rwlock instrumentation initialisation API. 
#### Returns
an instrumented rwlock

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered rwlock key |
| `identity` |  | the address of the rwlock itself |
| `key` |  | the registered rwlock key |
| `identity` |  | the address of the rwlock itself |

---

### destroy_rwlock_v1_t

```cpp
using destroy_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1466

Rwlock instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `rwlock` |  | the rwlock to destroy |
| `rwlock` |  | the rwlock to destroy |

---

### init_cond_v1_t

```cpp
using init_cond_v1_t = struct PSI_cond *(*
```

Defined in psi/psi.h:1466

Cond instrumentation initialisation API. 
#### Returns
an instrumented cond

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered key |
| `identity` |  | the address of the rwlock itself |
| `key` |  | the registered key |
| `identity` |  | the address of the rwlock itself |

---

### destroy_cond_v1_t

```cpp
using destroy_cond_v1_t = void(*
```

Defined in psi/psi.h:1481

Cond instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cond` |  | the rcond to destroy |
| `cond` |  | the rcond to destroy |

---

### init_socket_v1_t

```cpp
using init_socket_v1_t = struct PSI_socket *(*
```

Defined in psi/psi.h:1481

Socket instrumentation initialisation API. 
#### Returns
an instrumented socket

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered socket key |
| `fd` |  | the socket descriptor |
| `addr` |  | the socket ip address |
| `addr_len` |  | length of socket ip address |
| `key` |  | the registered socket key |
| `fd` |  | the socket descriptor |
| `addr` |  | the socket ip address |
| `addr_len` |  | length of socket ip address |

---

### destroy_socket_v1_t

```cpp
using destroy_socket_v1_t = void(*
```

Defined in psi/psi.h:1499

socket instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | the socket to destroy |
| `socket` |  | the socket to destroy |

---

### get_table_share_v1_t

```cpp
using get_table_share_v1_t = struct PSI_table_share *(*
```

Defined in psi/psi.h:1499

Acquire a table share instrumentation. 
#### Returns
a table share instrumentation, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `temporary` |  | True for temporary tables |
| `share` |  | The SQL layer table share |
| `temporary` |  | True for temporary tables |
| `share` |  | The SQL layer table share |

---

### release_table_share_v1_t

```cpp
using release_table_share_v1_t = void(*
```

Defined in psi/psi.h:1514

Release a table share.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `share` |  | the table share to release |
| `share` |  | the table share to release |

---

### drop_table_share_v1_t

```cpp
using drop_table_share_v1_t = void(*
```

Defined in psi/psi.h:1524

Drop a table share.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `temporary` |  | True for temporary tables |
| `schema_name` |  | the table schema name |
| `schema_name_length` |  | the table schema name length |
| `table_name` |  | the table name |
| `table_name_length` |  | the table name length |
| `temporary` |  | True for temporary tables |
| `schema_name` |  | the table schema name |
| `schema_name_length` |  | the table schema name length |
| `table_name` |  | the table name |
| `table_name_length` |  | the table name length |

---

### open_table_v1_t

```cpp
using open_table_v1_t = struct PSI_table *(*
```

Defined in psi/psi.h:1524

Open an instrumentation table handle. 
#### Returns
a table handle, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `share` |  | the table to open |
| `identity` |  | table handle identity |
| `share` |  | the table to open |
| `identity` |  | table handle identity |

---

### unbind_table_v1_t

```cpp
using unbind_table_v1_t = void(*
```

Defined in psi/psi.h:1542

Unbind a table handle from the current thread. This operation happens when an opened table is added to the open table cache.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `table` |  | the table to unbind |
| `table` |  | the table to unbind |

---

### rebind_table_v1_t

```cpp
using rebind_table_v1_t = PSI_table *(*
```

Defined in psi/psi.h:1550

Rebind a table handle to the current thread. This operation happens when a table from the open table cache is reused for a thread.

---

### close_table_v1_t

```cpp
using close_table_v1_t = void(*
```

Defined in psi/psi.h:1557

Close an instrumentation table handle. Note that the table handle is invalid after this call.

---

### create_file_v1_t

```cpp
using create_file_v1_t = void(*
```

Defined in psi/psi.h:1568

Create a file instrumentation for a created file. This method does not create the file itself, but is used to notify the instrumentation interface that a file was just created.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the file instrumentation key for this file |
| `name` |  | the file name |
| `file` |  | the file handle |
| `key` |  | the file instrumentation key for this file |
| `name` |  | the file name |
| `file` |  | the file handle |

---

### spawn_thread_v1_t

```cpp
using spawn_thread_v1_t = int(*
```

Defined in psi/psi.h:1580

Spawn a thread. This method creates a new thread, with instrumentation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the instrumentation key for this thread |
| `thread` |  | the resulting thread |
| `attr` |  | the thread attributes |
| `start_routine` |  | the thread start routine |
| `arg` |  | the thread start routine argument |
| `key` |  | the instrumentation key for this thread |
| `thread` |  | the resulting thread |
| `attr` |  | the thread attributes |
| `start_routine` |  | the thread start routine |
| `arg` |  | the thread start routine argument |

---

### new_thread_v1_t

```cpp
using new_thread_v1_t = struct PSI_thread *(*
```

Defined in psi/psi.h:1580

Create instrumentation for a thread. 
#### Returns
an instrumented thread

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered key |
| `identity` |  | an address typical of the thread |
| `thread_id` |  | the id of the thread |
| `key` |  | the registered key |
| `identity` |  | an address typical of the thread |
| `thread_id` |  | the id of the thread |

---

### set_thread_THD_v1_t

```cpp
using set_thread_THD_v1_t = void(*
```

Defined in psi/psi.h:1600

Assign a THD to an instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the instrumented thread |
| `thd` |  | the sql layer THD to assign |
| `thread` |  | the instrumented thread |
| `thd` |  | the sql layer THD to assign |

---

### set_thread_id_v1_t

```cpp
using set_thread_id_v1_t = void(*
```

Defined in psi/psi.h:1608

Assign an id to an instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the instrumented thread |
| `id` |  | the id to assign |
| `thread` |  | the instrumented thread |
| `id` |  | the id to assign |

---

### set_thread_os_id_v1_t

```cpp
using set_thread_os_id_v1_t = void(*
```

Defined in psi/psi.h:1616

Assign the current operating system thread id to an instrumented thread. The operating system task id is obtained from `gettid()`

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the instrumented thread |
| `thread` |  | the instrumented thread |

---

### get_thread_v1_t

```cpp
using get_thread_v1_t = struct PSI_thread *(*
```

Defined in psi/psi.h:1616

Get the instrumentation for the running thread. For this function to return a result, the thread instrumentation must have been attached to the running thread using `set_thread()`
#### Returns
the instrumentation for the running thread

---

### get_thread_class_name_v1_t

```cpp
using get_thread_class_name_v1_t = const char *(*
```

Defined in psi/psi.h:1631

Get name of the thread, according to the thread class. The name is returns without the thread/subsystem prefix.

---

### set_thread_user_v1_t

```cpp
using set_thread_user_v1_t = void(*
```

Defined in psi/psi.h:1638

Assign a user name to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `user` |  | the user name |
| `user_len` |  | the user name length |
| `user` |  | the user name |
| `user_len` |  | the user name length |

---

### set_thread_account_v1_t

```cpp
using set_thread_account_v1_t = void(*
```

Defined in psi/psi.h:1647

Assign a user name and host name to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `user` |  | the user name |
| `user_len` |  | the user name length |
| `host` |  | the host name |
| `host_len` |  | the host name length |
| `user` |  | the user name |
| `user_len` |  | the user name length |
| `host` |  | the host name |
| `host_len` |  | the host name length |

---

### set_thread_db_v1_t

```cpp
using set_thread_db_v1_t = void(*
```

Defined in psi/psi.h:1655

Assign a current database to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `db` |  | the database name |
| `db_len` |  | the database name length |
| `db` |  | the database name |
| `db_len` |  | the database name length |

---

### set_thread_command_v1_t

```cpp
using set_thread_command_v1_t = void(*
```

Defined in psi/psi.h:1661

Assign a current command to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `command` |  | the current command |
| `command` |  | the current command |

---

### set_connection_type_v1_t

```cpp
using set_connection_type_v1_t = void(*
```

Defined in psi/psi.h:1667

Assign a connection type to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `conn_type` |  | the connection type |
| `conn_type` |  | the connection type |

---

### set_thread_start_time_v1_t

```cpp
using set_thread_start_time_v1_t = void(*
```

Defined in psi/psi.h:1674

Assign a start time to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `start_time` |  | the thread start time |
| `start_time` |  | the thread start time |

---

### set_thread_state_v1_t

```cpp
using set_thread_state_v1_t = void(*
```

Defined in psi/psi.h:1680

Assign a state to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | the thread state |
| `state` |  | the thread state |

---

### set_thread_info_v1_t

```cpp
using set_thread_info_v1_t = void(*
```

Defined in psi/psi.h:1687

Assign a process info to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `info` |  | the process into string |
| `info_len` |  | the process into string length |
| `info` |  | the process into string |
| `info_len` |  | the process into string length |

---

### set_thread_v1_t

```cpp
using set_thread_v1_t = void(*
```

Defined in psi/psi.h:1698

Attach a thread instrumentation to the running thread. In case of thread pools, this method should be called when a worker thread picks a work item and runs it. Also, this method should be called if the instrumented code does not keep the pointer returned by `new_thread()` and relies on `get_thread()` instead.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the thread instrumentation |
| `thread` |  | the thread instrumentation |

---

### set_thread_peer_port_v1_t

```cpp
using set_thread_peer_port_v1_t = void(*
```

Defined in psi/psi.h:1706

Assign the remote (peer) port to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | pointer to the thread instrumentation |
| `port` |  | the remote port |
| `thread` |  | pointer to the thread instrumentation |
| `port` |  | the remote port |

---

### delete_current_thread_v1_t

```cpp
using delete_current_thread_v1_t = void(*
```

Defined in psi/psi.h:1710

Delete the current thread instrumentation.

---

### delete_thread_v1_t

```cpp
using delete_thread_v1_t = void(*
```

Defined in psi/psi.h:1713

Delete a thread instrumentation.

---

### get_thread_file_name_locker_v1_t

```cpp
using get_thread_file_name_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1713

Get a file instrumentation locker, for opening or creating a file. 
#### Returns
a file locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `key` |  | the file instrumentation key |
| `op` |  | the operation to perform |
| `name` |  | the file name |
| `identity` |  | a pointer representative of this file. |
| `state` |  | data storage for the locker |
| `key` |  | the file instrumentation key |
| `op` |  | the operation to perform |
| `name` |  | the file name |
| `identity` |  | a pointer representative of this file. |

---

### get_thread_file_stream_locker_v1_t

```cpp
using get_thread_file_stream_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1713

Get a file stream instrumentation locker. 
#### Returns
a file locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `file` |  | the file stream to access |
| `op` |  | the operation to perform |
| `state` |  | data storage for the locker |
| `file` |  | the file stream to access |
| `op` |  | the operation to perform |

---

### get_thread_file_descriptor_locker_v1_t

```cpp
using get_thread_file_descriptor_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1713

Get a file instrumentation locker. 
#### Returns
a file locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `file` |  | the file descriptor to access |
| `op` |  | the operation to perform |
| `state` |  | data storage for the locker |
| `file` |  | the file descriptor to access |
| `op` |  | the operation to perform |

---

### unlock_mutex_v1_t

```cpp
using unlock_mutex_v1_t = void(*
```

Defined in psi/psi.h:1755

Record a mutex instrumentation unlock event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mutex` |  | the mutex instrumentation |
| `mutex` |  | the mutex instrumentation |

---

### unlock_rwlock_v1_t

```cpp
using unlock_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1762

Record a rwlock instrumentation unlock event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `rwlock` |  | the rwlock instrumentation |
| `rwlock` |  | the rwlock instrumentation |

---

### signal_cond_v1_t

```cpp
using signal_cond_v1_t = void(*
```

Defined in psi/psi.h:1769

Record a condition instrumentation signal event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cond` |  | the cond instrumentation |
| `cond` |  | the cond instrumentation |

---

### broadcast_cond_v1_t

```cpp
using broadcast_cond_v1_t = void(*
```

Defined in psi/psi.h:1776

Record a condition instrumentation broadcast event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cond` |  | the cond instrumentation |
| `cond` |  | the cond instrumentation |

---

### start_idle_wait_v1_t

```cpp
using start_idle_wait_v1_t = struct PSI_idle_locker *(*
```

Defined in psi/psi.h:1776

Record an idle instrumentation wait start event. 
#### Returns
an idle locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `state` |  | data storage for the locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

### end_idle_wait_v1_t

```cpp
using end_idle_wait_v1_t = void(*
```

Defined in psi/psi.h:1793

Record an idle instrumentation wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `locker` |  | a thread locker for the running thread |

---

### start_mutex_wait_v1_t

```cpp
using start_mutex_wait_v1_t = struct PSI_mutex_locker *(*
```

Defined in psi/psi.h:1793

Record a mutex instrumentation wait start event. 
#### Returns
a mutex locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `mutex` |  | the instrumented mutex to lock |
| `op` |  | the operation to perform |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `state` |  | data storage for the locker |
| `mutex` |  | the instrumented mutex to lock |
| `op` |  | the operation to perform |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

### end_mutex_wait_v1_t

```cpp
using end_mutex_wait_v1_t = void(*
```

Defined in psi/psi.h:1816

Record a mutex instrumentation wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

### start_rwlock_rdwait_v1_t

```cpp
using start_rwlock_rdwait_v1_t = struct PSI_rwlock_locker *(*
```

Defined in psi/psi.h:1816

Record a rwlock instrumentation read wait start event.

---

### end_rwlock_rdwait_v1_t

```cpp
using end_rwlock_rdwait_v1_t = void(*
```

Defined in psi/psi.h:1833

Record a rwlock instrumentation read wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

### start_rwlock_wrwait_v1_t

```cpp
using start_rwlock_wrwait_v1_t = struct PSI_rwlock_locker *(*
```

Defined in psi/psi.h:1833

Record a rwlock instrumentation write wait start event.

---

### end_rwlock_wrwait_v1_t

```cpp
using end_rwlock_wrwait_v1_t = void(*
```

Defined in psi/psi.h:1850

Record a rwlock instrumentation write wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

### start_cond_wait_v1_t

```cpp
using start_cond_wait_v1_t = struct PSI_cond_locker *(*
```

Defined in psi/psi.h:1850

Record a condition instrumentation wait start event.

---

### end_cond_wait_v1_t

```cpp
using end_cond_wait_v1_t = void(*
```

Defined in psi/psi.h:1868

Record a condition instrumentation wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

### start_table_io_wait_v1_t

```cpp
using start_table_io_wait_v1_t = struct PSI_table_locker *(*
```

Defined in psi/psi.h:1868

Record a table instrumentation io wait start event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `table` |  | the instrumented table to lock |
| `op` |  | the operation to perform |
| `index` |  | the index number to lock, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `state` |  | data storage for the locker |
| `table` |  | the instrumented table to lock |
| `op` |  | the operation to perform |
| `index` |  | the index number to lock, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

### end_table_io_wait_v1_t

```cpp
using end_table_io_wait_v1_t = void(*
```

Defined in psi/psi.h:1892

Record a table instrumentation io wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a table locker for the running thread |
| `numrows` |  | the number of rows involved in io |
| `locker` |  | a table locker for the running thread |
| `numrows` |  | the number of rows involved in io |

---

### start_table_lock_wait_v1_t

```cpp
using start_table_lock_wait_v1_t = struct PSI_table_locker *(*
```

Defined in psi/psi.h:1892

Record a table instrumentation lock wait start event.

---

### end_table_lock_wait_v1_t

```cpp
using end_table_lock_wait_v1_t = void(*
```

Defined in psi/psi.h:1910

Record a table instrumentation lock wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a table locker for the running thread |
| `locker` |  | a table locker for the running thread |

---

### unlock_table_v1_t

```cpp
using unlock_table_v1_t = void(*
```

Defined in psi/psi.h:1912

---

### start_file_open_wait_v1_t

```cpp
using start_file_open_wait_v1_t = void(*
```

Defined in psi/psi.h:1920

Start a file instrumentation open operation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `locker` |  | the file locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

### end_file_open_wait_v1_t

```cpp
using end_file_open_wait_v1_t = struct PSI_file *(*
```

Defined in psi/psi.h:1920

End a file instrumentation open operation, for file streams. 
#### Returns
an instrumented file handle

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `result` |  | the opened file (NULL indicates failure, non NULL success). |
| `locker` |  | the file locker. |
| `result` |  | the opened file (NULL indicates failure, non NULL success). |

---

### end_file_open_wait_and_bind_to_descriptor_v1_t

```cpp
using end_file_open_wait_and_bind_to_descriptor_v1_t = void(*
```

Defined in psi/psi.h:1937

End a file instrumentation open operation, for non stream files.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |

---

### end_temp_file_open_wait_and_bind_to_descriptor_v1_t

```cpp
using end_temp_file_open_wait_and_bind_to_descriptor_v1_t = void(*
```

Defined in psi/psi.h:1946

End a file instrumentation open operation, for non stream temporary files.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |
| `filename` |  | the file name generated during temporary file creation. |
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |
| `filename` |  | the file name generated during temporary file creation. |

---

### start_file_wait_v1_t

```cpp
using start_file_wait_v1_t = void(*
```

Defined in psi/psi.h:1956

Record a file instrumentation start event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a file locker for the running thread |
| `count` |  | the number of bytes requested, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `locker` |  | a file locker for the running thread |
| `count` |  | the number of bytes requested, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

### end_file_wait_v1_t

```cpp
using end_file_wait_v1_t = void(*
```

Defined in psi/psi.h:1972

Record a file instrumentation end event. Note that for file close operations, the instrumented file handle associated with the file (which was provided to obtain a locker) is invalid after this call. **See also**: get_thread_file_name_locker 

**See also**: get_thread_file_stream_locker 

**See also**: get_thread_file_descriptor_locker

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a file locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |
| `locker` |  | a file locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |

---

### start_file_close_wait_v1_t

```cpp
using start_file_close_wait_v1_t = void(*
```

Defined in psi/psi.h:1981

Start a file instrumentation close operation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `locker` |  | the file locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

### end_file_close_wait_v1_t

```cpp
using end_file_close_wait_v1_t = void(*
```

Defined in psi/psi.h:1990

End a file instrumentation close operation. 
#### Returns
an instrumented file handle

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `rc` |  | the close operation return code (0 for success). |
| `locker` |  | the file locker. |
| `rc` |  | the close operation return code (0 for success). |

---

### end_file_rename_wait_v1_t

```cpp
using end_file_rename_wait_v1_t = void(*
```

Defined in psi/psi.h:2000

Rename a file instrumentation close operation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `old_name` |  | name of the file to be renamed. |
| `new_name` |  | name of the file after rename. |
| `rc` |  | the rename operation return code (0 for success). |
| `locker` |  | the file locker. |
| `old_name` |  | name of the file to be renamed. |
| `new_name` |  | name of the file after rename. |
| `rc` |  | the rename operation return code (0 for success). |

---

### start_stage_v1_t

```cpp
using start_stage_v1_t = PSI_stage_progress *(*
```

Defined in psi/psi.h:2011

Start a new stage, and implicitly end the previous stage. 
#### Returns
the new stage progress

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the key of the new stage |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `key` |  | the key of the new stage |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

### get_current_stage_progress_v1_t

```cpp
using get_current_stage_progress_v1_t = PSI_stage_progress *(*
```

Defined in psi/psi.h:2014

---

### end_stage_v1_t

```cpp
using end_stage_v1_t = void(*
```

Defined in psi/psi.h:2017

End the current stage.

---

### get_thread_statement_locker_v1_t

```cpp
using get_thread_statement_locker_v1_t = struct PSI_statement_locker *(*
```

Defined in psi/psi.h:2017

Get a statement instrumentation locker. 
#### Returns
a statement locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `key` |  | the statement instrumentation key |
| `charset` |  | client character set |
| `sp_share` |  | the share |
| `state` |  | data storage for the locker |
| `key` |  | the statement instrumentation key |
| `charset` |  | client character set |
| `sp_share` |  | the share |

---

### refine_statement_v1_t

```cpp
using refine_statement_v1_t = struct PSI_statement_locker *(*
```

Defined in psi/psi.h:2017

Refine a statement locker to a more specific key. Note that only events declared mutable can be refined. **See also**: [PSI_FLAG_MUTABLE](#psi_flag_mutable)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | statement locker for the current event |
| `key` |  | the new key for the event |
| `locker` |  | statement locker for the current event |
| `key` |  | the new key for the event |

---

### start_statement_v1_t

```cpp
using start_statement_v1_t = void(*
```

Defined in psi/psi.h:2050

Start a new statement event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker for this event |
| `db` |  | the active database name for this statement |
| `db_length` |  | the active database name length for this statement |
| `src_file` |  | source file name |
| `src_line` |  | source line number |
| `locker` |  | the statement locker for this event |
| `db` |  | the active database name for this statement |
| `db_length` |  | the active database name length for this statement |
| `src_file` |  | source file name |
| `src_line` |  | source line number |

---

### set_statement_text_v1_t

```cpp
using set_statement_text_v1_t = void(*
```

Defined in psi/psi.h:2061

Set the statement text for a statement event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the current statement locker |
| `text` |  | the statement text |
| `text_len` |  | the statement text length |
| `locker` |  | the current statement locker |
| `text` |  | the statement text |
| `text_len` |  | the statement text length |

---

### set_statement_lock_time_t

```cpp
using set_statement_lock_time_t = void(*
```

Defined in psi/psi.h:2070

Set a statement event lock time.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `lock_time` |  | the locked time, in microseconds |
| `locker` |  | the statement locker |
| `lock_time` |  | the locked time, in microseconds |

---

### set_statement_rows_sent_t

```cpp
using set_statement_rows_sent_t = void(*
```

Defined in psi/psi.h:2078

Set a statement event rows sent metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the number of rows sent |
| `locker` |  | the statement locker |
| `count` |  | the number of rows sent |

---

### set_statement_rows_examined_t

```cpp
using set_statement_rows_examined_t = void(*
```

Defined in psi/psi.h:2086

Set a statement event rows examined metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the number of rows examined |
| `locker` |  | the statement locker |
| `count` |  | the number of rows examined |

---

### inc_statement_created_tmp_disk_tables_t

```cpp
using inc_statement_created_tmp_disk_tables_t = void(*
```

Defined in psi/psi.h:2094

Increment a statement event "created tmp disk tables" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_created_tmp_tables_t

```cpp
using inc_statement_created_tmp_tables_t = void(*
```

Defined in psi/psi.h:2102

Increment a statement event "created tmp tables" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_select_full_join_t

```cpp
using inc_statement_select_full_join_t = void(*
```

Defined in psi/psi.h:2110

Increment a statement event "select full join" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_select_full_range_join_t

```cpp
using inc_statement_select_full_range_join_t = void(*
```

Defined in psi/psi.h:2118

Increment a statement event "select full range join" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_select_range_t

```cpp
using inc_statement_select_range_t = void(*
```

Defined in psi/psi.h:2126

Increment a statement event "select range join" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_select_range_check_t

```cpp
using inc_statement_select_range_check_t = void(*
```

Defined in psi/psi.h:2134

Increment a statement event "select range check" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_select_scan_t

```cpp
using inc_statement_select_scan_t = void(*
```

Defined in psi/psi.h:2142

Increment a statement event "select scan" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_sort_merge_passes_t

```cpp
using inc_statement_sort_merge_passes_t = void(*
```

Defined in psi/psi.h:2150

Increment a statement event "sort merge passes" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_sort_range_t

```cpp
using inc_statement_sort_range_t = void(*
```

Defined in psi/psi.h:2158

Increment a statement event "sort range" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_sort_rows_t

```cpp
using inc_statement_sort_rows_t = void(*
```

Defined in psi/psi.h:2166

Increment a statement event "sort rows" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### inc_statement_sort_scan_t

```cpp
using inc_statement_sort_scan_t = void(*
```

Defined in psi/psi.h:2174

Increment a statement event "sort scan" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

### set_statement_no_index_used_t

```cpp
using set_statement_no_index_used_t = void(*
```

Defined in psi/psi.h:2181

Set a statement event "no index used" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `locker` |  | the statement locker |

---

### set_statement_no_good_index_used_t

```cpp
using set_statement_no_good_index_used_t = void(*
```

Defined in psi/psi.h:2188

Set a statement event "no good index used" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `locker` |  | the statement locker |

---

### end_statement_v1_t

```cpp
using end_statement_v1_t = void(*
```

Defined in psi/psi.h:2197

End a statement event. **See also**: Diagnostics_area

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `stmt_da` |  | the statement diagnostics area. |
| `locker` |  | the statement locker |
| `stmt_da` |  | the statement diagnostics area. |

---

### get_thread_transaction_locker_v1_t

```cpp
using get_thread_transaction_locker_v1_t = struct PSI_transaction_locker *(*
```

Defined in psi/psi.h:2197

Get a transaction instrumentation locker. 
#### Returns
a transaction locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `xid` |  | the xid for this transaction |
| `trxid` |  | the InnoDB transaction id |
| `isolation_level` |  | isolation level for this transaction |
| `read_only` |  | true if transaction access mode is read-only |
| `autocommit` |  | true if transaction is autocommit |
| `state` |  | data storage for the locker |
| `xid` |  | the xid for this transaction |
| `trxid` |  | the InnoDB transaction id |
| `isolation_level` |  | isolation level for this transaction |
| `read_only` |  | true if transaction access mode is read-only |
| `autocommit` |  | true if transaction is autocommit |

---

### start_transaction_v1_t

```cpp
using start_transaction_v1_t = void(*
```

Defined in psi/psi.h:2221

Start a new transaction event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `src_file` |  | source file name |
| `src_line` |  | source line number |
| `locker` |  | the transaction locker for this event |
| `src_file` |  | source file name |
| `src_line` |  | source line number |

---

### set_transaction_xid_v1_t

```cpp
using set_transaction_xid_v1_t = void(*
```

Defined in psi/psi.h:2231

Set the transaction xid.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `xid` |  | the id of the XA transaction |
| `xa_state` |  | is the state of the XA transaction |
| `locker` |  | the transaction locker for this event |
| `xid` |  | the id of the XA transaction |
| `xa_state` |  | is the state of the XA transaction |

---

### set_transaction_xa_state_v1_t

```cpp
using set_transaction_xa_state_v1_t = void(*
```

Defined in psi/psi.h:2240

Set the state of the XA transaction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `xa_state` |  | the new state of the xa transaction |
| `locker` |  | the transaction locker for this event |
| `xa_state` |  | the new state of the xa transaction |

---

### set_transaction_gtid_v1_t

```cpp
using set_transaction_gtid_v1_t = void(*
```

Defined in psi/psi.h:2250

Set the transaction gtid.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `sid` |  | the source id for the transaction, mapped from sidno |
| `gtid_spec` |  | the gtid specifier for the transaction |
| `locker` |  | the transaction locker for this event |
| `sid` |  | the source id for the transaction, mapped from sidno |
| `gtid_spec` |  | the gtid specifier for the transaction |

---

### set_transaction_trxid_v1_t

```cpp
using set_transaction_trxid_v1_t = void(*
```

Defined in psi/psi.h:2259

Set the transaction trx_id.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `trxid` |  | the storage engine transaction ID |
| `locker` |  | the transaction locker for this event |
| `trxid` |  | the storage engine transaction ID |

---

### inc_transaction_savepoints_v1_t

```cpp
using inc_transaction_savepoints_v1_t = void(*
```

Defined in psi/psi.h:2268

Increment a transaction event savepoint count.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker |
| `count` |  | the increment value |
| `locker` |  | the transaction locker |
| `count` |  | the increment value |

---

### inc_transaction_rollback_to_savepoint_v1_t

```cpp
using inc_transaction_rollback_to_savepoint_v1_t = void(*
```

Defined in psi/psi.h:2276

Increment a transaction event rollback to savepoint count.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker |
| `count` |  | the increment value |
| `locker` |  | the transaction locker |
| `count` |  | the increment value |

---

### inc_transaction_release_savepoint_v1_t

```cpp
using inc_transaction_release_savepoint_v1_t = void(*
```

Defined in psi/psi.h:2284

Increment a transaction event release savepoint count.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker |
| `count` |  | the increment value |
| `locker` |  | the transaction locker |
| `count` |  | the increment value |

---

### end_transaction_v1_t

```cpp
using end_transaction_v1_t = void(*
```

Defined in psi/psi.h:2292

Commit or rollback the transaction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `commit` |  | true if transaction was committed, false if rolled back |
| `locker` |  | the transaction locker for this event |
| `commit` |  | true if transaction was committed, false if rolled back |

---

### start_socket_wait_v1_t

```cpp
using start_socket_wait_v1_t = struct PSI_socket_locker *(*
```

Defined in psi/psi.h:2292

Record a socket instrumentation start event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | locker state for the running thread |
| `socket` |  | the instrumented socket |
| `op` |  | socket operation to be performed |
| `count` |  | the number of bytes requested, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `state` |  | locker state for the running thread |
| `socket` |  | the instrumented socket |
| `op` |  | socket operation to be performed |
| `count` |  | the number of bytes requested, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

### end_socket_wait_v1_t

```cpp
using end_socket_wait_v1_t = void(*
```

Defined in psi/psi.h:2322

Record a socket instrumentation end event. Note that for socket close operations, the instrumented socket handle associated with the socket (which was provided to obtain a locker) is invalid after this call. **See also**: get_thread_socket_locker

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a socket locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |
| `locker` |  | a socket locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |

---

### set_socket_state_v1_t

```cpp
using set_socket_state_v1_t = void(*
```

Defined in psi/psi.h:2330

Set the socket state for an instrumented socket.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | the instrumented socket |
| `state` |  | socket state |
| `socket` |  | the instrumented socket |
| `state` |  | socket state |

---

### set_socket_info_v1_t

```cpp
using set_socket_info_v1_t = void(*
```

Defined in psi/psi.h:2340

Set the socket info for an instrumented socket.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | the instrumented socket |
| `fd` |  | the socket descriptor |
| `addr` |  | the socket ip address |
| `addr_len` |  | length of socket ip address |
| `socket` |  | the instrumented socket |
| `fd` |  | the socket descriptor |
| `addr` |  | the socket ip address |
| `addr_len` |  | length of socket ip address |

---

### set_socket_thread_owner_v1_t

```cpp
using set_socket_thread_owner_v1_t = void(*
```

Defined in psi/psi.h:2349

Bind a socket to the thread that owns it.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | instrumented socket |
| `socket` |  | instrumented socket |

---

### create_prepared_stmt_v1_t

```cpp
using create_prepared_stmt_v1_t = PSI_prepared_stmt *(*
```

Defined in psi/psi.h:2354

Get a prepare statement.

---

### destroy_prepared_stmt_v1_t

```cpp
using destroy_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2362

destroy a prepare statement.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prepared_stmt` |  | prepared statement. |
| `prepared_stmt` |  | prepared statement. |

---

### reprepare_prepared_stmt_v1_t

```cpp
using reprepare_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2369

reprepare a prepare statement.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prepared_stmt` |  | prepared statement. |
| `prepared_stmt` |  | prepared statement. |

---

### execute_prepared_stmt_v1_t

```cpp
using execute_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2377

Record a prepare statement instrumentation execute event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a statement locker for the running thread. |
| `prepared_stmt` |  | prepared statement. |
| `locker` |  | a statement locker for the running thread. |
| `prepared_stmt` |  | prepared statement. |

---

### set_prepared_stmt_text_v1_t

```cpp
using set_prepared_stmt_text_v1_t = void(*
```

Defined in psi/psi.h:2386

Set the statement text for a prepared statement event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prepared_stmt` |  | prepared statement. |
| `text` |  | the prepared statement text |
| `text_len` |  | the prepared statement text length |
| `prepared_stmt` |  | prepared statement. |
| `text` |  | the prepared statement text |
| `text_len` |  | the prepared statement text length |

---

### digest_start_v1_t

```cpp
using digest_start_v1_t = struct PSI_digest_locker *(*
```

Defined in psi/psi.h:2386

Get a digest locker for the current statement.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a statement locker for the running thread |
| `locker` |  | a statement locker for the running thread |

---

### digest_end_v1_t

```cpp
using digest_end_v1_t = void(*
```

Defined in psi/psi.h:2401

Add a token to the current digest instrumentation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a digest locker for the current statement |
| `digest` |  | The digest storage to add the token to |
| `locker` |  | a digest locker for the current statement |
| `digest` |  | The digest storage to add the token to |

---

### start_sp_v1_t

```cpp
using start_sp_v1_t = PSI_sp_locker *(*
```

Defined in psi/psi.h:2404

---

### end_sp_v1_t

```cpp
using end_sp_v1_t = void(*
```

Defined in psi/psi.h:2407

---

### drop_sp_v1_t

```cpp
using drop_sp_v1_t = void(*
```

Defined in psi/psi.h:2410

---

### get_sp_share_v1_t

```cpp
using get_sp_share_v1_t = struct PSI_sp_share *(*
```

Defined in psi/psi.h:2410

Acquire a sp share instrumentation. 
#### Returns
a stored program share instrumentation, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `object_type` |  | of stored program |
| `schema_name` |  | of stored program |
| `schema_name_length` |  | of stored program |
| `object_name` |  | of stored program |
| `object_name_length` |  | of stored program |
| `object_type` |  | of stored program |
| `schema_name` |  | of stored program |
| `schema_name_length` |  | of stored program |
| `object_name` |  | of stored program |
| `object_name_length` |  | of stored program |

---

### release_sp_share_v1_t

```cpp
using release_sp_share_v1_t = void(*
```

Defined in psi/psi.h:2433

Release a stored program share.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `share` |  | the stored program share to release |
| `share` |  | the stored program share to release |

---

### create_metadata_lock_v1_t

```cpp
using create_metadata_lock_v1_t = PSI_metadata_lock *(*
```

Defined in psi/psi.h:2435

---

### set_metadata_lock_status_v1_t

```cpp
using set_metadata_lock_status_v1_t = void(*
```

Defined in psi/psi.h:2444

---

### destroy_metadata_lock_v1_t

```cpp
using destroy_metadata_lock_v1_t = void(*
```

Defined in psi/psi.h:2447

---

### start_metadata_wait_v1_t

```cpp
using start_metadata_wait_v1_t = struct PSI_metadata_locker *(*
```

Defined in psi/psi.h:2447

---

### end_metadata_wait_v1_t

```cpp
using end_metadata_wait_v1_t = void(*
```

Defined in psi/psi.h:2454

---

### set_thread_connect_attrs_v1_t

```cpp
using set_thread_connect_attrs_v1_t = int(*
```

Defined in psi/psi.h:2467

Stores an array of connection attributes 
#### Returns
state

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `buffer` |  | char array of length encoded connection attributes in network format |
| `length` |  | length of the data in buffer |
| `from_cs` |  | charset in which `buffer` is encoded |
| `buffer` |  | char array of length encoded connection attributes in network format |
| `length` |  | length of the data in buffer |
| `from_cs` |  | charset in which `buffer` is encoded |

#### Return Values

| Value | Description |
|-------|-------------|
| `non_0` | attributes truncated |
| `0` | stored the attribute |

---

### PSI

```cpp
using PSI = struct PSI_v1
```

Type: struct [`PSI_v1`](Group_PSI_v1.md#psi_v1)

Defined in psi/psi.h:2932

The instrumentation interface for the current version. **See also**: PSI_CURRENT_VERSION

---

### PSI_mutex_info

```cpp
using PSI_mutex_info = struct PSI_mutex_info_v1
```

Type: struct [`PSI_mutex_info_v1`](Group_PSI_v1.md#psi_mutex_info_v1-1)

Defined in psi/psi.h:2933

The mutex information structure for the current version.

---

### PSI_rwlock_info

```cpp
using PSI_rwlock_info = struct PSI_rwlock_info_v1
```

Type: struct [`PSI_rwlock_info_v1`](Group_PSI_v1.md#psi_rwlock_info_v1-1)

Defined in psi/psi.h:2934

The rwlock information structure for the current version.

---

### PSI_cond_info

```cpp
using PSI_cond_info = struct PSI_cond_info_v1
```

Type: struct [`PSI_cond_info_v1`](Group_PSI_v1.md#psi_cond_info_v1-1)

Defined in psi/psi.h:2935

The cond information structure for the current version.

---

### PSI_thread_info

```cpp
using PSI_thread_info = struct PSI_thread_info_v1
```

Type: struct [`PSI_thread_info_v1`](Group_PSI_v1.md#psi_thread_info_v1-1)

Defined in psi/psi.h:2936

The thread information structure for the current version.

---

### PSI_file_info

```cpp
using PSI_file_info = struct PSI_file_info_v1
```

Type: struct [`PSI_file_info_v1`](Group_PSI_v1.md#psi_file_info_v1-1)

Defined in psi/psi.h:2937

The file information structure for the current version.

---

### PSI_stage_info

```cpp
using PSI_stage_info = struct PSI_stage_info_v1
```

Type: struct [`PSI_stage_info_v1`](Group_PSI_v1.md#psi_stage_info_v1-1)

Defined in psi/psi.h:2938

The stage instrumentation has to co exist with the legacy THD::set_proc_info instrumentation. To avoid duplication of the instrumentation in the server, the common PSI_stage_info structure is used, so we export it here, even when not building with HAVE_PSI_INTERFACE.

---

### PSI_statement_info

```cpp
using PSI_statement_info = struct PSI_statement_info_v1
```

Type: struct [`PSI_statement_info_v1`](Group_PSI_v1.md#psi_statement_info_v1-1)

Defined in psi/psi.h:2939

---

### PSI_transaction_info

```cpp
using PSI_transaction_info = struct PSI_transaction_info_v1
```

Defined in psi/psi.h:2940

---

### PSI_socket_info

```cpp
using PSI_socket_info = struct PSI_socket_info_v1
```

Type: struct [`PSI_socket_info_v1`](Group_PSI_v1.md#psi_socket_info_v1-1)

Defined in psi/psi.h:2941

---

### PSI_idle_locker_state

```cpp
using PSI_idle_locker_state = struct PSI_idle_locker_state_v1
```

Type: struct [`PSI_idle_locker_state_v1`](Group_PSI_v1.md#psi_idle_locker_state_v1-1)

Defined in psi/psi.h:2942

---

### PSI_mutex_locker_state

```cpp
using PSI_mutex_locker_state = struct PSI_mutex_locker_state_v1
```

Type: struct [`PSI_mutex_locker_state_v1`](Group_PSI_v1.md#psi_mutex_locker_state_v1-1)

Defined in psi/psi.h:2943

---

### PSI_rwlock_locker_state

```cpp
using PSI_rwlock_locker_state = struct PSI_rwlock_locker_state_v1
```

Type: struct [`PSI_rwlock_locker_state_v1`](Group_PSI_v1.md#psi_rwlock_locker_state_v1-1)

Defined in psi/psi.h:2944

---

### PSI_cond_locker_state

```cpp
using PSI_cond_locker_state = struct PSI_cond_locker_state_v1
```

Type: struct [`PSI_cond_locker_state_v1`](Group_PSI_v1.md#psi_cond_locker_state_v1-1)

Defined in psi/psi.h:2945

---

### PSI_file_locker_state

```cpp
using PSI_file_locker_state = struct PSI_file_locker_state_v1
```

Type: struct [`PSI_file_locker_state_v1`](Group_PSI_v1.md#psi_file_locker_state_v1-1)

Defined in psi/psi.h:2946

---

### PSI_statement_locker_state

```cpp
using PSI_statement_locker_state = struct PSI_statement_locker_state_v1
```

Type: struct [`PSI_statement_locker_state_v1`](Group_PSI_v1.md#psi_statement_locker_state_v1-1)

Defined in psi/psi.h:2947

---

### PSI_transaction_locker_state

```cpp
using PSI_transaction_locker_state = struct PSI_transaction_locker_state_v1
```

Type: struct [`PSI_transaction_locker_state_v1`](Group_PSI_v1.md#psi_transaction_locker_state_v1-1)

Defined in psi/psi.h:2948

---

### PSI_socket_locker_state

```cpp
using PSI_socket_locker_state = struct PSI_socket_locker_state_v1
```

Type: struct [`PSI_socket_locker_state_v1`](Group_PSI_v1.md#psi_socket_locker_state_v1-1)

Defined in psi/psi.h:2949

---

### PSI_sp_locker_state

```cpp
using PSI_sp_locker_state = struct PSI_sp_locker_state_v1
```

Type: struct [`PSI_sp_locker_state_v1`](Group_PSI_v1.md#psi_sp_locker_state_v1-1)

Defined in psi/psi.h:2950

---

### PSI_metadata_locker_state

```cpp
using PSI_metadata_locker_state = struct PSI_metadata_locker_state_v1
```

Type: struct [`PSI_metadata_locker_state_v1`](Group_PSI_v1.md#psi_metadata_locker_state_v1-1)

Defined in psi/psi.h:2951

---

### PSI_metadata_locker

```cpp
using PSI_metadata_locker = struct PSI_stage_info_none
```

Type: struct [`PSI_stage_info_none`](Instrumentation_interface.md#psi_stage_info_none)

Defined in psi/psi.h:3017

---

### my_bool

```cpp
using my_bool = char
```

Defined in plugin.h:72

---

### MYSQL_PLUGIN

```cpp
using MYSQL_PLUGIN = void *
```

Defined in plugin.h:78

Opaque type for a plugin handle.

---

### MYSQL_XID

```cpp
using MYSQL_XID = struct st_mysql_xid
```

Type: struct [`st_mysql_xid`](storage_engine_plugin_data.md#st_mysql_xid)

Defined in plugin.h:102

---

### mysql_show_var_func

```cpp
using mysql_show_var_func = int(*
```

Defined in plugin.h:299

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

---

### PSI_memory_key

```cpp
using PSI_memory_key = unsigned int
```

Defined in psi/psi_base.h:175

Instrumented memory key. To instrument memory, a memory key must be obtained using `register_memory`. Using a zero key always disable the instrumentation.

---

### MYSQL_FILE

```cpp
using MYSQL_FILE = struct st_mysql_file
```

Type: struct [`st_mysql_file`](File_instrumentation.md#st_mysql_file)

Defined in psi/mysql_file.h:515

Type of an instrumented file. `MYSQL_FILE` is a drop-in replacement for `FILE`. **See also**: [mysql_file_open](#mysql_file_open)

---

### PSI_memory_info_v1

```cpp
using PSI_memory_info_v1 = struct PSI_memory_info_v1
```

Type: struct [`PSI_memory_info_v1`](Group_PSI_v1.md#psi_memory_info_v1-1)

Defined in psi/psi_memory.h:80

---

### register_memory_v1_t

```cpp
using register_memory_v1_t = void(*
```

Defined in psi/psi_memory.h:88

Memory registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of memory info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of memory info to register |
| `count` |  | the size of the info array |

---

### memory_alloc_v1_t

```cpp
using memory_alloc_v1_t = PSI_memory_key(*
```

Defined in psi/psi_memory.h:98

Instrument memory allocation. 
#### Returns
the effective memory instrument key

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |

---

### memory_realloc_v1_t

```cpp
using memory_realloc_v1_t = PSI_memory_key(*
```

Defined in psi/psi_memory.h:109

Instrument memory re allocation. 
#### Returns
the effective memory instrument key

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the memory instrument key |
| `old_size` |  | the size of memory previously allocated |
| `new_size` |  | the size of memory re allocated |
| `owner` |  | the memory owner |
| `key` |  | the memory instrument key |
| `old_size` |  | the size of memory previously allocated |
| `new_size` |  | the size of memory re allocated |
| `owner` |  | the memory owner |

---

### memory_claim_v1_t

```cpp
using memory_claim_v1_t = PSI_memory_key(*
```

Defined in psi/psi_memory.h:119

Instrument memory claim. 
#### Returns
the effective memory instrument key

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |

---

### memory_free_v1_t

```cpp
using memory_free_v1_t = void(*
```

Defined in psi/psi_memory.h:128

Instrument memory free.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |

---

### PSI_memory_info

```cpp
using PSI_memory_info = struct PSI_memory_info_v1
```

Type: struct [`PSI_memory_info_v1`](Group_PSI_v1.md#psi_memory_info_v1-1)

Defined in psi/psi_memory.h:148

---

### MYSQL_SERVER_AUTH_INFO

```cpp
using MYSQL_SERVER_AUTH_INFO = struct st_mysql_server_auth_info
```

Type: struct [`st_mysql_server_auth_info`](authentication_plugin.md#st_mysql_server_auth_info)

Defined in plugin_auth.h:128

Provides server plugin access to authentication information

---

### MYSQL_SOCKET

```cpp
using MYSQL_SOCKET = struct st_mysql_socket
```

Type: struct [`st_mysql_socket`](Socket_instrumentation.md#st_mysql_socket)

Defined in psi/mysql_socket.h:101

An instrumented socket. `MYSQL_SOCKET` is a replacement for `my_socket`.

---

### mysql_mutex_t

```cpp
using mysql_mutex_t = struct st_mysql_mutex
```

Type: struct [`st_mysql_mutex`](Thread_instrumentation.md#st_mysql_mutex)

Defined in psi/mysql_thread.h:159

Type of an instrumented mutex. `mysql_mutex_t` is a drop-in replacement for `pthread_mutex_t`. **See also**: [mysql_mutex_assert_owner](#mysql_mutex_assert_owner)

**See also**: [mysql_mutex_assert_not_owner](#mysql_mutex_assert_not_owner)

**See also**: [mysql_mutex_init](#mysql_mutex_init)

**See also**: [mysql_mutex_lock](#mysql_mutex_lock)

**See also**: [mysql_mutex_unlock](#mysql_mutex_unlock)

**See also**: [mysql_mutex_destroy](#mysql_mutex_destroy)

---

### mysql_rwlock_t

```cpp
using mysql_rwlock_t = struct st_mysql_rwlock
```

Type: struct [`st_mysql_rwlock`](Thread_instrumentation.md#st_mysql_rwlock)

Defined in psi/mysql_thread.h:204

Type of an instrumented rwlock. `mysql_rwlock_t` is a drop-in replacement for `pthread_rwlock_t`. **See also**: [mysql_rwlock_init](#mysql_rwlock_init)

**See also**: [mysql_rwlock_rdlock](#mysql_rwlock_rdlock)

**See also**: [mysql_rwlock_tryrdlock](#mysql_rwlock_tryrdlock)

**See also**: [mysql_rwlock_wrlock](#mysql_rwlock_wrlock)

**See also**: [mysql_rwlock_trywrlock](#mysql_rwlock_trywrlock)

**See also**: [mysql_rwlock_unlock](#mysql_rwlock_unlock)

**See also**: [mysql_rwlock_destroy](#mysql_rwlock_destroy)

---

### mysql_prlock_t

```cpp
using mysql_prlock_t = struct st_mysql_prlock
```

Type: struct [`st_mysql_prlock`](Thread_instrumentation.md#st_mysql_prlock)

Defined in psi/mysql_thread.h:216

Type of an instrumented prlock. A prlock is a read write lock that 'prefers readers' (pr). `mysql_prlock_t` is a drop-in replacement for `rw_pr_lock_t`. **See also**: [mysql_prlock_init](#mysql_prlock_init)

**See also**: [mysql_prlock_rdlock](#mysql_prlock_rdlock)

**See also**: [mysql_prlock_wrlock](#mysql_prlock_wrlock)

**See also**: [mysql_prlock_unlock](#mysql_prlock_unlock)

**See also**: [mysql_prlock_destroy](#mysql_prlock_destroy)

---

### mysql_cond_t

```cpp
using mysql_cond_t = struct st_mysql_cond
```

Type: struct [`st_mysql_cond`](Thread_instrumentation.md#st_mysql_cond)

Defined in psi/mysql_thread.h:244

Type of an instrumented condition. `mysql_cond_t` is a drop-in replacement for `pthread_cond_t`. **See also**: [mysql_cond_init](#mysql_cond_init)

**See also**: [mysql_cond_wait](#mysql_cond_wait)

**See also**: [mysql_cond_timedwait](#mysql_cond_timedwait)

**See also**: [mysql_cond_signal](#mysql_cond_signal)

**See also**: [mysql_cond_broadcast](#mysql_cond_broadcast)

**See also**: [mysql_cond_destroy](#mysql_cond_destroy)

---

### query_id_t

```cpp
using query_id_t = int64
```

Defined in service_wsrep.h:60

Must match to definition in sql/mysqld.h

---

### LOGGER_HANDLE

```cpp
using LOGGER_HANDLE = struct logger_handle_st
```

Defined in service_logger.h:69

---

### MYSQL_FTPARSER_BOOLEAN_INFO

```cpp
using MYSQL_FTPARSER_BOOLEAN_INFO = struct st_mysql_ftparser_boolean_info
```

Type: struct [`st_mysql_ftparser_boolean_info`](ftparser_plugin_data.md#st_mysql_ftparser_boolean_info)

Defined in plugin_ftparser.h:145

Structure for boolean mode search.

This structure is used in boolean search mode only. It conveys boolean-mode metadata to the MySQL search engine for every word in the search query. A valid instance of this structure must be filled in by the plugin parser and passed as an argument in the call to mysql_add_word (the callback function in the MYSQL_FTPARSER_PARAM structure) when a query is parsed in boolean mode.

---

### MYSQL_FTPARSER_PARAM

```cpp
using MYSQL_FTPARSER_PARAM = struct st_mysql_ftparser_param
```

Type: struct [`st_mysql_ftparser_param`](ftparser_plugin_data.md#st_mysql_ftparser_param)

Defined in plugin_ftparser.h:231

An argument of the full-text parser plugin.

This structure is filled in by MySQL server and passed to the parsing function of the plugin as an in/out parameter.

---

### CHARSET_INFO

```cpp
using CHARSET_INFO = const struct charset_info_st
```

Defined in psi/mysql_statement.h:41

---

### thd_wait_type

```cpp
using thd_wait_type = enum _thd_wait_type_e
```

Type: enum [`_thd_wait_type_e`](#thd_wait_type_e)

Defined in service_thd_wait.h:70

---

### MYSQL_CONST_LEX_STRING

```cpp
using MYSQL_CONST_LEX_STRING = struct st_mysql_const_lex_string
```

Type: struct [`st_mysql_const_lex_string`](plugin_api_service_thd_alloc.md#st_mysql_const_lex_string)

Defined in service_thd_alloc.h:56

---

### MYSQL_LEX_STRING

```cpp
using MYSQL_LEX_STRING = struct st_mysql_lex_string
```

Type: struct [`st_mysql_lex_string`](plugin_api_service_thd_alloc.md#st_mysql_lex_string)

Defined in service_thd_alloc.h:70

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

---

### MYSQL_PLUGIN_VIO_INFO

```cpp
using MYSQL_PLUGIN_VIO_INFO = struct st_plugin_vio_info
```

Type: struct [`st_plugin_vio_info`](authentication_plugin.md#st_plugin_vio_info)

Defined in plugin_auth_common.h:110

---

### MYSQL_PLUGIN_VIO

```cpp
using MYSQL_PLUGIN_VIO = struct st_plugin_vio
```

Type: struct [`st_plugin_vio`](authentication_plugin.md#st_plugin_vio)

Defined in plugin_auth_common.h:139

Provides plugin access to communication channel

---

### MYSQL_THD_KEY_T

```cpp
using MYSQL_THD_KEY_T = int
```

Defined in service_thd_specifics.h:72

## Functions

---

### SHOW_FUNC_ENTRY

`static` `inline`

```cpp
static inline struct st_mysql_show_var SHOW_FUNC_ENTRY(const char * name, mysql_show_var_func func_arg, const char * name, mysql_show_var_func func_arg)
```

Defined in plugin.h:303

---

### thd_in_lock_tables

```cpp
int thd_in_lock_tables(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:904

---

### thd_tablespace_op

```cpp
int thd_tablespace_op(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:905

---

### thd_test_options

```cpp
long long thd_test_options(const MYSQL_THD thd, long long test_options, const MYSQL_THD thd, long long test_options)
```

Defined in plugin.h:906

---

### thd_sql_command

```cpp
int thd_sql_command(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:907

---

### thd_ddl_options

```cpp
struct DDL_options_st * thd_ddl_options(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:909

---

### thd_storage_lock_wait

```cpp
void thd_storage_lock_wait(MYSQL_THD thd, long long value, MYSQL_THD thd, long long value)
```

Defined in plugin.h:910

---

### thd_tx_isolation

```cpp
int thd_tx_isolation(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:911

---

### thd_tx_is_read_only

```cpp
int thd_tx_is_read_only(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:912

---

### mysql_tmpfile

```cpp
int mysql_tmpfile(const char * prefix, const char * prefix)
```

Defined in plugin.h:926

Create a temporary file.

The temporary file is created in a location specified by the mysql server configuration (&ndash;tmpdir option). The caller does not need to delete the file, it will be deleted automatically.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prefix` | `const char *` | prefix for temporary file name |
| `prefix` | `const char *` | prefix for temporary file name |

#### Return Values

| Value | Description |
|-------|-------------|
| `-1` | error |
| `>=` | 0 a file handle that can be passed to dup or my_close |

---

### thd_get_thread_id

```cpp
unsigned long thd_get_thread_id(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:934

Return the thread id of a user thread

#### Returns
thread id

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |

---

### thd_get_xid

```cpp
void thd_get_xid(const MYSQL_THD thd, MYSQL_XID * xid, const MYSQL_THD thd, MYSQL_XID * xid)
```

Defined in plugin.h:946

Get the XID for this connection's transaction

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |
| `xid` | [`MYSQL_XID`](#mysql_xid) * | location where identifier is stored |
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |
| `xid` | [`MYSQL_XID`](#mysql_xid) * | location where identifier is stored |

---

### mysql_query_cache_invalidate4

```cpp
void mysql_query_cache_invalidate4(MYSQL_THD thd, const char * key, unsigned int key_length, int using_trx, MYSQL_THD thd, const char * key, unsigned int key_length, int using_trx)
```

Defined in plugin.h:958

Invalidate the query cache for a given table.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | [`MYSQL_THD`](#mysql_thd) | user thread connection handle |
| `key` | `const char *` | databasename\0tablename\0 |
| `key_length` | `unsigned int` | length of key in bytes, including the NUL bytes |
| `using_trx` | `int` | flag: TRUE if using transactions, FALSE otherwise |
| `thd` | [`MYSQL_THD`](#mysql_thd) | user thread connection handle |
| `key` | `const char *` | databasename\0tablename\0 |
| `key_length` | `unsigned int` | length of key in bytes, including the NUL bytes |
| `using_trx` | `int` | flag: TRUE if using transactions, FALSE otherwise |

---

### thd_get_ha_data

```cpp
void * thd_get_ha_data(const MYSQL_THD thd, const struct transaction_participant * hton, const MYSQL_THD thd, const struct transaction_participant * hton)
```

Defined in plugin.h:966

Provide a handler data getter to simplify coding

---

### thd_set_ha_data

```cpp
void thd_set_ha_data(MYSQL_THD thd, const struct transaction_participant * hton, const void * ha_data, MYSQL_THD thd, const struct transaction_participant * hton, const void * ha_data)
```

Defined in plugin.h:990

Provide a handler data setter to simplify coding

Set ha_data pointer (storage engine per-connection information).

To avoid unclean deactivation (uninstall) of storage engine plugin in the middle of transaction, additional storage engine plugin lock is acquired.

If ha_data is not null and storage engine plugin was not locked by [thd_set_ha_data()](#thd_set_ha_data) in this connection before, storage engine plugin gets locked.

If ha_data is null and storage engine plugin was locked by [thd_set_ha_data()](#thd_set_ha_data) in this connection before, storage engine plugin lock gets released.

If transaction_participant::close_connection() didn't reset ha_data, server does it immediately after calling transaction_participant::close_connection()

---

### thd_wakeup_subsequent_commits

```cpp
void thd_wakeup_subsequent_commits(MYSQL_THD thd, int wakeup_error, MYSQL_THD thd, int wakeup_error)
```

Defined in plugin.h:1025

Signal that the first part of handler commit is finished, and that the committed transaction is now visible and has fixed commit ordering with respect to other transactions. The commit need *not* be durable yet, and typically will not be when this call makes sense.

This call is optional, if the storage engine does not call it the upper layer will after the handler commit() method is done. However, the storage engine may choose to call it itself to increase the possibility for group commit.

In-order parallel replication uses this to apply different transaction in parallel, but delay the commits of later transactions until earlier transactions have committed first, thus achieving increased performance on multi-core systems while still preserving full transaction consistency.

The storage engine can call this from within the commit() method, typically after the commit record has been written to the transaction log, but before the log has been fsync()'ed. This will allow the next replicated transaction to proceed to commit before the first one has done fsync() or similar. Thus, it becomes possible for multiple sequential replicated transactions to share a single fsync() inside the engine in group commit.

Note that this method should *not* be called from within the commit_ordered() method, or any other place in the storage engine. When commit_ordered() is used (typically when binlog is enabled), the transaction coordinator takes care of this and makes group commit in the storage engine possible without any other action needed on the part of the storage engine. This function [thd_wakeup_subsequent_commits()](#thd_wakeup_subsequent_commits) is only needed when no transaction coordinator is used, meaning a single storage engine and no binary log.

---

### inline_mysql_file_register

`static` `inline`

```cpp
static inline void inline_mysql_file_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_file.h:517

---

### inline_mysql_file_fgets

`static` `inline`

```cpp
static inline char * inline_mysql_file_fgets(char * str, int size, MYSQL_FILE * file, char * str, int size, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:535

---

### inline_mysql_file_fgetc

`static` `inline`

```cpp
static inline int inline_mysql_file_fgetc(MYSQL_FILE * file, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:563

---

### inline_mysql_file_fputs

`static` `inline`

```cpp
static inline int inline_mysql_file_fputs(const char * str, MYSQL_FILE * file, const char * str, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:591

---

### inline_mysql_file_fputc

`static` `inline`

```cpp
static inline int inline_mysql_file_fputc(char c, MYSQL_FILE * file, char c, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:621

---

### inline_mysql_file_fprintf

`static` `inline`

```cpp
static inline int inline_mysql_file_fprintf(MYSQL_FILE * file, const char * format, ..., MYSQL_FILE * file, const char * format, ...)
```

Defined in psi/mysql_file.h:649

---

### inline_mysql_file_vfprintf

`static` `inline`

```cpp
static inline int inline_mysql_file_vfprintf(MYSQL_FILE * file, const char * format, va_list args, MYSQL_FILE * file, const char * format, va_list args)
```

Defined in psi/mysql_file.h:681

---

### inline_mysql_file_fflush

`static` `inline`

```cpp
static inline int inline_mysql_file_fflush(MYSQL_FILE * file, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:709

---

### inline_mysql_file_feof

`static` `inline`

```cpp
static inline int inline_mysql_file_feof(MYSQL_FILE * file, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:736

---

### inline_mysql_file_fstat

`static` `inline`

```cpp
static inline int inline_mysql_file_fstat(int filenr, MY_STAT * stat_area, myf flags, int filenr, MY_STAT * stat_area, myf flags)
```

Defined in psi/mysql_file.h:743

---

### inline_mysql_file_stat

`static` `inline`

```cpp
static inline MY_STAT * inline_mysql_file_stat(const char * path, MY_STAT * stat_area, myf flags, const char * path, MY_STAT * stat_area, myf flags)
```

Defined in psi/mysql_file.h:768

---

### inline_mysql_file_chsize

`static` `inline`

```cpp
static inline int inline_mysql_file_chsize(File file, my_off_t newlength, int filler, myf flags, File file, my_off_t newlength, int filler, myf flags)
```

Defined in psi/mysql_file.h:793

---

### inline_mysql_file_fopen

`static` `inline`

```cpp
static inline MYSQL_FILE * inline_mysql_file_fopen(const char * filename, int flags, myf myFlags, const char * filename, int flags, myf myFlags)
```

Defined in psi/mysql_file.h:819

---

### inline_mysql_file_fclose

`static` `inline`

```cpp
static inline int inline_mysql_file_fclose(MYSQL_FILE * file, myf flags, MYSQL_FILE * file, myf flags)
```

Defined in psi/mysql_file.h:861

---

### inline_mysql_file_fread

`static` `inline`

```cpp
static inline size_t inline_mysql_file_fread(MYSQL_FILE * file, uchar * buffer, size_t count, myf flags, MYSQL_FILE * file, uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql_file.h:895

---

### inline_mysql_file_fwrite

`static` `inline`

```cpp
static inline size_t inline_mysql_file_fwrite(MYSQL_FILE * file, const uchar * buffer, size_t count, myf flags, MYSQL_FILE * file, const uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql_file.h:928

---

### inline_mysql_file_fseek

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_fseek(MYSQL_FILE * file, my_off_t pos, int whence, myf flags, MYSQL_FILE * file, my_off_t pos, int whence, myf flags)
```

Defined in psi/mysql_file.h:961

---

### inline_mysql_file_ftell

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_ftell(MYSQL_FILE * file, myf flags, MYSQL_FILE * file, myf flags)
```

Defined in psi/mysql_file.h:989

---

### inline_mysql_file_create

`static` `inline`

```cpp
static inline File inline_mysql_file_create(const char * filename, mode_t create_flags, int access_flags, myf myFlags, const char * filename, mode_t create_flags, int access_flags, myf myFlags)
```

Defined in psi/mysql_file.h:1017

---

### inline_mysql_file_create_temp

`static` `inline`

```cpp
static inline File inline_mysql_file_create_temp(char * to, const char * dir, const char * pfx, int mode, myf myFlags, char * to, const char * dir, const char * pfx, int mode, myf myFlags)
```

Defined in psi/mysql_file.h:1043

---

### inline_mysql_file_open

`static` `inline`

```cpp
static inline File inline_mysql_file_open(const char * filename, int flags, myf myFlags, const char * filename, int flags, myf myFlags)
```

Defined in psi/mysql_file.h:1070

---

### inline_mysql_file_close

`static` `inline`

```cpp
static inline int inline_mysql_file_close(File file, myf flags, File file, myf flags)
```

Defined in psi/mysql_file.h:1096

---

### inline_mysql_file_read

`static` `inline`

```cpp
static inline size_t inline_mysql_file_read(File file, uchar * buffer, size_t count, myf flags, File file, uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql_file.h:1121

---

### inline_mysql_file_write

`static` `inline`

```cpp
static inline size_t inline_mysql_file_write(File file, const uchar * buffer, size_t count, myf flags, File file, const uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql_file.h:1151

---

### inline_mysql_file_pread

`static` `inline`

```cpp
static inline size_t inline_mysql_file_pread(File file, uchar * buffer, size_t count, my_off_t offset, myf flags, File file, uchar * buffer, size_t count, my_off_t offset, myf flags)
```

Defined in psi/mysql_file.h:1181

---

### inline_mysql_file_pwrite

`static` `inline`

```cpp
static inline size_t inline_mysql_file_pwrite(File file, const uchar * buffer, size_t count, my_off_t offset, myf flags, File file, const uchar * buffer, size_t count, my_off_t offset, myf flags)
```

Defined in psi/mysql_file.h:1211

---

### inline_mysql_file_seek

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_seek(File file, my_off_t pos, int whence, myf flags, File file, my_off_t pos, int whence, myf flags)
```

Defined in psi/mysql_file.h:1241

---

### inline_mysql_file_tell

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_tell(File file, myf flags, File file, myf flags)
```

Defined in psi/mysql_file.h:1266

---

### inline_mysql_file_delete

`static` `inline`

```cpp
static inline int inline_mysql_file_delete(const char * name, myf flags, const char * name, myf flags)
```

Defined in psi/mysql_file.h:1291

---

### inline_mysql_file_rename

`static` `inline`

```cpp
static inline int inline_mysql_file_rename(const char * from, const char * to, myf flags, const char * from, const char * to, myf flags)
```

Defined in psi/mysql_file.h:1316

---

### inline_mysql_file_create_with_symlink

`static` `inline`

```cpp
static inline File inline_mysql_file_create_with_symlink(const char * linkname, const char * filename, mode_t create_flags, int access_flags, myf flags, const char * linkname, const char * filename, mode_t create_flags, int access_flags, myf flags)
```

Defined in psi/mysql_file.h:1343

---

### inline_mysql_file_delete_with_symlink

`static` `inline`

```cpp
static inline int inline_mysql_file_delete_with_symlink(const char * name, const char * ext, myf flags, const char * name, const char * ext, myf flags)
```

Defined in psi/mysql_file.h:1373

---

### inline_mysql_file_rename_with_symlink

`static` `inline`

```cpp
static inline int inline_mysql_file_rename_with_symlink(const char * from, const char * to, myf flags, const char * from, const char * to, myf flags)
```

Defined in psi/mysql_file.h:1402

---

### inline_mysql_file_sync

`static` `inline`

```cpp
static inline int inline_mysql_file_sync(File fd, myf flags, File fd, myf flags)
```

Defined in psi/mysql_file.h:1428

---

### inline_mysql_memory_register

`static` `inline`

```cpp
static inline void inline_mysql_memory_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_memory.h:61

---

### mysql_socket_invalid

`static` `inline`

```cpp
static inline MYSQL_SOCKET mysql_socket_invalid()
```

Defined in psi/mysql_socket.h:117

MYSQL_SOCKET helper. Initialize instrumented socket. **See also**: mysql_socket_getfd 

**See also**: mysql_socket_setfd

---

### mysql_socket_set_address

`static` `inline`

```cpp
static inline void mysql_socket_set_address(MYSQL_SOCKET socket, const struct sockaddr * addr, socklen_t addr_len, MYSQL_SOCKET socket, const struct sockaddr * addr, socklen_t addr_len)
```

Defined in psi/mysql_socket.h:132

Set socket descriptor and address.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | instrumented socket |
| `addr` | `const struct sockaddr *` | unformatted socket address |
| `addr_len` | `socklen_t` | length of socket address |
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | instrumented socket |
| `addr` | `const struct sockaddr *` | unformatted socket address |
| `addr_len` | `socklen_t` | length of socket address |

---

### mysql_socket_set_thread_owner

`static` `inline`

```cpp
static inline void mysql_socket_set_thread_owner(MYSQL_SOCKET socket, MYSQL_SOCKET socket)
```

Defined in psi/mysql_socket.h:155

Set socket descriptor and address.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | instrumented socket |
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | instrumented socket |

---

### mysql_socket_getfd

`static` `inline`

```cpp
static inline my_socket mysql_socket_getfd(MYSQL_SOCKET mysql_socket, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql_socket.h:175

MYSQL_SOCKET helper. Get socket descriptor. **See also**: mysql_socket_getfd

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql_socket` | [`MYSQL_SOCKET`](#mysql_socket) | Instrumented socket |
| `mysql_socket` | [`MYSQL_SOCKET`](#mysql_socket) | Instrumented socket |

---

### mysql_socket_setfd

`static` `inline`

```cpp
static inline void mysql_socket_setfd(MYSQL_SOCKET * mysql_socket, my_socket fd, MYSQL_SOCKET * mysql_socket, my_socket fd)
```

Defined in psi/mysql_socket.h:187

MYSQL_SOCKET helper. Set socket descriptor. **See also**: mysql_socket_setfd

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql_socket` | [`MYSQL_SOCKET`](#mysql_socket) * | Instrumented socket |
| `fd` | `my_socket` | Socket descriptor |
| `mysql_socket` | [`MYSQL_SOCKET`](#mysql_socket) * | Instrumented socket |
| `fd` | `my_socket` | Socket descriptor |

---

### inline_mysql_start_socket_wait

`static` `inline`

```cpp
static inline struct PSI_socket_locker * inline_mysql_start_socket_wait(PSI_socket_locker_state * state, MYSQL_SOCKET mysql_socket, enum PSI_socket_operation op, size_t byte_count, const char * src_file, uint src_line, PSI_socket_locker_state * state, MYSQL_SOCKET mysql_socket, enum PSI_socket_operation op, size_t byte_count, const char * src_file, uint src_line)
```

Defined in psi/mysql_socket.h:268

Instrumentation calls for MYSQL_START_SOCKET_WAIT. **See also**: [MYSQL_START_SOCKET_WAIT](#mysql_start_socket_wait).

---

### inline_mysql_end_socket_wait

`static` `inline`

```cpp
static inline void inline_mysql_end_socket_wait(struct PSI_socket_locker * locker, size_t byte_count, struct PSI_socket_locker * locker, size_t byte_count)
```

Defined in psi/mysql_socket.h:290

Instrumentation calls for MYSQL_END_SOCKET_WAIT. **See also**: [MYSQL_END_SOCKET_WAIT](#mysql_end_socket_wait).

---

### inline_mysql_socket_set_state

`static` `inline`

```cpp
static inline void inline_mysql_socket_set_state(MYSQL_SOCKET socket, enum PSI_socket_state state, MYSQL_SOCKET socket, enum PSI_socket_state state)
```

Defined in psi/mysql_socket.h:303

Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI_socket_state

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | the instrumented socket |
| `state` | `enum PSI_socket_state` | the new state |
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | the instrumented socket |
| `state` | `enum PSI_socket_state` | the new state |

---

### inline_mysql_socket_register

`static` `inline`

```cpp
static inline void inline_mysql_socket_register(const char * category, PSI_socket_info * info, int count, const char * category, PSI_socket_info * info, int count)
```

Defined in psi/mysql_socket.h:591

---

### inline_mysql_socket_fd

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_fd(PSI_socket_key key, int fd, PSI_socket_key key, int fd)
```

Defined in psi/mysql_socket.h:603

mysql_socket_fd

---

### inline_mysql_socket_socket

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_socket(PSI_socket_key key, int domain, int type, int protocol, PSI_socket_key key, int domain, int type, int protocol)
```

Defined in psi/mysql_socket.h:636

mysql_socket_socket

---

### inline_mysql_socket_bind

`static` `inline`

```cpp
static inline int inline_mysql_socket_bind(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, size_t len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, size_t len)
```

Defined in psi/mysql_socket.h:665

mysql_socket_bind

---

### inline_mysql_socket_getsockname

`static` `inline`

```cpp
static inline int inline_mysql_socket_getsockname(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len)
```

Defined in psi/mysql_socket.h:705

mysql_socket_getsockname

---

### inline_mysql_socket_connect

`static` `inline`

```cpp
static inline int inline_mysql_socket_connect(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, socklen_t len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, socklen_t len)
```

Defined in psi/mysql_socket.h:743

mysql_socket_connect

---

### inline_mysql_socket_getpeername

`static` `inline`

```cpp
static inline int inline_mysql_socket_getpeername(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len)
```

Defined in psi/mysql_socket.h:781

mysql_socket_getpeername

---

### inline_mysql_socket_send

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_send(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags)
```

Defined in psi/mysql_socket.h:819

mysql_socket_send

---

### inline_mysql_socket_recv

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_recv(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags)
```

Defined in psi/mysql_socket.h:860

mysql_socket_recv

---

### inline_mysql_socket_sendto

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_sendto(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const struct sockaddr * addr, socklen_t addr_len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const struct sockaddr * addr, socklen_t addr_len)
```

Defined in psi/mysql_socket.h:901

mysql_socket_sendto

---

### inline_mysql_socket_recvfrom

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_recvfrom(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, struct sockaddr * addr, socklen_t * addr_len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, struct sockaddr * addr, socklen_t * addr_len)
```

Defined in psi/mysql_socket.h:942

mysql_socket_recvfrom

---

### inline_mysql_socket_getsockopt

`static` `inline`

```cpp
static inline int inline_mysql_socket_getsockopt(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, SOCKBUF_T * optval, socklen_t * optlen, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, SOCKBUF_T * optval, socklen_t * optlen)
```

Defined in psi/mysql_socket.h:984

mysql_socket_getsockopt

---

### inline_mysql_socket_setsockopt

`static` `inline`

```cpp
static inline int inline_mysql_socket_setsockopt(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, const SOCKBUF_T * optval, socklen_t optlen, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, const SOCKBUF_T * optval, socklen_t optlen)
```

Defined in psi/mysql_socket.h:1022

mysql_socket_setsockopt

---

### set_socket_nonblock

`static` `inline`

```cpp
static inline int set_socket_nonblock(my_socket fd, my_socket fd)
```

Defined in psi/mysql_socket.h:1060

set_socket_nonblock

---

### inline_mysql_sock_set_nonblocking

`static` `inline`

```cpp
static inline int inline_mysql_sock_set_nonblocking(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql_socket.h:1093

mysql_socket_set_nonblocking

---

### inline_mysql_socket_listen

`static` `inline`

```cpp
static inline int inline_mysql_socket_listen(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int backlog, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int backlog)
```

Defined in psi/mysql_socket.h:1133

mysql_socket_listen

---

### inline_mysql_socket_accept

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_accept(const char * src_file, uint src_line, PSI_socket_key key, MYSQL_SOCKET socket_listen, struct sockaddr * addr, socklen_t * addr_len, const char * src_file, uint src_line, PSI_socket_key key, MYSQL_SOCKET socket_listen, struct sockaddr * addr, socklen_t * addr_len)
```

Defined in psi/mysql_socket.h:1171

mysql_socket_accept

---

### inline_mysql_socket_close

`static` `inline`

```cpp
static inline int inline_mysql_socket_close(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql_socket.h:1252

mysql_socket_close

---

### inline_mysql_socket_shutdown

`static` `inline`

```cpp
static inline int inline_mysql_socket_shutdown(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int how, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int how)
```

Defined in psi/mysql_socket.h:1293

mysql_socket_shutdown

---

### inline_mysql_mutex_register

`static` `inline`

```cpp
static inline void inline_mysql_mutex_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:669

---

### inline_mysql_mutex_init

`static` `inline`

```cpp
static inline int inline_mysql_mutex_init(mysql_mutex_t * that, const pthread_mutexattr_t * attr, mysql_mutex_t * that, const pthread_mutexattr_t * attr)
```

Defined in psi/mysql_thread.h:686

---

### inline_mysql_mutex_destroy

`static` `inline`

```cpp
static inline int inline_mysql_mutex_destroy(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:709

---

### inline_mysql_mutex_lock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_lock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:737

---

### inline_mysql_mutex_trylock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_trylock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:756

---

### inline_mysql_mutex_unlock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_unlock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:775

---

### inline_mysql_rwlock_register

`static` `inline`

```cpp
static inline void inline_mysql_rwlock_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:798

---

### inline_mysql_rwlock_init

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_init(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:815

---

### inline_mysql_prlock_init

`static` `inline`

```cpp
static inline int inline_mysql_prlock_init(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:833

---

### inline_mysql_rwlock_destroy

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_destroy(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:848

---

### inline_mysql_prlock_destroy

`static` `inline`

```cpp
static inline int inline_mysql_prlock_destroy(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:862

---

### inline_mysql_rwlock_rdlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_rdlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:893

---

### inline_mysql_prlock_rdlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_rdlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:908

---

### inline_mysql_rwlock_wrlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_wrlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:923

---

### inline_mysql_prlock_wrlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_wrlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:938

---

### inline_mysql_rwlock_tryrdlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_tryrdlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:953

---

### inline_mysql_rwlock_trywrlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_trywrlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:967

---

### inline_mysql_rwlock_unlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_unlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:981

---

### inline_mysql_prlock_unlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_unlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:994

---

### inline_mysql_cond_register

`static` `inline`

```cpp
static inline void inline_mysql_cond_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:1007

---

### inline_mysql_cond_init

`static` `inline`

```cpp
static inline int inline_mysql_cond_init(mysql_cond_t * that, const pthread_condattr_t * attr, mysql_cond_t * that, const pthread_condattr_t * attr)
```

Defined in psi/mysql_thread.h:1024

---

### inline_mysql_cond_destroy

`static` `inline`

```cpp
static inline int inline_mysql_cond_destroy(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql_thread.h:1039

---

### inline_mysql_cond_wait

`static` `inline`

```cpp
static inline int inline_mysql_cond_wait(mysql_cond_t * that, mysql_mutex_t * mutex, mysql_cond_t * that, mysql_mutex_t * mutex)
```

Defined in psi/mysql_thread.h:1060

---

### inline_mysql_cond_timedwait

`static` `inline`

```cpp
static inline int inline_mysql_cond_timedwait(mysql_cond_t * that, mysql_mutex_t * mutex, const struct timespec * abstime, mysql_cond_t * that, mysql_mutex_t * mutex, const struct timespec * abstime)
```

Defined in psi/mysql_thread.h:1075

---

### inline_mysql_cond_signal

`static` `inline`

```cpp
static inline int inline_mysql_cond_signal(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql_thread.h:1091

---

### inline_mysql_cond_broadcast

`static` `inline`

```cpp
static inline int inline_mysql_cond_broadcast(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql_thread.h:1103

---

### inline_mysql_thread_register

`static` `inline`

```cpp
static inline void inline_mysql_thread_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:1115

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
| `plugin` | struct [`st_mysql_client_plugin`](plugin_client_api.md#st_mysql_client_plugin) * | an [st_mysql_client_plugin](plugin_client_api.md#st_mysql_client_plugin) structure to register |
| `mysql` | `struct st_mysql *` | MYSQL structure. It is only used for error reporting |
| `plugin` | struct [`st_mysql_client_plugin`](plugin_client_api.md#st_mysql_client_plugin) * | an [st_mysql_client_plugin](plugin_client_api.md#st_mysql_client_plugin) structure to register |

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
| `plugin` | struct [`st_mysql_client_plugin`](plugin_client_api.md#st_mysql_client_plugin) * | an [st_mysql_client_plugin](plugin_client_api.md#st_mysql_client_plugin) structure |
| `option` | `const char *` | a string which specifies the option to set |
| `value` | `const void *` | value for the option. |
| `plugin` | struct [`st_mysql_client_plugin`](plugin_client_api.md#st_mysql_client_plugin) * | an [st_mysql_client_plugin](plugin_client_api.md#st_mysql_client_plugin) structure |
| `option` | `const char *` | a string which specifies the option to set |
| `value` | `const void *` | value for the option. |

#### Return Values

| Value | Description |
|-------|-------------|
| `0` | on success, 1 in case of failure |

---

### encryption_key_id_exists

`static` `inline`

```cpp
static inline unsigned int encryption_key_id_exists(unsigned int id, unsigned int id)
```

Defined in service_encryption.h:100

---

### encryption_key_version_exists

`static` `inline`

```cpp
static inline unsigned int encryption_key_version_exists(unsigned int id, unsigned int version, unsigned int id, unsigned int version)
```

Defined in service_encryption.h:105

---

### encryption_crypt

`static` `inline`

```cpp
static inline int encryption_crypt(const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen, int flags, unsigned int key_id, unsigned int key_version, const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen, int flags, unsigned int key_id, unsigned int key_version)
```

Defined in service_encryption.h:116

main entrypoint to perform encryption or decryption 
#### Invariants
`src` is valid for `slen`

#### Invariants
`dst` is valid for `*dlen`, `*dlen` is initialized 

#### Invariants
`src` and `dst` do not overlap

## Variables

---

### PSI_server

```cpp
MYSQL_PLUGIN_IMPORT PSI * PSI_server
```

Type: MYSQL_PLUGIN_IMPORT [`PSI`](#psi) *

Defined in psi/psi.h:3021

---

### my_md5_service

```cpp
struct my_md5_service_st * my_md5_service
```

Type: struct [`my_md5_service_st`](plugin_api_service_md5.md#my_md5_service_st) *

Defined in service_md5.h:49

---

### sql_service

```cpp
struct sql_service_st * sql_service
```

Type: struct [`sql_service_st`](plugin_api_service_sql.md#sql_service_st) *

Defined in service_sql.h:86

---

### thd_service

```cpp
struct thd_service_st * thd_service
```

Type: struct [`thd_service_st`](plugin_api_service_thd.md#thd_service_st) *

Defined in service_thd.h:42

---

### json_service

```cpp
struct json_service_st * json_service
```

Type: struct [`json_service_st`](plugin_api_service_json.md#json_service_st) *

Defined in service_json.h:89

---

### my_sha1_service

```cpp
struct my_sha1_service_st * my_sha1_service
```

Type: struct [`my_sha1_service_st`](plugin_api_service_sha1.md#my_sha1_service_st) *

Defined in service_sha1.h:50

---

### my_sha2_service

```cpp
struct my_sha2_service_st * my_sha2_service
```

Type: struct [`my_sha2_service_st`](plugin_api_service_sha2.md#my_sha2_service_st) *

Defined in service_sha2.h:71

---

### wsrep_service

```cpp
struct wsrep_service_st * wsrep_service
```

Type: struct [`wsrep_service_st`](plugin_api_service_wsrep.md#wsrep_service_st) *

Defined in service_wsrep.h:110

---

### base64_service

```cpp
struct base64_service_st * base64_service
```

Type: struct [`base64_service_st`](plugin_api_service_base64.md#base64_service_st) *

Defined in service_base64.h:55

---

### logger_service

```cpp
struct logger_service_st * logger_service
```

Type: struct [`logger_service_st`](plugin_api_service_logger.md#logger_service_st) *

Defined in service_logger.h:88

---

### thd_mdl_service

```cpp
struct thd_mdl_service_st * thd_mdl_service
```

Type: struct [`thd_mdl_service_st`](plugin_api_service_thd_mdl.md#thd_mdl_service_st) *

Defined in service_thd_mdl.h:41

---

### thd_rnd_service

```cpp
struct thd_rnd_service_st * thd_rnd_service
```

Type: struct [`thd_rnd_service_st`](plugin_api_service_thd_rnd.md#thd_rnd_service_st) *

Defined in service_thd_rnd.h:49

---

### my_crypt_service

```cpp
struct my_crypt_service_st * my_crypt_service
```

Type: struct [`my_crypt_service_st`](plugin_api_service_my_crypt.md#my_crypt_service_st) *

Defined in service_my_crypt.h:86

---

### thd_wait_service

```cpp
struct thd_wait_service_st * thd_wait_service
```

Type: struct [`thd_wait_service_st`](plugin_api_service_thd_wait.md#thd_wait_service_st) *

Defined in service_thd_wait.h:75

---

### encryption_service

```cpp
struct encryption_service_st * encryption_service
```

Type: struct [`encryption_service_st`](plugin_api_service_encryption.md#encryption_service_st) *

Defined in service_encryption.h:78

---

### thd_alloc_service

```cpp
struct thd_alloc_service_st * thd_alloc_service
```

Type: struct [`thd_alloc_service_st`](plugin_api_service_thd_alloc.md#thd_alloc_service_st) *

Defined in service_thd_alloc.h:81

---

### debug_sync_service

```cpp
void(* debug_sync_service)(MYSQL_THD, const char *, size_t)
```

Defined in service_debug_sync.h:338

---

### my_snprintf_service

```cpp
struct my_snprintf_service_st * my_snprintf_service
```

Type: struct [`my_snprintf_service_st`](plugin_api_service_my_snprintf.md#my_snprintf_service_st) *

Defined in service_my_snprintf.h:55

---

### thd_autoinc_service

```cpp
struct thd_autoinc_service_st * thd_autoinc_service
```

Type: struct [`thd_autoinc_service_st`](plugin_api_service_thd_autoinc.md#thd_autoinc_service_st) *

Defined in service_thd_autoinc.h:46

---

### thd_log_warnings_service

```cpp
struct thd_log_warnings_service_st * thd_log_warnings_service
```

Type: struct [`thd_log_warnings_service_st`](plugin_api_service_log_warnings.md#thd_log_warnings_service_st) *

Defined in service_log_warnings.h:40

---

### thd_timezone_service

```cpp
struct thd_timezone_service_st * thd_timezone_service
```

Type: struct [`thd_timezone_service_st`](plugin_api_service_thd_timezone.md#thd_timezone_service_st) *

Defined in service_thd_timezone.h:63

---

### thd_specifics_service

```cpp
struct thd_specifics_service_st * thd_specifics_service
```

Type: struct [`thd_specifics_service_st`](plugin_api_service_thd_specifics.md#thd_specifics_service_st) *

Defined in service_thd_specifics.h:79

---

### thd_kill_statement_service

```cpp
struct kill_statement_service_st * thd_kill_statement_service
```

Type: struct [`kill_statement_service_st`](plugin_api_service_kill_statement.md#kill_statement_service_st) *

Defined in service_kill_statement.h:53

---

### my_print_error_service

```cpp
struct my_print_error_service_st * my_print_error_service
```

Type: struct [`my_print_error_service_st`](plugin_api_service_my_print_error.md#my_print_error_service_st) *

Defined in service_my_print_error.h:57

---

### progress_report_service

```cpp
struct progress_report_service_st * progress_report_service
```

Type: struct [`progress_report_service_st`](plugin_api_service_progress_report.md#progress_report_service_st) *

Defined in service_progress_report.h:58

---

### print_check_msg_service

```cpp
struct print_check_msg_service_st * print_check_msg_service
```

Type: struct [`print_check_msg_service_st`](plugin_api_service_print_check_msg.md#print_check_msg_service_st) *

Defined in service_print_check_msg.h:38

---

### encryption_scheme_service

```cpp
struct encryption_scheme_service_st * encryption_scheme_service
```

Type: struct [`encryption_scheme_service_st`](plugin_api_service_encryption_scheme.md#encryption_scheme_service_st) *

Defined in service_encryption_scheme.h:105

---

### thd_error_context_service

```cpp
struct thd_error_context_service_st * thd_error_context_service
```

Type: struct [`thd_error_context_service_st`](plugin_api_service_thd_error_context.md#thd_error_context_service_st) *

Defined in service_thd_error_context.h:51

Generated by [Moxygen](https://0state.com/moxygen)