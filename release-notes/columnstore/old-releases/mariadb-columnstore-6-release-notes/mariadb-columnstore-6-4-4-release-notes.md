# MariaDB ColumnStore 6.4.4 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 6.4.4 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) . MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the sixth release in the Enterprise ColumnStore 6 series.

MariaDB Enterprise ColumnStore 6.4.4 was released on 2022-08-09. This release is of General Availability (GA) maturity.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.8-4.

## Issues Fixed

### Can result in unexpected behavior

* When disk-based aggregations are enabled, aggregations can fail with the ER\_INTERNAL\_ERROR error code. ([MCOL-5153](https://jira.mariadb.org/browse/MCOL-5153))
  * The following error message could be raised to the client:

```
ERROR 1815 (HY000): Internal error: TupleAggregateStep::threadedAggregateRowGroups()[24] MCS-2054: Unknown error while aggregation.
```

## Platforms

In alignment with the [enterprise lifecycle](../../../enterprise-server/enterprise-server-lifecycle.md), MariaDB Enterprise ColumnStore 6.4.4 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* Rocky Linux 8 (x86\_64)
* Ubuntu 18.04 (x86\_64)
* Ubuntu 20.04 (x86\_64)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
