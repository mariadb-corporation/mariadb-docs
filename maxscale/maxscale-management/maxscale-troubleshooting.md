---
description: >-
  Troubleshoot MariaDB MaxScale issues effectively. This section provides common
  problems, diagnostic steps, and solutions to help you maintain a stable and
  high-performing database proxy.
---

# MaxScale Troubleshooting

## SystemD Watchdog Kills MaxScale

This can occur if a reverse DNS name lookup takes a long time. To disable reverse name lookups of client IPs to client hostnames, add skip\_name\_resolve=true under the `[maxscale]` section.

## High Memory Usage

**MaxScale starting with 22.08.4**

The default value of writeq\_high\_water was lowered to 64KiB to reduce excessive memory usage. This change should result in a net decrease in memory usage and possibly a small improvement in performance.

Set writeq\_high\_water and writeq\_low\_water to lower values, for example `writeq_high_water=512` and `writeq_low_water=128`. The default is to buffer a maximum of 16MB in memory before network throttling begins which under intensive loads can result in a large amount of memory being used per client.

The query classifier cache in MaxScale by default takes up to 15% of memory to cache query classification data. This value can be lowered using the query\_classifier\_cache\_size parameter.

The retain\_last\_statements and session\_trace debugging parameters can cause memory usage to increase. Disabling them under intensive loads is recommended if they are not needed. Note that the `maxctrl list queries` requires that `retain_last_statements=1` is set.

### Profiling Memory Usage

Profiling the memory usage can be useful for finding out why MaxScale appears to use more memory than it should. It is especially helpful for analyzing OOM situations or other cases where the memory grows linearly and causes problems.

To profile the memory usage of MaxScale, there are multiple options. The following sections describe the methods that are available.

