---
description: >-
  The mysql_mdl_create, mysql_mdl_set_status, and mysql_mdl_destroy macros, which instrument metadata locks for the Performance Schema.
---



# Metadata Instrumentation

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Instrumentation Interface`](Instrumentation_interface.md)

Instrumentation helpers for metadata locks.

## Macros

| Name | Description |
|------|-------------|
| [`PSI_CALL_start_metadata_wait`](#psi_call_start_metadata_wait)  |  |
| [`PSI_CALL_end_metadata_wait`](#psi_call_end_metadata_wait)  |  |
| [`PSI_CALL_create_metadata_lock`](#psi_call_create_metadata_lock)  |  |
| [`PSI_CALL_set_metadata_lock_status`](#psi_call_set_metadata_lock_status)  |  |
| [`PSI_CALL_destroy_metadata_lock`](#psi_call_destroy_metadata_lock)  |  |
| [`mysql_mdl_create`](#mysql_mdl_create)  | Instrumented metadata lock creation. |
| [`mysql_mdl_set_status`](#mysql_mdl_set_status)  |  |
| [`mysql_mdl_destroy`](#mysql_mdl_destroy)  | Instrumented metadata lock destruction. |

---

### PSI_CALL_start_metadata_wait

```cpp
#define PSI_CALL_start_metadata_wait(A, B, C, D, A, B, C, D) 0
```

Defined in psi/mysql_mdl.h:52

---

### PSI_CALL_end_metadata_wait

```cpp
#define PSI_CALL_end_metadata_wait(A, B, A, B) do { } while(0)
```

Defined in psi/mysql_mdl.h:53

---

### PSI_CALL_create_metadata_lock

```cpp
#define PSI_CALL_create_metadata_lock(A, B, C, D, E, F, G, A, B, C, D, E, F, G) 0
```

Defined in psi/mysql_mdl.h:54

---

### PSI_CALL_set_metadata_lock_status

```cpp
#define PSI_CALL_set_metadata_lock_status(A, B, A, B) do {} while(0)
```

Defined in psi/mysql_mdl.h:55

---

### PSI_CALL_destroy_metadata_lock

```cpp
#define PSI_CALL_destroy_metadata_lock(A, A) do {} while(0)
```

Defined in psi/mysql_mdl.h:56

---

### mysql_mdl_create

```cpp
#define mysql_mdl_create(I, K, T, D, S, F, L, I, K, T, D, S, F, L) NULL
```

Defined in psi/mysql_mdl.h:75

Instrumented metadata lock creation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `I` |  | Metadata lock identity |
| `K` |  | Metadata key |
| `T` |  | Metadata lock type |
| `D` |  | Metadata lock duration |
| `S` |  | Metadata lock status |
| `F` |  | request source file |
| `L` |  | request source line |
| `I` |  | Metadata lock identity |
| `K` |  | Metadata key |
| `T` |  | Metadata lock type |
| `D` |  | Metadata lock duration |
| `S` |  | Metadata lock status |
| `F` |  | request source file |
| `L` |  | request source line |

---

### mysql_mdl_set_status

```cpp
#define mysql_mdl_set_status(L, S, L, S) do {} while (0)
```

Defined in psi/mysql_mdl.h:82

---

### mysql_mdl_destroy

```cpp
#define mysql_mdl_destroy(M, M) do {} while (0)
```

Defined in psi/mysql_mdl.h:96

Instrumented metadata lock destruction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `M` |  | Metadata lock |
| `M` |  | Metadata lock |

