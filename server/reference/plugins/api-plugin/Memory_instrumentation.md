---
description: >-
  The mysql_memory_register macro, which registers memory instruments with the Performance Schema.
---



# Memory Instrumentation

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Instrumentation Interface`](Instrumentation_interface.md)

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_MEMORY_H`](#mysql_memory_h)  |  |
| [`PSI_CALL_memory_alloc`](#psi_call_memory_alloc)  |  |
| [`PSI_CALL_memory_free`](#psi_call_memory_free)  |  |
| [`PSI_CALL_memory_realloc`](#psi_call_memory_realloc)  |  |
| [`PSI_CALL_register_memory`](#psi_call_register_memory)  |  |
| [`PSI_MEMORY_CALL`](#psi_memory_call)  |  |
| [`mysql_memory_register`](#mysql_memory_register)  | Memory registration. |

---

### MYSQL_MEMORY_H

```cpp
#define MYSQL_MEMORY_H
```

Defined in psi/mysql_memory.h:34

---

### PSI_CALL_memory_alloc

```cpp
#define PSI_CALL_memory_alloc(A1, A2, A3, A1, A2, A3) 0
```

Defined in psi/mysql_memory.h:44

---

### PSI_CALL_memory_free

```cpp
#define PSI_CALL_memory_free(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql_memory.h:45

---

### PSI_CALL_memory_realloc

```cpp
#define PSI_CALL_memory_realloc(A1, A2, A3, A4, A1, A2, A3, A4) 0
```

Defined in psi/mysql_memory.h:46

---

### PSI_CALL_register_memory

```cpp
#define PSI_CALL_register_memory(A1, A2, A3, A1, A2, A3) do { } while(0)
```

Defined in psi/mysql_memory.h:47

---

### PSI_MEMORY_CALL

```cpp
#define PSI_MEMORY_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_memory.h:51

---

### mysql_memory_register

```cpp
#define mysql_memory_register(P1, P2, P3, P1, P2, P3) inline_mysql_memory_register(P1, P2, P3)
```

Defined in psi/mysql_memory.h:58

Memory registration.

## Functions

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`inline_mysql_memory_register`](#inline_mysql_memory_register) `static` `inline` |  |

---

### inline_mysql_memory_register

`static` `inline`

```cpp
static inline void inline_mysql_memory_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_memory.h:61

