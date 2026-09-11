---
description: >-
  Complete generated Plugin API reference, built from the MariaDB server headers by doxygen and moxygen.
---

# API Reference

## Groups

| Name | Description |
|------|-------------|
| [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface) |  |

## Classes

| Name | Description |
|------|-------------|
| [`opaque_THD`](#opaque_thd) |  |
| [`st_mysql_xid`](#st_mysql_xid) | struct [st_mysql_xid](#st_mysql_xid) is binary compatible with the XID structure as in the X/Open CAE Specification, Distributed Transaction Processing: The XA Specification, X/Open Company Ltd., 1991. [http://www.opengroup.org/bookstore/catalog/c193.htm](http://www.opengroup.org/bookstore/catalog/c193.htm) |
| [`st_mysql_auth`](#st_mysql_auth) | Server authentication plugin descriptor |
| [`st_plugin_vio`](#st_plugin_vio) | Provides plugin access to communication channel |
| [`sql_service_st`](#sql_service_st) |  |
| [`st_mysql_audit`](#st_mysql_audit) |  |
| [`st_mysql_value`](#st_mysql_value) |  |
| [`thd_service_st`](#thd_service_st) |  |
| [`json_service_st`](#json_service_st) |  |
| [`st_maria_plugin`](#st_maria_plugin) | MariaDB extension for plugins declaration structure. |
| [`st_mysql_daemon`](#st_mysql_daemon) |  |
| [`st_mysql_plugin`](#st_mysql_plugin) | Plugin description structure. |
| [`Mysql_replication`](#mysql_replication) | Replication plugin descriptor |
| [`wsrep_service_st`](#wsrep_service_st) |  |
| [`base64_service_st`](#base64_service_st) |  |
| [`logger_service_st`](#logger_service_st) |  |
| [`mysql_event_table`](#mysql_event_table) |  |
| [`st_mysql_ftparser`](#st_mysql_ftparser) |  |
| [`my_md5_service_st`](#my_md5_service_st) |  |
| [`st_mysql_show_var`](#st_mysql_show_var) |  |
| [`my_sha1_service_st`](#my_sha1_service_st) |  |
| [`my_sha2_service_st`](#my_sha2_service_st) |  |
| [`mysql_event_general`](#mysql_event_general) |  |
| [`st_plugin_vio_info`](#st_plugin_vio_info) |  |
| [`thd_mdl_service_st`](#thd_mdl_service_st) |  |
| [`thd_rnd_service_st`](#thd_rnd_service_st) |  |
| [`my_crypt_service_st`](#my_crypt_service_st) |  |
| [`st_encryption_scheme`](#st_encryption_scheme) |  |
| [`st_mysql_lex_string`](#st_mysql_lex_string) |  |
| [`thd_wait_service_st`](#thd_wait_service_st) |  |
| [`encryption_service_st`](#encryption_service_st) |  |
| [`st_mariadb_encryption`](#st_mariadb_encryption) | Encryption plugin descriptor |
| [`thd_alloc_service_st`](#thd_alloc_service_st) |  |
| [`mysql_event_connection`](#mysql_event_connection) |  |
| [`my_snprintf_service_st`](#my_snprintf_service_st) |  |
| [`st_mysql_client_plugin`](#st_mysql_client_plugin) |  |
| [`thd_autoinc_service_st`](#thd_autoinc_service_st) |  |
| [`st_mysql_ftparser_param`](#st_mysql_ftparser_param) |  |
| [`st_mysql_storage_engine`](#st_mysql_storage_engine) |  |
| [`thd_timezone_service_st`](#thd_timezone_service_st) |  |
| [`st_encryption_scheme_key`](#st_encryption_scheme_key) |  |
| [`thd_specifics_service_st`](#thd_specifics_service_st) |  |
| [`kill_statement_service_st`](#kill_statement_service_st) |  |
| [`my_print_error_service_st`](#my_print_error_service_st) |  |
| [`progress_report_service_st`](#progress_report_service_st) |  |
| [`st_mysql_const_lex_string`](#st_mysql_const_lex_string) |  |
| [`st_mysql_server_auth_info`](#st_mysql_server_auth_info) | Provides server plugin access to authentication information |
| [`print_check_msg_service_st`](#print_check_msg_service_st) |  |
| [`st_mysql_information_schema`](#st_mysql_information_schema) |  |
| [`encryption_scheme_service_st`](#encryption_scheme_service_st) |  |
| [`thd_log_warnings_service_st`](#thd_log_warnings_service_st) |  |
| [`thd_error_context_service_st`](#thd_error_context_service_st) |  |
| [`st_mariadb_password_validation`](#st_mariadb_password_validation) | Password validation plugin descriptor |
| [`st_mysql_ftparser_boolean_info`](#st_mysql_ftparser_boolean_info) |  |
| [`st_mysql_client_plugin_AUTHENTICATION`](#st_mysql_client_plugin_authentication) |  |

## Macros

---

{#psi_likely}

### psi_likely

```cpp
#define psi_likely(A) unlikely(A)
```

Defined in psi/psi.h:47

---

{#psi_unlikely}

### psi_unlikely

```cpp
#define psi_unlikely(A) likely(A)
```

Defined in psi/psi.h:48

---

{#psi_schema_name_len}

### PSI_SCHEMA_NAME_LEN

```cpp
#define PSI_SCHEMA_NAME_LEN (64 * 3)
```

Defined in psi/psi.h:1198

---

{#psi_dynamic_call}

### PSI_DYNAMIC_CALL

```cpp
#define PSI_DYNAMIC_CALL(M, M) PSI_server->M
```

Defined in psi/psi.h:3028

---

{#mysql_dllexport}

### MYSQL_DLLEXPORT

```cpp
#define MYSQL_DLLEXPORT
```

Defined in plugin.h:39

---

{#mysql_plugin_export}

### MYSQL_PLUGIN_EXPORT

```cpp
#define MYSQL_PLUGIN_EXPORT MYSQL_DLLEXPORT
```

Defined in plugin.h:45

---

{#mysql_xiddatasize}

### MYSQL_XIDDATASIZE

```cpp
#define MYSQL_XIDDATASIZE 128
```

Defined in plugin.h:62

---

{#mysql_plugin_interface_version}

### MYSQL_PLUGIN_INTERFACE_VERSION

```cpp
#define MYSQL_PLUGIN_INTERFACE_VERSION 0x0105
```

Defined in plugin.h:84

MySQL plugin interface version

---

{#maria_plugin_interface_version}

### MARIA_PLUGIN_INTERFACE_VERSION

```cpp
#define MARIA_PLUGIN_INTERFACE_VERSION 0x0110
```

Defined in plugin.h:87

MariaDB plugin interface version

---

{#mysql_udf_plugin}

### MYSQL_UDF_PLUGIN

```cpp
#define MYSQL_UDF_PLUGIN 0
```

Defined in plugin.h:92

not implemented <br/>

---

{#mysql_storage_engine_plugin}

### MYSQL_STORAGE_ENGINE_PLUGIN

```cpp
#define MYSQL_STORAGE_ENGINE_PLUGIN 1
```

Defined in plugin.h:93

---

{#mysql_ftparser_plugin}

### MYSQL_FTPARSER_PLUGIN

```cpp
#define MYSQL_FTPARSER_PLUGIN 2
```

Defined in plugin.h:94

Full-text parser plugin <br/>

---

{#mysql_daemon_plugin}

### MYSQL_DAEMON_PLUGIN

```cpp
#define MYSQL_DAEMON_PLUGIN 3
```

Defined in plugin.h:95

---

{#mysql_information_schema_plugin}

### MYSQL_INFORMATION_SCHEMA_PLUGIN

```cpp
#define MYSQL_INFORMATION_SCHEMA_PLUGIN 4
```

Defined in plugin.h:96

---

{#mysql_audit_plugin}

### MYSQL_AUDIT_PLUGIN

```cpp
#define MYSQL_AUDIT_PLUGIN 5
```

Defined in plugin.h:97

---

{#mysql_replication_plugin}

### MYSQL_REPLICATION_PLUGIN

```cpp
#define MYSQL_REPLICATION_PLUGIN 6
```

Defined in plugin.h:98

---

{#mysql_authentication_plugin}

### MYSQL_AUTHENTICATION_PLUGIN

```cpp
#define MYSQL_AUTHENTICATION_PLUGIN 7
```

Defined in plugin.h:99

---

{#mysql_max_plugin_type_num}

### MYSQL_MAX_PLUGIN_TYPE_NUM

```cpp
#define MYSQL_MAX_PLUGIN_TYPE_NUM 12
```

Defined in plugin.h:100

The number of plugin types

---

{#mariadb_password_validation_plugin}

### MariaDB_PASSWORD_VALIDATION_PLUGIN

```cpp
#define MariaDB_PASSWORD_VALIDATION_PLUGIN 8
```

Defined in plugin.h:104

Client and server password validation Encryption and key management plugins

---

{#mariadb_encryption_plugin}

### MariaDB_ENCRYPTION_PLUGIN

```cpp
#define MariaDB_ENCRYPTION_PLUGIN 9
```

Defined in plugin.h:106

Plugins for SQL data storage types

---

{#mariadb_data_type_plugin}

### MariaDB_DATA_TYPE_PLUGIN

```cpp
#define MariaDB_DATA_TYPE_PLUGIN 10
```

Defined in plugin.h:108

Plugins for new native SQL functions

---

{#mariadb_function_plugin}

### MariaDB_FUNCTION_PLUGIN

```cpp
#define MariaDB_FUNCTION_PLUGIN 11
```

Defined in plugin.h:110

---

{#plugin_license_proprietary}

### PLUGIN_LICENSE_PROPRIETARY

```cpp
#define PLUGIN_LICENSE_PROPRIETARY 0
```

Defined in plugin.h:113

---

{#plugin_license_gpl}

### PLUGIN_LICENSE_GPL

```cpp
#define PLUGIN_LICENSE_GPL 1
```

Defined in plugin.h:114

---

{#plugin_license_bsd}

### PLUGIN_LICENSE_BSD

```cpp
#define PLUGIN_LICENSE_BSD 2
```

Defined in plugin.h:115

---

{#plugin_license_proprietary_string}

### PLUGIN_LICENSE_PROPRIETARY_STRING

```cpp
#define PLUGIN_LICENSE_PROPRIETARY_STRING "PROPRIETARY"
```

Defined in plugin.h:117

---

{#plugin_license_gpl_string}

### PLUGIN_LICENSE_GPL_STRING

```cpp
#define PLUGIN_LICENSE_GPL_STRING "GPL"
```

Defined in plugin.h:118

---

{#plugin_license_bsd_string}

### PLUGIN_LICENSE_BSD_STRING

```cpp
#define PLUGIN_LICENSE_BSD_STRING "BSD"
```

Defined in plugin.h:119

---

{#mariadb_plugin_maturity_unknown}

### MariaDB_PLUGIN_MATURITY_UNKNOWN

```cpp
#define MariaDB_PLUGIN_MATURITY_UNKNOWN 0
```

Defined in plugin.h:122

---

{#mariadb_plugin_maturity_experimental}

### MariaDB_PLUGIN_MATURITY_EXPERIMENTAL

```cpp
#define MariaDB_PLUGIN_MATURITY_EXPERIMENTAL 1
```

Defined in plugin.h:123

---

{#mariadb_plugin_maturity_alpha}

### MariaDB_PLUGIN_MATURITY_ALPHA

```cpp
#define MariaDB_PLUGIN_MATURITY_ALPHA 2
```

Defined in plugin.h:124

---

{#mariadb_plugin_maturity_beta}

### MariaDB_PLUGIN_MATURITY_BETA

```cpp
#define MariaDB_PLUGIN_MATURITY_BETA 3
```

Defined in plugin.h:125

---

{#mariadb_plugin_maturity_gamma}

### MariaDB_PLUGIN_MATURITY_GAMMA

```cpp
#define MariaDB_PLUGIN_MATURITY_GAMMA 4
```

Defined in plugin.h:126

---

{#mariadb_plugin_maturity_stable}

### MariaDB_PLUGIN_MATURITY_STABLE

```cpp
#define MariaDB_PLUGIN_MATURITY_STABLE 5
```

Defined in plugin.h:127

---

{#__mysql_declare_plugin}

### __MYSQL_DECLARE_PLUGIN

```cpp
#define __MYSQL_DECLARE_PLUGIN(NAME, VERSION, PSIZE, DECLS) int VERSION= MYSQL_PLUGIN_INTERFACE_VERSION;                                  \
int PSIZE= sizeof(struct st_mysql_plugin);                                    \
struct st_mysql_plugin DECLS[]= {
```

Defined in plugin.h:137

---

{#maria_declare_plugin__}

### MARIA_DECLARE_PLUGIN__

```cpp
#define MARIA_DECLARE_PLUGIN__(NAME, VERSION, PSIZE, DECLS) MYSQL_PLUGIN_EXPORT int VERSION;                                              \
int VERSION= MARIA_PLUGIN_INTERFACE_VERSION;                                  \
MYSQL_PLUGIN_EXPORT int PSIZE;                                                \
int PSIZE= sizeof(struct st_maria_plugin);                                    \
MYSQL_PLUGIN_EXPORT struct st_maria_plugin DECLS[];                           \
struct st_maria_plugin DECLS[]= {
```

Defined in plugin.h:142

---

{#mysql_declare_plugin}

### mysql_declare_plugin

```cpp
#define mysql_declare_plugin(NAME) __MYSQL_DECLARE_PLUGIN(NAME, \
                 builtin_ ## NAME ## _plugin_interface_version, \
                 builtin_ ## NAME ## _sizeof_struct_st_plugin, \
                 builtin_ ## NAME ## _plugin)
```

Defined in plugin.h:169

---

{#maria_declare_plugin}

### maria_declare_plugin

```cpp
#define maria_declare_plugin(NAME) MARIA_DECLARE_PLUGIN__(NAME, \
                 builtin_maria_ ## NAME ## _plugin_interface_version, \
                 builtin_maria_ ## NAME ## _sizeof_struct_st_plugin, \
                 builtin_maria_ ## NAME ## _plugin)
```

Defined in plugin.h:175

---

{#mysql_declare_plugin_end}

### mysql_declare_plugin_end

```cpp
#define mysql_declare_plugin_end ,{0,0,0,0,0,0,0,0,0,0,0,0,0}}
```

Defined in plugin.h:181

---

{#maria_declare_plugin_end}

### maria_declare_plugin_end

```cpp
#define maria_declare_plugin_end ,{0,0,0,0,0,0,0,0,0,0,0,0,0}}
```

Defined in plugin.h:182

---

{#show_int}

### SHOW_INT

```cpp
#define SHOW_INT SHOW_UINT
```

Defined in plugin.h:197

---

{#show_long}

### SHOW_LONG

```cpp
#define SHOW_LONG SHOW_ULONG
```

Defined in plugin.h:198

---

{#show_longlong}

### SHOW_LONGLONG

```cpp
#define SHOW_LONGLONG SHOW_ULONGLONG
```

Defined in plugin.h:199

---

{#show_var_func_buff_size}

### SHOW_VAR_FUNC_BUFF_SIZE

```cpp
#define SHOW_VAR_FUNC_BUFF_SIZE (256 * sizeof(void*))
```

Defined in plugin.h:214

---

{#plugin_opt_no_install}

### PLUGIN_OPT_NO_INSTALL

```cpp
#define PLUGIN_OPT_NO_INSTALL 1UL
```

Defined in plugin.h:234

Not dynamically loadable

---

{#plugin_opt_no_uninstall}

### PLUGIN_OPT_NO_UNINSTALL

```cpp
#define PLUGIN_OPT_NO_UNINSTALL 2UL
```

Defined in plugin.h:235

Not dynamically unloadable

---

{#plugin_var_bool}

### PLUGIN_VAR_BOOL

```cpp
#define PLUGIN_VAR_BOOL 0x0001
```

Defined in plugin.h:243

---

{#plugin_var_int}

### PLUGIN_VAR_INT

```cpp
#define PLUGIN_VAR_INT 0x0002
```

Defined in plugin.h:244

---

{#plugin_var_long}

### PLUGIN_VAR_LONG

```cpp
#define PLUGIN_VAR_LONG 0x0003
```

Defined in plugin.h:245

---

{#plugin_var_longlong}

### PLUGIN_VAR_LONGLONG

```cpp
#define PLUGIN_VAR_LONGLONG 0x0004
```

Defined in plugin.h:246

---

{#plugin_var_str}

### PLUGIN_VAR_STR

```cpp
#define PLUGIN_VAR_STR 0x0005
```

Defined in plugin.h:247

---

{#plugin_var_enum}

### PLUGIN_VAR_ENUM

```cpp
#define PLUGIN_VAR_ENUM 0x0006
```

Defined in plugin.h:248

---

{#plugin_var_set}

### PLUGIN_VAR_SET

```cpp
#define PLUGIN_VAR_SET 0x0007
```

Defined in plugin.h:249

---

{#plugin_var_double}

### PLUGIN_VAR_DOUBLE

```cpp
#define PLUGIN_VAR_DOUBLE 0x0008
```

Defined in plugin.h:250

---

{#plugin_var_unsigned}

### PLUGIN_VAR_UNSIGNED

```cpp
#define PLUGIN_VAR_UNSIGNED 0x0080
```

Defined in plugin.h:251

---

{#plugin_var_thdlocal}

### PLUGIN_VAR_THDLOCAL

```cpp
#define PLUGIN_VAR_THDLOCAL 0x0100
```

Defined in plugin.h:252

Variable is per-connection

---

{#plugin_var_readonly}

### PLUGIN_VAR_READONLY

```cpp
#define PLUGIN_VAR_READONLY 0x0200
```

Defined in plugin.h:253

Server variable is read only

---

{#plugin_var_nosysvar}

### PLUGIN_VAR_NOSYSVAR

```cpp
#define PLUGIN_VAR_NOSYSVAR 0x0400
```

Defined in plugin.h:254

Not a server variable

---

{#plugin_var_nocmdopt}

### PLUGIN_VAR_NOCMDOPT

```cpp
#define PLUGIN_VAR_NOCMDOPT 0x0800
```

Defined in plugin.h:255

Not a command line option

---

{#plugin_var_nocmdarg}

### PLUGIN_VAR_NOCMDARG

```cpp
#define PLUGIN_VAR_NOCMDARG 0x1000
```

Defined in plugin.h:256

No argument for cmd line

---

{#plugin_var_rqcmdarg}

### PLUGIN_VAR_RQCMDARG

```cpp
#define PLUGIN_VAR_RQCMDARG 0x0000
```

Defined in plugin.h:257

Argument required for cmd line

---

{#plugin_var_opcmdarg}

### PLUGIN_VAR_OPCMDARG

```cpp
#define PLUGIN_VAR_OPCMDARG 0x2000
```

Defined in plugin.h:258

Argument optional for cmd line

---

{#plugin_var_deprecated}

### PLUGIN_VAR_DEPRECATED

```cpp
#define PLUGIN_VAR_DEPRECATED 0x4000
```

Defined in plugin.h:259

Server variable is deprecated

---

{#plugin_var_memalloc}

### PLUGIN_VAR_MEMALLOC

```cpp
#define PLUGIN_VAR_MEMALLOC 0x8000
```

Defined in plugin.h:260

String needs memory allocated

---

{#plugin_var_mask}

### PLUGIN_VAR_MASK

```cpp
#define PLUGIN_VAR_MASK (PLUGIN_VAR_READONLY | PLUGIN_VAR_NOSYSVAR | \
         PLUGIN_VAR_NOCMDOPT | PLUGIN_VAR_NOCMDARG | \
         PLUGIN_VAR_OPCMDARG | PLUGIN_VAR_RQCMDARG | \
         PLUGIN_VAR_DEPRECATED | PLUGIN_VAR_MEMALLOC)
```

Defined in plugin.h:310

---

{#mysql_plugin_var_header}

### MYSQL_PLUGIN_VAR_HEADER

```cpp
#define MYSQL_PLUGIN_VAR_HEADER int flags;                    \
  const char *name;             \
  const char *comment;          \
  mysql_var_check_func check;   \
  mysql_var_update_func update
```

Defined in plugin.h:316

---

{#mysql_sysvar_name}

### MYSQL_SYSVAR_NAME

```cpp
#define MYSQL_SYSVAR_NAME(name) mysql_sysvar_ ## name
```

Defined in plugin.h:323

---

{#mysql_sysvar}

### MYSQL_SYSVAR

```cpp
#define MYSQL_SYSVAR(name) ((struct st_mysql_sys_var *)&(MYSQL_SYSVAR_NAME(name)))
```

Defined in plugin.h:324

---

{#declare_mysql_sysvar_basic}

### DECLARE_MYSQL_SYSVAR_BASIC

```cpp
#define DECLARE_MYSQL_SYSVAR_BASIC(name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  type *value;                  \
  const type def_val;                 \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:335

---

{#declare_mysql_sysvar_const_basic}

### DECLARE_MYSQL_SYSVAR_CONST_BASIC

```cpp
#define DECLARE_MYSQL_SYSVAR_CONST_BASIC(name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  const type *value;                  \
  const type def_val;                 \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:341

---

{#declare_mysql_sysvar_simple}

### DECLARE_MYSQL_SYSVAR_SIMPLE

```cpp
#define DECLARE_MYSQL_SYSVAR_SIMPLE(name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  type *value; type def_val;    \
  type min_val; type max_val;   \
  type blk_sz;                  \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:347

---

{#declare_mysql_sysvar_typelib}

### DECLARE_MYSQL_SYSVAR_TYPELIB

```cpp
#define DECLARE_MYSQL_SYSVAR_TYPELIB(name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  type *value; type def_val;    \
  TYPELIB *typelib;             \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:354

---

{#declare_thdvar_func}

### DECLARE_THDVAR_FUNC

```cpp
#define DECLARE_THDVAR_FUNC(type) type *(*resolve)(MYSQL_THD thd, int offset)
```

Defined in plugin.h:360

---

{#declare_mysql_thdvar_basic}

### DECLARE_MYSQL_THDVAR_BASIC

```cpp
#define DECLARE_MYSQL_THDVAR_BASIC(name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  int offset;                   \
  const type def_val;           \
  DECLARE_THDVAR_FUNC(type);    \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:363

---

{#declare_mysql_thdvar_simple}

### DECLARE_MYSQL_THDVAR_SIMPLE

```cpp
#define DECLARE_MYSQL_THDVAR_SIMPLE(name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  int offset;                   \
  type def_val; type min_val;   \
  type max_val; type blk_sz;    \
  DECLARE_THDVAR_FUNC(type);    \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:370

---

{#declare_mysql_thdvar_typelib}

### DECLARE_MYSQL_THDVAR_TYPELIB

```cpp
#define DECLARE_MYSQL_THDVAR_TYPELIB(name, type) struct { \
  MYSQL_PLUGIN_VAR_HEADER;      \
  int offset;                   \
  const type def_val;           \
  DECLARE_THDVAR_FUNC(type);    \
  TYPELIB *typelib;             \
} MYSQL_SYSVAR_NAME(name)
```

Defined in plugin.h:378

---

{#mysql_sysvar_bool}

### MYSQL_SYSVAR_BOOL

```cpp
#define MYSQL_SYSVAR_BOOL(name, varname, opt, comment, check, update, def) DECLARE_MYSQL_SYSVAR_BASIC(name, char) = { \
  PLUGIN_VAR_BOOL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def}
```

Defined in plugin.h:391

---

{#mysql_sysvar_str}

### MYSQL_SYSVAR_STR

```cpp
#define MYSQL_SYSVAR_STR(name, varname, opt, comment, check, update, def) DECLARE_MYSQL_SYSVAR_BASIC(name, char *) = { \
  PLUGIN_VAR_STR | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def}
```

Defined in plugin.h:396

---

{#mysql_sysvar_const_str}

### MYSQL_SYSVAR_CONST_STR

```cpp
#define MYSQL_SYSVAR_CONST_STR(name, varname, opt, comment, check, update, def) DECLARE_MYSQL_SYSVAR_CONST_BASIC(name, char *) = { \
  PLUGIN_VAR_STR | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def}
```

Defined in plugin.h:401

---

{#mysql_sysvar_int}

### MYSQL_SYSVAR_INT

```cpp
#define MYSQL_SYSVAR_INT(name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, int) = { \
  PLUGIN_VAR_INT | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:406

---

{#mysql_sysvar_uint}

### MYSQL_SYSVAR_UINT

```cpp
#define MYSQL_SYSVAR_UINT(name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, unsigned int) = { \
  PLUGIN_VAR_INT | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:411

---

{#mysql_sysvar_long}

### MYSQL_SYSVAR_LONG

```cpp
#define MYSQL_SYSVAR_LONG(name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, long) = { \
  PLUGIN_VAR_LONG | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:416

---

{#mysql_sysvar_ulong}

### MYSQL_SYSVAR_ULONG

```cpp
#define MYSQL_SYSVAR_ULONG(name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, unsigned long) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:421

---

{#mysql_sysvar_longlong}

### MYSQL_SYSVAR_LONGLONG

```cpp
#define MYSQL_SYSVAR_LONGLONG(name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, long long) = { \
  PLUGIN_VAR_LONGLONG | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:426

---

{#mysql_sysvar_ulonglong}

### MYSQL_SYSVAR_ULONGLONG

```cpp
#define MYSQL_SYSVAR_ULONGLONG(name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, unsigned long long) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:431

---

{#mysql_sysvar_uint64_t}

### MYSQL_SYSVAR_UINT64_T

```cpp
#define MYSQL_SYSVAR_UINT64_T(name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, uint64_t) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:436

---

{#mysql_sysvar_size_t}

### MYSQL_SYSVAR_SIZE_T

```cpp
#define MYSQL_SYSVAR_SIZE_T(name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, size_t) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:447

---

{#mysql_sysvar_enum}

### MYSQL_SYSVAR_ENUM

```cpp
#define MYSQL_SYSVAR_ENUM(name, varname, opt, comment, check, update, def, typelib) DECLARE_MYSQL_SYSVAR_TYPELIB(name, unsigned long) = { \
  PLUGIN_VAR_ENUM | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, typelib }
```

Defined in plugin.h:453

---

{#mysql_sysvar_set}

### MYSQL_SYSVAR_SET

```cpp
#define MYSQL_SYSVAR_SET(name, varname, opt, comment, check, update, def, typelib) DECLARE_MYSQL_SYSVAR_TYPELIB(name, unsigned long long) = { \
  PLUGIN_VAR_SET | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, typelib }
```

Defined in plugin.h:458

---

{#mysql_sysvar_double}

### MYSQL_SYSVAR_DOUBLE

```cpp
#define MYSQL_SYSVAR_DOUBLE(name, varname, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_SYSVAR_SIMPLE(name, double) = { \
  PLUGIN_VAR_DOUBLE | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, &varname, def, min, max, blk }
```

Defined in plugin.h:463

---

{#mysql_thdvar_bool}

### MYSQL_THDVAR_BOOL

```cpp
#define MYSQL_THDVAR_BOOL(name, opt, comment, check, update, def) DECLARE_MYSQL_THDVAR_BASIC(name, char) = { \
  PLUGIN_VAR_BOOL | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, NULL}
```

Defined in plugin.h:468

---

{#mysql_thdvar_str}

### MYSQL_THDVAR_STR

```cpp
#define MYSQL_THDVAR_STR(name, opt, comment, check, update, def) DECLARE_MYSQL_THDVAR_BASIC(name, char *) = { \
  PLUGIN_VAR_STR | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, NULL}
```

Defined in plugin.h:473

---

{#mysql_thdvar_int}

### MYSQL_THDVAR_INT

```cpp
#define MYSQL_THDVAR_INT(name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, int) = { \
  PLUGIN_VAR_INT | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:478

---

{#mysql_thdvar_uint}

### MYSQL_THDVAR_UINT

```cpp
#define MYSQL_THDVAR_UINT(name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, unsigned int) = { \
  PLUGIN_VAR_INT | PLUGIN_VAR_THDLOCAL | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:483

---

{#mysql_thdvar_long}

### MYSQL_THDVAR_LONG

```cpp
#define MYSQL_THDVAR_LONG(name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, long) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:488

---

{#mysql_thdvar_ulong}

### MYSQL_THDVAR_ULONG

```cpp
#define MYSQL_THDVAR_ULONG(name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, unsigned long) = { \
  PLUGIN_VAR_LONG | PLUGIN_VAR_THDLOCAL | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:493

---

{#mysql_thdvar_longlong}

### MYSQL_THDVAR_LONGLONG

```cpp
#define MYSQL_THDVAR_LONGLONG(name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, long long) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:498

---

{#mysql_thdvar_ulonglong}

### MYSQL_THDVAR_ULONGLONG

```cpp
#define MYSQL_THDVAR_ULONGLONG(name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, unsigned long long) = { \
  PLUGIN_VAR_LONGLONG | PLUGIN_VAR_THDLOCAL | PLUGIN_VAR_UNSIGNED | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:503

---

{#mysql_thdvar_enum}

### MYSQL_THDVAR_ENUM

```cpp
#define MYSQL_THDVAR_ENUM(name, opt, comment, check, update, def, typelib) DECLARE_MYSQL_THDVAR_TYPELIB(name, unsigned long) = { \
  PLUGIN_VAR_ENUM | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, NULL, typelib }
```

Defined in plugin.h:508

---

{#mysql_thdvar_set}

### MYSQL_THDVAR_SET

```cpp
#define MYSQL_THDVAR_SET(name, opt, comment, check, update, def, typelib) DECLARE_MYSQL_THDVAR_TYPELIB(name, unsigned long long) = { \
  PLUGIN_VAR_SET | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, NULL, typelib }
```

Defined in plugin.h:513

---

{#mysql_thdvar_double}

### MYSQL_THDVAR_DOUBLE

```cpp
#define MYSQL_THDVAR_DOUBLE(name, opt, comment, check, update, def, min, max, blk) DECLARE_MYSQL_THDVAR_SIMPLE(name, double) = { \
  PLUGIN_VAR_DOUBLE | PLUGIN_VAR_THDLOCAL | ((opt) & PLUGIN_VAR_MASK), \
  #name, comment, check, update, -1, def, min, max, blk, NULL }
```

Defined in plugin.h:518

---

{#sysvar}

### SYSVAR

```cpp
#define SYSVAR(name) (*(MYSQL_SYSVAR_NAME(name).value))
```

Defined in plugin.h:525

---

{#thdvar}

### THDVAR

```cpp
#define THDVAR(thd, name) (*(MYSQL_SYSVAR_NAME(name).resolve(thd, MYSQL_SYSVAR_NAME(name).offset)))
```

Defined in plugin.h:529

---

{#mysql_daemon_interface_version}

### MYSQL_DAEMON_INTERFACE_VERSION

```cpp
#define MYSQL_DAEMON_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:600

---

{#mysql_information_schema_interface_version}

### MYSQL_INFORMATION_SCHEMA_INTERFACE_VERSION

```cpp
#define MYSQL_INFORMATION_SCHEMA_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:618

---

{#mysql_handlerton_interface_version}

### MYSQL_HANDLERTON_INTERFACE_VERSION

```cpp
#define MYSQL_HANDLERTON_INTERFACE_VERSION (MYSQL_VERSION_ID << 8)
```

Defined in plugin.h:636

---

{#mysql_replication_interface_version}

### MYSQL_REPLICATION_INTERFACE_VERSION

```cpp
#define MYSQL_REPLICATION_INTERFACE_VERSION 0x0200
```

Defined in plugin.h:655

---

{#mysql_value_type_string}

### MYSQL_VALUE_TYPE_STRING

```cpp
#define MYSQL_VALUE_TYPE_STRING 0
```

Defined in plugin.h:664

---

{#mysql_value_type_real}

### MYSQL_VALUE_TYPE_REAL

```cpp
#define MYSQL_VALUE_TYPE_REAL 1
```

Defined in plugin.h:665

---

{#mysql_value_type_int}

### MYSQL_VALUE_TYPE_INT

```cpp
#define MYSQL_VALUE_TYPE_INT 2
```

Defined in plugin.h:666

---

{#mysql_services_included}

### MYSQL_SERVICES_INCLUDED

```cpp
#define MYSQL_SERVICES_INCLUDED
```

Defined in services.h:51

---

{#psi_ps_call}

### PSI_PS_CALL

```cpp
#define PSI_PS_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_ps.h:34

---

{#mysql_create_ps}

### MYSQL_CREATE_PS

```cpp
#define MYSQL_CREATE_PS(IDENTITY, ID, LOCKER, NAME, NAME_LENGTH) NULL
```

Defined in psi/mysql_ps.h:49

---

{#mysql_execute_ps}

### MYSQL_EXECUTE_PS

```cpp
#define MYSQL_EXECUTE_PS(LOCKER, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql_ps.h:51

---

{#mysql_destroy_ps}

### MYSQL_DESTROY_PS

```cpp
#define MYSQL_DESTROY_PS(PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql_ps.h:53

---

{#mysql_reprepare_ps}

### MYSQL_REPREPARE_PS

```cpp
#define MYSQL_REPREPARE_PS(PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql_ps.h:55

---

{#mysql_set_ps_text}

### MYSQL_SET_PS_TEXT

```cpp
#define MYSQL_SET_PS_TEXT(PREPARED_STMT, SQLTEXT, SQLTEXT_LENGTH) do {} while (0)
```

Defined in psi/mysql_ps.h:57

---

{#psi_sp_call}

### PSI_SP_CALL

```cpp
#define PSI_SP_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_sp.h:34

---

{#mysql_start_sp}

### MYSQL_START_SP

```cpp
#define MYSQL_START_SP(STATE, SP_SHARE) NULL
```

Defined in psi/mysql_sp.h:41

---

{#mysql_end_sp}

### MYSQL_END_SP

```cpp
#define MYSQL_END_SP(LOCKER) do {} while (0)
```

Defined in psi/mysql_sp.h:50

---

{#mysql_drop_sp}

### MYSQL_DROP_SP

```cpp
#define MYSQL_DROP_SP(OT, SN, SNL, ON, ONL) do {} while (0)
```

Defined in psi/mysql_sp.h:58

---

{#mysql_get_sp_share}

### MYSQL_GET_SP_SHARE

```cpp
#define MYSQL_GET_SP_SHARE(OT, SN, SNL, ON, ONL) NULL
```

Defined in psi/mysql_sp.h:66

---

{#psi_instrument_me}

### PSI_INSTRUMENT_ME

```cpp
#define PSI_INSTRUMENT_ME 0
```

Defined in psi/psi_base.h:47

---

{#psi_instrument_mem}

### PSI_INSTRUMENT_MEM

```cpp
#define PSI_INSTRUMENT_MEM ((PSI_memory_key)0)
```

Defined in psi/psi_base.h:48

---

{#psi_not_instrumented}

### PSI_NOT_INSTRUMENTED

```cpp
#define PSI_NOT_INSTRUMENTED 0
```

Defined in psi/psi_base.h:50

---

{#psi_flag_global}

### PSI_FLAG_GLOBAL

```cpp
#define PSI_FLAG_GLOBAL (1 << 0)
```

Defined in psi/psi_base.h:57

Global flag. This flag indicate that an instrumentation point is a global variable, or a singleton.

---

{#psi_flag_mutable}

### PSI_FLAG_MUTABLE

```cpp
#define PSI_FLAG_MUTABLE (1 << 1)
```

Defined in psi/psi_base.h:64

Mutable flag. This flag indicate that an instrumentation point is a general placeholder, that can mutate into a more specific instrumentation point.

---

{#psi_flag_thread}

### PSI_FLAG_THREAD

```cpp
#define PSI_FLAG_THREAD (1 << 2)
```

Defined in psi/psi_base.h:66

---

{#psi_flag_stage_progress}

### PSI_FLAG_STAGE_PROGRESS

```cpp
#define PSI_FLAG_STAGE_PROGRESS (1 << 3)
```

Defined in psi/psi_base.h:73

Stage progress flag. This flag apply to the stage instruments only. It indicates the instrumentation provides progress data.

---

{#psi_rwlock_flag_sx}

### PSI_RWLOCK_FLAG_SX

```cpp
#define PSI_RWLOCK_FLAG_SX (1 << 4)
```

Defined in psi/psi_base.h:79

Shared Exclusive flag. Indicates that rwlock support the shared exclusive state.

---

{#psi_flag_transfer}

### PSI_FLAG_TRANSFER

```cpp
#define PSI_FLAG_TRANSFER (1 << 5)
```

Defined in psi/psi_base.h:86

Transferable flag. This flag indicate that an instrumented object can be created by a thread and destroyed by another thread.

---

{#psi_flag_volatility_session}

### PSI_FLAG_VOLATILITY_SESSION

```cpp
#define PSI_FLAG_VOLATILITY_SESSION (1 << 6)
```

Defined in psi/psi_base.h:94

Volatility flag. This flag indicate that an instrumented object has a volatility (life cycle) comparable to the volatility of a session.

---

{#psi_flag_thread_system}

### PSI_FLAG_THREAD_SYSTEM

```cpp
#define PSI_FLAG_THREAD_SYSTEM (1 << 9)
```

Defined in psi/psi_base.h:100

System thread flag. Indicates that the instrumented object exists on a system thread.

---

{#psi_call_start_metadata_wait}

### PSI_CALL_start_metadata_wait

```cpp
#define PSI_CALL_start_metadata_wait(A, B, C, D) 0
```

Defined in psi/mysql_mdl.h:45

---

{#psi_call_end_metadata_wait}

### PSI_CALL_end_metadata_wait

```cpp
#define PSI_CALL_end_metadata_wait(A, B) do { } while(0)
```

Defined in psi/mysql_mdl.h:46

---

{#psi_call_create_metadata_lock}

### PSI_CALL_create_metadata_lock

```cpp
#define PSI_CALL_create_metadata_lock(A, B, C, D, E, F, G) 0
```

Defined in psi/mysql_mdl.h:47

---

{#psi_call_set_metadata_lock_status}

### PSI_CALL_set_metadata_lock_status

```cpp
#define PSI_CALL_set_metadata_lock_status(A, B) do {} while(0)
```

Defined in psi/mysql_mdl.h:48

---

{#psi_call_destroy_metadata_lock}

### PSI_CALL_destroy_metadata_lock

```cpp
#define PSI_CALL_destroy_metadata_lock(A) do {} while(0)
```

Defined in psi/mysql_mdl.h:49

---

{#mysql_mdl_create}

### mysql_mdl_create

```cpp
#define mysql_mdl_create(I, K, T, D, S, F, L, I, K, T, D, S, F, L) NULL
```

Defined in psi/mysql_mdl.h:74

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

{#mysql_mdl_set_status}

### mysql_mdl_set_status

```cpp
#define mysql_mdl_set_status(L, S, L, S) do {} while (0)
```

Defined in psi/mysql_mdl.h:81

---

{#mysql_mdl_destroy}

### mysql_mdl_destroy

```cpp
#define mysql_mdl_destroy(M, M) do {} while (0)
```

Defined in psi/mysql_mdl.h:95

Instrumented metadata lock destruction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `M` |  | Metadata lock |
| `M` |  | Metadata lock |

---

{#psi_file_call}

### PSI_FILE_CALL

```cpp
#define PSI_FILE_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_file.h:52

---

{#mysql_file_register}

### mysql_file_register

```cpp
#define mysql_file_register(P1, P2, P3, P1, P2, P3) inline_mysql_file_register(P1, P2, P3)
```

Defined in psi/mysql_file.h:65

File registration.

---

{#mysql_file_fgets}

### mysql_file_fgets

```cpp
#define mysql_file_fgets(P1, P2, F, P1, P2, F) inline_mysql_file_fgets(P1, P2, F)
```

Defined in psi/mysql_file.h:77

Instrumented fgets. `mysql_file_fgets` is a replacement for `fgets`.

---

{#mysql_file_fgetc}

### mysql_file_fgetc

```cpp
#define mysql_file_fgetc(F, F) inline_mysql_file_fgetc(F)
```

Defined in psi/mysql_file.h:89

Instrumented fgetc. `mysql_file_fgetc` is a replacement for `fgetc`.

---

{#mysql_file_fputs}

### mysql_file_fputs

```cpp
#define mysql_file_fputs(P1, F, P1, F) inline_mysql_file_fputs(P1, F)
```

Defined in psi/mysql_file.h:101

Instrumented fputs. `mysql_file_fputs` is a replacement for `fputs`.

---

{#mysql_file_fputc}

### mysql_file_fputc

```cpp
#define mysql_file_fputc(P1, F, P1, F) inline_mysql_file_fputc(P1, F)
```

Defined in psi/mysql_file.h:114

Instrumented fputc. `mysql_file_fputc` is a replacement for `fputc`.

---

{#mysql_file_fprintf}

### mysql_file_fprintf

```cpp
#define mysql_file_fprintf inline_mysql_file_fprintf
```

Defined in psi/mysql_file.h:123

Instrumented fprintf. `mysql_file_fprintf` is a replacement for `fprintf`.

---

{#mysql_file_vfprintf}

### mysql_file_vfprintf

```cpp
#define mysql_file_vfprintf(F, P1, P2, F, P1, P2) inline_mysql_file_vfprintf(F, P1, P2)
```

Defined in psi/mysql_file.h:134

Instrumented vfprintf. `mysql_file_vfprintf` is a replacement for `vfprintf`.

---

{#mysql_file_fflush}

### mysql_file_fflush

```cpp
#define mysql_file_fflush(F, F) inline_mysql_file_fflush(F)
```

Defined in psi/mysql_file.h:147

Instrumented fflush. `mysql_file_fflush` is a replacement for `fflush`.

---

{#mysql_file_feof}

### mysql_file_feof

```cpp
#define mysql_file_feof(F, F) inline_mysql_file_feof(F)
```

Defined in psi/mysql_file.h:156

Instrumented feof. `mysql_file_feof` is a replacement for `feof`.

---

{#mysql_file_fstat}

### mysql_file_fstat

```cpp
#define mysql_file_fstat(FN, S, FL, FN, S, FL) inline_mysql_file_fstat(FN, S, FL)
```

Defined in psi/mysql_file.h:167

Instrumented fstat. `mysql_file_fstat` is a replacement for `my_fstat`.

---

{#mysql_file_stat}

### mysql_file_stat

```cpp
#define mysql_file_stat(K, FN, S, FL, K, FN, S, FL) inline_mysql_file_stat(FN, S, FL)
```

Defined in psi/mysql_file.h:180

Instrumented stat. `mysql_file_stat` is a replacement for `my_stat`.

---

{#mysql_file_chsize}

### mysql_file_chsize

```cpp
#define mysql_file_chsize(F, P1, P2, P3, F, P1, P2, P3) inline_mysql_file_chsize(F, P1, P2, P3)
```

Defined in psi/mysql_file.h:193

Instrumented chsize. `mysql_file_chsize` is a replacement for `my_chsize`.

---

{#mysql_file_fopen}

### mysql_file_fopen

```cpp
#define mysql_file_fopen(K, N, F1, F2, K, N, F1, F2) inline_mysql_file_fopen(N, F1, F2)
```

Defined in psi/mysql_file.h:206

Instrumented fopen. `mysql_file_fopen` is a replacement for `my_fopen`.

---

{#mysql_file_fclose}

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

{#mysql_file_fread}

### mysql_file_fread

```cpp
#define mysql_file_fread(FD, P1, P2, P3, FD, P1, P2, P3) inline_mysql_file_fread(FD, P1, P2, P3)
```

Defined in psi/mysql_file.h:239

Instrumented fread. `mysql_file_fread` is a replacement for `my_fread`.

---

{#mysql_file_fwrite}

### mysql_file_fwrite

```cpp
#define mysql_file_fwrite(FD, P1, P2, P3, FD, P1, P2, P3) inline_mysql_file_fwrite(FD, P1, P2, P3)
```

Defined in psi/mysql_file.h:252

Instrumented fwrite. `mysql_file_fwrite` is a replacement for `my_fwrite`.

---

{#mysql_file_fseek}

### mysql_file_fseek

```cpp
#define mysql_file_fseek(FD, P, W, F, FD, P, W, F) inline_mysql_file_fseek(FD, P, W, F)
```

Defined in psi/mysql_file.h:265

Instrumented fseek. `mysql_file_fseek` is a replacement for `my_fseek`.

---

{#mysql_file_ftell}

### mysql_file_ftell

```cpp
#define mysql_file_ftell(FD, F, FD, F) inline_mysql_file_ftell(FD, F)
```

Defined in psi/mysql_file.h:278

Instrumented ftell. `mysql_file_ftell` is a replacement for `my_ftell`.

---

{#mysql_file_create}

### mysql_file_create

```cpp
#define mysql_file_create(K, N, F1, F2, F3, K, N, F1, F2, F3) inline_mysql_file_create(N, F1, F2, F3)
```

Defined in psi/mysql_file.h:291

Instrumented create. `mysql_file_create` is a replacement for `my_create`.

---

{#mysql_file_create_temp}

### mysql_file_create_temp

```cpp
#define mysql_file_create_temp(K, T, D, P, M, F, K, T, D, P, M, F) inline_mysql_file_create_temp(T, D, P, M, F)
```

Defined in psi/mysql_file.h:304

Instrumented create_temp_file. `mysql_file_create_temp` is a replacement for `create_temp_file`.

---

{#mysql_file_open}

### mysql_file_open

```cpp
#define mysql_file_open(K, N, F1, F2, K, N, F1, F2) inline_mysql_file_open(N, F1, F2)
```

Defined in psi/mysql_file.h:317

Instrumented open. `mysql_file_open` is a replacement for `my_open`.

---

{#mysql_file_close}

### mysql_file_close

```cpp
#define mysql_file_close(FD, F, FD, F) inline_mysql_file_close(FD, F)
```

Defined in psi/mysql_file.h:330

Instrumented close. `mysql_file_close` is a replacement for `my_close`.

---

{#mysql_file_read}

### mysql_file_read

```cpp
#define mysql_file_read(FD, B, S, F, FD, B, S, F) inline_mysql_file_read(FD, B, S, F)
```

Defined in psi/mysql_file.h:343

Instrumented read. `mysql_read` is a replacement for `my_read`.

---

{#mysql_file_write}

### mysql_file_write

```cpp
#define mysql_file_write(FD, B, S, F, FD, B, S, F) inline_mysql_file_write(FD, B, S, F)
```

Defined in psi/mysql_file.h:356

Instrumented write. `mysql_file_write` is a replacement for `my_write`.

---

{#mysql_file_pread}

### mysql_file_pread

```cpp
#define mysql_file_pread(FD, B, S, O, F, FD, B, S, O, F) inline_mysql_file_pread(FD, B, S, O, F)
```

Defined in psi/mysql_file.h:369

Instrumented pread. `mysql_pread` is a replacement for `my_pread`.

---

{#mysql_file_pwrite}

### mysql_file_pwrite

```cpp
#define mysql_file_pwrite(FD, B, S, O, F, FD, B, S, O, F) inline_mysql_file_pwrite(FD, B, S, O, F)
```

Defined in psi/mysql_file.h:382

Instrumented pwrite. `mysql_file_pwrite` is a replacement for `my_pwrite`.

---

{#mysql_file_seek}

### mysql_file_seek

```cpp
#define mysql_file_seek(FD, P, W, F, FD, P, W, F) inline_mysql_file_seek(FD, P, W, F)
```

Defined in psi/mysql_file.h:395

Instrumented seek. `mysql_file_seek` is a replacement for `my_seek`.

---

{#mysql_file_tell}

### mysql_file_tell

```cpp
#define mysql_file_tell(FD, F, FD, F) inline_mysql_file_tell(FD, F)
```

Defined in psi/mysql_file.h:408

Instrumented tell. `mysql_file_tell` is a replacement for `my_tell`.

---

{#mysql_file_delete}

### mysql_file_delete

```cpp
#define mysql_file_delete(K, P1, P2, K, P1, P2) inline_mysql_file_delete(P1, P2)
```

Defined in psi/mysql_file.h:421

Instrumented delete. `mysql_file_delete` is a replacement for `my_delete`.

---

{#mysql_file_rename}

### mysql_file_rename

```cpp
#define mysql_file_rename(K, P1, P2, P3, K, P1, P2, P3) inline_mysql_file_rename(P1, P2, P3)
```

Defined in psi/mysql_file.h:434

Instrumented rename. `mysql_file_rename` is a replacement for `my_rename`.

---

{#mysql_file_create_with_symlink}

### mysql_file_create_with_symlink

```cpp
#define mysql_file_create_with_symlink(K, P1, P2, P3, P4, P5, K, P1, P2, P3, P4, P5) inline_mysql_file_create_with_symlink(P1, P2, P3, P4, P5)
```

Defined in psi/mysql_file.h:449

Instrumented create with symbolic link. `mysql_file_create_with_symlink` is a replacement for `my_create_with_symlink`.

---

{#mysql_file_delete_with_symlink}

### mysql_file_delete_with_symlink

```cpp
#define mysql_file_delete_with_symlink(K, P1, P2, P3, K, P1, P2, P3) inline_mysql_file_delete_with_symlink(P1, P2, P3)
```

Defined in psi/mysql_file.h:463

Instrumented delete with symbolic link. `mysql_file_delete_with_symlink` is a replacement for `my_handler_delete_with_symlink`.

---

{#mysql_file_rename_with_symlink}

### mysql_file_rename_with_symlink

```cpp
#define mysql_file_rename_with_symlink(K, P1, P2, P3, K, P1, P2, P3) inline_mysql_file_rename_with_symlink(P1, P2, P3)
```

Defined in psi/mysql_file.h:477

Instrumented rename with symbolic link. `mysql_file_rename_with_symlink` is a replacement for `my_rename_with_symlink`.

---

{#mysql_file_sync}

### mysql_file_sync

```cpp
#define mysql_file_sync(P1, P2, P1, P2) inline_mysql_file_sync(P1, P2)
```

Defined in psi/mysql_file.h:490

Instrumented file sync. `mysql_file_sync` is a replacement for `my_sync`.

---

{#psi_idle_call}

### PSI_IDLE_CALL

```cpp
#define PSI_IDLE_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_idle.h:35

---

{#mysql_start_idle_wait}

### MYSQL_START_IDLE_WAIT

```cpp
#define MYSQL_START_IDLE_WAIT(LOCKER, STATE, LOCKER, STATE) do {} while (0)
```

Defined in psi/mysql_idle.h:56

Instrumentation helper for table io_waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_IDLE_WAIT](#mysql_end_idle_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |

---

{#mysql_end_idle_wait}

### MYSQL_END_IDLE_WAIT

```cpp
#define MYSQL_END_IDLE_WAIT(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql_idle.h:71

Instrumentation helper for idle waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_IDLE_WAIT](#mysql_start_idle_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `LOCKER` |  | the locker |

---

{#mysql_plugin_auth_included}

### MYSQL_PLUGIN_AUTH_INCLUDED

```cpp
#define MYSQL_PLUGIN_AUTH_INCLUDED
```

Defined in plugin_auth.h:26

---

{#mysql_authentication_interface_version}

### MYSQL_AUTHENTICATION_INTERFACE_VERSION

```cpp
#define MYSQL_AUTHENTICATION_INTERFACE_VERSION 0x0203
```

Defined in plugin_auth.h:30

---

{#password_used_no}

### PASSWORD_USED_NO

```cpp
#define PASSWORD_USED_NO 0
```

Defined in plugin_auth.h:40

---

{#password_used_yes}

### PASSWORD_USED_YES

```cpp
#define PASSWORD_USED_YES 1
```

Defined in plugin_auth.h:41

---

{#password_used_no_mention}

### PASSWORD_USED_NO_MENTION

```cpp
#define PASSWORD_USED_NO_MENTION 2
```

Defined in plugin_auth.h:42

---

{#psi_stage_call}

### PSI_STAGE_CALL

```cpp
#define PSI_STAGE_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_stage.h:34

---

{#mysql_stage_register}

### mysql_stage_register

```cpp
#define mysql_stage_register(P1, P2, P3, P1, P2, P3) do {} while (0)
```

Defined in psi/mysql_stage.h:51

Stage registration.

---

{#mysql_set_stage}

### MYSQL_SET_STAGE

```cpp
#define MYSQL_SET_STAGE(K, F, L, K, F, L) NULL
```

Defined in psi/mysql_stage.h:69

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

{#mysql_set_stage-1}

### mysql_set_stage

```cpp
#define mysql_set_stage(K, K) NULL
```

Defined in psi/mysql_stage.h:83

Set the current stage. 
#### Returns
the current stage progress

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | the stage key |
| `K` |  | the stage key |

---

{#mysql_end_stage}

### mysql_end_stage

```cpp
#define mysql_end_stage() do {} while (0)
```

Defined in psi/mysql_stage.h:95

End the last stage

---

{#mysql_stage_set_work_completed}

### mysql_stage_set_work_completed

```cpp
#define mysql_stage_set_work_completed(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql_stage.h:131

---

{#mysql_stage_get_work_completed}

### mysql_stage_get_work_completed

```cpp
#define mysql_stage_get_work_completed(P1, P1) do {} while (0)
```

Defined in psi/mysql_stage.h:134

---

{#mysql_stage_inc_work_completed}

### mysql_stage_inc_work_completed

```cpp
#define mysql_stage_inc_work_completed(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql_stage.h:142

---

{#mysql_stage_set_work_estimated}

### mysql_stage_set_work_estimated

```cpp
#define mysql_stage_set_work_estimated(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql_stage.h:153

---

{#mysql_stage_get_work_estimated}

### mysql_stage_get_work_estimated

```cpp
#define mysql_stage_get_work_estimated(P1, P1) do {} while (0)
```

Defined in psi/mysql_stage.h:156

---

{#psi_table_call}

### PSI_TABLE_CALL

```cpp
#define PSI_TABLE_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_table.h:35

---

{#mysql_unbind_table}

### MYSQL_UNBIND_TABLE

```cpp
#define MYSQL_UNBIND_TABLE(handler, handler) do { } while(0)
```

Defined in psi/mysql_table.h:55

---

{#psi_call_unbind_table}

### PSI_CALL_unbind_table

```cpp
#define PSI_CALL_unbind_table(A1, A1) do { } while(0)
```

Defined in psi/mysql_table.h:57

---

{#psi_call_rebind_table}

### PSI_CALL_rebind_table

```cpp
#define PSI_CALL_rebind_table(A1, A2, A3, A1, A2, A3) NULL
```

Defined in psi/mysql_table.h:58

---

{#psi_call_close_table}

### PSI_CALL_close_table

```cpp
#define PSI_CALL_close_table(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_table.h:59

---

{#psi_call_open_table}

### PSI_CALL_open_table

```cpp
#define PSI_CALL_open_table(A1, A2, A1, A2) NULL
```

Defined in psi/mysql_table.h:60

---

{#psi_call_get_table_share}

### PSI_CALL_get_table_share

```cpp
#define PSI_CALL_get_table_share(A1, A2, A1, A2) NULL
```

Defined in psi/mysql_table.h:61

---

{#psi_call_release_table_share}

### PSI_CALL_release_table_share

```cpp
#define PSI_CALL_release_table_share(A1, A1) do { } while(0)
```

Defined in psi/mysql_table.h:62

---

{#psi_call_drop_table_share}

### PSI_CALL_drop_table_share

```cpp
#define PSI_CALL_drop_table_share(A1, A2, A3, A4, A5, A1, A2, A3, A4, A5) do { } while(0)
```

Defined in psi/mysql_table.h:63

---

{#mysql_table_wait_variables}

### MYSQL_TABLE_WAIT_VARIABLES

```cpp
#define MYSQL_TABLE_WAIT_VARIABLES(LOCKER, STATE, LOCKER, STATE)
```

Defined in psi/mysql_table.h:83

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

{#mysql_start_table_lock_wait}

### MYSQL_START_TABLE_LOCK_WAIT

```cpp
#define MYSQL_START_TABLE_LOCK_WAIT(LOCKER, STATE, PSI, OP, FLAGS, LOCKER, STATE, PSI, OP, FLAGS) do {} while (0)
```

Defined in psi/mysql_table.h:102

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

{#mysql_end_table_lock_wait}

### MYSQL_END_TABLE_LOCK_WAIT

```cpp
#define MYSQL_END_TABLE_LOCK_WAIT(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql_table.h:117

Instrumentation helper for table lock waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_TABLE_LOCK_WAIT](#mysql_start_table_lock_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `LOCKER` |  | the locker |

---

{#mysql_unlock_table}

### MYSQL_UNLOCK_TABLE

```cpp
#define MYSQL_UNLOCK_TABLE(T, T) do {} while (0)
```

Defined in psi/mysql_table.h:125

---

{#my_global_included}

### MY_GLOBAL_INCLUDED

```cpp
#define MY_GLOBAL_INCLUDED
```

Defined in psi/psi_abi_v0.h:29

---

{#use_psi_1}

### USE_PSI_1

```cpp
#define USE_PSI_1
```

Defined in psi/psi_abi_v1.h:29

---

{#have_psi_interface}

### HAVE_PSI_INTERFACE

```cpp
#define HAVE_PSI_INTERFACE
```

Defined in psi/psi_abi_v1.h:30

---

{#my_global_included-1}

### MY_GLOBAL_INCLUDED

```cpp
#define MY_GLOBAL_INCLUDED
```

Defined in psi/psi_abi_v1.h:31

---

{#use_psi_2}

### USE_PSI_2

```cpp
#define USE_PSI_2
```

Defined in psi/psi_abi_v2.h:29

---

{#have_psi_interface-1}

### HAVE_PSI_INTERFACE

```cpp
#define HAVE_PSI_INTERFACE
```

Defined in psi/psi_abi_v2.h:30

---

{#my_global_included-2}

### MY_GLOBAL_INCLUDED

```cpp
#define MY_GLOBAL_INCLUDED
```

Defined in psi/psi_abi_v2.h:31

---

{#my_md5_hash_size}

### MY_MD5_HASH_SIZE

```cpp
#define MY_MD5_HASH_SIZE 16 /* Hash size in bytes */
```

Defined in service_md5.h:32

---

{#mysql_service_md5_included}

### MYSQL_SERVICE_MD5_INCLUDED

```cpp
#define MYSQL_SERVICE_MD5_INCLUDED
```

Defined in service_md5.h:67

---

{#mysql_service_thd_included}

### MYSQL_SERVICE_THD_INCLUDED

```cpp
#define MYSQL_SERVICE_THD_INCLUDED
```

Defined in service_thd.h:45

---

{#mysql_audit_class_mask_size}

### MYSQL_AUDIT_CLASS_MASK_SIZE

```cpp
#define MYSQL_AUDIT_CLASS_MASK_SIZE 1
```

Defined in plugin_audit.h:30

---

{#mysql_audit_interface_version}

### MYSQL_AUDIT_INTERFACE_VERSION

```cpp
#define MYSQL_AUDIT_INTERFACE_VERSION 0x0303
```

Defined in plugin_audit.h:32

---

{#mysql_audit_general_class}

### MYSQL_AUDIT_GENERAL_CLASS

```cpp
#define MYSQL_AUDIT_GENERAL_CLASS 0
```

Defined in plugin_audit.h:45

---

{#mysql_audit_general_classmask}

### MYSQL_AUDIT_GENERAL_CLASSMASK

```cpp
#define MYSQL_AUDIT_GENERAL_CLASSMASK (1 << MYSQL_AUDIT_GENERAL_CLASS)
```

Defined in plugin_audit.h:46

---

{#mysql_audit_general_log}

### MYSQL_AUDIT_GENERAL_LOG

```cpp
#define MYSQL_AUDIT_GENERAL_LOG 0
```

Defined in plugin_audit.h:47

---

{#mysql_audit_general_error}

### MYSQL_AUDIT_GENERAL_ERROR

```cpp
#define MYSQL_AUDIT_GENERAL_ERROR 1
```

Defined in plugin_audit.h:48

---

{#mysql_audit_general_result}

### MYSQL_AUDIT_GENERAL_RESULT

```cpp
#define MYSQL_AUDIT_GENERAL_RESULT 2
```

Defined in plugin_audit.h:49

---

{#mysql_audit_general_status}

### MYSQL_AUDIT_GENERAL_STATUS

```cpp
#define MYSQL_AUDIT_GENERAL_STATUS 3
```

Defined in plugin_audit.h:50

---

{#mysql_audit_general_warning}

### MYSQL_AUDIT_GENERAL_WARNING

```cpp
#define MYSQL_AUDIT_GENERAL_WARNING 4
```

Defined in plugin_audit.h:51

---

{#mysql_audit_connection_class}

### MYSQL_AUDIT_CONNECTION_CLASS

```cpp
#define MYSQL_AUDIT_CONNECTION_CLASS 1
```

Defined in plugin_audit.h:83

---

{#mysql_audit_connection_classmask}

### MYSQL_AUDIT_CONNECTION_CLASSMASK

```cpp
#define MYSQL_AUDIT_CONNECTION_CLASSMASK (1 << MYSQL_AUDIT_CONNECTION_CLASS)
```

Defined in plugin_audit.h:84

---

{#mysql_audit_connection_connect}

### MYSQL_AUDIT_CONNECTION_CONNECT

```cpp
#define MYSQL_AUDIT_CONNECTION_CONNECT 0
```

Defined in plugin_audit.h:85

---

{#mysql_audit_connection_disconnect}

### MYSQL_AUDIT_CONNECTION_DISCONNECT

```cpp
#define MYSQL_AUDIT_CONNECTION_DISCONNECT 1
```

Defined in plugin_audit.h:86

---

{#mysql_audit_connection_change_user}

### MYSQL_AUDIT_CONNECTION_CHANGE_USER

```cpp
#define MYSQL_AUDIT_CONNECTION_CHANGE_USER 2
```

Defined in plugin_audit.h:87

---

{#mysql_audit_table_class}

### MYSQL_AUDIT_TABLE_CLASS

```cpp
#define MYSQL_AUDIT_TABLE_CLASS 15
```

Defined in plugin_audit.h:126

---

{#mysql_audit_table_classmask}

### MYSQL_AUDIT_TABLE_CLASSMASK

```cpp
#define MYSQL_AUDIT_TABLE_CLASSMASK (1 << MYSQL_AUDIT_TABLE_CLASS)
```

Defined in plugin_audit.h:127

---

{#mysql_audit_table_lock}

### MYSQL_AUDIT_TABLE_LOCK

```cpp
#define MYSQL_AUDIT_TABLE_LOCK 0
```

Defined in plugin_audit.h:128

---

{#mysql_audit_table_create}

### MYSQL_AUDIT_TABLE_CREATE

```cpp
#define MYSQL_AUDIT_TABLE_CREATE 1
```

Defined in plugin_audit.h:129

---

{#mysql_audit_table_drop}

### MYSQL_AUDIT_TABLE_DROP

```cpp
#define MYSQL_AUDIT_TABLE_DROP 2
```

Defined in plugin_audit.h:130

---

{#mysql_audit_table_rename}

### MYSQL_AUDIT_TABLE_RENAME

```cpp
#define MYSQL_AUDIT_TABLE_RENAME 3
```

Defined in plugin_audit.h:131

---

{#mysql_audit_table_alter}

### MYSQL_AUDIT_TABLE_ALTER

```cpp
#define MYSQL_AUDIT_TABLE_ALTER 4
```

Defined in plugin_audit.h:132

---

{#psi_call_memory_alloc}

### PSI_CALL_memory_alloc

```cpp
#define PSI_CALL_memory_alloc(A1, A2, A3) 0
```

Defined in psi/mysql_memory.h:39

---

{#psi_call_memory_free}

### PSI_CALL_memory_free

```cpp
#define PSI_CALL_memory_free(A1, A2, A3) do { } while(0)
```

Defined in psi/mysql_memory.h:40

---

{#psi_call_memory_realloc}

### PSI_CALL_memory_realloc

```cpp
#define PSI_CALL_memory_realloc(A1, A2, A3, A4) 0
```

Defined in psi/mysql_memory.h:41

---

{#psi_call_register_memory}

### PSI_CALL_register_memory

```cpp
#define PSI_CALL_register_memory(A1, A2, A3) do { } while(0)
```

Defined in psi/mysql_memory.h:42

---

{#psi_memory_call}

### PSI_MEMORY_CALL

```cpp
#define PSI_MEMORY_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_memory.h:46

---

{#mysql_memory_register}

### mysql_memory_register

```cpp
#define mysql_memory_register(P1, P2, P3, P1, P2, P3) inline_mysql_memory_register(P1, P2, P3)
```

Defined in psi/mysql_memory.h:59

Memory registration.

---

{#sockbuf_t}

### SOCKBUF_T

```cpp
#define SOCKBUF_T void
```

Defined in psi/mysql_socket.h:41

---

{#psi_socket_call}

### PSI_SOCKET_CALL

```cpp
#define PSI_SOCKET_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_socket.h:51

---

{#mysql_socket_register}

### mysql_socket_register

```cpp
#define mysql_socket_register(P1, P2, P3, P1, P2, P3) inline_mysql_socket_register(P1, P2, P3)
```

Defined in psi/mysql_socket.h:65

Socket registration.

---

{#mysql_invalid_socket}

### MYSQL_INVALID_SOCKET

```cpp
#define MYSQL_INVALID_SOCKET mysql_socket_invalid()
```

Defined in psi/mysql_socket.h:107

MYSQL_SOCKET initial value.

---

{#mysql_socket_wait_variables}

### MYSQL_SOCKET_WAIT_VARIABLES

```cpp
#define MYSQL_SOCKET_WAIT_VARIABLES(LOCKER, STATE, LOCKER, STATE) struct PSI_socket_locker* LOCKER; \
    PSI_socket_locker_state STATE;
```

Defined in psi/mysql_socket.h:202

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

{#mysql_start_socket_wait}

### MYSQL_START_SOCKET_WAIT

```cpp
#define MYSQL_START_SOCKET_WAIT(LOCKER, STATE, SOCKET, OP, COUNT, LOCKER, STATE, SOCKET, OP, COUNT) LOCKER= inline_mysql_start_socket_wait(STATE, SOCKET, OP, COUNT,\
                                           __FILE__, __LINE__)
```

Defined in psi/mysql_socket.h:221

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

{#mysql_end_socket_wait}

### MYSQL_END_SOCKET_WAIT

```cpp
#define MYSQL_END_SOCKET_WAIT(LOCKER, COUNT, LOCKER, COUNT) inline_mysql_end_socket_wait(LOCKER, COUNT)
```

Defined in psi/mysql_socket.h:238

Instrumentation helper for socket waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_SOCKET_WAIT](#mysql_start_socket_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | locker |
| `COUNT` |  | actual bytes written/read, or -1 |
| `LOCKER` |  | locker |
| `COUNT` |  | actual bytes written/read, or -1 |

---

{#mysql_socket_set_state}

### MYSQL_SOCKET_SET_STATE

```cpp
#define MYSQL_SOCKET_SET_STATE(SOCKET, STATE, SOCKET, STATE) inline_mysql_socket_set_state(SOCKET, STATE)
```

Defined in psi/mysql_socket.h:253

Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI_socket_state

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `SOCKET` |  | the instrumented socket |
| `STATE` |  | the new state |
| `SOCKET` |  | the instrumented socket |
| `STATE` |  | the new state |

---

{#mysql_socket_fd}

### mysql_socket_fd

```cpp
#define mysql_socket_fd(K, F, K, F) inline_mysql_socket_fd(K, F)
```

Defined in psi/mysql_socket.h:317

Create a socket. `mysql_socket_fd` is a replacement for `socket`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | PSI_socket_key for this instrumented socket |
| `F` |  | File descriptor |
| `K` |  | PSI_socket_key for this instrumented socket |
| `F` |  | File descriptor |

---

{#mysql_socket_socket}

### mysql_socket_socket

```cpp
#define mysql_socket_socket(K, D, T, P, K, D, T, P) inline_mysql_socket_socket(K, D, T, P)
```

Defined in psi/mysql_socket.h:335

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

{#mysql_socket_bind}

### mysql_socket_bind

```cpp
#define mysql_socket_bind(FD, AP, L, FD, AP, L) inline_mysql_socket_bind(__FILE__, __LINE__, FD, AP, L)
```

Defined in psi/mysql_socket.h:351

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

{#mysql_socket_getsockname}

### mysql_socket_getsockname

```cpp
#define mysql_socket_getsockname(FD, AP, LP, FD, AP, LP) inline_mysql_socket_getsockname(__FILE__, __LINE__, FD, AP, LP)
```

Defined in psi/mysql_socket.h:367

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

{#mysql_socket_connect}

### mysql_socket_connect

```cpp
#define mysql_socket_connect(FD, AP, L, FD, AP, L) inline_mysql_socket_connect(__FILE__, __LINE__, FD, AP, L)
```

Defined in psi/mysql_socket.h:383

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

{#mysql_socket_getpeername}

### mysql_socket_getpeername

```cpp
#define mysql_socket_getpeername(FD, AP, LP, FD, AP, LP) inline_mysql_socket_getpeername(__FILE__, __LINE__, FD, AP, LP)
```

Defined in psi/mysql_socket.h:399

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

{#mysql_socket_send}

### mysql_socket_send

```cpp
#define mysql_socket_send(FD, B, N, FL, FD, B, N, FL) inline_mysql_socket_send(__FILE__, __LINE__, FD, B, N, FL)
```

Defined in psi/mysql_socket.h:416

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

{#mysql_socket_recv}

### mysql_socket_recv

```cpp
#define mysql_socket_recv(FD, B, N, FL, FD, B, N, FL) inline_mysql_socket_recv(__FILE__, __LINE__, FD, B, N, FL)
```

Defined in psi/mysql_socket.h:433

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

{#mysql_socket_sendto}

### mysql_socket_sendto

```cpp
#define mysql_socket_sendto(FD, B, N, FL, AP, L, FD, B, N, FL, AP, L) inline_mysql_socket_sendto(__FILE__, __LINE__, FD, B, N, FL, AP, L)
```

Defined in psi/mysql_socket.h:452

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

{#mysql_socket_recvfrom}

### mysql_socket_recvfrom

```cpp
#define mysql_socket_recvfrom(FD, B, N, FL, AP, LP, FD, B, N, FL, AP, LP) inline_mysql_socket_recvfrom(__FILE__, __LINE__, FD, B, N, FL, AP, LP)
```

Defined in psi/mysql_socket.h:471

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

{#mysql_socket_getsockopt}

### mysql_socket_getsockopt

```cpp
#define mysql_socket_getsockopt(FD, LV, ON, OP, OL, FD, LV, ON, OP, OL) inline_mysql_socket_getsockopt(__FILE__, __LINE__, FD, LV, ON, OP, OL)
```

Defined in psi/mysql_socket.h:489

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

{#mysql_socket_setsockopt}

### mysql_socket_setsockopt

```cpp
#define mysql_socket_setsockopt(FD, LV, ON, OP, OL, FD, LV, ON, OP, OL) inline_mysql_socket_setsockopt(__FILE__, __LINE__, FD, LV, ON, OP, OL)
```

Defined in psi/mysql_socket.h:507

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

{#mysql_sock_set_nonblocking}

### mysql_sock_set_nonblocking

```cpp
#define mysql_sock_set_nonblocking(FD, FD) inline_mysql_sock_set_nonblocking(__FILE__, __LINE__, FD)
```

Defined in psi/mysql_socket.h:520

Set socket to non-blocking.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | instrumented socket descriptor |
| `FD` |  | instrumented socket descriptor |

---

{#mysql_socket_listen}

### mysql_socket_listen

```cpp
#define mysql_socket_listen(FD, N, FD, N) inline_mysql_socket_listen(__FILE__, __LINE__, FD, N)
```

Defined in psi/mysql_socket.h:535

Set socket state to listen for an incoming connection. `mysql_socket_listen` is a replacement for `listen`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor, bound and connected |
| `N` |  | Maximum number of pending connections allowed. |
| `FD` |  | Instrumented socket descriptor, bound and connected |
| `N` |  | Maximum number of pending connections allowed. |

---

{#mysql_socket_accept}

### mysql_socket_accept

```cpp
#define mysql_socket_accept(K, FD, AP, LP, K, FD, AP, LP) inline_mysql_socket_accept(__FILE__, __LINE__, K, FD, AP, LP)
```

Defined in psi/mysql_socket.h:552

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

{#mysql_socket_close}

### mysql_socket_close

```cpp
#define mysql_socket_close(FD, FD) inline_mysql_socket_close(__FILE__, __LINE__, FD)
```

Defined in psi/mysql_socket.h:566

Close a socket and sever any connections. `mysql_socket_close` is a replacement for `close`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |

---

{#mysql_socket_shutdown}

### mysql_socket_shutdown

```cpp
#define mysql_socket_shutdown(FD, H, FD, H) inline_mysql_socket_shutdown(__FILE__, __LINE__, FD, H)
```

Defined in psi/mysql_socket.h:581

Disable receives and/or sends on a socket. `mysql_socket_shutdown` is a replacement for `shutdown`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `H` |  | Specifies which operations to shutdown |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `H` |  | Specifies which operations to shutdown |

---

{#psi_mutex_call}

### PSI_MUTEX_CALL

```cpp
#define PSI_MUTEX_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_thread.h:73

---

{#psi_rwlock_call}

### PSI_RWLOCK_CALL

```cpp
#define PSI_RWLOCK_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_thread.h:77

---

{#psi_cond_call}

### PSI_COND_CALL

```cpp
#define PSI_COND_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_thread.h:81

---

{#psi_thread_call}

### PSI_THREAD_CALL

```cpp
#define PSI_THREAD_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_thread.h:85

---

{#psi_call_delete_current_thread}

### PSI_CALL_delete_current_thread

```cpp
#define PSI_CALL_delete_current_thread() do { } while(0)
```

Defined in psi/mysql_thread.h:111

---

{#psi_call_get_thread}

### PSI_CALL_get_thread

```cpp
#define PSI_CALL_get_thread() NULL
```

Defined in psi/mysql_thread.h:112

---

{#psi_call_new_thread}

### PSI_CALL_new_thread

```cpp
#define PSI_CALL_new_thread(A1, A2, A3, A1, A2, A3) NULL
```

Defined in psi/mysql_thread.h:113

---

{#psi_call_register_thread}

### PSI_CALL_register_thread

```cpp
#define PSI_CALL_register_thread(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql_thread.h:114

---

{#psi_call_set_thread}

### PSI_CALL_set_thread

```cpp
#define PSI_CALL_set_thread(A1, A1) do { } while(0)
```

Defined in psi/mysql_thread.h:115

---

{#psi_call_set_thread_thd}

### PSI_CALL_set_thread_THD

```cpp
#define PSI_CALL_set_thread_THD(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:116

---

{#psi_call_set_thread_connect_attrs}

### PSI_CALL_set_thread_connect_attrs

```cpp
#define PSI_CALL_set_thread_connect_attrs(A1, A2, A3, A1, A2, A3) 0
```

Defined in psi/mysql_thread.h:117

---

{#psi_call_set_thread_db}

### PSI_CALL_set_thread_db

```cpp
#define PSI_CALL_set_thread_db(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:118

---

{#psi_call_set_thread_id}

### PSI_CALL_set_thread_id

```cpp
#define PSI_CALL_set_thread_id(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:119

---

{#psi_call_set_thread_os_id}

### PSI_CALL_set_thread_os_id

```cpp
#define PSI_CALL_set_thread_os_id(A1, A1) do { } while(0)
```

Defined in psi/mysql_thread.h:120

---

{#psi_call_set_thread_info}

### PSI_CALL_set_thread_info

```cpp
#define PSI_CALL_set_thread_info(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_thread.h:121

---

{#psi_call_set_thread_start_time}

### PSI_CALL_set_thread_start_time

```cpp
#define PSI_CALL_set_thread_start_time(A1, A1) do { } while(0)
```

Defined in psi/mysql_thread.h:122

---

{#psi_call_set_thread_account}

### PSI_CALL_set_thread_account

```cpp
#define PSI_CALL_set_thread_account(A1, A2, A3, A4, A1, A2, A3, A4) do { } while(0)
```

Defined in psi/mysql_thread.h:123

---

{#psi_call_spawn_thread}

### PSI_CALL_spawn_thread

```cpp
#define PSI_CALL_spawn_thread(A1, A2, A3, A4, A5, A1, A2, A3, A4, A5) 0
```

Defined in psi/mysql_thread.h:124

---

{#psi_call_set_connection_type}

### PSI_CALL_set_connection_type

```cpp
#define PSI_CALL_set_connection_type(A, A) do { } while(0)
```

Defined in psi/mysql_thread.h:125

---

{#mysql_mutex_is_owner}

### mysql_mutex_is_owner

```cpp
#define mysql_mutex_is_owner(M, M) safe_mutex_is_owner(&(M)->m_mutex)
```

Defined in psi/mysql_thread.h:266

---

{#mysql_mutex_assert_owner}

### mysql_mutex_assert_owner

```cpp
#define mysql_mutex_assert_owner(M, M) safe_mutex_assert_owner(&(M)->m_mutex)
```

Defined in psi/mysql_thread.h:273

Wrapper, to use safe_mutex_assert_owner with instrumented mutexes. `mysql_mutex_assert_owner` is a drop-in replacement for `safe_mutex_assert_owner`.

---

{#mysql_mutex_assert_not_owner}

### mysql_mutex_assert_not_owner

```cpp
#define mysql_mutex_assert_not_owner(M, M) safe_mutex_assert_not_owner(&(M)->m_mutex)
```

Defined in psi/mysql_thread.h:282

Wrapper, to use safe_mutex_assert_not_owner with instrumented mutexes. `mysql_mutex_assert_not_owner` is a drop-in replacement for `safe_mutex_assert_not_owner`.

---

{#mysql_mutex_setflags}

### mysql_mutex_setflags

```cpp
#define mysql_mutex_setflags(M, F, M, F) safe_mutex_setflags(&(M)->m_mutex, (F))
```

Defined in psi/mysql_thread.h:285

---

{#mysql_prlock_assert_write_owner}

### mysql_prlock_assert_write_owner

```cpp
#define mysql_prlock_assert_write_owner(M, M) rw_pr_lock_assert_write_owner(&(M)->m_prlock)
```

Defined in psi/mysql_thread.h:293

Drop-in replacement for `rw_pr_lock_assert_write_owner`.

---

{#mysql_prlock_assert_not_write_owner}

### mysql_prlock_assert_not_write_owner

```cpp
#define mysql_prlock_assert_not_write_owner(M, M) rw_pr_lock_assert_not_write_owner(&(M)->m_prlock)
```

Defined in psi/mysql_thread.h:301

Drop-in replacement for `rw_pr_lock_assert_not_write_owner`.

---

{#mysql_mutex_register}

### mysql_mutex_register

```cpp
#define mysql_mutex_register(P1, P2, P3, P1, P2, P3) inline_mysql_mutex_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:308

Mutex registration.

---

{#mysql_mutex_init}

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

{#mysql_mutex_destroy}

### mysql_mutex_destroy

```cpp
#define mysql_mutex_destroy(M, M) inline_mysql_mutex_destroy(M)
```

Defined in psi/mysql_thread.h:348

Instrumented mutex_destroy. `mysql_mutex_destroy` is a drop-in replacement for `pthread_mutex_destroy`.

---

{#mysql_mutex_lock}

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

{#mysql_mutex_trylock}

### mysql_mutex_trylock

```cpp
#define mysql_mutex_trylock(M, M) inline_mysql_mutex_trylock(M)
```

Defined in psi/mysql_thread.h:378

Instrumented mutex_lock. `mysql_mutex_trylock` is a drop-in replacement for `pthread_mutex_trylock`.

---

{#mysql_mutex_unlock}

### mysql_mutex_unlock

```cpp
#define mysql_mutex_unlock(M, M) inline_mysql_mutex_unlock(M)
```

Defined in psi/mysql_thread.h:391

Instrumented mutex_unlock. `mysql_mutex_unlock` is a drop-in replacement for `pthread_mutex_unlock`.

---

{#mysql_rwlock_register}

### mysql_rwlock_register

```cpp
#define mysql_rwlock_register(P1, P2, P3, P1, P2, P3) inline_mysql_rwlock_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:399

Rwlock registration.

---

{#mysql_rwlock_init}

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

{#mysql_prlock_init}

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

{#mysql_rwlock_destroy}

### mysql_rwlock_destroy

```cpp
#define mysql_rwlock_destroy(RW, RW) inline_mysql_rwlock_destroy(RW)
```

Defined in psi/mysql_thread.h:435

Instrumented rwlock_destroy. `mysql_rwlock_destroy` is a drop-in replacement for `pthread_rwlock_destroy`.

---

{#mysql_prlock_destroy}

### mysql_prlock_destroy

```cpp
#define mysql_prlock_destroy(RW, RW) inline_mysql_prlock_destroy(RW)
```

Defined in psi/mysql_thread.h:443

Instrumented rw_pr_destroy. `mysql_prlock_destroy` is a drop-in replacement for `rw_pr_destroy`.

---

{#mysql_rwlock_rdlock}

### mysql_rwlock_rdlock

```cpp
#define mysql_rwlock_rdlock(RW, RW) inline_mysql_rwlock_rdlock(RW)
```

Defined in psi/mysql_thread.h:455

Instrumented rwlock_rdlock. `mysql_rwlock_rdlock` is a drop-in replacement for `pthread_rwlock_rdlock`.

---

{#mysql_prlock_rdlock}

### mysql_prlock_rdlock

```cpp
#define mysql_prlock_rdlock(RW, RW) inline_mysql_prlock_rdlock(RW)
```

Defined in psi/mysql_thread.h:469

Instrumented rw_pr_rdlock. `mysql_prlock_rdlock` is a drop-in replacement for `rw_pr_rdlock`.

---

{#mysql_rwlock_wrlock}

### mysql_rwlock_wrlock

```cpp
#define mysql_rwlock_wrlock(RW, RW) inline_mysql_rwlock_wrlock(RW)
```

Defined in psi/mysql_thread.h:483

Instrumented rwlock_wrlock. `mysql_rwlock_wrlock` is a drop-in replacement for `pthread_rwlock_wrlock`.

---

{#mysql_prlock_wrlock}

### mysql_prlock_wrlock

```cpp
#define mysql_prlock_wrlock(RW, RW) inline_mysql_prlock_wrlock(RW)
```

Defined in psi/mysql_thread.h:497

Instrumented rw_pr_wrlock. `mysql_prlock_wrlock` is a drop-in replacement for `rw_pr_wrlock`.

---

{#mysql_rwlock_tryrdlock}

### mysql_rwlock_tryrdlock

```cpp
#define mysql_rwlock_tryrdlock(RW, RW) inline_mysql_rwlock_tryrdlock(RW)
```

Defined in psi/mysql_thread.h:511

Instrumented rwlock_tryrdlock. `mysql_rwlock_tryrdlock` is a drop-in replacement for `pthread_rwlock_tryrdlock`.

---

{#mysql_rwlock_trywrlock}

### mysql_rwlock_trywrlock

```cpp
#define mysql_rwlock_trywrlock(RW, RW) inline_mysql_rwlock_trywrlock(RW)
```

Defined in psi/mysql_thread.h:525

Instrumented rwlock_trywrlock. `mysql_rwlock_trywrlock` is a drop-in replacement for `pthread_rwlock_trywrlock`.

---

{#mysql_rwlock_unlock}

### mysql_rwlock_unlock

```cpp
#define mysql_rwlock_unlock(RW, RW) inline_mysql_rwlock_unlock(RW)
```

Defined in psi/mysql_thread.h:535

Instrumented rwlock_unlock. `mysql_rwlock_unlock` is a drop-in replacement for `pthread_rwlock_unlock`.

---

{#mysql_prlock_unlock}

### mysql_prlock_unlock

```cpp
#define mysql_prlock_unlock(RW, RW) inline_mysql_prlock_unlock(RW)
```

Defined in psi/mysql_thread.h:543

Instrumented rw_pr_unlock. `mysql_prlock_unlock` is a drop-in replacement for `rw_pr_unlock`.

---

{#mysql_cond_register}

### mysql_cond_register

```cpp
#define mysql_cond_register(P1, P2, P3, P1, P2, P3) inline_mysql_cond_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:549

Cond registration.

---

{#mysql_cond_init}

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

{#mysql_cond_destroy}

### mysql_cond_destroy

```cpp
#define mysql_cond_destroy(C, C) inline_mysql_cond_destroy(C)
```

Defined in psi/mysql_thread.h:571

Instrumented cond_destroy. `mysql_cond_destroy` is a drop-in replacement for `pthread_cond_destroy`.

---

{#mysql_cond_wait}

### mysql_cond_wait

```cpp
#define mysql_cond_wait(C, M, C, M) inline_mysql_cond_wait(C, M)
```

Defined in psi/mysql_thread.h:582

Instrumented cond_wait. `mysql_cond_wait` is a drop-in replacement for `pthread_cond_wait`.

---

{#mysql_cond_timedwait}

### mysql_cond_timedwait

```cpp
#define mysql_cond_timedwait(C, M, W, C, M, W) inline_mysql_cond_timedwait(C, M, W)
```

Defined in psi/mysql_thread.h:596

Instrumented cond_timedwait. `mysql_cond_timedwait` is a drop-in replacement for `pthread_cond_timedwait`.

---

{#mysql_cond_signal}

### mysql_cond_signal

```cpp
#define mysql_cond_signal(C, C) inline_mysql_cond_signal(C)
```

Defined in psi/mysql_thread.h:605

Instrumented cond_signal. `mysql_cond_signal` is a drop-in replacement for `pthread_cond_signal`.

---

{#mysql_cond_broadcast}

### mysql_cond_broadcast

```cpp
#define mysql_cond_broadcast(C, C) inline_mysql_cond_broadcast(C)
```

Defined in psi/mysql_thread.h:613

Instrumented cond_broadcast. `mysql_cond_broadcast` is a drop-in replacement for `pthread_cond_broadcast`.

---

{#mysql_thread_register}

### mysql_thread_register

```cpp
#define mysql_thread_register(P1, P2, P3, P1, P2, P3) inline_mysql_thread_register(P1, P2, P3)
```

Defined in psi/mysql_thread.h:619

Thread registration.

---

{#mysql_thread_create}

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

{#mysql_thread_set_psi_id}

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

{#mysql_thread_set_psi_thd}

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

{#my_sha1_hash_size}

### MY_SHA1_HASH_SIZE

```cpp
#define MY_SHA1_HASH_SIZE 20 /* Hash size in bytes */
```

Defined in service_sha1.h:32

---

{#mysql_service_sha1_included}

### MYSQL_SERVICE_SHA1_INCLUDED

```cpp
#define MYSQL_SERVICE_SHA1_INCLUDED
```

Defined in service_sha1.h:67

---

{#mysql_service_sha2_included}

### MYSQL_SERVICE_SHA2_INCLUDED

```cpp
#define MYSQL_SERVICE_SHA2_INCLUDED
```

Defined in service_sha2.h:128

---

{#mysql_client_plugin_included}

### MYSQL_CLIENT_PLUGIN_INCLUDED

```cpp
#define MYSQL_CLIENT_PLUGIN_INCLUDED
```

Defined in client_plugin.h:25

---

{#mysql_plugin_export_c}

### MYSQL_PLUGIN_EXPORT_C

```cpp
#define MYSQL_PLUGIN_EXPORT_C
```

Defined in client_plugin.h:37

---

{#mysql_plugin_export-1}

### MYSQL_PLUGIN_EXPORT

```cpp
#define MYSQL_PLUGIN_EXPORT MYSQL_PLUGIN_EXPORT_C
```

Defined in client_plugin.h:44

---

{#c_mode_start}

### C_MODE_START

```cpp
#define C_MODE_START
```

Defined in client_plugin.h:45

---

{#c_mode_end}

### C_MODE_END

```cpp
#define C_MODE_END
```

Defined in client_plugin.h:46

---

{#mysql_client_reserved1}

### MYSQL_CLIENT_reserved1

```cpp
#define MYSQL_CLIENT_reserved1 0
```

Defined in client_plugin.h:55

---

{#mysql_client_reserved2}

### MYSQL_CLIENT_reserved2

```cpp
#define MYSQL_CLIENT_reserved2 1
```

Defined in client_plugin.h:56

---

{#mysql_client_authentication_plugin}

### MYSQL_CLIENT_AUTHENTICATION_PLUGIN

```cpp
#define MYSQL_CLIENT_AUTHENTICATION_PLUGIN 2
```

Defined in client_plugin.h:57

---

{#mysql_client_authentication_plugin_interface_version}

### MYSQL_CLIENT_AUTHENTICATION_PLUGIN_INTERFACE_VERSION

```cpp
#define MYSQL_CLIENT_AUTHENTICATION_PLUGIN_INTERFACE_VERSION 0x0101
```

Defined in client_plugin.h:59

---

{#mysql_client_max_plugins}

### MYSQL_CLIENT_MAX_PLUGINS

```cpp
#define MYSQL_CLIENT_MAX_PLUGINS 3
```

Defined in client_plugin.h:61

---

{#mysql_declare_client_plugin}

### mysql_declare_client_plugin

```cpp
#define mysql_declare_client_plugin(X) C_MODE_STARTMYSQL_PLUGIN_EXPORT_C         \
        struct st_mysql_client_plugin_ ## X        \
        _mysql_client_plugin_declaration_ = {   \
          MYSQL_CLIENT_ ## X ## _PLUGIN,        \
          MYSQL_CLIENT_ ## X ## _PLUGIN_INTERFACE_VERSION,
```

Defined in client_plugin.h:63

---

{#mysql_end_client_plugin}

### mysql_end_client_plugin

```cpp
#define mysql_end_client_plugin }; C_MODE_END
```

Defined in client_plugin.h:69

---

{#mysql_client_plugin_header}

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

Defined in client_plugin.h:72

---

{#wsrep_assert_innodb_trx}

### WSREP_ASSERT_INNODB_TRX

```cpp
#define WSREP_ASSERT_INNODB_TRX 1
```

Defined in service_wsrep.h:14

---

{#mysql_service_wsrep_included}

### MYSQL_SERVICE_WSREP_INCLUDED

```cpp
#define MYSQL_SERVICE_WSREP_INCLUDED
```

Defined in service_wsrep.h:107

---

{#mysql_service_wsrep_static_included}

### MYSQL_SERVICE_WSREP_STATIC_INCLUDED

```cpp
#define MYSQL_SERVICE_WSREP_STATIC_INCLUDED
```

Defined in service_wsrep.h:158

---

{#my_base64_decode_allow_multiple_chunks}

### MY_BASE64_DECODE_ALLOW_MULTIPLE_CHUNKS

```cpp
#define MY_BASE64_DECODE_ALLOW_MULTIPLE_CHUNKS 1
```

Defined in service_base64.h:33

---

{#mysql_service_base64_included}

### MYSQL_SERVICE_BASE64_INCLUDED

```cpp
#define MYSQL_SERVICE_BASE64_INCLUDED
```

Defined in service_base64.h:81

---

{#mysql_ftparser_interface_version}

### MYSQL_FTPARSER_INTERFACE_VERSION

```cpp
#define MYSQL_FTPARSER_INTERFACE_VERSION 0x0100
```

Defined in plugin_ftparser.h:29

---

{#mysql_ftflags_need_copy}

### MYSQL_FTFLAGS_NEED_COPY

```cpp
#define MYSQL_FTFLAGS_NEED_COPY 1
```

Defined in plugin_ftparser.h:142

---

{#psi_statement_call}

### PSI_STATEMENT_CALL

```cpp
#define PSI_STATEMENT_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_statement.h:38

---

{#psi_digest_call}

### PSI_DIGEST_CALL

```cpp
#define PSI_DIGEST_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_statement.h:42

---

{#mysql_statement_register}

### mysql_statement_register

```cpp
#define mysql_statement_register(P1, P2, P3, P1, P2, P3) do {} while (0)
```

Defined in psi/mysql_statement.h:59

Statement registration.

---

{#mysql_digest_start}

### MYSQL_DIGEST_START

```cpp
#define MYSQL_DIGEST_START(LOCKER, LOCKER) NULL
```

Defined in psi/mysql_statement.h:67

---

{#mysql_digest_end}

### MYSQL_DIGEST_END

```cpp
#define MYSQL_DIGEST_END(LOCKER, DIGEST, LOCKER, DIGEST) do {} while (0)
```

Defined in psi/mysql_statement.h:75

---

{#mysql_start_statement}

### MYSQL_START_STATEMENT

```cpp
#define MYSQL_START_STATEMENT(STATE, K, DB, DB_LEN, CS, SPS, STATE, K, DB, DB_LEN, CS, SPS) NULL
```

Defined in psi/mysql_statement.h:83

---

{#mysql_refine_statement}

### MYSQL_REFINE_STATEMENT

```cpp
#define MYSQL_REFINE_STATEMENT(LOCKER, K, LOCKER, K) NULL
```

Defined in psi/mysql_statement.h:91

---

{#mysql_set_statement_text}

### MYSQL_SET_STATEMENT_TEXT

```cpp
#define MYSQL_SET_STATEMENT_TEXT(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql_statement.h:99

---

{#mysql_set_statement_lock_time}

### MYSQL_SET_STATEMENT_LOCK_TIME

```cpp
#define MYSQL_SET_STATEMENT_LOCK_TIME(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_statement.h:107

---

{#mysql_set_statement_rows_sent}

### MYSQL_SET_STATEMENT_ROWS_SENT

```cpp
#define MYSQL_SET_STATEMENT_ROWS_SENT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_statement.h:115

---

{#mysql_set_statement_rows_examined}

### MYSQL_SET_STATEMENT_ROWS_EXAMINED

```cpp
#define MYSQL_SET_STATEMENT_ROWS_EXAMINED(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_statement.h:123

---

{#mysql_end_statement}

### MYSQL_END_STATEMENT

```cpp
#define MYSQL_END_STATEMENT(LOCKER, DA, LOCKER, DA) do {} while (0)
```

Defined in psi/mysql_statement.h:131

---

{#mysql_service_thd_rnd_included}

### MYSQL_SERVICE_THD_RND_INCLUDED

```cpp
#define MYSQL_SERVICE_THD_RND_INCLUDED
```

Defined in service_thd_rnd.h:62

---

{#mysql_plugin_encryption_included}

### MYSQL_PLUGIN_ENCRYPTION_INCLUDED

```cpp
#define MYSQL_PLUGIN_ENCRYPTION_INCLUDED
```

Defined in plugin_encryption.h:26

---

{#mariadb_encryption_interface_version}

### MariaDB_ENCRYPTION_INTERFACE_VERSION

```cpp
#define MariaDB_ENCRYPTION_INTERFACE_VERSION 0x0300
```

Defined in plugin_encryption.h:34

---

{#psi_transaction_call}

### PSI_TRANSACTION_CALL

```cpp
#define PSI_TRANSACTION_CALL(M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_transaction.h:34

---

{#mysql_start_transaction}

### MYSQL_START_TRANSACTION

```cpp
#define MYSQL_START_TRANSACTION(STATE, XID, TRXID, ISO, RO, AC, STATE, XID, TRXID, ISO, RO, AC) 0
```

Defined in psi/mysql_transaction.h:47

---

{#mysql_set_transaction_gtid}

### MYSQL_SET_TRANSACTION_GTID

```cpp
#define MYSQL_SET_TRANSACTION_GTID(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql_transaction.h:55

---

{#mysql_set_transaction_xid}

### MYSQL_SET_TRANSACTION_XID

```cpp
#define MYSQL_SET_TRANSACTION_XID(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql_transaction.h:63

---

{#mysql_set_transaction_xa_state}

### MYSQL_SET_TRANSACTION_XA_STATE

```cpp
#define MYSQL_SET_TRANSACTION_XA_STATE(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:71

---

{#mysql_set_transaction_trxid}

### MYSQL_SET_TRANSACTION_TRXID

```cpp
#define MYSQL_SET_TRANSACTION_TRXID(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:79

---

{#mysql_inc_transaction_savepoints}

### MYSQL_INC_TRANSACTION_SAVEPOINTS

```cpp
#define MYSQL_INC_TRANSACTION_SAVEPOINTS(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:87

---

{#mysql_inc_transaction_rollback_to_savepoint}

### MYSQL_INC_TRANSACTION_ROLLBACK_TO_SAVEPOINT

```cpp
#define MYSQL_INC_TRANSACTION_ROLLBACK_TO_SAVEPOINT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:95

---

{#mysql_inc_transaction_release_savepoint}

### MYSQL_INC_TRANSACTION_RELEASE_SAVEPOINT

```cpp
#define MYSQL_INC_TRANSACTION_RELEASE_SAVEPOINT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:103

---

{#mysql_rollback_transaction}

### MYSQL_ROLLBACK_TRANSACTION

```cpp
#define MYSQL_ROLLBACK_TRANSACTION(LOCKER, LOCKER) do { } while(0)
```

Defined in psi/mysql_transaction.h:111

---

{#mysql_commit_transaction}

### MYSQL_COMMIT_TRANSACTION

```cpp
#define MYSQL_COMMIT_TRANSACTION(LOCKER, LOCKER) do { } while(0)
```

Defined in psi/mysql_transaction.h:119

---

{#my_aes_ok}

### MY_AES_OK

```cpp
#define MY_AES_OK 0
```

Defined in service_my_crypt.h:37

---

{#my_aes_bad_data}

### MY_AES_BAD_DATA

```cpp
#define MY_AES_BAD_DATA -100
```

Defined in service_my_crypt.h:38

---

{#my_aes_openssl_error}

### MY_AES_OPENSSL_ERROR

```cpp
#define MY_AES_OPENSSL_ERROR -101
```

Defined in service_my_crypt.h:39

---

{#my_aes_bad_keysize}

### MY_AES_BAD_KEYSIZE

```cpp
#define MY_AES_BAD_KEYSIZE -102
```

Defined in service_my_crypt.h:40

---

{#my_aes_block_size}

### MY_AES_BLOCK_SIZE

```cpp
#define MY_AES_BLOCK_SIZE 16
```

Defined in service_my_crypt.h:43

---

{#my_aes_max_key_length}

### MY_AES_MAX_KEY_LENGTH

```cpp
#define MY_AES_MAX_KEY_LENGTH 32
```

Defined in service_my_crypt.h:46

---

{#my_aes_ctx_size}

### MY_AES_CTX_SIZE

```cpp
#define MY_AES_CTX_SIZE 1040
```

Defined in service_my_crypt.h:48

---

{#encryption_key_version_invalid}

### ENCRYPTION_KEY_VERSION_INVALID

```cpp
#define ENCRYPTION_KEY_VERSION_INVALID (~(unsigned int)0)
```

Defined in service_encryption.h:44

---

{#encryption_key_not_encrypted}

### ENCRYPTION_KEY_NOT_ENCRYPTED

```cpp
#define ENCRYPTION_KEY_NOT_ENCRYPTED (0)
```

Defined in service_encryption.h:45

---

{#encryption_key_system_data}

### ENCRYPTION_KEY_SYSTEM_DATA

```cpp
#define ENCRYPTION_KEY_SYSTEM_DATA 1
```

Defined in service_encryption.h:47

---

{#encryption_key_temporary_data}

### ENCRYPTION_KEY_TEMPORARY_DATA

```cpp
#define ENCRYPTION_KEY_TEMPORARY_DATA 2
```

Defined in service_encryption.h:48

---

{#encryption_key_buffer_too_small}

### ENCRYPTION_KEY_BUFFER_TOO_SMALL

```cpp
#define ENCRYPTION_KEY_BUFFER_TOO_SMALL (100)
```

Defined in service_encryption.h:51

---

{#encryption_flag_decrypt}

### ENCRYPTION_FLAG_DECRYPT

```cpp
#define ENCRYPTION_FLAG_DECRYPT 0
```

Defined in service_encryption.h:53

---

{#encryption_flag_encrypt}

### ENCRYPTION_FLAG_ENCRYPT

```cpp
#define ENCRYPTION_FLAG_ENCRYPT 1
```

Defined in service_encryption.h:54

---

{#encryption_flag_nopad}

### ENCRYPTION_FLAG_NOPAD

```cpp
#define ENCRYPTION_FLAG_NOPAD 2
```

Defined in service_encryption.h:55

---

{#encryption_key_get_latest_version}

### encryption_key_get_latest_version

```cpp
#define encryption_key_get_latest_version(KI) encryption_handler.encryption_key_get_latest_version_func(KI)
```

Defined in service_encryption.h:87

---

{#encryption_key_get}

### encryption_key_get

```cpp
#define encryption_key_get(KI, KV, K, S) encryption_handler.encryption_key_get_func((KI),(KV),(K),(S))
```

Defined in service_encryption.h:88

---

{#encryption_ctx_size}

### encryption_ctx_size

```cpp
#define encryption_ctx_size(KI, KV) encryption_handler.encryption_ctx_size_func((KI),(KV))
```

Defined in service_encryption.h:89

---

{#encryption_ctx_init}

### encryption_ctx_init

```cpp
#define encryption_ctx_init(CTX, K, KL, IV, IVL, F, KI, KV) encryption_handler.encryption_ctx_init_func((CTX),(K),(KL),(IV),(IVL),(F),(KI),(KV))
```

Defined in service_encryption.h:90

---

{#encryption_ctx_update}

### encryption_ctx_update

```cpp
#define encryption_ctx_update(CTX, S, SL, D, DL) encryption_handler.encryption_ctx_update_func((CTX),(S),(SL),(D),(DL))
```

Defined in service_encryption.h:91

---

{#encryption_ctx_finish}

### encryption_ctx_finish

```cpp
#define encryption_ctx_finish(CTX, D, DL) encryption_handler.encryption_ctx_finish_func((CTX),(D),(DL))
```

Defined in service_encryption.h:92

---

{#encryption_encrypted_length}

### encryption_encrypted_length

```cpp
#define encryption_encrypted_length(SL, KI, KV) encryption_handler.encryption_encrypted_length_func((SL),(KI),(KV))
```

Defined in service_encryption.h:93

---

{#mysql_service_encryption_included}

### MYSQL_SERVICE_ENCRYPTION_INCLUDED

```cpp
#define MYSQL_SERVICE_ENCRYPTION_INCLUDED
```

Defined in service_encryption.h:145

---

{#mysql_service_thd_alloc_included}

### MYSQL_SERVICE_THD_ALLOC_INCLUDED

```cpp
#define MYSQL_SERVICE_THD_ALLOC_INCLUDED
```

Defined in service_thd_alloc.h:144

---

{#mysql_auth_dialog_client_included}

### MYSQL_AUTH_DIALOG_CLIENT_INCLUDED

```cpp
#define MYSQL_AUTH_DIALOG_CLIENT_INCLUDED
```

Defined in auth_dialog_client.h:25

---

{#ordinary_question}

### ORDINARY_QUESTION

```cpp
#define ORDINARY_QUESTION "\2"
```

Defined in auth_dialog_client.h:51

first byte of the question string is the question "type". It can be an "ordinary" or a "password" question. The last bit set marks a last question in the authentication exchange.

---

{#last_question}

### LAST_QUESTION

```cpp
#define LAST_QUESTION "\3"
```

Defined in auth_dialog_client.h:52

---

{#password_question}

### PASSWORD_QUESTION

```cpp
#define PASSWORD_QUESTION "\4"
```

Defined in auth_dialog_client.h:53

---

{#last_password}

### LAST_PASSWORD

```cpp
#define LAST_PASSWORD "\5"
```

Defined in auth_dialog_client.h:54

---

{#mysql_plugin_auth_common_included}

### MYSQL_PLUGIN_AUTH_COMMON_INCLUDED

```cpp
#define MYSQL_PLUGIN_AUTH_COMMON_INCLUDED
```

Defined in plugin_auth_common.h:28

---

{#mysql_username_length}

### MYSQL_USERNAME_LENGTH

```cpp
#define MYSQL_USERNAME_LENGTH 512
```

Defined in plugin_auth_common.h:31

the max allowed length for a user name

---

{#cr_auth_plugin_error}

### CR_AUTH_PLUGIN_ERROR

```cpp
#define CR_AUTH_PLUGIN_ERROR 3
```

Defined in plugin_auth_common.h:43

return values of the plugin authenticate_user() method. Authentication failed, plugin internal error. An error occurred in the authentication plugin itself. These errors are reported in table performance_schema.host_cache, column COUNT_AUTH_PLUGIN_ERRORS.

---

{#cr_auth_handshake}

### CR_AUTH_HANDSHAKE

```cpp
#define CR_AUTH_HANDSHAKE 2
```

Defined in plugin_auth_common.h:50

Authentication failed, client server handshake. An error occurred during the client server handshake. These errors are reported in table performance_schema.host_cache, column COUNT_HANDSHAKE_ERRORS.

---

{#cr_auth_user_credentials}

### CR_AUTH_USER_CREDENTIALS

```cpp
#define CR_AUTH_USER_CREDENTIALS 1
```

Defined in plugin_auth_common.h:57

Authentication failed, user credentials. For example, wrong passwords. These errors are reported in table performance_schema.host_cache, column COUNT_AUTHENTICATION_ERRORS.

---

{#cr_error}

### CR_ERROR

```cpp
#define CR_ERROR 0
```

Defined in plugin_auth_common.h:68

Authentication failed. Additionally, all other CR_xxx values (libmysql error code) can be used too.

The client plugin may set the error code and the error message directly in the MYSQL structure and return CR_ERROR. If a CR_xxx specific error code was returned, an error message in the MYSQL structure will be overwritten. If CR_ERROR is returned without setting the error in MYSQL, CR_UNKNOWN_ERROR will be user.

---

{#cr_ok}

### CR_OK

```cpp
#define CR_OK -1
```

Defined in plugin_auth_common.h:76

Authentication (client part) was successful. It does not mean that the authentication as a whole was successful, usually it only means that the client was able to send the user name and the password to the server. If CR_OK is returned, the libmysql reads the next packet expecting it to be one of OK, ERROR, or CHANGE_PLUGIN packets.

---

{#cr_ok_handshake_complete}

### CR_OK_HANDSHAKE_COMPLETE

```cpp
#define CR_OK_HANDSHAKE_COMPLETE -2
```

Defined in plugin_auth_common.h:91

Authentication was successful. It means that the client has done its part successfully and also that a plugin has read the last packet (one of OK, ERROR, CHANGE_PLUGIN). In this case, libmysql will not read a packet from the server, but it will use the data at mysql->net.read_pos.

A plugin may return this value if the number of roundtrips in the authentication protocol is not known in advance, and the client plugin needs to read one packet more to determine if the authentication is finished or not.

Server plugins should not return this value.

---

{#debug_sync_service}

### debug_sync_service

```cpp
#define debug_sync_service debug_sync_C_callback_ptr
```

Defined in service_debug_sync.h:332

---

{#debug_sync}

### DEBUG_SYNC

```cpp
#define DEBUG_SYNC(thd, name) do { } while(0)
```

Defined in service_debug_sync.h:349

---

{#debug_sync_c_if_thd}

### DEBUG_SYNC_C_IF_THD

```cpp
#define DEBUG_SYNC_C_IF_THD(thd, _sync_point_name_) do { } while(0)
```

Defined in service_debug_sync.h:350

---

{#debug_sync_c}

### DEBUG_SYNC_C

```cpp
#define DEBUG_SYNC_C(name) DEBUG_SYNC(NULL, name)
```

Defined in service_debug_sync.h:357

---

{#mysql_service_debug_sync_included}

### MYSQL_SERVICE_DEBUG_SYNC_INCLUDED

```cpp
#define MYSQL_SERVICE_DEBUG_SYNC_INCLUDED
```

Defined in service_debug_sync.h:364

---

{#mysql_service_my_snprintf_included}

### MYSQL_SERVICE_MY_SNPRINTF_INCLUDED

```cpp
#define MYSQL_SERVICE_MY_SNPRINTF_INCLUDED
```

Defined in service_my_snprintf.h:124

---

{#mysql_service_thd_autoinc_included}

### MYSQL_SERVICE_THD_AUTOINC_INCLUDED

```cpp
#define MYSQL_SERVICE_THD_AUTOINC_INCLUDED
```

Defined in service_thd_autoinc.h:52

---

{#mysql_service_thd_timezone_included}

### MYSQL_SERVICE_THD_TIMEZONE_INCLUDED

```cpp
#define MYSQL_SERVICE_THD_TIMEZONE_INCLUDED
```

Defined in service_thd_timezone.h:77

---

{#thd_key_create_from_var}

### thd_key_create_from_var

```cpp
#define thd_key_create_from_var(K, V) do { *(K)= MYSQL_SYSVAR_NAME(V).offset; } while(0)
```

Defined in service_thd_specifics.h:69

---

{#mysql_service_thd_specifics_included}

### MYSQL_SERVICE_THD_SPECIFICS_INCLUDED

```cpp
#define MYSQL_SERVICE_THD_SPECIFICS_INCLUDED
```

Defined in service_thd_specifics.h:108

---

{#thd_killed}

### thd_killed

```cpp
#define thd_killed(THD) (thd_kill_level(THD) == THD_ABORT_ASAP)
```

Defined in service_kill_statement.h:53

---

{#me_error_log}

### ME_ERROR_LOG

```cpp
#define ME_ERROR_LOG 64 /* Write the message to the error log */
```

Defined in service_my_print_error.h:36

---

{#me_error_log_only}

### ME_ERROR_LOG_ONLY

```cpp
#define ME_ERROR_LOG_ONLY 128 /* Write the error message to error log only */
```

Defined in service_my_print_error.h:37

---

{#me_note}

### ME_NOTE

```cpp
#define ME_NOTE 1024 /* Not an error, just a note */
```

Defined in service_my_print_error.h:38

---

{#me_warning}

### ME_WARNING

```cpp
#define ME_WARNING 2048 /* Not an error, just a warning */
```

Defined in service_my_print_error.h:39

---

{#me_fatal}

### ME_FATAL

```cpp
#define ME_FATAL 4096 /* Fatal statement error */
```

Defined in service_my_print_error.h:40

---

{#thd_proc_info}

### thd_proc_info

```cpp
#define thd_proc_info(thd, msg) set_thd_proc_info(thd, msg, \
                                                   __func__, __FILE__, __LINE__)
```

Defined in service_progress_report.h:32

---

{#mysql_service_progress_report_included}

### MYSQL_SERVICE_PROGRESS_REPORT_INCLUDED

```cpp
#define MYSQL_SERVICE_PROGRESS_REPORT_INCLUDED
```

Defined in service_progress_report.h:80

---

{#encryption_scheme_key_invalid}

### ENCRYPTION_SCHEME_KEY_INVALID

```cpp
#define ENCRYPTION_SCHEME_KEY_INVALID -1
```

Defined in service_encryption_scheme.h:74

---

{#encryption_scheme_block_length}

### ENCRYPTION_SCHEME_BLOCK_LENGTH

```cpp
#define ENCRYPTION_SCHEME_BLOCK_LENGTH 16
```

Defined in service_encryption_scheme.h:75

---

{#mysql_service_encryption_scheme_included}

### MYSQL_SERVICE_ENCRYPTION_SCHEME_INCLUDED

```cpp
#define MYSQL_SERVICE_ENCRYPTION_SCHEME_INCLUDED
```

Defined in service_encryption_scheme.h:132

---

{#mysql_plugin_password_validation_included}

### MYSQL_PLUGIN_PASSWORD_VALIDATION_INCLUDED

```cpp
#define MYSQL_PLUGIN_PASSWORD_VALIDATION_INCLUDED
```

Defined in plugin_password_validation.h:25

---

{#mariadb_password_validation_interface_version}

### MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION

```cpp
#define MariaDB_PASSWORD_VALIDATION_INTERFACE_VERSION 0x0101
```

Defined in plugin_password_validation.h:33

---

{#mysql_service_thd_stmt_da_included}

### MYSQL_SERVICE_THD_STMT_DA_INCLUDED

```cpp
#define MYSQL_SERVICE_THD_STMT_DA_INCLUDED
```

Defined in service_thd_error_context.h:92

## Enumerations

---

{#psi_table_io_operation}

### PSI_table_io_operation

```cpp
enum PSI_table_io_operation
```

Defined in psi/psi.h:241

IO operation performed on an instrumented table.

| Value | Description |
|-------|-------------|
| `PSI_TABLE_FETCH_ROW` | Row fetch. |
| `PSI_TABLE_WRITE_ROW` | Row write. |
| `PSI_TABLE_UPDATE_ROW` | Row update. |
| `PSI_TABLE_DELETE_ROW` | Row delete. |

---

{#enum_mysql_show_type}

### enum_mysql_show_type

```cpp
enum enum_mysql_show_type
```

Defined in plugin.h:187

| Value | Description |
|-------|-------------|
| `SHOW_UNDEF` |  |
| `SHOW_BOOL` |  |
| `SHOW_UINT` |  |
| `SHOW_ULONG` |  |
| `SHOW_ULONGLONG` |  |
| `SHOW_CHAR` |  |
| `SHOW_CHAR_PTR` |  |
| `SHOW_ARRAY` |  |
| `SHOW_FUNC` |  |
| `SHOW_DOUBLE` |  |
| `SHOW_SINT` |  |
| `SHOW_SLONG` |  |
| `SHOW_SLONGLONG` |  |
| `SHOW_SIMPLE_FUNC` |  |
| `SHOW_SIZE_T` |  |
| `SHOW_always_last` |  |

---

{#enum_var_type}

### enum_var_type

```cpp
enum enum_var_type
```

Defined in plugin.h:201

| Value | Description |
|-------|-------------|
| `SHOW_OPT_DEFAULT` |  |
| `SHOW_OPT_SESSION` |  |
| `SHOW_OPT_GLOBAL` |  |
| `SHOW_OPT_SESSION_NO_LOCK` |  |

---

{#json_types}

### json_types

```cpp
enum json_types
```

Defined in service_json.h:51

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

{#wsrep_service_key_type}

### Wsrep_service_key_type

```cpp
enum Wsrep_service_key_type
```

Defined in service_wsrep.h:4

| Value | Description |
|-------|-------------|
| `WSREP_SERVICE_KEY_SHARED` |  |
| `WSREP_SERVICE_KEY_REFERENCE` |  |
| `WSREP_SERVICE_KEY_UPDATE` |  |
| `WSREP_SERVICE_KEY_EXCLUSIVE` |  |

---

{#enum_ftparser_mode}

### enum_ftparser_mode

```cpp
enum enum_ftparser_mode
```

Defined in plugin_ftparser.h:32

| Value | Description |
|-------|-------------|
| `MYSQL_FTPARSER_SIMPLE_MODE` |  |
| `MYSQL_FTPARSER_WITH_STOPWORDS` |  |
| `MYSQL_FTPARSER_FULL_BOOLEAN_INFO` |  |

---

{#enum_ft_token_type}

### enum_ft_token_type

```cpp
enum enum_ft_token_type
```

Defined in plugin_ftparser.h:80

| Value | Description |
|-------|-------------|
| `FT_TOKEN_EOF` |  |
| `FT_TOKEN_WORD` |  |
| `FT_TOKEN_LEFT_PAREN` |  |
| `FT_TOKEN_RIGHT_PAREN` |  |
| `FT_TOKEN_STOPWORD` |  |

---

{#my_aes_mode}

### my_aes_mode

```cpp
enum my_aes_mode
```

Defined in service_my_crypt.h:50

| Value | Description |
|-------|-------------|
| `MY_AES_ECB` |  |
| `MY_AES_CBC` |  |

---

{#my_digest}

### my_digest

```cpp
enum my_digest
```

Defined in service_my_crypt.h:60

| Value | Description |
|-------|-------------|
| `MY_DIGEST_SHA1` |  |
| `MY_DIGEST_SHA224` |  |
| `MY_DIGEST_SHA256` |  |
| `MY_DIGEST_SHA384` |  |
| `MY_DIGEST_SHA512` |  |

---

{#_thd_wait_type_e}

### _thd_wait_type_e

```cpp
enum _thd_wait_type_e
```

Defined in service_thd_wait.h:66

| Value | Description |
|-------|-------------|
| `THD_WAIT_SLEEP` |  |
| `THD_WAIT_DISKIO` |  |
| `THD_WAIT_ROW_LOCK` |  |
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

{#thd_kill_levels}

### thd_kill_levels

```cpp
enum thd_kill_levels
```

Defined in service_kill_statement.h:42

| Value | Description |
|-------|-------------|
| `THD_IS_NOT_KILLED` |  |
| `THD_ABORT_SOFTLY` | abort when possible, don't leave tables corrupted |
| `THD_ABORT_ASAP` | abort asap |
## Typedefs

---

{#mdl_key}

### MDL_key

```cpp
using MDL_key = struct MDL_key
```

Type: struct [`MDL_key`](#mdl_key)

Defined in psi/psi.h:70

---

{#opaque_mdl_type}

### opaque_mdl_type

```cpp
using opaque_mdl_type = int
```

Defined in psi/psi.h:73

**See also**: enum_mdl_type.

---

{#opaque_mdl_duration}

### opaque_mdl_duration

```cpp
using opaque_mdl_duration = int
```

Defined in psi/psi.h:76

**See also**: enum_mdl_duration.

---

{#opaque_mdl_status}

### opaque_mdl_status

```cpp
using opaque_mdl_status = int
```

Defined in psi/psi.h:79

**See also**: MDL_wait::enum_wait_status.

---

{#opaque_vio_type}

### opaque_vio_type

```cpp
using opaque_vio_type = int
```

Defined in psi/psi.h:82

**See also**: enum_vio_type.

---

{#thd}

### THD

```cpp
using THD = struct opaque_THD
```

Type: struct [`opaque_THD`](#opaque_thd)

Defined in psi/psi.h:99

---

{#psi_mutex}

### PSI_mutex

```cpp
using PSI_mutex = struct PSI_mutex
```

Type: struct [`PSI_mutex`](#psi_mutex)

Defined in psi/psi.h:115

---

{#psi_rwlock}

### PSI_rwlock

```cpp
using PSI_rwlock = struct PSI_rwlock
```

Type: struct [`PSI_rwlock`](#psi_rwlock)

Defined in psi/psi.h:122

---

{#psi_cond}

### PSI_cond

```cpp
using PSI_cond = struct PSI_cond
```

Type: struct [`PSI_cond`](#psi_cond)

Defined in psi/psi.h:129

---

{#psi_table_share}

### PSI_table_share

```cpp
using PSI_table_share = struct PSI_table_share
```

Type: struct [`PSI_table_share`](#psi_table_share)

Defined in psi/psi.h:136

---

{#psi_table}

### PSI_table

```cpp
using PSI_table = struct PSI_table
```

Type: struct [`PSI_table`](#psi_table)

Defined in psi/psi.h:143

---

{#psi_thread}

### PSI_thread

```cpp
using PSI_thread = struct PSI_thread
```

Type: struct [`PSI_thread`](#psi_thread)

Defined in psi/psi.h:150

---

{#psi_file}

### PSI_file

```cpp
using PSI_file = struct PSI_file
```

Type: struct [`PSI_file`](#psi_file)

Defined in psi/psi.h:157

---

{#psi_socket}

### PSI_socket

```cpp
using PSI_socket = struct PSI_socket
```

Type: struct [`PSI_socket`](#psi_socket)

Defined in psi/psi.h:164

---

{#psi_prepared_stmt}

### PSI_prepared_stmt

```cpp
using PSI_prepared_stmt = struct PSI_prepared_stmt
```

Type: struct [`PSI_prepared_stmt`](#psi_prepared_stmt)

Defined in psi/psi.h:171

---

{#psi_table_locker}

### PSI_table_locker

```cpp
using PSI_table_locker = struct PSI_table_locker
```

Type: struct [`PSI_table_locker`](#psi_table_locker)

Defined in psi/psi.h:178

---

{#psi_statement_locker}

### PSI_statement_locker

```cpp
using PSI_statement_locker = struct PSI_statement_locker
```

Type: struct [`PSI_statement_locker`](#psi_statement_locker)

Defined in psi/psi.h:185

---

{#psi_transaction_locker}

### PSI_transaction_locker

```cpp
using PSI_transaction_locker = struct PSI_transaction_locker
```

Type: struct [`PSI_transaction_locker`](#psi_transaction_locker)

Defined in psi/psi.h:192

---

{#psi_idle_locker}

### PSI_idle_locker

```cpp
using PSI_idle_locker = struct PSI_idle_locker
```

Type: struct [`PSI_idle_locker`](#psi_idle_locker)

Defined in psi/psi.h:199

---

{#psi_digest_locker}

### PSI_digest_locker

```cpp
using PSI_digest_locker = struct PSI_digest_locker
```

Type: struct [`PSI_digest_locker`](#psi_digest_locker)

Defined in psi/psi.h:206

---

{#psi_sp_share}

### PSI_sp_share

```cpp
using PSI_sp_share = struct PSI_sp_share
```

Type: struct [`PSI_sp_share`](#psi_sp_share)

Defined in psi/psi.h:213

---

{#psi_sp_locker}

### PSI_sp_locker

```cpp
using PSI_sp_locker = struct PSI_sp_locker
```

Type: struct [`PSI_sp_locker`](#psi_sp_locker)

Defined in psi/psi.h:220

---

{#psi_metadata_lock}

### PSI_metadata_lock

```cpp
using PSI_metadata_lock = struct PSI_metadata_lock
```

Type: struct [`PSI_metadata_lock`](#psi_metadata_lock)

Defined in psi/psi.h:227

---

{#psi_stage_progress}

### PSI_stage_progress

```cpp
using PSI_stage_progress = struct PSI_stage_progress
```

Type: struct [`PSI_stage_progress`](Instrumentation_interface.md#psi_stage_progress-1)

Defined in psi/psi.h:238

---

{#psi_table_io_operation-1}

### PSI_table_io_operation

```cpp
using PSI_table_io_operation = enum PSI_table_io_operation
```

Type: enum [`PSI_table_io_operation`](#psi_table_io_operation)

Defined in psi/psi.h:252

---

{#psi_table_locker_state}

### PSI_table_locker_state

```cpp
using PSI_table_locker_state = struct PSI_table_locker_state
```

Type: struct [`PSI_table_locker_state`](Instrumentation_interface.md#psi_table_locker_state-1)

Defined in psi/psi.h:290

---

{#psi_bootstrap}

### PSI_bootstrap

```cpp
using PSI_bootstrap = struct PSI_bootstrap
```

Type: struct [`PSI_bootstrap`](Instrumentation_interface.md#psi_bootstrap-1)

Defined in psi/psi.h:310

---

{#psi_mutex_key}

### PSI_mutex_key

```cpp
using PSI_mutex_key = unsigned int
```

Defined in psi/psi.h:792

Instrumented mutex key. To instrument a mutex, a mutex key must be obtained using `register_mutex`. Using a zero key always disable the instrumentation.

---

{#psi_rwlock_key}

### PSI_rwlock_key

```cpp
using PSI_rwlock_key = unsigned int
```

Defined in psi/psi.h:800

Instrumented rwlock key. To instrument a rwlock, a rwlock key must be obtained using `register_rwlock`. Using a zero key always disable the instrumentation.

---

{#psi_cond_key}

### PSI_cond_key

```cpp
using PSI_cond_key = unsigned int
```

Defined in psi/psi.h:808

Instrumented cond key. To instrument a condition, a condition key must be obtained using `register_cond`. Using a zero key always disable the instrumentation.

---

{#psi_thread_key}

### PSI_thread_key

```cpp
using PSI_thread_key = unsigned int
```

Defined in psi/psi.h:816

Instrumented thread key. To instrument a thread, a thread key must be obtained using `register_thread`. Using a zero key always disable the instrumentation.

---

{#psi_file_key}

### PSI_file_key

```cpp
using PSI_file_key = unsigned int
```

Defined in psi/psi.h:823

Instrumented file key. To instrument a file, a file key must be obtained using `register_file`. Using a zero key always disable the instrumentation.

---

{#psi_stage_key}

### PSI_stage_key

```cpp
using PSI_stage_key = unsigned int
```

Defined in psi/psi.h:830

Instrumented stage key. To instrument a stage, a stage key must be obtained using `register_stage`. Using a zero key always disable the instrumentation.

---

{#psi_statement_key}

### PSI_statement_key

```cpp
using PSI_statement_key = unsigned int
```

Defined in psi/psi.h:837

Instrumented statement key. To instrument a statement, a statement key must be obtained using `register_statement`. Using a zero key always disable the instrumentation.

---

{#psi_socket_key}

### PSI_socket_key

```cpp
using PSI_socket_key = unsigned int
```

Defined in psi/psi.h:844

Instrumented socket key. To instrument a socket, a socket key must be obtained using `register_socket`. Using a zero key always disable the instrumentation.

---

{#psi_mutex_info_v1}

### PSI_mutex_info_v1

```cpp
using PSI_mutex_info_v1 = struct PSI_mutex_info_v1
```

Type: struct [`PSI_mutex_info_v1`](Group_PSI_v1.md#psi_mutex_info_v1-1)

Defined in psi/psi.h:875

---

{#psi_rwlock_info_v1}

### PSI_rwlock_info_v1

```cpp
using PSI_rwlock_info_v1 = struct PSI_rwlock_info_v1
```

Type: struct [`PSI_rwlock_info_v1`](Group_PSI_v1.md#psi_rwlock_info_v1-1)

Defined in psi/psi.h:898

---

{#psi_cond_info_v1}

### PSI_cond_info_v1

```cpp
using PSI_cond_info_v1 = struct PSI_cond_info_v1
```

Type: struct [`PSI_cond_info_v1`](Group_PSI_v1.md#psi_cond_info_v1-1)

Defined in psi/psi.h:921

---

{#psi_thread_info_v1}

### PSI_thread_info_v1

```cpp
using PSI_thread_info_v1 = struct PSI_thread_info_v1
```

Type: struct [`PSI_thread_info_v1`](Group_PSI_v1.md#psi_thread_info_v1-1)

Defined in psi/psi.h:944

---

{#psi_file_info_v1}

### PSI_file_info_v1

```cpp
using PSI_file_info_v1 = struct PSI_file_info_v1
```

Type: struct [`PSI_file_info_v1`](Group_PSI_v1.md#psi_file_info_v1-1)

Defined in psi/psi.h:967

---

{#psi_stage_info_v1}

### PSI_stage_info_v1

```cpp
using PSI_stage_info_v1 = struct PSI_stage_info_v1
```

Type: struct [`PSI_stage_info_v1`](Group_PSI_v1.md#psi_stage_info_v1-1)

Defined in psi/psi.h:983

---

{#psi_statement_info_v1}

### PSI_statement_info_v1

```cpp
using PSI_statement_info_v1 = struct PSI_statement_info_v1
```

Type: struct [`PSI_statement_info_v1`](Group_PSI_v1.md#psi_statement_info_v1-1)

Defined in psi/psi.h:999

---

{#psi_socket_info_v1}

### PSI_socket_info_v1

```cpp
using PSI_socket_info_v1 = struct PSI_socket_info_v1
```

Type: struct [`PSI_socket_info_v1`](Group_PSI_v1.md#psi_socket_info_v1-1)

Defined in psi/psi.h:1022

---

{#psi_idle_locker_state_v1}

### PSI_idle_locker_state_v1

```cpp
using PSI_idle_locker_state_v1 = struct PSI_idle_locker_state_v1
```

Type: struct [`PSI_idle_locker_state_v1`](Group_PSI_v1.md#psi_idle_locker_state_v1-1)

Defined in psi/psi.h:1046

---

{#psi_mutex_locker_state_v1}

### PSI_mutex_locker_state_v1

```cpp
using PSI_mutex_locker_state_v1 = struct PSI_mutex_locker_state_v1
```

Type: struct [`PSI_mutex_locker_state_v1`](Group_PSI_v1.md#psi_mutex_locker_state_v1-1)

Defined in psi/psi.h:1074

---

{#psi_rwlock_locker_state_v1}

### PSI_rwlock_locker_state_v1

```cpp
using PSI_rwlock_locker_state_v1 = struct PSI_rwlock_locker_state_v1
```

Type: struct [`PSI_rwlock_locker_state_v1`](Group_PSI_v1.md#psi_rwlock_locker_state_v1-1)

Defined in psi/psi.h:1103

---

{#psi_cond_locker_state_v1}

### PSI_cond_locker_state_v1

```cpp
using PSI_cond_locker_state_v1 = struct PSI_cond_locker_state_v1
```

Type: struct [`PSI_cond_locker_state_v1`](Group_PSI_v1.md#psi_cond_locker_state_v1-1)

Defined in psi/psi.h:1133

---

{#psi_file_locker_state_v1}

### PSI_file_locker_state_v1

```cpp
using PSI_file_locker_state_v1 = struct PSI_file_locker_state_v1
```

Type: struct [`PSI_file_locker_state_v1`](Group_PSI_v1.md#psi_file_locker_state_v1-1)

Defined in psi/psi.h:1169

---

{#psi_metadata_locker_state_v1}

### PSI_metadata_locker_state_v1

```cpp
using PSI_metadata_locker_state_v1 = struct PSI_metadata_locker_state_v1
```

Type: struct [`PSI_metadata_locker_state_v1`](Group_PSI_v1.md#psi_metadata_locker_state_v1-1)

Defined in psi/psi.h:1195

---

{#psi_statement_locker_state_v1}

### PSI_statement_locker_state_v1

```cpp
using PSI_statement_locker_state_v1 = struct PSI_statement_locker_state_v1
```

Type: struct [`PSI_statement_locker_state_v1`](Group_PSI_v1.md#psi_statement_locker_state_v1-1)

Defined in psi/psi.h:1271

---

{#psi_transaction_locker_state_v1}

### PSI_transaction_locker_state_v1

```cpp
using PSI_transaction_locker_state_v1 = struct PSI_transaction_locker_state_v1
```

Type: struct [`PSI_transaction_locker_state_v1`](Group_PSI_v1.md#psi_transaction_locker_state_v1-1)

Defined in psi/psi.h:1311

---

{#psi_socket_locker_state_v1}

### PSI_socket_locker_state_v1

```cpp
using PSI_socket_locker_state_v1 = struct PSI_socket_locker_state_v1
```

Type: struct [`PSI_socket_locker_state_v1`](Group_PSI_v1.md#psi_socket_locker_state_v1-1)

Defined in psi/psi.h:1345

---

{#psi_sp_locker_state_v1}

### PSI_sp_locker_state_v1

```cpp
using PSI_sp_locker_state_v1 = struct PSI_sp_locker_state_v1
```

Type: struct [`PSI_sp_locker_state_v1`](Group_PSI_v1.md#psi_sp_locker_state_v1-1)

Defined in psi/psi.h:1360

---

{#register_mutex_v1_t}

### register_mutex_v1_t

```cpp
using register_mutex_v1_t = void(*
```

Defined in psi/psi.h:1370

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

{#register_rwlock_v1_t}

### register_rwlock_v1_t

```cpp
using register_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1379

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

{#register_cond_v1_t}

### register_cond_v1_t

```cpp
using register_cond_v1_t = void(*
```

Defined in psi/psi.h:1388

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

{#register_thread_v1_t}

### register_thread_v1_t

```cpp
using register_thread_v1_t = void(*
```

Defined in psi/psi.h:1397

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

{#register_file_v1_t}

### register_file_v1_t

```cpp
using register_file_v1_t = void(*
```

Defined in psi/psi.h:1406

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

{#register_stage_v1_t}

### register_stage_v1_t

```cpp
using register_stage_v1_t = void(*
```

Defined in psi/psi.h:1415

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

{#register_statement_v1_t}

### register_statement_v1_t

```cpp
using register_statement_v1_t = void(*
```

Defined in psi/psi.h:1424

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

{#register_socket_v1_t}

### register_socket_v1_t

```cpp
using register_socket_v1_t = void(*
```

Defined in psi/psi.h:1433

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

{#init_mutex_v1_t}

### init_mutex_v1_t

```cpp
using init_mutex_v1_t = struct PSI_mutex *(*
```

Defined in psi/psi.h:1433

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

{#destroy_mutex_v1_t}

### destroy_mutex_v1_t

```cpp
using destroy_mutex_v1_t = void(*
```

Defined in psi/psi.h:1449

Mutex instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mutex` |  | the mutex to destroy |
| `mutex` |  | the mutex to destroy |

---

{#init_rwlock_v1_t}

### init_rwlock_v1_t

```cpp
using init_rwlock_v1_t = struct PSI_rwlock *(*
```

Defined in psi/psi.h:1449

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

{#destroy_rwlock_v1_t}

### destroy_rwlock_v1_t

```cpp
using destroy_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1464

Rwlock instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `rwlock` |  | the rwlock to destroy |
| `rwlock` |  | the rwlock to destroy |

---

{#init_cond_v1_t}

### init_cond_v1_t

```cpp
using init_cond_v1_t = struct PSI_cond *(*
```

Defined in psi/psi.h:1464

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

{#destroy_cond_v1_t}

### destroy_cond_v1_t

```cpp
using destroy_cond_v1_t = void(*
```

Defined in psi/psi.h:1479

Cond instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cond` |  | the rcond to destroy |
| `cond` |  | the rcond to destroy |

---

{#init_socket_v1_t}

### init_socket_v1_t

```cpp
using init_socket_v1_t = struct PSI_socket *(*
```

Defined in psi/psi.h:1479

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

{#destroy_socket_v1_t}

### destroy_socket_v1_t

```cpp
using destroy_socket_v1_t = void(*
```

Defined in psi/psi.h:1497

socket instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | the socket to destroy |
| `socket` |  | the socket to destroy |

---

{#get_table_share_v1_t}

### get_table_share_v1_t

```cpp
using get_table_share_v1_t = struct PSI_table_share *(*
```

Defined in psi/psi.h:1497

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

{#release_table_share_v1_t}

### release_table_share_v1_t

```cpp
using release_table_share_v1_t = void(*
```

Defined in psi/psi.h:1512

Release a table share.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `share` |  | the table share to release |
| `share` |  | the table share to release |

---

{#drop_table_share_v1_t}

### drop_table_share_v1_t

```cpp
using drop_table_share_v1_t = void(*
```

Defined in psi/psi.h:1522

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

{#open_table_v1_t}

### open_table_v1_t

```cpp
using open_table_v1_t = struct PSI_table *(*
```

Defined in psi/psi.h:1522

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

{#unbind_table_v1_t}

### unbind_table_v1_t

```cpp
using unbind_table_v1_t = void(*
```

Defined in psi/psi.h:1540

Unbind a table handle from the current thread. This operation happens when an opened table is added to the open table cache.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `table` |  | the table to unbind |
| `table` |  | the table to unbind |

---

{#rebind_table_v1_t}

### rebind_table_v1_t

```cpp
using rebind_table_v1_t = PSI_table *(*
```

Defined in psi/psi.h:1548

Rebind a table handle to the current thread. This operation happens when a table from the open table cache is reused for a thread.

---

{#close_table_v1_t}

### close_table_v1_t

```cpp
using close_table_v1_t = void(*
```

Defined in psi/psi.h:1555

Close an instrumentation table handle. Note that the table handle is invalid after this call.

---

{#create_file_v1_t}

### create_file_v1_t

```cpp
using create_file_v1_t = void(*
```

Defined in psi/psi.h:1566

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

{#spawn_thread_v1_t}

### spawn_thread_v1_t

```cpp
using spawn_thread_v1_t = int(*
```

Defined in psi/psi.h:1578

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

{#new_thread_v1_t}

### new_thread_v1_t

```cpp
using new_thread_v1_t = struct PSI_thread *(*
```

Defined in psi/psi.h:1578

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

{#set_thread_thd_v1_t}

### set_thread_THD_v1_t

```cpp
using set_thread_THD_v1_t = void(*
```

Defined in psi/psi.h:1598

Assign a THD to an instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the instrumented thread |
| `thd` |  | the sql layer THD to assign |
| `thread` |  | the instrumented thread |
| `thd` |  | the sql layer THD to assign |

---

{#set_thread_id_v1_t}

### set_thread_id_v1_t

```cpp
using set_thread_id_v1_t = void(*
```

Defined in psi/psi.h:1606

Assign an id to an instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the instrumented thread |
| `id` |  | the id to assign |
| `thread` |  | the instrumented thread |
| `id` |  | the id to assign |

---

{#set_thread_os_id_v1_t}

### set_thread_os_id_v1_t

```cpp
using set_thread_os_id_v1_t = void(*
```

Defined in psi/psi.h:1614

Assign the current operating system thread id to an instrumented thread. The operating system task id is obtained from `gettid()`

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the instrumented thread |
| `thread` |  | the instrumented thread |

---

{#get_thread_v1_t}

### get_thread_v1_t

```cpp
using get_thread_v1_t = struct PSI_thread *(*
```

Defined in psi/psi.h:1614

Get the instrumentation for the running thread. For this function to return a result, the thread instrumentation must have been attached to the running thread using `set_thread()`
#### Returns
the instrumentation for the running thread

---

{#get_thread_class_name_v1_t}

### get_thread_class_name_v1_t

```cpp
using get_thread_class_name_v1_t = const char *(*
```

Defined in psi/psi.h:1629

Get name of the thread, according to the thread class. The name is returns without the thread/subsystem prefix.

---

{#set_thread_user_v1_t}

### set_thread_user_v1_t

```cpp
using set_thread_user_v1_t = void(*
```

Defined in psi/psi.h:1636

Assign a user name to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `user` |  | the user name |
| `user_len` |  | the user name length |
| `user` |  | the user name |
| `user_len` |  | the user name length |

---

{#set_thread_account_v1_t}

### set_thread_account_v1_t

```cpp
using set_thread_account_v1_t = void(*
```

Defined in psi/psi.h:1645

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

{#set_thread_db_v1_t}

### set_thread_db_v1_t

```cpp
using set_thread_db_v1_t = void(*
```

Defined in psi/psi.h:1653

Assign a current database to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `db` |  | the database name |
| `db_len` |  | the database name length |
| `db` |  | the database name |
| `db_len` |  | the database name length |

---

{#set_thread_command_v1_t}

### set_thread_command_v1_t

```cpp
using set_thread_command_v1_t = void(*
```

Defined in psi/psi.h:1659

Assign a current command to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `command` |  | the current command |
| `command` |  | the current command |

---

{#set_connection_type_v1_t}

### set_connection_type_v1_t

```cpp
using set_connection_type_v1_t = void(*
```

Defined in psi/psi.h:1665

Assign a connection type to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `conn_type` |  | the connection type |
| `conn_type` |  | the connection type |

---

{#set_thread_start_time_v1_t}

### set_thread_start_time_v1_t

```cpp
using set_thread_start_time_v1_t = void(*
```

Defined in psi/psi.h:1672

Assign a start time to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `start_time` |  | the thread start time |
| `start_time` |  | the thread start time |

---

{#set_thread_state_v1_t}

### set_thread_state_v1_t

```cpp
using set_thread_state_v1_t = void(*
```

Defined in psi/psi.h:1678

Assign a state to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | the thread state |
| `state` |  | the thread state |

---

{#set_thread_info_v1_t}

### set_thread_info_v1_t

```cpp
using set_thread_info_v1_t = void(*
```

Defined in psi/psi.h:1685

Assign a process info to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `info` |  | the process into string |
| `info_len` |  | the process into string length |
| `info` |  | the process into string |
| `info_len` |  | the process into string length |

---

{#set_thread_v1_t}

### set_thread_v1_t

```cpp
using set_thread_v1_t = void(*
```

Defined in psi/psi.h:1696

Attach a thread instrumentation to the running thread. In case of thread pools, this method should be called when a worker thread picks a work item and runs it. Also, this method should be called if the instrumented code does not keep the pointer returned by `new_thread()` and relies on `get_thread()` instead.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the thread instrumentation |
| `thread` |  | the thread instrumentation |

---

{#set_thread_peer_port_v1_t}

### set_thread_peer_port_v1_t

```cpp
using set_thread_peer_port_v1_t = void(*
```

Defined in psi/psi.h:1704

Assign the remote (peer) port to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | pointer to the thread instrumentation |
| `port` |  | the remote port |
| `thread` |  | pointer to the thread instrumentation |
| `port` |  | the remote port |

---

{#delete_current_thread_v1_t}

### delete_current_thread_v1_t

```cpp
using delete_current_thread_v1_t = void(*
```

Defined in psi/psi.h:1708

Delete the current thread instrumentation.

---

{#delete_thread_v1_t}

### delete_thread_v1_t

```cpp
using delete_thread_v1_t = void(*
```

Defined in psi/psi.h:1711

Delete a thread instrumentation.

---

{#get_thread_file_name_locker_v1_t}

### get_thread_file_name_locker_v1_t

```cpp
using get_thread_file_name_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1711

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

{#get_thread_file_stream_locker_v1_t}

### get_thread_file_stream_locker_v1_t

```cpp
using get_thread_file_stream_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1711

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

{#get_thread_file_descriptor_locker_v1_t}

### get_thread_file_descriptor_locker_v1_t

```cpp
using get_thread_file_descriptor_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1711

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

{#unlock_mutex_v1_t}

### unlock_mutex_v1_t

```cpp
using unlock_mutex_v1_t = void(*
```

Defined in psi/psi.h:1753

Record a mutex instrumentation unlock event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mutex` |  | the mutex instrumentation |
| `mutex` |  | the mutex instrumentation |

---

{#unlock_rwlock_v1_t}

### unlock_rwlock_v1_t

```cpp
using unlock_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1760

Record a rwlock instrumentation unlock event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `rwlock` |  | the rwlock instrumentation |
| `rwlock` |  | the rwlock instrumentation |

---

{#signal_cond_v1_t}

### signal_cond_v1_t

```cpp
using signal_cond_v1_t = void(*
```

Defined in psi/psi.h:1767

Record a condition instrumentation signal event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cond` |  | the cond instrumentation |
| `cond` |  | the cond instrumentation |

---

{#broadcast_cond_v1_t}

### broadcast_cond_v1_t

```cpp
using broadcast_cond_v1_t = void(*
```

Defined in psi/psi.h:1774

Record a condition instrumentation broadcast event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cond` |  | the cond instrumentation |
| `cond` |  | the cond instrumentation |

---

{#start_idle_wait_v1_t}

### start_idle_wait_v1_t

```cpp
using start_idle_wait_v1_t = struct PSI_idle_locker *(*
```

Defined in psi/psi.h:1774

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

{#end_idle_wait_v1_t}

### end_idle_wait_v1_t

```cpp
using end_idle_wait_v1_t = void(*
```

Defined in psi/psi.h:1791

Record an idle instrumentation wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `locker` |  | a thread locker for the running thread |

---

{#start_mutex_wait_v1_t}

### start_mutex_wait_v1_t

```cpp
using start_mutex_wait_v1_t = struct PSI_mutex_locker *(*
```

Defined in psi/psi.h:1791

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

{#end_mutex_wait_v1_t}

### end_mutex_wait_v1_t

```cpp
using end_mutex_wait_v1_t = void(*
```

Defined in psi/psi.h:1814

Record a mutex instrumentation wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

{#start_rwlock_rdwait_v1_t}

### start_rwlock_rdwait_v1_t

```cpp
using start_rwlock_rdwait_v1_t = struct PSI_rwlock_locker *(*
```

Defined in psi/psi.h:1814

Record a rwlock instrumentation read wait start event.

---

{#end_rwlock_rdwait_v1_t}

### end_rwlock_rdwait_v1_t

```cpp
using end_rwlock_rdwait_v1_t = void(*
```

Defined in psi/psi.h:1831

Record a rwlock instrumentation read wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

{#start_rwlock_wrwait_v1_t}

### start_rwlock_wrwait_v1_t

```cpp
using start_rwlock_wrwait_v1_t = struct PSI_rwlock_locker *(*
```

Defined in psi/psi.h:1831

Record a rwlock instrumentation write wait start event.

---

{#end_rwlock_wrwait_v1_t}

### end_rwlock_wrwait_v1_t

```cpp
using end_rwlock_wrwait_v1_t = void(*
```

Defined in psi/psi.h:1848

Record a rwlock instrumentation write wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

{#start_cond_wait_v1_t}

### start_cond_wait_v1_t

```cpp
using start_cond_wait_v1_t = struct PSI_cond_locker *(*
```

Defined in psi/psi.h:1848

Record a condition instrumentation wait start event.

---

{#end_cond_wait_v1_t}

### end_cond_wait_v1_t

```cpp
using end_cond_wait_v1_t = void(*
```

Defined in psi/psi.h:1866

Record a condition instrumentation wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

{#start_table_io_wait_v1_t}

### start_table_io_wait_v1_t

```cpp
using start_table_io_wait_v1_t = struct PSI_table_locker *(*
```

Defined in psi/psi.h:1866

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

{#end_table_io_wait_v1_t}

### end_table_io_wait_v1_t

```cpp
using end_table_io_wait_v1_t = void(*
```

Defined in psi/psi.h:1890

Record a table instrumentation io wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a table locker for the running thread |
| `numrows` |  | the number of rows involved in io |
| `locker` |  | a table locker for the running thread |
| `numrows` |  | the number of rows involved in io |

---

{#start_table_lock_wait_v1_t}

### start_table_lock_wait_v1_t

```cpp
using start_table_lock_wait_v1_t = struct PSI_table_locker *(*
```

Defined in psi/psi.h:1890

Record a table instrumentation lock wait start event.

---

{#end_table_lock_wait_v1_t}

### end_table_lock_wait_v1_t

```cpp
using end_table_lock_wait_v1_t = void(*
```

Defined in psi/psi.h:1908

Record a table instrumentation lock wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a table locker for the running thread |
| `locker` |  | a table locker for the running thread |

---

{#unlock_table_v1_t}

### unlock_table_v1_t

```cpp
using unlock_table_v1_t = void(*
```

Defined in psi/psi.h:1910

---

{#start_file_open_wait_v1_t}

### start_file_open_wait_v1_t

```cpp
using start_file_open_wait_v1_t = void(*
```

Defined in psi/psi.h:1918

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

{#end_file_open_wait_v1_t}

### end_file_open_wait_v1_t

```cpp
using end_file_open_wait_v1_t = struct PSI_file *(*
```

Defined in psi/psi.h:1918

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

{#end_file_open_wait_and_bind_to_descriptor_v1_t}

### end_file_open_wait_and_bind_to_descriptor_v1_t

```cpp
using end_file_open_wait_and_bind_to_descriptor_v1_t = void(*
```

Defined in psi/psi.h:1935

End a file instrumentation open operation, for non stream files.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |

---

{#end_temp_file_open_wait_and_bind_to_descriptor_v1_t}

### end_temp_file_open_wait_and_bind_to_descriptor_v1_t

```cpp
using end_temp_file_open_wait_and_bind_to_descriptor_v1_t = void(*
```

Defined in psi/psi.h:1944

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

{#start_file_wait_v1_t}

### start_file_wait_v1_t

```cpp
using start_file_wait_v1_t = void(*
```

Defined in psi/psi.h:1954

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

{#end_file_wait_v1_t}

### end_file_wait_v1_t

```cpp
using end_file_wait_v1_t = void(*
```

Defined in psi/psi.h:1970

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

{#start_file_close_wait_v1_t}

### start_file_close_wait_v1_t

```cpp
using start_file_close_wait_v1_t = void(*
```

Defined in psi/psi.h:1979

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

{#end_file_close_wait_v1_t}

### end_file_close_wait_v1_t

```cpp
using end_file_close_wait_v1_t = void(*
```

Defined in psi/psi.h:1988

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

{#end_file_rename_wait_v1_t}

### end_file_rename_wait_v1_t

```cpp
using end_file_rename_wait_v1_t = void(*
```

Defined in psi/psi.h:1998

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

{#start_stage_v1_t}

### start_stage_v1_t

```cpp
using start_stage_v1_t = PSI_stage_progress *(*
```

Defined in psi/psi.h:2009

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

{#get_current_stage_progress_v1_t}

### get_current_stage_progress_v1_t

```cpp
using get_current_stage_progress_v1_t = PSI_stage_progress *(*
```

Defined in psi/psi.h:2012

---

{#end_stage_v1_t}

### end_stage_v1_t

```cpp
using end_stage_v1_t = void(*
```

Defined in psi/psi.h:2015

End the current stage.

---

{#get_thread_statement_locker_v1_t}

### get_thread_statement_locker_v1_t

```cpp
using get_thread_statement_locker_v1_t = struct PSI_statement_locker *(*
```

Defined in psi/psi.h:2015

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

{#refine_statement_v1_t}

### refine_statement_v1_t

```cpp
using refine_statement_v1_t = struct PSI_statement_locker *(*
```

Defined in psi/psi.h:2015

Refine a statement locker to a more specific key. Note that only events declared mutable can be refined. **See also**: [PSI_FLAG_MUTABLE](#psi_flag_mutable)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | statement locker for the current event |
| `key` |  | the new key for the event |
| `locker` |  | statement locker for the current event |
| `key` |  | the new key for the event |

---

{#start_statement_v1_t}

### start_statement_v1_t

```cpp
using start_statement_v1_t = void(*
```

Defined in psi/psi.h:2048

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

{#set_statement_text_v1_t}

### set_statement_text_v1_t

```cpp
using set_statement_text_v1_t = void(*
```

Defined in psi/psi.h:2059

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

{#set_statement_lock_time_t}

### set_statement_lock_time_t

```cpp
using set_statement_lock_time_t = void(*
```

Defined in psi/psi.h:2068

Set a statement event lock time.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `lock_time` |  | the locked time, in microseconds |
| `locker` |  | the statement locker |
| `lock_time` |  | the locked time, in microseconds |

---

{#set_statement_rows_sent_t}

### set_statement_rows_sent_t

```cpp
using set_statement_rows_sent_t = void(*
```

Defined in psi/psi.h:2076

Set a statement event rows sent metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the number of rows sent |
| `locker` |  | the statement locker |
| `count` |  | the number of rows sent |

---

{#set_statement_rows_examined_t}

### set_statement_rows_examined_t

```cpp
using set_statement_rows_examined_t = void(*
```

Defined in psi/psi.h:2084

Set a statement event rows examined metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the number of rows examined |
| `locker` |  | the statement locker |
| `count` |  | the number of rows examined |

---

{#inc_statement_created_tmp_disk_tables_t}

### inc_statement_created_tmp_disk_tables_t

```cpp
using inc_statement_created_tmp_disk_tables_t = void(*
```

Defined in psi/psi.h:2092

Increment a statement event "created tmp disk tables" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_created_tmp_tables_t}

### inc_statement_created_tmp_tables_t

```cpp
using inc_statement_created_tmp_tables_t = void(*
```

Defined in psi/psi.h:2100

Increment a statement event "created tmp tables" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_full_join_t}

### inc_statement_select_full_join_t

```cpp
using inc_statement_select_full_join_t = void(*
```

Defined in psi/psi.h:2108

Increment a statement event "select full join" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_full_range_join_t}

### inc_statement_select_full_range_join_t

```cpp
using inc_statement_select_full_range_join_t = void(*
```

Defined in psi/psi.h:2116

Increment a statement event "select full range join" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_range_t}

### inc_statement_select_range_t

```cpp
using inc_statement_select_range_t = void(*
```

Defined in psi/psi.h:2124

Increment a statement event "select range join" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_range_check_t}

### inc_statement_select_range_check_t

```cpp
using inc_statement_select_range_check_t = void(*
```

Defined in psi/psi.h:2132

Increment a statement event "select range check" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_scan_t}

### inc_statement_select_scan_t

```cpp
using inc_statement_select_scan_t = void(*
```

Defined in psi/psi.h:2140

Increment a statement event "select scan" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_sort_merge_passes_t}

### inc_statement_sort_merge_passes_t

```cpp
using inc_statement_sort_merge_passes_t = void(*
```

Defined in psi/psi.h:2148

Increment a statement event "sort merge passes" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_sort_range_t}

### inc_statement_sort_range_t

```cpp
using inc_statement_sort_range_t = void(*
```

Defined in psi/psi.h:2156

Increment a statement event "sort range" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_sort_rows_t}

### inc_statement_sort_rows_t

```cpp
using inc_statement_sort_rows_t = void(*
```

Defined in psi/psi.h:2164

Increment a statement event "sort rows" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_sort_scan_t}

### inc_statement_sort_scan_t

```cpp
using inc_statement_sort_scan_t = void(*
```

Defined in psi/psi.h:2172

Increment a statement event "sort scan" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#set_statement_no_index_used_t}

### set_statement_no_index_used_t

```cpp
using set_statement_no_index_used_t = void(*
```

Defined in psi/psi.h:2179

Set a statement event "no index used" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `locker` |  | the statement locker |

---

{#set_statement_no_good_index_used_t}

### set_statement_no_good_index_used_t

```cpp
using set_statement_no_good_index_used_t = void(*
```

Defined in psi/psi.h:2186

Set a statement event "no good index used" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `locker` |  | the statement locker |

---

{#end_statement_v1_t}

### end_statement_v1_t

```cpp
using end_statement_v1_t = void(*
```

Defined in psi/psi.h:2195

End a statement event. **See also**: Diagnostics_area

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `stmt_da` |  | the statement diagnostics area. |
| `locker` |  | the statement locker |
| `stmt_da` |  | the statement diagnostics area. |

---

{#get_thread_transaction_locker_v1_t}

### get_thread_transaction_locker_v1_t

```cpp
using get_thread_transaction_locker_v1_t = struct PSI_transaction_locker *(*
```

Defined in psi/psi.h:2195

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

{#start_transaction_v1_t}

### start_transaction_v1_t

```cpp
using start_transaction_v1_t = void(*
```

Defined in psi/psi.h:2219

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

{#set_transaction_xid_v1_t}

### set_transaction_xid_v1_t

```cpp
using set_transaction_xid_v1_t = void(*
```

Defined in psi/psi.h:2229

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

{#set_transaction_xa_state_v1_t}

### set_transaction_xa_state_v1_t

```cpp
using set_transaction_xa_state_v1_t = void(*
```

Defined in psi/psi.h:2238

Set the state of the XA transaction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `xa_state` |  | the new state of the xa transaction |
| `locker` |  | the transaction locker for this event |
| `xa_state` |  | the new state of the xa transaction |

---

{#set_transaction_gtid_v1_t}

### set_transaction_gtid_v1_t

```cpp
using set_transaction_gtid_v1_t = void(*
```

Defined in psi/psi.h:2248

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

{#set_transaction_trxid_v1_t}

### set_transaction_trxid_v1_t

```cpp
using set_transaction_trxid_v1_t = void(*
```

Defined in psi/psi.h:2257

Set the transaction trx_id.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `trxid` |  | the storage engine transaction ID |
| `locker` |  | the transaction locker for this event |
| `trxid` |  | the storage engine transaction ID |

---

{#inc_transaction_savepoints_v1_t}

### inc_transaction_savepoints_v1_t

```cpp
using inc_transaction_savepoints_v1_t = void(*
```

Defined in psi/psi.h:2266

Increment a transaction event savepoint count.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker |
| `count` |  | the increment value |
| `locker` |  | the transaction locker |
| `count` |  | the increment value |

---

{#inc_transaction_rollback_to_savepoint_v1_t}

### inc_transaction_rollback_to_savepoint_v1_t

```cpp
using inc_transaction_rollback_to_savepoint_v1_t = void(*
```

Defined in psi/psi.h:2274

Increment a transaction event rollback to savepoint count.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker |
| `count` |  | the increment value |
| `locker` |  | the transaction locker |
| `count` |  | the increment value |

---

{#inc_transaction_release_savepoint_v1_t}

### inc_transaction_release_savepoint_v1_t

```cpp
using inc_transaction_release_savepoint_v1_t = void(*
```

Defined in psi/psi.h:2282

Increment a transaction event release savepoint count.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker |
| `count` |  | the increment value |
| `locker` |  | the transaction locker |
| `count` |  | the increment value |

---

{#end_transaction_v1_t}

### end_transaction_v1_t

```cpp
using end_transaction_v1_t = void(*
```

Defined in psi/psi.h:2290

Commit or rollback the transaction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `commit` |  | true if transaction was committed, false if rolled back |
| `locker` |  | the transaction locker for this event |
| `commit` |  | true if transaction was committed, false if rolled back |

---

{#start_socket_wait_v1_t}

### start_socket_wait_v1_t

```cpp
using start_socket_wait_v1_t = struct PSI_socket_locker *(*
```

Defined in psi/psi.h:2290

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

{#end_socket_wait_v1_t}

### end_socket_wait_v1_t

```cpp
using end_socket_wait_v1_t = void(*
```

Defined in psi/psi.h:2320

Record a socket instrumentation end event. Note that for socket close operations, the instrumented socket handle associated with the socket (which was provided to obtain a locker) is invalid after this call. **See also**: get_thread_socket_locker

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a socket locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |
| `locker` |  | a socket locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |

---

{#set_socket_state_v1_t}

### set_socket_state_v1_t

```cpp
using set_socket_state_v1_t = void(*
```

Defined in psi/psi.h:2328

Set the socket state for an instrumented socket.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | the instrumented socket |
| `state` |  | socket state |
| `socket` |  | the instrumented socket |
| `state` |  | socket state |

---

{#set_socket_info_v1_t}

### set_socket_info_v1_t

```cpp
using set_socket_info_v1_t = void(*
```

Defined in psi/psi.h:2338

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

{#set_socket_thread_owner_v1_t}

### set_socket_thread_owner_v1_t

```cpp
using set_socket_thread_owner_v1_t = void(*
```

Defined in psi/psi.h:2347

Bind a socket to the thread that owns it.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | instrumented socket |
| `socket` |  | instrumented socket |

---

{#create_prepared_stmt_v1_t}

### create_prepared_stmt_v1_t

```cpp
using create_prepared_stmt_v1_t = PSI_prepared_stmt *(*
```

Defined in psi/psi.h:2352

Get a prepare statement.

---

{#destroy_prepared_stmt_v1_t}

### destroy_prepared_stmt_v1_t

```cpp
using destroy_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2360

destroy a prepare statement.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prepared_stmt` |  | prepared statement. |
| `prepared_stmt` |  | prepared statement. |

---

{#reprepare_prepared_stmt_v1_t}

### reprepare_prepared_stmt_v1_t

```cpp
using reprepare_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2367

reprepare a prepare statement.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prepared_stmt` |  | prepared statement. |
| `prepared_stmt` |  | prepared statement. |

---

{#execute_prepared_stmt_v1_t}

### execute_prepared_stmt_v1_t

```cpp
using execute_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2375

Record a prepare statement instrumentation execute event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a statement locker for the running thread. |
| `prepared_stmt` |  | prepared statement. |
| `locker` |  | a statement locker for the running thread. |
| `prepared_stmt` |  | prepared statement. |

---

{#set_prepared_stmt_text_v1_t}

### set_prepared_stmt_text_v1_t

```cpp
using set_prepared_stmt_text_v1_t = void(*
```

Defined in psi/psi.h:2384

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

{#digest_start_v1_t}

### digest_start_v1_t

```cpp
using digest_start_v1_t = struct PSI_digest_locker *(*
```

Defined in psi/psi.h:2384

Get a digest locker for the current statement.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a statement locker for the running thread |
| `locker` |  | a statement locker for the running thread |

---

{#digest_end_v1_t}

### digest_end_v1_t

```cpp
using digest_end_v1_t = void(*
```

Defined in psi/psi.h:2399

Add a token to the current digest instrumentation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a digest locker for the current statement |
| `digest` |  | The digest storage to add the token to |
| `locker` |  | a digest locker for the current statement |
| `digest` |  | The digest storage to add the token to |

---

{#start_sp_v1_t}

### start_sp_v1_t

```cpp
using start_sp_v1_t = PSI_sp_locker *(*
```

Defined in psi/psi.h:2402

---

{#end_sp_v1_t}

### end_sp_v1_t

```cpp
using end_sp_v1_t = void(*
```

Defined in psi/psi.h:2405

---

{#drop_sp_v1_t}

### drop_sp_v1_t

```cpp
using drop_sp_v1_t = void(*
```

Defined in psi/psi.h:2408

---

{#get_sp_share_v1_t}

### get_sp_share_v1_t

```cpp
using get_sp_share_v1_t = struct PSI_sp_share *(*
```

Defined in psi/psi.h:2408

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

{#release_sp_share_v1_t}

### release_sp_share_v1_t

```cpp
using release_sp_share_v1_t = void(*
```

Defined in psi/psi.h:2431

Release a stored program share.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `share` |  | the stored program share to release |
| `share` |  | the stored program share to release |

---

{#create_metadata_lock_v1_t}

### create_metadata_lock_v1_t

```cpp
using create_metadata_lock_v1_t = PSI_metadata_lock *(*
```

Defined in psi/psi.h:2433

---

{#set_metadata_lock_status_v1_t}

### set_metadata_lock_status_v1_t

```cpp
using set_metadata_lock_status_v1_t = void(*
```

Defined in psi/psi.h:2442

---

{#destroy_metadata_lock_v1_t}

### destroy_metadata_lock_v1_t

```cpp
using destroy_metadata_lock_v1_t = void(*
```

Defined in psi/psi.h:2445

---

{#start_metadata_wait_v1_t}

### start_metadata_wait_v1_t

```cpp
using start_metadata_wait_v1_t = struct PSI_metadata_locker *(*
```

Defined in psi/psi.h:2445

---

{#end_metadata_wait_v1_t}

### end_metadata_wait_v1_t

```cpp
using end_metadata_wait_v1_t = void(*
```

Defined in psi/psi.h:2452

---

{#set_thread_connect_attrs_v1_t}

### set_thread_connect_attrs_v1_t

```cpp
using set_thread_connect_attrs_v1_t = int(*
```

Defined in psi/psi.h:2465

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

{#psi}

### PSI

```cpp
using PSI = struct PSI_v1
```

Type: struct [`PSI_v1`](Group_PSI_v1.md#psi_v1)

Defined in psi/psi.h:2930

The instrumentation interface for the current version. **See also**: PSI_CURRENT_VERSION

---

{#psi_mutex_info}

### PSI_mutex_info

```cpp
using PSI_mutex_info = struct PSI_mutex_info_v1
```

Type: struct [`PSI_mutex_info_v1`](Group_PSI_v1.md#psi_mutex_info_v1-1)

Defined in psi/psi.h:2931

The mutex information structure for the current version.

---

{#psi_rwlock_info}

### PSI_rwlock_info

```cpp
using PSI_rwlock_info = struct PSI_rwlock_info_v1
```

Type: struct [`PSI_rwlock_info_v1`](Group_PSI_v1.md#psi_rwlock_info_v1-1)

Defined in psi/psi.h:2932

The rwlock information structure for the current version.

---

{#psi_cond_info}

### PSI_cond_info

```cpp
using PSI_cond_info = struct PSI_cond_info_v1
```

Type: struct [`PSI_cond_info_v1`](Group_PSI_v1.md#psi_cond_info_v1-1)

Defined in psi/psi.h:2933

The cond information structure for the current version.

---

{#psi_thread_info}

### PSI_thread_info

```cpp
using PSI_thread_info = struct PSI_thread_info_v1
```

Type: struct [`PSI_thread_info_v1`](Group_PSI_v1.md#psi_thread_info_v1-1)

Defined in psi/psi.h:2934

The thread information structure for the current version.

---

{#psi_file_info}

### PSI_file_info

```cpp
using PSI_file_info = struct PSI_file_info_v1
```

Type: struct [`PSI_file_info_v1`](Group_PSI_v1.md#psi_file_info_v1-1)

Defined in psi/psi.h:2935

The file information structure for the current version.

---

{#psi_stage_info}

### PSI_stage_info

```cpp
using PSI_stage_info = struct PSI_stage_info_v1
```

Type: struct [`PSI_stage_info_v1`](Group_PSI_v1.md#psi_stage_info_v1-1)

Defined in psi/psi.h:2936

The stage instrumentation has to co exist with the legacy THD::set_proc_info instrumentation. To avoid duplication of the instrumentation in the server, the common PSI_stage_info structure is used, so we export it here, even when not building with HAVE_PSI_INTERFACE.

---

{#psi_statement_info}

### PSI_statement_info

```cpp
using PSI_statement_info = struct PSI_statement_info_v1
```

Type: struct [`PSI_statement_info_v1`](Group_PSI_v1.md#psi_statement_info_v1-1)

Defined in psi/psi.h:2937

---

{#psi_transaction_info}

### PSI_transaction_info

```cpp
using PSI_transaction_info = struct PSI_transaction_info_v1
```

Defined in psi/psi.h:2938

---

{#psi_socket_info}

### PSI_socket_info

```cpp
using PSI_socket_info = struct PSI_socket_info_v1
```

Type: struct [`PSI_socket_info_v1`](Group_PSI_v1.md#psi_socket_info_v1-1)

Defined in psi/psi.h:2939

---

{#psi_idle_locker_state}

### PSI_idle_locker_state

```cpp
using PSI_idle_locker_state = struct PSI_idle_locker_state_v1
```

Type: struct [`PSI_idle_locker_state_v1`](Group_PSI_v1.md#psi_idle_locker_state_v1-1)

Defined in psi/psi.h:2940

---

{#psi_mutex_locker_state}

### PSI_mutex_locker_state

```cpp
using PSI_mutex_locker_state = struct PSI_mutex_locker_state_v1
```

Type: struct [`PSI_mutex_locker_state_v1`](Group_PSI_v1.md#psi_mutex_locker_state_v1-1)

Defined in psi/psi.h:2941

---

{#psi_rwlock_locker_state}

### PSI_rwlock_locker_state

```cpp
using PSI_rwlock_locker_state = struct PSI_rwlock_locker_state_v1
```

Type: struct [`PSI_rwlock_locker_state_v1`](Group_PSI_v1.md#psi_rwlock_locker_state_v1-1)

Defined in psi/psi.h:2942

---

{#psi_cond_locker_state}

### PSI_cond_locker_state

```cpp
using PSI_cond_locker_state = struct PSI_cond_locker_state_v1
```

Type: struct [`PSI_cond_locker_state_v1`](Group_PSI_v1.md#psi_cond_locker_state_v1-1)

Defined in psi/psi.h:2943

---

{#psi_file_locker_state}

### PSI_file_locker_state

```cpp
using PSI_file_locker_state = struct PSI_file_locker_state_v1
```

Type: struct [`PSI_file_locker_state_v1`](Group_PSI_v1.md#psi_file_locker_state_v1-1)

Defined in psi/psi.h:2944

---

{#psi_statement_locker_state}

### PSI_statement_locker_state

```cpp
using PSI_statement_locker_state = struct PSI_statement_locker_state_v1
```

Type: struct [`PSI_statement_locker_state_v1`](Group_PSI_v1.md#psi_statement_locker_state_v1-1)

Defined in psi/psi.h:2945

---

{#psi_transaction_locker_state}

### PSI_transaction_locker_state

```cpp
using PSI_transaction_locker_state = struct PSI_transaction_locker_state_v1
```

Type: struct [`PSI_transaction_locker_state_v1`](Group_PSI_v1.md#psi_transaction_locker_state_v1-1)

Defined in psi/psi.h:2946

---

{#psi_socket_locker_state}

### PSI_socket_locker_state

```cpp
using PSI_socket_locker_state = struct PSI_socket_locker_state_v1
```

Type: struct [`PSI_socket_locker_state_v1`](Group_PSI_v1.md#psi_socket_locker_state_v1-1)

Defined in psi/psi.h:2947

---

{#psi_sp_locker_state}

### PSI_sp_locker_state

```cpp
using PSI_sp_locker_state = struct PSI_sp_locker_state_v1
```

Type: struct [`PSI_sp_locker_state_v1`](Group_PSI_v1.md#psi_sp_locker_state_v1-1)

Defined in psi/psi.h:2948

---

{#psi_metadata_locker_state}

### PSI_metadata_locker_state

```cpp
using PSI_metadata_locker_state = struct PSI_metadata_locker_state_v1
```

Type: struct [`PSI_metadata_locker_state_v1`](Group_PSI_v1.md#psi_metadata_locker_state_v1-1)

Defined in psi/psi.h:2949

---

{#psi_metadata_locker}

### PSI_metadata_locker

```cpp
using PSI_metadata_locker = struct PSI_stage_info_none
```

Type: struct [`PSI_stage_info_none`](Instrumentation_interface.md#psi_stage_info_none)

Defined in psi/psi.h:3015

---

{#mysql_thd}

### MYSQL_THD

```cpp
using MYSQL_THD = struct THD *
```

Type: struct [`THD`](#thd) *

Defined in plugin.h:54

---

{#my_bool}

### my_bool

```cpp
using my_bool = char
```

Defined in plugin.h:57

---

{#mysql_plugin}

### MYSQL_PLUGIN

```cpp
using MYSQL_PLUGIN = void *
```

Defined in plugin.h:58

---

{#mysql_xid}

### MYSQL_XID

```cpp
using MYSQL_XID = struct st_mysql_xid
```

Type: struct [`st_mysql_xid`](#st_mysql_xid)

Defined in plugin.h:77

---

{#mysql_show_var_func}

### mysql_show_var_func

```cpp
using mysql_show_var_func = int(*
```

Defined in plugin.h:215

---

{#mysql_var_check_func}

### mysql_var_check_func

```cpp
using mysql_var_check_func = int(*
```

Defined in plugin.h:284

SYNOPSIS (*mysql_var_check_func)() thd thread handle var dynamic variable being altered save pointer to temporary storage value user provided value RETURN 0 user provided value is OK and the update func may be called. any other value indicates error.

This function should parse the user provided value and store in the provided temporary storage any data as required by the update func. There is sufficient space in the temporary storage to store a double. Note that the update func may not be called if any other error occurs so any memory allocated should be thread-local so that it may be freed automatically at the end of the statement.

---

{#mysql_var_update_func}

### mysql_var_update_func

```cpp
using mysql_var_update_func = void(*
```

Defined in plugin.h:302

SYNOPSIS (*mysql_var_update_func)() thd thread handle var dynamic variable being altered var_ptr pointer to dynamic variable save pointer to temporary storage RETURN NONE

This function should use the validated value stored in the temporary store and persist it in the provided pointer to the dynamic variable. For example, strings may require memory to be allocated.

---

{#psi_memory_key}

### PSI_memory_key

```cpp
using PSI_memory_key = unsigned int
```

Defined in psi/psi_base.h:177

Instrumented memory key. To instrument memory, a memory key must be obtained using `register_memory`. Using a zero key always disable the instrumentation.

---

{#mysql_file}

### MYSQL_FILE

```cpp
using MYSQL_FILE = struct st_mysql_file
```

Type: struct [`st_mysql_file`](File_instrumentation.md#st_mysql_file)

Defined in psi/mysql_file.h:515

Type of an instrumented file. `MYSQL_FILE` is a drop-in replacement for `FILE`. **See also**: [mysql_file_open](#mysql_file_open)

---

{#psi_memory_info_v1}

### PSI_memory_info_v1

```cpp
using PSI_memory_info_v1 = struct PSI_memory_info_v1
```

Type: struct [`PSI_memory_info_v1`](Group_PSI_v1.md#psi_memory_info_v1-1)

Defined in psi/psi_memory.h:80

---

{#register_memory_v1_t}

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

{#memory_alloc_v1_t}

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

{#memory_realloc_v1_t}

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

{#memory_claim_v1_t}

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

{#memory_free_v1_t}

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

{#psi_memory_info}

### PSI_memory_info

```cpp
using PSI_memory_info = struct PSI_memory_info_v1
```

Type: struct [`PSI_memory_info_v1`](Group_PSI_v1.md#psi_memory_info_v1-1)

Defined in psi/psi_memory.h:148

---

{#mysql_server_auth_info}

### MYSQL_SERVER_AUTH_INFO

```cpp
using MYSQL_SERVER_AUTH_INFO = struct st_mysql_server_auth_info
```

Type: struct [`st_mysql_server_auth_info`](#st_mysql_server_auth_info)

Defined in plugin_auth.h:114

Provides server plugin access to authentication information

---

{#mysql_socket}

### MYSQL_SOCKET

```cpp
using MYSQL_SOCKET = struct st_mysql_socket
```

Type: struct [`st_mysql_socket`](Socket_instrumentation.md#st_mysql_socket)

Defined in psi/mysql_socket.h:99

An instrumented socket. `MYSQL_SOCKET` is a replacement for `my_socket`.

---

{#mysql_mutex_t}

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

{#mysql_rwlock_t}

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

{#mysql_prlock_t}

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

{#mysql_cond_t}

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

{#query_id_t}

### query_id_t

```cpp
using query_id_t = int64
```

Defined in service_wsrep.h:53

---

{#logger_handle}

### LOGGER_HANDLE

```cpp
using LOGGER_HANDLE = struct logger_handle_st
```

Defined in service_logger.h:61

---

{#mysql_ftparser_boolean_info}

### MYSQL_FTPARSER_BOOLEAN_INFO

```cpp
using MYSQL_FTPARSER_BOOLEAN_INFO = struct st_mysql_ftparser_boolean_info
```

Type: struct [`st_mysql_ftparser_boolean_info`](#st_mysql_ftparser_boolean_info)

Defined in plugin_ftparser.h:130

---

{#mysql_ftparser_param}

### MYSQL_FTPARSER_PARAM

```cpp
using MYSQL_FTPARSER_PARAM = struct st_mysql_ftparser_param
```

Type: struct [`st_mysql_ftparser_param`](#st_mysql_ftparser_param)

Defined in plugin_ftparser.h:198

---

{#charset_info}

### CHARSET_INFO

```cpp
using CHARSET_INFO = const struct charset_info_st
```

Defined in psi/mysql_statement.h:35

---

{#thd_wait_type}

### thd_wait_type

```cpp
using thd_wait_type = enum _thd_wait_type_e
```

Type: enum [`_thd_wait_type_e`](#_thd_wait_type_e)

Defined in service_thd_wait.h:79

---

{#mysql_const_lex_string}

### MYSQL_CONST_LEX_STRING

```cpp
using MYSQL_CONST_LEX_STRING = struct st_mysql_const_lex_string
```

Type: struct [`st_mysql_const_lex_string`](#st_mysql_const_lex_string)

Defined in service_thd_alloc.h:43

---

{#mysql_lex_string}

### MYSQL_LEX_STRING

```cpp
using MYSQL_LEX_STRING = struct st_mysql_lex_string
```

Type: struct [`st_mysql_lex_string`](#st_mysql_lex_string)

Defined in service_thd_alloc.h:57

---

{#mysql_authentication_dialog_ask_t}

### mysql_authentication_dialog_ask_t

```cpp
using mysql_authentication_dialog_ask_t = char *(*
```

Defined in auth_dialog_client.h:43

type of the mysql_authentication_dialog_ask function

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
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

{#mysql_plugin_vio_info}

### MYSQL_PLUGIN_VIO_INFO

```cpp
using MYSQL_PLUGIN_VIO_INFO = struct st_plugin_vio_info
```

Type: struct [`st_plugin_vio_info`](#st_plugin_vio_info)

Defined in plugin_auth_common.h:102

---

{#mysql_plugin_vio}

### MYSQL_PLUGIN_VIO

```cpp
using MYSQL_PLUGIN_VIO = struct st_plugin_vio
```

Type: struct [`st_plugin_vio`](#st_plugin_vio)

Defined in plugin_auth_common.h:131

Provides plugin access to communication channel

---

{#mysql_thd_key_t}

### MYSQL_THD_KEY_T

```cpp
using MYSQL_THD_KEY_T = int
```

Defined in service_thd_specifics.h:60

## Functions

---

{#show_func_entry}

### SHOW_FUNC_ENTRY

`static` `inline`

```cpp
static inline struct st_mysql_show_var SHOW_FUNC_ENTRY(const char * name, mysql_show_var_func func_arg)
```

Defined in plugin.h:219

---

{#thd_in_lock_tables}

### thd_in_lock_tables

```cpp
int thd_in_lock_tables(const MYSQL_THD thd)
```

Defined in plugin.h:696

---

{#thd_tablespace_op}

### thd_tablespace_op

```cpp
int thd_tablespace_op(const MYSQL_THD thd)
```

Defined in plugin.h:697

---

{#thd_test_options}

### thd_test_options

```cpp
long long thd_test_options(const MYSQL_THD thd, long long test_options)
```

Defined in plugin.h:698

---

{#thd_sql_command}

### thd_sql_command

```cpp
int thd_sql_command(const MYSQL_THD thd)
```

Defined in plugin.h:699

---

{#thd_ddl_options}

### thd_ddl_options

```cpp
struct DDL_options_st * thd_ddl_options(const MYSQL_THD thd)
```

Defined in plugin.h:701

---

{#thd_storage_lock_wait}

### thd_storage_lock_wait

```cpp
void thd_storage_lock_wait(MYSQL_THD thd, long long value)
```

Defined in plugin.h:702

---

{#thd_tx_isolation}

### thd_tx_isolation

```cpp
int thd_tx_isolation(const MYSQL_THD thd)
```

Defined in plugin.h:703

---

{#thd_tx_is_read_only}

### thd_tx_is_read_only

```cpp
int thd_tx_is_read_only(const MYSQL_THD thd)
```

Defined in plugin.h:704

---

{#mysql_tmpfile}

### mysql_tmpfile

```cpp
int mysql_tmpfile(const char * prefix)
```

Defined in plugin.h:718

Create a temporary file.

The temporary file is created in a location specified by the mysql server configuration (&ndash;tmpdir option). The caller does not need to delete the file, it will be deleted automatically.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prefix` | `const char *` | prefix for temporary file name |

#### Return Values

| Value | Description |
|-------|-------------|
| `-1` | error |
| `>=` | 0 a file handle that can be passed to dup or my_close |

---

{#thd_get_thread_id}

### thd_get_thread_id

```cpp
unsigned long thd_get_thread_id(const MYSQL_THD thd)
```

Defined in plugin.h:726

Return the thread id of a user thread

#### Returns
thread id

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |

---

{#thd_get_xid}

### thd_get_xid

```cpp
void thd_get_xid(const MYSQL_THD thd, MYSQL_XID * xid)
```

Defined in plugin.h:734

Get the XID for this connection's transaction

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |
| `xid` | [`MYSQL_XID`](#mysql_xid) * | location where identifier is stored |

---

{#mysql_query_cache_invalidate4}

### mysql_query_cache_invalidate4

```cpp
void mysql_query_cache_invalidate4(MYSQL_THD thd, const char * key, unsigned int key_length, int using_trx)
```

Defined in plugin.h:744

Invalidate the query cache for a given table.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | [`MYSQL_THD`](#mysql_thd) | user thread connection handle |
| `key` | `const char *` | databasename\0tablename\0 |
| `key_length` | `unsigned int` | length of key in bytes, including the NUL bytes |
| `using_trx` | `int` | flag: TRUE if using transactions, FALSE otherwise |

---

{#thd_get_ha_data}

### thd_get_ha_data

```cpp
void * thd_get_ha_data(const MYSQL_THD thd, const struct transaction_participant * hton)
```

Defined in plugin.h:752

Provide a handler data getter to simplify coding

---

{#thd_set_ha_data}

### thd_set_ha_data

```cpp
void thd_set_ha_data(MYSQL_THD thd, const struct transaction_participant * hton, const void * ha_data)
```

Defined in plugin.h:776

Provide a handler data setter to simplify coding

Set ha_data pointer (storage engine per-connection information).

To avoid unclean deactivation (uninstall) of storage engine plugin in the middle of transaction, additional storage engine plugin lock is acquired.

If ha_data is not null and storage engine plugin was not locked by [thd_set_ha_data()](#thd_set_ha_data) in this connection before, storage engine plugin gets locked.

If ha_data is null and storage engine plugin was locked by [thd_set_ha_data()](#thd_set_ha_data) in this connection before, storage engine plugin lock gets released.

If transaction_participant::close_connection() didn't reset ha_data, server does it immediately after calling transaction_participant::close_connection()

---

{#thd_wakeup_subsequent_commits}

### thd_wakeup_subsequent_commits

```cpp
void thd_wakeup_subsequent_commits(MYSQL_THD thd, int wakeup_error)
```

Defined in plugin.h:811

Signal that the first part of handler commit is finished, and that the committed transaction is now visible and has fixed commit ordering with respect to other transactions. The commit need *not* be durable yet, and typically will not be when this call makes sense.

This call is optional, if the storage engine does not call it the upper layer will after the handler commit() method is done. However, the storage engine may choose to call it itself to increase the possibility for group commit.

In-order parallel replication uses this to apply different transaction in parallel, but delay the commits of later transactions until earlier transactions have committed first, thus achieving increased performance on multi-core systems while still preserving full transaction consistency.

The storage engine can call this from within the commit() method, typically after the commit record has been written to the transaction log, but before the log has been fsync()'ed. This will allow the next replicated transaction to proceed to commit before the first one has done fsync() or similar. Thus, it becomes possible for multiple sequential replicated transactions to share a single fsync() inside the engine in group commit.

Note that this method should *not* be called from within the commit_ordered() method, or any other place in the storage engine. When commit_ordered() is used (typically when binlog is enabled), the transaction coordinator takes care of this and makes group commit in the storage engine possible without any other action needed on the part of the storage engine. This function [thd_wakeup_subsequent_commits()](#thd_wakeup_subsequent_commits) is only needed when no transaction coordinator is used, meaning a single storage engine and no binary log.

---

{#inline_mysql_file_register}

### inline_mysql_file_register

`static` `inline`

```cpp
static inline void inline_mysql_file_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_file.h:517

---

{#inline_mysql_file_fgets}

### inline_mysql_file_fgets

`static` `inline`

```cpp
static inline char * inline_mysql_file_fgets(char * str, int size, MYSQL_FILE * file, char * str, int size, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:535

---

{#inline_mysql_file_fgetc}

### inline_mysql_file_fgetc

`static` `inline`

```cpp
static inline int inline_mysql_file_fgetc(MYSQL_FILE * file, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:563

---

{#inline_mysql_file_fputs}

### inline_mysql_file_fputs

`static` `inline`

```cpp
static inline int inline_mysql_file_fputs(const char * str, MYSQL_FILE * file, const char * str, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:591

---

{#inline_mysql_file_fputc}

### inline_mysql_file_fputc

`static` `inline`

```cpp
static inline int inline_mysql_file_fputc(char c, MYSQL_FILE * file, char c, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:621

---

{#inline_mysql_file_fprintf}

### inline_mysql_file_fprintf

`static` `inline`

```cpp
static inline int inline_mysql_file_fprintf(MYSQL_FILE * file, const char * format, ..., MYSQL_FILE * file, const char * format, ...)
```

Defined in psi/mysql_file.h:649

---

{#inline_mysql_file_vfprintf}

### inline_mysql_file_vfprintf

`static` `inline`

```cpp
static inline int inline_mysql_file_vfprintf(MYSQL_FILE * file, const char * format, va_list args, MYSQL_FILE * file, const char * format, va_list args)
```

Defined in psi/mysql_file.h:681

---

{#inline_mysql_file_fflush}

### inline_mysql_file_fflush

`static` `inline`

```cpp
static inline int inline_mysql_file_fflush(MYSQL_FILE * file, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:709

---

{#inline_mysql_file_feof}

### inline_mysql_file_feof

`static` `inline`

```cpp
static inline int inline_mysql_file_feof(MYSQL_FILE * file, MYSQL_FILE * file)
```

Defined in psi/mysql_file.h:736

---

{#inline_mysql_file_fstat}

### inline_mysql_file_fstat

`static` `inline`

```cpp
static inline int inline_mysql_file_fstat(int filenr, MY_STAT * stat_area, myf flags, int filenr, MY_STAT * stat_area, myf flags)
```

Defined in psi/mysql_file.h:743

---

{#inline_mysql_file_stat}

### inline_mysql_file_stat

`static` `inline`

```cpp
static inline MY_STAT * inline_mysql_file_stat(const char * path, MY_STAT * stat_area, myf flags, const char * path, MY_STAT * stat_area, myf flags)
```

Defined in psi/mysql_file.h:768

---

{#inline_mysql_file_chsize}

### inline_mysql_file_chsize

`static` `inline`

```cpp
static inline int inline_mysql_file_chsize(File file, my_off_t newlength, int filler, myf flags, File file, my_off_t newlength, int filler, myf flags)
```

Defined in psi/mysql_file.h:793

---

{#inline_mysql_file_fopen}

### inline_mysql_file_fopen

`static` `inline`

```cpp
static inline MYSQL_FILE * inline_mysql_file_fopen(const char * filename, int flags, myf myFlags, const char * filename, int flags, myf myFlags)
```

Defined in psi/mysql_file.h:819

---

{#inline_mysql_file_fclose}

### inline_mysql_file_fclose

`static` `inline`

```cpp
static inline int inline_mysql_file_fclose(MYSQL_FILE * file, myf flags, MYSQL_FILE * file, myf flags)
```

Defined in psi/mysql_file.h:861

---

{#inline_mysql_file_fread}

### inline_mysql_file_fread

`static` `inline`

```cpp
static inline size_t inline_mysql_file_fread(MYSQL_FILE * file, uchar * buffer, size_t count, myf flags, MYSQL_FILE * file, uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql_file.h:895

---

{#inline_mysql_file_fwrite}

### inline_mysql_file_fwrite

`static` `inline`

```cpp
static inline size_t inline_mysql_file_fwrite(MYSQL_FILE * file, const uchar * buffer, size_t count, myf flags, MYSQL_FILE * file, const uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql_file.h:928

---

{#inline_mysql_file_fseek}

### inline_mysql_file_fseek

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_fseek(MYSQL_FILE * file, my_off_t pos, int whence, myf flags, MYSQL_FILE * file, my_off_t pos, int whence, myf flags)
```

Defined in psi/mysql_file.h:961

---

{#inline_mysql_file_ftell}

### inline_mysql_file_ftell

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_ftell(MYSQL_FILE * file, myf flags, MYSQL_FILE * file, myf flags)
```

Defined in psi/mysql_file.h:989

---

{#inline_mysql_file_create}

### inline_mysql_file_create

`static` `inline`

```cpp
static inline File inline_mysql_file_create(const char * filename, mode_t create_flags, int access_flags, myf myFlags, const char * filename, mode_t create_flags, int access_flags, myf myFlags)
```

Defined in psi/mysql_file.h:1017

---

{#inline_mysql_file_create_temp}

### inline_mysql_file_create_temp

`static` `inline`

```cpp
static inline File inline_mysql_file_create_temp(char * to, const char * dir, const char * pfx, int mode, myf myFlags, char * to, const char * dir, const char * pfx, int mode, myf myFlags)
```

Defined in psi/mysql_file.h:1043

---

{#inline_mysql_file_open}

### inline_mysql_file_open

`static` `inline`

```cpp
static inline File inline_mysql_file_open(const char * filename, int flags, myf myFlags, const char * filename, int flags, myf myFlags)
```

Defined in psi/mysql_file.h:1070

---

{#inline_mysql_file_close}

### inline_mysql_file_close

`static` `inline`

```cpp
static inline int inline_mysql_file_close(File file, myf flags, File file, myf flags)
```

Defined in psi/mysql_file.h:1096

---

{#inline_mysql_file_read}

### inline_mysql_file_read

`static` `inline`

```cpp
static inline size_t inline_mysql_file_read(File file, uchar * buffer, size_t count, myf flags, File file, uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql_file.h:1121

---

{#inline_mysql_file_write}

### inline_mysql_file_write

`static` `inline`

```cpp
static inline size_t inline_mysql_file_write(File file, const uchar * buffer, size_t count, myf flags, File file, const uchar * buffer, size_t count, myf flags)
```

Defined in psi/mysql_file.h:1151

---

{#inline_mysql_file_pread}

### inline_mysql_file_pread

`static` `inline`

```cpp
static inline size_t inline_mysql_file_pread(File file, uchar * buffer, size_t count, my_off_t offset, myf flags, File file, uchar * buffer, size_t count, my_off_t offset, myf flags)
```

Defined in psi/mysql_file.h:1181

---

{#inline_mysql_file_pwrite}

### inline_mysql_file_pwrite

`static` `inline`

```cpp
static inline size_t inline_mysql_file_pwrite(File file, const uchar * buffer, size_t count, my_off_t offset, myf flags, File file, const uchar * buffer, size_t count, my_off_t offset, myf flags)
```

Defined in psi/mysql_file.h:1211

---

{#inline_mysql_file_seek}

### inline_mysql_file_seek

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_seek(File file, my_off_t pos, int whence, myf flags, File file, my_off_t pos, int whence, myf flags)
```

Defined in psi/mysql_file.h:1241

---

{#inline_mysql_file_tell}

### inline_mysql_file_tell

`static` `inline`

```cpp
static inline my_off_t inline_mysql_file_tell(File file, myf flags, File file, myf flags)
```

Defined in psi/mysql_file.h:1266

---

{#inline_mysql_file_delete}

### inline_mysql_file_delete

`static` `inline`

```cpp
static inline int inline_mysql_file_delete(const char * name, myf flags, const char * name, myf flags)
```

Defined in psi/mysql_file.h:1291

---

{#inline_mysql_file_rename}

### inline_mysql_file_rename

`static` `inline`

```cpp
static inline int inline_mysql_file_rename(const char * from, const char * to, myf flags, const char * from, const char * to, myf flags)
```

Defined in psi/mysql_file.h:1316

---

{#inline_mysql_file_create_with_symlink}

### inline_mysql_file_create_with_symlink

`static` `inline`

```cpp
static inline File inline_mysql_file_create_with_symlink(const char * linkname, const char * filename, mode_t create_flags, int access_flags, myf flags, const char * linkname, const char * filename, mode_t create_flags, int access_flags, myf flags)
```

Defined in psi/mysql_file.h:1343

---

{#inline_mysql_file_delete_with_symlink}

### inline_mysql_file_delete_with_symlink

`static` `inline`

```cpp
static inline int inline_mysql_file_delete_with_symlink(const char * name, const char * ext, myf flags, const char * name, const char * ext, myf flags)
```

Defined in psi/mysql_file.h:1373

---

{#inline_mysql_file_rename_with_symlink}

### inline_mysql_file_rename_with_symlink

`static` `inline`

```cpp
static inline int inline_mysql_file_rename_with_symlink(const char * from, const char * to, myf flags, const char * from, const char * to, myf flags)
```

Defined in psi/mysql_file.h:1402

---

{#inline_mysql_file_sync}

### inline_mysql_file_sync

`static` `inline`

```cpp
static inline int inline_mysql_file_sync(File fd, myf flags, File fd, myf flags)
```

Defined in psi/mysql_file.h:1428

---

{#my_md5}

### my_md5

```cpp
void my_md5(unsigned char *, const char *, size_t)
```

Defined in service_md5.h:54

---

{#my_md5_multi}

### my_md5_multi

```cpp
void my_md5_multi(unsigned char *, ...)
```

Defined in service_md5.h:55

---

{#my_md5_context_size}

### my_md5_context_size

```cpp
size_t my_md5_context_size()
```

Defined in service_md5.h:56

---

{#my_md5_init}

### my_md5_init

```cpp
void my_md5_init(void * context)
```

Defined in service_md5.h:57

---

{#my_md5_input}

### my_md5_input

```cpp
void my_md5_input(void * context, const unsigned char * buf, size_t len)
```

Defined in service_md5.h:58

---

{#my_md5_result}

### my_md5_result

```cpp
void my_md5_result(void * context, unsigned char * digest)
```

Defined in service_md5.h:59

---

{#mysql_real_connect_local}

### mysql_real_connect_local

```cpp
MYSQL * mysql_real_connect_local(MYSQL * mysql)
```

Defined in service_sql.h:112

---

{#get_current_thd}

### get_current_thd

```cpp
MYSQL_THD get_current_thd()
```

Defined in service_thd.h:38

current thd accessor 
#### Returns
pointer to current thd

---

{#inline_mysql_memory_register}

### inline_mysql_memory_register

`static` `inline`

```cpp
static inline void inline_mysql_memory_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_memory.h:62

---

{#mysql_socket_invalid}

### mysql_socket_invalid

`static` `inline`

```cpp
static inline MYSQL_SOCKET mysql_socket_invalid()
```

Defined in psi/mysql_socket.h:115

MYSQL_SOCKET helper. Initialize instrumented socket. **See also**: mysql_socket_getfd 

**See also**: mysql_socket_setfd

---

{#mysql_socket_set_address}

### mysql_socket_set_address

`static` `inline`

```cpp
static inline void mysql_socket_set_address(MYSQL_SOCKET socket, const struct sockaddr * addr, socklen_t addr_len, MYSQL_SOCKET socket, const struct sockaddr * addr, socklen_t addr_len)
```

Defined in psi/mysql_socket.h:130

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

{#mysql_socket_set_thread_owner}

### mysql_socket_set_thread_owner

`static` `inline`

```cpp
static inline void mysql_socket_set_thread_owner(MYSQL_SOCKET socket, MYSQL_SOCKET socket)
```

Defined in psi/mysql_socket.h:153

Set socket descriptor and address.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | instrumented socket |
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | instrumented socket |

---

{#mysql_socket_getfd}

### mysql_socket_getfd

`static` `inline`

```cpp
static inline my_socket mysql_socket_getfd(MYSQL_SOCKET mysql_socket, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql_socket.h:173

MYSQL_SOCKET helper. Get socket descriptor. **See also**: mysql_socket_getfd

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql_socket` | [`MYSQL_SOCKET`](#mysql_socket) | Instrumented socket |
| `mysql_socket` | [`MYSQL_SOCKET`](#mysql_socket) | Instrumented socket |

---

{#mysql_socket_setfd}

### mysql_socket_setfd

`static` `inline`

```cpp
static inline void mysql_socket_setfd(MYSQL_SOCKET * mysql_socket, my_socket fd, MYSQL_SOCKET * mysql_socket, my_socket fd)
```

Defined in psi/mysql_socket.h:185

MYSQL_SOCKET helper. Set socket descriptor. **See also**: mysql_socket_setfd

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql_socket` | [`MYSQL_SOCKET`](#mysql_socket) * | Instrumented socket |
| `fd` | `my_socket` | Socket descriptor |
| `mysql_socket` | [`MYSQL_SOCKET`](#mysql_socket) * | Instrumented socket |
| `fd` | `my_socket` | Socket descriptor |

---

{#inline_mysql_start_socket_wait}

### inline_mysql_start_socket_wait

`static` `inline`

```cpp
static inline struct PSI_socket_locker * inline_mysql_start_socket_wait(PSI_socket_locker_state * state, MYSQL_SOCKET mysql_socket, enum PSI_socket_operation op, size_t byte_count, const char * src_file, uint src_line, PSI_socket_locker_state * state, MYSQL_SOCKET mysql_socket, enum PSI_socket_operation op, size_t byte_count, const char * src_file, uint src_line)
```

Defined in psi/mysql_socket.h:266

Instrumentation calls for MYSQL_START_SOCKET_WAIT. **See also**: [MYSQL_START_SOCKET_WAIT](#mysql_start_socket_wait).

---

{#inline_mysql_end_socket_wait}

### inline_mysql_end_socket_wait

`static` `inline`

```cpp
static inline void inline_mysql_end_socket_wait(struct PSI_socket_locker * locker, size_t byte_count, struct PSI_socket_locker * locker, size_t byte_count)
```

Defined in psi/mysql_socket.h:288

Instrumentation calls for MYSQL_END_SOCKET_WAIT. **See also**: [MYSQL_END_SOCKET_WAIT](#mysql_end_socket_wait).

---

{#inline_mysql_socket_set_state}

### inline_mysql_socket_set_state

`static` `inline`

```cpp
static inline void inline_mysql_socket_set_state(MYSQL_SOCKET socket, enum PSI_socket_state state, MYSQL_SOCKET socket, enum PSI_socket_state state)
```

Defined in psi/mysql_socket.h:301

Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI_socket_state

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | the instrumented socket |
| `state` | `enum PSI_socket_state` | the new state |
| `socket` | [`MYSQL_SOCKET`](#mysql_socket) | the instrumented socket |
| `state` | `enum PSI_socket_state` | the new state |

---

{#inline_mysql_socket_register}

### inline_mysql_socket_register

`static` `inline`

```cpp
static inline void inline_mysql_socket_register(const char * category, PSI_socket_info * info, int count, const char * category, PSI_socket_info * info, int count)
```

Defined in psi/mysql_socket.h:589

---

{#inline_mysql_socket_fd}

### inline_mysql_socket_fd

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_fd(PSI_socket_key key, int fd, PSI_socket_key key, int fd)
```

Defined in psi/mysql_socket.h:601

mysql_socket_fd

---

{#inline_mysql_socket_socket}

### inline_mysql_socket_socket

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_socket(PSI_socket_key key, int domain, int type, int protocol, PSI_socket_key key, int domain, int type, int protocol)
```

Defined in psi/mysql_socket.h:634

mysql_socket_socket

---

{#inline_mysql_socket_bind}

### inline_mysql_socket_bind

`static` `inline`

```cpp
static inline int inline_mysql_socket_bind(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, size_t len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, size_t len)
```

Defined in psi/mysql_socket.h:663

mysql_socket_bind

---

{#inline_mysql_socket_getsockname}

### inline_mysql_socket_getsockname

`static` `inline`

```cpp
static inline int inline_mysql_socket_getsockname(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len)
```

Defined in psi/mysql_socket.h:703

mysql_socket_getsockname

---

{#inline_mysql_socket_connect}

### inline_mysql_socket_connect

`static` `inline`

```cpp
static inline int inline_mysql_socket_connect(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, socklen_t len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, socklen_t len)
```

Defined in psi/mysql_socket.h:741

mysql_socket_connect

---

{#inline_mysql_socket_getpeername}

### inline_mysql_socket_getpeername

`static` `inline`

```cpp
static inline int inline_mysql_socket_getpeername(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len)
```

Defined in psi/mysql_socket.h:779

mysql_socket_getpeername

---

{#inline_mysql_socket_send}

### inline_mysql_socket_send

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_send(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags)
```

Defined in psi/mysql_socket.h:817

mysql_socket_send

---

{#inline_mysql_socket_recv}

### inline_mysql_socket_recv

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_recv(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags)
```

Defined in psi/mysql_socket.h:858

mysql_socket_recv

---

{#inline_mysql_socket_sendto}

### inline_mysql_socket_sendto

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_sendto(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const struct sockaddr * addr, socklen_t addr_len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const struct sockaddr * addr, socklen_t addr_len)
```

Defined in psi/mysql_socket.h:899

mysql_socket_sendto

---

{#inline_mysql_socket_recvfrom}

### inline_mysql_socket_recvfrom

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_recvfrom(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, struct sockaddr * addr, socklen_t * addr_len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, struct sockaddr * addr, socklen_t * addr_len)
```

Defined in psi/mysql_socket.h:940

mysql_socket_recvfrom

---

{#inline_mysql_socket_getsockopt}

### inline_mysql_socket_getsockopt

`static` `inline`

```cpp
static inline int inline_mysql_socket_getsockopt(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, SOCKBUF_T * optval, socklen_t * optlen, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, SOCKBUF_T * optval, socklen_t * optlen)
```

Defined in psi/mysql_socket.h:982

mysql_socket_getsockopt

---

{#inline_mysql_socket_setsockopt}

### inline_mysql_socket_setsockopt

`static` `inline`

```cpp
static inline int inline_mysql_socket_setsockopt(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, const SOCKBUF_T * optval, socklen_t optlen, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, const SOCKBUF_T * optval, socklen_t optlen)
```

Defined in psi/mysql_socket.h:1020

mysql_socket_setsockopt

---

{#set_socket_nonblock}

### set_socket_nonblock

`static` `inline`

```cpp
static inline int set_socket_nonblock(my_socket fd, my_socket fd)
```

Defined in psi/mysql_socket.h:1058

set_socket_nonblock

---

{#inline_mysql_sock_set_nonblocking}

### inline_mysql_sock_set_nonblocking

`static` `inline`

```cpp
static inline int inline_mysql_sock_set_nonblocking(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql_socket.h:1091

mysql_socket_set_nonblocking

---

{#inline_mysql_socket_listen}

### inline_mysql_socket_listen

`static` `inline`

```cpp
static inline int inline_mysql_socket_listen(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int backlog, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int backlog)
```

Defined in psi/mysql_socket.h:1131

mysql_socket_listen

---

{#inline_mysql_socket_accept}

### inline_mysql_socket_accept

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_accept(const char * src_file, uint src_line, PSI_socket_key key, MYSQL_SOCKET socket_listen, struct sockaddr * addr, socklen_t * addr_len, const char * src_file, uint src_line, PSI_socket_key key, MYSQL_SOCKET socket_listen, struct sockaddr * addr, socklen_t * addr_len)
```

Defined in psi/mysql_socket.h:1169

mysql_socket_accept

---

{#inline_mysql_socket_close}

### inline_mysql_socket_close

`static` `inline`

```cpp
static inline int inline_mysql_socket_close(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql_socket.h:1250

mysql_socket_close

---

{#inline_mysql_socket_shutdown}

### inline_mysql_socket_shutdown

`static` `inline`

```cpp
static inline int inline_mysql_socket_shutdown(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int how, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int how)
```

Defined in psi/mysql_socket.h:1291

mysql_socket_shutdown

---

{#inline_mysql_mutex_register}

### inline_mysql_mutex_register

`static` `inline`

```cpp
static inline void inline_mysql_mutex_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:669

---

{#inline_mysql_mutex_init}

### inline_mysql_mutex_init

`static` `inline`

```cpp
static inline int inline_mysql_mutex_init(mysql_mutex_t * that, const pthread_mutexattr_t * attr, mysql_mutex_t * that, const pthread_mutexattr_t * attr)
```

Defined in psi/mysql_thread.h:686

---

{#inline_mysql_mutex_destroy}

### inline_mysql_mutex_destroy

`static` `inline`

```cpp
static inline int inline_mysql_mutex_destroy(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:709

---

{#inline_mysql_mutex_lock}

### inline_mysql_mutex_lock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_lock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:737

---

{#inline_mysql_mutex_trylock}

### inline_mysql_mutex_trylock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_trylock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:756

---

{#inline_mysql_mutex_unlock}

### inline_mysql_mutex_unlock

`static` `inline`

```cpp
static inline int inline_mysql_mutex_unlock(mysql_mutex_t * that, mysql_mutex_t * that)
```

Defined in psi/mysql_thread.h:775

---

{#inline_mysql_rwlock_register}

### inline_mysql_rwlock_register

`static` `inline`

```cpp
static inline void inline_mysql_rwlock_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:798

---

{#inline_mysql_rwlock_init}

### inline_mysql_rwlock_init

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_init(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:815

---

{#inline_mysql_prlock_init}

### inline_mysql_prlock_init

`static` `inline`

```cpp
static inline int inline_mysql_prlock_init(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:833

---

{#inline_mysql_rwlock_destroy}

### inline_mysql_rwlock_destroy

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_destroy(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:848

---

{#inline_mysql_prlock_destroy}

### inline_mysql_prlock_destroy

`static` `inline`

```cpp
static inline int inline_mysql_prlock_destroy(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:862

---

{#inline_mysql_rwlock_rdlock}

### inline_mysql_rwlock_rdlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_rdlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:893

---

{#inline_mysql_prlock_rdlock}

### inline_mysql_prlock_rdlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_rdlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:908

---

{#inline_mysql_rwlock_wrlock}

### inline_mysql_rwlock_wrlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_wrlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:923

---

{#inline_mysql_prlock_wrlock}

### inline_mysql_prlock_wrlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_wrlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:938

---

{#inline_mysql_rwlock_tryrdlock}

### inline_mysql_rwlock_tryrdlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_tryrdlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:953

---

{#inline_mysql_rwlock_trywrlock}

### inline_mysql_rwlock_trywrlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_trywrlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:967

---

{#inline_mysql_rwlock_unlock}

### inline_mysql_rwlock_unlock

`static` `inline`

```cpp
static inline int inline_mysql_rwlock_unlock(mysql_rwlock_t * that, mysql_rwlock_t * that)
```

Defined in psi/mysql_thread.h:981

---

{#inline_mysql_prlock_unlock}

### inline_mysql_prlock_unlock

`static` `inline`

```cpp
static inline int inline_mysql_prlock_unlock(mysql_prlock_t * that, mysql_prlock_t * that)
```

Defined in psi/mysql_thread.h:994

---

{#inline_mysql_cond_register}

### inline_mysql_cond_register

`static` `inline`

```cpp
static inline void inline_mysql_cond_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:1007

---

{#inline_mysql_cond_init}

### inline_mysql_cond_init

`static` `inline`

```cpp
static inline int inline_mysql_cond_init(mysql_cond_t * that, const pthread_condattr_t * attr, mysql_cond_t * that, const pthread_condattr_t * attr)
```

Defined in psi/mysql_thread.h:1024

---

{#inline_mysql_cond_destroy}

### inline_mysql_cond_destroy

`static` `inline`

```cpp
static inline int inline_mysql_cond_destroy(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql_thread.h:1039

---

{#inline_mysql_cond_wait}

### inline_mysql_cond_wait

`static` `inline`

```cpp
static inline int inline_mysql_cond_wait(mysql_cond_t * that, mysql_mutex_t * mutex, mysql_cond_t * that, mysql_mutex_t * mutex)
```

Defined in psi/mysql_thread.h:1060

---

{#inline_mysql_cond_timedwait}

### inline_mysql_cond_timedwait

`static` `inline`

```cpp
static inline int inline_mysql_cond_timedwait(mysql_cond_t * that, mysql_mutex_t * mutex, const struct timespec * abstime, mysql_cond_t * that, mysql_mutex_t * mutex, const struct timespec * abstime)
```

Defined in psi/mysql_thread.h:1075

---

{#inline_mysql_cond_signal}

### inline_mysql_cond_signal

`static` `inline`

```cpp
static inline int inline_mysql_cond_signal(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql_thread.h:1091

---

{#inline_mysql_cond_broadcast}

### inline_mysql_cond_broadcast

`static` `inline`

```cpp
static inline int inline_mysql_cond_broadcast(mysql_cond_t * that, mysql_cond_t * that)
```

Defined in psi/mysql_thread.h:1103

---

{#inline_mysql_thread_register}

### inline_mysql_thread_register

`static` `inline`

```cpp
static inline void inline_mysql_thread_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_thread.h:1115

---

{#json_type}

### json_type

```cpp
enum json_types json_type(const char * js, const char * js_end, const char ** value, int * value_len)
```

Defined in service_json.h:94

---

{#json_get_array_item}

### json_get_array_item

```cpp
enum json_types json_get_array_item(const char * js, const char * js_end, int n_item, const char ** value, int * value_len)
```

Defined in service_json.h:96

---

{#json_get_object_key}

### json_get_object_key

```cpp
enum json_types json_get_object_key(const char * js, const char * js_end, const char * key, const char ** value, int * value_len)
```

Defined in service_json.h:99

---

{#json_get_object_nkey}

### json_get_object_nkey

```cpp
enum json_types json_get_object_nkey(const char * js, const char * js_end, int nkey, const char ** keyname, const char ** keyname_end, const char ** value, int * value_len)
```

Defined in service_json.h:102

---

{#json_escape_string}

### json_escape_string

```cpp
int json_escape_string(const char * str, const char * str_end, char * json, char * json_end)
```

Defined in service_json.h:105

---

{#json_unescape_json}

### json_unescape_json

```cpp
int json_unescape_json(const char * json_str, const char * json_end, char * res, char * res_end)
```

Defined in service_json.h:107

---

{#my_sha1}

### my_sha1

```cpp
void my_sha1(unsigned char *, const char *, size_t)
```

Defined in service_sha1.h:54

---

{#my_sha1_multi}

### my_sha1_multi

```cpp
void my_sha1_multi(unsigned char *, ...)
```

Defined in service_sha1.h:55

---

{#my_sha1_context_size}

### my_sha1_context_size

```cpp
size_t my_sha1_context_size()
```

Defined in service_sha1.h:56

---

{#my_sha1_init}

### my_sha1_init

```cpp
void my_sha1_init(void * context)
```

Defined in service_sha1.h:57

---

{#my_sha1_input}

### my_sha1_input

```cpp
void my_sha1_input(void * context, const unsigned char * buf, size_t len)
```

Defined in service_sha1.h:58

---

{#my_sha1_result}

### my_sha1_result

```cpp
void my_sha1_result(void * context, unsigned char * digest)
```

Defined in service_sha1.h:59

---

{#my_sha224}

### my_sha224

```cpp
void my_sha224(unsigned char *, const char *, size_t)
```

Defined in service_sha2.h:94

---

{#my_sha224_multi}

### my_sha224_multi

```cpp
void my_sha224_multi(unsigned char *, ...)
```

Defined in service_sha2.h:95

---

{#my_sha224_context_size}

### my_sha224_context_size

```cpp
size_t my_sha224_context_size()
```

Defined in service_sha2.h:96

---

{#my_sha224_init}

### my_sha224_init

```cpp
void my_sha224_init(void * context)
```

Defined in service_sha2.h:97

---

{#my_sha224_input}

### my_sha224_input

```cpp
void my_sha224_input(void * context, const unsigned char * buf, size_t len)
```

Defined in service_sha2.h:98

---

{#my_sha224_result}

### my_sha224_result

```cpp
void my_sha224_result(void * context, unsigned char * digest)
```

Defined in service_sha2.h:99

---

{#my_sha256}

### my_sha256

```cpp
void my_sha256(unsigned char *, const char *, size_t)
```

Defined in service_sha2.h:101

---

{#my_sha256_multi}

### my_sha256_multi

```cpp
void my_sha256_multi(unsigned char *, ...)
```

Defined in service_sha2.h:102

---

{#my_sha256_context_size}

### my_sha256_context_size

```cpp
size_t my_sha256_context_size()
```

Defined in service_sha2.h:103

---

{#my_sha256_init}

### my_sha256_init

```cpp
void my_sha256_init(void * context)
```

Defined in service_sha2.h:104

---

{#my_sha256_input}

### my_sha256_input

```cpp
void my_sha256_input(void * context, const unsigned char * buf, size_t len)
```

Defined in service_sha2.h:105

---

{#my_sha256_result}

### my_sha256_result

```cpp
void my_sha256_result(void * context, unsigned char * digest)
```

Defined in service_sha2.h:106

---

{#my_sha384}

### my_sha384

```cpp
void my_sha384(unsigned char *, const char *, size_t)
```

Defined in service_sha2.h:108

---

{#my_sha384_multi}

### my_sha384_multi

```cpp
void my_sha384_multi(unsigned char *, ...)
```

Defined in service_sha2.h:109

---

{#my_sha384_context_size}

### my_sha384_context_size

```cpp
size_t my_sha384_context_size()
```

Defined in service_sha2.h:110

---

{#my_sha384_init}

### my_sha384_init

```cpp
void my_sha384_init(void * context)
```

Defined in service_sha2.h:111

---

{#my_sha384_input}

### my_sha384_input

```cpp
void my_sha384_input(void * context, const unsigned char * buf, size_t len)
```

Defined in service_sha2.h:112

---

{#my_sha384_result}

### my_sha384_result

```cpp
void my_sha384_result(void * context, unsigned char * digest)
```

Defined in service_sha2.h:113

---

{#my_sha512}

### my_sha512

```cpp
void my_sha512(unsigned char *, const char *, size_t)
```

Defined in service_sha2.h:115

---

{#my_sha512_multi}

### my_sha512_multi

```cpp
void my_sha512_multi(unsigned char *, ...)
```

Defined in service_sha2.h:116

---

{#my_sha512_context_size}

### my_sha512_context_size

```cpp
size_t my_sha512_context_size()
```

Defined in service_sha2.h:117

---

{#my_sha512_init}

### my_sha512_init

```cpp
void my_sha512_init(void * context)
```

Defined in service_sha2.h:118

---

{#my_sha512_input}

### my_sha512_input

```cpp
void my_sha512_input(void * context, const unsigned char * buf, size_t len)
```

Defined in service_sha2.h:119

---

{#my_sha512_result}

### my_sha512_result

```cpp
void my_sha512_result(void * context, unsigned char * digest)
```

Defined in service_sha2.h:120

---

{#mysql_load_plugin}

### mysql_load_plugin

```cpp
struct st_mysql_client_plugin * mysql_load_plugin(struct st_mysql * mysql, const char * name, int type, int argc, ...)
```

Defined in client_plugin.h:120

loads a plugin and initializes it

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql` | `struct st_mysql *` | MYSQL structure. |
| `name` | `const char *` | a name of the plugin to load |
| `type` | `int` | type of plugin that should be loaded, -1 to disable type check |
| `argc` | `int` | number of arguments to pass to the plugin initialization function |

#### Return Values

| Value | Description |
|-------|-------------|
| `a` | pointer to the loaded plugin, or NULL in case of a failure |

---

{#mysql_load_plugin_v}

### mysql_load_plugin_v

```cpp
struct st_mysql_client_plugin * mysql_load_plugin_v(struct st_mysql * mysql, const char * name, int type, int argc, va_list args)
```

Defined in client_plugin.h:140

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

#### Return Values

| Value | Description |
|-------|-------------|
| `a` | pointer to the loaded plugin, or NULL in case of a failure |

---

{#mysql_client_find_plugin}

### mysql_client_find_plugin

```cpp
struct st_mysql_client_plugin * mysql_client_find_plugin(struct st_mysql * mysql, const char * name, int type)
```

Defined in client_plugin.h:154

finds an already loaded plugin by name, or loads it, if necessary

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql` | `struct st_mysql *` | MYSQL structure. |
| `name` | `const char *` | a name of the plugin to load |
| `type` | `int` | type of plugin that should be loaded |

#### Return Values

| Value | Description |
|-------|-------------|
| `a` | pointer to the plugin, or NULL in case of a failure |

---

{#mysql_client_register_plugin}

### mysql_client_register_plugin

```cpp
struct st_mysql_client_plugin * mysql_client_register_plugin(struct st_mysql * mysql, struct st_mysql_client_plugin * plugin)
```

Defined in client_plugin.h:171

adds a plugin structure to the list of loaded plugins

This is useful if an application has the necessary functionality (for example, a special load data handler) statically linked into the application binary. It can use this function to register the plugin directly, avoiding the need to factor it out into a shared object.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql` | `struct st_mysql *` | MYSQL structure. It is only used for error reporting |
| `plugin` | struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | an [st_mysql_client_plugin](#st_mysql_client_plugin) structure to register |

#### Return Values

| Value | Description |
|-------|-------------|
| `a` | pointer to the plugin, or NULL in case of a failure |

---

{#mysql_plugin_options}

### mysql_plugin_options

```cpp
int mysql_plugin_options(struct st_mysql_client_plugin * plugin, const char * option, const void * value)
```

Defined in client_plugin.h:186

set plugin options

Can be used to set extra options and affect behavior for a plugin. This function may be called multiple times to set several options

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `plugin` | struct [`st_mysql_client_plugin`](#st_mysql_client_plugin) * | an [st_mysql_client_plugin](#st_mysql_client_plugin) structure |
| `option` | `const char *` | a string which specifies the option to set |
| `value` | `const void *` | value for the option. |

#### Return Values

| Value | Description |
|-------|-------------|
| `0` | on success, 1 in case of failure |

---

{#wsrep_consistency_check}

### wsrep_consistency_check

```cpp
bool wsrep_consistency_check(MYSQL_THD thd)
```

Defined in service_wsrep.h:167

---

{#wsrep_prepare_key_for_innodb}

### wsrep_prepare_key_for_innodb

```cpp
bool wsrep_prepare_key_for_innodb(MYSQL_THD thd, const unsigned char * cache_key, size_t cache_key_len, const unsigned char * row_id, size_t row_id_len, struct wsrep_buf * key, size_t * key_len)
```

Defined in service_wsrep.h:168

---

{#wsrep_thd_query}

### wsrep_thd_query

```cpp
const char * wsrep_thd_query(const MYSQL_THD thd)
```

Defined in service_wsrep.h:169

---

{#wsrep_is_wsrep_xid}

### wsrep_is_wsrep_xid

```cpp
int wsrep_is_wsrep_xid(const void * xid)
```

Defined in service_wsrep.h:170

---

{#wsrep_xid_seqno}

### wsrep_xid_seqno

```cpp
long long wsrep_xid_seqno(const struct xid_t * xid)
```

Defined in service_wsrep.h:171

---

{#wsrep_xid_uuid}

### wsrep_xid_uuid

```cpp
const unsigned char * wsrep_xid_uuid(const struct xid_t * xid)
```

Defined in service_wsrep.h:172

---

{#wsrep_thd_trx_seqno}

### wsrep_thd_trx_seqno

```cpp
long long wsrep_thd_trx_seqno(const MYSQL_THD thd)
```

Defined in service_wsrep.h:173

---

{#get_wsrep_recovery}

### get_wsrep_recovery

```cpp
my_bool get_wsrep_recovery()
```

Defined in service_wsrep.h:174

---

{#wsrep_thd_ignore_table}

### wsrep_thd_ignore_table

```cpp
bool wsrep_thd_ignore_table(MYSQL_THD thd)
```

Defined in service_wsrep.h:175

---

{#wsrep_set_data_home_dir}

### wsrep_set_data_home_dir

```cpp
void wsrep_set_data_home_dir(const char * data_dir)
```

Defined in service_wsrep.h:176

---

{#wsrep_on}

### wsrep_on

```cpp
my_bool wsrep_on(const MYSQL_THD thd)
```

Defined in service_wsrep.h:184

---

{#wsrep_thd_lock}

### wsrep_thd_LOCK

```cpp
void wsrep_thd_LOCK(const MYSQL_THD thd)
```

Defined in service_wsrep.h:186

---

{#wsrep_thd_trylock}

### wsrep_thd_TRYLOCK

```cpp
int wsrep_thd_TRYLOCK(const MYSQL_THD thd)
```

Defined in service_wsrep.h:188

---

{#wsrep_thd_unlock}

### wsrep_thd_UNLOCK

```cpp
void wsrep_thd_UNLOCK(const MYSQL_THD thd)
```

Defined in service_wsrep.h:190

---

{#wsrep_thd_kill_lock}

### wsrep_thd_kill_LOCK

```cpp
void wsrep_thd_kill_LOCK(const MYSQL_THD thd)
```

Defined in service_wsrep.h:192

---

{#wsrep_thd_kill_unlock}

### wsrep_thd_kill_UNLOCK

```cpp
void wsrep_thd_kill_UNLOCK(const MYSQL_THD thd)
```

Defined in service_wsrep.h:193

---

{#wsrep_thd_client_state_str}

### wsrep_thd_client_state_str

```cpp
const char * wsrep_thd_client_state_str(const MYSQL_THD thd)
```

Defined in service_wsrep.h:196

---

{#wsrep_thd_client_mode_str}

### wsrep_thd_client_mode_str

```cpp
const char * wsrep_thd_client_mode_str(const MYSQL_THD thd)
```

Defined in service_wsrep.h:198

---

{#wsrep_thd_transaction_state_str}

### wsrep_thd_transaction_state_str

```cpp
const char * wsrep_thd_transaction_state_str(const MYSQL_THD thd)
```

Defined in service_wsrep.h:200

---

{#wsrep_thd_transaction_id}

### wsrep_thd_transaction_id

```cpp
query_id_t wsrep_thd_transaction_id(const MYSQL_THD thd)
```

Defined in service_wsrep.h:203

---

{#wsrep_thd_self_abort}

### wsrep_thd_self_abort

```cpp
void wsrep_thd_self_abort(MYSQL_THD thd)
```

Defined in service_wsrep.h:205

---

{#wsrep_thd_is_local}

### wsrep_thd_is_local

```cpp
my_bool wsrep_thd_is_local(const MYSQL_THD thd)
```

Defined in service_wsrep.h:207

---

{#wsrep_thd_is_applying}

### wsrep_thd_is_applying

```cpp
my_bool wsrep_thd_is_applying(const MYSQL_THD thd)
```

Defined in service_wsrep.h:210

---

{#wsrep_thd_is_toi}

### wsrep_thd_is_toi

```cpp
my_bool wsrep_thd_is_toi(const MYSQL_THD thd)
```

Defined in service_wsrep.h:212

---

{#wsrep_thd_is_local_toi}

### wsrep_thd_is_local_toi

```cpp
my_bool wsrep_thd_is_local_toi(const MYSQL_THD thd)
```

Defined in service_wsrep.h:214

---

{#wsrep_thd_is_in_rsu}

### wsrep_thd_is_in_rsu

```cpp
my_bool wsrep_thd_is_in_rsu(const MYSQL_THD thd)
```

Defined in service_wsrep.h:216

---

{#wsrep_thd_is_bf}

### wsrep_thd_is_BF

```cpp
my_bool wsrep_thd_is_BF(const MYSQL_THD thd, my_bool sync)
```

Defined in service_wsrep.h:218

---

{#wsrep_thd_is_sr}

### wsrep_thd_is_SR

```cpp
my_bool wsrep_thd_is_SR(const MYSQL_THD thd)
```

Defined in service_wsrep.h:220

---

{#wsrep_handle_sr_rollback}

### wsrep_handle_SR_rollback

```cpp
void wsrep_handle_SR_rollback(MYSQL_THD BF_thd, MYSQL_THD victim_thd)
```

Defined in service_wsrep.h:221

---

{#wsrep_thd_retry_counter}

### wsrep_thd_retry_counter

```cpp
int wsrep_thd_retry_counter(const MYSQL_THD thd)
```

Defined in service_wsrep.h:223

---

{#wsrep_thd_bf_abort}

### wsrep_thd_bf_abort

```cpp
my_bool wsrep_thd_bf_abort(MYSQL_THD bf_thd, MYSQL_THD victim_thd, my_bool signal)
```

Defined in service_wsrep.h:225

---

{#wsrep_thd_order_before}

### wsrep_thd_order_before

```cpp
my_bool wsrep_thd_order_before(const MYSQL_THD left, const MYSQL_THD right)
```

Defined in service_wsrep.h:229

---

{#wsrep_thd_skip_locking}

### wsrep_thd_skip_locking

```cpp
my_bool wsrep_thd_skip_locking(const MYSQL_THD thd)
```

Defined in service_wsrep.h:232

---

{#wsrep_thd_is_aborting}

### wsrep_thd_is_aborting

```cpp
my_bool wsrep_thd_is_aborting(const MYSQL_THD thd)
```

Defined in service_wsrep.h:234

---

{#wsrep_thd_in_rollback}

### wsrep_thd_in_rollback

```cpp
my_bool wsrep_thd_in_rollback(const MYSQL_THD thd)
```

Defined in service_wsrep.h:236

---

{#wsrep_thd_append_key}

### wsrep_thd_append_key

```cpp
int wsrep_thd_append_key(MYSQL_THD thd, const struct wsrep_key * key, int n_keys, enum Wsrep_service_key_type)
```

Defined in service_wsrep.h:240

---

{#wsrep_thd_append_table_key}

### wsrep_thd_append_table_key

```cpp
int wsrep_thd_append_table_key(MYSQL_THD thd, const char * db, const char * table, enum Wsrep_service_key_type)
```

Defined in service_wsrep.h:245

---

{#wsrep_thd_is_local_transaction}

### wsrep_thd_is_local_transaction

```cpp
my_bool wsrep_thd_is_local_transaction(const MYSQL_THD thd)
```

Defined in service_wsrep.h:250

---

{#wsrep_get_sr_table_name}

### wsrep_get_sr_table_name

```cpp
const char * wsrep_get_sr_table_name()
```

Defined in service_wsrep.h:254

---

{#wsrep_get_debug}

### wsrep_get_debug

```cpp
my_bool wsrep_get_debug()
```

Defined in service_wsrep.h:256

---

{#wsrep_commit_ordered}

### wsrep_commit_ordered

```cpp
void wsrep_commit_ordered(MYSQL_THD thd)
```

Defined in service_wsrep.h:258

---

{#wsrep_osu_method_get}

### wsrep_OSU_method_get

```cpp
ulong wsrep_OSU_method_get(const MYSQL_THD thd)
```

Defined in service_wsrep.h:260

---

{#wsrep_thd_has_ignored_error}

### wsrep_thd_has_ignored_error

```cpp
my_bool wsrep_thd_has_ignored_error(const MYSQL_THD thd)
```

Defined in service_wsrep.h:261

---

{#wsrep_thd_set_ignored_error}

### wsrep_thd_set_ignored_error

```cpp
void wsrep_thd_set_ignored_error(MYSQL_THD thd, my_bool val)
```

Defined in service_wsrep.h:262

---

{#wsrep_report_bf_lock_wait}

### wsrep_report_bf_lock_wait

```cpp
void wsrep_report_bf_lock_wait(const THD * thd, unsigned long long trx_id)
```

Defined in service_wsrep.h:263

---

{#wsrep_thd_set_pa_unsafe}

### wsrep_thd_set_PA_unsafe

```cpp
void wsrep_thd_set_PA_unsafe(MYSQL_THD thd)
```

Defined in service_wsrep.h:266

---

{#wsrep_get_domain_id}

### wsrep_get_domain_id

```cpp
uint32 wsrep_get_domain_id()
```

Defined in service_wsrep.h:267

---

{#my_base64_needed_encoded_length}

### my_base64_needed_encoded_length

```cpp
int my_base64_needed_encoded_length(int length_of_data)
```

Defined in service_base64.h:57

---

{#my_base64_encode_max_arg_length}

### my_base64_encode_max_arg_length

```cpp
int my_base64_encode_max_arg_length(void)
```

Defined in service_base64.h:60

---

{#my_base64_needed_decoded_length}

### my_base64_needed_decoded_length

```cpp
int my_base64_needed_decoded_length(int length_of_encoded_data)
```

Defined in service_base64.h:63

---

{#my_base64_decode_max_arg_length}

### my_base64_decode_max_arg_length

```cpp
int my_base64_decode_max_arg_length()
```

Defined in service_base64.h:66

---

{#my_base64_encode}

### my_base64_encode

```cpp
int my_base64_encode(const void * src, size_t src_len, char * dst)
```

Defined in service_base64.h:69

---

{#my_base64_decode}

### my_base64_decode

```cpp
int my_base64_decode(const char * src, size_t src_len, void * dst, const char ** end_ptr, int flags)
```

Defined in service_base64.h:72

---

{#logger_init_mutexes}

### logger_init_mutexes

```cpp
void logger_init_mutexes()
```

Defined in service_logger.h:103

---

{#logger_open}

### logger_open

```cpp
LOGGER_HANDLE * logger_open(const char * path, unsigned long long size_limit, unsigned int rotations, size_t buffer_size)
```

Defined in service_logger.h:104

---

{#logger_close}

### logger_close

```cpp
int logger_close(LOGGER_HANDLE * log)
```

Defined in service_logger.h:107

---

{#logger_vprintf}

### logger_vprintf

```cpp
int logger_vprintf(LOGGER_HANDLE * log, const char * fmt, va_list argptr)
```

Defined in service_logger.h:108

---

{#logger_printf}

### logger_printf

```cpp
int int logger_printf(LOGGER_HANDLE * log, const char * fmt, ...)
```

Defined in service_logger.h:110

---

{#logger_write}

### logger_write

```cpp
int int int logger_write(LOGGER_HANDLE * log, const void * data, size_t size)
```

Defined in service_logger.h:112

---

{#logger_rotate}

### logger_rotate

```cpp
int logger_rotate(LOGGER_HANDLE * log)
```

Defined in service_logger.h:113

---

{#logger_sync}

### logger_sync

```cpp
int logger_sync(LOGGER_HANDLE * log)
```

Defined in service_logger.h:114

---

{#logger_resize_buffer}

### logger_resize_buffer

```cpp
int logger_resize_buffer(LOGGER_HANDLE * log, size_t new_buffer_size)
```

Defined in service_logger.h:115

---

{#logger_set_filesize_limit}

### logger_set_filesize_limit

```cpp
int logger_set_filesize_limit(LOGGER_HANDLE * log, unsigned long long new_file_limit)
```

Defined in service_logger.h:116

---

{#logger_set_rotations}

### logger_set_rotations

```cpp
int logger_set_rotations(LOGGER_HANDLE * log, unsigned int new_rotations)
```

Defined in service_logger.h:118

---

{#thd_mdl_context}

### thd_mdl_context

```cpp
void * thd_mdl_context(MYSQL_THD thd)
```

Defined in service_thd_mdl.h:41

MDL_context accessor 
#### Returns
pointer to thd->mdl_context

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | [`MYSQL_THD`](#mysql_thd) | the current session |

---

{#thd_rnd}

### thd_rnd

```cpp
double thd_rnd(MYSQL_THD thd)
```

Defined in service_thd_rnd.h:44

---

{#thd_create_random_password}

### thd_create_random_password

```cpp
void thd_create_random_password(MYSQL_THD thd, char * to, size_t length)
```

Defined in service_thd_rnd.h:54

Generate string of printable random characters of requested length.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | [`MYSQL_THD`](#mysql_thd) | User thread connection handle |
| `to` | `char *` | Buffer for generation; must be at least length+1 bytes long; result string is always null-terminated |
| `length` | `size_t` | How many random characters to put in buffer |

---

{#my_aes_crypt_init}

### my_aes_crypt_init

```cpp
int my_aes_crypt_init(void * ctx, enum my_aes_mode mode, int flags, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen)
```

Defined in service_my_crypt.h:110

---

{#my_aes_crypt_update}

### my_aes_crypt_update

```cpp
int my_aes_crypt_update(void * ctx, const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen)
```

Defined in service_my_crypt.h:113

---

{#my_aes_crypt_finish}

### my_aes_crypt_finish

```cpp
int my_aes_crypt_finish(void * ctx, unsigned char * dst, unsigned int * dlen)
```

Defined in service_my_crypt.h:115

---

{#my_aes_crypt}

### my_aes_crypt

```cpp
int my_aes_crypt(enum my_aes_mode mode, int flags, const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen)
```

Defined in service_my_crypt.h:116

---

{#my_random_bytes}

### my_random_bytes

```cpp
int my_random_bytes(unsigned char * buf, int num)
```

Defined in service_my_crypt.h:120

---

{#my_bytes_to_key}

### my_bytes_to_key

```cpp
void my_bytes_to_key(const unsigned char * salt, const unsigned char * input, unsigned int input_len, unsigned char * key, unsigned char * iv, enum my_digest digest, unsigned int use_pbkdf2)
```

Defined in service_my_crypt.h:121

---

{#my_aes_get_size}

### my_aes_get_size

```cpp
unsigned int my_aes_get_size(enum my_aes_mode mode, unsigned int source_length)
```

Defined in service_my_crypt.h:125

---

{#my_aes_ctx_size-1}

### my_aes_ctx_size

```cpp
unsigned int my_aes_ctx_size(enum my_aes_mode mode)
```

Defined in service_my_crypt.h:126

---

{#thd_wait_begin}

### thd_wait_begin

```cpp
void thd_wait_begin(MYSQL_THD thd, int wait_type)
```

Defined in service_thd_wait.h:94

---

{#thd_wait_end}

### thd_wait_end

```cpp
void thd_wait_end(MYSQL_THD thd)
```

Defined in service_thd_wait.h:95

---

{#encryption_key_id_exists}

### encryption_key_id_exists

`static` `inline`

```cpp
static inline unsigned int encryption_key_id_exists(unsigned int id)
```

Defined in service_encryption.h:96

---

{#encryption_key_version_exists}

### encryption_key_version_exists

`static` `inline`

```cpp
static inline unsigned int encryption_key_version_exists(unsigned int id, unsigned int version)
```

Defined in service_encryption.h:101

---

{#encryption_crypt}

### encryption_crypt

`static` `inline`

```cpp
static inline int encryption_crypt(const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen, int flags, unsigned int key_id, unsigned int key_version)
```

Defined in service_encryption.h:112

main entrypoint to perform encryption or decryption 
#### Invariants
`src` is valid for `slen`

#### Invariants
`dst` is valid for `*dlen`, `*dlen` is initialized 

#### Invariants
`src` and `dst` do not overlap

---

{#thd_alloc}

### thd_alloc

```cpp
void * thd_alloc(const MYSQL_THD thd, size_t size)
```

Defined in service_thd_alloc.h:102

Allocate memory in the connection's local memory pool

When properly used in place of `my_malloc()`, this can significantly improve concurrency. Don't use this or related functions to allocate large chunks of memory. Use for temporary storage only. The memory will be freed automatically at the end of the statement; no explicit code is required to prevent memory leaks.

**See also**: alloc_root()

---

{#thd_calloc}

### thd_calloc

```cpp
void * thd_calloc(const MYSQL_THD thd, size_t size)
```

Defined in service_thd_alloc.h:106

**See also**: [thd_alloc()](#thd_alloc)

---

{#thd_strdup}

### thd_strdup

```cpp
char * thd_strdup(const MYSQL_THD thd, const char * str)
```

Defined in service_thd_alloc.h:110

**See also**: [thd_alloc()](#thd_alloc)

---

{#thd_strmake}

### thd_strmake

```cpp
char * thd_strmake(const MYSQL_THD thd, const char * str, size_t size)
```

Defined in service_thd_alloc.h:114

**See also**: [thd_alloc()](#thd_alloc)

---

{#thd_memdup}

### thd_memdup

```cpp
void * thd_memdup(const MYSQL_THD thd, const void * str, size_t size)
```

Defined in service_thd_alloc.h:118

**See also**: [thd_alloc()](#thd_alloc)

---

{#thd_make_lex_string}

### thd_make_lex_string

```cpp
MYSQL_CONST_LEX_STRING * thd_make_lex_string(const MYSQL_THD thd, MYSQL_CONST_LEX_STRING * lex_str, const char * str, size_t size, int allocate_lex_string)
```

Defined in service_thd_alloc.h:134

Create a LEX_STRING in this connection's local memory pool

#### Returns
NULL on failure, or pointer to the LEX_STRING object

**See also**: [thd_alloc()](#thd_alloc)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |
| `lex_str` | [`MYSQL_CONST_LEX_STRING`](#mysql_const_lex_string) * | pointer to LEX_STRING object to be initialized |
| `str` | `const char *` | initializer to be copied into lex_str |
| `size` | `size_t` | length of str, in bytes |
| `allocate_lex_string` | `int` | flag: if TRUE, allocate new LEX_STRING object, instead of using lex_str value |

---

{#my_snprintf}

### my_snprintf

```cpp
size_t my_snprintf(char * to, size_t n, const char * fmt, ...)
```

Defined in service_my_snprintf.h:113

---

{#my_vsnprintf}

### my_vsnprintf

```cpp
size_t size_t my_vsnprintf(char * to, size_t n, const char * fmt, va_list ap)
```

Defined in service_my_snprintf.h:115

---

{#thd_get_autoinc}

### thd_get_autoinc

```cpp
void thd_get_autoinc(const MYSQL_THD thd, unsigned long * off, unsigned long * inc)
```

Defined in service_thd_autoinc.h:44

Return autoincrement system variables

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |
| `off` | `unsigned long *` | the value of @SESSION.auto_increment_offset |
| `inc` | `unsigned long *` | the value of @SESSION.auto_increment_increment |

---

{#thd_log_warnings}

### thd_log_warnings

```cpp
int thd_log_warnings(MYSQL_THD thd)
```

Defined in service_log_warnings.h:44

MDL_context accessor 
#### Returns
pointer to thd->mdl_context

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | [`MYSQL_THD`](#mysql_thd) | the current session |

---

{#thd_time_to_gmt_sec}

### thd_TIME_to_gmt_sec

```cpp
my_time_t thd_TIME_to_gmt_sec(MYSQL_THD thd, const MYSQL_TIME * ltime, unsigned int * errcode)
```

Defined in service_thd_timezone.h:67

---

{#thd_gmt_sec_to_time}

### thd_gmt_sec_to_TIME

```cpp
void thd_gmt_sec_to_TIME(MYSQL_THD thd, MYSQL_TIME * ltime, my_time_t t)
```

Defined in service_thd_timezone.h:68

---

{#thd_time_to_str}

### thd_TIME_to_str

```cpp
void thd_TIME_to_str(MYSQL_THD thd, const MYSQL_TIME * ltime, const char * format, char * buf, unsigned int buf_len)
```

Defined in service_thd_timezone.h:69

---

{#thd_key_create}

### thd_key_create

```cpp
int thd_key_create(MYSQL_THD_KEY_T * key)
```

Defined in service_thd_specifics.h:85

create THD specific storage 
#### Returns
0 on success else errno is returned

---

{#thd_key_delete}

### thd_key_delete

```cpp
void thd_key_delete(MYSQL_THD_KEY_T * key)
```

Defined in service_thd_specifics.h:90

delete THD specific storage

---

{#thd_getspecific}

### thd_getspecific

```cpp
void * thd_getspecific(MYSQL_THD thd, MYSQL_THD_KEY_T key)
```

Defined in service_thd_specifics.h:99

get/set thd specific storage

* first time this is called from a thread it will return 0
* this call is thread-safe in that different threads may call this simultaneously if operating on different THDs.
* this call acquires no mutexes and is implemented as an array lookup

---

{#thd_setspecific}

### thd_setspecific

```cpp
int thd_setspecific(MYSQL_THD thd, MYSQL_THD_KEY_T key, void * value)
```

Defined in service_thd_specifics.h:100

---

{#thd_kill_level}

### thd_kill_level

```cpp
enum thd_kill_levels thd_kill_level(const MYSQL_THD)
```

Defined in service_kill_statement.h:62

---

{#my_error}

### my_error

```cpp
void my_error(unsigned int nr, unsigned long MyFlags, ...)
```

Defined in service_my_print_error.h:59

---

{#my_printf_error}

### my_printf_error

```cpp
void my_printf_error(unsigned int my_err, const char * format, unsigned long MyFlags, ...)
```

Defined in service_my_print_error.h:60

---

{#my_printv_error}

### my_printv_error

```cpp
void void my_printv_error(unsigned int error, const char * format, unsigned long MyFlags, va_list ap)
```

Defined in service_my_print_error.h:63

---

{#thd_progress_init}

### thd_progress_init

```cpp
void thd_progress_init(MYSQL_THD thd, unsigned int max_stage)
```

Defined in service_progress_report.h:58

---

{#thd_progress_report}

### thd_progress_report

```cpp
void thd_progress_report(MYSQL_THD thd, unsigned long long progress, unsigned long long max_progress)
```

Defined in service_progress_report.h:66

Report progress for long running operations

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | [`MYSQL_THD`](#mysql_thd) | User thread connection handle |
| `progress` | `unsigned long long` | Where we are now |
| `max_progress` | `unsigned long long` | Progress will continue up to this |

---

{#thd_progress_next_stage}

### thd_progress_next_stage

```cpp
void thd_progress_next_stage(MYSQL_THD thd)
```

Defined in service_progress_report.h:69

---

{#thd_progress_end}

### thd_progress_end

```cpp
void thd_progress_end(MYSQL_THD thd)
```

Defined in service_progress_report.h:70

---

{#set_thd_proc_info}

### set_thd_proc_info

```cpp
const char * set_thd_proc_info(MYSQL_THD, const char * info, const char * func, const char * file, unsigned int line)
```

Defined in service_progress_report.h:71

---

{#print_check_msg}

### print_check_msg

```cpp
void print_check_msg(MYSQL_THD, const char * db_name, const char * table_name, const char * op, const char * msg_type, const char * message, my_bool print_to_log)
```

Defined in service_print_check_msg.h:37

---

{#encryption_scheme_encrypt}

### encryption_scheme_encrypt

```cpp
int encryption_scheme_encrypt(const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, struct st_encryption_scheme * scheme, unsigned int key_version, unsigned int i32_1, unsigned int i32_2, unsigned long long i64)
```

Defined in service_encryption_scheme.h:114

---

{#encryption_scheme_decrypt}

### encryption_scheme_decrypt

```cpp
int encryption_scheme_decrypt(const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, struct st_encryption_scheme * scheme, unsigned int key_version, unsigned int i32_1, unsigned int i32_2, unsigned long long i64)
```

Defined in service_encryption_scheme.h:119

---

{#thd_get_error_message}

### thd_get_error_message

```cpp
const char * thd_get_error_message(const MYSQL_THD thd)
```

Defined in service_thd_error_context.h:61

Return error message 
#### Returns
error text

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |

---

{#thd_get_error_number}

### thd_get_error_number

```cpp
unsigned int thd_get_error_number(const MYSQL_THD thd)
```

Defined in service_thd_error_context.h:67

Return error number 
#### Returns
error number

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |

---

{#thd_get_error_row}

### thd_get_error_row

```cpp
unsigned long thd_get_error_row(const MYSQL_THD thd)
```

Defined in service_thd_error_context.h:73

Return the current row number (i.e. in a multiple INSERT statement) 
#### Returns
row number

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](#mysql_thd) | user thread connection handle |

---

{#thd_inc_error_row}

### thd_inc_error_row

```cpp
void thd_inc_error_row(MYSQL_THD thd)
```

Defined in service_thd_error_context.h:78

Increment the current row number

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | [`MYSQL_THD`](#mysql_thd) | user thread connection handle |

---

{#thd_get_error_context_description}

### thd_get_error_context_description

```cpp
char * thd_get_error_context_description(MYSQL_THD thd, char * buffer, unsigned int length, unsigned int max_query_length)
```

Defined in service_thd_error_context.h:83

Return a text description of a thread, its security context (user,host) and the current query.

## Variables

---

{#psi_server}

### PSI_server

```cpp
MYSQL_PLUGIN_IMPORT PSI * PSI_server
```

Type: MYSQL_PLUGIN_IMPORT [`PSI`](#psi) *

Defined in psi/psi.h:3019

---

{#my_md5_service}

### my_md5_service

```cpp
struct my_md5_service_st * my_md5_service
```

Type: struct [`my_md5_service_st`](#my_md5_service_st) *

Defined in service_md5.h:41

---

{#sql_service}

### sql_service

```cpp
struct sql_service_st * sql_service
```

Type: struct [`sql_service_st`](#sql_service_st) *

Defined in service_sql.h:77

---

{#thd_service}

### thd_service

```cpp
struct thd_service_st * thd_service
```

Type: struct [`thd_service_st`](#thd_service_st) *

Defined in service_thd.h:29

---

{#json_service}

### json_service

```cpp
struct json_service_st * json_service
```

Type: struct [`json_service_st`](#json_service_st) *

Defined in service_json.h:81

---

{#my_sha1_service}

### my_sha1_service

```cpp
struct my_sha1_service_st * my_sha1_service
```

Type: struct [`my_sha1_service_st`](#my_sha1_service_st) *

Defined in service_sha1.h:41

---

{#my_sha2_service}

### my_sha2_service

```cpp
struct my_sha2_service_st * my_sha2_service
```

Type: struct [`my_sha2_service_st`](#my_sha2_service_st) *

Defined in service_sha2.h:60

---

{#wsrep_service}

### wsrep_service

```cpp
struct wsrep_service_st * wsrep_service
```

Type: struct [`wsrep_service_st`](#wsrep_service_st) *

Defined in service_wsrep.h:105

---

{#wsrep_debug}

### wsrep_debug

```cpp
ulong wsrep_debug
```

Defined in service_wsrep.h:159

---

{#wsrep_log_conflicts}

### wsrep_log_conflicts

```cpp
my_bool wsrep_log_conflicts
```

Type: [`my_bool`](#my_bool)

Defined in service_wsrep.h:160

---

{#wsrep_certify_nonpk}

### wsrep_certify_nonPK

```cpp
my_bool wsrep_certify_nonPK
```

Type: [`my_bool`](#my_bool)

Defined in service_wsrep.h:161

---

{#wsrep_load_data_splitting}

### wsrep_load_data_splitting

```cpp
my_bool wsrep_load_data_splitting
```

Type: [`my_bool`](#my_bool)

Defined in service_wsrep.h:162

---

{#wsrep_drupal_282555_workaround}

### wsrep_drupal_282555_workaround

```cpp
my_bool wsrep_drupal_282555_workaround
```

Type: [`my_bool`](#my_bool)

Defined in service_wsrep.h:163

---

{#wsrep_recovery}

### wsrep_recovery

```cpp
my_bool wsrep_recovery
```

Type: [`my_bool`](#my_bool)

Defined in service_wsrep.h:164

---

{#wsrep_protocol_version}

### wsrep_protocol_version

```cpp
long wsrep_protocol_version
```

Defined in service_wsrep.h:165

---

{#wsrep_sr_table_name_full}

### wsrep_sr_table_name_full

```cpp
const char * wsrep_sr_table_name_full
```

Defined in service_wsrep.h:252

---

{#base64_service}

### base64_service

```cpp
struct base64_service_st * base64_service
```

Type: struct [`base64_service_st`](#base64_service_st) *

Defined in service_base64.h:43

---

{#logger_service}

### logger_service

```cpp
struct logger_service_st * logger_service
```

Type: struct [`logger_service_st`](#logger_service_st) *

Defined in service_logger.h:80

---

{#thd_mdl_service}

### thd_mdl_service

```cpp
struct thd_mdl_service_st * thd_mdl_service
```

Type: struct [`thd_mdl_service_st`](#thd_mdl_service_st) *

Defined in service_thd_mdl.h:31

---

{#thd_rnd_service}

### thd_rnd_service

```cpp
struct thd_rnd_service_st * thd_rnd_service
```

Type: struct [`thd_rnd_service_st`](#thd_rnd_service_st) *

Defined in service_thd_rnd.h:37

---

{#my_crypt_service}

### my_crypt_service

```cpp
struct my_crypt_service_st * my_crypt_service
```

Type: struct [`my_crypt_service_st`](#my_crypt_service_st) *

Defined in service_my_crypt.h:80

---

{#thd_wait_service}

### thd_wait_service

```cpp
struct thd_wait_service_st * thd_wait_service
```

Type: struct [`thd_wait_service_st`](#thd_wait_service_st) *

Defined in service_thd_wait.h:84

---

{#encryption_handler}

### encryption_handler

```cpp
struct encryption_service_st encryption_handler
```

Type: struct [`encryption_service_st`](#encryption_service_st)

Defined in service_encryption.h:85

---

{#thd_alloc_service}

### thd_alloc_service

```cpp
struct thd_alloc_service_st * thd_alloc_service
```

Type: struct [`thd_alloc_service_st`](#thd_alloc_service_st) *

Defined in service_thd_alloc.h:68

---

{#debug_sync_c_callback_ptr}

### debug_sync_C_callback_ptr

```cpp
void(* debug_sync_C_callback_ptr)(MYSQL_THD, const char *, size_t)
```

Defined in service_debug_sync.h:333

---

{#my_snprintf_service}

### my_snprintf_service

```cpp
struct my_snprintf_service_st * my_snprintf_service
```

Type: struct [`my_snprintf_service_st`](#my_snprintf_service_st) *

Defined in service_my_snprintf.h:104

---

{#thd_autoinc_service}

### thd_autoinc_service

```cpp
struct thd_autoinc_service_st * thd_autoinc_service
```

Type: struct [`thd_autoinc_service_st`](#thd_autoinc_service_st) *

Defined in service_thd_autoinc.h:32

---

{#thd_log_warnings_service}

### thd_log_warnings_service

```cpp
struct thd_log_warnings_service_st * thd_log_warnings_service
```

Type: struct [`thd_log_warnings_service_st`](#thd_log_warnings_service_st) *

Defined in service_log_warnings.h:34

---

{#thd_timezone_service}

### thd_timezone_service

```cpp
struct thd_timezone_service_st * thd_timezone_service
```

Type: struct [`thd_timezone_service_st`](#thd_timezone_service_st) *

Defined in service_thd_timezone.h:52

---

{#thd_specifics_service}

### thd_specifics_service

```cpp
struct thd_specifics_service_st * thd_specifics_service
```

Type: struct [`thd_specifics_service_st`](#thd_specifics_service_st) *

Defined in service_thd_specifics.h:67

---

{#thd_kill_statement_service}

### thd_kill_statement_service

```cpp
struct kill_statement_service_st * thd_kill_statement_service
```

Type: struct [`kill_statement_service_st`](#kill_statement_service_st) *

Defined in service_kill_statement.h:50

---

{#my_print_error_service}

### my_print_error_service

```cpp
struct my_print_error_service_st * my_print_error_service
```

Type: struct [`my_print_error_service_st`](#my_print_error_service_st) *

Defined in service_my_print_error.h:50

---

{#progress_report_service}

### progress_report_service

```cpp
struct progress_report_service_st * progress_report_service
```

Type: struct [`progress_report_service_st`](#progress_report_service_st) *

Defined in service_progress_report.h:46

---

{#print_check_msg_service}

### print_check_msg_service

```cpp
struct print_check_msg_service_st * print_check_msg_service
```

Type: struct [`print_check_msg_service_st`](#print_check_msg_service_st) *

Defined in service_print_check_msg.h:32

---

{#encryption_scheme_service}

### encryption_scheme_service

```cpp
struct encryption_scheme_service_st * encryption_scheme_service
```

Type: struct [`encryption_scheme_service_st`](#encryption_scheme_service_st) *

Defined in service_encryption_scheme.h:105

---

{#thd_error_context_service}

### thd_error_context_service

```cpp
struct thd_error_context_service_st * thd_error_context_service
```

Type: struct [`thd_error_context_service_st`](#thd_error_context_service_st) *

Defined in service_thd_error_context.h:39


## Class Definitions

{#opaque_thd}

### opaque_THD

```cpp
#include <psi.h>
```

```cpp
struct opaque_THD
```

Defined in psi/psi.h:95

{#st_mysql_xid}

### st_mysql_xid

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_xid
```

Defined in plugin.h:71

struct [st_mysql_xid](#st_mysql_xid) is binary compatible with the XID structure as in the X/Open CAE Specification, Distributed Transaction Processing: The XA Specification, X/Open Company Ltd., 1991. [http://www.opengroup.org/bookstore/catalog/c193.htm](http://www.opengroup.org/bookstore/catalog/c193.htm)

**See also**: XID in sql/handler.h

{#st_mysql_auth}

### st_mysql_auth

```cpp
#include <plugin_auth.h>
```

```cpp
struct st_mysql_auth
```

Defined in plugin_auth.h:119

Server authentication plugin descriptor

{#st_plugin_vio}

### st_plugin_vio

```cpp
#include <plugin_auth_common.h>
```

```cpp
struct st_plugin_vio
```

Defined in plugin_auth_common.h:107

Provides plugin access to communication channel

{#sql_service_st}

### sql_service_st

```cpp
#include <service_sql.h>
```

```cpp
struct sql_service_st
```

Defined in service_sql.h:49

{#st_mysql_audit}

### st_mysql_audit

```cpp
#include <plugin_audit.h>
```

```cpp
struct st_mysql_audit
```

Defined in plugin_audit.h:175

{#st_mysql_value}

### st_mysql_value

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_value
```

Defined in plugin.h:678

{#thd_service_st}

### thd_service_st

```cpp
#include <service_thd.h>
```

```cpp
struct thd_service_st
```

Defined in service_thd.h:27

{#json_service_st}

### json_service_st

```cpp
#include <service_json.h>
```

```cpp
struct json_service_st
```

Defined in service_json.h:64

{#st_maria_plugin}

### st_maria_plugin

```cpp
#include <plugin.h>
```

```cpp
struct st_maria_plugin
```

Defined in plugin.h:567

MariaDB extension for plugins declaration structure.

It also copies current MySQL plugin fields to have more independency in plugins extension

{#st_mysql_daemon}

### st_mysql_daemon

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_daemon
```

Defined in plugin.h:607

{#st_mysql_plugin}

### st_mysql_plugin

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_plugin
```

Defined in plugin.h:537

Plugin description structure.

{#mysql_replication}

### Mysql_replication

```cpp
#include <plugin.h>
```

```cpp
struct Mysql_replication
```

Defined in plugin.h:660

Replication plugin descriptor

{#wsrep_service_st}

### wsrep_service_st

```cpp
#include <service_wsrep.h>
```

```cpp
struct wsrep_service_st
```

Defined in service_wsrep.h:56

{#base64_service_st}

### base64_service_st

```cpp
#include <service_base64.h>
```

```cpp
struct base64_service_st
```

Defined in service_base64.h:35

{#logger_service_st}

### logger_service_st

```cpp
#include <service_logger.h>
```

```cpp
struct logger_service_st
```

Defined in service_logger.h:63

{#mysql_event_table}

### mysql_event_table

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_table
```

Defined in plugin_audit.h:134

{#st_mysql_ftparser}

### st_mysql_ftparser

```cpp
#include <plugin_ftparser.h>
```

```cpp
struct st_mysql_ftparser
```

Defined in plugin_ftparser.h:208

{#my_md5_service_st}

### my_md5_service_st

```cpp
#include <service_md5.h>
```

```cpp
struct my_md5_service_st
```

Defined in service_md5.h:34

{#st_mysql_show_var}

### st_mysql_show_var

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_show_var
```

Defined in plugin.h:206

{#my_sha1_service_st}

### my_sha1_service_st

```cpp
#include <service_sha1.h>
```

```cpp
struct my_sha1_service_st
```

Defined in service_sha1.h:34

{#my_sha2_service_st}

### my_sha2_service_st

```cpp
#include <service_sha2.h>
```

```cpp
struct my_sha2_service_st
```

Defined in service_sha2.h:32

{#mysql_event_general}

### mysql_event_general

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_general
```

Defined in plugin_audit.h:53

{#st_plugin_vio_info}

### st_plugin_vio_info

```cpp
#include <plugin_auth_common.h>
```

```cpp
struct st_plugin_vio_info
```

Defined in plugin_auth_common.h:93

{#thd_mdl_service_st}

### thd_mdl_service_st

```cpp
#include <service_thd_mdl.h>
```

```cpp
struct thd_mdl_service_st
```

Defined in service_thd_mdl.h:29

{#thd_rnd_service_st}

### thd_rnd_service_st

```cpp
#include <service_thd_rnd.h>
```

```cpp
struct thd_rnd_service_st
```

Defined in service_thd_rnd.h:34

{#my_crypt_service_st}

### my_crypt_service_st

```cpp
#include <service_my_crypt.h>
```

```cpp
struct my_crypt_service_st
```

Defined in service_my_crypt.h:63

{#st_encryption_scheme}

### st_encryption_scheme

```cpp
#include <service_encryption_scheme.h>
```

```cpp
struct st_encryption_scheme
```

Defined in service_encryption_scheme.h:82

{#st_mysql_lex_string}

### st_mysql_lex_string

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct st_mysql_lex_string
```

Defined in service_thd_alloc.h:45

{#thd_wait_service_st}

### thd_wait_service_st

```cpp
#include <service_thd_wait.h>
```

```cpp
struct thd_wait_service_st
```

Defined in service_thd_wait.h:81

{#encryption_service_st}

### encryption_service_st

```cpp
#include <service_encryption.h>
```

```cpp
struct encryption_service_st
```

Defined in service_encryption.h:57

{#st_mariadb_encryption}

### st_mariadb_encryption

```cpp
#include <plugin_encryption.h>
```

```cpp
struct st_mariadb_encryption
```

Defined in plugin_encryption.h:39

Encryption plugin descriptor

{#thd_alloc_service_st}

### thd_alloc_service_st

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct thd_alloc_service_st
```

Defined in service_thd_alloc.h:59

{#mysql_event_connection}

### mysql_event_connection

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_connection
```

Defined in plugin_audit.h:89

{#my_snprintf_service_st}

### my_snprintf_service_st

```cpp
#include <service_my_snprintf.h>
```

```cpp
struct my_snprintf_service_st
```

Defined in service_my_snprintf.h:99

{#st_mysql_client_plugin}

### st_mysql_client_plugin

```cpp
#include <client_plugin.h>
```

```cpp
struct st_mysql_client_plugin
```

Defined in client_plugin.h:85

{#thd_autoinc_service_st}

### thd_autoinc_service_st

```cpp
#include <service_thd_autoinc.h>
```

```cpp
struct thd_autoinc_service_st
```

Defined in service_thd_autoinc.h:29

{#st_mysql_ftparser_param}

### st_mysql_ftparser_param

```cpp
#include <plugin_ftparser.h>
```

```cpp
struct st_mysql_ftparser_param
```

Defined in plugin_ftparser.h:184

{#st_mysql_storage_engine}

### st_mysql_storage_engine

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_storage_engine
```

Defined in plugin.h:644

{#thd_timezone_service_st}

### thd_timezone_service_st

```cpp
#include <service_thd_timezone.h>
```

```cpp
struct thd_timezone_service_st
```

Defined in service_thd_timezone.h:48

{#st_encryption_scheme_key}

### st_encryption_scheme_key

```cpp
#include <service_encryption_scheme.h>
```

```cpp
struct st_encryption_scheme_key
```

Defined in service_encryption_scheme.h:77

{#thd_specifics_service_st}

### thd_specifics_service_st

```cpp
#include <service_thd_specifics.h>
```

```cpp
struct thd_specifics_service_st
```

Defined in service_thd_specifics.h:62

{#kill_statement_service_st}

### kill_statement_service_st

```cpp
#include <service_kill_statement.h>
```

```cpp
struct kill_statement_service_st
```

Defined in service_kill_statement.h:48

{#my_print_error_service_st}

### my_print_error_service_st

```cpp
#include <service_my_print_error.h>
```

```cpp
struct my_print_error_service_st
```

Defined in service_my_print_error.h:42

{#progress_report_service_st}

### progress_report_service_st

```cpp
#include <service_progress_report.h>
```

```cpp
struct progress_report_service_st
```

Defined in service_progress_report.h:35

{#st_mysql_const_lex_string}

### st_mysql_const_lex_string

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct st_mysql_const_lex_string
```

Defined in service_thd_alloc.h:38

{#st_mysql_server_auth_info}

### st_mysql_server_auth_info

```cpp
#include <plugin_auth.h>
```

```cpp
struct st_mysql_server_auth_info
```

Defined in plugin_auth.h:48

Provides server plugin access to authentication information

{#print_check_msg_service_st}

### print_check_msg_service_st

```cpp
#include <service_print_check_msg.h>
```

```cpp
struct print_check_msg_service_st
```

Defined in service_print_check_msg.h:28

{#st_mysql_information_schema}

### st_mysql_information_schema

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_information_schema
```

Defined in plugin.h:625

{#encryption_scheme_service_st}

### encryption_scheme_service_st

```cpp
#include <service_encryption_scheme.h>
```

```cpp
struct encryption_scheme_service_st
```

Defined in service_encryption_scheme.h:92

{#thd_log_warnings_service_st}

### thd_log_warnings_service_st

```cpp
#include <service_log_warnings.h>
```

```cpp
struct thd_log_warnings_service_st
```

Defined in service_log_warnings.h:32

{#thd_error_context_service_st}

### thd_error_context_service_st

```cpp
#include <service_thd_error_context.h>
```

```cpp
struct thd_error_context_service_st
```

Defined in service_thd_error_context.h:30

{#st_mariadb_password_validation}

### st_mariadb_password_validation

```cpp
#include <plugin_password_validation.h>
```

```cpp
struct st_mariadb_password_validation
```

Defined in plugin_password_validation.h:38

Password validation plugin descriptor

{#st_mysql_ftparser_boolean_info}

### st_mysql_ftparser_boolean_info

```cpp
#include <plugin_ftparser.h>
```

```cpp
struct st_mysql_ftparser_boolean_info
```

Defined in plugin_ftparser.h:120

{#st_mysql_client_plugin_authentication}

### st_mysql_client_plugin_AUTHENTICATION

```cpp
#include <client_plugin.h>
```

```cpp
struct st_mysql_client_plugin_AUTHENTICATION
```

Defined in client_plugin.h:95

Generated by [Moxygen](https://0state.com/moxygen)