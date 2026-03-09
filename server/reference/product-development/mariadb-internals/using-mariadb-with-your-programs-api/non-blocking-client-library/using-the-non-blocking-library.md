---
description: >-
  A practical guide on how to integrate and implement the non-blocking API
  within a C application to handle asynchronous database connections.
---

# Using the Non-Blocking Library

{% include "../../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

## Overview

The MariaDB non-blocking client API is modeled after the normal blocking library calls. This makes it easy to learn and remember. It makes it easier to translate code from using the blocking API to using the non-blocking API (or vice versa). And it also makes it simple to mix blocking and non-blocking calls in the same code path.

For every library call that may block on socket I/O, such as\
'`int mysql_real_query(MYSQL, query, query_length)`', two additional non-blocking calls are introduced:

```
int mysql_real_query_start(&status, MYSQL, query, query_length)
int mysql_real_query_cont(&status, MYSQL, wait_status)
```

To do non-blocking operation, an application first calls`mysql_real_query_start()` instead of `mysql_real_query()`, passing the same parameters.

If `mysql_real_query_start()` returns zero, then the operation completed without blocking, and 'status' is set to the value that would normally be returned from `mysql_real_query()`.

Else, the return value from `mysql_real_query_start()` is a bitmask of events that the library is waiting on. This can be `MYSQL_WAIT_READ`,`MYSQL_WAIT_WRITE`, or `MYSQL_WAIT_EXCEPT`, corresponding to the similar flags for `select()` or `poll()`; and it can include `MYSQL_WAIT_TIMEOUT` when waiting for a timeout to occur (e.g. a connection timeout).

In this case, the application continues other processing and eventually checks for the appropriate condition(s) to occur on the socket (or for timeout). When this occurs, the application can resume the operation by  calling `mysql_real_query_cont()`, passing in `'wait_status'` a bitmask of the events\
which actually occurred.

Just like `mysql_real_query_start()`, `mysql_real_query_cont()` returns zero when done, or a bitmask of events it needs to wait on. Thus the application continues to repeatedly call `mysql_real_query_cont()`, intermixed with other processing of its choice; until zero is returned, after which the result of the operation is stored in `'status'`.

Some calls, like `mysql_option()`, do not do any socket I/O, and so can never block. For these, there are no separate `_start()` or `_cont()` calls. See the "[Non-blocking API reference](non-blocking-api-reference.md)" page for a full list of what functions can and can not block.

The checking for events on the socket / timeout can be done with `select()` or `poll()` or a similar mechanism. Though often it will be done using a higher-level framework (such as libevent), which supplies facilities for registering and acting on such conditions.

The descriptor of the socket on which to check for events can be obtained by calling `mysql_get_socket()`. The duration of any timeout can be obtained from `mysql_get_timeout_value()`.

Here is a trivial (but full) example of running a query with the non-blocking API. The example is found in the MariaDB source tree as`client/async_example.c`. A larger, more realistic example using `libevent` is found as `tests/async_queries.c` in the source code:

```c
static void run_query(const char *host, const char *user, const char *password) {
  int err, status;
  MYSQL mysql, *ret;
  MYSQL_RES *res;
  MYSQL_ROW row;

  mysql_init(&mysql);
  mysql_options(&mysql, MYSQL_OPT_NONBLOCK, 0);

  status = mysql_real_connect_start(&ret, &mysql, host, user, password, NULL, 0, NULL, 0);
  while (status) {
    status = wait_for_mysql(&mysql, status);
    status = mysql_real_connect_cont(&ret, &mysql, status);
  }

  if (!ret)
    fatal(&mysql, "Failed to mysql_real_connect()");

  status = mysql_real_query_start(&err, &mysql, SL("SHOW STATUS"));
  while (status) {
    status = wait_for_mysql(&mysql, status);
    status = mysql_real_query_cont(&err, &mysql, status);
  }
  if (err)
    fatal(&mysql, "mysql_real_query() returns error");

  /* This method cannot block. */
  res= mysql_use_result(&mysql);
  if (!res)
    fatal(&mysql, "mysql_use_result() returns error");

  for (;;) {
    status= mysql_fetch_row_start(&row, res);
    while (status) {
      status= wait_for_mysql(&mysql, status);
      status= mysql_fetch_row_cont(&row, res, status);
    }
    if (!row)
      break;
    printf("%s: %s\n", row[0], row[1]);
  }
  if (mysql_errno(&mysql))
    fatal(&mysql, "Got error while retrieving rows");
  mysql_free_result(res);
  mysql_close(&mysql);
}

/* Helper function to do the waiting for events on the socket. */
static int wait_for_mysql(MYSQL *mysql, int status) {
  struct pollfd pfd;
  int timeout, res;

  pfd.fd = mysql_get_socket(mysql);
  pfd.events =
    (status & MYSQL_WAIT_READ ? POLLIN : 0) |
    (status & MYSQL_WAIT_WRITE ? POLLOUT : 0) |
    (status & MYSQL_WAIT_EXCEPT ? POLLPRI : 0);
  if (status & MYSQL_WAIT_TIMEOUT)
    timeout = 1000*mysql_get_timeout_value(mysql);
  else
    timeout = -1;
  res = poll(&pfd, 1, timeout);
  if (res == 0)
    return MYSQL_WAIT_TIMEOUT;
  else if (res < 0)
    return MYSQL_WAIT_TIMEOUT;
  else {
    int status = 0;
    if (pfd.revents & POLLIN) status |= MYSQL_WAIT_READ;
    if (pfd.revents & POLLOUT) status |= MYSQL_WAIT_WRITE;
    if (pfd.revents & POLLPRI) status |= MYSQL_WAIT_EXCEPT;
    return status;
  }
}
```

## Setting MYSQL\_OPT\_NONBLOCK

Before using any non-blocking operation, it is necessary to enable it first by setting the `MYSQL_OPT_NONBLOCK` option:

```c
mysql_options(&mysql, MYSQL_OPT_NONBLOCK, 0);
```

This call can be made at any time — typically it is done at the start, before `mysql_real_connect()`, but it can be done at any time to start using non-blocking operations.

If a non-blocking operation is attempted without setting the`MYSQL_OPT_NONBLOCK` option, the program will typically crash with a `NULL` pointer exception.

The argument for `MYSQL_OPT_NONBLOCK` is the size of the stack used to save the state of a non-blocking operation while it is waiting for I/O and the application is doing other processing. Normally, applications will not have to change this, and it can be passed as zero to use the default value.

## Mixing Blocking and Non-Blocking Operation

It is possible to freely mix blocking and non-blocking calls on the same `MYSQL` connection.

Thus, an application can do a normal blocking `mysql_real_connect()` and\
subsequently do a non-blocking `mysql_real_query_start()`. Or vice versa, do a non-blocking `mysql_real_connect_start()`, and later do a blocking `mysql_real_query()` on the resulting connection.

Mixing can be useful to allow code to use the simpler blocking API in parts of the program where waiting is not a problem. For example establishing the connection(s) at program startup, or doing small quick queries between large, long-running ones.

The only restriction is that any previous non-blocking operation must have finished before starting a new blocking (or non-blocking) operation, see the next section for more.

## Terminating a Non-Blocking Operation Early

When a non-blocking operation is started with `mysql_real_query_start()` or\
another `_start()` function, it must be allowed to finish before starting a new\
operation. Thus, the application must continue calling `mysql_real_query_cont()`\
until zero is returned, indicating that the operation is completed. It is not allowed to leave one operation "hanging" in the middle of processing and then start a new one on top of it.

It is, however, permissible to terminate the connection completely with `mysql_close()` in the middle of processing a non-blocking call. A new connection must then be initiated with `mysql_real_connect` before new queries can be run, either with a new `MYSQL` object or re-using the old one.

In the future, we may implement an abort facility to force an on-going operation to terminate as quickly as possible (but it will still be necessary to call `mysql_real_query_cont()` one last time after abort, allowing it to clean up the operation and return immediately with an appropriate error code).

## Restrictions

### DNS

When `mysql_real_connect_start()` is passed a hostname (as opposed to a local\
unix socket or an IP address, it may need to look up the hostname in DNS,\
depending on local host configuration (e.g. if the name is not in`/etc/hosts` or cached). Such DNS lookups do **not** happen in a non-blocking way. This means that `mysql_real_connect_start()` will not return control to the application while waiting for the DNS response. Thus the application may "hang" for some time if DNS is slow or non-functional.

If this is a problem, the application can pass an IP address to `mysql_real_connect_start()` instead of a hostname, which avoids the problem.\
The IP address can be obtained by the application with whatever non-blocking DNS loopup operation is available to it from the operating system or event framework used. Alternatively, a simple solution may be to just add the hostname to the local host lookup file (`/etc/hosts` on Posix/Unix/Linux machines).

### Windows Named Pipes and Shared Memory Connections

There is no support in the non-blocking API for connections using Windows named\
pipes or shared memory.

Named pipes and shared memory can still be used, using either the blocking or the non-blocking API. However, operations that need to wait on I/O on the named pipe do not return control to the application; instead they "hang", waiting for the operation to complete, just like the normal blocking API calls.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
