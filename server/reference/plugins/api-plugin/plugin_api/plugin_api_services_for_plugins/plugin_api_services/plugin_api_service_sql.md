---
description: >-
  Plugin API reference: SQL Service. Generated from the MariaDB server headers
  by doxygen and moxygen.
---

# SQL Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

SQL Service

Interface for plugins to execute SQL queries on the local server.

Functions of the service are the 'server-limited' client library:

* [mysql\_init](plugin_api_service_sql.md#mysql_init)
* [mysql\_real\_connect\_local](plugin_api_service_sql.md#mysql_real_connect_local)
* [mysql\_real\_connect](plugin_api_service_sql.md#mysql_real_connect)
* [mysql\_errno](plugin_api_service_sql.md#mysql_errno)
* [mysql\_error](plugin_api_service_sql.md#mysql_error)
* [mysql\_real\_query](plugin_api_service_sql.md#mysql_real_query)
* [mysql\_affected\_rows](plugin_api_service_sql.md#mysql_affected_rows)
* [mysql\_num\_rows](plugin_api_service_sql.md#mysql_num_rows)
* [mysql\_store\_result](plugin_api_service_sql.md#mysql_store_result)
* [mysql\_free\_result](plugin_api_service_sql.md#mysql_free_result)
* [mysql\_fetch\_row](plugin_api_service_sql.md#mysql_fetch_row)
* [mysql\_close](plugin_api_service_sql.md#mysql_close)

## Classes

| Name                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [`sql_service_st`](plugin_api_service_sql.md#sql_service_st) |             |

## Macros

| Name                                                                             | Description |
| -------------------------------------------------------------------------------- | ----------- |
| [`mysql_init`](plugin_api_service_sql.md#mysql_init)                             |             |
| [`mysql_real_connect_local`](plugin_api_service_sql.md#mysql_real_connect_local) |             |
| [`mysql_real_connect`](plugin_api_service_sql.md#mysql_real_connect)             |             |
| [`mysql_errno`](plugin_api_service_sql.md#mysql_errno)                           |             |
| [`mysql_error`](plugin_api_service_sql.md#mysql_error)                           |             |
| [`mysql_real_query`](plugin_api_service_sql.md#mysql_real_query)                 |             |
| [`mysql_affected_rows`](plugin_api_service_sql.md#mysql_affected_rows)           |             |
| [`mysql_num_rows`](plugin_api_service_sql.md#mysql_num_rows)                     |             |
| [`mysql_store_result`](plugin_api_service_sql.md#mysql_store_result)             |             |
| [`mysql_free_result`](plugin_api_service_sql.md#mysql_free_result)               |             |
| [`mysql_fetch_row`](plugin_api_service_sql.md#mysql_fetch_row)                   |             |
| [`mysql_close`](plugin_api_service_sql.md#mysql_close)                           |             |
| [`mysql_options`](plugin_api_service_sql.md#mysql_options)                       |             |
| [`mysql_fetch_lengths`](plugin_api_service_sql.md#mysql_fetch_lengths)           |             |
| [`mysql_set_character_set`](plugin_api_service_sql.md#mysql_set_character_set)   |             |
| [`mysql_num_fields`](plugin_api_service_sql.md#mysql_num_fields)                 |             |
| [`mysql_select_db`](plugin_api_service_sql.md#mysql_select_db)                   |             |
| [`mysql_use_result`](plugin_api_service_sql.md#mysql_use_result)                 |             |
| [`mysql_fetch_fields`](plugin_api_service_sql.md#mysql_fetch_fields)             |             |
| [`mysql_real_escape_string`](plugin_api_service_sql.md#mysql_real_escape_string) |             |
| [`mysql_ssl_set`](plugin_api_service_sql.md#mysql_ssl_set)                       |             |

***

### mysql\_init

```cpp
#define mysql_init(mysql, mysql) sql_service->mysql_init_func(mysql)
```

Defined in service\_sql.h:90

***

### mysql\_real\_connect\_local

```cpp
#define mysql_real_connect_local(mysql, mysql) sql_service->mysql_real_connect_local_func(mysql)
```

Defined in service\_sql.h:91

***

### mysql\_real\_connect

```cpp
#define mysql_real_connect(mysql, host, user, password, db, port, socket, flags, mysql, host, user, password, db, port, socket, flags) sql_service->mysql_real_connect_func(mysql,host,user,password,db,port,socket,flags)
```

Defined in service\_sql.h:92

***

### mysql\_errno

```cpp
#define mysql_errno(mysql, mysql) sql_service->mysql_errno_func(mysql)
```

Defined in service\_sql.h:94

***

### mysql\_error

```cpp
#define mysql_error(mysql, mysql) sql_service->mysql_error_func(mysql)
```

Defined in service\_sql.h:95

***

### mysql\_real\_query

```cpp
#define mysql_real_query sql_service->mysql_real_query_func
```

Defined in service\_sql.h:96

***

### mysql\_affected\_rows

```cpp
#define mysql_affected_rows(mysql, mysql) sql_service->mysql_affected_rows_func(mysql)
```

Defined in service\_sql.h:97

***

### mysql\_num\_rows

```cpp
#define mysql_num_rows(result, result) sql_service->mysql_num_rows_func(result)
```

Defined in service\_sql.h:98

***

### mysql\_store\_result

```cpp
#define mysql_store_result(mysql, mysql) sql_service->mysql_store_result_func(mysql)
```

Defined in service\_sql.h:99

***

### mysql\_free\_result

```cpp
#define mysql_free_result(result, result) sql_service->mysql_free_result_func(result)
```

Defined in service\_sql.h:100

***

### mysql\_fetch\_row

```cpp
#define mysql_fetch_row(result, result) sql_service->mysql_fetch_row_func(result)
```

Defined in service\_sql.h:101

***

### mysql\_close

```cpp
#define mysql_close(mysql, mysql) sql_service->mysql_close_func(mysql)
```

Defined in service\_sql.h:102

***

### mysql\_options

```cpp
#define mysql_options(mysql, option, arg, mysql, option, arg) sql_service->mysql_options_func(mysql,option,arg)
```

Defined in service\_sql.h:103

***

### mysql\_fetch\_lengths

```cpp
#define mysql_fetch_lengths(result, result) sql_service->mysql_fetch_lengths_func(result)
```

Defined in service\_sql.h:104

***

### mysql\_set\_character\_set

```cpp
#define mysql_set_character_set(mysql, cs_name, mysql, cs_name) sql_service->mysql_set_character_set_func(mysql,cs_name)
```

Defined in service\_sql.h:105

***

### mysql\_num\_fields

```cpp
#define mysql_num_fields(result, result) sql_service->mysql_num_fields_func(result)
```

Defined in service\_sql.h:106

***

### mysql\_select\_db

```cpp
#define mysql_select_db(mysql, db, mysql, db) sql_service->mysql_select_db_func(mysql,db)
```

Defined in service\_sql.h:107

***

### mysql\_use\_result

```cpp
#define mysql_use_result(mysql, mysql) sql_service->mysql_use_result_func(mysql)
```

Defined in service\_sql.h:108

***

### mysql\_fetch\_fields

```cpp
#define mysql_fetch_fields(result, result) sql_service->mysql_fetch_fields_func(result)
```

Defined in service\_sql.h:109

***

### mysql\_real\_escape\_string

```cpp
#define mysql_real_escape_string(mysql, to, from, length, mysql, to, from, length) sql_service->mysql_real_escape_string_func(mysql,to,from,length)
```

Defined in service\_sql.h:110

***

### mysql\_ssl\_set

```cpp
#define mysql_ssl_set(mysql, key, cert, ca, capath, cipher, mysql, key, cert, ca, capath, cipher) sql_service->mysql_ssl_set_func(mysql,key,cert,ca,capath,cipher)
```

Defined in service\_sql.h:111

## Variables

| Return                                                                 | Name                                                   | Description |
| ---------------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| struct [`sql_service_st`](plugin_api_service_sql.md#sql_service_st) \* | [`sql_service`](plugin_api_service_sql.md#sql_service) |             |

***

### sql\_service

```cpp
struct sql_service_st * sql_service
```

Type: struct [`sql_service_st`](plugin_api_service_sql.md#sql_service_st) \*

Defined in service\_sql.h:86

## Class Definitions

### sql\_service\_st

```cpp
#include <service_sql.h>
```

```cpp
struct sql_service_st
```

Defined in service\_sql.h:58

#### Public Attributes

| Return                                                                      | Name                                                                                       | Description |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------- |
| `MYSQL *(*`                                                                 | [`mysql_real_connect_local_func`](plugin_api_service_sql.md#mysql_real_connect_local_func) |             |
| `const char *`                                                              | [`q`](plugin_api_service_sql.md#q)                                                         |             |
| const char unsigned [`long`](plugin_api_service_sql.md#long)                | [`length`](plugin_api_service_sql.md#length)                                               |             |
| enum mysql\_option option const [`void`](plugin_api_service_sql.md#void) \* | [`arg`](plugin_api_service_sql.md#arg)                                                     |             |
| `const char *`                                                              | [`cs_name`](plugin_api_service_sql.md#cs_name)                                             |             |
| `const char *`                                                              | [`db`](plugin_api_service_sql.md#db)                                                       |             |
| `unsigned char *`                                                           | [`to`](plugin_api_service_sql.md#to)                                                       |             |
| `unsigned char const char *`                                                | [`from`](plugin_api_service_sql.md#from)                                                   |             |
| unsigned char const char unsigned [`long`](plugin_api_service_sql.md#long)  | [`length`](plugin_api_service_sql.md#length-1)                                             |             |
| `const char *`                                                              | [`key`](plugin_api_service_sql.md#key)                                                     |             |
| `const char const char *`                                                   | [`cert`](plugin_api_service_sql.md#cert)                                                   |             |
| `const char const char const char *`                                        | [`ca`](plugin_api_service_sql.md#ca)                                                       |             |
| `const char const char const char const char *`                             | [`capath`](plugin_api_service_sql.md#capath)                                               |             |
| `const char const char const char const char const char *`                  | [`cipher`](plugin_api_service_sql.md#cipher)                                               |             |

***

#### mysql\_real\_connect\_local\_func

```cpp
MYSQL *(* mysql_real_connect_local_func)(MYSQL *mysql)
```

Defined in service\_sql.h:60

***

#### q

```cpp
const char * q
```

Defined in service\_sql.h:66

***

#### length

```cpp
const char unsigned long length
```

Type: const char unsigned [`long`](plugin_api_service_sql.md#long)

Defined in service\_sql.h:67

***

#### arg

```cpp
enum mysql_option option const void * arg
```

Type: enum mysql\_option option const [`void`](plugin_api_service_sql.md#void) \*

Defined in service\_sql.h:75

***

#### cs\_name

```cpp
const char * cs_name
```

Defined in service\_sql.h:77

***

#### db

```cpp
const char * db
```

Defined in service\_sql.h:79

***

#### to

```cpp
unsigned char * to
```

Defined in service\_sql.h:82

***

#### from

```cpp
unsigned char const char * from
```

Defined in service\_sql.h:83

***

#### length

```cpp
unsigned char const char unsigned long length
```

Type: unsigned char const char unsigned [`long`](plugin_api_service_sql.md#long)

Defined in service\_sql.h:83

***

#### key

```cpp
const char * key
```

Defined in service\_sql.h:84

***

#### cert

```cpp
const char const char * cert
```

Defined in service\_sql.h:85

***

#### ca

```cpp
const char const char const char * ca
```

Defined in service\_sql.h:85

***

#### capath

```cpp
const char const char const char const char * capath
```

Defined in service\_sql.h:85

***

#### cipher

```cpp
const char const char const char const char const char * cipher
```

Defined in service\_sql.h:85

#### Public Methods

| Return                                                         | Name                                                                             | Description |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------- |
| `MYSQL *STDCALL *`                                             | [`mysql_init_func`](plugin_api_service_sql.md#mysql_init_func)                   |             |
| `MYSQL *STDCALL *`                                             | [`mysql_real_connect_func`](plugin_api_service_sql.md#mysql_real_connect_func)   |             |
| `unsigned`                                                     | [`int`](plugin_api_service_sql.md#int)                                           |             |
| `const char *STDCALL *`                                        | [`mysql_error_func`](plugin_api_service_sql.md#mysql_error_func)                 |             |
|                                                                | [`int`](plugin_api_service_sql.md#int-1)                                         |             |
|                                                                | [`my_ulonglong`](plugin_api_service_sql.md#my_ulonglong)                         |             |
|                                                                | [`my_ulonglong`](plugin_api_service_sql.md#my_ulonglong-1)                       |             |
| `MYSQL_RES *STDCALL *`                                         | [`mysql_store_result_func`](plugin_api_service_sql.md#mysql_store_result_func)   |             |
|                                                                | [`void`](plugin_api_service_sql.md#void)                                         |             |
|                                                                | [`MYSQL_ROW`](plugin_api_service_sql.md#mysql_row)                               |             |
|                                                                | [`void`](plugin_api_service_sql.md#void-1)                                       |             |
|                                                                | [`int`](plugin_api_service_sql.md#int-2)                                         |             |
| unsigned [`long`](plugin_api_service_sql.md#long) \*STDCALL \* | [`mysql_fetch_lengths_func`](plugin_api_service_sql.md#mysql_fetch_lengths_func) |             |
|                                                                | [`int`](plugin_api_service_sql.md#int-3)                                         |             |
| `unsigned`                                                     | [`int`](plugin_api_service_sql.md#int-4)                                         |             |
|                                                                | [`int`](plugin_api_service_sql.md#int-5)                                         |             |
| `MYSQL_RES *STDCALL *`                                         | [`mysql_use_result_func`](plugin_api_service_sql.md#mysql_use_result_func)       |             |
| `MYSQL_FIELD *STDCALL *`                                       | [`mysql_fetch_fields_func`](plugin_api_service_sql.md#mysql_fetch_fields_func)   |             |
| `unsigned`                                                     | [`long`](plugin_api_service_sql.md#long)                                         |             |
|                                                                | [`my_bool`](plugin_api_service_sql.md#my_bool)                                   |             |

***

#### mysql\_init\_func

```cpp
MYSQL *STDCALL * mysql_init_func(MYSQL * mysql)
```

Defined in service\_sql.h:59

***

#### mysql\_real\_connect\_func

```cpp
MYSQL *STDCALL * mysql_real_connect_func(MYSQL * mysql, const char * host, const char * user, const char * passwd, const char * db, unsigned int port, const char * unix_socket, unsigned long clientflag)
```

Defined in service\_sql.h:61

***

#### int

```cpp
unsigned int(STDCALL * mysql_errno_func)
```

Defined in service\_sql.h:64

***

#### mysql\_error\_func

```cpp
const char *STDCALL * mysql_error_func(MYSQL * mysql)
```

Defined in service\_sql.h:65

***

#### int

```cpp
int(STDCALL * mysql_real_query_func)
```

Defined in service\_sql.h:66

***

#### my\_ulonglong

```cpp
my_ulonglong(STDCALL * mysql_affected_rows_func)
```

Defined in service\_sql.h:68

***

#### my\_ulonglong

```cpp
my_ulonglong(STDCALL * mysql_num_rows_func)
```

Defined in service\_sql.h:69

***

#### mysql\_store\_result\_func

```cpp
MYSQL_RES *STDCALL * mysql_store_result_func(MYSQL * mysql)
```

Defined in service\_sql.h:70

***

#### void

```cpp
void(STDCALL * mysql_free_result_func)
```

Defined in service\_sql.h:71

***

#### MYSQL\_ROW

```cpp
MYSQL_ROW(STDCALL * mysql_fetch_row_func)
```

Defined in service\_sql.h:72

***

#### void

```cpp
void(STDCALL * mysql_close_func)
```

Defined in service\_sql.h:73

***

#### int

```cpp
int(STDCALL * mysql_options_func)
```

Defined in service\_sql.h:74

***

#### mysql\_fetch\_lengths\_func

```cpp
unsigned long *STDCALL * mysql_fetch_lengths_func(MYSQL_RES * res)
```

Defined in service\_sql.h:76

***

#### int

```cpp
int(STDCALL * mysql_set_character_set_func)
```

Defined in service\_sql.h:77

***

#### int

```cpp
unsigned int(STDCALL * mysql_num_fields_func)
```

Defined in service\_sql.h:78

***

#### int

```cpp
int(STDCALL * mysql_select_db_func)
```

Defined in service\_sql.h:79

***

#### mysql\_use\_result\_func

```cpp
MYSQL_RES *STDCALL * mysql_use_result_func(MYSQL * mysql)
```

Defined in service\_sql.h:80

***

#### mysql\_fetch\_fields\_func

```cpp
MYSQL_FIELD *STDCALL * mysql_fetch_fields_func(MYSQL_RES * res)
```

Defined in service\_sql.h:81

***

#### long

```cpp
unsigned long(STDCALL * mysql_real_escape_string_func)
```

Defined in service\_sql.h:82

***

#### my\_bool

```cpp
my_bool(STDCALL * mysql_ssl_set_func)
```

Defined in service\_sql.h:84
