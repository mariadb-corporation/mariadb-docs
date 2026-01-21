# Using mariadb-binlog

{% hint style="info" %}
Previously, the client was called `mysqlbinlog`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows. 
{% endhint %}

## Overview

The MariaDB server's [binary log](../../../server-management/server-monitoring-logs/binary-log/) is a set of files containing "events" which represent modifications to the contents of a MariaDB database.

Events are written in a binary (that is, non-human-readable) format. The `mariadb-binlog` utility is used to view these events in plain text.

Run [mariadb-binlog](./) from a command line:

```bash
mariadb-binlog [options] binlog-filename [binlog-filename ...]
```

See [mariadb-binlog Options](mariadb-binlog-options.md) for details on the available options.

## Usage

Display the contents of a [binary log](../../../server-management/server-monitoring-logs/binary-log/) file named `mariadb-bin.000152` like this:

```bash
mariadb-binlog mariadb-bin.000152
```

### Processing a Single Log File

The logging format is determined by the value of the [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) system variable. If you are using statement-based logging, the output includes the SQL statement, the ID of the server the statement was executed on, a timestamp, and how much time the statement took to execute. If you are using row-based logging, the output of an event will not include an SQL statement, but will instead output how individual rows were changed.

The output from `mariadb-binlog` can be used as input to the `mariadb` client to redo the statements contained in a [binary log](../../../server-management/server-monitoring-logs/binary-log/). This is useful for recovering after a server crash (replace _binlog-filename_ with the name of a binary log file):

```bash
mariadb-binlog binlog-filename | mysql -u root -p
```

If you would like to view and possibly edit the file before applying it to your database, use the `-r` flag to redirect the output to a file (replace _outputfile_ with the name of a file to store the output, and _binlog-filename_ with the name of a binary log file):

```bash
mariadb-binlog -r outputfile binlog-filename
```

In the output file, delete any statements you don't want executed (such as an accidental `DROP DATABASE`). Once you are satisfied with the contents, you can execute it:

```bash
mariadb -u root -p --binary-mode < outputfilename
```

Be careful to process multiple log files in a single connection, especially if one or more of them have any `CREATE TEMPORARY TABLE ...` statements. Temporary tables are dropped when the mariadb client terminates, so if you are processing multiple log files one at a time (i.e. multiple connections), and one log file creates a temporary table and then a subsequent log file refers to the table, you get an 'unknown table' error.

### Processing Multiple Log Files

To execute multiple log files using a single connection, list them all on the `mariadb-binlog` command line:

```bash
mariadb-binlog mariadb-bin.000001 mariadb-bin.000002 | mariadb -u root -p --binary-mode
```

If you need to manually edit the binlogs before executing them, combine them all into a single file before processing:

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
