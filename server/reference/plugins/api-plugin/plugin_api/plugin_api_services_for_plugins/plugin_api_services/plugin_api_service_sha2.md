---
description: >-
  Plugin API reference: SHA2 Service. Generated from the MariaDB server headers
  by doxygen and moxygen.
---

# SHA2 Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

my sha2 service

Functions to calculate SHA2 hash from a memory buffer

## Classes

| Name                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [`my_sha2_service_st`](plugin_api_service_sha2.md#my_sha2_service_st) |             |

## Macros

| Name                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [`my_sha224`](plugin_api_service_sha2.md#my_sha224)                           |             |
| [`my_sha224_multi`](plugin_api_service_sha2.md#my_sha224_multi)               |             |
| [`my_sha224_context_size`](plugin_api_service_sha2.md#my_sha224_context_size) |             |
| [`my_sha224_init`](plugin_api_service_sha2.md#my_sha224_init)                 |             |
| [`my_sha224_input`](plugin_api_service_sha2.md#my_sha224_input)               |             |
| [`my_sha224_result`](plugin_api_service_sha2.md#my_sha224_result)             |             |
| [`my_sha256`](plugin_api_service_sha2.md#my_sha256)                           |             |
| [`my_sha256_multi`](plugin_api_service_sha2.md#my_sha256_multi)               |             |
| [`my_sha256_context_size`](plugin_api_service_sha2.md#my_sha256_context_size) |             |
| [`my_sha256_init`](plugin_api_service_sha2.md#my_sha256_init)                 |             |
| [`my_sha256_input`](plugin_api_service_sha2.md#my_sha256_input)               |             |
| [`my_sha256_result`](plugin_api_service_sha2.md#my_sha256_result)             |             |
| [`my_sha384`](plugin_api_service_sha2.md#my_sha384)                           |             |
| [`my_sha384_multi`](plugin_api_service_sha2.md#my_sha384_multi)               |             |
| [`my_sha384_context_size`](plugin_api_service_sha2.md#my_sha384_context_size) |             |
| [`my_sha384_init`](plugin_api_service_sha2.md#my_sha384_init)                 |             |
| [`my_sha384_input`](plugin_api_service_sha2.md#my_sha384_input)               |             |
| [`my_sha384_result`](plugin_api_service_sha2.md#my_sha384_result)             |             |
| [`my_sha512`](plugin_api_service_sha2.md#my_sha512)                           |             |
| [`my_sha512_multi`](plugin_api_service_sha2.md#my_sha512_multi)               |             |
| [`my_sha512_context_size`](plugin_api_service_sha2.md#my_sha512_context_size) |             |
| [`my_sha512_init`](plugin_api_service_sha2.md#my_sha512_init)                 |             |
| [`my_sha512_input`](plugin_api_service_sha2.md#my_sha512_input)               |             |
| [`my_sha512_result`](plugin_api_service_sha2.md#my_sha512_result)             |             |

***

### my\_sha224

```cpp
#define my_sha224(digest, buf, len, digest, buf, len) my_sha2_service->my_sha224_type(digest, buf, len)
```

Defined in service\_sha2.h:75

***

### my\_sha224\_multi

```cpp
#define my_sha224_multi my_sha2_service->my_sha224_multi_type
```

Defined in service\_sha2.h:76

***

### my\_sha224\_context\_size

```cpp
#define my_sha224_context_size() my_sha2_service->my_sha224_context_size_type()
```

Defined in service\_sha2.h:77

***

### my\_sha224\_init

```cpp
#define my_sha224_init(context, context) my_sha2_service->my_sha224_init_type(context)
```

Defined in service\_sha2.h:78

***

### my\_sha224\_input

```cpp
#define my_sha224_input(context, buf, len, context, buf, len) my_sha2_service->my_sha224_input_type(context, buf, len)
```

Defined in service\_sha2.h:79

***

### my\_sha224\_result

```cpp
#define my_sha224_result(context, digest, context, digest) my_sha2_service->my_sha224_result_type(context, digest)
```

Defined in service\_sha2.h:80

***

### my\_sha256

```cpp
#define my_sha256(digest, buf, len, digest, buf, len) my_sha2_service->my_sha256_type(digest, buf, len)
```

Defined in service\_sha2.h:82

***

### my\_sha256\_multi

```cpp
#define my_sha256_multi my_sha2_service->my_sha256_multi_type
```

Defined in service\_sha2.h:83

***

### my\_sha256\_context\_size

```cpp
#define my_sha256_context_size() my_sha2_service->my_sha256_context_size_type()
```

Defined in service\_sha2.h:84

***

### my\_sha256\_init

```cpp
#define my_sha256_init(context, context) my_sha2_service->my_sha256_init_type(context)
```

Defined in service\_sha2.h:85

***

### my\_sha256\_input

```cpp
#define my_sha256_input(context, buf, len, context, buf, len) my_sha2_service->my_sha256_input_type(context, buf, len)
```

Defined in service\_sha2.h:86

***

### my\_sha256\_result

```cpp
#define my_sha256_result(context, digest, context, digest) my_sha2_service->my_sha256_result_type(context, digest)
```

Defined in service\_sha2.h:87

***

### my\_sha384

```cpp
#define my_sha384(digest, buf, len, digest, buf, len) my_sha2_service->my_sha384_type(digest, buf, len)
```

Defined in service\_sha2.h:89

***

### my\_sha384\_multi

```cpp
#define my_sha384_multi my_sha2_service->my_sha384_multi_type
```

Defined in service\_sha2.h:90

***

### my\_sha384\_context\_size

```cpp
#define my_sha384_context_size() my_sha2_service->my_sha384_context_size_type()
```

Defined in service\_sha2.h:91

***

### my\_sha384\_init

```cpp
#define my_sha384_init(context, context) my_sha2_service->my_sha384_init_type(context)
```

Defined in service\_sha2.h:92

***

### my\_sha384\_input

```cpp
#define my_sha384_input(context, buf, len, context, buf, len) my_sha2_service->my_sha384_input_type(context, buf, len)
```

Defined in service\_sha2.h:93

***

### my\_sha384\_result

```cpp
#define my_sha384_result(context, digest, context, digest) my_sha2_service->my_sha384_result_type(context, digest)
```

Defined in service\_sha2.h:94

***

### my\_sha512

```cpp
#define my_sha512(digest, buf, len, digest, buf, len) my_sha2_service->my_sha512_type(digest, buf, len)
```

Defined in service\_sha2.h:96

***

### my\_sha512\_multi

```cpp
#define my_sha512_multi my_sha2_service->my_sha512_multi_type
```

Defined in service\_sha2.h:97

***

### my\_sha512\_context\_size

```cpp
#define my_sha512_context_size() my_sha2_service->my_sha512_context_size_type()
```

Defined in service\_sha2.h:98

***

### my\_sha512\_init

```cpp
#define my_sha512_init(context, context) my_sha2_service->my_sha512_init_type(context)
```

Defined in service\_sha2.h:99

***

### my\_sha512\_input

```cpp
#define my_sha512_input(context, buf, len, context, buf, len) my_sha2_service->my_sha512_input_type(context, buf, len)
```

Defined in service\_sha2.h:100

***

### my\_sha512\_result

```cpp
#define my_sha512_result(context, digest, context, digest) my_sha2_service->my_sha512_result_type(context, digest)
```

Defined in service\_sha2.h:101

## Variables

| Return                                                                          | Name                                                            | Description |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------- |
| struct [`my_sha2_service_st`](plugin_api_service_sha2.md#my_sha2_service_st) \* | [`my_sha2_service`](plugin_api_service_sha2.md#my_sha2_service) |             |

***

### my\_sha2\_service

```cpp
struct my_sha2_service_st * my_sha2_service
```

Type: struct [`my_sha2_service_st`](plugin_api_service_sha2.md#my_sha2_service_st) \*

Defined in service\_sha2.h:71

## Class Definitions

### my\_sha2\_service\_st

```cpp
#include <service_sha2.h>
```

```cpp
struct my_sha2_service_st
```

Defined in service\_sha2.h:43

#### Public Attributes

| Return     | Name                                                                                    | Description |
| ---------- | --------------------------------------------------------------------------------------- | ----------- |
| `void(*`   | [`my_sha224_type`](plugin_api_service_sha2.md#my_sha224_type)                           |             |
| `void(*`   | [`my_sha224_multi_type`](plugin_api_service_sha2.md#my_sha224_multi_type)               |             |
| `size_t(*` | [`my_sha224_context_size_type`](plugin_api_service_sha2.md#my_sha224_context_size_type) |             |
| `void(*`   | [`my_sha224_init_type`](plugin_api_service_sha2.md#my_sha224_init_type)                 |             |
| `void(*`   | [`my_sha224_input_type`](plugin_api_service_sha2.md#my_sha224_input_type)               |             |
| `void(*`   | [`my_sha224_result_type`](plugin_api_service_sha2.md#my_sha224_result_type)             |             |
| `void(*`   | [`my_sha256_type`](plugin_api_service_sha2.md#my_sha256_type)                           |             |
| `void(*`   | [`my_sha256_multi_type`](plugin_api_service_sha2.md#my_sha256_multi_type)               |             |
| `size_t(*` | [`my_sha256_context_size_type`](plugin_api_service_sha2.md#my_sha256_context_size_type) |             |
| `void(*`   | [`my_sha256_init_type`](plugin_api_service_sha2.md#my_sha256_init_type)                 |             |
| `void(*`   | [`my_sha256_input_type`](plugin_api_service_sha2.md#my_sha256_input_type)               |             |
| `void(*`   | [`my_sha256_result_type`](plugin_api_service_sha2.md#my_sha256_result_type)             |             |
| `void(*`   | [`my_sha384_type`](plugin_api_service_sha2.md#my_sha384_type)                           |             |
| `void(*`   | [`my_sha384_multi_type`](plugin_api_service_sha2.md#my_sha384_multi_type)               |             |
| `size_t(*` | [`my_sha384_context_size_type`](plugin_api_service_sha2.md#my_sha384_context_size_type) |             |
| `void(*`   | [`my_sha384_init_type`](plugin_api_service_sha2.md#my_sha384_init_type)                 |             |
| `void(*`   | [`my_sha384_input_type`](plugin_api_service_sha2.md#my_sha384_input_type)               |             |
| `void(*`   | [`my_sha384_result_type`](plugin_api_service_sha2.md#my_sha384_result_type)             |             |
| `void(*`   | [`my_sha512_type`](plugin_api_service_sha2.md#my_sha512_type)                           |             |
| `void(*`   | [`my_sha512_multi_type`](plugin_api_service_sha2.md#my_sha512_multi_type)               |             |
| `size_t(*` | [`my_sha512_context_size_type`](plugin_api_service_sha2.md#my_sha512_context_size_type) |             |
| `void(*`   | [`my_sha512_init_type`](plugin_api_service_sha2.md#my_sha512_init_type)                 |             |
| `void(*`   | [`my_sha512_input_type`](plugin_api_service_sha2.md#my_sha512_input_type)               |             |
| `void(*`   | [`my_sha512_result_type`](plugin_api_service_sha2.md#my_sha512_result_type)             |             |

***

#### my\_sha224\_type

```cpp
void(* my_sha224_type)(unsigned char *, const char *, size_t)
```

Defined in service\_sha2.h:44

***

#### my\_sha224\_multi\_type

```cpp
void(* my_sha224_multi_type)(unsigned char *,...)
```

Defined in service\_sha2.h:45

***

#### my\_sha224\_context\_size\_type

```cpp
size_t(* my_sha224_context_size_type)()
```

Defined in service\_sha2.h:46

***

#### my\_sha224\_init\_type

```cpp
void(* my_sha224_init_type)(void *)
```

Defined in service\_sha2.h:47

***

#### my\_sha224\_input\_type

```cpp
void(* my_sha224_input_type)(void *, const unsigned char *, size_t)
```

Defined in service\_sha2.h:48

***

#### my\_sha224\_result\_type

```cpp
void(* my_sha224_result_type)(void *, unsigned char *)
```

Defined in service\_sha2.h:49

***

#### my\_sha256\_type

```cpp
void(* my_sha256_type)(unsigned char *, const char *, size_t)
```

Defined in service\_sha2.h:51

***

#### my\_sha256\_multi\_type

```cpp
void(* my_sha256_multi_type)(unsigned char *,...)
```

Defined in service\_sha2.h:52

***

#### my\_sha256\_context\_size\_type

```cpp
size_t(* my_sha256_context_size_type)()
```

Defined in service\_sha2.h:53

***

#### my\_sha256\_init\_type

```cpp
void(* my_sha256_init_type)(void *)
```

Defined in service\_sha2.h:54

***

#### my\_sha256\_input\_type

```cpp
void(* my_sha256_input_type)(void *, const unsigned char *, size_t)
```

Defined in service\_sha2.h:55

***

#### my\_sha256\_result\_type

```cpp
void(* my_sha256_result_type)(void *, unsigned char *)
```

Defined in service\_sha2.h:56

***

#### my\_sha384\_type

```cpp
void(* my_sha384_type)(unsigned char *, const char *, size_t)
```

Defined in service\_sha2.h:58

***

#### my\_sha384\_multi\_type

```cpp
void(* my_sha384_multi_type)(unsigned char *,...)
```

Defined in service\_sha2.h:59

***

#### my\_sha384\_context\_size\_type

```cpp
size_t(* my_sha384_context_size_type)()
```

Defined in service\_sha2.h:60

***

#### my\_sha384\_init\_type

```cpp
void(* my_sha384_init_type)(void *)
```

Defined in service\_sha2.h:61

***

#### my\_sha384\_input\_type

```cpp
void(* my_sha384_input_type)(void *, const unsigned char *, size_t)
```

Defined in service\_sha2.h:62

***

#### my\_sha384\_result\_type

```cpp
void(* my_sha384_result_type)(void *, unsigned char *)
```

Defined in service\_sha2.h:63

***

#### my\_sha512\_type

```cpp
void(* my_sha512_type)(unsigned char *, const char *, size_t)
```

Defined in service\_sha2.h:65

***

#### my\_sha512\_multi\_type

```cpp
void(* my_sha512_multi_type)(unsigned char *,...)
```

Defined in service\_sha2.h:66

***

#### my\_sha512\_context\_size\_type

```cpp
size_t(* my_sha512_context_size_type)()
```

Defined in service\_sha2.h:67

***

#### my\_sha512\_init\_type

```cpp
void(* my_sha512_init_type)(void *)
```

Defined in service\_sha2.h:68

***

#### my\_sha512\_input\_type

```cpp
void(* my_sha512_input_type)(void *, const unsigned char *, size_t)
```

Defined in service\_sha2.h:69

***

#### my\_sha512\_result\_type

```cpp
void(* my_sha512_result_type)(void *, unsigned char *)
```

Defined in service\_sha2.h:70
