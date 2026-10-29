---
description: >-
  The MYSQL_START_IDLE_WAIT and MYSQL_END_IDLE_WAIT macros, which mark the start and end of an idle wait event for the Performance Schema.
---



# Idle Instrumentation

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Instrumentation Interface`](Instrumentation_interface.md)

## Macros

| Name | Description |
|------|-------------|
| [`PSI_IDLE_CALL`](#psi_idle_call)  |  |
| [`MYSQL_START_IDLE_WAIT`](#mysql_start_idle_wait)  | Instrumentation helper for table io_waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_IDLE_WAIT](api.md#mysql_end_idle_wait). |
| [`MYSQL_END_IDLE_WAIT`](#mysql_end_idle_wait)  | Instrumentation helper for idle waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_IDLE_WAIT](api.md#mysql_start_idle_wait). |

---

### PSI_IDLE_CALL

```cpp
#define PSI_IDLE_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_idle.h:39

---

### MYSQL_START_IDLE_WAIT

```cpp
#define MYSQL_START_IDLE_WAIT(LOCKER, STATE, LOCKER, STATE) do {} while (0)
```

Defined in psi/mysql_idle.h:54

Instrumentation helper for table io_waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_IDLE_WAIT](api.md#mysql_end_idle_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |

---

### MYSQL_END_IDLE_WAIT

```cpp
#define MYSQL_END_IDLE_WAIT(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql_idle.h:69

Instrumentation helper for idle waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_IDLE_WAIT](api.md#mysql_start_idle_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `LOCKER` |  | the locker |

