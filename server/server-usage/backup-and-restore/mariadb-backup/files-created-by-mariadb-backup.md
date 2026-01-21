---
description: >-
  Reference of files generated during backup. This page explains the purpose of
  metadata files like xtrabackup_checkpoints created by the tool.
---

# Files Created by mariadb-backup

{% include "../../../.gitbook/includes/mariadb-backup-was-previous....md" %}

`mariadb-backup` creates the following files:

### `backup-my.cnf`

During the backup, any server options relevant to `mariadb-backup` are written to the `backup-my.cnf` option file, so that they can be re-read later during the `--prepare` stage.

### `ib_logfile0`

`mariadb-backup` creates an empty InnoDB redo log file called `ib_logfile0` as part of the `--prepare` stage. This file has 3 roles:

1. In the source server, `ib_logfile0` is the first (and possibly the only) InnoDB redo log file.
2. In the non-prepared backup, `ib_logfile0` contains all of the InnoDB redo log copied during the backup.
3. During the `--prepare` stage, `ib_logfile0` is initialized as an empty InnoDB redo log file. That way, if the backup is manually restored, any pre-existing InnoDB redo log files get overwritten by the empty one. This helps to prevent certain kinds of known issues.

{% tabs %}
{% tab title="Current" %}
### `mariadb_backup_binlog_info`

This file stores the binary log file name and position that corresponds to the backup.

