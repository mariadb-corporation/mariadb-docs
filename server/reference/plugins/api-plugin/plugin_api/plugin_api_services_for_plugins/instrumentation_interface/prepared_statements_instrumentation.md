---
description: >-
  Plugin API reference: Prepared Statements Instrumentation. Generated from the
  MariaDB server headers by doxygen and moxygen.
---

# Prepared Statements Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

Instrumentation helpers for prepared statements.

## Macros

| Name                                                                              | Description |
| --------------------------------------------------------------------------------- | ----------- |
| [`PSI_PS_CALL`](prepared_statements_instrumentation.md#psi_ps_call)               |             |
| [`MYSQL_CREATE_PS`](prepared_statements_instrumentation.md#mysql_create_ps)       |             |
| [`MYSQL_EXECUTE_PS`](prepared_statements_instrumentation.md#mysql_execute_ps)     |             |
| [`MYSQL_DESTROY_PS`](prepared_statements_instrumentation.md#mysql_destroy_ps)     |             |
| [`MYSQL_REPREPARE_PS`](prepared_statements_instrumentation.md#mysql_reprepare_ps) |             |
| [`MYSQL_SET_PS_TEXT`](prepared_statements_instrumentation.md#mysql_set_ps_text)   |             |

***

### PSI\_PS\_CALL

```cpp
#define PSI_PS_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_ps.h:41

***

### MYSQL\_CREATE\_PS

```cpp
#define MYSQL_CREATE_PS(IDENTITY, ID, LOCKER, NAME, NAME_LENGTH, IDENTITY, ID, LOCKER, NAME, NAME_LENGTH) NULL
```

Defined in psi/mysql\_ps.h:56

***

### MYSQL\_EXECUTE\_PS

```cpp
#define MYSQL_EXECUTE_PS(LOCKER, PREPARED_STMT, LOCKER, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql\_ps.h:58

***

### MYSQL\_DESTROY\_PS

```cpp
#define MYSQL_DESTROY_PS(PREPARED_STMT, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql\_ps.h:60

***

### MYSQL\_REPREPARE\_PS

```cpp
#define MYSQL_REPREPARE_PS(PREPARED_STMT, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql\_ps.h:62

***

### MYSQL\_SET\_PS\_TEXT

```cpp
#define MYSQL_SET_PS_TEXT(PREPARED_STMT, SQLTEXT, SQLTEXT_LENGTH, PREPARED_STMT, SQLTEXT, SQLTEXT_LENGTH) do {} while (0)
```

Defined in psi/mysql\_ps.h:64
