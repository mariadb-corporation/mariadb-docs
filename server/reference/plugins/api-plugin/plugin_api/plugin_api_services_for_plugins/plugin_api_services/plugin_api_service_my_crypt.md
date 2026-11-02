---
description: >-
  Plugin API reference: My Crypt Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# My Crypt Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

AES encryption functions, and a function to generate random bytes.

Include my\_config.h before this file to use CTR and GCM modes (they only work if server was compiled with openssl).

## Classes

| Name                                                                        | Description |
| --------------------------------------------------------------------------- | ----------- |
| [`my_crypt_service_st`](plugin_api_service_my_crypt.md#my_crypt_service_st) |             |

## Macros

| Name                                                                            | Description |
| ------------------------------------------------------------------------------- | ----------- |
| [`MY_AES_OK`](plugin_api_service_my_crypt.md#my_aes_ok)                         |             |
| [`MY_AES_BAD_DATA`](plugin_api_service_my_crypt.md#my_aes_bad_data)             |             |
| [`MY_AES_OPENSSL_ERROR`](plugin_api_service_my_crypt.md#my_aes_openssl_error)   |             |
| [`MY_AES_BAD_KEYSIZE`](plugin_api_service_my_crypt.md#my_aes_bad_keysize)       |             |
| [`MY_AES_BLOCK_SIZE`](plugin_api_service_my_crypt.md#my_aes_block_size)         |             |
| [`MY_AES_MAX_KEY_LENGTH`](plugin_api_service_my_crypt.md#my_aes_max_key_length) |             |
| [`MY_AES_CTX_SIZE`](plugin_api_service_my_crypt.md#my_aes_ctx_size)             |             |
| [`my_aes_crypt_init`](plugin_api_service_my_crypt.md#my_aes_crypt_init)         |             |
| [`my_aes_crypt_update`](plugin_api_service_my_crypt.md#my_aes_crypt_update)     |             |
| [`my_aes_crypt_finish`](plugin_api_service_my_crypt.md#my_aes_crypt_finish)     |             |
| [`my_aes_crypt`](plugin_api_service_my_crypt.md#my_aes_crypt)                   |             |
| [`my_aes_get_size`](plugin_api_service_my_crypt.md#my_aes_get_size)             |             |
| [`my_aes_ctx_size`](plugin_api_service_my_crypt.md#my_aes_ctx_size-1)           |             |
| [`my_random_bytes`](plugin_api_service_my_crypt.md#my_random_bytes)             |             |
| [`my_bytes_to_key`](plugin_api_service_my_crypt.md#my_bytes_to_key)             |             |

***

### MY\_AES\_OK

```cpp
#define MY_AES_OK 0
```

Defined in service\_my\_crypt.h:43

***

### MY\_AES\_BAD\_DATA

```cpp
#define MY_AES_BAD_DATA -100
```

Defined in service\_my\_crypt.h:44

***

### MY\_AES\_OPENSSL\_ERROR

```cpp
#define MY_AES_OPENSSL_ERROR -101
```

Defined in service\_my\_crypt.h:45

***

### MY\_AES\_BAD\_KEYSIZE

```cpp
#define MY_AES_BAD_KEYSIZE -102
```

Defined in service\_my\_crypt.h:46

***

### MY\_AES\_BLOCK\_SIZE

```cpp
#define MY_AES_BLOCK_SIZE 16
```

Defined in service\_my\_crypt.h:49

***

### MY\_AES\_MAX\_KEY\_LENGTH

```cpp
#define MY_AES_MAX_KEY_LENGTH 32
```

Defined in service\_my\_crypt.h:52

***

### MY\_AES\_CTX\_SIZE

```cpp
#define MY_AES_CTX_SIZE 1040
```

Defined in service\_my\_crypt.h:54

***

### my\_aes\_crypt\_init

```cpp
#define my_aes_crypt_init(A, B, C, D, E, F, G, A, B, C, D, E, F, G) my_crypt_service->my_aes_crypt_init(A,B,C,D,E,F,G)
```

Defined in service\_my\_crypt.h:90

***

### my\_aes\_crypt\_update

```cpp
#define my_aes_crypt_update(A, B, C, D, E, A, B, C, D, E) my_crypt_service->my_aes_crypt_update(A,B,C,D,E)
```

Defined in service\_my\_crypt.h:93

***

### my\_aes\_crypt\_finish

```cpp
#define my_aes_crypt_finish(A, B, C, A, B, C) my_crypt_service->my_aes_crypt_finish(A,B,C)
```

Defined in service\_my\_crypt.h:96

***

### my\_aes\_crypt

```cpp
#define my_aes_crypt(A, B, C, D, E, F, G, H, I, J, A, B, C, D, E, F, G, H, I, J) my_crypt_service->my_aes_crypt(A,B,C,D,E,F,G,H,I,J)
```

Defined in service\_my\_crypt.h:99

***

### my\_aes\_get\_size

```cpp
#define my_aes_get_size(A, B, A, B) my_crypt_service->my_aes_get_size(A,B)
```

Defined in service\_my\_crypt.h:102

***

### my\_aes\_ctx\_size

```cpp
#define my_aes_ctx_size(A, A) my_crypt_service->my_aes_ctx_size(A)
```

Defined in service\_my\_crypt.h:105

***

### my\_random\_bytes

```cpp
#define my_random_bytes(A, B, A, B) my_crypt_service->my_random_bytes(A,B)
```

Defined in service\_my\_crypt.h:108

***

### my\_bytes\_to\_key

```cpp
#define my_bytes_to_key(A, B, C, D, E, F, G, A, B, C, D, E, F, G) my_crypt_service->my_bytes_to_key(A,B,C,D,E,F,G)
```

Defined in service\_my\_crypt.h:111

## Enumerations

| Name                                                        | Description |
| ----------------------------------------------------------- | ----------- |
| [`my_aes_mode`](plugin_api_service_my_crypt.md#my_aes_mode) |             |
| [`my_digest`](plugin_api_service_my_crypt.md#my_digest)     |             |

***

### my\_aes\_mode

```cpp
enum my_aes_mode
```

Defined in service\_my\_crypt.h:56

| Value        | Description |
| ------------ | ----------- |
| `MY_AES_ECB` |             |
| `MY_AES_CBC` |             |

***

### my\_digest

```cpp
enum my_digest
```

Defined in service\_my\_crypt.h:66

| Value              | Description |
| ------------------ | ----------- |
| `MY_DIGEST_SHA1`   |             |
| `MY_DIGEST_SHA224` |             |
| `MY_DIGEST_SHA256` |             |
| `MY_DIGEST_SHA384` |             |
| `MY_DIGEST_SHA512` |             |

## Variables

| Return                                                                                | Name                                                                  | Description |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------- |
| struct [`my_crypt_service_st`](plugin_api_service_my_crypt.md#my_crypt_service_st) \* | [`my_crypt_service`](plugin_api_service_my_crypt.md#my_crypt_service) |             |

***

### my\_crypt\_service

```cpp
struct my_crypt_service_st * my_crypt_service
```

Type: struct [`my_crypt_service_st`](plugin_api_service_my_crypt.md#my_crypt_service_st) \*

Defined in service\_my\_crypt.h:86

## Class Definitions

### my\_crypt\_service\_st

```cpp
#include <service_my_crypt.h>
```

```cpp
struct my_crypt_service_st
```

Defined in service\_my\_crypt.h:69

#### Public Attributes

| Return           | Name                                                                          | Description |
| ---------------- | ----------------------------------------------------------------------------- | ----------- |
| `int(*`          | [`my_aes_crypt_init`](plugin_api_service_my_crypt.md#my_aes_crypt_init-1)     |             |
| `int(*`          | [`my_aes_crypt_update`](plugin_api_service_my_crypt.md#my_aes_crypt_update-1) |             |
| `int(*`          | [`my_aes_crypt_finish`](plugin_api_service_my_crypt.md#my_aes_crypt_finish-1) |             |
| `int(*`          | [`my_aes_crypt`](plugin_api_service_my_crypt.md#my_aes_crypt-1)               |             |
| `unsigned int(*` | [`my_aes_get_size`](plugin_api_service_my_crypt.md#my_aes_get_size-1)         |             |
| `unsigned int(*` | [`my_aes_ctx_size`](plugin_api_service_my_crypt.md#my_aes_ctx_size-2)         |             |
| `int(*`          | [`my_random_bytes`](plugin_api_service_my_crypt.md#my_random_bytes-1)         |             |
| `void(*`         | [`my_bytes_to_key`](plugin_api_service_my_crypt.md#my_bytes_to_key-1)         |             |

***

#### my\_aes\_crypt\_init

```cpp
int(* my_aes_crypt_init)(void *ctx, enum my_aes_mode mode, int flags, const unsigned char *key, unsigned int klen, const unsigned char *iv, unsigned int ivlen)
```

Defined in service\_my\_crypt.h:70

***

#### my\_aes\_crypt\_update

```cpp
int(* my_aes_crypt_update)(void *ctx, const unsigned char *src, unsigned int slen, unsigned char *dst, unsigned int *dlen)
```

Defined in service\_my\_crypt.h:73

***

#### my\_aes\_crypt\_finish

```cpp
int(* my_aes_crypt_finish)(void *ctx, unsigned char *dst, unsigned int *dlen)
```

Defined in service\_my\_crypt.h:75

***

#### my\_aes\_crypt

```cpp
int(* my_aes_crypt)(enum my_aes_mode mode, int flags, const unsigned char *src, unsigned int slen, unsigned char *dst, unsigned int *dlen, const unsigned char *key, unsigned int klen, const unsigned char *iv, unsigned int ivlen)
```

Defined in service\_my\_crypt.h:76

***

#### my\_aes\_get\_size

```cpp
unsigned int(* my_aes_get_size)(enum my_aes_mode mode, unsigned int source_length)
```

Defined in service\_my\_crypt.h:79

***

#### my\_aes\_ctx\_size

```cpp
unsigned int(* my_aes_ctx_size)(enum my_aes_mode mode)
```

Defined in service\_my\_crypt.h:80

***

#### my\_random\_bytes

```cpp
int(* my_random_bytes)(unsigned char *buf, int num)
```

Defined in service\_my\_crypt.h:81

***

#### my\_bytes\_to\_key

```cpp
void(* my_bytes_to_key)(const unsigned char *salt, const unsigned char *input, unsigned int input_len, unsigned char *key, unsigned char *iv, enum my_digest digest, unsigned int use_pbkdf2)
```

Defined in service\_my\_crypt.h:82
