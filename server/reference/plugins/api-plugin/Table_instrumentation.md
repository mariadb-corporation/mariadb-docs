{#tableinstrumentation}

# Table Instrumentation

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_UNBIND_TABLE`](#mysql_unbind_table)  |  |
| [`PSI_CALL_unbind_table`](#psi_call_unbind_table)  |  |
| [`PSI_CALL_rebind_table`](#psi_call_rebind_table)  |  |
| [`PSI_CALL_close_table`](#psi_call_close_table)  |  |
| [`PSI_CALL_open_table`](#psi_call_open_table)  |  |
| [`PSI_CALL_get_table_share`](#psi_call_get_table_share)  |  |
| [`PSI_CALL_release_table_share`](#psi_call_release_table_share)  |  |
| [`PSI_CALL_drop_table_share`](#psi_call_drop_table_share)  |  |
| [`MYSQL_TABLE_WAIT_VARIABLES`](#mysql_table_wait_variables)  | Instrumentation helper for table waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: MYSQL_START_TABLE_IO_WAIT. |
| [`MYSQL_START_TABLE_LOCK_WAIT`](#mysql_start_table_lock_wait)  | Instrumentation helper for table lock waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_TABLE_LOCK_WAIT](api.md#mysql_end_table_lock_wait). |
| [`MYSQL_END_TABLE_LOCK_WAIT`](#mysql_end_table_lock_wait)  | Instrumentation helper for table lock waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_TABLE_LOCK_WAIT](api.md#mysql_start_table_lock_wait). |
| [`MYSQL_UNLOCK_TABLE`](#mysql_unlock_table)  |  |

---

{#mysql_unbind_table}

### MYSQL_UNBIND_TABLE

```cpp
#define MYSQL_UNBIND_TABLE(handler, handler) do { } while(0)
```

Defined in psi/mysql_table.h:55

---

{#psi_call_unbind_table}

### PSI_CALL_unbind_table

```cpp
#define PSI_CALL_unbind_table(A1, A1) do { } while(0)
```

Defined in psi/mysql_table.h:57

---

{#psi_call_rebind_table}

### PSI_CALL_rebind_table

```cpp
#define PSI_CALL_rebind_table(A1, A2, A3, A1, A2, A3) NULL
```

Defined in psi/mysql_table.h:58

---

{#psi_call_close_table}

### PSI_CALL_close_table

```cpp
#define PSI_CALL_close_table(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql_table.h:59

---

{#psi_call_open_table}

### PSI_CALL_open_table

```cpp
#define PSI_CALL_open_table(A1, A2, A1, A2) NULL
```

Defined in psi/mysql_table.h:60

---

{#psi_call_get_table_share}

### PSI_CALL_get_table_share

```cpp
#define PSI_CALL_get_table_share(A1, A2, A1, A2) NULL
```

Defined in psi/mysql_table.h:61

---

{#psi_call_release_table_share}

### PSI_CALL_release_table_share

```cpp
#define PSI_CALL_release_table_share(A1, A1) do { } while(0)
```

Defined in psi/mysql_table.h:62

---

{#psi_call_drop_table_share}

### PSI_CALL_drop_table_share

```cpp
#define PSI_CALL_drop_table_share(A1, A2, A3, A4, A5, A1, A2, A3, A4, A5) do { } while(0)
```

Defined in psi/mysql_table.h:63

---

{#mysql_table_wait_variables}

### MYSQL_TABLE_WAIT_VARIABLES

```cpp
#define MYSQL_TABLE_WAIT_VARIABLES(LOCKER, STATE, LOCKER, STATE)
```

Defined in psi/mysql_table.h:83

Instrumentation helper for table waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: MYSQL_START_TABLE_IO_WAIT. 

**See also**: MYSQL_END_TABLE_IO_WAIT. 

**See also**: [MYSQL_START_TABLE_LOCK_WAIT](api.md#mysql_start_table_lock_wait). 

**See also**: [MYSQL_END_TABLE_LOCK_WAIT](api.md#mysql_end_table_lock_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |

---

{#mysql_start_table_lock_wait}

### MYSQL_START_TABLE_LOCK_WAIT

```cpp
#define MYSQL_START_TABLE_LOCK_WAIT(LOCKER, STATE, PSI, OP, FLAGS, LOCKER, STATE, PSI, OP, FLAGS) do {} while (0)
```

Defined in psi/mysql_table.h:102

Instrumentation helper for table lock waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_TABLE_LOCK_WAIT](api.md#mysql_end_table_lock_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `PSI` |  | the instrumented table |
| `OP` |  | the table operation to be performed |
| `FLAGS` |  | per table operation flags. |
| `LOCKER` |  | the locker |
| `STATE` |  | the locker state |
| `PSI` |  | the instrumented table |
| `OP` |  | the table operation to be performed |
| `FLAGS` |  | per table operation flags. |

---

{#mysql_end_table_lock_wait}

### MYSQL_END_TABLE_LOCK_WAIT

```cpp
#define MYSQL_END_TABLE_LOCK_WAIT(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql_table.h:117

Instrumentation helper for table lock waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_TABLE_LOCK_WAIT](api.md#mysql_start_table_lock_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | the locker |
| `LOCKER` |  | the locker |

---

{#mysql_unlock_table}

### MYSQL_UNLOCK_TABLE

```cpp
#define MYSQL_UNLOCK_TABLE(T, T) do {} while (0)
```

Defined in psi/mysql_table.h:125

