---
description: >-
  Macros that register statement execution stages, set the current stage, and
  report stage progress (work completed and work estimated) to the Performance
  Schema.
---

# Stage Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Macros

| Name                                                                                        | Description                                                                           |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| [`PSI_STAGE_CALL`](stage_instrumentation.md#psi_stage_call)                                 |                                                                                       |
| [`mysql_stage_register`](stage_instrumentation.md#mysql_stage_register)                     | Stage registration.                                                                   |
| [`MYSQL_SET_STAGE`](stage_instrumentation.md#mysql_set_stage)                               | Set the current stage. Use this API when the file and line is passed from the caller. |
| [`mysql_set_stage`](stage_instrumentation.md#mysql_set_stage-1)                             | Set the current stage.                                                                |
| [`mysql_end_stage`](stage_instrumentation.md#mysql_end_stage)                               | End the last stage                                                                    |
| [`mysql_stage_set_work_completed`](stage_instrumentation.md#mysql_stage_set_work_completed) |                                                                                       |
| [`mysql_stage_get_work_completed`](stage_instrumentation.md#mysql_stage_get_work_completed) |                                                                                       |
| [`mysql_stage_inc_work_completed`](stage_instrumentation.md#mysql_stage_inc_work_completed) |                                                                                       |
| [`mysql_stage_set_work_estimated`](stage_instrumentation.md#mysql_stage_set_work_estimated) |                                                                                       |
| [`mysql_stage_get_work_estimated`](stage_instrumentation.md#mysql_stage_get_work_estimated) |                                                                                       |

***

### PSI\_STAGE\_CALL

```cpp
#define PSI_STAGE_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_stage.h:38

***

### mysql\_stage\_register

```cpp
#define mysql_stage_register(P1, P2, P3, P1, P2, P3) do {} while (0)
```

Defined in psi/mysql\_stage.h:49

Stage registration.

***

### MYSQL\_SET\_STAGE

```cpp
#define MYSQL_SET_STAGE(K, F, L, K, F, L) NULL
```

Defined in psi/mysql\_stage.h:67

Set the current stage. Use this API when the file and line is passed from the caller.

#### Returns

the current stage progress

#### Parameters

| Parameter | Type | Description          |
| --------- | ---- | -------------------- |
| `K`       |      | the stage key        |
| `F`       |      | the source file name |
| `L`       |      | the source file line |
| `K`       |      | the stage key        |
| `F`       |      | the source file name |
| `L`       |      | the source file line |

***

### mysql\_set\_stage

```cpp
#define mysql_set_stage(K, K) NULL
```

Defined in psi/mysql\_stage.h:81

Set the current stage.

#### Returns

the current stage progress

#### Parameters

| Parameter | Type | Description   |
| --------- | ---- | ------------- |
| `K`       |      | the stage key |
| `K`       |      | the stage key |

***

### mysql\_end\_stage

```cpp
#define mysql_end_stage() do {} while (0)
```

Defined in psi/mysql\_stage.h:93

End the last stage

***

### mysql\_stage\_set\_work\_completed

```cpp
#define mysql_stage_set_work_completed(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql\_stage.h:129

***

### mysql\_stage\_get\_work\_completed

```cpp
#define mysql_stage_get_work_completed(P1, P1) do {} while (0)
```

Defined in psi/mysql\_stage.h:132

***

### mysql\_stage\_inc\_work\_completed

```cpp
#define mysql_stage_inc_work_completed(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql\_stage.h:140

***

### mysql\_stage\_set\_work\_estimated

```cpp
#define mysql_stage_set_work_estimated(P1, P2, P1, P2) do {} while (0)
```

Defined in psi/mysql\_stage.h:151

***

### mysql\_stage\_get\_work\_estimated

```cpp
#define mysql_stage_get_work_estimated(P1, P1) do {} while (0)
```

Defined in psi/mysql\_stage.h:154
