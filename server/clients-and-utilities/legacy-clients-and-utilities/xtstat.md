# xtstat

{% hint style="warning" %}
This tool is for PBXT, an unsupported storage engine.
{% endhint %}

`xtstat` can be used to monitor all internal activity of PBXT (a storage engine that is no longer supported).

`xtstat` polls the `INFORMATION_SCHEMA.PBXT_STATISTICS` table. The poll interval can be set using the `--delay` option, and is 1 second by default.

For most statistics, `xtstat` will display the difference in values between the current and previous polls. For example, if bytes written current value is 1000, and on the previous call it was 800, then `xtstat` will display 200. This means that 200 bytes were written to disk in the intervening period.

## Using `xtstat`

Invoke xtstat as follows:

```bash
$ xtstat [ options ]
```

For example, to poll every 10 seconds:

```bash
xtstat -D10
```

Note that statistic counters are never reset, even if a rollback occurs. For example, if an `UPDATE` statement is rolled back, `xtstat` will still indicate that one write statement (see stat-write below) was executed.

If MariaDB shuts down or crashes, `xtstat` will attempt to reconnect. `xtstat` can be terminated any time using the `CTRL-C` key cimbination.

Before PBXT has recovered, not all statistics are available. In particular, the statistics relating to PBXT background threads are not available (including the `sweep` and `chkpnt` statistics).

### Command line options

`xtstat` options are as follows:

| Option                  | Description                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------- |
| -?, --help              | Prints help text.                                                                            |
| -h, --host=value        | Connect to host.                                                                             |
| -u, --user=value        | User for login if not current user.                                                          |
| -p, --password\[=value] | Password to use when connecting to server. If password is not given it's asked from the tty. |
| -d, --database=value    | Database to be used (pbxt or information\_schema required), default is information\_schema   |
| -P, --port=value        | Port number to use for connection.                                                           |
| -S, --socket=value      | Socket file to use for connection.                                                           |
| -D, --delay=value       | Delay in seconds between polls of the database.                                              |
| --protocol=value        | Connection protocol to use: default/tcp/socket/pipe/memory                                   |
| --display=value         | Columns to display: use short names separated by                                             |

Connection options will also be taken from the MySQL config file if available.

#### Size indicators

Values displayed by `xtstat` are either a time in milliseconds, a value in bytes, or a counter. If these values are too large to be displayed then the value is rounded and a size indicator is added.

The following size indicators are used:

|   |   |                                     |
| - | - | ----------------------------------- |
| K | : | Kilobytes (1,024 bytes)             |
| M | : | Megabytes (1,048,576 bytes)         |
| G | : | Gigabytes (1,073,741,024 bytes)     |
| T | : | Terabytes (1,099,511,627,776 bytes) |
| t | : | thousands (1,000s)                  |
| m | : | millions (1,000,000s)               |
| b | : | billions (1,000,000,000s)           |

### Statistics

The following is a list of the statistics displayed by `xtstat`. Each statistic as a two-part display name. The first part is the category and the second part is the type.

You can select categories and types for display, as you require. For example `--display=read` will display all read activity, `--display=xact|stat` will display transaction and statement activity.

Note, for diagnostics it is best to capture all statistics. The reason is because you never now where a problem might turn up, so without certain statistics you may not be able to identify the problem.

