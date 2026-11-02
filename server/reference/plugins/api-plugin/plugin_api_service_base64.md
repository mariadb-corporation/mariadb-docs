---
description: >-
  Plugin API reference: Base64 Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Base64 Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Base64 service

Functions for base64 en- and decoding.

## Classes

| Name | Description |
|------|-------------|
| [`base64_service_st`](#base64_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`MY_BASE64_DECODE_ALLOW_MULTIPLE_CHUNKS`](#my_base64_decode_allow_multiple_chunks)  |  |
| [`my_base64_needed_encoded_length`](#my_base64_needed_encoded_length)  |  |
| [`my_base64_encode_max_arg_length`](#my_base64_encode_max_arg_length)  |  |
| [`my_base64_needed_decoded_length`](#my_base64_needed_decoded_length)  |  |
| [`my_base64_decode_max_arg_length`](#my_base64_decode_max_arg_length)  |  |
| [`my_base64_encode`](#my_base64_encode)  |  |
| [`my_base64_decode`](#my_base64_decode)  |  |

---

### MY_BASE64_DECODE_ALLOW_MULTIPLE_CHUNKS

```cpp
#define MY_BASE64_DECODE_ALLOW_MULTIPLE_CHUNKS 1
```

Defined in service_base64.h:45

---

### my_base64_needed_encoded_length

```cpp
#define my_base64_needed_encoded_length(A, A) base64_service->base64_needed_encoded_length_ptr(A)
```

Defined in service_base64.h:59

---

### my_base64_encode_max_arg_length

```cpp
#define my_base64_encode_max_arg_length() base64_service->base64_encode_max_arg_length_ptr()
```

Defined in service_base64.h:60

---

### my_base64_needed_decoded_length

```cpp
#define my_base64_needed_decoded_length(A, A) base64_service->base64_needed_decoded_length_ptr(A)
```

Defined in service_base64.h:61

---

### my_base64_decode_max_arg_length

```cpp
#define my_base64_decode_max_arg_length() base64_service->base64_decode_max_arg_length_ptr()
```

Defined in service_base64.h:62

---

### my_base64_encode

```cpp
#define my_base64_encode(A, B, C, A, B, C) base64_service->base64_encode_ptr(A,B,C)
```

Defined in service_base64.h:63

---

### my_base64_decode

```cpp
#define my_base64_decode(A, B, C, D, E, A, B, C, D, E) base64_service->base64_decode_ptr(A,B,C,D,E)
```

Defined in service_base64.h:64

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`base64_service_st`](#base64_service_st) * | [`base64_service`](#base64_service)  |  |

---

### base64_service

```cpp
struct base64_service_st * base64_service
```

Type: struct [`base64_service_st`](#base64_service_st) *

Defined in service_base64.h:55


## Class Definitions



### base64_service_st

```cpp
#include <service_base64.h>
```

```cpp
struct base64_service_st
```

Defined in service_base64.h:47

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`base64_needed_encoded_length_ptr`](#base64_needed_encoded_length_ptr)  |  |
| `int(*` | [`base64_encode_max_arg_length_ptr`](#base64_encode_max_arg_length_ptr)  |  |
| `int(*` | [`base64_needed_decoded_length_ptr`](#base64_needed_decoded_length_ptr)  |  |
| `int(*` | [`base64_decode_max_arg_length_ptr`](#base64_decode_max_arg_length_ptr)  |  |
| `int(*` | [`base64_encode_ptr`](#base64_encode_ptr)  |  |
| `int(*` | [`base64_decode_ptr`](#base64_decode_ptr)  |  |

---

#### base64_needed_encoded_length_ptr

```cpp
int(* base64_needed_encoded_length_ptr)(int length_of_data)
```

Defined in service_base64.h:48

---

#### base64_encode_max_arg_length_ptr

```cpp
int(* base64_encode_max_arg_length_ptr)(void)
```

Defined in service_base64.h:49

---

#### base64_needed_decoded_length_ptr

```cpp
int(* base64_needed_decoded_length_ptr)(int length_of_encoded_data)
```

Defined in service_base64.h:50

---

#### base64_decode_max_arg_length_ptr

```cpp
int(* base64_decode_max_arg_length_ptr)()
```

Defined in service_base64.h:51

---

#### base64_encode_ptr

```cpp
int(* base64_encode_ptr)(const void *src, size_t src_len, char *dst)
```

Defined in service_base64.h:52

---

#### base64_decode_ptr

```cpp
int(* base64_decode_ptr)(const char *src, size_t src_len, void *dst, const char **end_ptr, int flags)
```

Defined in service_base64.h:53

