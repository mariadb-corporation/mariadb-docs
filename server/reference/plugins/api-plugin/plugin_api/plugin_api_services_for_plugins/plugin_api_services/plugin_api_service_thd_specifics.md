---
description: >-
  Plugin API reference: THD Specifics Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# THD Specifics Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

THD specific for plugin(s)

This API provides pthread\_getspecific() like functionality to plugin authors. This is a functional alternative to the declarative MYSQL\_THDVAR\_\* API.

A plugin should at init call [thd\_key\_create()](plugin_api_service_thd_specifics.md#thd_key_create) that create a key that will have storage in each THD. The key should be used by all threads and can be used concurrently from all threads.

A plugin should at deinit call [thd\_key\_delete()](plugin_api_service_thd_specifics.md#thd_key_delete).

Alternatively, a plugin can use [thd\_key\_create\_from\_var(K,V)](plugin_api_service_thd_specifics.md#thd_key_create_from_var) to create a key that corresponds to a named MYSQL\_THDVAR\_\* variable.

This API is also safe when using pool-of-threads in which case pthread\_getspecific() is not, because the actual OS thread may change.

> \[!NOTE]

Normally one should prefer MYSQL\_THDVAR\_\* declarative API.

The benefits are:

* It supports typed variables (int, char\*, enum, etc), not only void\*.
* The memory allocated for MYSQL\_THDVAR\_\* is free'd automatically (if [PLUGIN\_VAR\_MEMALLOC](../../plugin_declaration/plugin_sys_vars/plugin_sysvar_flags.md#plugin_var_memalloc) is specified).
* Continuous loading and unloading of the same plugin does not allocate memory for same variables over and over again.

An example of using MYSQL\_THDVAR\_\* for a thd local storage:

```cpp
MYSQL_THDVAR_STR(my_tls,
        PLUGIN_VAR_MEMALLOC | PLUGIN_VAR_NOSYSVAR | PLUGIN_VAR_NOCMDOPT,
        "thd local storage example", 0, 0, 0);
```

## Classes

| Name                                                                                       | Description |
| ------------------------------------------------------------------------------------------ | ----------- |
| [`thd_specifics_service_st`](plugin_api_service_thd_specifics.md#thd_specifics_service_st) |             |

## Macros

| Name                                                                                     | Description                 |
| ---------------------------------------------------------------------------------------- | --------------------------- |
| [`thd_key_create_from_var`](plugin_api_service_thd_specifics.md#thd_key_create_from_var) |                             |
| [`thd_key_create`](plugin_api_service_thd_specifics.md#thd_key_create)                   | create THD specific storage |
| [`thd_key_delete`](plugin_api_service_thd_specifics.md#thd_key_delete)                   | delete THD specific storage |
| [`thd_getspecific`](plugin_api_service_thd_specifics.md#thd_getspecific)                 | get thd specific storage    |
| [`thd_setspecific`](plugin_api_service_thd_specifics.md#thd_setspecific)                 | set thd specific storage    |

***

### thd\_key\_create\_from\_var

```cpp
#define thd_key_create_from_var(K, V, K, V) do { *(K)= MYSQL_SYSVAR_NAME(V).offset; } while(0)
```

Defined in service\_thd\_specifics.h:81

***

### thd\_key\_create

```cpp
#define thd_key_create(key, key) (thd_specifics_service->thd_key_create_func(key))
```

Defined in service\_thd\_specifics.h:90

create THD specific storage

#### Returns

0 on success else errno is returned

***

### thd\_key\_delete

```cpp
#define thd_key_delete(key, key) (thd_specifics_service->thd_key_delete_func(key))
```

Defined in service\_thd\_specifics.h:94

delete THD specific storage

***

### thd\_getspecific

```cpp
#define thd_getspecific(thd, key, thd, key) (thd_specifics_service->thd_getspecific_func(thd, key))
```

Defined in service\_thd\_specifics.h:102

get thd specific storage

* first time this is called from a thread it will return 0
* this call is thread-safe in that different threads may call this simultaneously if operating on different THDs.
* this call acquires no mutexes and is implemented as an array lookup

***

### thd\_setspecific

```cpp
#define thd_setspecific(thd, key, value, thd, key, value) (thd_specifics_service->thd_setspecific_func(thd, key, value))
```

Defined in service\_thd\_specifics.h:110

set thd specific storage

* first time this is called from a thread it will return 0
* this call is thread-safe in that different threads may call this simultaneously if operating on different THDs.
* this call acquires no mutexes and is implemented as an array lookup

## Typedefs

| Return | Name                                                                     | Description |
| ------ | ------------------------------------------------------------------------ | ----------- |
| `int`  | [`MYSQL_THD_KEY_T`](plugin_api_service_thd_specifics.md#mysql_thd_key_t) |             |

***

### MYSQL\_THD\_KEY\_T

```cpp
using MYSQL_THD_KEY_T = int
```

Defined in service\_thd\_specifics.h:72

## Variables

| Return                                                                                               | Name                                                                                 | Description |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------- |
| struct [`thd_specifics_service_st`](plugin_api_service_thd_specifics.md#thd_specifics_service_st) \* | [`thd_specifics_service`](plugin_api_service_thd_specifics.md#thd_specifics_service) |             |

***

### thd\_specifics\_service

```cpp
struct thd_specifics_service_st * thd_specifics_service
```

Type: struct [`thd_specifics_service_st`](plugin_api_service_thd_specifics.md#thd_specifics_service_st) \*

Defined in service\_thd\_specifics.h:79

## Class Definitions

### thd\_specifics\_service\_st

```cpp
#include <service_thd_specifics.h>
```

```cpp
struct thd_specifics_service_st
```

Defined in service\_thd\_specifics.h:74

#### Public Attributes

| Return     | Name                                                                               | Description |
| ---------- | ---------------------------------------------------------------------------------- | ----------- |
| `int(*`    | [`thd_key_create_func`](plugin_api_service_thd_specifics.md#thd_key_create_func)   |             |
| `void(*`   | [`thd_key_delete_func`](plugin_api_service_thd_specifics.md#thd_key_delete_func)   |             |
| `void *(*` | [`thd_getspecific_func`](plugin_api_service_thd_specifics.md#thd_getspecific_func) |             |
| `int(*`    | [`thd_setspecific_func`](plugin_api_service_thd_specifics.md#thd_setspecific_func) |             |

***

#### thd\_key\_create\_func

```cpp
int(* thd_key_create_func)(MYSQL_THD_KEY_T *key)
```

Defined in service\_thd\_specifics.h:75

***

#### thd\_key\_delete\_func

```cpp
void(* thd_key_delete_func)(MYSQL_THD_KEY_T *key)
```

Defined in service\_thd\_specifics.h:76

***

#### thd\_getspecific\_func

```cpp
void *(* thd_getspecific_func)(MYSQL_THD thd, MYSQL_THD_KEY_T key)
```

Defined in service\_thd\_specifics.h:77

***

#### thd\_setspecific\_func

```cpp
int(* thd_setspecific_func)(MYSQL_THD thd, MYSQL_THD_KEY_T key, void *value)
```

Defined in service\_thd\_specifics.h:78
