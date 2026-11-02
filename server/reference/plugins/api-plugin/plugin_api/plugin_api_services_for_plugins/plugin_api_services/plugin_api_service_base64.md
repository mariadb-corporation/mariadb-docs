---
description: >-
  Plugin API reference: Base64 Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# Base64 Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

Base64 service

Functions for base64 en- and decoding.

## Classes

| Name                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [`base64_service_st`](plugin_api_service_base64.md#base64_service_st) |             |

## Macros

| Name                                                                                                            | Description |
| --------------------------------------------------------------------------------------------------------------- | ----------- |
| [`MY_BASE64_DECODE_ALLOW_MULTIPLE_CHUNKS`](plugin_api_service_base64.md#my_base64_decode_allow_multiple_chunks) |             |
| [`my_base64_needed_encoded_length`](plugin_api_service_base64.md#my_base64_needed_encoded_length)               |             |
| [`my_base64_encode_max_arg_length`](plugin_api_service_base64.md#my_base64_encode_max_arg_length)               |             |
| [`my_base64_needed_decoded_length`](plugin_api_service_base64.md#my_base64_needed_decoded_length)               |             |
| [`my_base64_decode_max_arg_length`](plugin_api_service_base64.md#my_base64_decode_max_arg_length)               |             |
| [`my_base64_encode`](plugin_api_service_base64.md#my_base64_encode)                                             |             |
| [`my_base64_decode`](plugin_api_service_base64.md#my_base64_decode)                                             |             |

***

### MY\_BASE64\_DECODE\_ALLOW\_MULTIPLE\_CHUNKS

```cpp
#define MY_BASE64_DECODE_ALLOW_MULTIPLE_CHUNKS 1
```

Defined in service\_base64.h:45

***

### my\_base64\_needed\_encoded\_length

```cpp
#define my_base64_needed_encoded_length(A, A) base64_service->base64_needed_encoded_length_ptr(A)
```

Defined in service\_base64.h:59

***

### my\_base64\_encode\_max\_arg\_length

```cpp
#define my_base64_encode_max_arg_length() base64_service->base64_encode_max_arg_length_ptr()
```

Defined in service\_base64.h:60

***

### my\_base64\_needed\_decoded\_length

```cpp
#define my_base64_needed_decoded_length(A, A) base64_service->base64_needed_decoded_length_ptr(A)
```

Defined in service\_base64.h:61

***

### my\_base64\_decode\_max\_arg\_length

```cpp
#define my_base64_decode_max_arg_length() base64_service->base64_decode_max_arg_length_ptr()
```

Defined in service\_base64.h:62

***

### my\_base64\_encode

```cpp
#define my_base64_encode(A, B, C, A, B, C) base64_service->base64_encode_ptr(A,B,C)
```

Defined in service\_base64.h:63

***

### my\_base64\_decode

```cpp
#define my_base64_decode(A, B, C, D, E, A, B, C, D, E) base64_service->base64_decode_ptr(A,B,C,D,E)
```

Defined in service\_base64.h:64

## Variables

| Return                                                                          | Name                                                            | Description |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------- |
| struct [`base64_service_st`](plugin_api_service_base64.md#base64_service_st) \* | [`base64_service`](plugin_api_service_base64.md#base64_service) |             |

***

### base64\_service

```cpp
struct base64_service_st * base64_service
```

Type: struct [`base64_service_st`](plugin_api_service_base64.md#base64_service_st) \*

Defined in service\_base64.h:55

## Class Definitions

### base64\_service\_st

```cpp
#include <service_base64.h>
```

```cpp
struct base64_service_st
```

Defined in service\_base64.h:47

#### Public Attributes

| Return  | Name                                                                                                | Description |
| ------- | --------------------------------------------------------------------------------------------------- | ----------- |
| `int(*` | [`base64_needed_encoded_length_ptr`](plugin_api_service_base64.md#base64_needed_encoded_length_ptr) |             |
| `int(*` | [`base64_encode_max_arg_length_ptr`](plugin_api_service_base64.md#base64_encode_max_arg_length_ptr) |             |
| `int(*` | [`base64_needed_decoded_length_ptr`](plugin_api_service_base64.md#base64_needed_decoded_length_ptr) |             |
| `int(*` | [`base64_decode_max_arg_length_ptr`](plugin_api_service_base64.md#base64_decode_max_arg_length_ptr) |             |
| `int(*` | [`base64_encode_ptr`](plugin_api_service_base64.md#base64_encode_ptr)                               |             |
| `int(*` | [`base64_decode_ptr`](plugin_api_service_base64.md#base64_decode_ptr)                               |             |

***

#### base64\_needed\_encoded\_length\_ptr

```cpp
int(* base64_needed_encoded_length_ptr)(int length_of_data)
```

Defined in service\_base64.h:48

***

#### base64\_encode\_max\_arg\_length\_ptr

```cpp
int(* base64_encode_max_arg_length_ptr)(void)
```

Defined in service\_base64.h:49

***

#### base64\_needed\_decoded\_length\_ptr

```cpp
int(* base64_needed_decoded_length_ptr)(int length_of_encoded_data)
```

Defined in service\_base64.h:50

***

#### base64\_decode\_max\_arg\_length\_ptr

```cpp
int(* base64_decode_max_arg_length_ptr)()
```

Defined in service\_base64.h:51

***

#### base64\_encode\_ptr

```cpp
int(* base64_encode_ptr)(const void *src, size_t src_len, char *dst)
```

Defined in service\_base64.h:52

***

#### base64\_decode\_ptr

```cpp
int(* base64_decode_ptr)(const char *src, size_t src_len, void *dst, const char **end_ptr, int flags)
```

Defined in service\_base64.h:53
