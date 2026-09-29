---
description: >-
  Operating system tuning for GridGain 9, including CPU power management, user
  limits, virtual memory, swappiness, RAM sharing, and advanced memory and I/O
  settings.
---

# OS Tuning

### CPU power management

Make sure you CPUs are in **performance** power mode:

```
# cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
performance
```

Disable CPU clock throttling in BIOS if necessary.

### Ulimits

You can configure user limits for GridGain in the `/etc/security/limits.conf` file. In it, you set the limits for each user in the following format:

```
<domain> <type> <item> <value>
```

For GridGain, you can set both soft and hard limit `types` on the maximum number of open file descriptors (`nofile`) and maximum number of processes (`nproc`). The recommended values for environments with several distribution zones:

```
gridgain - nofile 65536
gridgain - nproc 65536
```

If the system-wide number of file descriptors is low, setting the `nofile` limit to a high value will not eliminate the "Too many open files" error. You can resolve this issue by modifying `/proc/sys/fs/file-max`.

{% hint style="info" %}
The `limits.conf` file is ignored if GridGain is run as a systemctl service. In this case, configure user limits in the `/etc/systemd/system/gridgain.service` file:

```
[Service]
LimitNOFILE=65536
LimitNPROC=65536
```
{% endhint %}

### Linux Kernel Panic Delay

In case of kernel panic, GridGain needs some time to create data dumps. It is recommended to set the `kernel.panic` parameter to 3. You can set Linux kernel properties in the `/etc/sysctl.conf` file.

### Utilizing Linux Virtual Memory

Linux leaves space for an in-memory cache to handle I/O operations. You can manually configure them to provide more performance and better safety for larger operations. To configure the parameters below, set them in the `/etc/sysctl.conf` file and execute the `sudo sysctl –p` command, or run the `sysctl -w` command.

```
vm.dirty_background_ratio = 1
vm.dirty_ratio = 20
vm.dirty_expire_centisecs = 500
vm.dirty_writeback_centisecs = 100
vm.overcommit_memory = 2
vm.overcommit_ratio = 100
vm.swappiness = 0
vm.max_map_count=262144
```

Below is the expanded information on these parameters:

- The `vm.dirty_background_ratio` parameter sets how much of memory can be occupied by "dirty" pages after which they will be flushed to disk. Having too many dirty pages in memory can be detrimental to performance, so it is recommended to have a low percentage.

- The `vm.dirty_ratio` parameter sets the percent of memory occupied by dirty pages. If too many pages are dirty, they will be flushed to disk. Setting it low keeps the memory clean.

- The `vm.dirty_expire_centisecs` parameter sets how long dirty pages can be stored in memory. We recommend doing this every 5 seconds.

- The `vm.dirty_writeback_centisecs` parameter configures how often the system checks if any data needs to be flushed to the disk. It is recommended to keep checking it every 1 second.

- The `vm.overcommit_memory` parameter sets if applications can commit more data to memory than there is available space. Set to 2 to never overcommit.

- The `vm.overcommit_ratio` sets how much space is kept for overcommit, in percent. Set it to 100 to never commit more to memory than you have space available.

- The `vm.swappiness` parameter configures if swap will be used. We recommend disabling it to avoid it interfering with persistence.

- The `vm.max_map_count` controls the maximum number of memory map areas a single process can have. Low values can cause crashes and out of memory errors.

## Tune Swappiness Setting

An operating system starts swapping pages from RAM to disk when overall RAM usage hits a certain threshold.
Swapping can impact GridGain cluster performance.
You can adjust the operating system's setting to prevent this from happening.
For Unix, the best option is to either decrease the `vm.swappiness` parameter to `10`, or set it to `0` if native persistence is enabled:

```bash
sysctl -w vm.swappiness=0
```

The value of this setting can prolong GC pauses as well. For instance, if your GC logs show `low user time, high
system time, long GC pause` records, it might be caused by Java heap pages being swapped in and out. To
address this, use the `swappiness` settings above.

## Share RAM with OS and Apps

An individual machine's RAM is shared among the operating system, GridGain, and other applications.
As a general recommendation, if a GridGain cluster is deployed in pure in-memory mode (native
persistence is disabled), then you should not allocate more than 90% of RAM capacity to GridGain nodes.

On the other hand, if native persistence is used, then the OS requires extra RAM for its page cache in order to optimally sync up data to disk.
If the page cache is not disabled, then you should not give more than 70% of the server's RAM to GridGain.

See an [example configuration](general-configuration-tips.md) for more details.

In addition to that, because using native persistence might cause high page cache utilization, the `kswapd` daemon might not keep up with page reclamation, which is used by the page cache in the background.
As a result, this can cause high latencies due to direct page reclamation and lead to long GC pauses.

To work around this effect, add extra bytes of free memory to be reserved by the kernel:

```bash
sysctl -w vm.min_free_kbytes=1240000
```

### Advanced Memory Tuning

In Linux and Unix environments, it's possible that an application can face long GC pauses or lower performance due to I/O or memory starvation due to kernel specific settings.
This section provides some guidelines on how to modify kernel settings in order to overcome long GC pauses.

If GC logs show `low user time, high system time, long GC pause` then most likely memory constraints are triggering swapping or scanning of a free memory space.

- Add `-XX:+AlwaysPreTouch` to JVM settings on startup.
- Disable NUMA zone-reclaim optimization.

  ```bash
  sysctl -w vm.zone_reclaim_mode=0
  ```

- Enable Transparent Huge Pages.

  THP can reduce memory management overhead in operating system, especially for large heaps and data regions. Make sure THP is properly configured:

  ```bash
  $ cat /sys/kernel/mm/transparent_hugepage/enabled
  [always] madvise never

  $ cat /sys/kernel/mm/transparent_hugepage/defrag
  always defer [defer+madvise] madvise never

  $ cat /sys/kernel/mm/transparent_hugepage/khugepaged/max_ptes_none
  0
  ```

### Advanced I/O Tuning

If GC logs show `low user time, low system time, long GC pause` then GC threads might be spending too much time in the kernel space being blocked by various I/O activities.
For instance, this can be caused by journal commits, gzip, or log roll over procedures.

As a solution, you can try changing the page flushing interval from the default 30 seconds to 5 seconds:

```bash
sysctl -w vm.dirty_expire_centisecs=500
sysctl -w vm.dirty_writeback_centisecs=100
```

{% hint style="info" %}
Refer to the [persistence tuning](persistence-tuning.md) section for the optimizations related to disk. Those optimizations can have a positive impact on GC.
{% endhint %}

### Clock tuning

GridGain relies on loosely synchronized clock. It's very important to set up a source of time synchronization between cluster nodes, like [chrony](https://chrony-project.org).
