---
description: >-
  Tips for tuning MaxScale performance, and how to diagnose performance
  problems with MaxCtrl.
---

# MaxScale Performance Optimization

This page gives tips for tuning MaxScale performance and diagnosing performance problems.

* Tune `query_classifier_cache_size` to allow maximal use of the query classifier cache. Increase the value and/or system memory until the set of unique SQL patterns fits into memory. By default at most 15% of the system memory is used for this cache. To detect if the SQL statements fit into memory, monitor the `QC cache evictions` value in `maxctrl show threads` to see how many evictions take place. If it keeps increasing, increase the size of the query classifier cache. Using the query classifier cache with a CPU bound workload gives a roughly 20% improvement in performance compared to when it is turned off.
* A faster CPU with more CPU cores is better. This is true for most applications but especially for MaxScale as it is mostly limited by the speed of the CPU. Using `threads=auto` is recommended (the default starting with MaxScale 6).
* Network throughput between the client, MaxScale and the database nodes governs how much traffic can be handled. The client-to-MaxScale network is likely to be saturated first: having multiple MaxScales in front of the cluster is an easy way of solving this problem.
* Certain MaxScale modules store data on disk. A faster disk improves their performance but depending on the module, this might not be a big enough of a problem to worry about. Filters like the `qlafilter` that write information to disk for every SQL query can cause performance bottlenecks.

## MaxScale Diagnostics using MaxCtrl

From 22.08.2 onwards, `maxctrl show maxscale` shows a `System` object with information about the system MaxScale is running on. The fields are:

| Field                                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| machine.cores\_physical                 | The number of physical CPU cores on the machine.                                                                                                                                                                                                                                                                                                                                                                                           |
| machine.cores\_available                | The number of CPU cores available to MaxScale. This number may be smaller than machine.cores\_physical, if CPU affinities are used and only a subset of the physical cores are available to MaxScale.                                                                                                                                                                                                                                      |
| machine.cores\_virtual                  | The number of virtual CPU cores available to MaxScale. This number may be a decimal and smaller than machine.cores\_available, if MaxScale is running in a container whose CPU quota and period has been restricted. Note that if MaxScale is not, or fails to detect it is running in a container, the value shown will be identical with machine.cores\_available.                                                                       |
| machine.memory\_physical                | The amount of physical memory on the machine.                                                                                                                                                                                                                                                                                                                                                                                              |
| machine.memory\_available               | The amount of memory available to MaxScale. This number may be smaller than machine.memory\_physical, if MaxScale is running in a container whose memory has been restricted. Note that if MaxScale is not, or fails to detect it is running in a container, the value shown will be identical with machine.memory\_physical. Note also that the amount is available to all processes running in the same container, not just to MaxScale. |
| maxscale.query\_classifier\_cache\_size | The maximum size of the MaxScale query classifier cache.                                                                                                                                                                                                                                                                                                                                                                                   |
| maxscale.threads                        | The number of routing threads used by MaxScale.                                                                                                                                                                                                                                                                                                                                                                                            |

In addition there is an `os` object that contains what the Linux command `uname` displays.

### Configuration

**`threads`**

If `threads` has not been specified at all in the MaxScale configuration file, or if its value is `auto`, then MaxScale will use as many routing threads as there are physical cores on the machine. This is the right choice, if MaxScale is running on a dedicated machine or in a container that has not been restricted in any way.

However, if the number of cores available to MaxScale have been restricted or if MaxScale is running in a container whose CPU quota and period have been limited, then it will lead to MaxScale using more routing threads than what is appropriate in the environment where it is running.

If `machine.cores_virtual` is less than `machine.cores_physical`, then `threads` should be specified explicitly in the MaxScale configuration file and its value should be that of `machine.cores_virtual` rounded up to the nearest integer. If that value is `1` it may be beneficial to check whether `2` gives better performance.

**`query_classifier_cache_size`**

If `query_classifier_cache_size` has not been specified in the MaxScale configuration file, then MaxScale will use at most 15% of the amount of physical memory in the machine for the cache. This is a good starting point, if MaxScale is running on a dedicated machine or in a container that has not been restricted in any way. Note that the amount specifies how much memory the cache at maximum is allowed to use, not what would immediately be allocated for the cache.

However, if the amount of memory available to MaxScale has been restricted, which may be the case if MaxScale is running in a container, this may cause the cache to grow beyond what is available, which will lead to a crash or MaxScale being killed.

If the value of `machine.memory_available` is less than that of `machine.memory_physical`, then `query_classifier_cache_size` should be explicitly set to 15% of `maxscale.memory_available`. The value can be larger, but must not be a bigger share of `machine.memory_available` than what is reasonable.

### Example

```
$ maxctrl show maxscale
...
├──────────────┼────────────────────────────────────────────────────────────────────────────┤
│ System       │ {                                                                          │
│              │     "machine": {                                                           │
│              │         "cores_available": 8,                                              │
│              │         "cores_physical": 8,                                               │
│              │         "cores_virtual": 4,                                                │
│              │         "memory_available": 20858544128,                                   │
│              │         "memory_physical": 41717088256                                     │
│              │     },                                                                     │
│              │     "maxscale": {                                                          │
│              │         "query_classifier_cache_size": 6257563238,                         │
│              │         "threads": 8                                                       │
│              │     },                                                                     │
│              │     "os": {                                                                │
│              │         "machine": "x86_64",                                               │
│              │         "nodename": "johan-P53s",                                          │
│              │         "release": "5.4.0-125-generic",                                    │
│              │         "sysname": "Linux",                                                │
│              │         "version": "#141~18.04.1-Ubuntu SMP Thu Aug 11 20:15:56 UTC 2022"  │
│              │     }                                                                      │
│              │ }                                                                          │
└──────────────┴────────────────────────────────────────────────────────────────────────────┘
```

As can be seen, `maxscale.threads` is larger than `machine.cores_virtual` and thus, `threads=4` should explicitly be specified in the MaxScale configuration file.

`maxscale.query_classifier_cache_size` is the default 15% of `machine.memory_physical` but as `machine.memory_available` is just half of that, something like `query_classifier_cache_size=3100000000` (\~15% of `machine.memory_available`) should be added to the configuration file.

```
[maxscale]
threads=4
query_classifier_cache_size=3100000000
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
