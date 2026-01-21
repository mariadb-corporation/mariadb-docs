---
description: >-
  Outdated page regarding migrating from MySQL to MariaDB Server. While
  potentially outdated, these resources may offer historical context or insights
  for specific scenarios.
---

# Upgrading from MySQL 5.7 to MariaDB 10.2

Following compatibility report was done on 10.2.4 and may get some fixing in next minor releases

* MySQL unix socket plugin can be different. MariaDB can get similar usage via INSTALL PLUGIN unix\_socket SONAME 'auth\_socket.so'; you may have to enable this plugin in config files via load plugin.
* When using data type JSON , one should convert type to TEXT, virtual generated column works the same after.
* When using InnoDB FULLTEXT index one should not use innodb\_defragment
* MySQL re-implemented partitioning in 5.7, thus you cannot perform in-place upgrades for partitioned tables. They will require mysqldump/import to work correctly in MariaDB.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
