# Profiling Memory Usage

Profiling the memory usage can be useful for finding out why a program appears to use more memory than it should. It is especially helpful for analyzing OOM situations or other cases where the memory grows linearly and causes problems.

To profile the memory usage of a program, there are multiple options. The following sections describe the methods that are available.

If a problem in memory usage is identified and it appears to be due to a bug, please open a new bug report on the [MariaDB Jira](https://jira.mariadb.org/) under the correct project and include the relevant memory profiling output in it. Refer to [How to Write a Good Bug Report](reporting-bugs.md#contents-of-a-good-bug-report) for more details.

## Known issues that can cause extended memory usage

### Transparent huge pages (THP)

Transparent huge pages (THP), which is enabled by default in many newer Linux distributions, can cause out-of-memory-issues for MariaDB as THP is not suitable for databases. This is described at [MDEV-33279](https://jira.mariadb.org/browse/MDEV-33279).

MariaDB Community Server 10.6.17, MariaDB Enterprise Server 10.6.16-11 and all other MariaDB server releases after these have THP disabled.

### System malloc is not good if there are a lot of allocations of different size.

If [Memory\_used](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#memory_used) and [information\_schema.processlist](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table) do not show an increase in memory, but the process still increases in size, then a likely problem is the system memory allocation library (malloc). Replacing malloc with [tcmalloc or jemalloc](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/compiling-mariadb-with-extra-modulesoptions/using-mariadb-with-tcmalloc-or-jemalloc) should fix the issue in this case.

## Profiling with the MariaDB server

Recent MariaDB versions have a global variable [Memory\_used](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#memory_used) that shows how much memory the MariaDB server has allocated. By monitoring this variable one can find out if
if the MariaDB allocated memory grows.

One can also check memory usage per user with the [information\_schema.processlist](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table):

```
SELECT id, MEMORY_USED, MAX_MEMORY_USED FROM information_schema.processlist;
```

This shows the current memory used per connection and the maximum memory they have
used since the user connected.

The [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) can also be used to find out who is allocated memory and for what.

Note that one can also set the [max\_session\_mem\_used](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_session_mem_used) variable to restrict a user's memory usage.

## BPF Compiler Collection (bcc)

The [BPF Compiler Collection (bcc)](https://github.com/iovisor/bcc) toolkit comes with the `memleak` program that traces outstanding memory allocations. This is a very convenient way of debugging high memory usage as it'll immediately show where the memory is allocated at.

By default the tool will print output once every five seconds with the stacktraces that have the most open allocations. `Ctrl+C` can be used to interrupt the collection of the traces.

The profiling interval and the profiling duration can be passed as arguments to `memleak`. The first argument is how often a sample is taken and the second argument is how long to sample for. To help analyze excessive memory usage, collect the output of the `memleak` program for at least 60 seconds. The longer the profiling can be left on, the more accurate the information will be.

The overhead of the profiling can be large enough that it affects production workloads negatively. To reduce the overhead, the sampling frequency of memory allocations can be lowered using the `--sample-rate` option:

```bash
-s SAMPLE_RATE, --sample-rate SAMPLE_RATE
                        sample every N-th allocation to decrease the overhead
```

For example, `-s 10` will sample only 10% of memory allocations which may miss out memory leaks from individual allocations but the longer the system is left running, the more likely it is that a leaking memory allocation is sampled. This means that even with a lower sampling rate, the source of the memory leak will eventually be found.

### RHEL, CentOS, Rocky Linux and Fedora

On RHEL based systems, the package is named `bcc-tools`. After installing it, use the following command to profile the memory usage 5 times per second over a window of 60 seconds:

```bash
sudo /usr/share/bcc/tools/memleak -p $(pidof mariadbd) 5 60 | tee memleak.log
```

### Ubuntu and Debian

On Ubuntu/Debian the package is named `bpfcc-tools`. After installing it, use the following command to profile the memory usage 5 times per second over a window of 60 seconds:

```bash
sudo memleak-bpfcc -p $(pidof mariadbd) 5 60 | tee memleak.log
```

## Jemalloc Heap Profiling

Jemalloc is an alternative to the default glibc memory allocator. It is capable of analyzing the heap memory usage of a process which allows it to be used to detect all sorts of memory usage problems with a lower overhead compared to tools like Valgrind. Unlike the ASAN and LSAN sanitizers, it is capable of detecting cases where memory doesn't actually leak but keeps growing with no upper limit (e.g. items get appended to a list but are never removed).

### Ubuntu and Debian

To enable jemalloc, the packages for it must be first installed from the system repositories. Ubuntu 20.04 requires the following packages to be installed for jemalloc profiling:

```bash
apt-get -y install libjemalloc2 libjemalloc-dev binutils
```

### RHEL, CentOS, Rocky Linux and Fedora

The version of jemalloc that is available in most Red Hat repositories is not compiled with memory profiling support enabled. For RHEL based distributions, the only option is to [build jemalloc from source](https://github.com/jemalloc/jemalloc).

### Configuring Jemalloc for Heap Profiling

Once installed, edit the systemd service file with `systemctl edit mariadb.service` and add the following lines into it. The path to the `libjemalloc.so` file is OS-specific so make sure it points to the correct file. The example here is for Ubuntu and Debian environments.

```bash
[Service]
Environment=MALLOC_CONF=prof:true,prof_leak:true,prof_gdump:true,lg_prof_sample:18,prof_prefix:/var/lib/mysql/jeprof/jeprof
Environment=LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2
```

Then create the directory for the profile files:

```bash
mkdir /var/lib/mysql/jeprof/
chown mysql:mysql /var/lib/mysql/jeprof/
```

And finally restart MariaDB with `systemctl restart mariadb.service`.

The directory in `/var/lib/mysql/jeprof/` will start to be filled by versioned files with a `.heap` suffix. Every time the virtual memory usage reaches a new high, a file will be created. Initially, the files will be created very often but eventually the pace will slow down. Once the problematic memory usage has been identified, the latest `.heap` file can be analyzed with the `jeprof` program.

The simplest method is to generate a text report with the following command.

```bash
jeprof --txt /usr/sbin/mariadbd $(ls -1 /var/lib/mysql/jeprof/*.heap|sort -V|tail -n 1) > heap-report.txt
```

A better way to look at the generated heap profile is with the PDF output. However, this requires the installation of extra packages (`apt -y install graphviz ghostscript gv`). To generate the PDF report of the latest heap dump, run the following command:

```bash
jeprof --pdf /usr/sbin/mariadbd $(ls -1 /var/lib/mysql/jeprof/*.heap|sort -V|tail -n 1) > heap-report.pdf
```

The generated `heap-report.pdf` will contain a breakdown of the memory usage.

Note that the report generation with the `jeprof` program must be done on the same system where the profiling was done. If done elsewhere, the binaries do not necessarily match and can cause the report generation to fail.

## Tcmalloc Heap Profiling

Similarly to the jemalloc memory allocator, the [tcmalloc](https://github.com/google/tcmalloc) memory allocator comes with a leak checker and heap profiler.

### Installation

#### RHEL, CentOS and Rocky Linux

On RHEL based systems, the `gperftools` package is in the EPEL repositories. These must be first enabled by installing the `epel-release` package.

```bash
sudo dnf -y install epel-release
```

After this, the `gperftools` package can be installed.

```bash
sudo dnf -y install gperftools
```

#### Ubuntu 20.04

```bash
sudo apt -y install google-perftools
```

### Service file configuration

Once tcmalloc is installed, edit the systemd service file with `systemctl edit mariadb.service` and add the following lines into it.

**Note:** Make sure to use the correct **path** and **library name** to the tcmalloc library in `LD_PRELOAD`. The following example uses the Debian location of the library. The file is usually located in `/usr/lib64/libtcmalloc_and_profiler.so.4` on RHEL systems. The version number of the library can also change which might require other adjustments to the library path.

```bash
[Service]
Environment=LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc_and_profiler.so.4
Environment=HEAPPROFILE=/var/lib/mysql/pprof/mariadbd.prof
Environment=HEAPCHECK=normal
Environment=HEAP_CHECK_AFTER_DESTRUCTORS=true
```

Then create the directory for the profile files:

```bash
mkdir /var/lib/mysql/pprof/
chown mysql:mysql /var/lib/mysql/pprof/
```

And finally restart MariaDB with `systemctl restart mariadb.service`.

### Configuring Heap Dump Frequency

The heap profiling is configured using environment variables. The details can be found in the _Modifying Runtime Behavior_ section of the gperftools documentation: [heapprofile.html](https://gperftools.github.io/gperftools/heapprofile.html)

By default, tcmalloc dumps the heap profile every time 1GiB of memory has been allocated (`HEAP_PROFILE_ALLOCATION_INTERVAL`) or whenever the high-water memory usage mark increases by 100MiB (`HEAP_PROFILE_INUSE_INTERVAL`). If there's no activity, no memory dumps will be generated.

To trigger a memory dump based on a time interval, set the `HEAP_PROFILE_TIME_INTERVAL` environment variable to the number of seconds between each dump. For example, with `Environment=HEAP_PROFILE_TIME_INTERVAL=3600` there will be one heap dump per hour.

### Report generation

Depending on which OS you are using, the report generation program is named either `pprof` (RHEL) or `google-pprof` (Debian/Ubuntu).

It is important to pick the latest `.heap` file to analyze. The following command generates the `heap-report.pdf` from the latest heap dump. The file will show the breakdown of the memory usage.

```bash
pprof --pdf /usr/sbin/mariadbd $(ls /var/lib/mysql/pprof/*.heap|sort -V|tail -n 1) > heap-report.pdf
```

## See also

* [Using MariaDB with tcmalloc or jemalloc](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/compiling-mariadb-with-extra-modulesoptions/using-mariadb-with-tcmalloc-or-jemalloc)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
