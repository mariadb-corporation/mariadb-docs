---
description: >-
  Plugin API reference: Authentication Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Authentication Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for Authentication plugin. ([MYSQL_AUTHENTICATION_PLUGIN](api.md#mysql_authentication_plugin))

## Groups

| Name | Description |
|------|-------------|
| [`Values for st_mysql_server_auth_info.password_used`](authentication_plugin_password_used.md) |  |
| [`Return Codes for the Plugin authenticate_user() Method`](authentication_plugin_return_codes.md) |  |

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_server_auth_info`](#st_mysql_server_auth_info) | Provides server plugin access to authentication information |
| [`st_mysql_auth`](#st_mysql_auth) | Server authentication plugin descriptor |
| [`st_plugin_vio_info`](#st_plugin_vio_info) |  |
| [`st_plugin_vio`](#st_plugin_vio) | Provides plugin access to communication channel |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_AUTHENTICATION_INTERFACE_VERSION`](#mysql_authentication_interface_version)  |  |
| [`MYSQL_USERNAME_LENGTH`](#mysql_username_length)  | the max allowed length for a user name |

---

### MYSQL_AUTHENTICATION_INTERFACE_VERSION

```cpp
#define MYSQL_AUTHENTICATION_INTERFACE_VERSION 0x0203
```

Defined in plugin_auth.h:37

---

### MYSQL_USERNAME_LENGTH

```cpp
#define MYSQL_USERNAME_LENGTH 512
```

Defined in plugin_auth_common.h:37

the max allowed length for a user name

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| struct [`st_mysql_server_auth_info`](#st_mysql_server_auth_info) | [`MYSQL_SERVER_AUTH_INFO`](#mysql_server_auth_info)  | Provides server plugin access to authentication information |
| struct [`st_plugin_vio_info`](#st_plugin_vio_info) | [`MYSQL_PLUGIN_VIO_INFO`](#mysql_plugin_vio_info)  |  |
| struct [`st_plugin_vio`](#st_plugin_vio) | [`MYSQL_PLUGIN_VIO`](#mysql_plugin_vio)  | Provides plugin access to communication channel |

---

### MYSQL_SERVER_AUTH_INFO

```cpp
using MYSQL_SERVER_AUTH_INFO = struct st_mysql_server_auth_info
```

Type: struct [`st_mysql_server_auth_info`](#st_mysql_server_auth_info)

Defined in plugin_auth.h:128

Provides server plugin access to authentication information

---

### MYSQL_PLUGIN_VIO_INFO

```cpp
using MYSQL_PLUGIN_VIO_INFO = struct st_plugin_vio_info
```

Type: struct [`st_plugin_vio_info`](#st_plugin_vio_info)

Defined in plugin_auth_common.h:110

---

### MYSQL_PLUGIN_VIO

```cpp
using MYSQL_PLUGIN_VIO = struct st_plugin_vio
```

Type: struct [`st_plugin_vio`](#st_plugin_vio)

Defined in plugin_auth_common.h:139

Provides plugin access to communication channel


## Class Definitions



### st_mysql_server_auth_info

```cpp
#include <plugin_auth.h>
```

```cpp
struct st_mysql_server_auth_info
```

Defined in plugin_auth.h:59

Provides server plugin access to authentication information

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const char *` | [`user_name`](#user_name)  | User name as sent by the client and shown in USER(). NULL if the client packet with the user name was not received yet. |
| `unsigned int` | [`user_name_length`](#user_name_length)  | Length of user_name |
| `const char *` | [`auth_string`](#auth_string)  | A corresponding column value from the mysql.user table for the matching account name or the preprocessed value, if preprocess_hash method is not NULL |
| `unsigned long` | [`auth_string_length`](#auth_string_length)  | Length of auth_string |
| `char` | [`authenticated_as`](#authenticated_as)  | Matching account name as found in the mysql.user table. A plugin can override it with another name that will be used by MySQL for authorization, and shown in CURRENT_USER() |
| `char` | [`external_user`](#external_user)  | The unique user name that was used by the plugin to authenticate. Not used by the server. Available through the @EXTERNAL_USER variable. |
| `int` | [`password_used`](#password_used)  | This only affects the "Authentication failed. Password used: @%s" error message. has the following values: |
| `const char *` | [`host_or_ip`](#host_or_ip)  | Set to the name of the connected client host, if it can be resolved, or to its IP address otherwise. |
| `unsigned int` | [`host_or_ip_length`](#host_or_ip_length)  | Length of host_or_ip |
| [`MYSQL_THD`](api.md#mysql_thd) | [`thd`](#thd)  | Current THD pointer (to use with various services) |

---

#### user_name

```cpp
const char * user_name
```

Defined in plugin_auth.h:65

User name as sent by the client and shown in USER(). NULL if the client packet with the user name was not received yet.

---

#### user_name_length

```cpp
unsigned int user_name_length
```

Defined in plugin_auth.h:70

Length of user_name

---

#### auth_string

```cpp
const char * auth_string
```

Defined in plugin_auth.h:77

A corresponding column value from the mysql.user table for the matching account name or the preprocessed value, if preprocess_hash method is not NULL

---

#### auth_string_length

```cpp
unsigned long auth_string_length
```

Defined in plugin_auth.h:82

Length of auth_string

---

#### authenticated_as

```cpp
char authenticated_as[MYSQL_USERNAME_LENGTH+1]
```

Defined in plugin_auth.h:89

Matching account name as found in the mysql.user table. A plugin can override it with another name that will be used by MySQL for authorization, and shown in CURRENT_USER()

---

#### external_user

```cpp
char external_user[MYSQL_USERNAME_LENGTH+1]
```

Defined in plugin_auth.h:97

The unique user name that was used by the plugin to authenticate. Not used by the server. Available through the @EXTERNAL_USER variable.

---

#### password_used

```cpp
int password_used
```

Defined in plugin_auth.h:110

This only affects the "Authentication failed. Password used: @%s" error message. has the following values:

* PASSWORD_USED_NO: %s will be NO.
* PASSWORD_USED_YES: %s will be YES.
* PASSWORD_USED_NO_MENTION: there will be no %s.

Set it as appropriate or ignore at will.

**See also**: [Values for st_mysql_server_auth_info.password_used](authentication_plugin_password_used.md)

---

#### host_or_ip

```cpp
const char * host_or_ip
```

Defined in plugin_auth.h:116

Set to the name of the connected client host, if it can be resolved, or to its IP address otherwise.

---

#### host_or_ip_length

```cpp
unsigned int host_or_ip_length
```

Defined in plugin_auth.h:121

Length of host_or_ip

---

#### thd

```cpp
MYSQL_THD thd
```

Type: [`MYSQL_THD`](api.md#mysql_thd)

Defined in plugin_auth.h:126

Current THD pointer (to use with various services)



### st_mysql_auth

```cpp
#include <plugin_auth.h>
```

```cpp
struct st_mysql_auth
```

Defined in plugin_auth.h:133

Server authentication plugin descriptor

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version)  | version plugin uses |
| `const char *` | [`client_auth_plugin`](#client_auth_plugin)  | A plugin that a client must use for authentication with this server plugin. Can be NULL to mean "any plugin". |
| `int(*` | [`authenticate_user`](#authenticate_user)  | Function provided by the plugin which should perform authentication (using the vio functions if necessary) and return 0 if successful. The plugin can also fill the info.authenticated_as field if a different username should be used for authorization. |
| `int(*` | [`hash_password`](#hash_password)  | Create a password hash (or digest) out of a plain-text password |
| `int(*` | [`preprocess_hash`](#preprocess_hash)  | Prepare the password hash for authentication. |

---

#### interface_version

```cpp
int interface_version
```

Defined in plugin_auth.h:135

version plugin uses

---

#### client_auth_plugin

```cpp
const char * client_auth_plugin
```

Defined in plugin_auth.h:140

A plugin that a client must use for authentication with this server plugin. Can be NULL to mean "any plugin".

---

#### authenticate_user

```cpp
int(* authenticate_user)(MYSQL_PLUGIN_VIO *vio, MYSQL_SERVER_AUTH_INFO *info)
```

Defined in plugin_auth.h:147

Function provided by the plugin which should perform authentication (using the vio functions if necessary) and return 0 if successful. The plugin can also fill the info.authenticated_as field if a different username should be used for authorization.

---

#### hash_password

```cpp
int(* hash_password)(const char *password, size_t password_length, char *hash, size_t *hash_length)
```

Defined in plugin_auth.h:167

Create a password hash (or digest) out of a plain-text password

Used in SET PASSWORD, GRANT, and CREATE USER to convert user specified plain-text password into a value that will be stored in mysql.user table.

**See also**: [preprocess_hash](#preprocess_hash)

#### Returns
0 for ok, 1 for error

Can be NULL, in this case one will not be able to use SET PASSWORD or PASSWORD('...') in GRANT, CREATE USER, ALTER USER.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `password` |  | plain-text password |
| `password_length` |  | plain-text password length |
| `hash` |  | the digest will be stored there |
| `hash_length` |  | in: hash buffer size out: the actual length of the hash |

---

#### preprocess_hash

```cpp
int(* preprocess_hash)(const char *hash, size_t hash_length, unsigned char *out, size_t *out_length)
```

Defined in plugin_auth.h:188

Prepare the password hash for authentication.

Password hash is stored in the authentication_string column of the mysql.user table in a text form. If a plugin needs to preprocess the value somehow before the authentication (e.g. convert from hex or base64 to binary), it can do it in this method. This way the conversion will happen only once, not for every authentication attempt.

The value written to the out buffer will be cached and later made available to the [authenticate_user()](#authenticate_user) method in the [MYSQL_SERVER_AUTH_INFO::auth_string](#auth_string)[] buffer.

#### Returns
0 for ok, 1 for error

Can be NULL, in this case the mysql.user.authentication_string value will be given to the [authenticate_user()](#authenticate_user) method as is, unconverted.



### st_plugin_vio_info

```cpp
#include <plugin_auth_common.h>
```

```cpp
struct st_plugin_vio_info
```

Defined in plugin_auth_common.h:101

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `enum st_plugin_vio_info::@0` | [`protocol`](#protocol)  |  |
| `int` | [`socket`](#socket)  | it's set, if the protocol is SOCKET or TCP |
| `int` | [`tls`](#tls)  |  |

---

#### protocol

```cpp
enum st_plugin_vio_info::@0 protocol
```

Defined in plugin_auth_common.h:104

---

#### socket

```cpp
int socket
```

Defined in plugin_auth_common.h:105

it's set, if the protocol is SOCKET or TCP

---

#### tls

```cpp
int tls
```

Defined in plugin_auth_common.h:109

#### Public Types

| Name | Description |
|------|-------------|
| [`@0`](#id-0)  |  |

---

#### @0

```cpp
enum @0
```

Defined in plugin_auth_common.h:103

| Value | Description |
|-------|-------------|
| `MYSQL_VIO_INVALID` |  |
| `MYSQL_VIO_TCP` |  |
| `MYSQL_VIO_SOCKET` |  |
| `MYSQL_VIO_PIPE` |  |
| `MYSQL_VIO_MEMORY` |  |


### st_plugin_vio

```cpp
#include <plugin_auth_common.h>
```

```cpp
struct st_plugin_vio
```

Defined in plugin_auth_common.h:115

Provides plugin access to communication channel

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`read_packet`](#read_packet)  | Plugin provides a pointer reference and this function sets it to the contents of any incoming packet. Returns the packet length, or -1 if the plugin should terminate. |
| `int(*` | [`write_packet`](#write_packet)  | Plugin provides a buffer with data and the length and this function sends it as a packet. Returns 0 on success, 1 on failure. |
| `void(*` | [`info`](#info)  | Fills in a [st_plugin_vio_info](#st_plugin_vio_info) structure, providing the information about the connection. |

---

#### read_packet

```cpp
int(* read_packet)(struct st_plugin_vio *vio, unsigned char **buf)
```

Defined in plugin_auth_common.h:122

Plugin provides a pointer reference and this function sets it to the contents of any incoming packet. Returns the packet length, or -1 if the plugin should terminate.

---

#### write_packet

```cpp
int(* write_packet)(struct st_plugin_vio *vio, const unsigned char *packet, int packet_len)
```

Defined in plugin_auth_common.h:129

Plugin provides a buffer with data and the length and this function sends it as a packet. Returns 0 on success, 1 on failure.

---

#### info

```cpp
void(* info)(struct st_plugin_vio *vio, struct st_plugin_vio_info *info)
```

Defined in plugin_auth_common.h:137

Fills in a [st_plugin_vio_info](#st_plugin_vio_info) structure, providing the information about the connection.

