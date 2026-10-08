---
title: backports-10.5.18-13
---

MariaDB Enterprise Server enables a predictable development and operations experience through an enterprise lifecycle. These new features have been backported after reaching maturity in MariaDB Community Server:

* The new [slave\_max\_statement\_time system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is available to set the maximum execution time for queries on replica nodes. (MENT-1566, [MDEV-27161](https://jira.mariadb.org/browse/MDEV-27161))
  * When a query takes more than `slave_max_statement_time` seconds to run on the replica (slave) node, the query is aborted, and replication stops with an error.
  * The system variable can be set to a decimal value, where the decimal component has microsecond precision.
  * When set to `0`, there is no timeout.
  * The default value is `0`.
