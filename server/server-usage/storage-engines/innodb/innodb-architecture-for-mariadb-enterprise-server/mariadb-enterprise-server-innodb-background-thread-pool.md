---
description: >-
  This page details the dedicated thread pool in MariaDB Enterprise Server that
  manages InnoDB background tasks, improving scalability and performance.
---

# MariaDB Enterprise Server InnoDB Background Thread Pool

## Overview

Starting with MariaDB Enterprise Server 10.5 and MariaDB Community Server 10.5, InnoDB uses the InnoDB Background Thread Pool to perform internal operations in the background. In previous versions, the internal operations were performed by dedicated threads. By using the InnoDB Background Thread Pool instead of many dedicated threads, InnoDB can reduce context switching and use system resources more effectively.

The InnoDB Background Thread Pool performs internal operations in multiple categories: **tasks**, **timers**, and **asynchronous I/O**.

**Tasks** are used to perform internal operations that are triggered by some event. In ES 10.5 and later and CS 10.5 and later, the following threads have been replaced by **tasks** with the InnoDB Background Thread Pool:

* The InnoDB Buffer Pool Resize Thread
* The InnoDB Buffer Pool Dump Thread
* The InnoDB Full-Text Search (FTS) Optimization Thread

**Timers** are used to perform internal operations that are triggered periodically. In ES 10.5 and later and CS 10.5 and later, the following threads have been replaced by **timers** with the InnoDB Background Thread Pool:

* The InnoDB Master Thread
* The InnoDB Defragmentation Thread
* The InnoDB Monitor Thread
* The InnoDB Error Monitor Thread

**Asynchronous I/O** is used to read from and write to disk asynchronously. In ES 10.5 and later and CS 10.5 and later, the following threads have been replaced by **asynchronous I/O** with the InnoDB Background Thread Pool:

* The [InnoDB I/O Threads](mariadb-enterprise-server-innodb-io-threads.md)

## Feature Summary

| Feature        | Detail                              | Resources                                                                                           |
| -------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------- |
| Thread Pool    | InnoDB Background Thread Pool       |                                                                                                     |
| Storage Engine | InnoDB                              |                                                                                                     |
| Purpose        | Handles background tasks for InnoDB |                                                                                                     |
| Availability   | • ES 10.5+ • CS 10.5+               | [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/) |

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
