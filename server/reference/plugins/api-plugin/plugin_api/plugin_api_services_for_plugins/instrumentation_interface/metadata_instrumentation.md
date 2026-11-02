---
description: >-
  The mysql_mdl_create, mysql_mdl_set_status, and mysql_mdl_destroy macros,
  which instrument metadata locks for the Performance Schema.
---

# Metadata Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

Instrumentation helpers for metadata locks.

## Macros

| Name                                                                                                 | Description                             |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [`PSI_CALL_start_metadata_wait`](metadata_instrumentation.md#psi_call_start_metadata_wait)           |                                         |
| [`PSI_CALL_end_metadata_wait`](metadata_instrumentation.md#psi_call_end_metadata_wait)               |                                         |
| [`PSI_CALL_create_metadata_lock`](metadata_instrumentation.md#psi_call_create_metadata_lock)         |                                         |
| [`PSI_CALL_set_metadata_lock_status`](metadata_instrumentation.md#psi_call_set_metadata_lock_status) |                                         |
| [`PSI_CALL_destroy_metadata_lock`](metadata_instrumentation.md#psi_call_destroy_metadata_lock)       |                                         |
| [`mysql_mdl_create`](metadata_instrumentation.md#mysql_mdl_create)                                   | Instrumented metadata lock creation.    |
| [`mysql_mdl_set_status`](metadata_instrumentation.md#mysql_mdl_set_status)                           |                                         |
| [`mysql_mdl_destroy`](metadata_instrumentation.md#mysql_mdl_destroy)                                 | Instrumented metadata lock destruction. |

***

### PSI\_CALL\_start\_metadata\_wait

```cpp
#define PSI_CALL_start_metadata_wait(A, B, C, D, A, B, C, D) 0
```

Defined in psi/mysql\_mdl.h:52

***

### PSI\_CALL\_end\_metadata\_wait

```cpp
#define PSI_CALL_end_metadata_wait(A, B, A, B) do { } while(0)
```

Defined in psi/mysql\_mdl.h:53

***

### PSI\_CALL\_create\_metadata\_lock

```cpp
#define PSI_CALL_create_metadata_lock(A, B, C, D, E, F, G, A, B, C, D, E, F, G) 0
```

Defined in psi/mysql\_mdl.h:54

***

### PSI\_CALL\_set\_metadata\_lock\_status

```cpp
#define PSI_CALL_set_metadata_lock_status(A, B, A, B) do {} while(0)
```

Defined in psi/mysql\_mdl.h:55

***

### PSI\_CALL\_destroy\_metadata\_lock

```cpp
#define PSI_CALL_destroy_metadata_lock(A, A) do {} while(0)
```

Defined in psi/mysql\_mdl.h:56

***

### mysql\_mdl\_create

```cpp
#define mysql_mdl_create(I, K, T, D, S, F, L, I, K, T, D, S, F, L) NULL
```

Defined in psi/mysql\_mdl.h:75

Instrumented metadata lock creation.

#### Parameters

| Parameter | Type | Description            |
| --------- | ---- | ---------------------- |
| `I`       |      | Metadata lock identity |
| `K`       |      | Metadata key           |
| `T`       |      | Metadata lock type     |
| `D`       |      | Metadata lock duration |
| `S`       |      | Metadata lock status   |
| `F`       |      | request source file    |
| `L`       |      | request source line    |
| `I`       |      | Metadata lock identity |
| `K`       |      | Metadata key           |
| `T`       |      | Metadata lock type     |
| `D`       |      | Metadata lock duration |
| `S`       |      | Metadata lock status   |
| `F`       |      | request source file    |
| `L`       |      | request source line    |

***

### mysql\_mdl\_set\_status

```cpp
#define mysql_mdl_set_status(L, S, L, S) do {} while (0)
```

Defined in psi/mysql\_mdl.h:82

***

### mysql\_mdl\_destroy

```cpp
#define mysql_mdl_destroy(M, M) do {} while (0)
```

Defined in psi/mysql\_mdl.h:96

Instrumented metadata lock destruction.

#### Parameters

| Parameter | Type | Description   |
| --------- | ---- | ------------- |
| `M`       |      | Metadata lock |
| `M`       |      | Metadata lock |
