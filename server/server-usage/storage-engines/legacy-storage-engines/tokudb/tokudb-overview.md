# TokuDB Overview

{% include "../../../../.gitbook/includes/tokudb-has-been-deprecated-....md" %}

The TokuDB storage engine is for use in high-performance and write-intensive environments, offering increased compression and better performance.

It is available in an open-source version, included with 64-bit MariaDB (but not enabled by default), and an Enterprise edition available from Tokutek.

Note that the default value of [tokudb\_pk\_insert\_mode](tokudb-system-variables.md#tokudb_pk_insert_mode) will prevent row-based replication from working. To use RBR, change the value of this variable.

The version of TokuDB in your local MariaDB is available by querying the [tokudb\_version](tokudb-system-variables.md) status variable:

```
SHOW VARIABLES LIKE 'tokudb_version';
```

In the MariaDB binary tarballs, only the ones labeled "glibc\_214" have TokuDB.

1. [↑](tokudb-overview.md#_ref-0) with this version, TokuDB now follows the version numbering of Percona XtraDB

{% @marketo/form formId="4316" %}
