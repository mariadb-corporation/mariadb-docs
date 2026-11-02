---
description: >-
  Plugin API reference: MD5 Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# MD5 Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Functions to calculate MD5 hash from a memory buffer

## Classes

| Name | Description |
|------|-------------|
| [`my_md5_service_st`](#my_md5_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`MY_MD5_HASH_SIZE`](#my_md5_hash_size)  |  |
| [`my_md5`](#my_md5)  |  |
| [`my_md5_multi`](#my_md5_multi)  |  |
| [`my_md5_context_size`](#my_md5_context_size)  |  |
| [`my_md5_init`](#my_md5_init)  |  |
| [`my_md5_input`](#my_md5_input)  |  |
| [`my_md5_result`](#my_md5_result)  |  |

---

### MY_MD5_HASH_SIZE

```cpp
#define MY_MD5_HASH_SIZE 16 /* Hash size in bytes */
```

Defined in service_md5.h:40

---

### my_md5

```cpp
#define my_md5(A, B, C, A, B, C) my_md5_service->my_md5_type(A,B,C)
```

Defined in service_md5.h:53

---

### my_md5_multi

```cpp
#define my_md5_multi my_md5_service->my_md5_multi_type
```

Defined in service_md5.h:54

---

### my_md5_context_size

```cpp
#define my_md5_context_size() my_md5_service->my_md5_context_size_type()
```

Defined in service_md5.h:55

---

### my_md5_init

```cpp
#define my_md5_init(A, A) my_md5_service->my_md5_init_type(A)
```

Defined in service_md5.h:56

---

### my_md5_input

```cpp
#define my_md5_input(A, B, C, A, B, C) my_md5_service->my_md5_input_type(A,B,C)
```

Defined in service_md5.h:57

---

### my_md5_result

```cpp
#define my_md5_result(A, B, A, B) my_md5_service->my_md5_result_type(A,B)
```

Defined in service_md5.h:58

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`my_md5_service_st`](#my_md5_service_st) * | [`my_md5_service`](#my_md5_service)  |  |

---

### my_md5_service

```cpp
struct my_md5_service_st * my_md5_service
```

Type: struct [`my_md5_service_st`](#my_md5_service_st) *

Defined in service_md5.h:49


## Class Definitions



### my_md5_service_st

```cpp
#include <service_md5.h>
```

```cpp
struct my_md5_service_st
```

Defined in service_md5.h:42

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`my_md5_type`](#my_md5_type)  |  |
| `void(*` | [`my_md5_multi_type`](#my_md5_multi_type)  |  |
| `size_t(*` | [`my_md5_context_size_type`](#my_md5_context_size_type)  |  |
| `void(*` | [`my_md5_init_type`](#my_md5_init_type)  |  |
| `void(*` | [`my_md5_input_type`](#my_md5_input_type)  |  |
| `void(*` | [`my_md5_result_type`](#my_md5_result_type)  |  |

---

#### my_md5_type

```cpp
void(* my_md5_type)(unsigned char *, const char *, size_t)
```

Defined in service_md5.h:43

---

#### my_md5_multi_type

```cpp
void(* my_md5_multi_type)(unsigned char *,...)
```

Defined in service_md5.h:44

---

#### my_md5_context_size_type

```cpp
size_t(* my_md5_context_size_type)()
```

Defined in service_md5.h:45

---

#### my_md5_init_type

```cpp
void(* my_md5_init_type)(void *)
```

Defined in service_md5.h:46

---

#### my_md5_input_type

```cpp
void(* my_md5_input_type)(void *, const unsigned char *, size_t)
```

Defined in service_md5.h:47

---

#### my_md5_result_type

```cpp
void(* my_md5_result_type)(void *, unsigned char *)
```

Defined in service_md5.h:48

