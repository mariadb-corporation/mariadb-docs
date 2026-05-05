---
description: >-
  Recommended Linux kernel parameters for MariaDB ColumnStore:
  vm.overcommit_memory, dirty-page ratios, vfs_cache_pressure, network buffer
  sizes, and process limits in /etc/sysctl.conf.

---

# Optimizing Linux Kernel Parameters for MariaDB ColumnStore

## Introduction

MariaDB ColumnStore is a high-performance columnar database designed for analytical workloads. By optimizing the Linux kernel parameters, you can further enhance the performance of your MariaDB ColumnStore deployments.

## Recommended Parameters

The following table lists the recommended optimized Linux kernel parameters for MariaDB ColumnStore:

For more information refer to [Optimize Linux Kernel Parameters](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/community-server-with-columnstore#optimize-linux-kernel-parameters).

<table><thead><tr><th width="227">Parameter</th><th width="182">Recommended Value</th><th>Explanation</th></tr></thead><tbody><tr><td>vm.overcommit_memory</td><td>1</td><td>Disables overcommitting of memory, ensuring sufficient memory is available for MariaDB ColumnStore.</td></tr><tr><td>vm.dirty_background_ratio</td><td>5</td><td>Sets the percentage of dirty memory that can be written back to disk in the background. A lower value reduces the amount of dirty memory, improving performance.</td></tr><tr><td>vm.dirty_ratio</td><td>10</td><td>Sets the percentage of dirty memory that can be written back to disk before the kernel starts to write out clean pages. A lower value reduces the amount of dirty memory, improving performance.</td></tr><tr><td>vm.vfs_cache_pressure</td><td>50</td><td>Sets the pressure level for the kernel's VFS cache. A lower value reduces the amount of memory used by the VFS cache, improving performance.</td></tr><tr><td>net.core.netdev_max_backlog</td><td>2500</td><td>Sets the maximum number of packets that can be queued for a network device. A higher value allows for more packets to be queued, improving performance.</td></tr><tr><td>net.core.rmem_max</td><td>16777216</td><td>Sets the maximum receive buffer size for TCP sockets. A higher value allows for larger buffers, improving performance.</td></tr><tr><td>net.core.wmem_max</td><td>16777216</td><td>Sets the maximum send buffer size for TCP sockets. A higher value allows for larger buffers, improving performance.</td></tr><tr><td>net.ipv4.tcp_max_syn_backlog</td><td>8192</td><td>Sets the maximum number of queued SYN requests. A higher value allows for more queued requests, improving performance.</td></tr><tr><td>net.ipv4.tcp_timestamps</td><td>0</td><td>Disables TCP timestamps, reducing overhead and improving performance.</td></tr><tr><td>vm.max_map_count</td><td>4,262,144</td><td>Increases the maximum number of memory map areas a process may have. The default is 65,530, which can be too low for workloads like MariaDB ColumnStore. Raising this prevents mapping errors for processes that need large address spaces.</td></tr><tr><td>kernel.pid_max</td><td>4,194,304</td><td>Defines the maximum process ID value. Older Linux versions defaulted to 32,768; newer versions default to 4,194,304. Raising this ensures support for systems running a very large number of processes concurrently.</td></tr><tr><td>kernel.threads-max</td><td>2,000,000</td><td>Specifies the maximum number of threads allowed on the system. The default varies depending on available RAM. A value of 2 million is suitable for systems with 32–64GB RAM. Increase further if running with more RAM or requiring more threads.</td></tr></tbody></table>

### Configuration Example

To configure these parameters, you can add them to the `/etc/sysctl.conf` file. For example:

```ini
vm.overcommit_memory=1 
vm.dirty_background_ratio=5 
vm.dirty_ratio=10 
vm.vfs_cache_pressure=50 
net.core.netdev_max_backlog=2500 
net.core.rmem_max=16777216 
net.core.wmem_max=16777216 
net.ipv4.tcp_max_syn_backlog=8192 
net.ipv4.tcp_timestamps=0
```

After making changes to the `/etc/sysctl.conf file`, you need to apply the changes by running the following command:

```bash
sudo sysctl -p
```

### Increase the Limit for Memory-Mapped Areas

```sql
cat /proc/sys/kernel/threads-max
cat /proc/sys/kernel/pid_max
cat /proc/sys/vm/max_map_count


# Rhel /etc/sysctl.conf
sudo echo "vm.max_map_count=4262144" >> /etc/sysctl.conf
sudo echo "kernel.pid_max = 4194304" >> /etc/sysctl.conf
sudo echo "kernel.threads-max = 2000000" >> /etc/sysctl.conf

# There may be a file called 50-pid-max.conf or perhaps something similar. If so, modify it 
sudo echo "vm.max_map_count=4262144" > /usr/lib/sysctl.d/50-max_map_count.conf
sudo echo "kernel.pid_max = 4194304" > /usr/lib/sysctl.d/50-pid-max.conf
sudo sysctl -p
```

### Common Use Cases

These optimized parameters are recommended for all MariaDB ColumnStore deployments, regardless of the specific workload. They can improve performance for various use cases, including:

* Large-scale data warehousing
* Real-time analytics
* Business intelligence
* Machine learning

### Related Links

* [MariaDB ColumnStore Documentation](../columnstore-quickstart-guides/mariadb-columnstore-guide.md)
* [Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/)
* [MCOL-5165: Add optimized Linux kernel parameters for MariaDB ColumnStore](https://jira.mariadb.org/browse/MCOL-5165)

### Conclusion

By optimizing the Linux kernel parameters, you can significantly improve the performance of your MariaDB ColumnStore deployments. These recommendations provide a starting point for optimizing your system, and you may need to adjust the values based on your specific hardware and workload.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
