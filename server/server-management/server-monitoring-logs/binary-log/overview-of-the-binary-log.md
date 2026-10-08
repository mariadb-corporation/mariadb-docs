---
description: >-
  Introduction to the purpose and structure of the binary log, explaining how it
  records data changes (DML) and structure changes (DDL) for replication and
  recovery.
---

# Overview of the Binary Log

The binary log contains a record of all changes to the databases, both data and structure, as well as how long each statement took to execute. It consists of a set of binary log files and an index.

This means that statements such as [CREATE](../../../reference/sql-statements/data-definition/create/), [ALTER](../../../reference/sql-statements/data-definition/alter/), [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md), [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) are logged, whereas statements that have no effect on the data, such as `SELECT` and `SHOW`, are not be logged. If you want to log these, too (at a cost in performance), use the [general query log](../general-query-log.md).

If a statement may potentially have an effect, but doesn't, such as an `UPDATE` or `DELETE` that returns no rows, it is still logged (this applies to the default statement-based logging, not to row-based logging - see [Binary Log Formats](binary-log-formats.md)).

The purpose of the binary log is:

* To enable [replication](../../../ha-and-performance/standard-replication/), where data is sent from one or more primary servers to one or more replica servers based on the contents of the binary log.
* To assist in backup operations.

A MariaDB server with the binary log enabled runs slightly more slowly.

It is important to protect the binary log, as it may contain sensitive information, including passwords.

Binary logs are stored in a binary, not plain text, format, and so are not readable with a regular editor. However, MariaDB includes [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/), a command-line tool for plain-text processing of binary logs.

{% if  %}
{% hint style="info" %}
From MariaDB 12.3, InnoDB-based binary logs can be used. (This is configurable, and not the default.)

If configured, binary logs are stored in InnoDB tablespaces, rather than binary files. This removes the need of protecting binary logs separately, since they'll "inherit" the same protection as other MariaDB database tables. Also, any other information about log **files** doesn't apply – for example, you cannot specify a storage location for binary logs stored in an InnoDB tablespace.

InnoDB-based binary logs are enabled by setting `binlog_storage_engine=innodb` in the server configuration. See [InnoDB-Based Binary Log](../../../ha-and-performance/standard-replication/innodb-based-binary-log.md) for more information.
{% endhint %}
{% endif %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
