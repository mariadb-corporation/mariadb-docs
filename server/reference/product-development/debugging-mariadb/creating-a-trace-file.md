---
description: >-
  Details the process of generating a trace file to record the internal
  execution flow of the server for developer analysis.
---

# Creating a Trace File

{% include "../../../.gitbook/includes/hint-lower-level-development.md" %}

If `mysqld` is crashing, creating a trace file is a good way to find the issue.

A `mysqld` binary that has been compiled with debugging support can create trace files using the DBUG package created by Fred Fish. To find out if your `mysqld` binary has debugging support, run `mysqld -V` on the command line. If the version number ends in `-debug` then your `mysqld` binary was compiled with debugging support.

See [Compiling MariaDB for debugging](compiling-mariadb-for-debugging.md) for instructions on how to create your own `mysqld` binary with debugging enabled.

To create the trace log, start `mysqld` like so:

```
mysqld --debug
```

Without options for --debug, the trace file will be named `/tmp/mysqld.trace` in MySQL and older versions of MariaDB before 10.5 and `/tmp/mariadbd.trace` starting from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105).

On Windows, the debug `mysqld` is called `mysqld-debug` and you should also use the `--standalone` option. So the command on Windows will look like:

```
mysqld-debug --debug --standalone
```

Once the server is started, use the regular `mysql` command-line client (or another client) to connect and work with the server.

After you are finished debugging, stop the server with:

```
mysqladmin shutdown
```

## DBUG Options

Trace files can grow to a significant size. You can reduce their size by telling the server to only log certain items.

The `--debug` flag can take extra options in the form of a colon (:) delimited string of options. Individual options can have comma-separated sub-options.

For example:

```
mysqld --debug=d,info,error,query:o,/tmp/mariadbd.trace
```

The '`d`' option limits the output to the named DBUG\_ macros. In the above example, the `/tmp/mariadbd.trace` tracefile will contain output from the info, error, and query DBUG macros. A '`d`' by itself (with no sub-options) will select all DBUG\_ macros.

The '`o`' option redirects the output to a file (`/tmp/mariadbd.trace` in the example above) and overwrites the file if it exists.

## See Also

* [Options for --debug](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_debug)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
