# NEW\_MODE

The `NEW_MODE` system variable and command line switch were introduced in [MariaDB 11.4](https://mariadb.com/docs/release-notes/community-server/mariadb-11-4-series/what-is-mariadb-114) to provide a way to enable new behavior in otherwise stable versions. Specifying a flag in the `NEW_MODE` variable enables the corresponding new behavior; otherwise, the old (stable) behavior is used. This can be useful to preserve execution plans in stable versions that may change when the new behavior is active.

A sample usage scenario is:

* a fix (new behavior) is pushed into stable releases (for example, MariaDB 11.4 and MariaDB 11.8). It becomes available in `NEW_MODE` but isn't enabled by default.
* in MariaDB 12.1, the fix (new behavior) is enabled without the switch. There's no way to turn it off.
  * `NEW_MODE` does not list the fix as something that can be turned on.
  * if you specify `fix_X` that is no longer switchable, a warning is printed. However, if you specify `fix_that_never_existed`, an error is produced.

## Syntax

You can set `NEW_MODE` from the [command line](../starting-and-stopping-mariadb/mariadbd-options.md) using the `--new-mode` option, or by setting the [new\_mode](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#new_mode) system variable.

```sql
SET [GLOBAL|SESSION] new_mode = 'fix_1[,fix_2]...';
```

The session value only affects the current client and can be changed by the client when required. Setting the global value requires the SUPER privilege, and the change will affect any clients that connect from that point forward.

### Example

```sql
SET GLOBAL new_mode = 'FIX_DISK_TMPTABLE_COSTS';
...
SET new_mode = 'FIX_DISK_TMPTABLE_COSTS,FIX_INDEX_STATS_FOR_ALL_NULLS';
...
SET SESSION new_mode = 'FIX_INDEX_STATS_FOR_ALL_NULLS';

SET new_mode = '';
```

## Available NEW_MODE Flags

1. `FIX_DISK_TMPTABLE_COSTS`
2. `FIX_INDEX_STATS_FOR_ALL_NULLS`

### FIX_DISK_TMPTABLE_COSTS

This flag improves the cost computation for using temporary tables in certain cases, including semi-join subquery materialization ([MDEV-37723](https://jira.mariadb.org/browse/MDEV-37723)).

### FIX_INDEX_STATS_FOR_ALL_NULLS

This flag improves the selection of execution plans when indexed columns contain only NULL values ([MDEV-36761](https://jira.mariadb.org/browse/MDEV-36761)).
