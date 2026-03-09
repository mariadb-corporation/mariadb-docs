---
description: >-
  Provides specialized guidance on identifying the causes of server crashes and
  gathering the necessary data for reporting bugs.
---

# MariaDB Crashes

{% include "../../../../.gitbook/includes/hint-system-level-debugging.md" %}

There are a number of causes of MariaDB crashes. Most of these are MariaDB encountering a situation where it cannot safely proceed. Crashes on Linux/Unix systems are fatal signals. On Windows these are similar looking exceptions.

## InnoDB Semaphore wait

These are indicated by the following text in the error log:

```
[ERROR] [FATAL] InnoDB: Semaphore wait has lasted > 600 seconds. We intentionally crash the server because it appears to be hung.
```

For this its essential that a full backtrace of \[how-to-produce-a-full-stack-trace-for-mysqld/#getting-full-backtraces-for-all-threads-from-a-running-mariadbd-process|all the running threads].

## Assertions

These look like `[ERROR] mariadbd got signal 6`. There might be associated text in the error log like:

```
InnoDB: Assertion failure in file ./storage/innobase/os/os0file.cc line 3540
InnoDB: Failing assertion: cb->m_err == DB_SUCCESS
```

On OSX it might show up as `Exception Type: EXC_CRASH (SIGABRT)`.

There maybe a stack trace, and perhaps a user SQL query (depending on the location). These are usually program errors that MariaDB got into a state where the developers did not expect to happen. Occasionally like the above, there are operating system factors that the developers haven't written handling routines for. In all cases this should be reported as a bug.

## SEGV / Segment Violation

A SEGV, or Segment Violation, is an operating system concept in this case MariaDB accessing a location in memory it doesn't own. It will occur in the logs like:

`[ERROR] mysqld got signal 11 ;`

A full stack trace from the \[how-to-produce-a-full-stack-trace-for-mysqld/#analyzing-a-core-file-with-gdb-on-linux|core file generated] is needed to resolve this form of error.

If there is a SQL query in the log file, include this in the bug report, along with `EXPLAIN query` and `SHOW CREATE TABLE tblname` for tables involved to enable a test case for this crash.

## SIGBUS

This occurs when the alignment of memory doesn't correspond to the code accessing it.

`[ERROR] mysqld got signal 7`

Threat like SEGV.

## SIGILL / Illegal Instruction

This indicates the MariaDB you have has been compiled for a CPU hardware feature that isn't available.

One cause is distributions occasionally target a minimum CPU version and if you are running on an earlier version it will crash in this way.

MariaDB does use optimizations in a number of critical paths under feature detection. Its possible that these aren't comprehensive for you your hardware. Very precise reporting of the hardware CPU model is required when reporting these bugs.

## SIGKILL

This is an indicator that a user or OS killed of MariaDB. User invoked `SIGKILL` termination can be indirect using `podman kill {container}`.

The OS will kill MariaDB in an out of memory scenario in an attempt to regain memory. As MariaDB is a big memory user its usually fairly high on the list of processes killed by the OS.

If MariaDB is shutting down, it might be possible under some service manager that if it takes too long, it will get a SIGKILL. The default MariaDB systemd service has `SendSIGKILL=No`.

Galera SST scripts also have a `kill -9` in them.

Generally the SIGKILL won't be a bug, however the slow time that resulted in a service manager taking this drastic step might be.

## Hardware faults

This can be disk corruption where MariaDB reads data and that data wasn't what was written. This will result in MariaDB doing unexpected things, including potentially accessing unallocated memory.

RAM corruptions can also result in undefined behaviour that is unfixable with software.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
