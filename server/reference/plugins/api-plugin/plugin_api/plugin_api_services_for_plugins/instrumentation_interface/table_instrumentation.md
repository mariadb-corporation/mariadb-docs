---
description: >-
  Macros that instrument table handles, table shares, and table lock waits for
  the Performance Schema, including open, close, unbind, and rebind.
---

# Table Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Macros

| Name                                                                                    | Description                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`PSI_TABLE_CALL`](table_instrumentation.md#psi_table_call)                             |                                                                                                                                                                                                         |
| [`MYSQL_UNBIND_TABLE`](table_instrumentation.md#mysql_unbind_table)                     |                                                                                                                                                                                                         |
| [`PSI_CALL_unbind_table`](table_instrumentation.md#psi_call_unbind_table)               |                                                                                                                                                                                                         |
| [`PSI_CALL_rebind_table`](table_instrumentation.md#psi_call_rebind_table)               |                                                                                                                                                                                                         |
| [`PSI_CALL_close_table`](table_instrumentation.md#psi_call_close_table)                 |                                                                                                                                                                                                         |
| [`PSI_CALL_open_table`](table_instrumentation.md#psi_call_open_table)                   |                                                                                                                                                                                                         |
| [`PSI_CALL_get_table_share`](table_instrumentation.md#psi_call_get_table_share)         |                                                                                                                                                                                                         |
| [`PSI_CALL_release_table_share`](table_instrumentation.md#psi_call_release_table_share) |                                                                                                                                                                                                         |
| [`PSI_CALL_drop_table_share`](table_instrumentation.md#psi_call_drop_table_share)       |                                                                                                                                                                                                         |
| [`MYSQL_TABLE_WAIT_VARIABLES`](table_instrumentation.md#mysql_table_wait_variables)     | Instrumentation helper for table waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: MYSQL\_START\_TABLE\_IO\_WAIT.                                   |
| [`MYSQL_START_TABLE_LOCK_WAIT`](table_instrumentation.md#mysql_start_table_lock_wait)   | Instrumentation helper for table lock waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL\_END\_TABLE\_LOCK\_WAIT](table_instrumentation.md#mysql_end_table_lock_wait).   |
| [`MYSQL_END_TABLE_LOCK_WAIT`](table_instrumentation.md#mysql_end_table_lock_wait)       | Instrumentation helper for table lock waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL\_START\_TABLE\_LOCK\_WAIT](table_instrumentation.md#mysql_start_table_lock_wait). |
| [`MYSQL_UNLOCK_TABLE`](table_instrumentation.md#mysql_unlock_table)                     |                                                                                                                                                                                                         |

***

### PSI\_TABLE\_CALL

```cpp
#define PSI_TABLE_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_table.h:39

***

### MYSQL\_UNBIND\_TABLE

```cpp
#define MYSQL_UNBIND_TABLE(handler, handler) do { } while(0)
```

Defined in psi/mysql\_table.h:53

***

### PSI\_CALL\_unbind\_table

```cpp
#define PSI_CALL_unbind_table(A1, A1) do { } while(0)
```

Defined in psi/mysql\_table.h:55

***

### PSI\_CALL\_rebind\_table

```cpp
#define PSI_CALL_rebind_table(A1, A2, A3, A1, A2, A3) NULL
```

Defined in psi/mysql\_table.h:56

***

### PSI\_CALL\_close\_table

```cpp
#define PSI_CALL_close_table(A1, A2, A1, A2) do { } while(0)
```

Defined in psi/mysql\_table.h:57

***

### PSI\_CALL\_open\_table

```cpp
#define PSI_CALL_open_table(A1, A2, A1, A2) NULL
```

Defined in psi/mysql\_table.h:58

***

### PSI\_CALL\_get\_table\_share

```cpp
#define PSI_CALL_get_table_share(A1, A2, A1, A2) NULL
```

Defined in psi/mysql\_table.h:59

***

### PSI\_CALL\_release\_table\_share

```cpp
#define PSI_CALL_release_table_share(A1, A1) do { } while(0)
```

Defined in psi/mysql\_table.h:60

***

### PSI\_CALL\_drop\_table\_share

```cpp
#define PSI_CALL_drop_table_share(A1, A2, A3, A4, A5, A1, A2, A3, A4, A5) do { } while(0)
```

Defined in psi/mysql\_table.h:61

***

### MYSQL\_TABLE\_WAIT\_VARIABLES

```cpp
#define MYSQL_TABLE_WAIT_VARIABLES(LOCKER, STATE, LOCKER, STATE)
```

Defined in psi/mysql\_table.h:81

Instrumentation helper for table waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: MYSQL\_START\_TABLE\_IO\_WAIT.

**See also**: MYSQL\_END\_TABLE\_IO\_WAIT.

**See also**: [MYSQL\_START\_TABLE\_LOCK\_WAIT](table_instrumentation.md#mysql_start_table_lock_wait).

**See also**: [MYSQL\_END\_TABLE\_LOCK\_WAIT](table_instrumentation.md#mysql_end_table_lock_wait).

#### Parameters

| Parameter | Type | Description      |
| --------- | ---- | ---------------- |
| `LOCKER`  |      | the locker       |
| `STATE`   |      | the locker state |
| `LOCKER`  |      | the locker       |
| `STATE`   |      | the locker state |

***

### MYSQL\_START\_TABLE\_LOCK\_WAIT

```cpp
#define MYSQL_START_TABLE_LOCK_WAIT(LOCKER, STATE, PSI, OP, FLAGS, LOCKER, STATE, PSI, OP, FLAGS) do {} while (0)
```

Defined in psi/mysql\_table.h:100

Instrumentation helper for table lock waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL\_END\_TABLE\_LOCK\_WAIT](table_instrumentation.md#mysql_end_table_lock_wait).

#### Parameters

| Parameter | Type | Description                         |
| --------- | ---- | ----------------------------------- |
| `LOCKER`  |      | the locker                          |
| `STATE`   |      | the locker state                    |
| `PSI`     |      | the instrumented table              |
| `OP`      |      | the table operation to be performed |
| `FLAGS`   |      | per table operation flags.          |
| `LOCKER`  |      | the locker                          |
| `STATE`   |      | the locker state                    |
| `PSI`     |      | the instrumented table              |
| `OP`      |      | the table operation to be performed |
| `FLAGS`   |      | per table operation flags.          |

***

### MYSQL\_END\_TABLE\_LOCK\_WAIT

```cpp
#define MYSQL_END_TABLE_LOCK_WAIT(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql\_table.h:115

Instrumentation helper for table lock waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL\_START\_TABLE\_LOCK\_WAIT](table_instrumentation.md#mysql_start_table_lock_wait).

#### Parameters

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `LOCKER`  |      | the locker  |
| `LOCKER`  |      | the locker  |

***

### MYSQL\_UNLOCK\_TABLE

```cpp
#define MYSQL_UNLOCK_TABLE(T, T) do {} while (0)
```

Defined in psi/mysql\_table.h:123
