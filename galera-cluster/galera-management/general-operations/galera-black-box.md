---
description: >-
  The Galera Black Box is a MariaDB Enterprise Server feature that keeps recent
  debug log messages in a shared-memory ring buffer so they survive a crash and
  can be analyzed with mariadb-bbtool.
---

# Galera Black Box

{% hint style="info" %}
The Black Box is a **MariaDB Enterprise Server** feature. It is not available in community MariaDB Server, nor on Windows, macOS, or the embedded server.
{% endhint %}

## Overview

The Black Box is an in-memory (shared-memory) ring buffer that continuously records debug log messages. Because it lives in shared memory rather than in the server process, its contents survive a server crash and can be examined afterwards, which helps support and developers diagnose hard-to-reproduce failures, including in Galera Cluster.

It is disabled by default. To enable it, set a non-zero [wsrep\_black\_box\_size](../../reference/galera-cluster-system-variables.md#wsrep_black_box_size).

## Enabling the Black Box

Configure the size (in bytes) and, optionally, the name in an options file:

```ini
[mariadb]
wsrep_black_box_size = 10485760
wsrep_black_box_name = bb-mariadb
```

* [wsrep\_black\_box\_size](../../reference/galera-cluster-system-variables.md#wsrep_black_box_size) — size in bytes. `0` (default) means no Black Box is created. It is dynamic: changing it at runtime re-creates the Black Box at the new size.
* [wsrep\_black\_box\_name](../../reference/galera-cluster-system-variables.md#wsrep_black_box_name) — the name of the shared-memory object (default `bb-mariadb`). Read-only; set at startup only.

When the server starts, it opens the Black Box in the data directory. If a Black Box with the same name already exists (for example, left behind by a crashed server), its contents are first written to a dump file in the data directory and then it is re-created empty.

## Inspecting the Black Box with mariadb-bbtool

The `mariadb-bbtool` utility, installed alongside the server, operates on a Black Box by name:

```bash
mariadb-bbtool <name> <command>
```

| Command   | Action                                          |
| --------- | ----------------------------------------------- |
| `dump`    | Print the Black Box contents to standard output |
| `status`  | Report the Black Box state                      |
| `enable`  | Put the Black Box into the operational state    |
| `disable` | Put the Black Box into the disabled state       |
| `delete`  | Remove the active Black Box                     |

Run `mariadb-bbtool --help` for usage. A Black Box is in one of three states: Closed, Disabled, or Operational.

For example, to dump the running server's Black Box:

```bash
mariadb-bbtool bb-mariadb dump
```

## See Also

* [Galera Cluster System Variables: wsrep\_black\_box\_size](../../reference/galera-cluster-system-variables.md#wsrep_black_box_size)
* [Galera Cluster System Variables: wsrep\_black\_box\_name](../../reference/galera-cluster-system-variables.md#wsrep_black_box_name)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
