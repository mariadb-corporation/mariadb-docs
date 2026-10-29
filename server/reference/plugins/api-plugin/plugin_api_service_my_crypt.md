---
description: >-
  Plugin API reference: My Crypt Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# My Crypt Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

AES encryption functions, and a function to generate random bytes.

Include my_config.h before this file to use CTR and GCM modes (they only work if server was compiled with openssl).

## Classes

| Name | Description |
|------|-------------|
| [`my_crypt_service_st`](#my_crypt_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`MY_AES_OK`](#my_aes_ok)  |  |
| [`MY_AES_BAD_DATA`](#my_aes_bad_data)  |  |
| [`MY_AES_OPENSSL_ERROR`](#my_aes_openssl_error)  |  |
| [`MY_AES_BAD_KEYSIZE`](#my_aes_bad_keysize)  |  |
| [`MY_AES_BLOCK_SIZE`](#my_aes_block_size)  |  |
| [`MY_AES_MAX_KEY_LENGTH`](#my_aes_max_key_length)  |  |
| [`MY_AES_CTX_SIZE`](#my_aes_ctx_size)  |  |
| [`my_aes_crypt_init`](#my_aes_crypt_init)  |  |
| [`my_aes_crypt_update`](#my_aes_crypt_update)  |  |
| [`my_aes_crypt_finish`](#my_aes_crypt_finish)  |  |
| [`my_aes_crypt`](#my_aes_crypt)  |  |
| [`my_aes_get_size`](#my_aes_get_size)  |  |
| [`my_aes_ctx_size`](#my_aes_ctx_size-1)  |  |
| [`my_random_bytes`](#my_random_bytes)  |  |
| [`my_bytes_to_key`](#my_bytes_to_key)  |  |

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

## Enumerations

| Name | Description |
|------|-------------|
| [`my_aes_mode`](#my_aes_mode)  |  |
| [`my_digest`](#my_digest)  |  |

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
## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`my_crypt_service_st`](#my_crypt_service_st) * | [`my_crypt_service`](#my_crypt_service)  |  |

---

### my_crypt_service

```cpp
struct my_crypt_service_st * my_crypt_service
```

Type: struct [`my_crypt_service_st`](#my_crypt_service_st) *

Defined in service_my_crypt.h:86


## Class Definitions



### my_crypt_service_st

```cpp
#include <service_my_crypt.h>
```

```cpp
struct my_crypt_service_st
```

Defined in service_my_crypt.h:69

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`my_aes_crypt_init`](#my_aes_crypt_init-1)  |  |
| `int(*` | [`my_aes_crypt_update`](#my_aes_crypt_update-1)  |  |
| `int(*` | [`my_aes_crypt_finish`](#my_aes_crypt_finish-1)  |  |
| `int(*` | [`my_aes_crypt`](#my_aes_crypt-1)  |  |
| `unsigned int(*` | [`my_aes_get_size`](#my_aes_get_size-1)  |  |
| `unsigned int(*` | [`my_aes_ctx_size`](#my_aes_ctx_size-2)  |  |
| `int(*` | [`my_random_bytes`](#my_random_bytes-1)  |  |
| `void(*` | [`my_bytes_to_key`](#my_bytes_to_key-1)  |  |

---

#### my_aes_crypt_init

```cpp
int(* my_aes_crypt_init)(void *ctx, enum my_aes_mode mode, int flags, const unsigned char *key, unsigned int klen, const unsigned char *iv, unsigned int ivlen)
```

Defined in service_my_crypt.h:70

---

#### my_aes_crypt_update

```cpp
int(* my_aes_crypt_update)(void *ctx, const unsigned char *src, unsigned int slen, unsigned char *dst, unsigned int *dlen)
```

Defined in service_my_crypt.h:73

---

#### my_aes_crypt_finish

```cpp
int(* my_aes_crypt_finish)(void *ctx, unsigned char *dst, unsigned int *dlen)
```

Defined in service_my_crypt.h:75

---

#### my_aes_crypt

```cpp
int(* my_aes_crypt)(enum my_aes_mode mode, int flags, const unsigned char *src, unsigned int slen, unsigned char *dst, unsigned int *dlen, const unsigned char *key, unsigned int klen, const unsigned char *iv, unsigned int ivlen)
```

Defined in service_my_crypt.h:76

---

#### my_aes_get_size

```cpp
unsigned int(* my_aes_get_size)(enum my_aes_mode mode, unsigned int source_length)
```

Defined in service_my_crypt.h:79

---

#### my_aes_ctx_size

```cpp
unsigned int(* my_aes_ctx_size)(enum my_aes_mode mode)
```

Defined in service_my_crypt.h:80

---

#### my_random_bytes

```cpp
int(* my_random_bytes)(unsigned char *buf, int num)
```

Defined in service_my_crypt.h:81

---

#### my_bytes_to_key

```cpp
void(* my_bytes_to_key)(const unsigned char *salt, const unsigned char *input, unsigned int input_len, unsigned char *key, unsigned char *iv, enum my_digest digest, unsigned int use_pbkdf2)
```

Defined in service_my_crypt.h:82

