---
description: >-
  Using Control Center to diagnose data skew when one cluster node shows high
  CPU usage.
---

# Dealing with Data Skew with Control Center

You may encounter issues with clusters allocating data to each other constantly. In this topic we will show how to debug the issue when you notice high CPU usage with Control Center.

In this example we will look at a 4-node cluster, an application that runs read operations, and Control Center displays an alert about high CPU usage.

In Control Center dashboards you can see that one of the nodes is using a lot of CPU.

One of the possible reasons is incorrect data distribution. This can be checked in the **Caches** screen. The **Partition Distribution** screen contains information about partitions and keys on each node.

If everything is fine, you should look into the number of operations performed at each node. If, for example, one of the caches has a lot of operations performed on a single node, the problem is localized. In this case it is likely to be what is known as **Celebrity Users** problem. For example, a company is much bigger than others and has a lot more operations related to it.

Yet another possible issue is in cache configuration options, available from the **Caches** screen. Check the `readFromBackup` parameter. If it is set to `false`, GridGain always tries to read data from the cache, and this can cause a lot of load. If you have this parameter disabled, you will always read the latest update, but at a cost of repeated read requests. Set the parameter to `true` and recreate the cache.
