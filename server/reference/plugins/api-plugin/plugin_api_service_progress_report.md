---
description: >-
  Plugin API reference: Progress Report Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Progress Report Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Allows plugins to report progress of long running operations to the server.

The progress report is visible in SHOW PROCESSLIST, INFORMATION_SCHEMA.PROCESSLIST, and is sent to the client if requested.

The functions are documented at [https://mariadb.com/docs/server/reference/product-development/mariadb-internals/using-mariadb-with-your-programs-api](https://mariadb.com/docs/server/reference/product-development/mariadb-internals/using-mariadb-with-your-programs-api)

## Classes

| Name | Description |
|------|-------------|
| [`progress_report_service_st`](#progress_report_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`thd_proc_info`](#thd_proc_info)  |  |
| [`thd_progress_init`](#thd_progress_init)  |  |
| [`thd_progress_report`](#thd_progress_report)  |  |
| [`thd_progress_next_stage`](#thd_progress_next_stage)  |  |
| [`thd_progress_end`](#thd_progress_end)  |  |
| [`set_thd_proc_info`](#set_thd_proc_info)  |  |

---

### thd_proc_info

```cpp
#define thd_proc_info(thd, msg, thd, msg) set_thd_proc_info(thd, msg, \
                                                   __func__, __FILE__, __LINE__)
```

Defined in service_progress_report.h:44

---

### thd_progress_init

```cpp
#define thd_progress_init(thd, max_stage, thd, max_stage) (progress_report_service->thd_progress_init_func((thd),(max_stage)))
```

Defined in service_progress_report.h:62

---

### thd_progress_report

```cpp
#define thd_progress_report(thd, progress, max_progress, thd, progress, max_progress) (progress_report_service->thd_progress_report_func((thd), (progress), (max_progress)))
```

Defined in service_progress_report.h:63

---

### thd_progress_next_stage

```cpp
#define thd_progress_next_stage(thd, thd) (progress_report_service->thd_progress_next_stage_func(thd))
```

Defined in service_progress_report.h:64

---

### thd_progress_end

```cpp
#define thd_progress_end(thd, thd) (progress_report_service->thd_progress_end_func(thd))
```

Defined in service_progress_report.h:65

---

### set_thd_proc_info

```cpp
#define set_thd_proc_info(thd, info, func, file, line, thd, info, func, file, line) (progress_report_service->set_thd_proc_info_func((thd),(info),(func),(file),(line)))
```

Defined in service_progress_report.h:66

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`progress_report_service_st`](#progress_report_service_st) * | [`progress_report_service`](#progress_report_service)  |  |

---

### progress_report_service

```cpp
struct progress_report_service_st * progress_report_service
```

Type: struct [`progress_report_service_st`](#progress_report_service_st) *

Defined in service_progress_report.h:58


## Class Definitions



### progress_report_service_st

```cpp
#include <service_progress_report.h>
```

```cpp
struct progress_report_service_st
```

Defined in service_progress_report.h:47

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`thd_progress_init_func`](#thd_progress_init_func)  |  |
| `void(*` | [`thd_progress_report_func`](#thd_progress_report_func)  |  |
| `void(*` | [`thd_progress_next_stage_func`](#thd_progress_next_stage_func)  |  |
| `void(*` | [`thd_progress_end_func`](#thd_progress_end_func)  |  |
| `const char *(*` | [`set_thd_proc_info_func`](#set_thd_proc_info_func)  |  |

---

#### thd_progress_init_func

```cpp
void(* thd_progress_init_func)(MYSQL_THD thd, unsigned int max_stage)
```

Defined in service_progress_report.h:48

---

#### thd_progress_report_func

```cpp
void(* thd_progress_report_func)(MYSQL_THD thd, unsigned long long progress, unsigned long long max_progress)
```

Defined in service_progress_report.h:49

---

#### thd_progress_next_stage_func

```cpp
void(* thd_progress_next_stage_func)(MYSQL_THD thd)
```

Defined in service_progress_report.h:52

---

#### thd_progress_end_func

```cpp
void(* thd_progress_end_func)(MYSQL_THD thd)
```

Defined in service_progress_report.h:53

---

#### set_thd_proc_info_func

```cpp
const char *(* set_thd_proc_info_func)(MYSQL_THD, const char *info, const char *func, const char *file, unsigned int line)
```

Defined in service_progress_report.h:54

