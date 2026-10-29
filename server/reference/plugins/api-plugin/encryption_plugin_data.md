---
description: >-
  Plugin API reference: Encryption Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Encryption Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for Encryption plugin. ([MariaDB_ENCRYPTION_PLUGIN](api.md#mariadb_encryption_plugin))

The API for server plugins that manage encryption keys for MariaDB on-disk data encryption

The caller uses encryption as follows:

1. create the encryption context object of the crypt_ctx_size() bytes.
1. initialize it with crypt_ctx_init().
1. repeat crypt_ctx_update() until there are no more data to encrypt.
1. write the remaining output bytes and destroy the context object with crypt_ctx_finish().

## Classes

| Name | Description |
|------|-------------|
| [`st_mariadb_encryption`](#st_mariadb_encryption) | Encryption plugin descriptor |

## Macros

| Name | Description |
|------|-------------|
| [`MariaDB_ENCRYPTION_INTERFACE_VERSION`](#mariadb_encryption_interface_version)  |  |

---

### MariaDB_ENCRYPTION_INTERFACE_VERSION

```cpp
#define MariaDB_ENCRYPTION_INTERFACE_VERSION 0x0300
```

Defined in plugin_encryption.h:52


## Class Definitions



### st_mariadb_encryption

```cpp
#include <plugin_encryption.h>
```

```cpp
struct st_mariadb_encryption
```

Defined in plugin_encryption.h:57

Encryption plugin descriptor

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version)  | version plugin uses |
| `unsigned int(*` | [`get_latest_key_version`](#get_latest_key_version)  | function returning latest key version for a given key id |
| `unsigned int(*` | [`get_key`](#get_key)  | function returning a key for a key version |
| `unsigned int(*` | [`crypt_ctx_size`](#crypt_ctx_size)  | returns the size of the encryption context object in bytes |
| `int(*` | [`crypt_ctx_init`](#crypt_ctx_init)  | initializes the encryption context object. |
| `int(*` | [`crypt_ctx_update`](#crypt_ctx_update)  | processes (encrypts or decrypts) a chunk of data |
| `int(*` | [`crypt_ctx_finish`](#crypt_ctx_finish)  | writes the remaining output bytes and destroys the encryption context |
| `unsigned int(*` | [`encrypted_length`](#encrypted_length)  | returns the length of the encrypted data |

---

#### interface_version

```cpp
int interface_version
```

Defined in plugin_encryption.h:59

version plugin uses

---

#### get_latest_key_version

```cpp
unsigned int(* get_latest_key_version)(unsigned int key_id)
```

Defined in plugin_encryption.h:68

function returning latest key version for a given key id

#### Returns
a version or ENCRYPTION_KEY_VERSION_INVALID to indicate an error.

---

#### get_key

```cpp
unsigned int(* get_key)(unsigned int key_id, unsigned int version, unsigned char *key, unsigned int *key_length)
```

Defined in plugin_encryption.h:90

function returning a key for a key version

This method can be used to query the key length - the required buffer size - by passing key==NULL.

If the buffer size is less than the key length the content of the key buffer is undefined (the plugin is free to partially fill it with the key data or leave it untouched).

#### Returns
0 on success, or ENCRYPTION_KEY_VERSION_INVALID, ENCRYPTION_KEY_BUFFER_TOO_SMALL or any other non-zero number for errors

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `version` |  | the requested key version |
| `key` |  | the key will be stored there. Can be NULL - in which case no key will be returned |
| `key_length` |  | in: key buffer size out: the actual length of the key |

---

#### crypt_ctx_size

```cpp
unsigned int(* crypt_ctx_size)(unsigned int key_id, unsigned int key_version)
```

Defined in plugin_encryption.h:98

returns the size of the encryption context object in bytes

---

#### crypt_ctx_init

```cpp
int(* crypt_ctx_init)(void *ctx, const unsigned char *key, unsigned int klen, const unsigned char *iv, unsigned int ivlen, int flags, unsigned int key_id, unsigned int key_version)
```

Defined in plugin_encryption.h:102

initializes the encryption context object.

---

#### crypt_ctx_update

```cpp
int(* crypt_ctx_update)(void *ctx, const unsigned char *src, unsigned int slen, unsigned char *dst, unsigned int *dlen)
```

Defined in plugin_encryption.h:115

processes (encrypts or decrypts) a chunk of data

writes the output to the dst buffer. note that it might write more bytes that were in the input. or less. or none at all.

dlen points to the starting length of the output buffer. Upon return, it should be set to the number of bytes written.

---

#### crypt_ctx_finish

```cpp
int(* crypt_ctx_finish)(void *ctx, unsigned char *dst, unsigned int *dlen)
```

Defined in plugin_encryption.h:123

writes the remaining output bytes and destroys the encryption context

crypt_ctx_update might've cached part of the output in the context, this method will flush these data out.

---

#### encrypted_length

```cpp
unsigned int(* encrypted_length)(unsigned int slen, unsigned int key_id, unsigned int key_version)
```

Defined in plugin_encryption.h:132

returns the length of the encrypted data

it returns the exact length, given only the source length. which means, this API only supports encryption algorithms where the length of the encrypted data only depends on the length of the input (a.k.a. compression is not supported).

