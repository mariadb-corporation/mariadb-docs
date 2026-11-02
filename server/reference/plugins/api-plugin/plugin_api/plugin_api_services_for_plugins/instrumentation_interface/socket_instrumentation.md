---
description: >-
  The MYSQL_SOCKET structure and the mysql_socket_* wrappers for creating,
  connecting, sending, receiving, and closing sockets with Performance Schema
  instrumentation.
---

# Socket Instrumentation

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Classes

| Name                                                           | Description             |
| -------------------------------------------------------------- | ----------------------- |
| [`st_mysql_socket`](socket_instrumentation.md#st_mysql_socket) | An instrumented socket. |

## Macros

| Name                                                                                   | Description                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`SOCKBUF_T`](socket_instrumentation.md#sockbuf_t)                                     |                                                                                                                                                                                                                          |
| [`PSI_SOCKET_CALL`](socket_instrumentation.md#psi_socket_call)                         |                                                                                                                                                                                                                          |
| [`mysql_socket_register`](socket_instrumentation.md#mysql_socket_register)             | Socket registration.                                                                                                                                                                                                     |
| [`MYSQL_INVALID_SOCKET`](socket_instrumentation.md#mysql_invalid_socket)               | MYSQL\_SOCKET initial value.                                                                                                                                                                                             |
| [`MYSQL_SOCKET_WAIT_VARIABLES`](socket_instrumentation.md#mysql_socket_wait_variables) | Instrumentation helper for socket waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: [MYSQL\_START\_SOCKET\_WAIT](socket_instrumentation.md#mysql_start_socket_wait). |
| [`MYSQL_START_SOCKET_WAIT`](socket_instrumentation.md#mysql_start_socket_wait)         | Instrumentation helper for socket waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL\_END\_SOCKET\_WAIT](socket_instrumentation.md#mysql_end_socket_wait).                                |
| [`MYSQL_END_SOCKET_WAIT`](socket_instrumentation.md#mysql_end_socket_wait)             | Instrumentation helper for socket waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL\_START\_SOCKET\_WAIT](socket_instrumentation.md#mysql_start_socket_wait).                              |
| [`MYSQL_SOCKET_SET_STATE`](socket_instrumentation.md#mysql_socket_set_state)           | Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI\_socket\_state                                                                                                                                 |
| [`mysql_socket_fd`](socket_instrumentation.md#mysql_socket_fd)                         | Create a socket. `mysql_socket_fd` is a replacement for `socket`.                                                                                                                                                        |
| [`mysql_socket_socket`](socket_instrumentation.md#mysql_socket_socket)                 | Create a socket. `mysql_socket_socket` is a replacement for `socket`.                                                                                                                                                    |
| [`mysql_socket_bind`](socket_instrumentation.md#mysql_socket_bind)                     | Bind a socket to a local port number and IP address `mysql_socket_bind` is a replacement for `bind`.                                                                                                                     |
| [`mysql_socket_getsockname`](socket_instrumentation.md#mysql_socket_getsockname)       | Return port number and IP address of the local host `mysql_socket_getsockname` is a replacement for `getsockname`.                                                                                                       |
| [`mysql_socket_connect`](socket_instrumentation.md#mysql_socket_connect)               | Establish a connection to a remote host. `mysql_socket_connect` is a replacement for `connect`.                                                                                                                          |
| [`mysql_socket_getpeername`](socket_instrumentation.md#mysql_socket_getpeername)       | Get port number and IP address of remote host that a socket is connected to. `mysql_socket_getpeername` is a replacement for `getpeername`.                                                                              |
| [`mysql_socket_send`](socket_instrumentation.md#mysql_socket_send)                     | Send data from the buffer, B, to a connected socket. `mysql_socket_send` is a replacement for `send`.                                                                                                                    |
| [`mysql_socket_recv`](socket_instrumentation.md#mysql_socket_recv)                     | Receive data from a connected socket. `mysql_socket_recv` is a replacement for `recv`.                                                                                                                                   |
| [`mysql_socket_sendto`](socket_instrumentation.md#mysql_socket_sendto)                 | Send data to a socket at the specified address. `mysql_socket_sendto` is a replacement for `sendto`.                                                                                                                     |
| [`mysql_socket_recvfrom`](socket_instrumentation.md#mysql_socket_recvfrom)             | Receive data from a socket and return source address information `mysql_socket_recvfrom` is a replacement for `recvfrom`.                                                                                                |
| [`mysql_socket_getsockopt`](socket_instrumentation.md#mysql_socket_getsockopt)         | Get a socket option for the specified socket. `mysql_socket_getsockopt` is a replacement for `getsockopt`.                                                                                                               |
| [`mysql_socket_setsockopt`](socket_instrumentation.md#mysql_socket_setsockopt)         | Set a socket option for the specified socket. `mysql_socket_setsockopt` is a replacement for `setsockopt`.                                                                                                               |
| [`mysql_sock_set_nonblocking`](socket_instrumentation.md#mysql_sock_set_nonblocking)   | Set socket to non-blocking.                                                                                                                                                                                              |
| [`mysql_socket_listen`](socket_instrumentation.md#mysql_socket_listen)                 | Set socket state to listen for an incoming connection. `mysql_socket_listen` is a replacement for `listen`.                                                                                                              |
| [`mysql_socket_accept`](socket_instrumentation.md#mysql_socket_accept)                 | Accept a connection from any remote host; TCP only. `mysql_socket_accept` is a replacement for `accept`.                                                                                                                 |
| [`mysql_socket_close`](socket_instrumentation.md#mysql_socket_close)                   | Close a socket and sever any connections. `mysql_socket_close` is a replacement for `close`.                                                                                                                             |
| [`mysql_socket_shutdown`](socket_instrumentation.md#mysql_socket_shutdown)             | Disable receives and/or sends on a socket. `mysql_socket_shutdown` is a replacement for `shutdown`.                                                                                                                      |

***

### SOCKBUF\_T

```cpp
#define SOCKBUF_T void
```

Defined in psi/mysql\_socket.h:53

***

### PSI\_SOCKET\_CALL

```cpp
#define PSI_SOCKET_CALL(M, M) PSI_DYNAMIC_CALL(M)
```

Defined in psi/mysql\_socket.h:59

***

### mysql\_socket\_register

```cpp
#define mysql_socket_register(P1, P2, P3, P1, P2, P3) inline_mysql_socket_register(P1, P2, P3)
```

Defined in psi/mysql\_socket.h:67

Socket registration.

***

### MYSQL\_INVALID\_SOCKET

```cpp
#define MYSQL_INVALID_SOCKET mysql_socket_invalid()
```

Defined in psi/mysql\_socket.h:109

MYSQL\_SOCKET initial value.

***

### MYSQL\_SOCKET\_WAIT\_VARIABLES

```cpp
#define MYSQL_SOCKET_WAIT_VARIABLES(LOCKER, STATE, LOCKER, STATE) struct PSI_socket_locker* LOCKER; \
    PSI_socket_locker_state STATE;
```

Defined in psi/mysql\_socket.h:204

Instrumentation helper for socket waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: [MYSQL\_START\_SOCKET\_WAIT](socket_instrumentation.md#mysql_start_socket_wait).

**See also**: [MYSQL\_END\_SOCKET\_WAIT](socket_instrumentation.md#mysql_end_socket_wait).

#### Parameters

| Parameter | Type | Description  |
| --------- | ---- | ------------ |
| `LOCKER`  |      | locker       |
| `STATE`   |      | locker state |
| `LOCKER`  |      | locker       |
| `STATE`   |      | locker state |

***

### MYSQL\_START\_SOCKET\_WAIT

```cpp
#define MYSQL_START_SOCKET_WAIT(LOCKER, STATE, SOCKET, OP, COUNT, LOCKER, STATE, SOCKET, OP, COUNT) LOCKER= inline_mysql_start_socket_wait(STATE, SOCKET, OP, COUNT,\
                                           __FILE__, __LINE__)
```

Defined in psi/mysql\_socket.h:223

Instrumentation helper for socket waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL\_END\_SOCKET\_WAIT](socket_instrumentation.md#mysql_end_socket_wait).

#### Parameters

| Parameter | Type | Description                          |
| --------- | ---- | ------------------------------------ |
| `LOCKER`  |      | locker                               |
| `STATE`   |      | locker state                         |
| `SOCKET`  |      | instrumented socket                  |
| `OP`      |      | The socket operation to be performed |
| `COUNT`   |      | bytes to be written/read             |
| `LOCKER`  |      | locker                               |
| `STATE`   |      | locker state                         |
| `SOCKET`  |      | instrumented socket                  |
| `OP`      |      | The socket operation to be performed |
| `COUNT`   |      | bytes to be written/read             |

***

### MYSQL\_END\_SOCKET\_WAIT

```cpp
#define MYSQL_END_SOCKET_WAIT(LOCKER, COUNT, LOCKER, COUNT) inline_mysql_end_socket_wait(LOCKER, COUNT)
```

Defined in psi/mysql\_socket.h:240

Instrumentation helper for socket waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL\_START\_SOCKET\_WAIT](socket_instrumentation.md#mysql_start_socket_wait).

#### Parameters

| Parameter | Type | Description                      |
| --------- | ---- | -------------------------------- |
| `LOCKER`  |      | locker                           |
| `COUNT`   |      | actual bytes written/read, or -1 |
| `LOCKER`  |      | locker                           |
| `COUNT`   |      | actual bytes written/read, or -1 |

***

### MYSQL\_SOCKET\_SET\_STATE

```cpp
#define MYSQL_SOCKET_SET_STATE(SOCKET, STATE, SOCKET, STATE) inline_mysql_socket_set_state(SOCKET, STATE)
```

Defined in psi/mysql\_socket.h:255

Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI\_socket\_state

#### Parameters

| Parameter | Type | Description             |
| --------- | ---- | ----------------------- |
| `SOCKET`  |      | the instrumented socket |
| `STATE`   |      | the new state           |
| `SOCKET`  |      | the instrumented socket |
| `STATE`   |      | the new state           |

***

### mysql\_socket\_fd

```cpp
#define mysql_socket_fd(K, F, K, F) inline_mysql_socket_fd(K, F)
```

Defined in psi/mysql\_socket.h:319

Create a socket. `mysql_socket_fd` is a replacement for `socket`.

#### Parameters

| Parameter | Type | Description                                   |
| --------- | ---- | --------------------------------------------- |
| `K`       |      | PSI\_socket\_key for this instrumented socket |
| `F`       |      | File descriptor                               |
| `K`       |      | PSI\_socket\_key for this instrumented socket |
| `F`       |      | File descriptor                               |

***

### mysql\_socket\_socket

```cpp
#define mysql_socket_socket(K, D, T, P, K, D, T, P) inline_mysql_socket_socket(K, D, T, P)
```

Defined in psi/mysql\_socket.h:337

Create a socket. `mysql_socket_socket` is a replacement for `socket`.

#### Parameters

| Parameter | Type | Description                                   |
| --------- | ---- | --------------------------------------------- |
| `K`       |      | PSI\_socket\_key for this instrumented socket |
| `D`       |      | Socket domain                                 |
| `T`       |      | Protocol type                                 |
| `P`       |      | Transport protocol                            |
| `K`       |      | PSI\_socket\_key for this instrumented socket |
| `D`       |      | Socket domain                                 |
| `T`       |      | Protocol type                                 |
| `P`       |      | Transport protocol                            |

***

### mysql\_socket\_bind

```cpp
#define mysql_socket_bind(FD, AP, L, FD, AP, L) inline_mysql_socket_bind(__FILE__, __LINE__, FD, AP, L)
```

Defined in psi/mysql\_socket.h:353

Bind a socket to a local port number and IP address `mysql_socket_bind` is a replacement for `bind`.

#### Parameters

| Parameter | Type | Description                                                       |
| --------- | ---- | ----------------------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket()               |
| `AP`      |      | Pointer to local port number and IP address in sockaddr structure |
| `L`       |      | Length of sockaddr structure                                      |
| `FD`      |      | Instrumented socket descriptor returned by socket()               |
| `AP`      |      | Pointer to local port number and IP address in sockaddr structure |
| `L`       |      | Length of sockaddr structure                                      |

***

### mysql\_socket\_getsockname

```cpp
#define mysql_socket_getsockname(FD, AP, LP, FD, AP, LP) inline_mysql_socket_getsockname(__FILE__, __LINE__, FD, AP, LP)
```

Defined in psi/mysql\_socket.h:369

Return port number and IP address of the local host `mysql_socket_getsockname` is a replacement for `getsockname`.

#### Parameters

| Parameter | Type | Description                                                       |
| --------- | ---- | ----------------------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket()               |
| `AP`      |      | Pointer to returned address of local host in `sockaddr` structure |
| `LP`      |      | Pointer to length of `sockaddr` structure                         |
| `FD`      |      | Instrumented socket descriptor returned by socket()               |
| `AP`      |      | Pointer to returned address of local host in `sockaddr` structure |
| `LP`      |      | Pointer to length of `sockaddr` structure                         |

***

### mysql\_socket\_connect

```cpp
#define mysql_socket_connect(FD, AP, L, FD, AP, L) inline_mysql_socket_connect(__FILE__, __LINE__, FD, AP, L)
```

Defined in psi/mysql\_socket.h:385

Establish a connection to a remote host. `mysql_socket_connect` is a replacement for `connect`.

#### Parameters

| Parameter | Type | Description                                         |
| --------- | ---- | --------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket() |
| `AP`      |      | Pointer to target address in sockaddr structure     |
| `L`       |      | Length of sockaddr structure                        |
| `FD`      |      | Instrumented socket descriptor returned by socket() |
| `AP`      |      | Pointer to target address in sockaddr structure     |
| `L`       |      | Length of sockaddr structure                        |

***

### mysql\_socket\_getpeername

```cpp
#define mysql_socket_getpeername(FD, AP, LP, FD, AP, LP) inline_mysql_socket_getpeername(__FILE__, __LINE__, FD, AP, LP)
```

Defined in psi/mysql\_socket.h:401

Get port number and IP address of remote host that a socket is connected to. `mysql_socket_getpeername` is a replacement for `getpeername`.

#### Parameters

| Parameter | Type | Description                                                      |
| --------- | ---- | ---------------------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept()  |
| `AP`      |      | Pointer to returned address of remote host in sockaddr structure |
| `LP`      |      | Pointer to length of sockaddr structure                          |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept()  |
| `AP`      |      | Pointer to returned address of remote host in sockaddr structure |
| `LP`      |      | Pointer to length of sockaddr structure                          |

***

### mysql\_socket\_send

```cpp
#define mysql_socket_send(FD, B, N, FL, FD, B, N, FL) inline_mysql_socket_send(__FILE__, __LINE__, FD, B, N, FL)
```

Defined in psi/mysql\_socket.h:418

Send data from the buffer, B, to a connected socket. `mysql_socket_send` is a replacement for `send`.

#### Parameters

| Parameter | Type | Description                                                     |
| --------- | ---- | --------------------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept() |
| `B`       |      | Buffer to send                                                  |
| `N`       |      | Number of bytes to send                                         |
| `FL`      |      | Control flags                                                   |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept() |
| `B`       |      | Buffer to send                                                  |
| `N`       |      | Number of bytes to send                                         |
| `FL`      |      | Control flags                                                   |

***

### mysql\_socket\_recv

```cpp
#define mysql_socket_recv(FD, B, N, FL, FD, B, N, FL) inline_mysql_socket_recv(__FILE__, __LINE__, FD, B, N, FL)
```

Defined in psi/mysql\_socket.h:435

Receive data from a connected socket. `mysql_socket_recv` is a replacement for `recv`.

#### Parameters

| Parameter | Type | Description                                                     |
| --------- | ---- | --------------------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept() |
| `B`       |      | Buffer to receive to                                            |
| `N`       |      | Maximum bytes to receive                                        |
| `FL`      |      | Control flags                                                   |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept() |
| `B`       |      | Buffer to receive to                                            |
| `N`       |      | Maximum bytes to receive                                        |
| `FL`      |      | Control flags                                                   |

***

### mysql\_socket\_sendto

```cpp
#define mysql_socket_sendto(FD, B, N, FL, AP, L, FD, B, N, FL, AP, L) inline_mysql_socket_sendto(__FILE__, __LINE__, FD, B, N, FL, AP, L)
```

Defined in psi/mysql\_socket.h:454

Send data to a socket at the specified address. `mysql_socket_sendto` is a replacement for `sendto`.

#### Parameters

| Parameter | Type | Description                                         |
| --------- | ---- | --------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket() |
| `B`       |      | Buffer to send                                      |
| `N`       |      | Number of bytes to send                             |
| `FL`      |      | Control flags                                       |
| `AP`      |      | Pointer to destination sockaddr structure           |
| `L`       |      | Size of sockaddr structure                          |
| `FD`      |      | Instrumented socket descriptor returned by socket() |
| `B`       |      | Buffer to send                                      |
| `N`       |      | Number of bytes to send                             |
| `FL`      |      | Control flags                                       |
| `AP`      |      | Pointer to destination sockaddr structure           |
| `L`       |      | Size of sockaddr structure                          |

***

### mysql\_socket\_recvfrom

```cpp
#define mysql_socket_recvfrom(FD, B, N, FL, AP, LP, FD, B, N, FL, AP, LP) inline_mysql_socket_recvfrom(__FILE__, __LINE__, FD, B, N, FL, AP, LP)
```

Defined in psi/mysql\_socket.h:473

Receive data from a socket and return source address information `mysql_socket_recvfrom` is a replacement for `recvfrom`.

#### Parameters

| Parameter | Type | Description                                              |
| --------- | ---- | -------------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket()      |
| `B`       |      | Buffer to receive to                                     |
| `N`       |      | Maximum bytes to receive                                 |
| `FL`      |      | Control flags                                            |
| `AP`      |      | Pointer to source address in sockaddr\_storage structure |
| `LP`      |      | Size of sockaddr\_storage structure                      |
| `FD`      |      | Instrumented socket descriptor returned by socket()      |
| `B`       |      | Buffer to receive to                                     |
| `N`       |      | Maximum bytes to receive                                 |
| `FL`      |      | Control flags                                            |
| `AP`      |      | Pointer to source address in sockaddr\_storage structure |
| `LP`      |      | Size of sockaddr\_storage structure                      |

***

### mysql\_socket\_getsockopt

```cpp
#define mysql_socket_getsockopt(FD, LV, ON, OP, OL, FD, LV, ON, OP, OL) inline_mysql_socket_getsockopt(__FILE__, __LINE__, FD, LV, ON, OP, OL)
```

Defined in psi/mysql\_socket.h:491

Get a socket option for the specified socket. `mysql_socket_getsockopt` is a replacement for `getsockopt`.

#### Parameters

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| `FD`      |      | Instrumented socket descriptor returned by socket()          |
| `LV`      |      | Protocol level                                               |
| `ON`      |      | Option to query                                              |
| `OP`      |      | Buffer which will contain the value for the requested option |
| `OL`      |      | Pointer to length of OP                                      |
| `FD`      |      | Instrumented socket descriptor returned by socket()          |
| `LV`      |      | Protocol level                                               |
| `ON`      |      | Option to query                                              |
| `OP`      |      | Buffer which will contain the value for the requested option |
| `OL`      |      | Pointer to length of OP                                      |

***

### mysql\_socket\_setsockopt

```cpp
#define mysql_socket_setsockopt(FD, LV, ON, OP, OL, FD, LV, ON, OP, OL) inline_mysql_socket_setsockopt(__FILE__, __LINE__, FD, LV, ON, OP, OL)
```

Defined in psi/mysql\_socket.h:509

Set a socket option for the specified socket. `mysql_socket_setsockopt` is a replacement for `setsockopt`.

#### Parameters

| Parameter | Type | Description                                          |
| --------- | ---- | ---------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket()  |
| `LV`      |      | Protocol level                                       |
| `ON`      |      | Option to modify                                     |
| `OP`      |      | Buffer containing the value for the specified option |
| `OL`      |      | Pointer to length of OP                              |
| `FD`      |      | Instrumented socket descriptor returned by socket()  |
| `LV`      |      | Protocol level                                       |
| `ON`      |      | Option to modify                                     |
| `OP`      |      | Buffer containing the value for the specified option |
| `OL`      |      | Pointer to length of OP                              |

***

### mysql\_sock\_set\_nonblocking

```cpp
#define mysql_sock_set_nonblocking(FD, FD) inline_mysql_sock_set_nonblocking(__FILE__, __LINE__, FD)
```

Defined in psi/mysql\_socket.h:522

Set socket to non-blocking.

#### Parameters

| Parameter | Type | Description                    |
| --------- | ---- | ------------------------------ |
| `FD`      |      | instrumented socket descriptor |
| `FD`      |      | instrumented socket descriptor |

***

### mysql\_socket\_listen

```cpp
#define mysql_socket_listen(FD, N, FD, N) inline_mysql_socket_listen(__FILE__, __LINE__, FD, N)
```

Defined in psi/mysql\_socket.h:537

Set socket state to listen for an incoming connection. `mysql_socket_listen` is a replacement for `listen`.

#### Parameters

| Parameter | Type | Description                                         |
| --------- | ---- | --------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor, bound and connected |
| `N`       |      | Maximum number of pending connections allowed.      |
| `FD`      |      | Instrumented socket descriptor, bound and connected |
| `N`       |      | Maximum number of pending connections allowed.      |

***

### mysql\_socket\_accept

```cpp
#define mysql_socket_accept(K, FD, AP, LP, K, FD, AP, LP) inline_mysql_socket_accept(__FILE__, __LINE__, K, FD, AP, LP)
```

Defined in psi/mysql\_socket.h:554

Accept a connection from any remote host; TCP only. `mysql_socket_accept` is a replacement for `accept`.

#### Parameters

| Parameter | Type | Description                                                                       |
| --------- | ---- | --------------------------------------------------------------------------------- |
| `K`       |      | PSI\_socket\_key for this instrumented socket                                     |
| `FD`      |      | Instrumented socket descriptor, bound and placed in a listen state                |
| `AP`      |      | Pointer to sockaddr structure with returned IP address and port of connected host |
| `LP`      |      | Pointer to length of valid information in AP                                      |
| `K`       |      | PSI\_socket\_key for this instrumented socket                                     |
| `FD`      |      | Instrumented socket descriptor, bound and placed in a listen state                |
| `AP`      |      | Pointer to sockaddr structure with returned IP address and port of connected host |
| `LP`      |      | Pointer to length of valid information in AP                                      |

***

### mysql\_socket\_close

```cpp
#define mysql_socket_close(FD, FD) inline_mysql_socket_close(__FILE__, __LINE__, FD)
```

Defined in psi/mysql\_socket.h:568

Close a socket and sever any connections. `mysql_socket_close` is a replacement for `close`.

#### Parameters

| Parameter | Type | Description                                                     |
| --------- | ---- | --------------------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept() |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept() |

***

### mysql\_socket\_shutdown

```cpp
#define mysql_socket_shutdown(FD, H, FD, H) inline_mysql_socket_shutdown(__FILE__, __LINE__, FD, H)
```

Defined in psi/mysql\_socket.h:583

Disable receives and/or sends on a socket. `mysql_socket_shutdown` is a replacement for `shutdown`.

#### Parameters

| Parameter | Type | Description                                                     |
| --------- | ---- | --------------------------------------------------------------- |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept() |
| `H`       |      | Specifies which operations to shutdown                          |
| `FD`      |      | Instrumented socket descriptor returned by socket() or accept() |
| `H`       |      | Specifies which operations to shutdown                          |

## Typedefs

| Return                                                                | Name                                                     | Description                                                              |
| --------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------ |
| struct [`st_mysql_socket`](socket_instrumentation.md#st_mysql_socket) | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | An instrumented socket. `MYSQL_SOCKET` is a replacement for `my_socket`. |

***

### MYSQL\_SOCKET

```cpp
using MYSQL_SOCKET = struct st_mysql_socket
```

Type: struct [`st_mysql_socket`](socket_instrumentation.md#st_mysql_socket)

Defined in psi/mysql\_socket.h:101

An instrumented socket. `MYSQL_SOCKET` is a replacement for `my_socket`.

## Functions

| Return                                                   | Name                                                                                                                 | Description                                                                                                                                          |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | [`mysql_socket_invalid`](socket_instrumentation.md#mysql_socket_invalid) `static` `inline`                           | MYSQL\_SOCKET helper. Initialize instrumented socket. **See also**: mysql\_socket\_getfd                                                             |
| `void`                                                   | [`mysql_socket_set_address`](socket_instrumentation.md#mysql_socket_set_address) `static` `inline`                   | Set socket descriptor and address.                                                                                                                   |
| `void`                                                   | [`mysql_socket_set_thread_owner`](socket_instrumentation.md#mysql_socket_set_thread_owner) `static` `inline`         | Set socket descriptor and address.                                                                                                                   |
| `my_socket`                                              | [`mysql_socket_getfd`](socket_instrumentation.md#mysql_socket_getfd) `static` `inline`                               | MYSQL\_SOCKET helper. Get socket descriptor. **See also**: mysql\_socket\_getfd                                                                      |
| `void`                                                   | [`mysql_socket_setfd`](socket_instrumentation.md#mysql_socket_setfd) `static` `inline`                               | MYSQL\_SOCKET helper. Set socket descriptor. **See also**: mysql\_socket\_setfd                                                                      |
| `struct PSI_socket_locker *`                             | [`inline_mysql_start_socket_wait`](socket_instrumentation.md#inline_mysql_start_socket_wait) `static` `inline`       | Instrumentation calls for MYSQL\_START\_SOCKET\_WAIT. **See also**: [MYSQL\_START\_SOCKET\_WAIT](socket_instrumentation.md#mysql_start_socket_wait). |
| `void`                                                   | [`inline_mysql_end_socket_wait`](socket_instrumentation.md#inline_mysql_end_socket_wait) `static` `inline`           | Instrumentation calls for MYSQL\_END\_SOCKET\_WAIT. **See also**: [MYSQL\_END\_SOCKET\_WAIT](socket_instrumentation.md#mysql_end_socket_wait).       |
| `void`                                                   | [`inline_mysql_socket_set_state`](socket_instrumentation.md#inline_mysql_socket_set_state) `static` `inline`         | Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI\_socket\_state                                                             |
| `void`                                                   | [`inline_mysql_socket_register`](socket_instrumentation.md#inline_mysql_socket_register) `static` `inline`           |                                                                                                                                                      |
| [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | [`inline_mysql_socket_fd`](socket_instrumentation.md#inline_mysql_socket_fd) `static` `inline`                       | mysql\_socket\_fd                                                                                                                                    |
| [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | [`inline_mysql_socket_socket`](socket_instrumentation.md#inline_mysql_socket_socket) `static` `inline`               | mysql\_socket\_socket                                                                                                                                |
| `int`                                                    | [`inline_mysql_socket_bind`](socket_instrumentation.md#inline_mysql_socket_bind) `static` `inline`                   | mysql\_socket\_bind                                                                                                                                  |
| `int`                                                    | [`inline_mysql_socket_getsockname`](socket_instrumentation.md#inline_mysql_socket_getsockname) `static` `inline`     | mysql\_socket\_getsockname                                                                                                                           |
| `int`                                                    | [`inline_mysql_socket_connect`](socket_instrumentation.md#inline_mysql_socket_connect) `static` `inline`             | mysql\_socket\_connect                                                                                                                               |
| `int`                                                    | [`inline_mysql_socket_getpeername`](socket_instrumentation.md#inline_mysql_socket_getpeername) `static` `inline`     | mysql\_socket\_getpeername                                                                                                                           |
| `ssize_t`                                                | [`inline_mysql_socket_send`](socket_instrumentation.md#inline_mysql_socket_send) `static` `inline`                   | mysql\_socket\_send                                                                                                                                  |
| `ssize_t`                                                | [`inline_mysql_socket_recv`](socket_instrumentation.md#inline_mysql_socket_recv) `static` `inline`                   | mysql\_socket\_recv                                                                                                                                  |
| `ssize_t`                                                | [`inline_mysql_socket_sendto`](socket_instrumentation.md#inline_mysql_socket_sendto) `static` `inline`               | mysql\_socket\_sendto                                                                                                                                |
| `ssize_t`                                                | [`inline_mysql_socket_recvfrom`](socket_instrumentation.md#inline_mysql_socket_recvfrom) `static` `inline`           | mysql\_socket\_recvfrom                                                                                                                              |
| `int`                                                    | [`inline_mysql_socket_getsockopt`](socket_instrumentation.md#inline_mysql_socket_getsockopt) `static` `inline`       | mysql\_socket\_getsockopt                                                                                                                            |
| `int`                                                    | [`inline_mysql_socket_setsockopt`](socket_instrumentation.md#inline_mysql_socket_setsockopt) `static` `inline`       | mysql\_socket\_setsockopt                                                                                                                            |
| `int`                                                    | [`set_socket_nonblock`](socket_instrumentation.md#set_socket_nonblock) `static` `inline`                             | set\_socket\_nonblock                                                                                                                                |
| `int`                                                    | [`inline_mysql_sock_set_nonblocking`](socket_instrumentation.md#inline_mysql_sock_set_nonblocking) `static` `inline` | mysql\_socket\_set\_nonblocking                                                                                                                      |
| `int`                                                    | [`inline_mysql_socket_listen`](socket_instrumentation.md#inline_mysql_socket_listen) `static` `inline`               | mysql\_socket\_listen                                                                                                                                |
| [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | [`inline_mysql_socket_accept`](socket_instrumentation.md#inline_mysql_socket_accept) `static` `inline`               | mysql\_socket\_accept                                                                                                                                |
| `int`                                                    | [`inline_mysql_socket_close`](socket_instrumentation.md#inline_mysql_socket_close) `static` `inline`                 | mysql\_socket\_close                                                                                                                                 |
| `int`                                                    | [`inline_mysql_socket_shutdown`](socket_instrumentation.md#inline_mysql_socket_shutdown) `static` `inline`           | mysql\_socket\_shutdown                                                                                                                              |

***

### mysql\_socket\_invalid

`static` `inline`

```cpp
static inline MYSQL_SOCKET mysql_socket_invalid()
```

Defined in psi/mysql\_socket.h:117

MYSQL\_SOCKET helper. Initialize instrumented socket. **See also**: mysql\_socket\_getfd

**See also**: mysql\_socket\_setfd

***

### mysql\_socket\_set\_address

`static` `inline`

```cpp
static inline void mysql_socket_set_address(MYSQL_SOCKET socket, const struct sockaddr * addr, socklen_t addr_len, MYSQL_SOCKET socket, const struct sockaddr * addr, socklen_t addr_len)
```

Defined in psi/mysql\_socket.h:132

Set socket descriptor and address.

#### Parameters

| Parameter  | Type                                                     | Description                |
| ---------- | -------------------------------------------------------- | -------------------------- |
| `socket`   | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | instrumented socket        |
| `addr`     | `const struct sockaddr *`                                | unformatted socket address |
| `addr_len` | `socklen_t`                                              | length of socket address   |
| `socket`   | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | instrumented socket        |
| `addr`     | `const struct sockaddr *`                                | unformatted socket address |
| `addr_len` | `socklen_t`                                              | length of socket address   |

***

### mysql\_socket\_set\_thread\_owner

`static` `inline`

```cpp
static inline void mysql_socket_set_thread_owner(MYSQL_SOCKET socket, MYSQL_SOCKET socket)
```

Defined in psi/mysql\_socket.h:155

Set socket descriptor and address.

#### Parameters

| Parameter | Type                                                     | Description         |
| --------- | -------------------------------------------------------- | ------------------- |
| `socket`  | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | instrumented socket |
| `socket`  | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | instrumented socket |

***

### mysql\_socket\_getfd

`static` `inline`

```cpp
static inline my_socket mysql_socket_getfd(MYSQL_SOCKET mysql_socket, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql\_socket.h:175

MYSQL\_SOCKET helper. Get socket descriptor. **See also**: mysql\_socket\_getfd

#### Parameters

| Parameter      | Type                                                     | Description         |
| -------------- | -------------------------------------------------------- | ------------------- |
| `mysql_socket` | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | Instrumented socket |
| `mysql_socket` | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | Instrumented socket |

***

### mysql\_socket\_setfd

`static` `inline`

```cpp
static inline void mysql_socket_setfd(MYSQL_SOCKET * mysql_socket, my_socket fd, MYSQL_SOCKET * mysql_socket, my_socket fd)
```

Defined in psi/mysql\_socket.h:187

MYSQL\_SOCKET helper. Set socket descriptor. **See also**: mysql\_socket\_setfd

#### Parameters

| Parameter      | Type                                                        | Description         |
| -------------- | ----------------------------------------------------------- | ------------------- |
| `mysql_socket` | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) \* | Instrumented socket |
| `fd`           | `my_socket`                                                 | Socket descriptor   |
| `mysql_socket` | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) \* | Instrumented socket |
| `fd`           | `my_socket`                                                 | Socket descriptor   |

***

### inline\_mysql\_start\_socket\_wait

`static` `inline`

```cpp
static inline struct PSI_socket_locker * inline_mysql_start_socket_wait(PSI_socket_locker_state * state, MYSQL_SOCKET mysql_socket, enum PSI_socket_operation op, size_t byte_count, const char * src_file, uint src_line, PSI_socket_locker_state * state, MYSQL_SOCKET mysql_socket, enum PSI_socket_operation op, size_t byte_count, const char * src_file, uint src_line)
```

Defined in psi/mysql\_socket.h:268

Instrumentation calls for MYSQL\_START\_SOCKET\_WAIT. **See also**: [MYSQL\_START\_SOCKET\_WAIT](socket_instrumentation.md#mysql_start_socket_wait).

***

### inline\_mysql\_end\_socket\_wait

`static` `inline`

```cpp
static inline void inline_mysql_end_socket_wait(struct PSI_socket_locker * locker, size_t byte_count, struct PSI_socket_locker * locker, size_t byte_count)
```

Defined in psi/mysql\_socket.h:290

Instrumentation calls for MYSQL\_END\_SOCKET\_WAIT. **See also**: [MYSQL\_END\_SOCKET\_WAIT](socket_instrumentation.md#mysql_end_socket_wait).

***

### inline\_mysql\_socket\_set\_state

`static` `inline`

```cpp
static inline void inline_mysql_socket_set_state(MYSQL_SOCKET socket, enum PSI_socket_state state, MYSQL_SOCKET socket, enum PSI_socket_state state)
```

Defined in psi/mysql\_socket.h:303

Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI\_socket\_state

#### Parameters

| Parameter | Type                                                     | Description             |
| --------- | -------------------------------------------------------- | ----------------------- |
| `socket`  | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | the instrumented socket |
| `state`   | `enum PSI_socket_state`                                  | the new state           |
| `socket`  | [`MYSQL_SOCKET`](socket_instrumentation.md#mysql_socket) | the instrumented socket |
| `state`   | `enum PSI_socket_state`                                  | the new state           |

***

### inline\_mysql\_socket\_register

`static` `inline`

```cpp
static inline void inline_mysql_socket_register(const char * category, PSI_socket_info * info, int count, const char * category, PSI_socket_info * info, int count)
```

Defined in psi/mysql\_socket.h:591

***

### inline\_mysql\_socket\_fd

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_fd(PSI_socket_key key, int fd, PSI_socket_key key, int fd)
```

Defined in psi/mysql\_socket.h:603

mysql\_socket\_fd

***

### inline\_mysql\_socket\_socket

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_socket(PSI_socket_key key, int domain, int type, int protocol, PSI_socket_key key, int domain, int type, int protocol)
```

Defined in psi/mysql\_socket.h:636

mysql\_socket\_socket

***

### inline\_mysql\_socket\_bind

`static` `inline`

```cpp
static inline int inline_mysql_socket_bind(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, size_t len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, size_t len)
```

Defined in psi/mysql\_socket.h:665

mysql\_socket\_bind

***

### inline\_mysql\_socket\_getsockname

`static` `inline`

```cpp
static inline int inline_mysql_socket_getsockname(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len)
```

Defined in psi/mysql\_socket.h:705

mysql\_socket\_getsockname

***

### inline\_mysql\_socket\_connect

`static` `inline`

```cpp
static inline int inline_mysql_socket_connect(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, socklen_t len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, socklen_t len)
```

Defined in psi/mysql\_socket.h:743

mysql\_socket\_connect

***

### inline\_mysql\_socket\_getpeername

`static` `inline`

```cpp
static inline int inline_mysql_socket_getpeername(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len)
```

Defined in psi/mysql\_socket.h:781

mysql\_socket\_getpeername

***

### inline\_mysql\_socket\_send

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_send(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags)
```

Defined in psi/mysql\_socket.h:819

mysql\_socket\_send

***

### inline\_mysql\_socket\_recv

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_recv(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags)
```

Defined in psi/mysql\_socket.h:860

mysql\_socket\_recv

***

### inline\_mysql\_socket\_sendto

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_sendto(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const struct sockaddr * addr, socklen_t addr_len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const struct sockaddr * addr, socklen_t addr_len)
```

Defined in psi/mysql\_socket.h:901

mysql\_socket\_sendto

***

### inline\_mysql\_socket\_recvfrom

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_recvfrom(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, struct sockaddr * addr, socklen_t * addr_len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, struct sockaddr * addr, socklen_t * addr_len)
```

Defined in psi/mysql\_socket.h:942

mysql\_socket\_recvfrom

***

### inline\_mysql\_socket\_getsockopt

`static` `inline`

```cpp
static inline int inline_mysql_socket_getsockopt(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, SOCKBUF_T * optval, socklen_t * optlen, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, SOCKBUF_T * optval, socklen_t * optlen)
```

Defined in psi/mysql\_socket.h:984

mysql\_socket\_getsockopt

***

### inline\_mysql\_socket\_setsockopt

`static` `inline`

```cpp
static inline int inline_mysql_socket_setsockopt(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, const SOCKBUF_T * optval, socklen_t optlen, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, const SOCKBUF_T * optval, socklen_t optlen)
```

Defined in psi/mysql\_socket.h:1022

mysql\_socket\_setsockopt

***

### set\_socket\_nonblock

`static` `inline`

```cpp
static inline int set_socket_nonblock(my_socket fd, my_socket fd)
```

Defined in psi/mysql\_socket.h:1060

set\_socket\_nonblock

***

### inline\_mysql\_sock\_set\_nonblocking

`static` `inline`

```cpp
static inline int inline_mysql_sock_set_nonblocking(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql\_socket.h:1093

mysql\_socket\_set\_nonblocking

***

### inline\_mysql\_socket\_listen

`static` `inline`

```cpp
static inline int inline_mysql_socket_listen(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int backlog, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int backlog)
```

Defined in psi/mysql\_socket.h:1133

mysql\_socket\_listen

***

### inline\_mysql\_socket\_accept

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_accept(const char * src_file, uint src_line, PSI_socket_key key, MYSQL_SOCKET socket_listen, struct sockaddr * addr, socklen_t * addr_len, const char * src_file, uint src_line, PSI_socket_key key, MYSQL_SOCKET socket_listen, struct sockaddr * addr, socklen_t * addr_len)
```

Defined in psi/mysql\_socket.h:1171

mysql\_socket\_accept

***

### inline\_mysql\_socket\_close

`static` `inline`

```cpp
static inline int inline_mysql_socket_close(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql\_socket.h:1252

mysql\_socket\_close

***

### inline\_mysql\_socket\_shutdown

`static` `inline`

```cpp
static inline int inline_mysql_socket_shutdown(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int how, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int how)
```

Defined in psi/mysql\_socket.h:1293

mysql\_socket\_shutdown

## Class Definitions

### st\_mysql\_socket

```cpp
#include <mysql_socket.h>
```

```cpp
struct st_mysql_socket
```

Defined in psi/mysql\_socket.h:75

An instrumented socket.

#### Public Attributes

| Return                                  | Name                                                                       | Description                                                                                                                           |
| --------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `my_socket`                             | [`fd`](socket_instrumentation.md#fd)                                       | The real socket descriptor.                                                                                                           |
| `char`                                  | [`is_unix_domain_socket`](socket_instrumentation.md#is_unix_domain_socket) | Is this a Unix-domain socket?                                                                                                         |
| `char`                                  | [`is_extra_port`](socket_instrumentation.md#is_extra_port)                 | Is this a socket opened for the extra port?                                                                                           |
| `unsigned short`                        | [`address_family`](socket_instrumentation.md#address_family)               | Address family of the socket. (See sa\_family from struct sockaddr).                                                                  |
| struct [`PSI_socket`](./#psi_socket) \* | [`m_psi`](socket_instrumentation.md#m_psi)                                 | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `MYSQL_SOCKET` interface. |

***

#### fd

```cpp
my_socket fd
```

Defined in psi/mysql\_socket.h:78

The real socket descriptor.

***

#### is\_unix\_domain\_socket

```cpp
char is_unix_domain_socket
```

Defined in psi/mysql\_socket.h:81

Is this a Unix-domain socket?

***

#### is\_extra\_port

```cpp
char is_extra_port
```

Defined in psi/mysql\_socket.h:84

Is this a socket opened for the extra port?

***

#### address\_family

```cpp
unsigned short address_family
```

Defined in psi/mysql\_socket.h:87

Address family of the socket. (See sa\_family from struct sockaddr).

***

#### m\_psi

```cpp
struct PSI_socket * m_psi
```

Type: struct [`PSI_socket`](./#psi_socket) \*

Defined in psi/mysql\_socket.h:94

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `MYSQL_SOCKET` interface.
