---
description: >-
  Explains how to attach debugging tools to a live MariaDB process on Linux
  systems without restarting the service.
---

# Debugging a Running Server (on Linux)

{% include "../../../.gitbook/includes/hint-lower-level-development.md" %}

Even if you don't have a server that is [compiled for debugging](compiling-mariadb-for-debugging.md), there are still ways to get more information out from it if things go wrong.

When things go wrong, it's always better to have a version of mysqld daemon that is not stripped.

```
shell> file /usr/sbin/mysqld
```

If this doesn't say 'stripped' then you are fine. If not, you should either [download a binary with debugging information](https://downloads.mariadb.org) or [compile it, without stripping the binary](compiling-mariadb-for-debugging.md#building-with-debug-symbols).

### Debugging Memory Consumption With tcmalloc

Read the [Profiling Memory Usage](../../community/community/bug-tracking/profiling-memory-usage.md) page for more information on how to debug high memory consumption.

If you have a problem with a mysqld process that keeps on growing, you can use tcmalloc to find out\
what is allocating memory:

Depending on the system you have to install the `tcmalloc` (OpenSuse) or the `google-perftools-lib` (RedHat, Centos) package.

The following set of commands starts mysqld with memory profiling and if you kill it with SIGABRT, you will get a core dump that you can examine:

```
HEAPPROFILE=/tmp/mysqld.prof /usr/sbin/mysqld_safe --malloc-lib=tcmalloc --core-file-size=unlimited --core-file
```

or if you prefer to invoke mysqld directly:

```
ulimit -c unlimted
LD_PRELOAD=/usr/lib64/libtcmalloc.so.4 HEAPPROFILE=/tmp/mysqld.prof /usr/sbin/mysqld --core-file
```

You can of course add other [mysqld options](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) to the end of the above line.

Now start your client/application that uses MariaDB. You can find where memory is allocated in the `/tmp/mysqld.prof` file. If you find any memory issues, please report this in the [MariaDB bug tracker](https://jira.mariadb.org/secure/Dashboard.jspa)!

### ptrace Protection and Attaching GDB to a mysqld Instance

New Ubuntu releases do not allow one process to examine the memory of an\
arbitrary user's process. As a result, when trying to attach GDB to a running\
MariaDB (or any other process) instance, one gets the following error in GDB:

```
ptrace: Operation not permitted
```

More details are available in the [Ubuntu Wiki](https://wiki.ubuntu.com/SecurityTeam/Roadmap/KernelHardening#ptrace%20Protection).

To allow GDB to attach, one needs to edit the value of the`/proc/sys/kernel/yama/ptrace_scope` sysctl value.

* To change it temporarily, open a root shell and issue:

```
echo 0 > /proc/sys/kernel/yama/ptrace_scope
```

* To change it permanently, edit as root:

```
/etc/sysctl.d/10-ptrace.conf
```

and set the value to `0`.

### Debugging a Server That Hangs

If your mysqld server hangs, you may want to debug it to know what happened.

Preferably the server should be compiled for debugging, but it's not strictly necessary:

```
cmake -DCMAKE_BUILD_TYPE=Debug -DWITH_VALGRIND=ON .
make -j4
```

To know what the server is doing:

* Find out the process number of mysqld

```
ps -edalf | grep mysqld
```

* Attach to the process and get a back trace:

```
gdb -p 'pid of mysqld' path-to-mysqld
set height 0
set logging file /tmp/mysqld.log
set logging on
thread apply all backtrace full
```

After the above, you have a full backtrace, including all local variables, in the `mysqld.log` file. Note that you will only get all variables if the server is not stripped.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
