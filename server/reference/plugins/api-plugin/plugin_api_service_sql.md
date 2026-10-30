---
description: >-
  Plugin API reference: SQL Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# SQL Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

SQL Service

Interface for plugins to execute SQL queries on the local server.

Functions of the service are the 'server-limited' client library:

* [mysql_init](#mysql_init)
* [mysql_real_connect_local](#mysql_real_connect_local)
* [mysql_real_connect](#mysql_real_connect)
* [mysql_errno](#mysql_errno)
* [mysql_error](#mysql_error)
* [mysql_real_query](#mysql_real_query)
* [mysql_affected_rows](#mysql_affected_rows)
* [mysql_num_rows](#mysql_num_rows)
* [mysql_store_result](#mysql_store_result)
* [mysql_free_result](#mysql_free_result)
* [mysql_fetch_row](#mysql_fetch_row)
* [mysql_close](#mysql_close)

## Classes

| Name | Description |
|------|-------------|
| [`sql_service_st`](#sql_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`mysql_init`](#mysql_init)  |  |
| [`mysql_real_connect_local`](#mysql_real_connect_local)  |  |
| [`mysql_real_connect`](#mysql_real_connect)  |  |
| [`mysql_errno`](#mysql_errno)  |  |
| [`mysql_error`](#mysql_error)  |  |
| [`mysql_real_query`](#mysql_real_query)  |  |
| [`mysql_affected_rows`](#mysql_affected_rows)  |  |
| [`mysql_num_rows`](#mysql_num_rows)  |  |
| [`mysql_store_result`](#mysql_store_result)  |  |
| [`mysql_free_result`](#mysql_free_result)  |  |
| [`mysql_fetch_row`](#mysql_fetch_row)  |  |
| [`mysql_close`](#mysql_close)  |  |
| [`mysql_options`](#mysql_options)  |  |
| [`mysql_fetch_lengths`](#mysql_fetch_lengths)  |  |
| [`mysql_set_character_set`](#mysql_set_character_set)  |  |
| [`mysql_num_fields`](#mysql_num_fields)  |  |
| [`mysql_select_db`](#mysql_select_db)  |  |
| [`mysql_use_result`](#mysql_use_result)  |  |
| [`mysql_fetch_fields`](#mysql_fetch_fields)  |  |
| [`mysql_real_escape_string`](#mysql_real_escape_string)  |  |
| [`mysql_ssl_set`](#mysql_ssl_set)  |  |

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

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`sql_service_st`](#sql_service_st) * | [`sql_service`](#sql_service)  |  |

---

### sql_service

```cpp
struct sql_service_st * sql_service
```

Type: struct [`sql_service_st`](#sql_service_st) *

Defined in service_sql.h:86


## Class Definitions



### sql_service_st

```cpp
#include <service_sql.h>
```

```cpp
struct sql_service_st
```

Defined in service_sql.h:58

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `MYSQL *(*` | [`mysql_real_connect_local_func`](#mysql_real_connect_local_func)  |  |
| `const char *` | [`q`](#q)  |  |
| const char unsigned [`long`](#long) | [`length`](#length)  |  |
| enum mysql_option option const [`void`](#void) * | [`arg`](#arg)  |  |
| `const char *` | [`cs_name`](#cs_name)  |  |
| `const char *` | [`db`](#db)  |  |
| `unsigned char *` | [`to`](#to)  |  |
| `unsigned char const char *` | [`from`](#from)  |  |
| unsigned char const char unsigned [`long`](#long) | [`length`](#length-1)  |  |
| `const char *` | [`key`](#key)  |  |
| `const char const char *` | [`cert`](#cert)  |  |
| `const char const char const char *` | [`ca`](#ca)  |  |
| `const char const char const char const char *` | [`capath`](#capath)  |  |
| `const char const char const char const char const char *` | [`cipher`](#cipher)  |  |

---

#### mysql_real_connect_local_func

```cpp
MYSQL *(* mysql_real_connect_local_func)(MYSQL *mysql)
```

Defined in service_sql.h:60

---

#### q

```cpp
const char * q
```

Defined in service_sql.h:66

---

#### length

```cpp
const char unsigned long length
```

Type: const char unsigned [`long`](#long)

Defined in service_sql.h:67

---

#### arg

```cpp
enum mysql_option option const void * arg
```

Type: enum mysql_option option const [`void`](#void) *

Defined in service_sql.h:75

---

#### cs_name

```cpp
const char * cs_name
```

Defined in service_sql.h:77

---

#### db

```cpp
const char * db
```

Defined in service_sql.h:79

---

#### to

```cpp
unsigned char * to
```

Defined in service_sql.h:82

---

#### from

```cpp
unsigned char const char * from
```

Defined in service_sql.h:83

---

#### length

```cpp
unsigned char const char unsigned long length
```

Type: unsigned char const char unsigned [`long`](#long)

Defined in service_sql.h:83

---

#### key

```cpp
const char * key
```

Defined in service_sql.h:84

---

#### cert

```cpp
const char const char * cert
```

Defined in service_sql.h:85

---

#### ca

```cpp
const char const char const char * ca
```

Defined in service_sql.h:85

---

#### capath

```cpp
const char const char const char const char * capath
```

Defined in service_sql.h:85

---

#### cipher

```cpp
const char const char const char const char const char * cipher
```

Defined in service_sql.h:85

#### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `MYSQL *STDCALL *` | [`mysql_init_func`](#mysql_init_func)  |  |
| `MYSQL *STDCALL *` | [`mysql_real_connect_func`](#mysql_real_connect_func)  |  |
| `unsigned` | [`int`](#int)  |  |
| `const char *STDCALL *` | [`mysql_error_func`](#mysql_error_func)  |  |
|  | [`int`](#int-1)  |  |
|  | [`my_ulonglong`](#my_ulonglong)  |  |
|  | [`my_ulonglong`](#my_ulonglong-1)  |  |
| `MYSQL_RES *STDCALL *` | [`mysql_store_result_func`](#mysql_store_result_func)  |  |
|  | [`void`](#void)  |  |
|  | [`MYSQL_ROW`](#mysql_row)  |  |
|  | [`void`](#void-1)  |  |
|  | [`int`](#int-2)  |  |
| unsigned [`long`](#long) *STDCALL * | [`mysql_fetch_lengths_func`](#mysql_fetch_lengths_func)  |  |
|  | [`int`](#int-3)  |  |
| `unsigned` | [`int`](#int-4)  |  |
|  | [`int`](#int-5)  |  |
| `MYSQL_RES *STDCALL *` | [`mysql_use_result_func`](#mysql_use_result_func)  |  |
| `MYSQL_FIELD *STDCALL *` | [`mysql_fetch_fields_func`](#mysql_fetch_fields_func)  |  |
| `unsigned` | [`long`](#long)  |  |
|  | [`my_bool`](#my_bool)  |  |

---

#### mysql_init_func

```cpp
MYSQL *STDCALL * mysql_init_func(MYSQL * mysql)
```

Defined in service_sql.h:59

---

#### mysql_real_connect_func

```cpp
MYSQL *STDCALL * mysql_real_connect_func(MYSQL * mysql, const char * host, const char * user, const char * passwd, const char * db, unsigned int port, const char * unix_socket, unsigned long clientflag)
```

Defined in service_sql.h:61

---

#### int

```cpp
unsigned int(STDCALL * mysql_errno_func)
```

Defined in service_sql.h:64

---

#### mysql_error_func

```cpp
const char *STDCALL * mysql_error_func(MYSQL * mysql)
```

Defined in service_sql.h:65

---

#### int

```cpp
int(STDCALL * mysql_real_query_func)
```

Defined in service_sql.h:66

---

#### my_ulonglong

```cpp
my_ulonglong(STDCALL * mysql_affected_rows_func)
```

Defined in service_sql.h:68

---

#### my_ulonglong

```cpp
my_ulonglong(STDCALL * mysql_num_rows_func)
```

Defined in service_sql.h:69

---

#### mysql_store_result_func

```cpp
MYSQL_RES *STDCALL * mysql_store_result_func(MYSQL * mysql)
```

Defined in service_sql.h:70

---

#### void

```cpp
void(STDCALL * mysql_free_result_func)
```

Defined in service_sql.h:71

---

#### MYSQL_ROW

```cpp
MYSQL_ROW(STDCALL * mysql_fetch_row_func)
```

Defined in service_sql.h:72

---

#### void

```cpp
void(STDCALL * mysql_close_func)
```

Defined in service_sql.h:73

---

#### int

```cpp
int(STDCALL * mysql_options_func)
```

Defined in service_sql.h:74

---

#### mysql_fetch_lengths_func

```cpp
unsigned long *STDCALL * mysql_fetch_lengths_func(MYSQL_RES * res)
```

Defined in service_sql.h:76

---

#### int

```cpp
int(STDCALL * mysql_set_character_set_func)
```

Defined in service_sql.h:77

---

#### int

```cpp
unsigned int(STDCALL * mysql_num_fields_func)
```

Defined in service_sql.h:78

---

#### int

```cpp
int(STDCALL * mysql_select_db_func)
```

Defined in service_sql.h:79

---

#### mysql_use_result_func

```cpp
MYSQL_RES *STDCALL * mysql_use_result_func(MYSQL * mysql)
```

Defined in service_sql.h:80

---

#### mysql_fetch_fields_func

```cpp
MYSQL_FIELD *STDCALL * mysql_fetch_fields_func(MYSQL_RES * res)
```

Defined in service_sql.h:81

---

#### long

```cpp
unsigned long(STDCALL * mysql_real_escape_string_func)
```

Defined in service_sql.h:82

---

#### my_bool

```cpp
my_bool(STDCALL * mysql_ssl_set_func)
```

Defined in service_sql.h:84

