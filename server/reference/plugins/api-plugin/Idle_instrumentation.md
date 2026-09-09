{#idleinstrumentation}

# Idle Instrumentation

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_START_IDLE_WAIT`](#mysql_start_idle_wait)  | Instrumentation helper for table io_waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_IDLE_WAIT](api.md#mysql_end_idle_wait). |
| [`MYSQL_END_IDLE_WAIT`](#mysql_end_idle_wait)  | Instrumentation helper for idle waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_IDLE_WAIT](api.md#mysql_start_idle_wait). |

---

{#mysql_start_idle_wait}

### MYSQL_START_IDLE_WAIT

```cpp
#define MYSQL_START_IDLE_WAIT(LOCKER, STATE, LOCKER, STATE) do {} while (0)
```

Defined in psi/mysql_idle.h:56

Instrumentation helper for table io_waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_IDLE_WAIT](api.md#mysql_end_idle_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |

---

{#mysql_end_idle_wait}

### MYSQL_END_IDLE_WAIT

```cpp
#define MYSQL_END_IDLE_WAIT(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql_idle.h:71

Instrumentation helper for idle waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_IDLE_WAIT](api.md#mysql_start_idle_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `LOCKER` |  | the locker |

