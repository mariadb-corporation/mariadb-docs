# mysqlhotcopy

{% hint style="warning" %}
mysqlhotcopy is deprecated and may be removed in a future release.
{% endhint %}

`mysqlhotcopy` uses [FLUSH TABLES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), [LOCK TABLES](../../reference/sql-statements/transactions/lock-tables.md), and cp or scp to make a database backup.

From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), the client is called `mariadb-hotcopy`. It can still be accessed under its original `mysqlhotcopy` name via a symlink in Linux, or an alternate binary in Windows.

See [mariadb-hotcopy](../backup-restore-and-import-clients/mariadb-hotcopy.md) for details.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
