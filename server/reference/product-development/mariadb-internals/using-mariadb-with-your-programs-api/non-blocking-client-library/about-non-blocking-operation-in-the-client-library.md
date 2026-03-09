---
description: >-
  Explains the concepts behind non-blocking operations, which allow applications
  to process other tasks while waiting for database network I/O.
---

# Non-Blocking Operation in the Client Library

{% include "../../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

MariaDB supports _non-blocking_ operations in the client library. This allows an application to start a query or other operation against the database, and then continue to do other work (in the same thread) while the request is sent over the network, the query is processed in the server, and the result travels back. As parts of the result become ready, the application can — at its leisure — call back into the library to continue processing, repeating this until the operation is completed.

Non-blocking operation is implemented entirely within the client library. This means no special server support is necessary and non-blocking operation works with any version of the MariaDB or MySQL server, the same as the normal blocking API. It also means that it is not possible to have two queries running at the same time on the same connection (this is a protocol limitation). But a single thread can have any number of non-blocking queries running at the same time, each using its own MYSQL connection object.

Non-blocking operation is useful when an application needs to run a number of\
independent queries in parallel at the same time, to speed up operation compared to running them sequentially one after the other. This could be multiple queries against a single server (to better utilize multiple CPU cores and/or a high-capacity I/O system on the server), or it could be queries against multiple servers (e.g. [SHOW STATUS](../../../../sql-statements/administrative-sql-statements/show/show-status.md) against all running servers for monitoring, or a map/reduce-like operation against a big sharded database).

Non-blocking operation is also very useful in applications that are already written in a non-blocking style, for example using a framework like [libevent](https://libevent.org/), or, for example, a GUI-application using an event loop. Using the non-blocking client library allows the integrations of database queries into such applications, without the risk of long-running queries "hanging" the user interface or stalling the event loop, and without having to manually spawn separate threads to run the queries and re-synchronize\
with the threads to get the results back.

In this context, "blocking" means the situation where communication on the network socket to the server has to wait while processing the query. Waiting can be necessary because the server has not yet had time to process the query, or because the data needs to travel over the network from the server, or even because the first part of a large request needs to be sent out on the network before local socket buffers can accept the last part. Whenever such a wait is necessary, control returns to the application. The application will then run`select()` or `poll()` (or something similar) to detect when any wait condition is satisfied, and then call back into the library to continue processing.

An example program is available in the MariaDB source tree:

```bash
tests/async_queries.c
```

It uses `libevent` to run a set of queries in parallel from within a single thread / event loop. This is a good example of how to integrate non-blocking query processing into an event-based framework.

The non-blocking API in the client library is entirely optional. The new library is completely ABI- and source-compatible with existing applications. Also, applications not using non-blocking operations are not affected, nor is there any significant performance penalty for having support for non-blocking operations in the library for applications which do not use them.

The library internally uses co-routines, and requires a co-routine implementation to work. Native implementations are included for i386, amd64, and (since Connector/C version 3.3.12) aarch64 architectures. For other architectures, a fallback to `ucontext` is automatically used if available. An alternate fallback `boost::context` can also be used instead of `ucontext` by building with `-DWITH_BOOST_CONTEXT=ON` (`boost::context` is not used by default). If no co-routine implementation is available, the non-blocking operations are disabled and do not work.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
