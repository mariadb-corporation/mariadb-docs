---
description: >-
  Historical guide on compiling older MariaDB versions with the original Oracle
  InnoDB plugin instead of XtraDB.
---

# Compiling with the InnoDB Plugin from Oracle

MariaDB uses InnoDB as the default storage engine.&#x20;

If you want to use Oracle's InnoDB plugin, then you need to compile MariaDB and**not** specify `--without-plugin-innodb_plugin` when configuring. For example, a simple `./configure` without any options will do.

When the InnoDB plugin is compiled, the `innodb_plugin` test suite will test the InnoDB plugin in addition to xtradb:

```bash
./mysql-test-run --suite=innodb_plugin
```

To use the `innodb_plugin` instead of `xtradb` you can do (for [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)):

```bash
mysqld --ignore-builtin-innodb --plugin-load=innodb=ha_innodb.so \
--plugin_dir=/usr/local/mysql/lib/mysql/plugin
```

## See Also

[replacing-builtin-innodb.html](https://dev.mysql.com/doc/refman/5.1/en/replacing-builtin-innodb.html)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
