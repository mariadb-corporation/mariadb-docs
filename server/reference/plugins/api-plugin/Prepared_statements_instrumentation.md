---
description: >-
  Plugin API reference: Prepared Statements Instrumentation. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Prepared Statements Instrumentation

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Instrumentation Interface`](Instrumentation_interface.md)

Instrumentation helpers for prepared statements.

## Macros

| Name | Description |
|------|-------------|
| [`PSI_PS_CALL`](#psi_ps_call)  |  |
| [`MYSQL_CREATE_PS`](#mysql_create_ps)  |  |
| [`MYSQL_EXECUTE_PS`](#mysql_execute_ps)  |  |
| [`MYSQL_DESTROY_PS`](#mysql_destroy_ps)  |  |
| [`MYSQL_REPREPARE_PS`](#mysql_reprepare_ps)  |  |
| [`MYSQL_SET_PS_TEXT`](#mysql_set_ps_text)  |  |

---

### PSI_PS_CALL

```cpp
#define PSI_PS_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_ps.h:41

---

### MYSQL_CREATE_PS

```cpp
#define MYSQL_CREATE_PS(IDENTITY, ID, LOCKER, NAME, NAME_LENGTH, IDENTITY, ID, LOCKER, NAME, NAME_LENGTH) NULL
```

Defined in psi/mysql_ps.h:56

---

### MYSQL_EXECUTE_PS

```cpp
#define MYSQL_EXECUTE_PS(LOCKER, PREPARED_STMT, LOCKER, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql_ps.h:58

---

### MYSQL_DESTROY_PS

```cpp
#define MYSQL_DESTROY_PS(PREPARED_STMT, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql_ps.h:60

---

### MYSQL_REPREPARE_PS

```cpp
#define MYSQL_REPREPARE_PS(PREPARED_STMT, PREPARED_STMT) do {} while (0)
```

Defined in psi/mysql_ps.h:62

---

### MYSQL_SET_PS_TEXT

```cpp
#define MYSQL_SET_PS_TEXT(PREPARED_STMT, SQLTEXT, SQLTEXT_LENGTH, PREPARED_STMT, SQLTEXT, SQLTEXT_LENGTH) do {} while (0)
```

Defined in psi/mysql_ps.h:64