If a problem in memory usage is identified and it appears to be due to a bug in MaxScale, please open a new bug report on the [MariaDB Jira under the MaxScale project](https://jira.mariadb.org/browse/MXS). Remember to include all the profiling and leak check reports along with the MaxScale version number and the configuration file with all password and other sensitive information removed.

#### Debug Binaries

The easiest option is to install the MaxScale debug binaries which are built with [AddressSanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer) and [LeakSanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizerLeakSanitizer) enabled. These are low-impact instrumentation tools that detect memory access errors as well as memory leaks.

Once installed, make sure that the `maxlog` parameter is not disabled and then start MaxScale. Let it run until the memory usage grows beyond normal limits and then shut MaxScale down with `systemctl stop maxscale.service`. The MaxScale log should contain a verbose explanation of where memory leaks occurred, if any were found.

#### Profiling Release Mode Binaries

The instructions on the [profiling-memory-usage](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/company-and-community/bug-tracking/profiling-memory-usage) page that are for the MariaDB server also apply to MaxScale. The following modifications to the commands must be done in order for them to work with MaxScale.

* Replace `/usr/sbin/mariadbd` with `/usr/bin/maxscale`
* Replace `/var/lib/mysql/` with `/var/log/maxscale/`
* Replace `pidof mariadbd` with `pidof maxscale`
* Replace `mariadb.service` with `maxscale.service`

#### Valgrind

Valgrind can be used to analyze memory usage problems but usually it is left as the last resort due to the heavy performance penalty that it incurs. However, the use of Valgrind is simple as it is widely available and can be used with existing MaxScale binaries.

To use `valgrind` for memory leak detection, edit the systemd service file with `systemctl edit maxscale.service` and add the following values to it:

```
[Service]
ExecStart=valgrind --leak-check=full /usr/bin/maxscale -d
Type=simple
```

Then restart the MaxScale process with `systemctl restart maxscale.service`. Once the memory problem is confirmed, stop the MaxScale process with `systemctl stop maxscale.service`. Valgrind will print the leak report into the system journal that can be viewed with `journalctl -u maxscale`.

## Authentication Errors

### `Access Denied`

If you are receiving authentication errors like this:

```
ERROR 1045 (28000): Access denied for user 'bob'@'office' (using password: YES)
```

Make sure you create users for both `'bob'@'office'` and `'bob'@'maxscale'`. The host `'office'` is where the client is attempting to connect from and `'maxscale'` is the host where MaxScale is installed.

If you do not want to create a second set of users, you can enable proxy\_protocol in MaxScale and configure the MariaDB server to [allow proxied connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#proxy_protocol_networks) from the MaxScale host.

#### Verifying that a user is allowed to connect

* MaxScale connection
  1. SSH to the server where MaxScale is installed
  2. Connect to MariaDB
  3. Check output of [SHOW GRANTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-grants)
* Client connection
  1. SSH to theserver where client is connecting from
  2. Connect to MariaDB
  3. Check output of [SHOW GRANTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-grants)

#### Checking MaxScale has correct grants

**Service Grants**

Make sure that the MaxScale services have a user configured and that it has the correct grants. Refer to the MariaDB protocol documentation on what grants are required for services.

**Monitor Grants**

The monitor user requires different grants than the service user and each monitor type requires different grants.

* Asynchronous MariaDB replication with mariadbmon
* Galera clusters with galeramon
* Xpand replication

### Other Errors

For all authentication and permission related errors, add `debug=enable-statement-logging` under the `[maxscale]` section of your MaxScale configuration file. This will cause all SQL statements to be logged on the notice level which will help you figure out what the problem is.

### Access denied errors for user root!

If you want to connect as root, you'll need to add [enable\_root\_user=true](https://mariadb.com/kb/en/mariadb-maxscale-2208-mariadb-maxscale-configuration-guide/#enable_root_user) to the service.

### Access denied on databases/tables containing underscores

There seems to be a bug for databases containing underscores. Connect as root and use "SHOW GRANTS FOR user".

GRANT SELECT ON `my\_database`.\* TO 'user'@'%' <-- bad

GRANT SELECT ON `my_database`.\* TO 'user'@'%' <-- good

If you got a grant containing a escaped underscore, you can add the strip\_db\_esc=true parameter to the service to automatically strip escape characters or just replace the grant with a unescaped one.

## System Errors

### `Failed to write message: 11, Resource temporarily unavailable`

**MaxScale starting with 22.08.0**

MaxScale 22.08 no longer uses pipes for internal communication. This means that this error is never logged and the pipe size no longer needs to be adjusted.

**MaxScale starting with 6.4.5**

Older MaxScale versions suffer from a bug ([MXS-4474](https://jira.mariadb.org/browse/MXS-4474)) that caused messages in the queue to take up 4096 bytes of memory per message instead of the intended 24 bytes which translates to a maximum of 256 messages instead of the expected 43690 messages with a 1MiB pipe size.
Starting with MaxScale 6.4.5 and 2.5.25, the size is 24 bytes as expected which causes the maximum limit to be the expected 43690 messages. The problem still theoretically exists under extreme workloads where there are more than 43k concurrent clients but in practice the problem should almost never occur.

The MaxScale can log the `Failed to write message: 11, Resource temporarily unavailable` message under extremely intensive workloads (see [MXS-1983](https://jira.mariadb.org/browse/MXS-1983) and [MXS-4474](https://jira.mariadb.org/browse/MXS-4474)).

The first action to take when these messages are encountered is to upgrade your MaxScale installation to the latest version. Whenever this message is seen, it means that something is causing the internal message queue in MaxScale to fill up. More often than not it is a sign of a possible bug in MaxScale and most likely has been fixed in the most recent release of MaxScale.

If this is still seen even after upgrading to the latest release, the pipe buffer size can be increased from the default 1MB to a higher value to prevent the problem from occurring. At least 8MB is recommended and should be increased until the message stops appearing.

To set the pipe buffer size, execute the following command.

```
sudo sysctl -w fs.pipe-max-size=8388608
```

If after all these actions you still see these warnings, please open a bug report on the MariaDB Jira under the MaxScale project.

### Error 23: Too many open files

This is a common error when system limits for open files is too low. The fix to this is to increase the limits.

#### Systemd

Edit or add `LimitNOFILE=<number of files>` under the `[Service]` section in `/usr/lib/systemd/system/maxscale.service`.

## MaxCtrl

### `Error: ENOENT: no such file or directory, uv_cwd`

If MaxCtrl fails to start and throws the following error, it means that the current working directory no longer exists. Moving into a directory that does exist fixes the problem.

```
pkg/prelude/bootstrap.js:1872
      throw error;
      ^

Error: ENOENT: no such file or directory, uv_cwd
1) If you want to compile the package/file into executable, please pay attention to compilation warnings and specify a literal in 'require' call. 2) If you don't want to compile the package/file into executable and want to 'require' it from filesystem (likely plugin), specify an absolute path in 'require' call using process.cwd() or process.execPath.
    at Object.wrappedCwd [as cwd] (internal/bootstrap/switches/does_own_process_state.js:130:28)
    at /snapshot/maxctrl/node_modules/yargs/build/index.cjs:1:59463
    at Argv (/snapshot/maxctrl/node_modules/yargs/index.cjs:12:16)
    at Object.<anonymous> (/snapshot/maxctrl/node_modules/yargs/index.cjs:7:1)
    at Module._compile (pkg/prelude/bootstrap.js:1926:22)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1114:10)
    at Module.load (internal/modules/cjs/loader.js:950:32)
    at Function.Module._load (internal/modules/cjs/loader.js:790:12)
    at Module.require (internal/modules/cjs/loader.js:974:19)
    at Module.require (pkg/prelude/bootstrap.js:1851:31) {
  errno: -2,
  code: 'ENOENT',
  syscall: 'uv_cwd',
  pkg: true
}
```

### `Pkg: Error reading from file.`

If MaxCtrl fails to start and throws this error, it most likely means that the `maxctrl` executable has been stripped of symbols. To fix this problem, reinstall the MaxScale package.

## Binlogrouter

### Commands not Working

Make sure you are connecting on the port where the binlogrouter is listening. A common mistake is to connect to a readwritesplit or readconnroute port and execute the replication configuration commands there.

## MaxScale CDC: Avrorouter

For most problems, resetting the conversion state is the solution. If the conversion repeatedly stops at a certain point, please [open a bug report](https://jira.mariadb.org/browse/MXS).

### Resetting conversion state

* Stop MaxScale
* Remove the `avro.index` and `avro-conversion.ini` files along with any generated `.avro` files from the director where the Avro files are stored
* Start MaxScale

### Binlog files are not found

Make sure the `start_index` parameter is set to the lowest binlog file number. For example, to start from `mariadb-bin-000005`, set `start_index=5`.

### Access denied to CDC interface

Create the user with `maxadmin call command cdc add_user <service name> <user> <password>` or `maxctrl call command cdc add_user <service name> <user> <password>`.

## Coredumps Are Not Being Generated

Check that `sysctl kernel.core_pattern` is set to forward coredupms to systemd-coredump:

```
sysctl -w kernel.core_pattern='|/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %e'
```

Also make sure that SystemD is configured to allow coredumps. In External images are disabled suitable size limits must be set as they are set to zero by default.

```
$ cat /etc/systemd/coredump.conf
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.
#
# Entries in this file show the compile time defaults.
# You can change settings by editing this file.
# Defaults can be restored by simply deleting this file.
#
# See coredump.conf(5) for details.

[Coredump]
Storage=external
Compress=yes
ProcessSizeMax=1G
ExternalSizeMax=1G
JournalSizeMax=1G
#MaxUse=
#KeepFree=
```

Read the MariaDB documentation for [enabling-core-dumps](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/enabling-core-dumps) and [how-to-produce-a-full-stack-trace-for-mysqld](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/how-to-produce-a-full-stack-trace-for-mariadbd). Most of the operating system level documentation applies to MaxScale as well except that MaxScale is always run as a SystemD service and it only supports Linux as the platform.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
