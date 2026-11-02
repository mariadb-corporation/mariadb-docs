---
description: >-
  Macros that register statement instruments and report a statement's start,
  text, digest, lock time, rows sent and examined, and end to the Performance
  Schema.
---

# Statement Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Macros

| Name                                                                                                  | Description             |
| ----------------------------------------------------------------------------------------------------- | ----------------------- |
| [`PSI_STATEMENT_CALL`](statement_instrumentation.md#psi_statement_call)                               |                         |
| [`PSI_DIGEST_CALL`](statement_instrumentation.md#psi_digest_call)                                     |                         |
| [`mysql_statement_register`](statement_instrumentation.md#mysql_statement_register)                   | Statement registration. |
| [`MYSQL_DIGEST_START`](statement_instrumentation.md#mysql_digest_start)                               |                         |
| [`MYSQL_DIGEST_END`](statement_instrumentation.md#mysql_digest_end)                                   |                         |
| [`MYSQL_START_STATEMENT`](statement_instrumentation.md#mysql_start_statement)                         |                         |
| [`MYSQL_REFINE_STATEMENT`](statement_instrumentation.md#mysql_refine_statement)                       |                         |
| [`MYSQL_SET_STATEMENT_TEXT`](statement_instrumentation.md#mysql_set_statement_text)                   |                         |
| [`MYSQL_SET_STATEMENT_LOCK_TIME`](statement_instrumentation.md#mysql_set_statement_lock_time)         |                         |
| [`MYSQL_SET_STATEMENT_ROWS_SENT`](statement_instrumentation.md#mysql_set_statement_rows_sent)         |                         |
| [`MYSQL_SET_STATEMENT_ROWS_EXAMINED`](statement_instrumentation.md#mysql_set_statement_rows_examined) |                         |
| [`MYSQL_END_STATEMENT`](statement_instrumentation.md#mysql_end_statement)                             |                         |

***

### PSI\_STATEMENT\_CALL

```cpp
#define PSI_STATEMENT_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_statement.h:44

***

### PSI\_DIGEST\_CALL

```cpp
#define PSI_DIGEST_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_statement.h:48

***

### mysql\_statement\_register

```cpp
#define mysql_statement_register(P1, P2, P3, P1, P2, P3) do {} while (0)
```

Defined in psi/mysql\_statement.h:59

Statement registration.

***

### MYSQL\_DIGEST\_START

```cpp
#define MYSQL_DIGEST_START(LOCKER, LOCKER) NULL
```

Defined in psi/mysql\_statement.h:67

***

### MYSQL\_DIGEST\_END

```cpp
#define MYSQL_DIGEST_END(LOCKER, DIGEST, LOCKER, DIGEST) do {} while (0)
```

Defined in psi/mysql\_statement.h:75

***

### MYSQL\_START\_STATEMENT

```cpp
#define MYSQL_START_STATEMENT(STATE, K, DB, DB_LEN, CS, SPS, STATE, K, DB, DB_LEN, CS, SPS) NULL
```

Defined in psi/mysql\_statement.h:83

***

### MYSQL\_REFINE\_STATEMENT

```cpp
#define MYSQL_REFINE_STATEMENT(LOCKER, K, LOCKER, K) NULL
```

Defined in psi/mysql\_statement.h:91

***

### MYSQL\_SET\_STATEMENT\_TEXT

```cpp
#define MYSQL_SET_STATEMENT_TEXT(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql\_statement.h:99

***

### MYSQL\_SET\_STATEMENT\_LOCK\_TIME

```cpp
#define MYSQL_SET_STATEMENT_LOCK_TIME(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql\_statement.h:107

***

### MYSQL\_SET\_STATEMENT\_ROWS\_SENT

```cpp
#define MYSQL_SET_STATEMENT_ROWS_SENT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql\_statement.h:115

***

### MYSQL\_SET\_STATEMENT\_ROWS\_EXAMINED

```cpp
#define MYSQL_SET_STATEMENT_ROWS_EXAMINED(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql\_statement.h:123

***

### MYSQL\_END\_STATEMENT

```cpp
#define MYSQL_END_STATEMENT(LOCKER, DA, LOCKER, DA) do {} while (0)
```

Defined in psi/mysql\_statement.h:131

## Typedefs

| Return                         | Name                                                        | Description |
| ------------------------------ | ----------------------------------------------------------- | ----------- |
| `const struct charset_info_st` | [`CHARSET_INFO`](statement_instrumentation.md#charset_info) |             |

***

### CHARSET\_INFO

```cpp
using CHARSET_INFO = const struct charset_info_st
```

Defined in psi/mysql\_statement.h:41
