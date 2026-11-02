---
description: >-
  Plugin API reference: Stored Programs Instrumentation. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Stored Programs Instrumentation

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Instrumentation Interface`](Instrumentation_interface.md)

Instrumentation helpers for stored programs.

## Macros

| Name | Description |
|------|-------------|
| [`PSI_SP_CALL`](#psi_sp_call)  |  |
| [`MYSQL_START_SP`](#mysql_start_sp)  |  |
| [`MYSQL_END_SP`](#mysql_end_sp)  |  |
| [`MYSQL_DROP_SP`](#mysql_drop_sp)  |  |
| [`MYSQL_GET_SP_SHARE`](#mysql_get_sp_share)  |  |

---

### PSI_SP_CALL

```cpp
#define PSI_SP_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql_sp.h:41

---

### MYSQL_START_SP

```cpp
#define MYSQL_START_SP(STATE, SP_SHARE, STATE, SP_SHARE) NULL
```

Defined in psi/mysql_sp.h:48

---

### MYSQL_END_SP

```cpp
#define MYSQL_END_SP(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql_sp.h:57

---

### MYSQL_DROP_SP

```cpp
#define MYSQL_DROP_SP(OT, SN, SNL, ON, ONL, OT, SN, SNL, ON, ONL) do {} while (0)
```

Defined in psi/mysql_sp.h:65

---

### MYSQL_GET_SP_SHARE

```cpp
#define MYSQL_GET_SP_SHARE(OT, SN, SNL, ON, ONL, OT, SN, SNL, ON, ONL) NULL
```

Defined in psi/mysql_sp.h:73

