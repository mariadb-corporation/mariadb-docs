---
description: >-
  Use GridGain distributed reentrant locks to lock threads across the cluster, with optional failover safety and fair or non-fair ordering.
---

# Locks

You can use distributed reentry locks to lock threads for specific purposes.

## Creating Distributed Lock

To create a lock object, use the `ignite.reentrantLock()` method. The method has the following parameters:

- name - The name of the lock.
- failoverSafe - If `true`, the lock will be protected from failover.
- fair - If `true`, a `fair` lock will be created.
- create - If true, a data structure will be created if it does not exist.

After you have the IgniteLock object, you can lock the thread by using the `lock()` method, release it with `unlock()` method and then close it with a `close()` method.

```java
IgniteLock lock = ignite.reentrantLock("lockName", false, false, true);
lock.lock();
try{
 // ...
}
finally {
 lock.unlock();
 lock.close();
}
```

{% hint style="info" %}
Remember to close the lock after you are done with it to avoid keeping it in memory.
{% endhint %}

## Protection From Failover

Ignite locks can automatically recover from node failure, depending on the `failoverSafe` flag.

- If `failoverSafe` flag is set to `true`, in case a node owning the lock fails, lock will be automatically released and become available for threads on other nodes to acquire. No exception will be thrown.
- If `failoverSafe` flag is set to `false`, in case a node owning the lock fails, IgniteException will be thrown on every other attempt to perform any operation on this lock. No automatic recovery will be attempted, and lock will be marked as broken (i.e. unusable). You can check if the lock is broken by using the `#isBroken()` method. Broken lock cannot be reused again.

## Fair and Non-fair locks

GridGain can handle two types of locks: fair and non-fair.

- Non-fair lock assumes no ordering should be imposed on acquiring threads; in case of contention, threads from all nodes compete for the lock once the lock is released. In most cases this is the desired behaviour. However, in some cases, using the non-fair lock can lead to uneven load distribution among nodes.
- Fair lock imposes a strict FIFO ordering policy at a cost of an additional transaction. This ordering does not guarantee fairness of thread scheduling. Thus, one of many threads on any node using a fair lock may obtain it multiple times in succession while other active threads are not progressing and not currently holding the lock.

{% hint style="info" %}
The untimed `tryLock` method does not honor the fairness setting. It will succeed if the lock is available even if other threads are waiting.
{% endhint %}

As a rule of thumb, whenever there is a reasonable time window between successive calls to release and acquire the lock, non-fair lock should be preferred:

```java
while(someCondition){
  // do anything
  lock.lock();
  try{
      // ...
  }
  finally {
      lock.unlock();
      lock.close();
  }
}
```

If successive calls to release/acquire can happen close to each other, using the fair lock is reasonable in order to allow even distribution of load among nodes (although overall throughput may be lower due to increased overhead).

```java
while(someCondition){
  lock.lock();
  try {
      // do something
  }
  finally {
      lock.unlock();
      lock.close();
  }
}
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
