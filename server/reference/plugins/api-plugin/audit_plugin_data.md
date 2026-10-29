---
description: >-
  Plugin API reference: Audit Plugin. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Audit Plugin

> [`Plugin API`](plugin_api.md) / [`Plugin Types`](plugin_types.md)

API for Audit plugin. ([MYSQL_AUDIT_PLUGIN](api.md#mysql_audit_plugin))

## Groups

| Name | Description |
|------|-------------|
| [`Audit Class: General`](audit_general_class.md) | LOG events occurs before emitting to the general query log. ERROR events occur before transmitting errors to the user. RESULT events occur after transmitting a resultset to the user. STATUS events occur after transmitting a resultset or errors to the user. |
| [`Audit Class: Connection`](audit_connection_class.md) | CONNECT occurs after authentication phase is completed. DISCONNECT occurs after connection is terminated. CHANGE_USER occurs after COM_CHANGE_USER RPC is completed. |
| [`Audit Class: Table`](audit_table_class.md) | LOCK occurs when a connection "locks" (this does not necessarily mean a table lock and also happens for row-locking engines) the table at the beginning of a statement. This event is generated at the beginning of every statement for every affected table, unless there's a LOCK TABLES statement in effect (in which case it is generated once for LOCK TABLES and then is suppressed until the tables are unlocked). |

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_audit`](#st_mysql_audit) | The descriptor structure, that is referred from [st_mysql_plugin](plugin_declaration.md#st_mysql_plugin). |

## Macros

| Name | Description |
|------|-------------|
| [`MYSQL_AUDIT_CLASS_MASK_SIZE`](#mysql_audit_class_mask_size)  |  |
| [`MYSQL_AUDIT_INTERFACE_VERSION`](#mysql_audit_interface_version)  |  |

---

### MYSQL_AUDIT_CLASS_MASK_SIZE

```cpp
#define MYSQL_AUDIT_CLASS_MASK_SIZE 1
```

Defined in plugin_audit.h:34

---

### MYSQL_AUDIT_INTERFACE_VERSION

```cpp
#define MYSQL_AUDIT_INTERFACE_VERSION 0x0304
```

Defined in plugin_audit.h:36


## Class Definitions



### st_mysql_audit

```cpp
#include <plugin_audit.h>
```

```cpp
struct st_mysql_audit
```

Defined in plugin_audit.h:195

The descriptor structure, that is referred from [st_mysql_plugin](plugin_declaration.md#st_mysql_plugin).

[release_thd()](#release_thd) event occurs when the event class consumer is to be disassociated from the specified THD. This would typically occur before some operation which may require sleeping - such as when waiting for the next query from the client.

[event_notify()](#event_notify) is invoked whenever an event occurs which is of any class for which the plugin has interest. The second argument indicates the specific event class and the third argument is data as required for that class.

class_mask is an array of bits used to indicate what event classes that this plugin wants to receive.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version)  |  |
| `void(*` | [`release_thd`](#release_thd)  |  |
| `void(*` | [`event_notify`](#event_notify)  |  |
| `unsigned long` | [`class_mask`](#class_mask)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in plugin_audit.h:197

---

#### release_thd

```cpp
void(* release_thd)(MYSQL_THD)
```

Defined in plugin_audit.h:198

---

#### event_notify

```cpp
void(* event_notify)(MYSQL_THD, unsigned int, const void *)
```

Defined in plugin_audit.h:199

---

#### class_mask

```cpp
unsigned long class_mask[MYSQL_AUDIT_CLASS_MASK_SIZE]
```

Defined in plugin_audit.h:200

