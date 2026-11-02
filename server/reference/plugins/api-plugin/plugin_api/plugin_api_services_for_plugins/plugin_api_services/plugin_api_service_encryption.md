---
description: >-
  Plugin API reference: Encryption Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# Encryption Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

Functions to support data encryption and encryption key management.

They are normally implemented in an encryption plugin, so this service connects encryption _consumers_ (e.g. storage engines) to the encryption provider\* (encryption plugin).

## Classes

| Name                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [`encryption_service_st`](plugin_api_service_encryption.md#encryption_service_st) |             |

## Macros

| Name                                                                                                      | Description |
| --------------------------------------------------------------------------------------------------------- | ----------- |
| [`ENCRYPTION_KEY_VERSION_INVALID`](plugin_api_service_encryption.md#encryption_key_version_invalid)       |             |
| [`ENCRYPTION_KEY_NOT_ENCRYPTED`](plugin_api_service_encryption.md#encryption_key_not_encrypted)           |             |
| [`ENCRYPTION_KEY_SYSTEM_DATA`](plugin_api_service_encryption.md#encryption_key_system_data)               |             |
| [`ENCRYPTION_KEY_TEMPORARY_DATA`](plugin_api_service_encryption.md#encryption_key_temporary_data)         |             |
| [`ENCRYPTION_KEY_BUFFER_TOO_SMALL`](plugin_api_service_encryption.md#encryption_key_buffer_too_small)     |             |
| [`ENCRYPTION_FLAG_DECRYPT`](plugin_api_service_encryption.md#encryption_flag_decrypt)                     |             |
| [`ENCRYPTION_FLAG_ENCRYPT`](plugin_api_service_encryption.md#encryption_flag_encrypt)                     |             |
| [`ENCRYPTION_FLAG_NOPAD`](plugin_api_service_encryption.md#encryption_flag_nopad)                         |             |
| [`encryption_key_get_latest_version`](plugin_api_service_encryption.md#encryption_key_get_latest_version) |             |
| [`encryption_key_get`](plugin_api_service_encryption.md#encryption_key_get)                               |             |
| [`encryption_ctx_size`](plugin_api_service_encryption.md#encryption_ctx_size)                             |             |
| [`encryption_ctx_init`](plugin_api_service_encryption.md#encryption_ctx_init)                             |             |
| [`encryption_ctx_update`](plugin_api_service_encryption.md#encryption_ctx_update)                         |             |
| [`encryption_ctx_finish`](plugin_api_service_encryption.md#encryption_ctx_finish)                         |             |
| [`encryption_encrypted_length`](plugin_api_service_encryption.md#encryption_encrypted_length)             |             |

***

### ENCRYPTION\_KEY\_VERSION\_INVALID

```cpp
#define ENCRYPTION_KEY_VERSION_INVALID (~(unsigned int)0)
```

Defined in service\_encryption.h:48

***

### ENCRYPTION\_KEY\_NOT\_ENCRYPTED

```cpp
#define ENCRYPTION_KEY_NOT_ENCRYPTED (0)
```

Defined in service\_encryption.h:49

***

### ENCRYPTION\_KEY\_SYSTEM\_DATA

```cpp
#define ENCRYPTION_KEY_SYSTEM_DATA 1
```

Defined in service\_encryption.h:51

***

### ENCRYPTION\_KEY\_TEMPORARY\_DATA

```cpp
#define ENCRYPTION_KEY_TEMPORARY_DATA 2
```

Defined in service\_encryption.h:52

***

### ENCRYPTION\_KEY\_BUFFER\_TOO\_SMALL

```cpp
#define ENCRYPTION_KEY_BUFFER_TOO_SMALL (100)
```

Defined in service\_encryption.h:55

***

### ENCRYPTION\_FLAG\_DECRYPT

```cpp
#define ENCRYPTION_FLAG_DECRYPT 0
```

Defined in service\_encryption.h:57

***

### ENCRYPTION\_FLAG\_ENCRYPT

```cpp
#define ENCRYPTION_FLAG_ENCRYPT 1
```

Defined in service\_encryption.h:58

***

### ENCRYPTION\_FLAG\_NOPAD

```cpp
#define ENCRYPTION_FLAG_NOPAD 2
```

Defined in service\_encryption.h:59

***

### encryption\_key\_get\_latest\_version

```cpp
#define encryption_key_get_latest_version(KI, KI) encryption_service->encryption_key_get_latest_version_func(KI)
```

Defined in service\_encryption.h:80

***

### encryption\_key\_get

```cpp
#define encryption_key_get(KI, KV, K, S, KI, KV, K, S) encryption_service->encryption_key_get_func((KI),(KV),(K),(S))
```

Defined in service\_encryption.h:81

***

### encryption\_ctx\_size

```cpp
#define encryption_ctx_size(KI, KV, KI, KV) encryption_service->encryption_ctx_size_func((KI),(KV))
```

Defined in service\_encryption.h:82

***

### encryption\_ctx\_init

```cpp
#define encryption_ctx_init(CTX, K, KL, IV, IVL, F, KI, KV, CTX, K, KL, IV, IVL, F, KI, KV) encryption_service->encryption_ctx_init_func((CTX),(K),(KL),(IV),(IVL),(F),(KI),(KV))
```

Defined in service\_encryption.h:83

***

### encryption\_ctx\_update

```cpp
#define encryption_ctx_update(CTX, S, SL, D, DL, CTX, S, SL, D, DL) encryption_service->encryption_ctx_update_func((CTX),(S),(SL),(D),(DL))
```

Defined in service\_encryption.h:84

***

### encryption\_ctx\_finish

```cpp
#define encryption_ctx_finish(CTX, D, DL, CTX, D, DL) encryption_service->encryption_ctx_finish_func((CTX),(D),(DL))
```

Defined in service\_encryption.h:85

***

### encryption\_encrypted\_length

```cpp
#define encryption_encrypted_length(SL, KI, KV, SL, KI, KV) encryption_service->encryption_encrypted_length_func((SL),(KI),(KV))
```

Defined in service\_encryption.h:86

## Functions

| Return         | Name                                                                                                                | Description                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| `unsigned int` | [`encryption_key_id_exists`](plugin_api_service_encryption.md#encryption_key_id_exists) `static` `inline`           |                                                     |
| `unsigned int` | [`encryption_key_version_exists`](plugin_api_service_encryption.md#encryption_key_version_exists) `static` `inline` |                                                     |
| `int`          | [`encryption_crypt`](plugin_api_service_encryption.md#encryption_crypt) `static` `inline`                           | main entrypoint to perform encryption or decryption |

***

### encryption\_key\_id\_exists

`static` `inline`

```cpp
static inline unsigned int encryption_key_id_exists(unsigned int id, unsigned int id)
```

Defined in service\_encryption.h:100

***

### encryption\_key\_version\_exists

`static` `inline`

```cpp
static inline unsigned int encryption_key_version_exists(unsigned int id, unsigned int version, unsigned int id, unsigned int version)
```

Defined in service\_encryption.h:105

***

### encryption\_crypt

`static` `inline`

```cpp
static inline int encryption_crypt(const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen, int flags, unsigned int key_id, unsigned int key_version, const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen, int flags, unsigned int key_id, unsigned int key_version)
```

Defined in service\_encryption.h:116

main entrypoint to perform encryption or decryption

#### Invariants

`src` is valid for `slen`

#### Invariants

`dst` is valid for `*dlen`, `*dlen` is initialized

#### Invariants

`src` and `dst` do not overlap

## Variables

| Return                                                                                      | Name                                                                        | Description |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------- |
| struct [`encryption_service_st`](plugin_api_service_encryption.md#encryption_service_st) \* | [`encryption_service`](plugin_api_service_encryption.md#encryption_service) |             |

***

### encryption\_service

```cpp
struct encryption_service_st * encryption_service
```

Type: struct [`encryption_service_st`](plugin_api_service_encryption.md#encryption_service_st) \*

Defined in service\_encryption.h:78

## Class Definitions

### encryption\_service\_st

```cpp
#include <service_encryption.h>
```

```cpp
struct encryption_service_st
```

Defined in service\_encryption.h:61

#### Public Attributes

| Return           | Name                                                                                                                | Description |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- | ----------- |
| `unsigned int(*` | [`encryption_key_get_latest_version_func`](plugin_api_service_encryption.md#encryption_key_get_latest_version_func) |             |
| `unsigned int(*` | [`encryption_key_get_func`](plugin_api_service_encryption.md#encryption_key_get_func)                               |             |
| `unsigned int(*` | [`encryption_ctx_size_func`](plugin_api_service_encryption.md#encryption_ctx_size_func)                             |             |
| `int(*`          | [`encryption_ctx_init_func`](plugin_api_service_encryption.md#encryption_ctx_init_func)                             |             |
| `int(*`          | [`encryption_ctx_update_func`](plugin_api_service_encryption.md#encryption_ctx_update_func)                         |             |
| `int(*`          | [`encryption_ctx_finish_func`](plugin_api_service_encryption.md#encryption_ctx_finish_func)                         |             |
| `unsigned int(*` | [`encryption_encrypted_length_func`](plugin_api_service_encryption.md#encryption_encrypted_length_func)             |             |

***

#### encryption\_key\_get\_latest\_version\_func

```cpp
unsigned int(* encryption_key_get_latest_version_func)(unsigned int key_id)
```

Defined in service\_encryption.h:62

***

#### encryption\_key\_get\_func

```cpp
unsigned int(* encryption_key_get_func)(unsigned int key_id, unsigned int key_version, unsigned char *buffer, unsigned int *length)
```

Defined in service\_encryption.h:63

***

#### encryption\_ctx\_size\_func

```cpp
unsigned int(* encryption_ctx_size_func)(unsigned int key_id, unsigned int key_version)
```

Defined in service\_encryption.h:65

***

#### encryption\_ctx\_init\_func

```cpp
int(* encryption_ctx_init_func)(void *ctx, const unsigned char *key, unsigned int klen, const unsigned char *iv, unsigned int ivlen, int flags, unsigned int key_id, unsigned int key_version)
```

Defined in service\_encryption.h:66

***

#### encryption\_ctx\_update\_func

```cpp
int(* encryption_ctx_update_func)(void *ctx, const unsigned char *src, unsigned int slen, unsigned char *dst, unsigned int *dlen)
```

Defined in service\_encryption.h:70

***

#### encryption\_ctx\_finish\_func

```cpp
int(* encryption_ctx_finish_func)(void *ctx, unsigned char *dst, unsigned int *dlen)
```

Defined in service\_encryption.h:72

***

#### encryption\_encrypted\_length\_func

```cpp
unsigned int(* encryption_encrypted_length_func)(unsigned int slen, unsigned int key_id, unsigned int key_version)
```

Defined in service\_encryption.h:73
