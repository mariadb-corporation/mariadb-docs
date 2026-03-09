---
description: >-
  Steps to generate a complete stack trace for the main server daemon, essential
  for pinpointing the location of software faults.
---

# Producing a Full Stack Trace for mariadbd

{% include "../../../.gitbook/includes/hint-lower-level-development.md" %}

## Partial Stack Traces in the Error Log

When `mariadbd` crashes, it will write a stack trace in the [error log](../../../server-management/server-monitoring-logs/error-log.md) by default. This is because the [stack\_trace](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-stack-trace) option defaults to `ON`. With a normal release build, this stack trace in the [error log](../../../server-management/server-monitoring-logs/error-log.md) may look something like this:

```
2019-03-28 23:31:08 0x7ff4dc62d700  InnoDB: Assertion failure in file /home/buildbot/buildbot/build/mariadb-10.2.23/storage/innobase/rem/rem0rec.cc line 574
InnoDB: We intentionally generate a memory trap.
InnoDB: Submit a detailed bug report to https://jira.mariadb.org/
InnoDB: If you get repeated assertion failures or crashes, even
InnoDB: immediately after the mysqld startup, there may be
InnoDB: corruption in the InnoDB tablespace. Please refer to
InnoDB: https://mariadb.com/kb/en/library/innodb-recovery-modes/
InnoDB: about forcing recovery.
190328 23:31:08 [ERROR] mysqld got signal 6 ;
This could be because you hit a bug. It is also possible that this binary
or one of the libraries it was linked against is corrupt, improperly built,
or misconfigured. This error can also be caused by malfunctioning hardware.
 
To report this bug, see https://mariadb.com/kb/en/reporting-bugs
 
We will try our best to scrape up some info that will hopefully help
diagnose the problem, but since we have already crashed, 
something is definitely wrong and this may fail.
 
Server version: 10.2.23-MariaDB-10.2.23+maria~stretch
key_buffer_size=134217728
read_buffer_size=131072
max_used_connections=234
max_threads=752
thread_count=273
It is possible that mysqld could use up to 
key_buffer_size + (read_buffer_size + sort_buffer_size)*max_threads = 1783435 K  bytes of memory
Hope that's ok; if not, decrease some variables in the equation.
 
Thread pointer: 0x7ff4d8001f28
Attempting backtrace. You can use the following information to find out
where mysqld died. If you see no messages after this, something went
terribly wrong...
stack_bottom = 0x7ff4dc62ccc8 thread_stack 0x49000
*** buffer overflow detected ***: /usr/sbin/mysqld terminated
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x70bfb)[0x7ffa09af5bfb]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x37)[0x7ffa09b7e437]
/lib/x86_64-linux-gnu/libc.so.6(+0xf7570)[0x7ffa09b7c570]
/lib/x86_64-linux-gnu/libc.so.6(+0xf93aa)[0x7ffa09b7e3aa]
/usr/sbin/mysqld(my_addr_resolve+0xe2)[0x55ca42284922]
/usr/sbin/mysqld(my_print_stacktrace+0x1bb)[0x55ca4226b1eb]
/usr/sbin/mysqld(handle_fatal_signal+0x41d)[0x55ca41d0a01d]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x110e0)[0x7ffa0b4180e0]
/lib/x86_64-linux-gnu/libc.so.6(gsignal+0xcf)[0x7ffa09ab7fff]
/lib/x86_64-linux-gnu/libc.so.6(abort+0x16a)[0x7ffa09ab942a]
/usr/sbin/mysqld(+0x40f971)[0x55ca41ab8971]
/usr/sbin/mysqld(+0x887df6)[0x55ca41f30df6]
/usr/sbin/mysqld(+0x863673)[0x55ca41f0c673]
/usr/sbin/mysqld(+0x96648e)[0x55ca4200f48e]
/usr/sbin/mysqld(+0x89b559)[0x55ca41f44559]
/usr/sbin/mysqld(+0x8a15e4)[0x55ca41f4a5e4]
/usr/sbin/mysqld(+0x8a2187)[0x55ca41f4b187]
/usr/sbin/mysqld(+0x8b1a20)[0x55ca41f5aa20]
/usr/sbin/mysqld(+0x7f5c04)[0x55ca41e9ec04]
/usr/sbin/mysqld(_ZN7handler12ha_write_rowEPh+0x107)[0x55ca41d140d7]
/usr/sbin/mysqld(_Z12write_recordP3THDP5TABLEP12st_copy_info+0x72)[0x55ca41b4b992]
/usr/sbin/mysqld(_Z12mysql_insertP3THDP10TABLE_LISTR4ListI4ItemERS3_IS5_ES6_S6_15enum_duplicatesb+0x1206)[0x55ca41b560f6]
/usr/sbin/mysqld(_Z21mysql_execute_commandP3THD+0x3f68)[0x55ca41b6bee8]
/usr/sbin/mysqld(_Z11mysql_parseP3THDPcjP12Parser_statebb+0x28a)[0x55ca41b70e4a]
/usr/sbin/mysqld(+0x4c864f)[0x55ca41b7164f]
/usr/sbin/mysqld(_Z16dispatch_command19enum_server_commandP3THDPcjbb+0x1a7c)[0x55ca41b737fc]
/usr/sbin/mysqld(_Z10do_commandP3THD+0x176)[0x55ca41b748a6]
/usr/sbin/mysqld(_Z24do_handle_one_connectionP7CONNECT+0x25a)[0x55ca41c3ec0a]
/usr/sbin/mysqld(handle_one_connection+0x3d)[0x55ca41c3ed7d]
/usr/sbin/mysqld(+0xb75791)[0x55ca4221e791]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x74a4)[0x7ffa0b40e4a4]
/lib/x86_64-linux-gnu/libc.so.6(clone+0x3f)[0x7ffa09b6dd0f]
```

