---
description: >-
  Plugin API reference: SHA1 Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# SHA1 Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

my sha1 service

Functions to calculate SHA1 hash from a memory buffer

## Classes

| Name | Description |
|------|-------------|
| [`my_sha1_service_st`](#my_sha1_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`MY_SHA1_HASH_SIZE`](#my_sha1_hash_size)  |  |
| [`my_sha1`](#my_sha1)  |  |
| [`my_sha1_multi`](#my_sha1_multi)  |  |
| [`my_sha1_context_size`](#my_sha1_context_size)  |  |
| [`my_sha1_init`](#my_sha1_init)  |  |
| [`my_sha1_input`](#my_sha1_input)  |  |
| [`my_sha1_result`](#my_sha1_result)  |  |

---

### MY_SHA1_HASH_SIZE

```cpp
#define MY_SHA1_HASH_SIZE 20 /* Hash size in bytes */
```

Defined in service_sha1.h:41

---

### my_sha1

```cpp
#define my_sha1(digest, buf, len, digest, buf, len) my_sha1_service->my_sha1_type(digest, buf, len)
```

Defined in service_sha1.h:54

---

### my_sha1_multi

```cpp
#define my_sha1_multi my_sha1_service->my_sha1_multi_type
```

Defined in service_sha1.h:55

---

### my_sha1_context_size

```cpp
#define my_sha1_context_size() my_sha1_service->my_sha1_context_size_type()
```

Defined in service_sha1.h:56

---

### my_sha1_init

```cpp
#define my_sha1_init(context, context) my_sha1_service->my_sha1_init_type(context)
```

Defined in service_sha1.h:57

---

### my_sha1_input

```cpp
#define my_sha1_input(context, buf, len, context, buf, len) my_sha1_service->my_sha1_input_type(context, buf, len)
```

Defined in service_sha1.h:58

---

### my_sha1_result

```cpp
#define my_sha1_result(context, digest, context, digest) my_sha1_service->my_sha1_result_type(context, digest)
```

Defined in service_sha1.h:59

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`my_sha1_service_st`](#my_sha1_service_st) * | [`my_sha1_service`](#my_sha1_service)  |  |

---

### my_sha1_service

```cpp
struct my_sha1_service_st * my_sha1_service
```

Type: struct [`my_sha1_service_st`](#my_sha1_service_st) *

Defined in service_sha1.h:50


## Class Definitions



### my_sha1_service_st

```cpp
#include <service_sha1.h>
```

```cpp
struct my_sha1_service_st
```

Defined in service_sha1.h:43

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`my_sha1_type`](#my_sha1_type)  |  |
| `void(*` | [`my_sha1_multi_type`](#my_sha1_multi_type)  |  |
| `size_t(*` | [`my_sha1_context_size_type`](#my_sha1_context_size_type)  |  |
| `void(*` | [`my_sha1_init_type`](#my_sha1_init_type)  |  |
| `void(*` | [`my_sha1_input_type`](#my_sha1_input_type)  |  |
| `void(*` | [`my_sha1_result_type`](#my_sha1_result_type)  |  |

---

#### my_sha1_type

```cpp
void(* my_sha1_type)(unsigned char *, const char *, size_t)
```

Defined in service_sha1.h:44

---

#### my_sha1_multi_type

```cpp
void(* my_sha1_multi_type)(unsigned char *,...)
```

Defined in service_sha1.h:45

---

#### my_sha1_context_size_type

```cpp
size_t(* my_sha1_context_size_type)()
```

Defined in service_sha1.h:46

---

#### my_sha1_init_type

```cpp
void(* my_sha1_init_type)(void *)
```

Defined in service_sha1.h:47

---

#### my_sha1_input_type

```cpp
void(* my_sha1_input_type)(void *, const unsigned char *, size_t)
```

Defined in service_sha1.h:48

---

#### my_sha1_result_type

```cpp
void(* my_sha1_result_type)(void *, unsigned char *)
```

Defined in service_sha1.h:49

