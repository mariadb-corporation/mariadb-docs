---
description: >-
  The mysql_memory_register macro, which registers memory instruments with the
  Performance Schema.
---

# Memory Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Macros

| Name                                                                             | Description          |
| -------------------------------------------------------------------------------- | -------------------- |
| [`MYSQL_MEMORY_H`](memory_instrumentation.md#mysql_memory_h)                     |                      |
| [`PSI_CALL_memory_alloc`](memory_instrumentation.md#psi_call_memory_alloc)       |                      |
| [`PSI_CALL_memory_free`](memory_instrumentation.md#psi_call_memory_free)         |                      |
| [`PSI_CALL_memory_realloc`](memory_instrumentation.md#psi_call_memory_realloc)   |                      |
| [`PSI_CALL_register_memory`](memory_instrumentation.md#psi_call_register_memory) |                      |
| [`PSI_MEMORY_CALL`](memory_instrumentation.md#psi_memory_call)                   |                      |
| [`mysql_memory_register`](memory_instrumentation.md#mysql_memory_register)       | Memory registration. |

***

### MYSQL\_MEMORY\_H

```cpp
#define MYSQL_MEMORY_H
```

Defined in psi/mysql\_memory.h:34

***

### PSI\_CALL\_memory\_alloc

```cpp
#define PSI_CALL_memory_alloc(A1, A2, A3, A1, A2, A3) 0
```

Defined in psi/mysql\_memory.h:44

***

### PSI\_CALL\_memory\_free

```cpp
#define PSI_CALL_memory_free(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql\_memory.h:45

***

### PSI\_CALL\_memory\_realloc

```cpp
#define PSI_CALL_memory_realloc(A1, A2, A3, A4, A1, A2, A3, A4) 0
```

Defined in psi/mysql\_memory.h:46

***

### PSI\_CALL\_register\_memory

```cpp
#define PSI_CALL_register_memory(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql\_memory.h:47

***

### PSI\_MEMORY\_CALL

```cpp
#define PSI_MEMORY_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_memory.h:51

***

### mysql\_memory\_register

```cpp
#define mysql_memory_register(P1, P2, P3, P1, P2, P3) inline_mysql_memory_register(P1, P2, P3)
```

Defined in psi/mysql\_memory.h:58

Memory registration.

## Functions

| Return | Name                                                                                                       | Description |
| ------ | ---------------------------------------------------------------------------------------------------------- | ----------- |
| `void` | [`inline_mysql_memory_register`](memory_instrumentation.md#inline_mysql_memory_register) `static` `inline` |             |

***

### inline\_mysql\_memory\_register

`static` `inline`

```cpp
static inline void inline_mysql_memory_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql\_memory.h:61
