{#transactioninstrumentation}

# Transaction Instrumentation

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_START_TRANSACTION`](#mysql_start_transaction)  |  |
| [`MYSQL_SET_TRANSACTION_GTID`](#mysql_set_transaction_gtid)  |  |
| [`MYSQL_SET_TRANSACTION_XID`](#mysql_set_transaction_xid)  |  |
| [`MYSQL_SET_TRANSACTION_XA_STATE`](#mysql_set_transaction_xa_state)  |  |
| [`MYSQL_SET_TRANSACTION_TRXID`](#mysql_set_transaction_trxid)  |  |
| [`MYSQL_INC_TRANSACTION_SAVEPOINTS`](#mysql_inc_transaction_savepoints)  |  |
| [`MYSQL_INC_TRANSACTION_ROLLBACK_TO_SAVEPOINT`](#mysql_inc_transaction_rollback_to_savepoint)  |  |
| [`MYSQL_INC_TRANSACTION_RELEASE_SAVEPOINT`](#mysql_inc_transaction_release_savepoint)  |  |
| [`MYSQL_ROLLBACK_TRANSACTION`](#mysql_rollback_transaction)  |  |
| [`MYSQL_COMMIT_TRANSACTION`](#mysql_commit_transaction)  |  |

---

{#mysql_start_transaction}

### MYSQL_START_TRANSACTION

```cpp
#define MYSQL_START_TRANSACTION(STATE, XID, TRXID, ISO, RO, AC, STATE, XID, TRXID, ISO, RO, AC) 0
```

Defined in psi/mysql_transaction.h:47

---

{#mysql_set_transaction_gtid}

### MYSQL_SET_TRANSACTION_GTID

```cpp
#define MYSQL_SET_TRANSACTION_GTID(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql_transaction.h:55

---

{#mysql_set_transaction_xid}

### MYSQL_SET_TRANSACTION_XID

```cpp
#define MYSQL_SET_TRANSACTION_XID(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql_transaction.h:63

---

{#mysql_set_transaction_xa_state}

### MYSQL_SET_TRANSACTION_XA_STATE

```cpp
#define MYSQL_SET_TRANSACTION_XA_STATE(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:71

---

{#mysql_set_transaction_trxid}

### MYSQL_SET_TRANSACTION_TRXID

```cpp
#define MYSQL_SET_TRANSACTION_TRXID(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:79

---

{#mysql_inc_transaction_savepoints}

### MYSQL_INC_TRANSACTION_SAVEPOINTS

```cpp
#define MYSQL_INC_TRANSACTION_SAVEPOINTS(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:87

---

{#mysql_inc_transaction_rollback_to_savepoint}

### MYSQL_INC_TRANSACTION_ROLLBACK_TO_SAVEPOINT

```cpp
#define MYSQL_INC_TRANSACTION_ROLLBACK_TO_SAVEPOINT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:95

---

{#mysql_inc_transaction_release_savepoint}

### MYSQL_INC_TRANSACTION_RELEASE_SAVEPOINT

```cpp
#define MYSQL_INC_TRANSACTION_RELEASE_SAVEPOINT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_transaction.h:103

---

{#mysql_rollback_transaction}

### MYSQL_ROLLBACK_TRANSACTION

```cpp
#define MYSQL_ROLLBACK_TRANSACTION(LOCKER, LOCKER) do { } while(0)
```

Defined in psi/mysql_transaction.h:111

---

{#mysql_commit_transaction}

### MYSQL_COMMIT_TRANSACTION

```cpp
#define MYSQL_COMMIT_TRANSACTION(LOCKER, LOCKER) do { } while(0)
```

Defined in psi/mysql_transaction.h:119