This file also stores the value of the [gtid\_current\_pos](../../../ha-and-performance/standard-replication/gtid.md#gtid_current_pos) system variable that correspond to the backup, like this:

```bash
mariadb-bin.000096 568 0-1-2
```

The values in this file are only guaranteed to be consistent with the backup if the [--no-lock](mariadb-backup-options.md#no-lock) option was **not** provided when the backup was taken.
{% endtab %}

{% tab title="< 11.1" %}
### `xtrabackup_binlog_info`

This file stores the binary log file name and position that corresponds to the backup.

This file also stores the value of the [gtid\_current\_pos](../../../ha-and-performance/standard-replication/gtid.md#gtid_current_pos) system variable that correspond to the backup, like this:

```bash
mariadb-bin.000096 568 0-1-2
```

The values in this file are only guaranteed to be consistent with the backup if the [--no-lock](mariadb-backup-options.md#no-lock) option was **not** provided when the backup was taken.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
### `mariadb_backup_binlog_pos_innodb`

This file is created by `mariadb-backup` to provide the binary log file name and position when the `--no-lock` option is used. It can be used instead of the `xtrabackup_binlog_info` file to obtain transactionally consistent binlog coordinates from the backup of a master server with the `--no-lock` option to minimize the impact on a running server.

Whenever a transaction is committed inside InnoDB when the binary log is enabled, the corresponding binlog coordinates are written to the InnoDB redo log along with the transaction commit. This allows one to restore the binlog coordinates corresponding to the last commit done by InnoDB along with a backup.

The limitation of using `xtrabackup_binlog_pos_innodb` with the `--no-lock` option is that no DDL or modification of non-transactional tables should be done during the backup. If the last event in the binlog is a DDL/non-transactional update, the coordinates in the file `xtrabackup_binlog_pos_innodb` are too old. But as long as only InnoDB updates are done during the backup, the coordinates are correct.
{% endtab %}

{% tab title="< 11.1" %}
### `xtrabackup_binlog_pos_innodb`

This file is created by `mariadb-backup` to provide the binary log file name and position when the `--no-lock` option is used. It can be used instead of the `xtrabackup_binlog_info` file to obtain transactionally consistent binlog coordinates from the backup of a master server with the `--no-lock` option to minimize the impact on a running server.

Whenever a transaction is committed inside InnoDB when the binary log is enabled, the corresponding binlog coordinates are written to the InnoDB redo log along with the transaction commit. This allows one to restore the binlog coordinates corresponding to the last commit done by InnoDB along with a backup.

The limitation of using `xtrabackup_binlog_pos_innodb` with the `--no-lock` option is that no DDL or modification of non-transactional tables should be done during the backup. If the last event in the binlog is a DDL/non-transactional update, the coordinates in the file `xtrabackup_binlog_pos_innodb` are too old. But as long as only InnoDB updates are done during the backup, the coordinates are correct.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
### `mariadb_backup_checkpoints`

The `xtrabackup_checkpoints` file contains metadata about the backup.

For example:

```ini
backup_type = full-backuped
from_lsn = 0
to_lsn = 1635102
last_lsn = 1635102
recover_binlog_info = 0
```

See below for a description of the fields.

If the `--extra-lsndir` option is provided, then an extra copy of this file are saved in that directory.
{% endtab %}

{% tab title="< 11.1" %}
### `xtrabackup_checkpoints`

The `xtrabackup_checkpoints` file contains metadata about the backup.

For example:

```ini
backup_type = full-backuped
from_lsn = 0
to_lsn = 1635102
last_lsn = 1635102
recover_binlog_info = 0
```

See below for a description of the fields.

If the `--extra-lsndir` option is provided, then an extra copy of this file are saved in that directory.
{% endtab %}
{% endtabs %}

#### `backup_type`

If the backup is a non-prepared full backup or a non-prepared partial backup, then `backup_type` is set to `full-backuped`.

If the backup is a non-prepared incremental backup, then `backup_type` is set to `incremental`.

If the backup has already been prepared, then `backup_type` is set to `log-applied`.

#### `from_lsn`

If `backup_type` is `full-backuped`, then `from_lsn` has the value of `0`.

If `backup_type` is `incremental`, then `from_lsn` has the value of the log sequence number (LSN) at which the backup started reading from the InnoDB redo log. This is internally used by mariadb-backup when preparing incremental backups.

This value can be manually set during an incremental backup with the --incremental-lsn option. However, it is generally better to let mariadb-backup figure out the `from_lsn` automatically by specifying a parent backup with the `--incremental-basedir` option.

#### `to_lsn`

`to_lsn` has the value of the log sequence number (LSN) of the last checkpoint in the InnoDB redo log. This is internally used by mariadb-backup when preparing incremental backups.

#### `last_lsn`

`last_lsn` has the value of the last log sequence number (LSN) read from the InnoDB redo log. This is internally used by mariadb-backup when preparing incremental backups.

{% tabs %}
{% tab title="Current" %}
### `mariadb_backup_info`

Contains information about the backup. The fields in this file are listed below.

If the `--extra-lsndir` option is provided, an extra copy of this file is saved in that directory.
{% endtab %}

{% tab title="< 11.1" %}
### `xtrabackup_info`

Contains information about the backup. The fields in this file are listed below.

If the `--extra-lsndir` option is provided, an extra copy of this file is saved in that directory.
{% endtab %}
{% endtabs %}

#### `uuid`

If a UUID was provided by the --incremental-history-uuid option, then it are saved here. Otherwise, this is the empty string.

#### `name`

If a name was provided by the `--history` or the `---incremental-history-name` options, then it are saved here. Otherwise, this is the empty string.

#### `tool_name`

The name of the mariadb-backup executable that performed the backup. This is generally `mariadb-backup`.

#### `tool_command`

The arguments that were provided to mariadb-backup when it performed the backup.

#### `tool_version`

The version of mariadb-backup that performed the backup.

#### `ibbackup_version`

The version of mariadb-backup that performed the backup.

#### `server_version`

The version of MariaDB Server that was backed up.

#### `start_time`

The time that the backup started.

#### `end_time`

The time that the backup ended.

#### `lock_time`

The amount of time that mariadb-backup held its locks.

#### `binlog_pos`

This field stores the binary log file name and position that corresponds to the backup.

This field also stores the value of the `gtid_current_pos` system variable that correspond to the backup.

The values in this field are only guaranteed to be consistent with the backup if the `--no-lock` option was **not** provided when the backup was taken.

#### `innodb_from_lsn`

This is identical to `from_lsn` in `xtrabackup_checkpoints`.

If the backup is a full backup, then `innodb_from_lsn` has the value of `0`.

If the backup is an incremental backup, then `innodb_from_lsn` has the value of the log sequence number (LSN) at which the backup started reading from the InnoDB redo log.

#### `innodb_to_lsn`

This is identical to `to_lsn` in `xtrabackup_checkpoints`.

`innodb_to_lsn` has the value of the log sequence number (LSN) of the last checkpoint in the InnoDB redo log.

#### `partial`

If the backup is a partial backup, then this value are `Y`.

Otherwise, this value are `N`.

#### `incremental`

If the backup is an incremental backup, then this value are `Y`.

Otherwise, this value are `N`.

#### `format`

This field's value is the format of the backup.

If the `--stream` option was set to `xbstream`, then this value are `xbstream`.

If the `--stream` option was **not** provided, then this value are `file`.

#### `compressed`

If the `--compress` option was provided, then this value are `compressed`.

Otherwise, this value are `N`.

{% tabs %}
{% tab title="Current" %}
### `mariadb_backup_slave_info`

If the `--slave-info` option is provided, this file contains the `CHANGE MASTER` command that can be used to set up a new server as a slave of the original server's master after the backup has been restored.

`mariadb-backup` does **not** check if GTIDs are being used in replication. It takes a shortcut and assumes that if the [gtid\_slave\_pos](../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos) system variable is non-empty, then it writes the `CHANGE MASTER` command with the `MASTER_USE_GTID` option set to `slave_pos`. Otherwise, it writes the `CHANGE MASTER` command with the `MASTER_LOG_FILE` and `MASTER_LOG_POS` options using the master's binary log file and position. See [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) for more information.
{% endtab %}

{% tab title="< 11.1" %}
### `xtrabackup_slave_info`

If the `--slave-info` option is provided, this file contains the `CHANGE MASTER` command that can be used to set up a new server as a slave of the original server's master after the backup has been restored.

`mariadb-backup` does **not** check if GTIDs are being used in replication. It takes a shortcut and assumes that if the [gtid\_slave\_pos](../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos) system variable is non-empty, then it writes the `CHANGE MASTER` command with the `MASTER_USE_GTID` option set to `slave_pos`. Otherwise, it writes the `CHANGE MASTER` command with the `MASTER_LOG_FILE` and `MASTER_LOG_POS` options using the master's binary log file and position. See [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) for more information.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
### `mariadb_backup_galera_info`

If the `--galera-info` option is provided, this file contains information about a Galera Cluster node's state.

The file contains the values of the [wsrep\_local\_state\_uuid](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_local_state_uuid) and [wsrep\_last\_committed](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_last_committed) status variables.

The values are written in the following format:

```bash
wsrep_local_state_uuid:wsrep_last_committed
```

For example:

```bash
d38587ce-246c-11e5-bcce-6bbd0831cc0f:1352215
```
{% endtab %}

{% tab title="< 11.1" %}
### `xtrabackup_galera_info`

If the `--galera-info` option is provided, this file contains information about a Galera Cluster node's state.

The file contains the values of the [wsrep\_local\_state\_uuid](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_local_state_uuid) and [wsrep\_last\_committed](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_last_committed) status variables.

The values are written in the following format:

```bash
wsrep_local_state_uuid:wsrep_last_committed
```

For example:

```bash
d38587ce-246c-11e5-bcce-6bbd0831cc0f:1352215
```
{% endtab %}
{% endtabs %}

### `<table>.delta`

If the backup is an incremental backup, this file contains changed pages for the table.

### `<table>.delta.meta`

If the backup is an incremental backup, this file contains metadata about `<table>.delta` files. The fields in this file are listed below.

#### `page_size`

This field contains either the value of `innodb_page_size` or the value of the `KEY_BLOCK_SIZE` table option for the table if the `ROW_FORMAT` table option for the table is set to `COMPRESSED`.

#### `zip_size`

If the `ROW_FORMAT` table option for this table is set to `COMPRESSED`, this field contains the value of the compressed page size.

#### `space_id`

This field contains the value of the table's `space_id`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
