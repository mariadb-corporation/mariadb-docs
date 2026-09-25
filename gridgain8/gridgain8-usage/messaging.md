---
description: >-
  Topic-based, cluster-wide messaging in GridGain using the IgniteMessaging
  interface to publish and subscribe to messages.
---

# Topic-Based Messaging with GridGain

## Overview

GridGain distributed messaging enables topic-based cluster-wide communication between all nodes. Messages via a specified
message topic can be distributed to all or sub-group of nodes that have subscribed to that topic.

GridGain messaging is based on the publish-subscribe paradigm where publishers and subscribers are tethered together with
a common topic. When one of the nodes sends a message `A` for topic `T`, it is published on all nodes that have subscribed to `T`.

{% hint style="info" %}
Any new node joining the cluster automatically gets subscribed to all the topics that other nodes in the cluster
(or [cluster group](distributed-computing/cluster-groups.md)) are subscribed to.
{% endhint %}

## IgniteMessaging

Distributed messaging functionality in GridGain is available via the `IgniteMessaging` interface. You can get an instance
of `IgniteMessaging` like so:

{% code title="Java" %}
```java
Ignite ignite = Ignition.ignite();

// Messaging instance over this cluster.
IgniteMessaging msg = ignite.message();

// Messaging instance over given cluster group (in this case, remote nodes).
IgniteMessaging rmtMsg = ignite.message(ignite.cluster().forRemotes());
```
{% endcode %}

## Publish Messages

Send methods help sending/publishing messages with a specified message topic to all nodes. Messages can be sent
in _ordered_ or _unordered_ manner.

### Ordered Messages

The `sendOrdered(...)` method can be used if you want to receive messages in the order they were sent. The timeout parameter
is passed to specify how long a message will stay in the queue to wait for messages that are supposed to be sent before
this message. If the timeout expires, then all the messages that have not yet arrived for a given topic on that node will be ignored.

### Unordered Messages

The `send(...)` methods do not guarantee message ordering. This means that, when you sequentially send message `A` and
message `B`, you are not guaranteed that the target node first receives `A` and then `B`.

## Subscribe for Messages

Listen methods help to listen/subscribe for messages. When these methods are called, a listener with specified message
topic is registered on  all (or sub-group of ) nodes to listen for new messages. With listen methods, a predicate is
passed that returns a boolean value which tells the listener to continue or stop listening for new messages.

### Local Listen

The `localListen(...)` method registers a message listener with specified topic only on the local node and listens for
messages from any node in the _given_ cluster group.

### Remote Listen

The `remoteListen(...)` method registers message listeners with specified topic on all nodes in the _given_ cluster group
and listens for messages from any node in _this_ cluster group.

## Example

{% code title="Java" %}
```java
Ignite ignite = Ignition.ignite();

IgniteMessaging rmtMsg = ignite.message(ignite.cluster().forRemotes());

// Add listener for ordered messages on all remote nodes.
rmtMsg.remoteListen("MyOrderedTopic", (nodeId, msg) -> {
    System.out.println("Received ordered message [msg=" + msg + ", from=" + nodeId + ']');

    return true; // Return true to continue listening.
});

// Send ordered messages to remote nodes.
for (int i = 0; i < 10; i++)
    rmtMsg.sendOrdered("MyOrderedTopic", Integer.toString(i),0);
```
{% endcode %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
