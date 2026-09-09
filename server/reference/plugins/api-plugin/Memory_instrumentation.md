---
description: >-
  Plugin API reference: Memory Instrumentation. Generated from the MariaDB server headers by doxygen and moxygen.
---

{#memoryinstrumentation}

# Memory Instrumentation

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Macros

| Name | Description |
|------|-------------|
| [`mysql_memory_register`](#mysql_memory_register)  | Memory registration. |

---

{#mysql_memory_register}

### mysql_memory_register

```cpp
#define mysql_memory_register(P1, P2, P3, P1, P2, P3) inline_mysql_memory_register(P1, P2, P3)
```

Defined in psi/mysql_memory.h:59

Memory registration.

## Functions

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`inline_mysql_memory_register`](#inline_mysql_memory_register) `static` `inline` |  |

---

{#inline_mysql_memory_register}

### inline_mysql_memory_register

`static` `inline`

```cpp
static inline void inline_mysql_memory_register(const char *category __attribute__, void *info __attribute__, int count __attribute__, const char *category __attribute__, void *info __attribute__, int count __attribute__)
```

Defined in psi/mysql_memory.h:62

