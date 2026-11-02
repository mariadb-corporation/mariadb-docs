---
description: >-
  Plugin API reference: Return Codes for the Plugin authenticate_user() Method. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Return Codes for the Plugin authenticate_user() Method

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md) / [`Authentication Plugin`](authentication_plugin.md)

## Macros

| Name | Description |
|------|-------------|
| [`CR_AUTH_PLUGIN_ERROR`](#cr_auth_plugin_error)  | Authentication failed, plugin internal error. An error occurred in the authentication plugin itself. These errors are reported in table performance_schema.host_cache, column COUNT_AUTH_PLUGIN_ERRORS. |
| [`CR_AUTH_HANDSHAKE`](#cr_auth_handshake)  | Authentication failed, client server handshake. An error occurred during the client server handshake. These errors are reported in table performance_schema.host_cache, column COUNT_HANDSHAKE_ERRORS. |
| [`CR_AUTH_USER_CREDENTIALS`](#cr_auth_user_credentials)  | Authentication failed, user credentials. For example, wrong passwords. These errors are reported in table performance_schema.host_cache, column COUNT_AUTHENTICATION_ERRORS. |
| [`CR_ERROR`](#cr_error)  | Authentication failed. Additionally, all other CR_xxx values (libmysql error code) can be used too. |
| [`CR_OK`](#cr_ok)  | Authentication (client part) was successful. It does not mean that the authentication as a whole was successful, usually it only means that the client was able to send the user name and the password to the server. If CR_OK is returned, the libmysql reads the next packet expecting it to be one of OK, ERROR, or CHANGE_PLUGIN packets. |
| [`CR_OK_HANDSHAKE_COMPLETE`](#cr_ok_handshake_complete)  | Authentication was successful. It means that the client has done its part successfully and also that a plugin has read the last packet (one of OK, ERROR, CHANGE_PLUGIN). In this case, libmysql will not read a packet from the server, but it will use the data at mysql->net.read_pos. |

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

