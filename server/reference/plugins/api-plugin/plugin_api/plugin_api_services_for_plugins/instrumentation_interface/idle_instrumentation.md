---
description: >-
  The MYSQL_START_IDLE_WAIT and MYSQL_END_IDLE_WAIT macros, which mark the start
  and end of an idle wait event for the Performance Schema.
---

# Idle Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Macros

| Name                                                                     | Description                                                                                                                                                                            |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`PSI_IDLE_CALL`](idle_instrumentation.md#psi_idle_call)                 |                                                                                                                                                                                        |
| [`MYSQL_START_IDLE_WAIT`](idle_instrumentation.md#mysql_start_idle_wait) | Instrumentation helper for table io\_waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL\_END\_IDLE\_WAIT](idle_instrumentation.md#mysql_end_idle_wait). |
| [`MYSQL_END_IDLE_WAIT`](idle_instrumentation.md#mysql_end_idle_wait)     | Instrumentation helper for idle waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL\_START\_IDLE\_WAIT](idle_instrumentation.md#mysql_start_idle_wait).    |

***

### PSI\_IDLE\_CALL

```cpp
#define PSI_IDLE_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_idle.h:39

***

### MYSQL\_START\_IDLE\_WAIT

```cpp
#define MYSQL_START_IDLE_WAIT(LOCKER, STATE, LOCKER, STATE) do {} while (0)
```

Defined in psi/mysql\_idle.h:54

Instrumentation helper for table io\_waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL\_END\_IDLE\_WAIT](idle_instrumentation.md#mysql_end_idle_wait).

#### Parameters

| Parameter | Type | Description      |
| --------- | ---- | ---------------- |
| `LOCKER`  |      | the locker       |
| `STATE`   |      | the locker state |
| `LOCKER`  |      | the locker       |
| `STATE`   |      | the locker state |

***

### MYSQL\_END\_IDLE\_WAIT

```cpp
#define MYSQL_END_IDLE_WAIT(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql\_idle.h:69

Instrumentation helper for idle waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL\_START\_IDLE\_WAIT](idle_instrumentation.md#mysql_start_idle_wait).

#### Parameters

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `LOCKER`  |      | the locker  |
| `LOCKER`  |      | the locker  |