If you plan to [report a bug](../../community/community/bug-tracking/reporting-bugs.md) about the problem, then this information can be very useful for MariaDB's developers to track down the root cause. However, notice that some of the function names in the call stack are missing. In some cases, this partial stack trace may not be enough to find out exactly where the problem is.

A full stack trace can only be produced if you have debugging symbols for your `mariadbd` binary.

## Obtaining Debugging Symbols for Your mariadbd executable

Debug information is used by debugging tools to produce a meaningful stack trace. Importantly these packages do not replace any executables or any existing production executables or in any way interfere with the way the production server ran before these packages where installed.

If you are obtaining a backtrace for a coredump, you can move the core dump to a difference server that has the identical mariadb-server and debug info packages, and perform the backtrace there with no loss of information.

### Installing Debug Info Packages on Linux

On some Linux distributions, you may be able to install `debuginfo` packages that contain debugging symbols.

Currently, `debuginfo` packages may not allow the server to print a nice stack trace in the error log. They also allow users to extract full stack traces from core dumps. See [MDEV-20738](https://jira.mariadb.org/browse/MDEV-20738) for more information.

#### Installing Debug Info Packages with yum/dnf

The MariaDB `yum` repository contains [debuginfo](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Developer_Guide/intro.debuginfo.html) packages.

On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's repository using [yum](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum.md) or [dnf](https://en.wikipedia.org/wiki/DNF_\(software\)). Starting with RHEL 8 and Fedora 22, `yum` has been replaced by `dnf`, which is the next major version of `yum`. However, `yum` commands still work on many systems that use `dnf`. For example:

```bash
sudo yum install MariaDB-server-debuginfo
```

See [Installing MariaDB with yum/dnf: Installing Debug Info Packages with YUM](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum.md#installing-debug-info-packages-with-yum) for more information.

#### Installing Debug Info Packages with zypper

The MariaDB `zypper` repository contains [debuginfo](https://en.opensuse.org/openSUSE:Packaging_guidelines#Debuginfo) packages.

On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) from MariaDB's repository using [zypper](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md). For example:

```bash
sudo zypper install MariaDB-server-debuginfo
```

See [Installing MariaDB with zypper: Installing Debug Info Packages with ZYpp](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#installing-debug-info-packages-with-zypp) for more information.

#### Installing Debug Info Packages from MariaDB's Debian or Ubuntu repository

These are for when you already installed MariaDB from a MariaDB mirror.

For Ubuntu an additional repository step is needed:

```
sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el,s390x]  https://ftp.osuosl.org/pub/mariadb/repo/10.5/ubuntu focal main/debug'
```

Adjust `10.5` to the major version you are debugging and `focal` to the required distribution.

```
apt-get update && apt-get install -y mariadb-server-core-10.5-dbgsym
```

From [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/what-is-mariadb-109) the version isn't included in the package name and `mariadb-server-core-dbgsym` can be used as the package name.

#### Installing Debug Info Packages packaged by Ubuntu or Debian

If you used the MariaDB versions provided by Debian or Ubuntu see the following links.

For Debian see [AutomaticDebugPackages](https://wiki.debian.org/AutomaticDebugPackages)

For Ubuntu see [Debug%20Symbol%20Packages](https://wiki.ubuntu.com/Debug%20Symbol%20Packages)

### Installing Debugging Symbols on Windows

Debugging symbols are available to install on Windows.

#### Installing Debugging Symbols with the MSI Installer on Windows

Debugging symbols can be installed with the [MSI](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows.md) installer. Debugging symbols are not installed by default. You must perform a custom installation and explicitly choose to install debugging symbols.

The [MSI](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows.md) installer can be downloaded from the [MariaDB downloads page](https://downloads.mariadb.org).

#### Installing Debugging Symbols with the ZIP Package on Windows

MariaDB also provides a [ZIP](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-windows-zip-packages.md) package that contains debugging symbols on Windows.

The [ZIP](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-windows-zip-packages.md) package that contains debugging symbol can be downloaded from the [MariaDB downloads page](https://mariadb.com/downloads).

### Containers with Debug Symbols

#### Prebuilt Debug Containers

These are currently only per major release version and are generated out of CI. They are always the latest version in the main branch on [GitHub](https://github.com/MariaDB/server).

There are available on at [mariadb-debug?tab=tags](https://quay.io/repository/mariadb-foundation/mariadb-debug?tab=tags).

Use the container name `quay.io/mariadb-foundation/mariadb-debug:VERSION`.

Where `VERSION` corresponds to the major version you wish to test with.

#### Creating a Container with Debugging Symbols

Build using a Containerfile/Dockerfile:

```
ARG VERSION=10.11
FROM mariadb:$VERSION

RUN apt-get update \
        && apt-get install -y gdb mariadb-server-core-dbgsym=$(dpkg -s mariadb-server-core |  awk '/Version/{print $NF}') ; \
        rm -rf /var/lib/apt/lists/*
```

Build with:

```
buildah bud --tag mariadb_debug --build-arg VERSION=10.11.6 -f Containerfile .
```

Then you will have a `mariadb_debug` container.

Example use:

```
podman run --entrypoint gdb --user mysql --volume mariadb_data:/var/lib/mysql mariadb_debug -ex r --args /usr/sbin/mariadbd
```

## Enabling Core Dumps

To enable core dumps, see [Enabling Core Dumps](enabling-core-dumps.md) for details.

## Where is the Core File on Linux?

At the bottom of the error log there will be some text about the core location including:

```
Writing a core file...
Working directory at /var/lib/mariadb
Resource Limits:
Limit                     Soft Limit           Hard Limit           Units     
...
Max core file size        unlimited            unlimited            bytes     
...
Core pattern: |/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h

Kernel version: Linux version 6.0.0-0.rc2.19.fc38.x86_64 (mockbuild@bkernel01.iad2.fedoraproject.org) (gcc (GCC) 12.2.1 20220819 (Red Hat 12.2.1-1), GNU ld version 2.39-2.fc38) #1 SMP PREEMPT_DYNAMIC Mon Aug 22 12:52:40 UTC 2022
```

If the was a core limit in the resource limits there may be limited or no core file information.

If the core pattern begins with a **|**, then the following is the executable that handled the core file during the crash. The following show a few techniques to access the core depending on the pattern. If another program is used, look at its manual page to see how to get access to the core file.

If a plain core filename is in the "Core pattern" there's a good chance it will be in the Working directory location. It might have a `.{process number}` suffix on the filename.

### Extracting a core file from a container

If you are running MariaDB in a container, the locations where the core dump can be generated are limited. Looking at the container log, this will likely be where the error log information is. The "Core pattern" of a Linux system is currently a global fixed value. The consequence is if this core pattern refers to a program, that program isn't likely to be in the container and won't be executed on the crash.

The system wide crash handler can be changed with `sysctl kernel.core_pattern=core` to set this back to a file based crash. With this, the crash should occur in the working directory, normally the `/var/lib/mysql` data directory of the container volume.

### Extracting a core file from systemd-coredump

For `systemd-coredump`, there is a program `coredumpctl` to manage access.

```
coredumpctl list
TIME                            PID   UID   GID SIG     COREFILE EXE                                                                                        >
Fri 2022-09-09 14:16:37 AEST 213571  1000  1000 SIGSEGV present  /usr/sbin/mariadbd
```

To access the program using `gdb`, `coredumpctl debug` (defaults to last crash), will load the core dump in gdb. The instructions in the [next section](how-to-produce-a-full-stack-trace-for-mariadbd.md#getting-backtraces-with-gdb-on-linux) for extracting information.

See also: [extracting core dumps with systemd-coredump](enabling-core-dumps.md#extracting-linux-core-dumps-with-systemd-coredump).

### Extract a core file from abrt

A core pattern of `|/usr/libexec/abrt-hook-ccpp` indicates `abrt` system is used.

[abrt-cli](https://abrt.readthedocs.io/en/latest/usage.html) is a command line user interface for access the core file.

### Extract a core file from apport

A core pattern of `[|/usr/share/apport/apport` indicates `apport`.

For more information see [Apport Project Wiki](https://wiki.ubuntu.com/Apport).

[apport-retrace](https://wiki.ubuntu.com/DebuggingProgramCrash#Using_apport-retrace) allows you to "Examine Locally" and run a `gdb` session. One you have gdb started instructions in the [next section](how-to-produce-a-full-stack-trace-for-mariadbd.md#getting-backtraces-with-gdb-on-linux) can be used for extracting information.

## Analyzing a Core File with `gdb` on Linux

To analyze the core file on Linux, you can use [gdb](https://www.gnu.org/software/gdb/documentation).

For example, to open a core file with [gdb](https://www.gnu.org/software/gdb/documentation), you could execute the following:

```
sudo gdb /usr/sbin/mariadbd  /var/lib/mysql/core.932
```

Be sure to replace `/usr/sbin/mariadbd` with the path to your `mariadbd` binary (might be `mysqld` on [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) and earlier) and to also replace `/var/lib/mysql/core.932` with the path to your core file.

Once [gdb](https://www.gnu.org/software/gdb/documentation) has opened the core file, if you want to [log all output to a file](https://sourceware.org/gdb/current/onlinedocs/gdb/Logging-Output.html#Logging-Output), then you could execute the following commands:

```
set logging file /tmp/gdb_output.log
set logging on
```

If you do not execute `set logging file`, then the `set logging on` command creates a `gdb.txt` in your current working directory. Redirecting the output to a file is useful, because it can make it easier to analyze. It also makes it easier to send the information to a MariaDB developer, if that becomes necessary.

Do any commands that you would like to do. For example, you could [get the backtraces](how-to-produce-a-full-stack-trace-for-mariadbd.md#getting-backtraces-with-gdb-on-linux).

Once you are done, you can exit [gdb](https://www.gnu.org/software/gdb/documentation) by executing the [quit](https://sourceware.org/gdb/current/onlinedocs/gdb/Quitting-GDB.html#Quitting-GDB) command.

## Getting Backtraces with `gdb` on Linux

On Linux, once you have debugging symbols for your `mariadbd` binary, you can use the [gdb](https://www.gnu.org/software/gdb/documentation) utility to get [backtraces](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace), which are what `gdb` calls stack traces. Backtraces can be obtained from a core file or from a running `mariadbd` process.

Full [backtraces](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) are preferred and will contain function arguments, which can contain useful information such as query strings, so it can make the information easier to analyze.

To get a **full** [backtrace](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) of the main thread, then you could execute the following:

```
bt -frame-arguments all full
```

If you want to get a **full** [backtrace](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) of **all** threads, then you could execute the following:

```
thread apply all bt -frame-arguments all full
```

If you want to get a full backtrace to a file to report a bug, the recommended way is to use gdb:

```
set logging on
set pagination off
set print frame-arguments all
thread apply all bt full
set logging off
```

This will write the full backtrace into the file `gdb.txt`.

### Getting Full Backtraces For All Threads From a Core File

Sometimes it can be helpful to get **full** [backtraces](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) for all threads. The full [backtraces](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) will contain function arguments, which can contain useful information such as query strings, so it can make the information easier to analyze.

To get **full** [backtraces](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) for all threads from a `mariadbd` core file, execute a command like the following:

```
sudo gdb --batch --eval-command="set print frame-arguments all" --eval-command="thread apply all bt full" /usr/sbin/mariadbd /var/lib/mysql/core.932  > mariadbd_full_bt_all_threads.txt
```

Be sure to replace `/usr/sbin/mariadbd` with the path to your `mariadbd` binary and to also replace `/var/lib/mysql/core.932` with the path to your core dump.

The [backtraces](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) will be output to the file `mariadbd_full_bt_all_threads.txt`.

### Getting Full Backtraces For All Threads From a Running `mariadbd` Process

Sometimes it can be helpful to get **full** [backtraces](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) for all threads. The full backtraces will contain function arguments, which can contain useful information such as query strings, so it can make the information easier to analyze.

To get **full** [backtraces](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) for all threads from a running `mariadbd` process, execute a command like the following:

```
sudo gdb --batch --eval-command="set print frame-arguments all"  --eval-command="thread apply all bt full" /usr/sbin/mariadbd $(pgrep -xn mariadbd)  > mariadbd_full_bt_all_threads.txt
```

Be sure to replace `/usr/sbin/mariadbd` with the path to your `mariadbd` binary.

The [backtraces](https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html#Backtrace) will be output to the file `mariadbd_full_bt_all_threads.txt`.

Sometimes very busy systems are too busy to batch obtain the backtrace. If this is the case, `gcore $(pidof mariadbd)` can save the core and then obtain the backtrace out of the dumped core.

### Getting a Full Backtrace out of a Container

If the crash or assertion is repeatable it could be easiest to run `mariadbd` under #gdb`.`

The container image name here can be a prebuilt one from `quay.io/mariadb-foundation/mariadb-debug` or an explicit version built yourself as above.

```
docker run -v datavolume:/var/lib/mysql/ --rm --user mysql  quay.io/mariadb-foundation/mariadb-debug:10.11 gdb -ex r  -ex 'thread apply all bt -frame-arguments all full'  --args mariadbd
```

In docker-compose.yml form this looks like:

```
services:
  mariadb:
    image: quay.io/mariadb-foundation/mariadb-debug:10.11
    volumes:
      - mariadbdata:/var/lib/mysql
    environment:
      - MARIADB_ROOT_PASSWORD=bob
    command: gdb -ex r  -ex 'thread apply all bt -frame-arguments all full'  --args mariadbd
    user: mysql
volumes:
  mariadbdata: {}
```

Note, the initialization of data is assumed. Omit `command` and `user` if it isn't.

If you wish to attach to and existing process in a container, the container needs to be started with the SYS\_PTRACE capability. The sysctl `kernel.yama.ptrace_scope` that allows this should also be set to 0.

```
$ podman run -v data:/var/lib/mysql/ --cap-add SYS_PTRACE --name mtest -d quay.io/mariadb-foundation/mariadb-debug:11.2
$ podman exec --user mysql mtest gdb -p 1 -ex  'thread apply all bt -frame-arguments all full'
```

Note: `podman` has the same arguments and behaviour as `docker` if you'd rather use that.

or in compose:

```
cap_add:
    - SYS_PTRACE
```

The container process is always pid one, and here we use `c` then `thread apply all bt -frame-arguments all full` as the pre-loaded `gdb` commands. When a particular signal like assert or SEGV is triggered, the backtrace will be displayed.

## Letting a Container coredump

First, the `sysctl kernel.core_pattern` needs to be `core`. If it starts with a pipe character it try to execute this within the container. This is a kernel wide setting and cannot be applied to a specific container. The bottom of a crash will show you want it is set to.

With this set, just running a container with debug info is sufficient. The core should be dumped on the datadir volume. With the `core` dump here, analysis can occur like:

```
podman run --rm --user mysql --volume data:/var/lib/mysql -i mariadb_debug gdb --batch --eval-command="set print frame-arguments all" --eval-command="thread apply all bt full" /usr/sbin/mariadbd /var/lib/mysql/core | tee mariadbd_full_bt_all_threads.txt
```

## Running a Copy of the Database Directory

If you are concerned with debuggers running on your production database\
you can also copy the database to another location.

This is useful when you know which statement crashed the server.

Just start mariadbd with the options`--datadir=/copy-of-original-data-directory --core-file --stack-trace --socket=/tmp/mariadbd-alone.sock --skip-networking`

## Disabling Stack Traces in the Error Log

In order to disable stack traces in the [error log](../../../server-management/server-monitoring-logs/error-log.md), you can configure the [skip\_stack\_trace](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#stack-trace) option either on the command-line or in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
skip_stack_trace
```

## Reporting the Problem

If you encounter some problem in MariaDB, then MariaDB's developers would appreciate if you would [report a bug](../../community/community/bug-tracking/reporting-bugs.md) at the [MariaDB JIRA bug tracker](https://jira.mariadb.org). Please include the following information:

* Your full stack trace.
* Your [error log](../../../server-management/server-monitoring-logs/error-log.md).
* Your [option files](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).
* How to reproduce the problem.
* [SHOW ENGINE INNODB STATUS](../../sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md)
* [SHOW CREATE TABLE {table](../../sql-statements/administrative-sql-statements/show/show-create-table.md) (for each table in query) and [EXPLAIN {query}](../../sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) if a query related crash.

A [MariaDB FTP server](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-ftp-server/README.md) is available for large and/or sensitive information. Please upload in `.tar.gz` or `.zip` archive.

For very difficult or critical errors, you should consider uploading the following information to the [MariaDB FTP server](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-ftp-server/README.md) the following:

* Your build of `mariadbd` (if you compiled it), otherwise version information on the mariadb-server package.
* Your core file.
* Your contact information.
* The associated [JIRA issue identifier](https://jira.mariadb.org) for the bug, if you [reported a bug](../../community/community/bug-tracking/reporting-bugs.md).

This information will allow MariaDB developers to analyze it and try to create a fix.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
