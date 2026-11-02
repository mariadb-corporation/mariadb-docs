---
description: >-
  Plugin API reference: Stored Programs Instrumentation. Generated from the
  MariaDB server headers by doxygen and moxygen.
---

# Stored Programs Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

Instrumentation helpers for stored programs.

## Macros

| Name                                                                          | Description |
| ----------------------------------------------------------------------------- | ----------- |
| [`PSI_SP_CALL`](stored_programs_instrumentation.md#psi_sp_call)               |             |
| [`MYSQL_START_SP`](stored_programs_instrumentation.md#mysql_start_sp)         |             |
| [`MYSQL_END_SP`](stored_programs_instrumentation.md#mysql_end_sp)             |             |
| [`MYSQL_DROP_SP`](stored_programs_instrumentation.md#mysql_drop_sp)           |             |
| [`MYSQL_GET_SP_SHARE`](stored_programs_instrumentation.md#mysql_get_sp_share) |             |

***

### PSI\_SP\_CALL

```cpp
#define PSI_SP_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_sp.h:41

***

### MYSQL\_START\_SP

```cpp
#define MYSQL_START_SP(STATE, SP_SHARE, STATE, SP_SHARE) NULL
```

Defined in psi/mysql\_sp.h:48

***

### MYSQL\_END\_SP

```cpp
#define MYSQL_END_SP(LOCKER, LOCKER) do {} while (0)
```

Defined in psi/mysql\_sp.h:57

***

### MYSQL\_DROP\_SP

```cpp
#define MYSQL_DROP_SP(OT, SN, SNL, ON, ONL, OT, SN, SNL, ON, ONL) do {} while (0)
```

Defined in psi/mysql\_sp.h:65

***

### MYSQL\_GET\_SP\_SHARE

```cpp
#define MYSQL_GET_SP_SHARE(OT, SN, SNL, ON, ONL, OT, SN, SNL, ON, ONL) NULL
```

Defined in psi/mysql\_sp.h:73
