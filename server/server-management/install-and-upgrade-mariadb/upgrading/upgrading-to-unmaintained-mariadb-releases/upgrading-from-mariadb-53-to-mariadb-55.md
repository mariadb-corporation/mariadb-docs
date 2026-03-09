---
description: An upgrading guide for unmaintained versions of MariaDB Community Server.
---

# Upgrading from MariaDB 5.3 to MariaDB 5.5

## What you need to know

There are no changes in table or index formats between [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3) and [MariaDB\
5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3), so on most servers the upgrade should be painless.

### How to upgrade

The suggested upgrade procedure is:

1. For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.
2. Shutdown [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3)
3. Take a backup (this is the perfect time to take a backup of your databases)
4. Uninstall [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3)
5. Install [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) \[[1](upgrading-from-mariadb-53-to-mariadb-55.md#_note-0)]
6. Run [mysql\_upgrade](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md)

* Ubuntu and Debian packages do this automatically when they are installed; Red Hat, CentOS, and Fedora packages do not
* `mysql_upgrade` does two things:
  1. Upgrades the permission tables in the `mysql` database with some new fields
  2. Does a very quick check of all tables and marks them as compatible with [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* In most cases this should be a fast operation (depending of course on the number of tables)

1. Add new options to [my.cnf](../../configuring-mariadb/configuring-mariadb-with-option-files.md) to enable features

* If you change `my.cnf` then you need to restart `mysqld`

### Incompatible changes between 5.3 and 5.5

As mentioned previously, on most servers upgrading from 5.5 should be painless.\
However, there are some things that have changed which could affect an upgrade:

#### XtraDB options that have changed default values

| Option                                                                                                                                   | Old value | New value |
| ---------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------- |
| [innodb\_change\_buffering](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering)          | inserts   | all       |
| [innodb\_flush\_neighbor\_pages](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_neighbor_pages) | 1         | area      |

#### Options that have been removed or renamed

Percona, the provider of [XtraDB](../../../../server-usage/storage-engines/innodb/innodb-unmaintained/about-xtradb.md), does not provide all earlier XtraDB features in the 5.5 code base. Because of that, [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) can't provide them either. The following options are not supported by XtraDB 5.5. If you are using them in any of your my.cnf files, you should remove them before upgrading to 5.5.

* [innodb\_adaptive\_checkpoint](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_checkpoint); Use [innodb\_adaptive\_flushing\_method](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_flushing_method) instead.
* [innodb\_auto\_lru\_dump](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_auto_lru_dump); Use [innodb\_buffer\_pool\_restore\_at\_startup](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_restore_at_startup) instead (and [innodb\_buffer\_pool\_load\_at\_startup](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_load_at_startup) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)).
* innodb\_blocking\_lru\_restore; Use [innodb\_blocking\_buffer\_pool\_restore](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_blocking_buffer_pool_restore) instead.
* [innodb\_enable\_unsafe\_group\_commit](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_enable_unsafe_group_commit)
* innodb\_expand\_import; Use [innodb\_import\_table\_from\_xtrabackup](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_import_table_from_xtrabackup) instead.
* [innodb\_extra\_rsegments](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_extra_rsegments); Use [innodb\_rollback\_segments](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_rollback_segments) instead.
* [innodb\_extra\_undoslots](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_extra_undoslots)
* innodb\_fast\_recovery
* innodb\_flush\_log\_at\_trx\_commit\_session
* [innodb\_overwrite\_relay\_log\_info](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_recovery_update_relay_log); Use [innodb\_recovery\_update\_relay\_log](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_recovery_update_relay_log) instead.
* [innodb\_pass\_corrupt\_table](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_pass_corrupt_table); Use [innodb\_corrupt\_table\_action](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_corrupt_table_action) instead.
* [innodb\_use\_purge\_thread](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_use_purge_thread)

## Notes

1. [↑](upgrading-from-mariadb-53-to-mariadb-55.md#_ref-0) If using a MariaDB `apt` or `yum` [repository](https://downloads.mariadb.org/mariadb/repositories/), it is often enough to replace instances of '5.3' with '5.5' and then run an update/upgrade. For example, in Ubuntu/Debian update the MariaDB `sources.list` entry from something that looks similar to this:

```
deb http://ftp.osuosl.org/pub/mariadb/repo/5.3/ubuntu trusty main
```

To something like this:

```
deb http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntu trusty main
```

And then run

```
apt-get update && apt-get upgrade
```

And in Red Hat, CentOS, and Fedora, change the `baseurl` line from something that looks like this:

```
baseurl = http://yum.mariadb.org/5.3/centos6-amd64
```

To something that looks like this:

```
baseurl = http://yum.mariadb.org/5.5/centos6-amd64
```

And then run

```
yum update
```

## See also

* [The features in MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* [Perconas guide of how to upgrade to 5.5](https://www.percona.com/doc/percona-server/5.5/upgrading_guide_51_55.html)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
