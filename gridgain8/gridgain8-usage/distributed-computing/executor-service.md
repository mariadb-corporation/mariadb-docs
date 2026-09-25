---
description: >-
  GridGain provides a distributed ExecutorService implementation that submits load-balanced tasks to the cluster's server nodes for execution.
---

# Executor Service

GridGain provides a distributed implementation of `java.util.concurrent.ExecutorService` that submits tasks to a cluster's server nodes for execution. The tasks are load balanced across the cluster nodes and are guaranteed to be executed as long as there is at least one node in the cluster.

An executor service can be obtained from an instance of `Ignite`:

```java
// Get cluster-enabled executor service.
ExecutorService exec = ignite.executorService();

// Iterate through all words in the sentence and create jobs.
for (final String word : "Print words using runnable".split(" ")) {
    // Execute runnable on some node.
    exec.submit(new IgniteRunnable() {
        @Override
        public void run() {
            System.out.println(">>> Printing '" + word + "' on this node from grid job.");
        }
    });
}
```

You can also limit the set of nodes available for the executor service by specifying a [cluster group](cluster-groups.md):

```java
// A group for nodes where the attribute 'worker' is defined.
ClusterGroup workerGrp = ignite.cluster().forAttribute("ROLE", "worker");

// Get an executor service for the cluster group.
ExecutorService exec = ignite.executorService(workerGrp);
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
