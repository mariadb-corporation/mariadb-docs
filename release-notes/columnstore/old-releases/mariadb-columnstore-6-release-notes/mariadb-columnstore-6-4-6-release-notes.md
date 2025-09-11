# MariaDB ColumnStore 6.4.6 Release Notes

## Overview

[MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) 6.4.6 is a maintenance release of [MariaDB Enterprise ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) . MariaDB Enterprise ColumnStore is a columnar storage engine included with MariaDB Enterprise Server. This is the seventh release in the Enterprise ColumnStore 6 series.

MariaDB Enterprise ColumnStore 6.4.6 was released on 2022-09-30. This release is of General Availability (GA) maturity.

This release of MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server 10.6.8-4.

## Issues Fixed

### Can result in unexpected behavior

* An error can be returned during disk aggregation. ([MCOL-5213](https://jira.mariadb.org/browse/MCOL-5213))
  * The following error message could be raised to the client:

```
MCS-2056: There was an IO error during a disk-based aggregation: No such file or directory
```

**GROUP BY can return duplicates. (**[**MCOL-5213**](https://jira.mariadb.org/browse/MCOL-5213)**)**

## Platforms

In alignment to the enterprise lifecycle, MariaDB Enterprise ColumnStore 6.4.6 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64)
* Rocky Linux 8 (x86\_64)
* Ubuntu 18.04 (x86\_64)
* Ubuntu 20.04 (x86\_64)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
