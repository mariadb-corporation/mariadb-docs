---
description: >-
  Describes the API and mechanisms that allow client applications to receive
  real-time progress updates for long-running server-side operations.
---

# Progress Reporting

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

MariaDB supports progress reporting for some long running commands.

## What is Progress Reporting?

Progress reporting means that:

* There is a `Progress` column
  in [SHOW PROCESSLIST](../../../sql-statements/administrative-sql-statements/show/show-processlist.md) which shows the total progress\
  (0-100%)
* [INFORMATION\_SCHEMA.PROCESSLIST](../../../system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) has three columns which allow you to see in which process stage we are and how much of that stage is completed:
  * `STAGE`
  * `MAX_STAGE`
  * `PROGRESS` (within current stage).
* The client receives progress messages which it can display to the user to
  indicate how long the command will take.

We have separate progress reporting for stages because different stages take
different amounts of time.

## Supported Commands

The following commands can send progress report messages to the
client:

* [ALTER TABLE](../../../sql-statements/data-definition/alter/alter-table/)
* [CREATE INDEX](../../../sql-statements/data-definition/create/create-index.md)
* [DROP INDEX](../../../sql-statements/data-definition/drop/drop-index.md)
* [LOAD DATA INFILE](../../../sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) (not `LOAD DATA LOCAL INFILE`, as in that case we
  don't know the size of the file).

Some Aria storage engine operations also support progress messages:

* [CHECK TABLE](../../../sql-statements/table-statements/check-table.md)
* [REPAIR TABLE](../../../sql-statements/table-statements/repair-table.md)
* [ANALYZE TABLE](../../../sql-statements/table-statements/analyze-table.md)
* [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md)

### Limitations

Although the above commands support progress reporting, there are some limitations to what progress is reported.

Client progress messages are sent while a table is being copied, as in `ALTER TABLE` with `ALGORITHM=COPY`. An InnoDB operation that uses [ALGORITHM=INPLACE](../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md) (the default where InnoDB supports it) does not send them. In that case, the `mariadb` client shows no `Stage:` line, and `SHOW PROCESSLIST` reports no progress.

{% hint style="info" %}
Before MDEV-29913, InnoDB reported client progress for one step of an in-place operation, the merge sort phase while it built indexes. That report was removed in 10.4.33, 10.5.24, 10.6.17, 10.11.7, 11.0.5, 11.1.4, and 11.2.3, so it is also absent from 11.4 and later.
{% endhint %}

InnoDB reports the progress of an in-place operation through the [Performance Schema](../../../system-tables/performance-schema/performance-schema-overview.md) instead. Each phase is a stage event, such as `stage/innodb/alter table (read PK and internal sort)` and `stage/innodb/alter table (merge sort)`. To follow one, make sure the stage instruments and the `events_stages_current` consumer are enabled, then query [events\_stages\_current](../../../system-tables/performance-schema/performance-schema-tables/performance-schema-events_stages_current-table.md) from another connection. Compare `WORK_COMPLETED` with `WORK_ESTIMATED` to see how far the current stage has got:

```sql
SELECT EVENT_NAME, WORK_COMPLETED, WORK_ESTIMATED
  FROM performance_schema.events_stages_current
 WHERE EVENT_NAME LIKE 'stage/innodb/alter table%';
```

## Enabling and Disabling Progress Reporting

`mysqld` (the MariaDB server) automatically sends progress report messages to clients that support the new protocol, using the value of the [progress\_report\_time](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#progress_report_time) variable. They are sent every
max(`global.progress_report_time` , `progress_report_time`) seconds (by default 5). You can disable the sending of progress report messages to the client by setting either the local variable (affects only the current connection) or the global variable (affects all connections) to `0`.

If the extra column in `SHOW PROCESSLIST` gives you a compatibility problem,
you can disable it by starting `mysqld` with the `--old` flag.

## Clients Which Support Progress Reporting

* The [mariadb command line client](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md)
* The `mytop` that comes with MariaDB has a `'%'` column which shows
  the progress.

## Progress Reporting in the mysql Command Line Client

Progress reporting is enabled by default in the [mariadb client](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md). You can
disable it with `--disable-progress-reports`. It is automatically disabled in
batch mode.

When enabled, for every supported command you get a progress report like:

```
ALTER TABLE my_mail ENGINE=aria;
Stage: 1 of 2 'copy to tmp table'  5.37% of stage done
```

This is updated every [progress\_report\_time](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#progress_report_time) seconds (the default is 5). If the global `progress_report_time` is higher, this will be used. You can also disable error reporting by setting the variable to `0`.

## How to Add Support for Progress Reporting to a Client

You need to use a MariaDB client library. You can check that the library
supports progress reporting by doing:

```
#ifdef CLIENT_PROGRESS
```

To enable progress reporting to the client you need to add`CLIENT_PROGRESS` to the `connect_flag` in `mysql_real_connect()`:

```
mysql_real_connect(mysql, host, user, password,
                   database, opt_mysql_port, opt_mysql_unix_port,
                   connect_flag | CLIENT_PROGRESS);
```

Then you need to provide a callback function for progress reports:

```
static void report_progress(const MYSQL *mysql, uint stage, uint max_stage,
                            double progress, const char *proc_info,
                            uint proc_info_length);

mysql_options(&mysql, MYSQL_PROGRESS_CALLBACK, (void*) report_progress);
```

The above `report_progress` function will be called for each
progress message.

This is the implementation used by `mysql.cc`:

```
uint last_progress_report_length;

static void report_progress(const MYSQL *mysql, uint stage, uint max_stage,
                            double progress, const char *proc_info,
                            uint proc_info_length)
{
  uint length= printf("Stage: %d of %d '%.*s' %6.3g%% of stage done",
                      stage, max_stage, proc_info_length, proc_info, 
                      progress);
  if (length < last_progress_report_length)
    printf("%*s", last_progress_report_length - length, "");
  putc('\r', stdout);
  fflush(stdout);
  last_progress_report_length= length;
}
```

If you want only one number for the total progress, you can calculate it with:

```
double total_progress=
 ((stage -1) / (double) max_stage * 100.00 + progress / max_stage);
```

**Note:** `proc_info` is totally independent of stage. You can have many
different `proc_info` values within a stage. The idea behind `proc_info` is
to give the user more information about what the server is doing.

## How to Add Support for Progress Reporting to a Storage Engine

The functions to use for progress reporting are:

```
void thd_progress_init(MYSQL_THD thd, unsigned int max_stage);
```

Initialize progress reporting with stages. This is mainly used for
commands that are totally executed within the engine, like `CHECK TABLE`.\
You should not use this for operations that could be called by, for example,`ALTER TABLE` as this has already called the function.

`max_stage` is the number of stages your storage engine will have.

```
void thd_progress_report(MYSQL_THD thd, unsigned long long progress,
                         unsigned long long max_progress);
```

The above is used for reporting progress.

* `progress` is how much of the file/rows/keys you have gone through.
* `max_progress` is the max number of rows you will go through.

You can call this with varying numbers, but normally the ratio`progress/max_progress` should be increasing.

This function can be called even if you are not using stages, for example when
enabling keys as part of `ALTER TABLE` or `ADD INDEX`.

```
void thd_progress_next_stage(MYSQL_THD thd);
```

To go to the next stage in a multi-stage process initiated by`thd_progress_init()`:

```
void thd_progress_end(MYSQL_THD thd);
```

End progress reporting; Sets 'Progress' back to 0 in `SHOW PROCESSLIST`.

```
const char *thd_proc_info(thd, 'stage name');
```

This sets the name of the current status/stage that is displayed in`SHOW PROCESSLIST` and in the client. It's recommended that you call
this between stages and thus before `thd_progress_report()` and`thd_progress_next_stage()`.

This functions returns the last used `proc_info`. It's recommended that
you restore `proc_info` to its original value when you are done
processing.

**Note:** `thd_proc_info()` is totally independent of stage. You can have
many different `proc_info` values within a stage to give the user more
information about what is going on.

## Examples to Look at in the MariaDB Source:

* `client/mysql.cc` for an example of how to use reporting.
* `libmysql/client.c:cli_safe_read()` to see how progress packets are handled
  in client
* `sql/protocol.cc::net_send_progress_packet()` for how progress packets are
  handled in server.

## Format of Progress Packets

The progress packet is sent as an error packet with error number `65535`.

It contains the following data (in addition to the error header):

| Option         | Number of bytes | Other info                                             |
| -------------- | --------------- | ------------------------------------------------------ |
| 1              | 1               | Number of strings. For future                          |
| Stage          | 1               | Stage from 1 - Max\_stage                              |
| Max\_stage     | 1               | Max number of stages                                   |
| Progress       | 3               | Progress in % \* 1000                                  |
| Status\_length | 1-2             | Packet length of string in net\_field\_length() format |
| Status         | Status\_length  | Status / Stage name                                    |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
