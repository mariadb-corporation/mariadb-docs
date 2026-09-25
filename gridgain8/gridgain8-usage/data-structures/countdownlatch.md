---
description: >-
  IgniteCountDownLatch provides a distributed count-down latch that synchronizes operations across cluster nodes.
---

# CountDownLatch

`IgniteCountDownLatch` provides functionality that is similar to that of `java.util.concurrent.CountDownLatch` and allows you to synchronize operations across cluster nodes.

A distributed CountDownLatch can be created as follows:

```java
Ignite ignite = Ignition.start();

IgniteCountDownLatch latch = ignite.countDownLatch("latchName", // Latch name.
        10, // Initial count.
        false, // Auto remove, when counter has reached zero.
        true // Create if it does not exist.
);
```

After the above code is executed, all nodes in the specified cache will be able to synchronize on the latch named `latchName`.
Below is a code example of such synchronization:

```java
Ignite ignite = Ignition.start();

final IgniteCountDownLatch latch = ignite.countDownLatch("latchName", 10, false, true);

// Execute jobs.
for (int i = 0; i < 10; i++)
    // Execute a job on some remote cluster node.
    ignite.compute().run(() -> {
        int newCnt = latch.countDown();

        System.out.println("Counted down: newCnt=" + newCnt);
    });

// Wait for all jobs to complete.
latch.await();
latch.close();
```

{% hint style="info" %}
Remember to close the CountDownLatch after you are done with it to avoid keeping it in memory.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
