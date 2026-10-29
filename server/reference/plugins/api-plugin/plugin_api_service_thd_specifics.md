---
description: >-
  Plugin API reference: THD Specifics Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# THD Specifics Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

THD specific for plugin(s)

This API provides pthread_getspecific() like functionality to plugin authors. This is a functional alternative to the declarative MYSQL_THDVAR_* API.

A plugin should at init call [thd_key_create()](api.md#thd_key_create) that create a key that will have storage in each THD. The key should be used by all threads and can be used concurrently from all threads.

A plugin should at deinit call [thd_key_delete()](api.md#thd_key_delete).

Alternatively, a plugin can use [thd_key_create_from_var(K,V)](api.md#thd_key_create_from_var) to create a key that corresponds to a named MYSQL_THDVAR_* variable.

This API is also safe when using pool-of-threads in which case pthread_getspecific() is not, because the actual OS thread may change.

> [!NOTE]
>

Normally one should prefer MYSQL_THDVAR_* declarative API.

The benefits are:

* It supports typed variables (int, char*, enum, etc), not only void*.
* The memory allocated for MYSQL_THDVAR_* is free'd automatically (if [PLUGIN_VAR_MEMALLOC](api.md#plugin_var_memalloc) is specified).
* Continuous loading and unloading of the same plugin does not allocate memory for same variables over and over again.

An example of using MYSQL_THDVAR_* for a thd local storage: 
```cpp
MYSQL_THDVAR_STR(my_tls,
        PLUGIN_VAR_MEMALLOC | PLUGIN_VAR_NOSYSVAR | PLUGIN_VAR_NOCMDOPT,
        "thd local storage example", 0, 0, 0);
```

## Classes

| Name | Description |
|------|-------------|
| [`thd_specifics_service_st`](#thd_specifics_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_key_create_from_var`](#thd_key_create_from_var)  |  |
| [`thd_key_create`](#thd_key_create)  | create THD specific storage |
| [`thd_key_delete`](#thd_key_delete)  | delete THD specific storage |
| [`thd_getspecific`](#thd_getspecific)  | get thd specific storage |
| [`thd_setspecific`](#thd_setspecific)  | set thd specific storage |

---

### thd_key_create_from_var

```cpp
#define thd_key_create_from_var(K, V, K, V) do { *(K)= MYSQL_SYSVAR_NAME(V).offset; } while(0)
```

Defined in service_thd_specifics.h:81

---

### thd_key_create

```cpp
#define thd_key_create(key, key) (thd_specifics_service->thd_key_create_func(key))
```

Defined in service_thd_specifics.h:90

create THD specific storage 
#### Returns
0 on success else errno is returned

---

### thd_key_delete

```cpp
#define thd_key_delete(key, key) (thd_specifics_service->thd_key_delete_func(key))
```

Defined in service_thd_specifics.h:94

delete THD specific storage

---

### thd_getspecific

```cpp
#define thd_getspecific(thd, key, thd, key) (thd_specifics_service->thd_getspecific_func(thd, key))
```

Defined in service_thd_specifics.h:102

get thd specific storage

* first time this is called from a thread it will return 0
* this call is thread-safe in that different threads may call this simultaneously if operating on different THDs.
* this call acquires no mutexes and is implemented as an array lookup

---

### thd_setspecific

```cpp
#define thd_setspecific(thd, key, value, thd, key, value) (thd_specifics_service->thd_setspecific_func(thd, key, value))
```

Defined in service_thd_specifics.h:110

set thd specific storage

* first time this is called from a thread it will return 0
* this call is thread-safe in that different threads may call this simultaneously if operating on different THDs.
* this call acquires no mutexes and is implemented as an array lookup

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`MYSQL_THD_KEY_T`](#mysql_thd_key_t)  |  |

---

### MYSQL_THD_KEY_T

```cpp
using MYSQL_THD_KEY_T = int
```

Defined in service_thd_specifics.h:72

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_specifics_service_st`](#thd_specifics_service_st) * | [`thd_specifics_service`](#thd_specifics_service)  |  |

---

### thd_specifics_service

```cpp
struct thd_specifics_service_st * thd_specifics_service
```

Type: struct [`thd_specifics_service_st`](#thd_specifics_service_st) *

Defined in service_thd_specifics.h:79


## Class Definitions



### thd_specifics_service_st

```cpp
#include <service_thd_specifics.h>
```

```cpp
struct thd_specifics_service_st
```

Defined in service_thd_specifics.h:74

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`thd_key_create_func`](#thd_key_create_func)  |  |
| `void(*` | [`thd_key_delete_func`](#thd_key_delete_func)  |  |
| `void *(*` | [`thd_getspecific_func`](#thd_getspecific_func)  |  |
| `int(*` | [`thd_setspecific_func`](#thd_setspecific_func)  |  |

---

#### thd_key_create_func

```cpp
int(* thd_key_create_func)(MYSQL_THD_KEY_T *key)
```

Defined in service_thd_specifics.h:75

---

#### thd_key_delete_func

```cpp
void(* thd_key_delete_func)(MYSQL_THD_KEY_T *key)
```

Defined in service_thd_specifics.h:76

---

#### thd_getspecific_func

```cpp
void *(* thd_getspecific_func)(MYSQL_THD thd, MYSQL_THD_KEY_T key)
```

Defined in service_thd_specifics.h:77

---

#### thd_setspecific_func

```cpp
int(* thd_setspecific_func)(MYSQL_THD thd, MYSQL_THD_KEY_T key, void *value)
```

Defined in service_thd_specifics.h:78

