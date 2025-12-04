---
description: Information about XtraDB, an storage engine used in old MariaDB versions.
---

# Using InnoDB Instead of XtraDB

XtraDB, previously the default InnoDB replacement in MariaDB, is no longer included in standard distributions. MariaDB now uses InnoDB by default.

The reasons you may want to use InnoDB instead of XtraDB in earlier versions of MariaDB are:

* You want to benchmark the difference between InnoDB/XtraDB
* You hit a bug in XtraDB
* You got a table space crash in XtraDB and recovery doesn't work. In some cases InnoDB may do a better job to recover data.

## See Also

* [Compiling with the InnoDB plugin from Oracle](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/compiling-with-the-innodb-plugin-from-oracle.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
