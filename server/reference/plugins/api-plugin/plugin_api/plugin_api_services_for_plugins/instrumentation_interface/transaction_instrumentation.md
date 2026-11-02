---
description: >-
  Macros that report a transaction's start, GTID, XID, XA state, savepoints,
  commit, and rollback to the Performance Schema.
---

# Transaction Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Macros

| Name                                                                                                                        | Description |
| --------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [`PSI_TRANSACTION_CALL`](transaction_instrumentation.md#psi_transaction_call)                                               |             |
| [`MYSQL_START_TRANSACTION`](transaction_instrumentation.md#mysql_start_transaction)                                         |             |
| [`MYSQL_SET_TRANSACTION_GTID`](transaction_instrumentation.md#mysql_set_transaction_gtid)                                   |             |
| [`MYSQL_SET_TRANSACTION_XID`](transaction_instrumentation.md#mysql_set_transaction_xid)                                     |             |
| [`MYSQL_SET_TRANSACTION_XA_STATE`](transaction_instrumentation.md#mysql_set_transaction_xa_state)                           |             |
| [`MYSQL_SET_TRANSACTION_TRXID`](transaction_instrumentation.md#mysql_set_transaction_trxid)                                 |             |
| [`MYSQL_INC_TRANSACTION_SAVEPOINTS`](transaction_instrumentation.md#mysql_inc_transaction_savepoints)                       |             |
| [`MYSQL_INC_TRANSACTION_ROLLBACK_TO_SAVEPOINT`](transaction_instrumentation.md#mysql_inc_transaction_rollback_to_savepoint) |             |
| [`MYSQL_INC_TRANSACTION_RELEASE_SAVEPOINT`](transaction_instrumentation.md#mysql_inc_transaction_release_savepoint)         |             |
| [`MYSQL_ROLLBACK_TRANSACTION`](transaction_instrumentation.md#mysql_rollback_transaction)                                   |             |
| [`MYSQL_COMMIT_TRANSACTION`](transaction_instrumentation.md#mysql_commit_transaction)                                       |             |

***

### PSI\_TRANSACTION\_CALL

```cpp
#define PSI_TRANSACTION_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_transaction.h:40

***

### MYSQL\_START\_TRANSACTION

```cpp
#define MYSQL_START_TRANSACTION(STATE, XID, TRXID, ISO, RO, AC, STATE, XID, TRXID, ISO, RO, AC) 0
```

Defined in psi/mysql\_transaction.h:47

***

### MYSQL\_SET\_TRANSACTION\_GTID

```cpp
#define MYSQL_SET_TRANSACTION_GTID(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql\_transaction.h:55

***

### MYSQL\_SET\_TRANSACTION\_XID

```cpp
#define MYSQL_SET_TRANSACTION_XID(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql\_transaction.h:63

***

### MYSQL\_SET\_TRANSACTION\_XA\_STATE

```cpp
#define MYSQL_SET_TRANSACTION_XA_STATE(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql\_transaction.h:71

***

### MYSQL\_SET\_TRANSACTION\_TRXID

```cpp
#define MYSQL_SET_TRANSACTION_TRXID(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql\_transaction.h:79

***

### MYSQL\_INC\_TRANSACTION\_SAVEPOINTS

```cpp
#define MYSQL_INC_TRANSACTION_SAVEPOINTS(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql\_transaction.h:87

***

### MYSQL\_INC\_TRANSACTION\_ROLLBACK\_TO\_SAVEPOINT

```cpp
#define MYSQL_INC_TRANSACTION_ROLLBACK_TO_SAVEPOINT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql\_transaction.h:95

***

### MYSQL\_INC\_TRANSACTION\_RELEASE\_SAVEPOINT

```cpp
#define MYSQL_INC_TRANSACTION_RELEASE_SAVEPOINT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql\_transaction.h:103

***

### MYSQL\_ROLLBACK\_TRANSACTION

```cpp
#define MYSQL_ROLLBACK_TRANSACTION(LOCKER, LOCKER) do { } while(0)
```

Defined in psi/mysql\_transaction.h:111

***

### MYSQL\_COMMIT\_TRANSACTION

```cpp
#define MYSQL_COMMIT_TRANSACTION(LOCKER, LOCKER) do { } while(0)
```

Defined in psi/mysql\_transaction.h:119
