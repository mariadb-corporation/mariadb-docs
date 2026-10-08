---
title: backports-10.6.8-4
---

MariaDB Enterprise Server enables a predictable development and operations experience through an [enterprise lifecycle](../../enterprise-server/about/enterprise-server-lifecycle.md). These new features have been backported after reaching maturity in MariaDB Community Server:

* [mariadb-dump option --as-of](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) reads data as of specific timestamp from system-versioned tables. (MENT-1457)
* Added [JSON\_EQUALS() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals) to check JSON equality. (MENT-1452)
* Added [JSON\_NORMALIZE() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize) to normalize JSON values. (MENT-1456)
* Added [password\_reuse\_check password validation plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password-reuse-check-plugin). (MENT-1451)
