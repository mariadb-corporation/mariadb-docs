---
description: >-
  Instructions for monitoring and analyzing memory allocation to identify leaks
  or excessive consumption within the server.
---

# Debugging Memory Usage

{% include "../../../.gitbook/includes/hint-system-level-debugging.md" %}

## Troubleshooting Memory Usage

This page describes how to debug MariaDB's memory usage. It uses CentOS 7 but can be applied to other systems as well.

Use Google PerfTools for debugging memory usage: [heapprofile.html](https://gperftools.github.io/gperftools/heapprofile.html)

On CentOS, install PerfTools like this:

```bash
sudo yum install gperftools 
service mariadb stop
systemctl edit mariadb
```

In the editor that opens, add and save this content:

```ini
[Service]
Environment="HEAPPROFILE=/tmp/heap-prof-1"
Environment="HEAP_PROFILE_ALLOCATION_INTERVAL=10737418240"
Environment="HEAP_PROFILE_INUSE_INTERVAL=1073741824"
Environment="LD_PRELOAD=/usr/lib64/libtcmalloc.so.4"
```

Then run this command:

```bash
service mariadb start
```

Now, run the workload. When memory consumption becomes large enough, run this command:

```bash
ls -la /tmp/heap-prof-*
```

This should show several files. Copy the last file from the list:

```bash
cp /tmp/heap-prof-1.0007.heap .
```

Then, run this command:

```bash
pprof --dot /usr/sbin/mysqld heap-prof-1.0007.heap  > 7.dot
```

{% hint style="info" %}
This produces a lot of lines, like `/bin/addr2line: Dwarf Error: ...`.
{% endhint %}

Then, please send us the `7.dot` file.

## Memory Leak Overview

Operating system memory can be assigned, giving MariaDB a virtual address space, and allocated (paged in), once MariaDB starts to use this memory.

When looking at something that might be a memory leak, pay particular attention between the virtual size and the resident size.

When MariaDB has the same virtual size, but the resident size increases over time, this is a good indication that the memory buffers allocated to MariaDB are slowly being used. In this case its unlikely to be a memory leak.

Because memory leaks are hard to track down, documenting a known good version and a version that is leaking memory can make it easier to examine code changes in those versions against some other criteria like those obtained from the sections below to identify the cause.

## Performance Schema

The memory instrumentation of the performance schema can be enable with the following:

```
performance_schema=on
performance-schema-instrument='memory/%=ON'
```

This is available since [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2). With this enabled, [performance\_schema.memory\_summary\_global\_by\_event\_name](../../system-tables/performance-schema/performance-schema-tables/performance-schema-memory_summary_global_by_event_name-table.md) can start to show where the memory leak is occurring.

## Memleak

`memleak` is a BPF program for Linux that is frequently packaged like bcc-tools or similar ([bpfcc-tools](https://packages.debian.org/stable/bpfcc-tools) on Debian).

The upstream documentation provides [this example](https://github.com/iovisor/bcc/blob/master/tools/memleak_example.txt).

The important aspect on measurement is to let MariaDB startup, and commence an normal workload before measurement. Starting too early or before the caches are populated is likely to result in false recording of memory allocations that will be eventually released.

Increasing the time interval of `memleak` is important to run longer than the usual query. If your memory is leaking over hours, then a high interval of 10 minutes so will reduce memory temporary allocated for a query. Recording for a longer time or multiple times should provide enough information to narrow down the location of the leak.

{% hint style="info" %}
Very old Linux kernels like Centos/RHEL 7 might not have sufficient hooks to measure this correctly.
{% endhint %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
