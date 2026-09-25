---
description: >-
  GridGain's counting distributed semaphore restricts access to a resource or synchronizes execution flow cluster-wide.
---

# Semaphore

GridGain's counting distributed semaphore implementation and behavior is similar to the concept of a well-known `java.util.concurrent.Semaphore`. As any other semaphore it maintains a set of permits that are taken using `acquire()` method and released with `release()` counterpart allowing to restrict access to some logical or physical resource or synchronize execution flow. The only difference is that GridGain's semaphore empowers you to fulfill these kind of actions not only in boundaries of a single JVM but rather a cluster wide, across many remote nodes.

You can create a distributed semaphore as follows:

```java
Ignite ignite = Ignition.start();

IgniteSemaphore semaphore = ignite.semaphore("semName", // Distributed semaphore name.
        20, // Number of permits.
        true, // Release acquired permits if node, that owned them, left topology.
        true // Create if it doesn't exist.
);
```

Once the semaphore is created, it can be used concurrently by multiple cluster nodes in order to implement some distributed logic or restrict access to a distributed resource like in the following example:

```java
Ignite ignite = Ignition.start();

IgniteSemaphore semaphore = ignite.semaphore("semName", // Distributed semaphore name.
        20, // Number of permits.
        true, // Release acquired permits if node, that owned them, left topology.
        true // Create if it doesn't exist.
);

// Acquires a permit, blocking until it's available.
semaphore.acquire();

try {
    // Semaphore permit is acquired. Execute a distributed task.
    ignite.compute().run(() -> {
        System.out.println("Executed on:" + ignite.cluster().localNode().id());

        // Additional logic.
    });
} finally {
    // Releases a permit, returning it to the semaphore.
    semaphore.release();
    semaphore.close();
}
```

{% hint style="info" %}
Remember to close the semaphore after you are done with it to avoid keeping it in memory.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
