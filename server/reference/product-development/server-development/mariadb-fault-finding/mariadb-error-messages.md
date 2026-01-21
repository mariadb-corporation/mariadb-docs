---
description: >-
  Explains how to interpret server error codes and messages to quickly identify
  configuration or runtime failures.
---

# MariaDB Error Messages

{% include "../../../../.gitbook/includes/hint-system-level-debugging.md" %}

MariaDB has a number of error messages. If the meaning is not clear, use the following table to guide you to the desired actions.

## Can't lock aria control file, error 11

`[ERROR] mysqld: Can't lock aria control file '/var/lib/mysql/aria_log_control' for exclusive use, error: 11. Will retry for 30 seconds`

The `perror 11` is 'Resource temporarily unavailable'. This is an indication that an operating system lock couldn't be obtained on the ariia\_log\_control file. This is a strong indication that an existing MariaDB server is already running on the datadir.

Look at the operating system process list. Identify if the existing mysqld/mariadbd process is shutting down (look at the logs, and if its listening to new connections). MariaDB will stop accepting new SQL connections immediately once the shutdown starts.

If its shutting down, its best to let it continue. Force killing off the process will cause a crash recovery on the next restart. If you are about to upgrade there is a possibility your next upgraded version will not complete the crash recovery and you will need the current version to complete the log recovery.

If it completing the shutdown, take two \[how-to-produce-a-full-stack-trace-for-mysqld/#getting-full-backtraces-for-all-threads-from-a-running-mariadbd-process|backtraces] with 30 seconds to a minute between them.

## Can't create/write/read to file .... .. Errcode X

`[ERROR] mariadbd: Can't create/write to file '/var/run/mariadb/mariadb.pid' (Errcode: 2 "No such file or directory")`.

The errcode can be look up with `[perror](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/perror) X` to return a text description of the code if not already there. In may cases there are directly the same as operating system errors. Common ones are:

* Error 2 - No such file or directory. MariaDB is expecting to read/write/create a file somewhere and it doesn't exist. If creating, the directory doesn't exist.
* Error 13 - EPERM, permission denied. Either file permissions or an access control mechanism like selinux or apparmor or systemd is preventing access to this location. Alternately you are running MariaDB as the incorrect user for the data it is trying to access.
* Error 28 - ENOSPC - no space left on device. The filesytem where writing is occurring is full and cannot fit any more data.

## \[ERROR] InnoDB: Invalid flags 0x4800 in ./ibdata1

This indicates that MariaDB is starting on a MySQL-8.0 data directory. Other flags are possible if a different page size or different features (see [MDEV-27882](https://jira.mariadb.org/browse/MDEV-27882)).

MariaDB cannot startup on MySQL-8.0 data directory. MySQL should be run on the MySQL data directory and if the objective is to migrate, take logical dumps from MySQL before recreating a MariaDB database, prehaps in a different location, or after the MySQL data directory has been moved.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
