{#statementinstrumentation}

# Statement Instrumentation

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Macros

| Name | Description |
|------|-------------|
| [`mysql_statement_register`](#mysql_statement_register)  | Statement registration. |
| [`MYSQL_DIGEST_START`](#mysql_digest_start)  |  |
| [`MYSQL_DIGEST_END`](#mysql_digest_end)  |  |
| [`MYSQL_START_STATEMENT`](#mysql_start_statement)  |  |
| [`MYSQL_REFINE_STATEMENT`](#mysql_refine_statement)  |  |
| [`MYSQL_SET_STATEMENT_TEXT`](#mysql_set_statement_text)  |  |
| [`MYSQL_SET_STATEMENT_LOCK_TIME`](#mysql_set_statement_lock_time)  |  |
| [`MYSQL_SET_STATEMENT_ROWS_SENT`](#mysql_set_statement_rows_sent)  |  |
| [`MYSQL_SET_STATEMENT_ROWS_EXAMINED`](#mysql_set_statement_rows_examined)  |  |
| [`MYSQL_END_STATEMENT`](#mysql_end_statement)  |  |

---

{#mysql_statement_register}

### mysql_statement_register

```cpp
#define mysql_statement_register(P1, P2, P3, P1, P2, P3) do {} while (0)
```

Defined in psi/mysql_statement.h:59

Statement registration.

---

{#mysql_digest_start}

### MYSQL_DIGEST_START

```cpp
#define MYSQL_DIGEST_START(LOCKER, LOCKER) NULL
```

Defined in psi/mysql_statement.h:67

---

{#mysql_digest_end}

### MYSQL_DIGEST_END

```cpp
#define MYSQL_DIGEST_END(LOCKER, DIGEST, LOCKER, DIGEST) do {} while (0)
```

Defined in psi/mysql_statement.h:75

---

{#mysql_start_statement}

### MYSQL_START_STATEMENT

```cpp
#define MYSQL_START_STATEMENT(STATE, K, DB, DB_LEN, CS, SPS, STATE, K, DB, DB_LEN, CS, SPS) NULL
```

Defined in psi/mysql_statement.h:83

---

{#mysql_refine_statement}

### MYSQL_REFINE_STATEMENT

```cpp
#define MYSQL_REFINE_STATEMENT(LOCKER, K, LOCKER, K) NULL
```

Defined in psi/mysql_statement.h:91

---

{#mysql_set_statement_text}

### MYSQL_SET_STATEMENT_TEXT

```cpp
#define MYSQL_SET_STATEMENT_TEXT(LOCKER, P1, P2, LOCKER, P1, P2) do {} while (0)
```

Defined in psi/mysql_statement.h:99

---

{#mysql_set_statement_lock_time}

### MYSQL_SET_STATEMENT_LOCK_TIME

```cpp
#define MYSQL_SET_STATEMENT_LOCK_TIME(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_statement.h:107

---

{#mysql_set_statement_rows_sent}

### MYSQL_SET_STATEMENT_ROWS_SENT

```cpp
#define MYSQL_SET_STATEMENT_ROWS_SENT(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_statement.h:115

---

{#mysql_set_statement_rows_examined}

### MYSQL_SET_STATEMENT_ROWS_EXAMINED

```cpp
#define MYSQL_SET_STATEMENT_ROWS_EXAMINED(LOCKER, P1, LOCKER, P1) do {} while (0)
```

Defined in psi/mysql_statement.h:123

---

{#mysql_end_statement}

### MYSQL_END_STATEMENT

```cpp
#define MYSQL_END_STATEMENT(LOCKER, DA, LOCKER, DA) do {} while (0)
```

Defined in psi/mysql_statement.h:131

