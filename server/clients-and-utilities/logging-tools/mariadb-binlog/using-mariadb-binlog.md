# Using mariadb-binlog

The MariaDB server's [binary log](../../../server-management/server-monitoring-logs/binary-log/) is a set of files containing "events" which represent modifications to the contents of a MariaDB database.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105), the client was called `mysqlbinlog`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.These events are written in a binary (i.e. non-human-readable) format. The _mariadb-binlog_ utility is used to view these events in plain text.

Run [mariadb-binlog](./) from a command line like this:

```bash
mariadb-binlog [options] log_file ...
```

See [mariadb-binlog Options](mariadb-binlog-options.md) for details on the available options.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105), the client was called `mysqlbinlog`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

As an example, here is how you could display the contents of a [binary log](../../../server-management/server-monitoring-logs/binary-log/) file named "mariadb-bin.000152":

```bash
mariadb-binlog mariadb-bin.000152
```

The logging format is determined by the value of the [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) system variable. If you are using statement-based logging, the output includes the SQL statement, the ID of the server the statement was executed on, a timestamp, and how much time the statement took to execute. If you are using row-based logging the output of an event will not include an SQL statement but will instead output how individual rows were changed.

The output from mariadb-binlog can be used as input to the mariadb client to redo the statements contained in a [binary log](../../../server-management/server-monitoring-logs/binary-log/). This is useful for recovering after a server crash. Here is an example:

```bash
mariadb-binlog binlog-filenames | mysql -u root -p
```

If you would like to view and possibly edit the file before applying it to your database, use the '-r' flag to redirect the output to a file:

```bash
mariadb-binlog -r filename binlog-filenames
```

You can then open the file and view it and delete any statements you don't want executed (such as an accidental DROP DATABASE). Once you are satisfied with the contents you can execute it with:

```bash
mariadb -u root -p --binary-mode < filename
```

Be careful to process multiple log files in a single connection, especially if one or more of them have any `CREATE TEMPORARY TABLE ...` statements. Temporary tables are dropped when the mariadb client terminates, so if you are processing multiple log files one at a time (i.e. multiple connections) and one log file creates a temporary table and then a subsequent log file refers to the table you will get an 'unknown table' error.

To execute multiple logfiles using a single connection, list them all on the mariadb-binlog command line:

```bash
mariadb-binlog mariadb-bin.000001 mariadb-bin.000002 | mariadb -u root -p --binary-mode
```

If you need to manually edit the binlogs before executing them, combine them all into a single file before processing. Here is an example:

```bash
mariadb-binlog mariadb-bin.000001 > /tmp/mariadb-bin.sql
mariadb-binlog mariadb-bin.000002 >> /tmp/mariadb-bin.sql
# make any edits
mariadb -u root -p -e "source /tmp/mariadb-bin.sql"
```

## See Also

* [mariadb-binlog](./)
* [mariadb-binlog Options](mariadb-binlog-options.md)

{% include "../../../.gitbook/includes/license-gplv2-fill-help-tables.md" %}

{% @marketo/form formId="4316" %}
