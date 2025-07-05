# Enabling Core Dumps

## Enabling in an Option File

Core dumps are enabled by default on **Windows**, so **this step can be skipped on Windows** in those versions. See [MDEV-18439](https://jira.mariadb.org/browse/MDEV-18439) for more information.

In order to enable core dumps, you need to set the [core_file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables#core_file) system variable either on the command-line or in a relevant server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb-with-option-files). For example:

```
[mariadb]
...
core_file
```

You can check your current value by executing:

```
my_print_defaults --mariadbd
```

[core\_file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#core_file) is a system variable. Its value can be checked at runtime by executing the following:

```
SHOW GLOBAL VARIABLES LIKE 'core_file';
```

## Core Files on Linux

There are some additional details related to using core files on Linux.

### Disabling Core File Size Restrictions on Linux

On some systems there is a limit on the sizes of core files that can be dumped. You can check the system's current system-wide limit by executing the following:

```
ulimit -c
```

You can check the current limit of the `mariadbd` process specifically by executing the following:

```
sudo cat /proc/$(pidof mariadbd)/limits | grep "core file"
```

If you need to change the core size limit, the method you use depends on how you start `mariadbd`. See the sections below for more details.

The resource limits for the `mariadbd` process are printed to the [error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) when the `mariadbd` process crashes. That way, users can confirm whether the process may have been allowed to dump a core file. See [MDEV-15051](https://jira.mariadb.org/browse/MDEV-15051) for more information.

#### Running mariadbd Using mysqld\_safe

If you are starting MariaDB by running [mysqld_safe](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe), then configuring the following in the `[mysqld_safe]` option group in an option file should allow for unlimited sized core files:

```
[mysqld_safe]
...
core_file_size=unlimited
```

You can check your current values by executing:

```
my_print_defaults mysqld_safe
```

See [mysqld\_safe: Configuring the Core File Size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe) for more details.

**Note:** If you are using [mysqld_safe](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe) and running `mariadbd` as the `root` user, then no\
core file is created on some systems. The solution is to run `mariadbd` as another user.

#### Running mariadbd Manually

If you are starting mariadbd manually or in a custom script, then you can allow for unlimited sized core files by executing the following in the same shell or script in which mariadbd is executed:

```
ulimit -c unlimited
```

#### Running mariadbd Using systemd

If you are starting `mariadbd` using [systemd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd), then you may need to customize the MariaDB service to allow for unlimited size core files. For example, you could execute the following:

Using `sudo systemctl edit mariadb.service` add the contents:

```
[Service]

LimitCORE=infinity
```

See [systemd: Configuring the Core File Size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/starting-and-stopping-mariadb/systemd#configuring-the-core-file-size) for more details.

#### Running MariaDB Containers

To get a core dump in a `mariadb` container requires [setting the path on Linux](enabling-core-dumps.md#setting-the-path-on-linux) to not include a `sysctl kernel.core_pattern` beginning with a pipe to an executable that doesn't exist in the container. Setting to a straight `core` is recommended.

Also see [Container with Debug Symbols](how-to-produce-a-full-stack-trace-for-mariadbd.md#containers-with-debug-symbols).

#### Changing the System-Wide Limit

If you want to change the system-wide limit to allow for unlimited size core files for the `mysql` user account, then you can do so by adding the following lines to a file in [/etc/security/limits.d/](https://linux.die.net/man/5/limits.conf). For example:

```
sudo tee /etc/security/limits.d/mariadb_core.conf <<EOF
mysql soft core unlimited
mysql hard core unlimited
EOF
```

The system would have to be restarted for this change to take effect.

See [Configuring Linux for MariaDB: Configuring the Core File Size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-performance-advanced-configurations/configuring-linux-for-mariadb#configuring-the-core-file-size) for more details.

### Setting the Path on Linux

If you are using Linux, then it can be helpful to change a few settings to alter where the core files is written and what file name is used. This is done by setting the `kernel.core_pattern` and `kernel.core_uses_pid` attributes. You can check the current values by executing the following:

```
sysctl kernel.core_pattern
sysctl kernel.core_uses_pid
```

If you are using `mysql-test-run` and want to have the core as part of the test result, the optimal\
setting is probably the following (store cores in the current directory as `core.number-of-process-id`):

```
sudo sysctl kernel.core_pattern=core.%p kernel.core_uses_pid=0
```

If you are using a production system, you probably want to have the core files in a specific directory,\
not in the data directory. They place to store cores can be temporarily altered using the [sysctl](https://linux.die.net/man/8/sysctl) utility, but it is often more common to alter them via the [/proc](https://linux.die.net/man/5/proc) file system. See the following example:

```
sudo mkdir /tmp/corefiles
sudo chmod 777 /tmp/corefiles
sudo sysctl kernel.core_pattern=/tmp/corefiles/core
sudo sysctl kernel.core_uses_pid=1
```

The above commands will tell the system to put core files in `/tmp/corefiles`, and it also tells the system to put the process ID in the file name.

If you want to make these changes permanent, then you can add the following to a file in [/etc/sysctl.conf.d/](https://linux.die.net/man/5/sysctl.conf). For example:

```
sudo tee /etc/sysctl.d/mariadb_core.conf <<EOF
kernel.core_pattern=/tmp/corefiles/core
kernel.core_uses_pid=1
EOF
```

Note: if you are using containers, the pid is always going to be 1, so this may not be a useful setting. Appending an identifier like %t to the [kernel.core_pattern](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/kernel.html#core-pattern) will generate more unique files.

The value of `kernel.core_pattern` is printed to the [error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) when the `mariadbd` process crashes. That way, users can determine where the process may have dumped a core file. See [MDEV-15051](https://jira.mariadb.org/browse/MDEV-15051) for more information.

**Note:** Ensure that you have enough free disk space in the path pointed to by `kernel.core_pattern`.

#### Extracting Linux core dumps with systemd-coredump

Core dump management can be automated using [systemd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd), which then centrally manages all core dump files and provides information about detected core dumps and access to collected core files using the [coredumpctl](https://www.freedesktop.org/software/systemd/man/coredumpctl.html) utility.

This is enabled per default on Red Hat Enterprise Linux 8 and CentOS 8, and maybe other contemporary Linux distribution releases by now, too. It can be easily checked for by looking at the `kernel.core_pattern setting`. If it looks like this systemd-coredump is enabled:

```
# sysctl kernel.core_pattern
kernel.core_pattern = |/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h %e
```

On other distributions like Ubuntu (at least up to 21.10) it is not enabled by default, but can be set up manually.

To see all recent core dumps on the system you can then simply run

```
# coredumpctl list
```

Or you can check for MariaDB Server core dumps specifically with:

```
# coredumpctl list /usr/sbin/mariadbd
```

If an actual core file got stored you'll see `present` in the COREFILE column of the output, you can then extract the core file with:

```
# coredumpctl dump -o mariadbd.core ...PID...
```

using the process id number from the PID column, or when you just want to retrieve the latest MariaDB Server related entry:

```
# coredumpctl dump -o mariadb.core /usr/sbin/mariadbd
```

Starting with `systemd` 248 it is also possible to invoke the `gdb` debugger directly using the new `--debugger-arguments=...` option, e.g. making the extraction of all thread backtraces from the most recent MariaDB server crash a one liner without even having to extract the core dump file first (requires `gdb` to be installed):

```
# coredumpctl debug --debugger-arguments="-batch -ex 'thread apply all bt full'" /usr/sbin/mariadbd
```

So far none of the long term support Linux distribution releases have a new enough `systemd` version for this, the (as of this writing) still upcoming Ubuntu 22.04 "Jammy Jellyfish" will probably the first to support this.

### Core Dumps and setuid on Linux

Since `mariadbd` executes [setuid](https://linux.die.net/man/2/setuid), you may have to set `fs.suid_dumpable=2` to allow core dumps on Linux. You can check the current `fs.suid_dumpable` value by using the [sysctl](https://linux.die.net/man/8/sysctl) utility. For example:

```
sysctl fs.suid_dumpable
```

You can temporarily set it to `2` by using the [sysctl](https://linux.die.net/man/8/sysctl) utility. For example:

```
sudo sysctl -w fs.suid_dumpable=2
```

Or you can temporarily set it to `2` by writing to the [/proc](https://linux.die.net/man/5/proc) file system. For example:

```
sudo echo 2 > /proc/sys/fs/suid_dumpable
```

If you want to permanently set it to `2` then you can add the following to a file in [/etc/sysctl.conf.d/](https://linux.die.net/man/5/sysctl.conf):

```
sudo tee /etc/sysctl.d/mariadb_fs_suid_dumpable.conf <<EOF
fs.suid_dumpable=2
EOF
```

**Note:** If you don't want to change `fs.suid_dumpable`, then another solution is to start `mariadbd` directly as the `mysql` user, so that the [setuid](https://linux.die.net/man/2/setuid) call is not needed.

### Forcing a Core File on Linux

You can get a core dump from a running server with:

```
sudo gcore -o filename $(pidof mariadbd)
```

This will store a core dump in `filename.pid` where pid is the process ID of `mariadbd`.`mariadbd` will continue to be running and will not be affected by `gcore`.

Another method is to force a core file for `mariadbd` by sending the process the `sigabrt` signal, which has the signal code `6`. This is very useful to get the state of the unresponsive `mariadbd` process. However, this will cause `mariadbd` to crash, and crash recovery will be run on restart.

You can send the signal with the [kill](https://linux.die.net/man/1/kill) command. For example:

```
sudo kill -6 $(pidof mariadbd)
```

As an alternative to `$(pidof mariadbd)`, you can find the process ID either by using the [ps](https://linux.die.net/man/1/ps) utility or by checking the file defined by the [pid_file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables#pid_file) system variable.

## Core Files on Windows

Core dumps are enabled by default on Windows. See [MDEV-18439](https://jira.mariadb.org/browse/MDEV-18439) for more information.

There are some additional details related to using core files on Windows.

### Minidump Files on Windows

On Windows, the core file is created as a [minidump file](https://docs.microsoft.com/en-us/windows/desktop/debug/minidump-files).

For details on how to configure and read the [minidump file](https://docs.microsoft.com/en-us/windows/desktop/debug/minidump-files), see [How to read the small memory dump file that is created by Windows if a crash occurs](https://support.microsoft.com/en-us/help/315263/how-to-read-the-small-memory-dump-file-that-is-created-by-windows-if-a).

## Core Files on Kubernetes

See the IBM [Core Dump Handler](https://github.com/IBM/core-dump-handler) project.

## Core Files and Address Sanitizer (ASAN)

If your `mariadbd` binary is built with [Address Sanitizer (ASAN)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/compiling-mariadb-from-source/compile-and-using-mariadb-with-sanitizers-asan-ubsan-tsan-msan) then it will not be able to generate a core file.

## What's Included in Core Files

Core files usually contain a dump of all memory in the process's full address space. This means that if a server has some large buffers configured (such as a large [InnoDB buffer pool](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-buffer-pool)), then the server's core files can get very large.

Some large buffers have been excluded from core files on some systems as a way to reduce the size.

The following buffers are excluded:

* [InnoDB buffer pool](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-buffer-pool)
* [InnoDB log buffer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_buffer_size)
* InnoDB Redo log buffer (fixed 2M)
* [Query cache](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache)

The buffers are only excluded on Linux when using kernel version 3.4 and above and when using a non-debug build of `mariadbd`. Some Linux kernel versions have a [bug](https://lists.launchpad.net/maria-discuss/msg05245.html) which would cause the following warning to be printed to the log:

```
Sep 25 10:41:19 srv1 mysqld: 2018-09-25 10:41:19 0 [Warning] InnoDB: Failed to set memory to DODUMP: Invalid argument ptr 0x2aaac3400000 size 33554432
```

In those cases, the core dump may exclude some additional data. If that is not a concern, then the warning can be ignored. The problem can be fixed by upgrading to a Linux kernel version in which the bug is fixed.

## See Also

* [How to Produce a Full Stack Trace for mariadbd](how-to-produce-a-full-stack-trace-for-mariadbd.md)
* [HowTo: Debug Crashed Linux Application Core Files Like A Pro](https://www.cyberciti.biz/tips/linux-core-dumps.html)
* [A Nice Feature in MariaDB 10.3: no InnoDB Buffer Pool in Core Dumps](https://www.percona.com/community-blog/2018/06/28/nice-feature-in-mariadb-103-no-innodb-buffer-pool-in-coredumps/)
* [Getting MySQL Core file on Linux](https://www.percona.com/blog/2011/08/26/getting-mysql-core-file-on-linux/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
