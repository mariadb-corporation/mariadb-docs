# Recommended Settings for Benchmarks

Running benchmarks requires a lot of different settings. In this article we collect our best known settings and recommendations.

## Hardware and BIOS Settings

We have had good experiences with Intel's hyperthreading on newer Xeon CPUs. Please turn on hyperthreading in your BIOS.

## NUMA

The NUMA architecture attaches resources (most important: memory) to individual NUMA nodes (typically: NUMA node = cpu socket). This results in a performance penalty when a cpu core from one NUMA node accesses memory from another NUMA node.

The NUMA topology can be checked with the _numactl_ command:

```
~ $numactl --hardware
available: 2 nodes (0-1)
node 0 cpus: 0 1 2 3 4 5 12 13 14 15 16 17
node 0 size: 12278 MB
node 0 free: 11624 MB
node 1 cpus: 6 7 8 9 10 11 18 19 20 21 22 23
node 1 size: 12288 MB
node 1 free: 11778 MB
node distances:
node   0   1 
  0:  10  21 
  1:  21  10
```

The Linux kernel uses ACPI tables from BIOS to detect if the hardware is NUMA. On NUMA hardware extra optimizations kick in:

* if a task has been scheduled on a certain NUMA node, the scheduler tries to put it on the same node again in the future
* if a task running on a certain NUMA node allocates memory, the kernel tries hard to map physical memory from the same NUMA node

This results in all kinds of weird behavior when you run one big process (mysqld) that consumes most of the memory. In such cases it is recommended to either turn off NUMA (BIOS or kernel command line) or prefix such problem processes with _numactl --interleave all_. You can enable this by running [mysqld\_safe](../../../../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) with the `--numa-interleave` option.

[More details can be found here](https://blog.jcole.us/2010/09/28/mysql-swap-insanity-and-the-numa-architecture/).

## Linux Kernel Settings

See [configuring Linux for MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-performance-advanced-configurations/configuring-linux-for-mariadb).

## InnoDB Settings

[innodb\_buffer\_pool\_size](../../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#innodb_buffer_pool_size) to about 80% of RAM or leaving <5G RAM free (on large RAM systems). Less if lots of connections are used.

[innodb\_log\_file\_size](../../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#innodb_log_file_size) to be larger than the amount of writes in the test run or sufficient to cover several minutes of the test run at least.

## MyISAM Settings

## General Settings

[threads\_cache\_size](../../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#threads_cache_size) should be the same as [max\_connections](../../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_connections) (unless using thread pools).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
