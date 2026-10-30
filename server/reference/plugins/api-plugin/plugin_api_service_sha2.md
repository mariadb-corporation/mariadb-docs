---
description: >-
  Plugin API reference: SHA2 Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# SHA2 Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

my sha2 service

Functions to calculate SHA2 hash from a memory buffer

## Classes

| Name | Description |
|------|-------------|
| [`my_sha2_service_st`](#my_sha2_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`my_sha224`](#my_sha224)  |  |
| [`my_sha224_multi`](#my_sha224_multi)  |  |
| [`my_sha224_context_size`](#my_sha224_context_size)  |  |
| [`my_sha224_init`](#my_sha224_init)  |  |
| [`my_sha224_input`](#my_sha224_input)  |  |
| [`my_sha224_result`](#my_sha224_result)  |  |
| [`my_sha256`](#my_sha256)  |  |
| [`my_sha256_multi`](#my_sha256_multi)  |  |
| [`my_sha256_context_size`](#my_sha256_context_size)  |  |
| [`my_sha256_init`](#my_sha256_init)  |  |
| [`my_sha256_input`](#my_sha256_input)  |  |
| [`my_sha256_result`](#my_sha256_result)  |  |
| [`my_sha384`](#my_sha384)  |  |
| [`my_sha384_multi`](#my_sha384_multi)  |  |
| [`my_sha384_context_size`](#my_sha384_context_size)  |  |
| [`my_sha384_init`](#my_sha384_init)  |  |
| [`my_sha384_input`](#my_sha384_input)  |  |
| [`my_sha384_result`](#my_sha384_result)  |  |
| [`my_sha512`](#my_sha512)  |  |
| [`my_sha512_multi`](#my_sha512_multi)  |  |
| [`my_sha512_context_size`](#my_sha512_context_size)  |  |
| [`my_sha512_init`](#my_sha512_init)  |  |
| [`my_sha512_input`](#my_sha512_input)  |  |
| [`my_sha512_result`](#my_sha512_result)  |  |

---

### my_sha224

```cpp
#define my_sha224(digest, buf, len, digest, buf, len) my_sha2_service->my_sha224_type(digest, buf, len)
```

Defined in service_sha2.h:75

---

### my_sha224_multi

```cpp
#define my_sha224_multi my_sha2_service->my_sha224_multi_type
```

Defined in service_sha2.h:76

---

### my_sha224_context_size

```cpp
#define my_sha224_context_size() my_sha2_service->my_sha224_context_size_type()
```

Defined in service_sha2.h:77

---

### my_sha224_init

```cpp
#define my_sha224_init(context, context) my_sha2_service->my_sha224_init_type(context)
```

Defined in service_sha2.h:78

---

### my_sha224_input

```cpp
#define my_sha224_input(context, buf, len, context, buf, len) my_sha2_service->my_sha224_input_type(context, buf, len)
```

Defined in service_sha2.h:79

---

### my_sha224_result

```cpp
#define my_sha224_result(context, digest, context, digest) my_sha2_service->my_sha224_result_type(context, digest)
```

Defined in service_sha2.h:80

---

### my_sha256

```cpp
#define my_sha256(digest, buf, len, digest, buf, len) my_sha2_service->my_sha256_type(digest, buf, len)
```

Defined in service_sha2.h:82

---

### my_sha256_multi

```cpp
#define my_sha256_multi my_sha2_service->my_sha256_multi_type
```

Defined in service_sha2.h:83

---

### my_sha256_context_size

```cpp
#define my_sha256_context_size() my_sha2_service->my_sha256_context_size_type()
```

Defined in service_sha2.h:84

---

### my_sha256_init

```cpp
#define my_sha256_init(context, context) my_sha2_service->my_sha256_init_type(context)
```

Defined in service_sha2.h:85

---

### my_sha256_input

```cpp
#define my_sha256_input(context, buf, len, context, buf, len) my_sha2_service->my_sha256_input_type(context, buf, len)
```

Defined in service_sha2.h:86

---

### my_sha256_result

```cpp
#define my_sha256_result(context, digest, context, digest) my_sha2_service->my_sha256_result_type(context, digest)
```

Defined in service_sha2.h:87

---

### my_sha384

```cpp
#define my_sha384(digest, buf, len, digest, buf, len) my_sha2_service->my_sha384_type(digest, buf, len)
```

Defined in service_sha2.h:89

---

### my_sha384_multi

```cpp
#define my_sha384_multi my_sha2_service->my_sha384_multi_type
```

Defined in service_sha2.h:90

---

### my_sha384_context_size

```cpp
#define my_sha384_context_size() my_sha2_service->my_sha384_context_size_type()
```

Defined in service_sha2.h:91

---

### my_sha384_init

```cpp
#define my_sha384_init(context, context) my_sha2_service->my_sha384_init_type(context)
```

Defined in service_sha2.h:92

---

### my_sha384_input

```cpp
#define my_sha384_input(context, buf, len, context, buf, len) my_sha2_service->my_sha384_input_type(context, buf, len)
```

Defined in service_sha2.h:93

---

### my_sha384_result

```cpp
#define my_sha384_result(context, digest, context, digest) my_sha2_service->my_sha384_result_type(context, digest)
```

Defined in service_sha2.h:94

---

### my_sha512

```cpp
#define my_sha512(digest, buf, len, digest, buf, len) my_sha2_service->my_sha512_type(digest, buf, len)
```

Defined in service_sha2.h:96

---

### my_sha512_multi

```cpp
#define my_sha512_multi my_sha2_service->my_sha512_multi_type
```

Defined in service_sha2.h:97

---

### my_sha512_context_size

```cpp
#define my_sha512_context_size() my_sha2_service->my_sha512_context_size_type()
```

Defined in service_sha2.h:98

---

### my_sha512_init

```cpp
#define my_sha512_init(context, context) my_sha2_service->my_sha512_init_type(context)
```

Defined in service_sha2.h:99

---

### my_sha512_input

```cpp
#define my_sha512_input(context, buf, len, context, buf, len) my_sha2_service->my_sha512_input_type(context, buf, len)
```

Defined in service_sha2.h:100

---

### my_sha512_result

```cpp
#define my_sha512_result(context, digest, context, digest) my_sha2_service->my_sha512_result_type(context, digest)
```

Defined in service_sha2.h:101

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`my_sha2_service_st`](#my_sha2_service_st) * | [`my_sha2_service`](#my_sha2_service)  |  |

---

### my_sha2_service

```cpp
struct my_sha2_service_st * my_sha2_service
```

Type: struct [`my_sha2_service_st`](#my_sha2_service_st) *

Defined in service_sha2.h:71


## Class Definitions



### my_sha2_service_st

```cpp
#include <service_sha2.h>
```

```cpp
struct my_sha2_service_st
```

Defined in service_sha2.h:43

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`my_sha224_type`](#my_sha224_type)  |  |
| `void(*` | [`my_sha224_multi_type`](#my_sha224_multi_type)  |  |
| `size_t(*` | [`my_sha224_context_size_type`](#my_sha224_context_size_type)  |  |
| `void(*` | [`my_sha224_init_type`](#my_sha224_init_type)  |  |
| `void(*` | [`my_sha224_input_type`](#my_sha224_input_type)  |  |
| `void(*` | [`my_sha224_result_type`](#my_sha224_result_type)  |  |
| `void(*` | [`my_sha256_type`](#my_sha256_type)  |  |
| `void(*` | [`my_sha256_multi_type`](#my_sha256_multi_type)  |  |
| `size_t(*` | [`my_sha256_context_size_type`](#my_sha256_context_size_type)  |  |
| `void(*` | [`my_sha256_init_type`](#my_sha256_init_type)  |  |
| `void(*` | [`my_sha256_input_type`](#my_sha256_input_type)  |  |
| `void(*` | [`my_sha256_result_type`](#my_sha256_result_type)  |  |
| `void(*` | [`my_sha384_type`](#my_sha384_type)  |  |
| `void(*` | [`my_sha384_multi_type`](#my_sha384_multi_type)  |  |
| `size_t(*` | [`my_sha384_context_size_type`](#my_sha384_context_size_type)  |  |
| `void(*` | [`my_sha384_init_type`](#my_sha384_init_type)  |  |
| `void(*` | [`my_sha384_input_type`](#my_sha384_input_type)  |  |
| `void(*` | [`my_sha384_result_type`](#my_sha384_result_type)  |  |
| `void(*` | [`my_sha512_type`](#my_sha512_type)  |  |
| `void(*` | [`my_sha512_multi_type`](#my_sha512_multi_type)  |  |
| `size_t(*` | [`my_sha512_context_size_type`](#my_sha512_context_size_type)  |  |
| `void(*` | [`my_sha512_init_type`](#my_sha512_init_type)  |  |
| `void(*` | [`my_sha512_input_type`](#my_sha512_input_type)  |  |
| `void(*` | [`my_sha512_result_type`](#my_sha512_result_type)  |  |

---

#### my_sha224_type

```cpp
void(* my_sha224_type)(unsigned char *, const char *, size_t)
```

Defined in service_sha2.h:44

---

#### my_sha224_multi_type

```cpp
void(* my_sha224_multi_type)(unsigned char *,...)
```

Defined in service_sha2.h:45

---

#### my_sha224_context_size_type

```cpp
size_t(* my_sha224_context_size_type)()
```

Defined in service_sha2.h:46

---

#### my_sha224_init_type

```cpp
void(* my_sha224_init_type)(void *)
```

Defined in service_sha2.h:47

---

#### my_sha224_input_type

```cpp
void(* my_sha224_input_type)(void *, const unsigned char *, size_t)
```

Defined in service_sha2.h:48

---

#### my_sha224_result_type

```cpp
void(* my_sha224_result_type)(void *, unsigned char *)
```

Defined in service_sha2.h:49

---

#### my_sha256_type

```cpp
void(* my_sha256_type)(unsigned char *, const char *, size_t)
```

Defined in service_sha2.h:51

---

#### my_sha256_multi_type

```cpp
void(* my_sha256_multi_type)(unsigned char *,...)
```

Defined in service_sha2.h:52

---

#### my_sha256_context_size_type

```cpp
size_t(* my_sha256_context_size_type)()
```

Defined in service_sha2.h:53

---

#### my_sha256_init_type

```cpp
void(* my_sha256_init_type)(void *)
```

Defined in service_sha2.h:54

---

#### my_sha256_input_type

```cpp
void(* my_sha256_input_type)(void *, const unsigned char *, size_t)
```

Defined in service_sha2.h:55

---

#### my_sha256_result_type

```cpp
void(* my_sha256_result_type)(void *, unsigned char *)
```

Defined in service_sha2.h:56

---

#### my_sha384_type

```cpp
void(* my_sha384_type)(unsigned char *, const char *, size_t)
```

Defined in service_sha2.h:58

---

#### my_sha384_multi_type

```cpp
void(* my_sha384_multi_type)(unsigned char *,...)
```

Defined in service_sha2.h:59

---

#### my_sha384_context_size_type

```cpp
size_t(* my_sha384_context_size_type)()
```

Defined in service_sha2.h:60

---

#### my_sha384_init_type

```cpp
void(* my_sha384_init_type)(void *)
```

Defined in service_sha2.h:61

---

#### my_sha384_input_type

```cpp
void(* my_sha384_input_type)(void *, const unsigned char *, size_t)
```

Defined in service_sha2.h:62

---

#### my_sha384_result_type

```cpp
void(* my_sha384_result_type)(void *, unsigned char *)
```

Defined in service_sha2.h:63

---

#### my_sha512_type

```cpp
void(* my_sha512_type)(unsigned char *, const char *, size_t)
```

Defined in service_sha2.h:65

---

#### my_sha512_multi_type

```cpp
void(* my_sha512_multi_type)(unsigned char *,...)
```

Defined in service_sha2.h:66

---

#### my_sha512_context_size_type

```cpp
size_t(* my_sha512_context_size_type)()
```

Defined in service_sha2.h:67

---

#### my_sha512_init_type

```cpp
void(* my_sha512_init_type)(void *)
```

Defined in service_sha2.h:68

---

#### my_sha512_input_type

```cpp
void(* my_sha512_input_type)(void *, const unsigned char *, size_t)
```

Defined in service_sha2.h:69

---

#### my_sha512_result_type

```cpp
void(* my_sha512_result_type)(void *, unsigned char *)
```

Defined in service_sha2.h:70

