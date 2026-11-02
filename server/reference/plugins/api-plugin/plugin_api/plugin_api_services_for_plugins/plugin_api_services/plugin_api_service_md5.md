---
description: >-
  Plugin API reference: MD5 Service. Generated from the MariaDB server headers
  by doxygen and moxygen.
---

# MD5 Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

Functions to calculate MD5 hash from a memory buffer

## Classes

| Name                                                               | Description |
| ------------------------------------------------------------------ | ----------- |
| [`my_md5_service_st`](plugin_api_service_md5.md#my_md5_service_st) |             |

## Macros

| Name                                                                   | Description |
| ---------------------------------------------------------------------- | ----------- |
| [`MY_MD5_HASH_SIZE`](plugin_api_service_md5.md#my_md5_hash_size)       |             |
| [`my_md5`](plugin_api_service_md5.md#my_md5)                           |             |
| [`my_md5_multi`](plugin_api_service_md5.md#my_md5_multi)               |             |
| [`my_md5_context_size`](plugin_api_service_md5.md#my_md5_context_size) |             |
| [`my_md5_init`](plugin_api_service_md5.md#my_md5_init)                 |             |
| [`my_md5_input`](plugin_api_service_md5.md#my_md5_input)               |             |
| [`my_md5_result`](plugin_api_service_md5.md#my_md5_result)             |             |

***

### MY\_MD5\_HASH\_SIZE

```cpp
#define MY_MD5_HASH_SIZE 16 /* Hash size in bytes */
```

Defined in service\_md5.h:40

***

### my\_md5

```cpp
#define my_md5(A, B, C, A, B, C) my_md5_service->my_md5_type(A,B,C)
```

Defined in service\_md5.h:53

***

### my\_md5\_multi

```cpp
#define my_md5_multi my_md5_service->my_md5_multi_type
```

Defined in service\_md5.h:54

***

### my\_md5\_context\_size

```cpp
#define my_md5_context_size() my_md5_service->my_md5_context_size_type()
```

Defined in service\_md5.h:55

***

### my\_md5\_init

```cpp
#define my_md5_init(A, A) my_md5_service->my_md5_init_type(A)
```

Defined in service\_md5.h:56

***

### my\_md5\_input

```cpp
#define my_md5_input(A, B, C, A, B, C) my_md5_service->my_md5_input_type(A,B,C)
```

Defined in service\_md5.h:57

***

### my\_md5\_result

```cpp
#define my_md5_result(A, B, A, B) my_md5_service->my_md5_result_type(A,B)
```

Defined in service\_md5.h:58

## Variables

| Return                                                                       | Name                                                         | Description |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------- |
| struct [`my_md5_service_st`](plugin_api_service_md5.md#my_md5_service_st) \* | [`my_md5_service`](plugin_api_service_md5.md#my_md5_service) |             |

***

### my\_md5\_service

```cpp
struct my_md5_service_st * my_md5_service
```

Type: struct [`my_md5_service_st`](plugin_api_service_md5.md#my_md5_service_st) \*

Defined in service\_md5.h:49

## Class Definitions

### my\_md5\_service\_st

```cpp
#include <service_md5.h>
```

```cpp
struct my_md5_service_st
```

Defined in service\_md5.h:42

#### Public Attributes

| Return     | Name                                                                             | Description |
| ---------- | -------------------------------------------------------------------------------- | ----------- |
| `void(*`   | [`my_md5_type`](plugin_api_service_md5.md#my_md5_type)                           |             |
| `void(*`   | [`my_md5_multi_type`](plugin_api_service_md5.md#my_md5_multi_type)               |             |
| `size_t(*` | [`my_md5_context_size_type`](plugin_api_service_md5.md#my_md5_context_size_type) |             |
| `void(*`   | [`my_md5_init_type`](plugin_api_service_md5.md#my_md5_init_type)                 |             |
| `void(*`   | [`my_md5_input_type`](plugin_api_service_md5.md#my_md5_input_type)               |             |
| `void(*`   | [`my_md5_result_type`](plugin_api_service_md5.md#my_md5_result_type)             |             |

***

#### my\_md5\_type

```cpp
void(* my_md5_type)(unsigned char *, const char *, size_t)
```

Defined in service\_md5.h:43

***

#### my\_md5\_multi\_type

```cpp
void(* my_md5_multi_type)(unsigned char *,...)
```

Defined in service\_md5.h:44

***

#### my\_md5\_context\_size\_type

```cpp
size_t(* my_md5_context_size_type)()
```

Defined in service\_md5.h:45

***

#### my\_md5\_init\_type

```cpp
void(* my_md5_init_type)(void *)
```

Defined in service\_md5.h:46

***

#### my\_md5\_input\_type

```cpp
void(* my_md5_input_type)(void *, const unsigned char *, size_t)
```

Defined in service\_md5.h:47

***

#### my\_md5\_result\_type

```cpp
void(* my_md5_result_type)(void *, unsigned char *)
```

Defined in service\_md5.h:48
