---
description: >-
  Plugin API reference: SHA1 Service. Generated from the MariaDB server headers
  by doxygen and moxygen.
---

# SHA1 Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

my sha1 service

Functions to calculate SHA1 hash from a memory buffer

## Classes

| Name                                                                  | Description |
| --------------------------------------------------------------------- | ----------- |
| [`my_sha1_service_st`](plugin_api_service_sha1.md#my_sha1_service_st) |             |

## Macros

| Name                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [`MY_SHA1_HASH_SIZE`](plugin_api_service_sha1.md#my_sha1_hash_size)       |             |
| [`my_sha1`](plugin_api_service_sha1.md#my_sha1)                           |             |
| [`my_sha1_multi`](plugin_api_service_sha1.md#my_sha1_multi)               |             |
| [`my_sha1_context_size`](plugin_api_service_sha1.md#my_sha1_context_size) |             |
| [`my_sha1_init`](plugin_api_service_sha1.md#my_sha1_init)                 |             |
| [`my_sha1_input`](plugin_api_service_sha1.md#my_sha1_input)               |             |
| [`my_sha1_result`](plugin_api_service_sha1.md#my_sha1_result)             |             |

***

### MY\_SHA1\_HASH\_SIZE

```cpp
#define MY_SHA1_HASH_SIZE 20 /* Hash size in bytes */
```

Defined in service\_sha1.h:41

***

### my\_sha1

```cpp
#define my_sha1(digest, buf, len, digest, buf, len) my_sha1_service->my_sha1_type(digest, buf, len)
```

Defined in service\_sha1.h:54

***

### my\_sha1\_multi

```cpp
#define my_sha1_multi my_sha1_service->my_sha1_multi_type
```

Defined in service\_sha1.h:55

***

### my\_sha1\_context\_size

```cpp
#define my_sha1_context_size() my_sha1_service->my_sha1_context_size_type()
```

Defined in service\_sha1.h:56

***

### my\_sha1\_init

```cpp
#define my_sha1_init(context, context) my_sha1_service->my_sha1_init_type(context)
```

Defined in service\_sha1.h:57

***

### my\_sha1\_input

```cpp
#define my_sha1_input(context, buf, len, context, buf, len) my_sha1_service->my_sha1_input_type(context, buf, len)
```

Defined in service\_sha1.h:58

***

### my\_sha1\_result

```cpp
#define my_sha1_result(context, digest, context, digest) my_sha1_service->my_sha1_result_type(context, digest)
```

Defined in service\_sha1.h:59

## Variables

| Return                                                                          | Name                                                            | Description |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------- |
| struct [`my_sha1_service_st`](plugin_api_service_sha1.md#my_sha1_service_st) \* | [`my_sha1_service`](plugin_api_service_sha1.md#my_sha1_service) |             |

***

### my\_sha1\_service

```cpp
struct my_sha1_service_st * my_sha1_service
```

Type: struct [`my_sha1_service_st`](plugin_api_service_sha1.md#my_sha1_service_st) \*

Defined in service\_sha1.h:50

## Class Definitions

### my\_sha1\_service\_st

```cpp
#include <service_sha1.h>
```

```cpp
struct my_sha1_service_st
```

Defined in service\_sha1.h:43

#### Public Attributes

| Return     | Name                                                                                | Description |
| ---------- | ----------------------------------------------------------------------------------- | ----------- |
| `void(*`   | [`my_sha1_type`](plugin_api_service_sha1.md#my_sha1_type)                           |             |
| `void(*`   | [`my_sha1_multi_type`](plugin_api_service_sha1.md#my_sha1_multi_type)               |             |
| `size_t(*` | [`my_sha1_context_size_type`](plugin_api_service_sha1.md#my_sha1_context_size_type) |             |
| `void(*`   | [`my_sha1_init_type`](plugin_api_service_sha1.md#my_sha1_init_type)                 |             |
| `void(*`   | [`my_sha1_input_type`](plugin_api_service_sha1.md#my_sha1_input_type)               |             |
| `void(*`   | [`my_sha1_result_type`](plugin_api_service_sha1.md#my_sha1_result_type)             |             |

***

#### my\_sha1\_type

```cpp
void(* my_sha1_type)(unsigned char *, const char *, size_t)
```

Defined in service\_sha1.h:44

***

#### my\_sha1\_multi\_type

```cpp
void(* my_sha1_multi_type)(unsigned char *,...)
```

Defined in service\_sha1.h:45

***

#### my\_sha1\_context\_size\_type

```cpp
size_t(* my_sha1_context_size_type)()
```

Defined in service\_sha1.h:46

***

#### my\_sha1\_init\_type

```cpp
void(* my_sha1_init_type)(void *)
```

Defined in service\_sha1.h:47

***

#### my\_sha1\_input\_type

```cpp
void(* my_sha1_input_type)(void *, const unsigned char *, size_t)
```

Defined in service\_sha1.h:48

***

#### my\_sha1\_result\_type

```cpp
void(* my_sha1_result_type)(void *, unsigned char *)
```

Defined in service\_sha1.h:49