| Display name  | Name                  | Description                                                                                                                                                                                                                                                                                                                       |
| ------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Display name  | Name                  | Description                                                                                                                                                                                                                                                                                                                       |
| time-curr     | Current Time          | The current time in seconds                                                                                                                                                                                                                                                                                                       |
| time-msec     | Time Since Last Call  | Time passed in milliseconds since last statistics call                                                                                                                                                                                                                                                                            |
| xact-commt    | Commit Count          | Number of transactions committed                                                                                                                                                                                                                                                                                                  |
| xact-rollb    | Rollback Count        | Number of transactions rolled back                                                                                                                                                                                                                                                                                                |
| xact-waits    | Wait for Xact Count   | Number of times waited for another transaction                                                                                                                                                                                                                                                                                    |
| xact-dirty    | Dirty Xact Count      | Number of transactions still to be cleaned up. This also includes all the currently running transactions. Cleanup means that the Sweeper thread must still scan the transaction and collect/mark any "garbage" left by the transaction. Garbage is, for example, versions of rows that are no longer visible by any transaction. |
| stat-read     | Read Statements       | Number of SELECT statements                                                                                                                                                                                                                                                                                                       |
| stat-write    | Write Statements      | Number of UPDATE/INSERT/DELETE statements                                                                                                                                                                                                                                                                                         |
| rec-in        | Record Bytes Read     | Bytes read from the record/row files                                                                                                                                                                                                                                                                                              |
| rec-out       | Record Bytes Written  | Bytes written to the record/row files. This data is transferred from the transaction logs to the handle data (xtd) and the row index files (xtr).                                                                                                                                                                                  |
| rec-syncs/ms  | Record File Flushes   | 2 values separated by a '/': the number of flushes to data handle (.xtd) and row index (.xtr) files and the time taken in milliseconds to perform the flush operations.                                                                                                                                                           |
| rec-hits      | Record Cache Hits     | Hits when accessing the record cache. The record cache caches the data handle (.xtd) and row index (.xtr) files.                                                                                                                                                                                                                  |
| rec-miss      | Record Cache Misses   | Misses when accessing the record cache                                                                                                                                                                                                                                                                                            |
| rec-frees     | Record Cache Frees    | Number of record cache pages freed                                                                                                                                                                                                                                                                                                |
| rec-%use      | Record Cache Usage    | Percentage of record cache in use. This value is displayed by xtstat as a percentage of the total cache available, but the value returned by PBXT\_STATISTICS table is in bytes used.                                                                                                                                             |
| ind-in        | Index Bytes Read      | Bytes read from the index files                                                                                                                                                                                                                                                                                                   |
| ind-out       | Index Bytes Written   | Bytes written to the index files. This data is transferred from the index log files (ilog) to the index files (xti), during a consistent flush of the index.                                                                                                                                                                       |
| ind-syncs/ms  | Index File Flushes    | 2 values separated by a '/': the number of flushes to index files and the time taken for the flush operations in milliseconds.                                                                                                                                                                                                    |
| ind-hits      | Index Cache Hits      | Hits when accessing the index cache                                                                                                                                                                                                                                                                                               |
| ind-miss      | Index Cache Misses    | Misses when accessing the index cache                                                                                                                                                                                                                                                                                             |
| ind-%use      | Index Cache Usage     | Percentage of index cache used. This value is displayed by xtstat as a percentage of the total cache available, but the value returned by PBXT\_STATISTICS table is in bytes used.                                                                                                                                                |
| ilog-in       | Index Log Bytes In    | Bytes read from the index log files                                                                                                                                                                                                                                                                                               |
| ilog-out      | Index Log Bytes Out   | Bytes written to the index log files. This data is transferred from the index cache in main memory to the index log files (ilog) during a consistent flush of the index.                                                                                                                                                           |
| ilog-syncs/ms | Index Log File Syncs  | 2 values separated by a '/': the number of flushes to index log files and the time taken for the flush operations in milliseconds                                                                                                                                                                                                 |
| xlog-in       | Xact Log Bytes In     | Bytes read from the transaction log files                                                                                                                                                                                                                                                                                         |
| xlog-out      | Xact Log Bytes Out    | Bytes written to the transaction log files. This is data transferred from the transaction log buffer (pbxt\_transaction\_buffer\_size) to the transaction log files (.xlog). This transfer occurs on commit or when the transaction log buffer is full.                                                                            |
| xlog-syncs    | Xact Log File Syncs   | Number of flushes to transaction log files                                                                                                                                                                                                                                                                                        |
| xlog-msec     | Xact Log Sync Time    | The time in milliseconds to flush transaction log files                                                                                                                                                                                                                                                                           |
| xlog-hits     | Xact Log Cache Hits   | Hits when accessing the transaction log cache                                                                                                                                                                                                                                                                                     |
| xlog-miss     | Xact Log Cache Misses | Misses when accessing the transaction log cache                                                                                                                                                                                                                                                                                   |
| xlog-%use     | Xact Log Cache Usage  | Percentage of transaction log cache used. This value is displayed by xtstat as a percentage of the total cache available, but the value returned by PBXT\_STATISTICS table is in bytes used.                                                                                                                                      |
| data-in       | Data Log Bytes In     | Bytes read from the data log files                                                                                                                                                                                                                                                                                                |
| data-out      | Data Log Bytes Out    | Bytes written to the data log files. This data is transferred from the data log buffer (pbxt\_log\_buffer\_size) to the data log files (.dlog), when the buffer is full, or on commit.                                                                                                                                             |
| data-syncs    | Data Log File Syncs   | Number of flushes to data log files                                                                                                                                                                                                                                                                                               |
| data-msec     | Data Log Sync Time    | The time in milliseconds spent flushing data log files                                                                                                                                                                                                                                                                            |
| to-chkpt      | Bytes to Checkpoint   | Bytes written to the transaction log since the last checkpoint                                                                                                                                                                                                                                                                    |
| to-write      | Log Bytes to Write    | Bytes written to the transaction log, still to be written to the database                                                                                                                                                                                                                                                         |
| to-sweep      | Log Bytes to Sweep    | Bytes written to the transaction log, still to be read by the Sweeper thread                                                                                                                                                                                                                                                      |
| sweep-waits   | Sweeper Wait on Xact  | Attempts to cleanup a transaction                                                                                                                                                                                                                                                                                                 |
| scan-index    | Index Scan Count      | Number of index scans                                                                                                                                                                                                                                                                                                             |
| scan-table    | Table Scan Count      | Number of table scans                                                                                                                                                                                                                                                                                                             |
| row-sel       | Select Row Count      | Number of rows selected                                                                                                                                                                                                                                                                                                           |
| row-ins       | Insert Row Count      | Number of rows inserted                                                                                                                                                                                                                                                                                                           |
| row-upd       | Update Row Count      | Number of rows updated                                                                                                                                                                                                                                                                                                            |
| row-del       | Delete Row Count      | Number of rows deleted                                                                                                                                                                                                                                                                                                            |

## More Information

Documentation on this page is based on the [xtstat documentation](https://primebase.org/documentation/index.php#xtstat) on the PrimeBase website.

Paul McCullagh's presentation from the 2010 User's Conference has some usage examples: [pbxt-uc-2010.pdf](https://www.primebase.org/download/pbxt-uc-2010.pdf)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
