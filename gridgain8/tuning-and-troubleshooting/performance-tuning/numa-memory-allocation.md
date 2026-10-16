---
description: >-
  Enable NUMA-aware memory allocation in GridGain 8 so data regions optimize memory access patterns on multiprocessor Linux hardware for higher performance.
---

# How to Configure NUMA-Aware Memory Allocation

## Prerequisites

- A Linux system, such as [amd64 Linux](https://askubuntu.com/questions/601553/what-is-the-difference-between-x86-64-amd64-and-64-bit) (NUMA only works on Linux).
- A [HotSpot Java implementation](https://en.wikipedia.org/wiki/HotSpot_(virtual_machine)).
- [Hardware that supports NUMA](https://www.baeldung.com/linux/numa-test-support). If it does not, NUMA-aware memory allocation will not improve performance.

## Overview

This guide explains how to leverage the NUMA-aware memory allocation within the GridGain Unified Real-Time Data Platform. [NUMA](https://en.wikipedia.org/wiki/Non-uniform_memory_access) stands for "Non-Uniform Memory Access." It is a computer memory design used in multiprocessors, where the memory access time depends on the memory location relative to the processor. Using NUMA-aware allocation, applications running on GridGain can achieve higher performance as they optimize memory access patterns. Specific performance benefits depend on your environment, application load, and system resources.

## Step 1: Install the Required Packages

Make sure that your Linux system has `libnuma` and `numactl` installed. These packages are necessary for managing and configuring NUMA on your system. Use your system's package manager to install them:

{% tabs %}
{% tab title="Debian/Ubuntu-based systems" %}

```bash
sudo apt-get update
sudo apt-get install libnuma-dev numactl
```

{% endtab %}

{% tab title="Red Hat/CentOS systems" %}

```bash
sudo yum install numactl libnuma-devel
```

{% endtab %}

{% endtabs %}

## Step 2: Configure NUMA Nodes

While `libnuma` comes with a default configuration that works seamlessly with GridGain, you may need to tailor the NUMA nodes to your specific requirements for optimal performance. Use `numactl` to modify the configuration.

- To view your system's NUMA configuration:

  ```bash
  numactl --hardware
  ```

- To set a specific NUMA policy for an application, use `numactl` with the relevant options. For example, to bind a process to a specific node:

  ```bash
  numactl --cpunodebind=0 --membind=0 your_command
  ```

- Adjust node numbers based on your hardware configuration and requirements.

## Step 3: Enable the NUMA Allocator in GridGain

Enable the `ignite-numa-allocator` module that enables GridGain data regions to allocate memory using NUMA:

1. Navigate to your GridGain installation directory.
1. Move the `ignite-numa-allocator` module from the `libs/optional` directory to `libs`.

   ```bash
   mv libs/optional/ignite-numa-allocator libs/
   ```

## Step 4: Configure NUMA for Data Regions

To enable NUMA-aware allocation for a specific data region, adjust the `memoryAllocator` property in that region's `DataRegionConfiguration` in the GridGain configuration file (e.g., ignite.xml):

1. Open your GridGain configuration file in a text editor.
1. Locate the `DataRegionConfiguration` section.
1. Set the `memoryAllocator` property to one of the NUMA allocation strategies (see strategy descriptions below).

### Simple Allocation Strategy

This strategy is the best for attaching a data region to a specific NUMA node.

#### On all NUMA Nodes

```xml
<property name="dataStorageConfiguration">
    <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
        <property name="defaultDataRegionConfiguration">
            <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                <property name="name" value="Default_Region"/>
                ...
                <property name="memoryAllocator">
                    <bean class="org.apache.ignite.mem.NumaAllocator">
                        <constructor-arg>
                            <bean class="org.apache.ignite.mem.SimpleNumaAllocationStrategy"/>
                        </constructor-arg>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>
</property>
```

#### On a Specific Node

```xml
<property name="dataStorageConfiguration">
    ...
    <property name="memoryAllocator">
        <bean class="org.apache.ignite.mem.NumaAllocator">
            <constructor-arg>
                <bean class="org.apache.ignite.mem.SimpleNumaAllocationStrategy">
                    <constructor-arg name="node" value="0"/>
                </bean>
            </constructor-arg>
        </bean>
    </property>
    ...
</property>
```

### Interleaved Allocation Strategy

This strategy is optimal for distributing a data region across multiple NUMA nodes.

#### On all NUMA Nodes

```xml
<property name="dataStorageConfiguration">
    ...
    <property name="memoryAllocator">
        <bean class="org.apache.ignite.mem.NumaAllocator">
            <constructor-arg>
                <bean class="org.apache.ignite.mem.InterleavedNumaAllocationStrategy"/>
            </constructor-arg>
        </bean>
    </property>
    ...
</property>
```

#### On Specified NUMA Nodes

```xml
<property name="dataStorageConfiguration">
    ...
    <property name="memoryAllocator">
        <bean class="org.apache.ignite.mem.NumaAllocator">
            <constructor-arg>
                <bean class="org.apache.ignite.mem.InterleavedNumaAllocationStrategy">
                    <constructor-arg name="nodes">
                        <array>
                            <value>0</value>
                            <value>1</value>
                        </array>
                    </constructor-arg>
                </bean>
            </constructor-arg>
        </bean>
    </property>
    ...
</property>
```

### Local Node Allocation Strategy

This strategy is used for allocating on the local NUMA node of the process.

```xml
<property name="dataStorageConfiguration">
    ...
    <property name="memoryAllocator">
        <bean class="org.apache.ignite.mem.NumaAllocator">
            <constructor-arg>
                <bean class="org.apache.ignite.mem.LocalNumaAllocationStrategy"/>
            </constructor-arg>
        </bean>
    </property>
    ...
</property>
```

## Step 5: Enable NUMA-Aware Allocation in the JVM

To ensure the JVM itself is optimized for NUMA, use the `-XX:+UseNUMA` JVM option by setting the `JVM_OPTS` environment variable:

```bash
export JVM_OPTS="-XX:+UseNUMA"
```

## Step 6: Start a GridGain Node and Load Data

1. Start your GridGain node with the modified configuration:

   ```bash
   bin/ignite.sh path/to/your/ignite.xml
   ```

1. Using either a thick or a thin client, put some data into the data region you have configured for NUMA allocation to trigger the allocation.

## Step 7: Verify NUMA Allocation

To confirm that NUMA allocation is functioning correctly, inspect the `numa_maps` file for the GridGain node's process:

1. Find your GridGain node's process ID (PID).
1. Check the `numa_maps` file:

   ```bash
   grep libnuma_alloc /proc/YOUR_GRIDGAIN_NODE_PID/numa_maps
   ```

A non-empty list of pages allocated with NUMA means that your data region is now utilizing NUMA-aware memory allocation, which should enhance the performance of your GridGain deployments on NUMA-enabled systems.

## Related

- [Non-Uniform Memory Access (NUMA)](https://en.wikipedia.org/wiki/Non-uniform_memory_access) - Background on the memory design this guide optimizes for.
- [HotSpot (virtual machine)](https://en.wikipedia.org/wiki/HotSpot_(virtual_machine)) - The Java implementation required for `-XX:+UseNUMA`.
