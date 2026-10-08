---
title: backports-10.6.12-7
---

* In previous releases, the number of undo logs was configurable before InnoDB was initialized. With this release, the number of undo logs can also be configured after install.
  * The number of undo logs is configured by the InnoDB system variable `--innodb-undo-tablespaces`.
  * Splitting undo logs over multiple tablespaces can reduce the size of a single tablespace, especially the InnoDB system tablespace.
  * In previous releases, the number of undo logs had to be configured before InnoDB was initialized, so changing the number of undo logs would require setting up a new server instance. With this backport from MariaDB Community Server 10.11, the number of undo logs can be changed so it will take effect with the next server start. (MENT-1650)
