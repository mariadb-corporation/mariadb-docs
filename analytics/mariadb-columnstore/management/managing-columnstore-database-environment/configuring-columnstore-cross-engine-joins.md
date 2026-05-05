---
description: >-
  Configure MariaDB ColumnStore to perform cross-engine joins with
  non-ColumnStore tables (InnoDB, MyISAM) by setting CrossEngineSupport
  connection details in Columnstore.xml.
hidden: true
---

# Configuring ColumnStore Cross-Engine Joins

## Overview

MariaDB ColumnStore allows ColumnStore tables to be joined with non-ColumnStore tables (e.g. [MyISAM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine) tables) within a query. The non-ColumnStore table may be on the MariaDB ColumnStore system _or_ on an external server that supports MariaDB client connections.

To enable this process, the section in `Columnstore.xml` is configured with connection information.

The following is an example entry in the Columnstore.XML configuration file to gain access to joined tables, Single Server MariaDB ColumnStore install. The Host needs to be either `127.0.0.1` or `localhost`:

```xml
<CrossEngineSupport>
       <Host>127.0.0.1</Host>
       <Port>3306</Port>
       <User>mydbuser</User>
       <Password>pwd</Password>
</CrossEngineSupport>
```

For a multi-node MariaDB Columnstore installation, the host needs to be the IP address of the user module #1 or the combination of user/performance module #1.

If the MariaDB client is running on an external server, it is the IP address of that server.

For version 1.2.0 onwards, the additional options in the section are supported to add SSL/TLS encryption to the connections:

```xml
<TLSCA></TLSCA>
       <TLSClientCert></TLSClientCert>
       <TLSClientKey></TLSClientKey>
```

This change must be made while the ColumnStore server is down. In a multi-node deployment, the change must be made on the PrimProc[^1] node only as this is replicated to other instances upon restart.

Read up on how to make changes via the command line to `Columnstore.xml`: [on this page](../columnstore-system/columnstore-configuration-file-update-and-distribution.md).

## Troubleshooting

**ERROR 1815 (HY000): Internal error: IDB-8001: CrossEngineSupport section in Columnstore.xml is not properly configured**

* Confirm that `Columnstore.xml` was correctly updated on pm1 and the server restarted.

**ERROR 1815 (HY000): Internal error: fatal error in drizzle\_con\_connect() (23)(23)**

* Confirm that the values specified for `CrossEngineSupport` in `ColumnStore.xml` are correct for the login to be used.

**ERROR 1815 (HY000): Internal error: fatal error executing query in crossengine client lib (17)(17)**

* Confirm that the login used has create temporary tables permission on `infinidb_vtable`:

```sql
GRANT CREATE temporary tables ON infinidb_vtable.* TO mydbuser@127.0.0.1;
```

* Confirm that the login used has the `SELECT` privilege on the table referenced in the cross-engine join. Verify by attempting to connect from each node using `mcsmysql` and query the table you want to reference:Prim

```sql
mcsmysql -u mydbuser -p -h 127.0.0.1 
> use mydb;
> select * from innodb_table limit 10;
```

## Notes

* Cross engine will not work against a `MyISAM/Aria` table that has 0 or 1 rows in it. This is due to MariaDB's optimizer shortcut for this specific condition. We recommend using InnoDB instead of `MyISAM/Aria` for this case.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: PrimProc is the ColumnStore Primitives Processor.
