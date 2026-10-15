---
description: >-
  Parallel logical backup, restore, and server-to-server copy of MariaDB
  databases with the dump, load, and copy utilities of MariaDB Shell.
icon: database
---

# Dump and Load

The dump and load utilities of MariaDB Shell take logical backups of a running MariaDB server, restore them, and copy databases from one server to another. A dump is a consistent snapshot of the whole server, of selected schemas, or of selected tables, written as compressed chunks in parallel to local disk or to cloud object storage. A load restores such a dump in parallel, completely or selectively, and resumes where it stopped if it is interrupted.

The utilities are functions of the `util` global object. In Python mode you call them in snake case, such as `util.dump_instance()`, and pass options as a dictionary with camelCase keys, such as `{"threads": 8}`. You can also call them from the operating system shell through [command line integration](../../using-mariadb-shell/command-line-integration.md).

```text
MariaDB localhost:3306 ssl  Py > util.dump_schemas(["shop"], "/backups/shop", {"threads": 8})
```

## Why Use Them

* **Fast.** Dumps and loads run on several threads at once. Each table is split into chunks, so even a single large table is dumped and loaded in parallel, and the data is compressed with zstd by default.
* **Safe.** A dump is consistent even while applications keep writing. Optional checksums computed at dump time are verified at load time, and a load records every completed step so that running it again continues where it stopped.
* **Flexible.** You can dump a server, some schemas, or some tables; filter by schema, table, routine, event, trigger, and account; restore only part of a dump; or load a schema under a new name.
* **Cloud-ready.** Besides local and network file systems, dumps can be written to and loaded from Amazon S3 and S3-compatible storage, OCI Object Storage, and Azure Blob Storage. A load can start while the dump is still being written.
* **Operations-friendly.** Dry runs, progress reporting, per-thread rate limits, and provisioning of new replicas at the exact GTID position of the dump.

## Where It Fits

| Tool | Type | Best for | Trade-off |
| --- | --- | --- | --- |
| `mariadb-dump` | Logical, single-threaded | Small databases, simple scripts, a single SQL file | Slow on large data sets; one output stream |
| `mariadb-backup` | Physical (copies data files) | The fastest full-server backup, point-in-time recovery | Whole server only; tied to the server version and platform |
| MariaDB Shell dump and load | Logical, parallel | Migrations and upgrades, partial restores, cloud storage, provisioning replicas | A logical restore of a full server is slower than a physical one |

The utilities complement `mariadb-backup`, and replace `mariadb-dump` for databases of any significant size.

{% hint style="info" %}
The utilities work with MariaDB 10.11 or later. Dumps of a MariaDB server can only be loaded into a MariaDB server. See [MariaDB-Specific Features](mariadb-specific-features.md#vendor-rules).
{% endhint %}

## Functions

All nine functions share one engine, so the capabilities described in this section apply to each of them. Every function documents its options in the shell, for example `\? util.dump_instance` or `util.help("dump_instance")`.

| Function | What it does | Reference |
| --- | --- | --- |
| `util.dump_instance(outputUrl[, options])` | Dumps every user schema, together with accounts, roles, and grants | [Dump Utilities](dump-utilities.md) |
| `util.dump_schemas(schemas, outputUrl[, options])` | Dumps the listed schemas | [Dump Utilities](dump-utilities.md) |
| `util.dump_tables(schema, tables, outputUrl[, options])` | Dumps the listed tables and views of one schema | [Dump Utilities](dump-utilities.md) |
| `util.load_dump(url[, options])` | Loads a dump made by any of the three dump functions, fully or selectively | [Load Dump Utility](load-dump-utility.md) |
| `util.copy_instance(connectionData[, options])` | Copies the whole server to another server, without intermediate files | [Copy Utilities](copy-utilities.md) |
| `util.copy_schemas(schemas, connectionData[, options])` | Copies the listed schemas to another server | [Copy Utilities](copy-utilities.md) |
| `util.copy_tables(schema, tables, connectionData[, options])` | Copies the listed tables and views to another server | [Copy Utilities](copy-utilities.md) |
| `util.export_table(table, outputUrl[, options])` | Writes the rows of one table to a delimited file | [Table Export and Import](../table-export-and-import.md) |
| `util.import_table(urls[, options])` | Loads delimited files into a table in parallel | [Table Export and Import](../table-export-and-import.md) |

## In This Section

{% columns %}
{% column %}
{% content-ref url="quick-start.md" %}
[quick-start.md](quick-start.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Prerequisites, and ready-to-adapt examples for a backup, a renamed restore, a server-to-server copy, and a new replica.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="how-dump-and-load-work.md" %}
[how-dump-and-load-work.md](how-dump-and-load-work.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The dump and load pipelines, the files in a dump directory, how a dump stays consistent, and how a load schedules and resumes its work.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dump-utilities.md" %}
[dump-utilities.md](dump-utilities.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The options of `util.dump_instance()`, `util.dump_schemas()`, and `util.dump_tables()`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="load-dump-utility.md" %}
[load-dump-utility.md](load-dump-utility.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The options of `util.load_dump()`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="copy-utilities.md" %}
[copy-utilities.md](copy-utilities.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The options of `util.copy_instance()`, `util.copy_schemas()`, and `util.copy_tables()`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="what-a-dump-carries.md" %}
[what-a-dump-carries.md](what-a-dump-carries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Which objects a dump contains, which it leaves out by design, and what the manifest records about the source server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-specific-features.md" %}
[mariadb-specific-features.md](mariadb-specific-features.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How sequences, packages, roles, system-versioned tables, MariaDB data types, `BACKUP STAGE`, and MariaDB GTIDs are dumped and loaded.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="object-storage.md" %}
[object-storage.md](object-storage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Writing dumps to and loading them from Amazon S3, S3-compatible storage, OCI Object Storage, and Azure Blob Storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="limitations.md" %}
[limitations.md](limitations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
What the utilities do not do on MariaDB, how to prepare a target server, and known issues.
{% endcolumn %}
{% endcolumns %}
