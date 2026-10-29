---
description: >-
  Plugin API reference: THD Alloc Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# THD Alloc Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

This service provides functions to allocate memory in a connection local memory pool

The memory allocated there will be automatically freed at the end of the statement, don't use it for allocations that should live longer than that. For short living allocations this is more efficient than using my_malloc and friends, and automatic "garbage collection" allows not to think about memory leaks.

The pool is best for small to medium objects, don't use it for large allocations - they are better served with my_malloc.

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_const_lex_string`](#st_mysql_const_lex_string) |  |
| [`st_mysql_lex_string`](#st_mysql_lex_string) |  |
| [`thd_alloc_service_st`](#thd_alloc_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_alloc`](#thd_alloc)  | Allocate memory in the connection's local memory pool |
| [`thd_calloc`](#thd_calloc)  | **See also**: [thd_alloc()](#thd_alloc) |
| [`thd_strdup`](#thd_strdup)  | **See also**: [thd_alloc()](#thd_alloc) |
| [`thd_strmake`](#thd_strmake)  | **See also**: [thd_alloc()](#thd_alloc) |
| [`thd_memdup`](#thd_memdup)  | **See also**: [thd_alloc()](#thd_alloc) |
| [`thd_make_lex_string`](#thd_make_lex_string)  | Create a LEX_STRING in this connection's local memory pool |

---

### thd_alloc

```cpp
#define thd_alloc(thd, size, thd, size) (thd_alloc_service->thd_alloc_func((thd), (size)))
```

Defined in service_thd_alloc.h:95

Allocate memory in the connection's local memory pool

When properly used in place of `my_malloc()`, this can significantly improve concurrency. Don't use this or related functions to allocate large chunks of memory. Use for temporary storage only. The memory will be freed automatically at the end of the statement; no explicit code is required to prevent memory leaks.

---

### thd_calloc

```cpp
#define thd_calloc(thd, size, thd, size) (thd_alloc_service->thd_calloc_func((thd), (size)))
```

Defined in service_thd_alloc.h:99

**See also**: [thd_alloc()](#thd_alloc)

---

### thd_strdup

```cpp
#define thd_strdup(thd, str, thd, str) (thd_alloc_service->thd_strdup_func((thd), (str)))
```

Defined in service_thd_alloc.h:103

**See also**: [thd_alloc()](#thd_alloc)

---

### thd_strmake

```cpp
#define thd_strmake(thd, str, size, thd, str, size) (thd_alloc_service->thd_strmake_func((thd), (str), (size)))
```

Defined in service_thd_alloc.h:107

**See also**: [thd_alloc()](#thd_alloc)

---

### thd_memdup

```cpp
#define thd_memdup(thd, str, size, thd, str, size) (thd_alloc_service->thd_memdup_func((thd), (str), (size)))
```

Defined in service_thd_alloc.h:112

**See also**: [thd_alloc()](#thd_alloc)

---

### thd_make_lex_string

```cpp
#define thd_make_lex_string(thd, lex_str, str, size, allocate_lex_string, thd, lex_str, str, size, allocate_lex_string) (thd_alloc_service->thd_make_lex_string_func((thd), (lex_str), (str), \
                                               (size), (allocate_lex_string)))
```

Defined in service_thd_alloc.h:127

Create a LEX_STRING in this connection's local memory pool

#### Returns
NULL on failure, or pointer to the LEX_STRING object

**See also**: [thd_alloc()](#thd_alloc)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` |  | user thread connection handle |
| `lex_str` |  | pointer to LEX_STRING object to be initialized |
| `str` |  | initializer to be copied into lex_str |
| `size` |  | length of str, in bytes |
| `allocate_lex_string` |  | flag: if TRUE, allocate new LEX_STRING object, instead of using lex_str value |
| `thd` |  | user thread connection handle |
| `lex_str` |  | pointer to LEX_STRING object to be initialized |
| `str` |  | initializer to be copied into lex_str |
| `size` |  | length of str, in bytes |
| `allocate_lex_string` |  | flag: if TRUE, allocate new LEX_STRING object, instead of using lex_str value |

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| struct [`st_mysql_const_lex_string`](#st_mysql_const_lex_string) | [`MYSQL_CONST_LEX_STRING`](#mysql_const_lex_string)  |  |
| struct [`st_mysql_lex_string`](#st_mysql_lex_string) | [`MYSQL_LEX_STRING`](#mysql_lex_string)  |  |

---

### MYSQL_CONST_LEX_STRING

```cpp
using MYSQL_CONST_LEX_STRING = struct st_mysql_const_lex_string
```

Type: struct [`st_mysql_const_lex_string`](#st_mysql_const_lex_string)

Defined in service_thd_alloc.h:56

---

### MYSQL_LEX_STRING

```cpp
using MYSQL_LEX_STRING = struct st_mysql_lex_string
```

Type: struct [`st_mysql_lex_string`](#st_mysql_lex_string)

Defined in service_thd_alloc.h:70

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`thd_alloc_service_st`](#thd_alloc_service_st) * | [`thd_alloc_service`](#thd_alloc_service)  |  |

---

### thd_alloc_service

```cpp
struct thd_alloc_service_st * thd_alloc_service
```

Type: struct [`thd_alloc_service_st`](#thd_alloc_service_st) *

Defined in service_thd_alloc.h:81


## Class Definitions



### st_mysql_const_lex_string

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct st_mysql_const_lex_string
```

Defined in service_thd_alloc.h:51

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const char *` | [`str`](#str)  |  |
| `size_t` | [`length`](#length)  |  |

---

#### str

```cpp
const char * str
```

Defined in service_thd_alloc.h:53

---

#### length

```cpp
size_t length
```

Defined in service_thd_alloc.h:54



### st_mysql_lex_string

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct st_mysql_lex_string
```

Defined in service_thd_alloc.h:58

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `char *` | [`str`](#str-1)  |  |
| `size_t` | [`length`](#length-1)  |  |

---

#### str

```cpp
char * str
```

Defined in service_thd_alloc.h:60

---

#### length

```cpp
size_t length
```

Defined in service_thd_alloc.h:61

#### Public Methods

| Return | Name | Description |
|--------|------|-------------|
|  | [`operator struct st_mysql_const_lex_string`](#operator-struct-st_mysql_const_lex_string) `const` `inline` |  |

---

#### operator struct st_mysql_const_lex_string

`const` `inline`

```cpp
inline operator struct st_mysql_const_lex_string() const
```

Defined in service_thd_alloc.h:64



### thd_alloc_service_st

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct thd_alloc_service_st
```

Defined in service_thd_alloc.h:72

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void *(*` | [`thd_alloc_func`](#thd_alloc_func)  |  |
| `void *(*` | [`thd_calloc_func`](#thd_calloc_func)  |  |
| `char *(*` | [`thd_strdup_func`](#thd_strdup_func)  |  |
| `char *(*` | [`thd_strmake_func`](#thd_strmake_func)  |  |
| `void *(*` | [`thd_memdup_func`](#thd_memdup_func)  |  |
| [`MYSQL_CONST_LEX_STRING`](#mysql_const_lex_string) *(* | [`thd_make_lex_string_func`](#thd_make_lex_string_func)  |  |

---

#### thd_alloc_func

```cpp
void *(* thd_alloc_func)(const MYSQL_THD, size_t)
```

Defined in service_thd_alloc.h:73

---

#### thd_calloc_func

```cpp
void *(* thd_calloc_func)(const MYSQL_THD, size_t)
```

Defined in service_thd_alloc.h:74

---

#### thd_strdup_func

```cpp
char *(* thd_strdup_func)(const MYSQL_THD, const char *)
```

Defined in service_thd_alloc.h:75

---

#### thd_strmake_func

```cpp
char *(* thd_strmake_func)(const MYSQL_THD, const char *, size_t)
```

Defined in service_thd_alloc.h:76

---

#### thd_memdup_func

```cpp
void *(* thd_memdup_func)(const MYSQL_THD, const void *, size_t)
```

Defined in service_thd_alloc.h:77

---

#### thd_make_lex_string_func

```cpp
MYSQL_CONST_LEX_STRING *(* thd_make_lex_string_func)(const MYSQL_THD, MYSQL_CONST_LEX_STRING *, const char *, size_t, int)
```

Defined in service_thd_alloc.h:78

