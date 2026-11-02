---
description: >-
  Plugin API reference: THD Alloc Service. Generated from the MariaDB server
  headers by doxygen and moxygen.
---

# THD Alloc Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

This service provides functions to allocate memory in a connection local memory pool

The memory allocated there will be automatically freed at the end of the statement, don't use it for allocations that should live longer than that. For short living allocations this is more efficient than using my\_malloc and friends, and automatic "garbage collection" allows not to think about memory leaks.

The pool is best for small to medium objects, don't use it for large allocations - they are better served with my\_malloc.

## Classes

| Name                                                                                     | Description |
| ---------------------------------------------------------------------------------------- | ----------- |
| [`st_mysql_const_lex_string`](plugin_api_service_thd_alloc.md#st_mysql_const_lex_string) |             |
| [`st_mysql_lex_string`](plugin_api_service_thd_alloc.md#st_mysql_lex_string)             |             |
| [`thd_alloc_service_st`](plugin_api_service_thd_alloc.md#thd_alloc_service_st)           |             |

## Macros

| Name                                                                         | Description                                                             |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [`thd_alloc`](plugin_api_service_thd_alloc.md#thd_alloc)                     | Allocate memory in the connection's local memory pool                   |
| [`thd_calloc`](plugin_api_service_thd_alloc.md#thd_calloc)                   | **See also**: [thd\_alloc()](plugin_api_service_thd_alloc.md#thd_alloc) |
| [`thd_strdup`](plugin_api_service_thd_alloc.md#thd_strdup)                   | **See also**: [thd\_alloc()](plugin_api_service_thd_alloc.md#thd_alloc) |
| [`thd_strmake`](plugin_api_service_thd_alloc.md#thd_strmake)                 | **See also**: [thd\_alloc()](plugin_api_service_thd_alloc.md#thd_alloc) |
| [`thd_memdup`](plugin_api_service_thd_alloc.md#thd_memdup)                   | **See also**: [thd\_alloc()](plugin_api_service_thd_alloc.md#thd_alloc) |
| [`thd_make_lex_string`](plugin_api_service_thd_alloc.md#thd_make_lex_string) | Create a LEX\_STRING in this connection's local memory pool             |

***

### thd\_alloc

```cpp
#define thd_alloc(thd, size, thd, size) (thd_alloc_service->thd_alloc_func((thd), (size)))
```

Defined in service\_thd\_alloc.h:95

Allocate memory in the connection's local memory pool

When properly used in place of `my_malloc()`, this can significantly improve concurrency. Don't use this or related functions to allocate large chunks of memory. Use for temporary storage only. The memory will be freed automatically at the end of the statement; no explicit code is required to prevent memory leaks.

***

### thd\_calloc

```cpp
#define thd_calloc(thd, size, thd, size) (thd_alloc_service->thd_calloc_func((thd), (size)))
```

Defined in service\_thd\_alloc.h:99

**See also**: [thd\_alloc()](plugin_api_service_thd_alloc.md#thd_alloc)

***

### thd\_strdup

```cpp
#define thd_strdup(thd, str, thd, str) (thd_alloc_service->thd_strdup_func((thd), (str)))
```

Defined in service\_thd\_alloc.h:103

**See also**: [thd\_alloc()](plugin_api_service_thd_alloc.md#thd_alloc)

***

### thd\_strmake

```cpp
#define thd_strmake(thd, str, size, thd, str, size) (thd_alloc_service->thd_strmake_func((thd), (str), (size)))
```

Defined in service\_thd\_alloc.h:107

**See also**: [thd\_alloc()](plugin_api_service_thd_alloc.md#thd_alloc)

***

### thd\_memdup

```cpp
#define thd_memdup(thd, str, size, thd, str, size) (thd_alloc_service->thd_memdup_func((thd), (str), (size)))
```

Defined in service\_thd\_alloc.h:112

**See also**: [thd\_alloc()](plugin_api_service_thd_alloc.md#thd_alloc)

***

### thd\_make\_lex\_string

```cpp
#define thd_make_lex_string(thd, lex_str, str, size, allocate_lex_string, thd, lex_str, str, size, allocate_lex_string) (thd_alloc_service->thd_make_lex_string_func((thd), (lex_str), (str), \
                                               (size), (allocate_lex_string)))
```

Defined in service\_thd\_alloc.h:127

Create a LEX\_STRING in this connection's local memory pool

#### Returns

NULL on failure, or pointer to the LEX\_STRING object

**See also**: [thd\_alloc()](plugin_api_service_thd_alloc.md#thd_alloc)

#### Parameters

| Parameter             | Type | Description                                                                     |
| --------------------- | ---- | ------------------------------------------------------------------------------- |
| `thd`                 |      | user thread connection handle                                                   |
| `lex_str`             |      | pointer to LEX\_STRING object to be initialized                                 |
| `str`                 |      | initializer to be copied into lex\_str                                          |
| `size`                |      | length of str, in bytes                                                         |
| `allocate_lex_string` |      | flag: if TRUE, allocate new LEX\_STRING object, instead of using lex\_str value |
| `thd`                 |      | user thread connection handle                                                   |
| `lex_str`             |      | pointer to LEX\_STRING object to be initialized                                 |
| `str`                 |      | initializer to be copied into lex\_str                                          |
| `size`                |      | length of str, in bytes                                                         |
| `allocate_lex_string` |      | flag: if TRUE, allocate new LEX\_STRING object, instead of using lex\_str value |

## Typedefs

| Return                                                                                          | Name                                                                               | Description |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------- |
| struct [`st_mysql_const_lex_string`](plugin_api_service_thd_alloc.md#st_mysql_const_lex_string) | [`MYSQL_CONST_LEX_STRING`](plugin_api_service_thd_alloc.md#mysql_const_lex_string) |             |
| struct [`st_mysql_lex_string`](plugin_api_service_thd_alloc.md#st_mysql_lex_string)             | [`MYSQL_LEX_STRING`](plugin_api_service_thd_alloc.md#mysql_lex_string)             |             |

***

### MYSQL\_CONST\_LEX\_STRING

```cpp
using MYSQL_CONST_LEX_STRING = struct st_mysql_const_lex_string
```

Type: struct [`st_mysql_const_lex_string`](plugin_api_service_thd_alloc.md#st_mysql_const_lex_string)

Defined in service\_thd\_alloc.h:56

***

### MYSQL\_LEX\_STRING

```cpp
using MYSQL_LEX_STRING = struct st_mysql_lex_string
```

Type: struct [`st_mysql_lex_string`](plugin_api_service_thd_alloc.md#st_mysql_lex_string)

Defined in service\_thd\_alloc.h:70

## Variables

| Return                                                                                   | Name                                                                     | Description |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------- |
| struct [`thd_alloc_service_st`](plugin_api_service_thd_alloc.md#thd_alloc_service_st) \* | [`thd_alloc_service`](plugin_api_service_thd_alloc.md#thd_alloc_service) |             |

***

### thd\_alloc\_service

```cpp
struct thd_alloc_service_st * thd_alloc_service
```

Type: struct [`thd_alloc_service_st`](plugin_api_service_thd_alloc.md#thd_alloc_service_st) \*

Defined in service\_thd\_alloc.h:81

## Class Definitions

### st\_mysql\_const\_lex\_string

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct st_mysql_const_lex_string
```

Defined in service\_thd\_alloc.h:51

#### Public Attributes

| Return         | Name                                               | Description |
| -------------- | -------------------------------------------------- | ----------- |
| `const char *` | [`str`](plugin_api_service_thd_alloc.md#str)       |             |
| `size_t`       | [`length`](plugin_api_service_thd_alloc.md#length) |             |

***

#### str

```cpp
const char * str
```

Defined in service\_thd\_alloc.h:53

***

#### length

```cpp
size_t length
```

Defined in service\_thd\_alloc.h:54

### st\_mysql\_lex\_string

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct st_mysql_lex_string
```

Defined in service\_thd\_alloc.h:58

#### Public Attributes

| Return   | Name                                                 | Description |
| -------- | ---------------------------------------------------- | ----------- |
| `char *` | [`str`](plugin_api_service_thd_alloc.md#str-1)       |             |
| `size_t` | [`length`](plugin_api_service_thd_alloc.md#length-1) |             |

***

#### str

```cpp
char * str
```

Defined in service\_thd\_alloc.h:60

***

#### length

```cpp
size_t length
```

Defined in service\_thd\_alloc.h:61

#### Public Methods

| Return | Name                                                                                                                                      | Description |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
|        | [`operator struct st_mysql_const_lex_string`](plugin_api_service_thd_alloc.md#operator-struct-st_mysql_const_lex_string) `const` `inline` |             |

***

#### operator struct st\_mysql\_const\_lex\_string

`const` `inline`

```cpp
inline operator struct st_mysql_const_lex_string() const
```

Defined in service\_thd\_alloc.h:64

### thd\_alloc\_service\_st

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct thd_alloc_service_st
```

Defined in service\_thd\_alloc.h:72

#### Public Attributes

| Return                                                                                 | Name                                                                                   | Description |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------- |
| `void *(*`                                                                             | [`thd_alloc_func`](plugin_api_service_thd_alloc.md#thd_alloc_func)                     |             |
| `void *(*`                                                                             | [`thd_calloc_func`](plugin_api_service_thd_alloc.md#thd_calloc_func)                   |             |
| `char *(*`                                                                             | [`thd_strdup_func`](plugin_api_service_thd_alloc.md#thd_strdup_func)                   |             |
| `char *(*`                                                                             | [`thd_strmake_func`](plugin_api_service_thd_alloc.md#thd_strmake_func)                 |             |
| `void *(*`                                                                             | [`thd_memdup_func`](plugin_api_service_thd_alloc.md#thd_memdup_func)                   |             |
| [`MYSQL_CONST_LEX_STRING`](plugin_api_service_thd_alloc.md#mysql_const_lex_string) _(_ | [`thd_make_lex_string_func`](plugin_api_service_thd_alloc.md#thd_make_lex_string_func) |             |

***

#### thd\_alloc\_func

```cpp
void *(* thd_alloc_func)(const MYSQL_THD, size_t)
```

Defined in service\_thd\_alloc.h:73

***

#### thd\_calloc\_func

```cpp
void *(* thd_calloc_func)(const MYSQL_THD, size_t)
```

Defined in service\_thd\_alloc.h:74

***

#### thd\_strdup\_func

```cpp
char *(* thd_strdup_func)(const MYSQL_THD, const char *)
```

Defined in service\_thd\_alloc.h:75

***

#### thd\_strmake\_func

```cpp
char *(* thd_strmake_func)(const MYSQL_THD, const char *, size_t)
```

Defined in service\_thd\_alloc.h:76

***

#### thd\_memdup\_func

```cpp
void *(* thd_memdup_func)(const MYSQL_THD, const void *, size_t)
```

Defined in service\_thd\_alloc.h:77

***

#### thd\_make\_lex\_string\_func

```cpp
MYSQL_CONST_LEX_STRING *(* thd_make_lex_string_func)(const MYSQL_THD, MYSQL_CONST_LEX_STRING *, const char *, size_t, int)
```

Defined in service\_thd\_alloc.h:78
