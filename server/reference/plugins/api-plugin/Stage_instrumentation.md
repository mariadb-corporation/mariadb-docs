---
description: >-
  Plugin API reference: Stage Instrumentation. Generated from the MariaDB server headers by doxygen and moxygen.
---

{#stageinstrumentation}

# Stage Instrumentation

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Macros

| Name | Description |
|------|-------------|
| [`mysql_stage_register`](#mysql_stage_register)  | Stage registration. |
| [`MYSQL_SET_STAGE`](#mysql_set_stage)  | Set the current stage. Use this API when the file and line is passed from the caller. |
| [`mysql_set_stage`](#mysql_set_stage-1)  | Set the current stage. |
| [`mysql_end_stage`](#mysql_end_stage)  | End the last stage |
| [`mysql_stage_set_work_completed`](#mysql_stage_set_work_completed)  |  |
| [`mysql_stage_get_work_completed`](#mysql_stage_get_work_completed)  |  |
| [`mysql_stage_inc_work_completed`](#mysql_stage_inc_work_completed)  |  |
| [`mysql_stage_set_work_estimated`](#mysql_stage_set_work_estimated)  |  |
| [`mysql_stage_get_work_estimated`](#mysql_stage_get_work_estimated)  |  |

---

{#mysql_stage_register}

### mysql_stage_register

```cpp
#define mysql_stage_register(P1, P2, P3, P1, P2, P3) do {} while (0)
```

Defined in psi/mysql_stage.h:51

Stage registration.

---

{#mysql_set_stage}

### MYSQL_SET_STAGE

```cpp
#define MYSQL_SET_STAGE(K, F, L, K, F, L) NULL
```

Defined in psi/mysql_stage.h:69

Set the current stage. Use this API when the file and line is passed from the caller. 
#### Returns
the current stage progress

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | the stage key |
| `F` |  | the source file name |
| `L` |  | the source file line |
| `K` |  | the stage key |
| `F` |  | the source file name |
| `L` |  | the source file line |

---

{#mysql_set_stage-1}

### mysql_set_stage

```cpp
#define mysql_set_stage(K, K) NULL
```

Defined in psi/mysql_stage.h:83

Set the current stage. 
#### Returns
the current stage progress

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | the stage key |
| `K` |  | the stage key |

---

{#mysql_end_stage}

### mysql_end_stage

```cpp
#define mysql_end_stage() do {} while (0)
```

Defined in psi/mysql_stage.h:95

End the last stage

---

{#mysql_stage_set_work_completed}

### mysql_stage_set_work_completed

```cpp
#define mysql_stage_set_work_completed(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql_stage.h:131

---

{#mysql_stage_get_work_completed}

### mysql_stage_get_work_completed

```cpp
#define mysql_stage_get_work_completed(P1, P1) do {} while (0)
```

Defined in psi/mysql_stage.h:134

---

{#mysql_stage_inc_work_completed}

### mysql_stage_inc_work_completed

```cpp
#define mysql_stage_inc_work_completed(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql_stage.h:142

---

{#mysql_stage_set_work_estimated}

### mysql_stage_set_work_estimated

```cpp
#define mysql_stage_set_work_estimated(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql_stage.h:153

---

{#mysql_stage_get_work_estimated}

### mysql_stage_get_work_estimated

```cpp
#define mysql_stage_get_work_estimated(P1, P1) do {} while (0)
```

Defined in psi/mysql_stage.h:156

