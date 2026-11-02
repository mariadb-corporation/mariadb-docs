---
description: >-
  Plugin API reference: Return Codes for the Plugin authenticate_user() Method.
  Generated from the MariaDB server headers by doxygen and moxygen.
---

# Return Codes for the Plugin authenticate\_user() Method

> [`Plugin API`](../../) / [`Plugin Types`](../) / [`Authentication Plugin`](./)

## Macros

| Name                                                                                         | Description                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`CR_AUTH_PLUGIN_ERROR`](authentication_plugin_return_codes.md#cr_auth_plugin_error)         | Authentication failed, plugin internal error. An error occurred in the authentication plugin itself. These errors are reported in table performance\_schema.host\_cache, column COUNT\_AUTH\_PLUGIN\_ERRORS.                                                                                                                                    |
| [`CR_AUTH_HANDSHAKE`](authentication_plugin_return_codes.md#cr_auth_handshake)               | Authentication failed, client server handshake. An error occurred during the client server handshake. These errors are reported in table performance\_schema.host\_cache, column COUNT\_HANDSHAKE\_ERRORS.                                                                                                                                      |
| [`CR_AUTH_USER_CREDENTIALS`](authentication_plugin_return_codes.md#cr_auth_user_credentials) | Authentication failed, user credentials. For example, wrong passwords. These errors are reported in table performance\_schema.host\_cache, column COUNT\_AUTHENTICATION\_ERRORS.                                                                                                                                                                |
| [`CR_ERROR`](authentication_plugin_return_codes.md#cr_error)                                 | Authentication failed. Additionally, all other CR\_xxx values (libmysql error code) can be used too.                                                                                                                                                                                                                                            |
| [`CR_OK`](authentication_plugin_return_codes.md#cr_ok)                                       | Authentication (client part) was successful. It does not mean that the authentication as a whole was successful, usually it only means that the client was able to send the user name and the password to the server. If CR\_OK is returned, the libmysql reads the next packet expecting it to be one of OK, ERROR, or CHANGE\_PLUGIN packets. |
| [`CR_OK_HANDSHAKE_COMPLETE`](authentication_plugin_return_codes.md#cr_ok_handshake_complete) | Authentication was successful. It means that the client has done its part successfully and also that a plugin has read the last packet (one of OK, ERROR, CHANGE\_PLUGIN). In this case, libmysql will not read a packet from the server, but it will use the data at mysql->net.read\_pos.                                                     |

***

### CR\_AUTH\_PLUGIN\_ERROR

```cpp
#define CR_AUTH_PLUGIN_ERROR 3
```

Defined in plugin\_auth\_common.h:50

Authentication failed, plugin internal error. An error occurred in the authentication plugin itself. These errors are reported in table performance\_schema.host\_cache, column COUNT\_AUTH\_PLUGIN\_ERRORS.

***

### CR\_AUTH\_HANDSHAKE

```cpp
#define CR_AUTH_HANDSHAKE 2
```

Defined in plugin\_auth\_common.h:57

Authentication failed, client server handshake. An error occurred during the client server handshake. These errors are reported in table performance\_schema.host\_cache, column COUNT\_HANDSHAKE\_ERRORS.

***

### CR\_AUTH\_USER\_CREDENTIALS

```cpp
#define CR_AUTH_USER_CREDENTIALS 1
```

Defined in plugin\_auth\_common.h:64

Authentication failed, user credentials. For example, wrong passwords. These errors are reported in table performance\_schema.host\_cache, column COUNT\_AUTHENTICATION\_ERRORS.

***

### CR\_ERROR

```cpp
#define CR_ERROR 0
```

Defined in plugin\_auth\_common.h:75

Authentication failed. Additionally, all other CR\_xxx values (libmysql error code) can be used too.

The client plugin may set the error code and the error message directly in the MYSQL structure and return CR\_ERROR. If a CR\_xxx specific error code was returned, an error message in the MYSQL structure will be overwritten. If CR\_ERROR is returned without setting the error in MYSQL, CR\_UNKNOWN\_ERROR will be user.

***

### CR\_OK

```cpp
#define CR_OK -1
```

Defined in plugin\_auth\_common.h:83

Authentication (client part) was successful. It does not mean that the authentication as a whole was successful, usually it only means that the client was able to send the user name and the password to the server. If CR\_OK is returned, the libmysql reads the next packet expecting it to be one of OK, ERROR, or CHANGE\_PLUGIN packets.

***

### CR\_OK\_HANDSHAKE\_COMPLETE

```cpp
#define CR_OK_HANDSHAKE_COMPLETE -2
```

Defined in plugin\_auth\_common.h:98

Authentication was successful. It means that the client has done its part successfully and also that a plugin has read the last packet (one of OK, ERROR, CHANGE\_PLUGIN). In this case, libmysql will not read a packet from the server, but it will use the data at mysql->net.read\_pos.

A plugin may return this value if the number of roundtrips in the authentication protocol is not known in advance, and the client plugin needs to read one packet more to determine if the authentication is finished or not.

Server plugins should not return this value.
