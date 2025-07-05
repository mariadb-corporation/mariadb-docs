# Limiting Size of Created Disk Temporary Files and Tables Overview

**MariaDB starting with** [**11.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)

From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115), it's possible to limit the size of created disk temporary files and tables.\
When the internal in-memory temporary table is oversize and converting to MyISAM/Aria table to store on disk, this option will limit the max space of tmp\_dir. If a new disk temporary table will cause tmp\_dir over the limitation, then this query will return an error.

## Temporary Space

The temporary space includes:

* All SQL level temporary files. This includes files for filesort, transaction temporary space, analyze, binlog\_stmt\_cache etc. It does not include engine internal temporary files used for repair, alter table, index pre sorting etc.
* All internal on disk temporary tables created as part of resolving a SELECT, multi-source update etc.

## Special Cases

* When doing a commit, the last flush of the binlog\_stmt\_cache will not cause an error even if the temporary space limit is exceeded. This is to avoid giving errors on commit. This means that a user can temporary go over the limit with up to [binlog\_stmt\_cache\_size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_stmt_cache_size).

## System Variables

There are two system variables used for controlling this feature:

* [max\_tmp\_session\_space\_usage](max_tmp_session_space_usage-system-variable.md): Limits the temporary space allowance per user
* [max\_tmp\_total\_space\_usage](max_tmp_total_space_usage-system-variable.md): Limits the temporary space allowance for all users.

## Status Variables

* [tmp\_space\_used](../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#tmp_space_used)
* [max\_tmp\_space\_used](../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#max_tmp_space_used)

## Information Schema

* New field in [information\_schema.process\_list](../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md): TMP\_SPACE\_USED

## Noteworthy issue

* One has to be careful when using small values for max\_tmp\_space limit together with [binary logging](../../server-management/server-monitoring-logs/binary-log/) and with non transactional tables.
* If a binary log entry for the query is larger than [binlog\_stmt\_cache\_size](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_stmt_cache_size) and one hits the limit of max\_tmp\_space when flushing the entry to disk, the query will abort and the binary log will not contain the last changes to the table. This will also stop the replica!
* This is also true for all Aria tables as Aria cannot do rollback (except in case of crashes)!
* One way to avoid it is to use [@@binlog\_format=statement](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) for queries that update many lot of rows.

## Implementation

* All writes to temporary files or internal temporary tables, that increase the file size, are routed through temp\_file\_size\_cb\_func() which updates and checks the temp space usage.
* Most of the temporary file monitoring is done inside IO\_CACHE. Temporary file monitoring is done inside the Aria engine.
* MY\_TRACK and MY\_TRACK\_WITH\_LIMIT are new flags for ini\_io\_cache(). MY\_TRACK means that we track the file usage. TRACK\_WITH\_LIMIT means that we track the file usage and we give an error if the limit is breached. This is used to not give an error on commit when binlog\_stmt\_cache is flushed.
* global\_tmp\_space\_used contains the total tmp space used so far. This is needed quickly check against max\_total\_tmp\_space\_usage.
* Temporary space errors are using EE\_LOCAL\_TMP\_SPACE\_FULL and handler errors are using HA\_ERR\_LOCAL\_TMP\_SPACE\_FULL. This is needed until we move general errors to it's own error space so that they cannot conflict with system error numbers.
* Return value of my\_chsize() and mysql\_file\_chsize() has changed so that -1 is returned in the case my\_chsize() could not decrease the file size (very unlikely and will not happen on modern systems). All calls to \_chsize() are updated to check for > 0 as the error condition.
* At the destruction of THD we check that THD::tmp\_file\_space == 0
* At server end we check that global\_tmp\_space\_used == 0
* As a precaution against errors in the tmp\_space\_used code, one can set max\_tmp\_space\_usage and max\_total\_tmp\_space\_usage to 0 to disable the tmp space quota errors.
* truncate\_io\_cache() function added.
* Aria tables using static or dynamic row length are registered in 8K increments to avoid some calls to update\_tmp\_file\_size().

## See Also

* [MDEV-9101](https://jira.mariadb.org/browse/MDEV-9101) - Limit size of created disk temporary files and tables

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
