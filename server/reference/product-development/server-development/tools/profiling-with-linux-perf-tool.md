---
description: >-
  A technical guide on using the Linux perf utility to analyze server
  performance and identify code bottlenecks.
---

# Profiling with Linux perf tool

Linux `perf` tool can be used to do non-intrusive profiling.

## Frequency Based Sampling

This mechanism can be used to answer the question, what is MariaDB doing on my CPU.

### Recording a sample

Perf records at a high frequency, so only a short recording is sufficient to answer the question. If this is too short adjust the frequency at which perf does its recordings.

```
sudo perf record -p ${pidof mysqld} -g -o sample.perf -- sleep 5
```

The `-g` option here records the calling stack. Because seeing time in a mutex function isn't particularly interesting without knowing which mutex it is.

### Viewing a sample

To view a recording, you need the debug symbols for your executable. See [this page](../../debugging-mariadb/how-to-produce-a-full-stack-trace-for-mariadbd.md) on getting the debug symbols available.

Changing the ownership of the recording means you can run perf report without sudo.

This shows where in the process MariaDB is spending most of its time at the top level. MariaDB uses threads per user connection so this will usually show a significant time in a `handle_connection` function. There are background threads that also run, so this can quickly show if its connection related time or a background thread.

```
sudo chown $USER: sample.perf
perf report -i sample.perf -g
```

To see which low level functions are consuming the most time, `--no-children` means that each function listed include only the time that is being spend it this function and excluding the other functions it calls.

```
perf report -i sample.perf -g --no-children
```

Expanding out the function shows the complete call stack again. Multiple functions may have called the function you are looking at so there may be a different frequency breakdown.

A more complete example of performance analysis using perf is on this [Percona community blog article](https://www.percona.com/community-blog/2020/02/05/finding-mysql-scaling-problems-using-perf/).

## Dynamic Tracepoints

### Adding dynamic tracepoints

One can add tracepoints at function entry/exit (and other locations too):

```
sudo perf probe -x /path/to/ha_rocksdb.so  --add rocksdb_prepare
sudo perf probe -x /path/to/ha_rocksdb.so  --add rocksdb_prepare%return
```

### Viewing the tracepoints

```
sudo perf probe -l
```

### Running the profiler

Something like:

```
perf record -e 'probe_ha_rocksdb:*' -a -- sleep 60
```

Note: `-a` means system-wide.

There's also `-p $PID` option

```
perf record -e 'probe_ha_rocksdb:*' -p $(pidof mysqld) -- sleep 60
```

### Examining the trace

```
perf script
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
