---
description: >-
  Plugin API reference: Socket Instrumentation. Generated from the MariaDB server headers by doxygen and moxygen.
---

{#socketinstrumentation}

# Socket Instrumentation

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Classes

| Name | Description |
|------|-------------|
| [`st_mysql_socket`](#st_mysql_socket) | An instrumented socket. |

## Macros

| Name | Description |
|------|-------------|
| [`mysql_socket_register`](#mysql_socket_register)  | Socket registration. |
| [`MYSQL_INVALID_SOCKET`](#mysql_invalid_socket)  | MYSQL_SOCKET initial value. |
| [`MYSQL_SOCKET_WAIT_VARIABLES`](#mysql_socket_wait_variables)  | Instrumentation helper for socket waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: [MYSQL_START_SOCKET_WAIT](api.md#mysql_start_socket_wait). |
| [`MYSQL_START_SOCKET_WAIT`](#mysql_start_socket_wait)  | Instrumentation helper for socket waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_SOCKET_WAIT](api.md#mysql_end_socket_wait). |
| [`MYSQL_END_SOCKET_WAIT`](#mysql_end_socket_wait)  | Instrumentation helper for socket waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_SOCKET_WAIT](api.md#mysql_start_socket_wait). |
| [`MYSQL_SOCKET_SET_STATE`](#mysql_socket_set_state)  | Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI_socket_state |
| [`mysql_socket_fd`](#mysql_socket_fd)  | Create a socket. `mysql_socket_fd` is a replacement for `socket`. |
| [`mysql_socket_socket`](#mysql_socket_socket)  | Create a socket. `mysql_socket_socket` is a replacement for `socket`. |
| [`mysql_socket_bind`](#mysql_socket_bind)  | Bind a socket to a local port number and IP address `mysql_socket_bind` is a replacement for `bind`. |
| [`mysql_socket_getsockname`](#mysql_socket_getsockname)  | Return port number and IP address of the local host `mysql_socket_getsockname` is a replacement for `getsockname`. |
| [`mysql_socket_connect`](#mysql_socket_connect)  | Establish a connection to a remote host. `mysql_socket_connect` is a replacement for `connect`. |
| [`mysql_socket_getpeername`](#mysql_socket_getpeername)  | Get port number and IP address of remote host that a socket is connected to. `mysql_socket_getpeername` is a replacement for `getpeername`. |
| [`mysql_socket_send`](#mysql_socket_send)  | Send data from the buffer, B, to a connected socket. `mysql_socket_send` is a replacement for `send`. |
| [`mysql_socket_recv`](#mysql_socket_recv)  | Receive data from a connected socket. `mysql_socket_recv` is a replacement for `recv`. |
| [`mysql_socket_sendto`](#mysql_socket_sendto)  | Send data to a socket at the specified address. `mysql_socket_sendto` is a replacement for `sendto`. |
| [`mysql_socket_recvfrom`](#mysql_socket_recvfrom)  | Receive data from a socket and return source address information `mysql_socket_recvfrom` is a replacement for `recvfrom`. |
| [`mysql_socket_getsockopt`](#mysql_socket_getsockopt)  | Get a socket option for the specified socket. `mysql_socket_getsockopt` is a replacement for `getsockopt`. |
| [`mysql_socket_setsockopt`](#mysql_socket_setsockopt)  | Set a socket option for the specified socket. `mysql_socket_setsockopt` is a replacement for `setsockopt`. |
| [`mysql_sock_set_nonblocking`](#mysql_sock_set_nonblocking)  | Set socket to non-blocking. |
| [`mysql_socket_listen`](#mysql_socket_listen)  | Set socket state to listen for an incoming connection. `mysql_socket_listen` is a replacement for `listen`. |
| [`mysql_socket_accept`](#mysql_socket_accept)  | Accept a connection from any remote host; TCP only. `mysql_socket_accept` is a replacement for `accept`. |
| [`mysql_socket_close`](#mysql_socket_close)  | Close a socket and sever any connections. `mysql_socket_close` is a replacement for `close`. |
| [`mysql_socket_shutdown`](#mysql_socket_shutdown)  | Disable receives and/or sends on a socket. `mysql_socket_shutdown` is a replacement for `shutdown`. |

---

{#mysql_socket_register}

### mysql_socket_register

```cpp
#define mysql_socket_register(P1, P2, P3, P1, P2, P3) inline_mysql_socket_register(P1, P2, P3)
```

Defined in psi/mysql_socket.h:65

Socket registration.

---

{#mysql_invalid_socket}

### MYSQL_INVALID_SOCKET

```cpp
#define MYSQL_INVALID_SOCKET mysql_socket_invalid()
```

Defined in psi/mysql_socket.h:107

MYSQL_SOCKET initial value.

---

{#mysql_socket_wait_variables}

### MYSQL_SOCKET_WAIT_VARIABLES

```cpp
#define MYSQL_SOCKET_WAIT_VARIABLES(LOCKER, STATE, LOCKER, STATE) struct PSI_socket_locker* LOCKER; \
    PSI_socket_locker_state STATE;
```

Defined in psi/mysql_socket.h:202

Instrumentation helper for socket waits. This instrumentation declares local variables. Do not use a ';' after this macro **See also**: [MYSQL_START_SOCKET_WAIT](api.md#mysql_start_socket_wait). 

**See also**: [MYSQL_END_SOCKET_WAIT](api.md#mysql_end_socket_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | locker |
| `STATE` |  | locker state |
| `LOCKER` |  | locker |
| `STATE` |  | locker state |

---

{#mysql_start_socket_wait}

### MYSQL_START_SOCKET_WAIT

```cpp
#define MYSQL_START_SOCKET_WAIT(LOCKER, STATE, SOCKET, OP, COUNT, LOCKER, STATE, SOCKET, OP, COUNT) LOCKER= inline_mysql_start_socket_wait(STATE, SOCKET, OP, COUNT,\
                                           __FILE__, __LINE__)
```

Defined in psi/mysql_socket.h:221

Instrumentation helper for socket waits. This instrumentation marks the start of a wait event. **See also**: [MYSQL_END_SOCKET_WAIT](api.md#mysql_end_socket_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | locker |
| `STATE` |  | locker state |
| `SOCKET` |  | instrumented socket |
| `OP` |  | The socket operation to be performed |
| `COUNT` |  | bytes to be written/read |
| `LOCKER` |  | locker |
| `STATE` |  | locker state |
| `SOCKET` |  | instrumented socket |
| `OP` |  | The socket operation to be performed |
| `COUNT` |  | bytes to be written/read |

---

{#mysql_end_socket_wait}

### MYSQL_END_SOCKET_WAIT

```cpp
#define MYSQL_END_SOCKET_WAIT(LOCKER, COUNT, LOCKER, COUNT) inline_mysql_end_socket_wait(LOCKER, COUNT)
```

Defined in psi/mysql_socket.h:238

Instrumentation helper for socket waits. This instrumentation marks the end of a wait event. **See also**: [MYSQL_START_SOCKET_WAIT](api.md#mysql_start_socket_wait).

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `LOCKER` |  | locker |
| `COUNT` |  | actual bytes written/read, or -1 |
| `LOCKER` |  | locker |
| `COUNT` |  | actual bytes written/read, or -1 |

---

{#mysql_socket_set_state}

### MYSQL_SOCKET_SET_STATE

```cpp
#define MYSQL_SOCKET_SET_STATE(SOCKET, STATE, SOCKET, STATE) inline_mysql_socket_set_state(SOCKET, STATE)
```

Defined in psi/mysql_socket.h:253

Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI_socket_state

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `SOCKET` |  | the instrumented socket |
| `STATE` |  | the new state |
| `SOCKET` |  | the instrumented socket |
| `STATE` |  | the new state |

---

{#mysql_socket_fd}

### mysql_socket_fd

```cpp
#define mysql_socket_fd(K, F, K, F) inline_mysql_socket_fd(K, F)
```

Defined in psi/mysql_socket.h:317

Create a socket. `mysql_socket_fd` is a replacement for `socket`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | PSI_socket_key for this instrumented socket |
| `F` |  | File descriptor |
| `K` |  | PSI_socket_key for this instrumented socket |
| `F` |  | File descriptor |

---

{#mysql_socket_socket}

### mysql_socket_socket

```cpp
#define mysql_socket_socket(K, D, T, P, K, D, T, P) inline_mysql_socket_socket(K, D, T, P)
```

Defined in psi/mysql_socket.h:335

Create a socket. `mysql_socket_socket` is a replacement for `socket`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | PSI_socket_key for this instrumented socket |
| `D` |  | Socket domain |
| `T` |  | Protocol type |
| `P` |  | Transport protocol |
| `K` |  | PSI_socket_key for this instrumented socket |
| `D` |  | Socket domain |
| `T` |  | Protocol type |
| `P` |  | Transport protocol |

---

{#mysql_socket_bind}

### mysql_socket_bind

```cpp
#define mysql_socket_bind(FD, AP, L, FD, AP, L) inline_mysql_socket_bind(__FILE__, __LINE__, FD, AP, L)
```

Defined in psi/mysql_socket.h:351

Bind a socket to a local port number and IP address `mysql_socket_bind` is a replacement for `bind`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to local port number and IP address in sockaddr structure |
| `L` |  | Length of sockaddr structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to local port number and IP address in sockaddr structure |
| `L` |  | Length of sockaddr structure |

---

{#mysql_socket_getsockname}

### mysql_socket_getsockname

```cpp
#define mysql_socket_getsockname(FD, AP, LP, FD, AP, LP) inline_mysql_socket_getsockname(__FILE__, __LINE__, FD, AP, LP)
```

Defined in psi/mysql_socket.h:367

Return port number and IP address of the local host `mysql_socket_getsockname` is a replacement for `getsockname`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to returned address of local host in `sockaddr` structure |
| `LP` |  | Pointer to length of `sockaddr` structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to returned address of local host in `sockaddr` structure |
| `LP` |  | Pointer to length of `sockaddr` structure |

---

{#mysql_socket_connect}

### mysql_socket_connect

```cpp
#define mysql_socket_connect(FD, AP, L, FD, AP, L) inline_mysql_socket_connect(__FILE__, __LINE__, FD, AP, L)
```

Defined in psi/mysql_socket.h:383

Establish a connection to a remote host. `mysql_socket_connect` is a replacement for `connect`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to target address in sockaddr structure |
| `L` |  | Length of sockaddr structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `AP` |  | Pointer to target address in sockaddr structure |
| `L` |  | Length of sockaddr structure |

---

{#mysql_socket_getpeername}

### mysql_socket_getpeername

```cpp
#define mysql_socket_getpeername(FD, AP, LP, FD, AP, LP) inline_mysql_socket_getpeername(__FILE__, __LINE__, FD, AP, LP)
```

Defined in psi/mysql_socket.h:399

Get port number and IP address of remote host that a socket is connected to. `mysql_socket_getpeername` is a replacement for `getpeername`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `AP` |  | Pointer to returned address of remote host in sockaddr structure |
| `LP` |  | Pointer to length of sockaddr structure |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `AP` |  | Pointer to returned address of remote host in sockaddr structure |
| `LP` |  | Pointer to length of sockaddr structure |

---

{#mysql_socket_send}

### mysql_socket_send

```cpp
#define mysql_socket_send(FD, B, N, FL, FD, B, N, FL) inline_mysql_socket_send(__FILE__, __LINE__, FD, B, N, FL)
```

Defined in psi/mysql_socket.h:416

Send data from the buffer, B, to a connected socket. `mysql_socket_send` is a replacement for `send`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `B` |  | Buffer to send |
| `N` |  | Number of bytes to send |
| `FL` |  | Control flags |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `B` |  | Buffer to send |
| `N` |  | Number of bytes to send |
| `FL` |  | Control flags |

---

{#mysql_socket_recv}

### mysql_socket_recv

```cpp
#define mysql_socket_recv(FD, B, N, FL, FD, B, N, FL) inline_mysql_socket_recv(__FILE__, __LINE__, FD, B, N, FL)
```

Defined in psi/mysql_socket.h:433

Receive data from a connected socket. `mysql_socket_recv` is a replacement for `recv`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `B` |  | Buffer to receive to |
| `N` |  | Maximum bytes to receive |
| `FL` |  | Control flags |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `B` |  | Buffer to receive to |
| `N` |  | Maximum bytes to receive |
| `FL` |  | Control flags |

---

{#mysql_socket_sendto}

### mysql_socket_sendto

```cpp
#define mysql_socket_sendto(FD, B, N, FL, AP, L, FD, B, N, FL, AP, L) inline_mysql_socket_sendto(__FILE__, __LINE__, FD, B, N, FL, AP, L)
```

Defined in psi/mysql_socket.h:452

Send data to a socket at the specified address. `mysql_socket_sendto` is a replacement for `sendto`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `B` |  | Buffer to send |
| `N` |  | Number of bytes to send |
| `FL` |  | Control flags |
| `AP` |  | Pointer to destination sockaddr structure |
| `L` |  | Size of sockaddr structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `B` |  | Buffer to send |
| `N` |  | Number of bytes to send |
| `FL` |  | Control flags |
| `AP` |  | Pointer to destination sockaddr structure |
| `L` |  | Size of sockaddr structure |

---

{#mysql_socket_recvfrom}

### mysql_socket_recvfrom

```cpp
#define mysql_socket_recvfrom(FD, B, N, FL, AP, LP, FD, B, N, FL, AP, LP) inline_mysql_socket_recvfrom(__FILE__, __LINE__, FD, B, N, FL, AP, LP)
```

Defined in psi/mysql_socket.h:471

Receive data from a socket and return source address information `mysql_socket_recvfrom` is a replacement for `recvfrom`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `B` |  | Buffer to receive to |
| `N` |  | Maximum bytes to receive |
| `FL` |  | Control flags |
| `AP` |  | Pointer to source address in sockaddr_storage structure |
| `LP` |  | Size of sockaddr_storage structure |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `B` |  | Buffer to receive to |
| `N` |  | Maximum bytes to receive |
| `FL` |  | Control flags |
| `AP` |  | Pointer to source address in sockaddr_storage structure |
| `LP` |  | Size of sockaddr_storage structure |

---

{#mysql_socket_getsockopt}

### mysql_socket_getsockopt

```cpp
#define mysql_socket_getsockopt(FD, LV, ON, OP, OL, FD, LV, ON, OP, OL) inline_mysql_socket_getsockopt(__FILE__, __LINE__, FD, LV, ON, OP, OL)
```

Defined in psi/mysql_socket.h:489

Get a socket option for the specified socket. `mysql_socket_getsockopt` is a replacement for `getsockopt`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `LV` |  | Protocol level |
| `ON` |  | Option to query |
| `OP` |  | Buffer which will contain the value for the requested option |
| `OL` |  | Pointer to length of OP |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `LV` |  | Protocol level |
| `ON` |  | Option to query |
| `OP` |  | Buffer which will contain the value for the requested option |
| `OL` |  | Pointer to length of OP |

---

{#mysql_socket_setsockopt}

### mysql_socket_setsockopt

```cpp
#define mysql_socket_setsockopt(FD, LV, ON, OP, OL, FD, LV, ON, OP, OL) inline_mysql_socket_setsockopt(__FILE__, __LINE__, FD, LV, ON, OP, OL)
```

Defined in psi/mysql_socket.h:507

Set a socket option for the specified socket. `mysql_socket_setsockopt` is a replacement for `setsockopt`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `LV` |  | Protocol level |
| `ON` |  | Option to modify |
| `OP` |  | Buffer containing the value for the specified option |
| `OL` |  | Pointer to length of OP |
| `FD` |  | Instrumented socket descriptor returned by socket() |
| `LV` |  | Protocol level |
| `ON` |  | Option to modify |
| `OP` |  | Buffer containing the value for the specified option |
| `OL` |  | Pointer to length of OP |

---

{#mysql_sock_set_nonblocking}

### mysql_sock_set_nonblocking

```cpp
#define mysql_sock_set_nonblocking(FD, FD) inline_mysql_sock_set_nonblocking(__FILE__, __LINE__, FD)
```

Defined in psi/mysql_socket.h:520

Set socket to non-blocking.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | instrumented socket descriptor |
| `FD` |  | instrumented socket descriptor |

---

{#mysql_socket_listen}

### mysql_socket_listen

```cpp
#define mysql_socket_listen(FD, N, FD, N) inline_mysql_socket_listen(__FILE__, __LINE__, FD, N)
```

Defined in psi/mysql_socket.h:535

Set socket state to listen for an incoming connection. `mysql_socket_listen` is a replacement for `listen`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor, bound and connected |
| `N` |  | Maximum number of pending connections allowed. |
| `FD` |  | Instrumented socket descriptor, bound and connected |
| `N` |  | Maximum number of pending connections allowed. |

---

{#mysql_socket_accept}

### mysql_socket_accept

```cpp
#define mysql_socket_accept(K, FD, AP, LP, K, FD, AP, LP) inline_mysql_socket_accept(__FILE__, __LINE__, K, FD, AP, LP)
```

Defined in psi/mysql_socket.h:552

Accept a connection from any remote host; TCP only. `mysql_socket_accept` is a replacement for `accept`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `K` |  | PSI_socket_key for this instrumented socket |
| `FD` |  | Instrumented socket descriptor, bound and placed in a listen state |
| `AP` |  | Pointer to sockaddr structure with returned IP address and port of connected host |
| `LP` |  | Pointer to length of valid information in AP |
| `K` |  | PSI_socket_key for this instrumented socket |
| `FD` |  | Instrumented socket descriptor, bound and placed in a listen state |
| `AP` |  | Pointer to sockaddr structure with returned IP address and port of connected host |
| `LP` |  | Pointer to length of valid information in AP |

---

{#mysql_socket_close}

### mysql_socket_close

```cpp
#define mysql_socket_close(FD, FD) inline_mysql_socket_close(__FILE__, __LINE__, FD)
```

Defined in psi/mysql_socket.h:566

Close a socket and sever any connections. `mysql_socket_close` is a replacement for `close`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |

---

{#mysql_socket_shutdown}

### mysql_socket_shutdown

```cpp
#define mysql_socket_shutdown(FD, H, FD, H) inline_mysql_socket_shutdown(__FILE__, __LINE__, FD, H)
```

Defined in psi/mysql_socket.h:581

Disable receives and/or sends on a socket. `mysql_socket_shutdown` is a replacement for `shutdown`.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `H` |  | Specifies which operations to shutdown |
| `FD` |  | Instrumented socket descriptor returned by socket() or accept() |
| `H` |  | Specifies which operations to shutdown |

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| struct [`st_mysql_socket`](#st_mysql_socket) | [`MYSQL_SOCKET`](#mysql_socket)  | An instrumented socket. `MYSQL_SOCKET` is a replacement for `my_socket`. |

---

{#mysql_socket}

### MYSQL_SOCKET

```cpp
using MYSQL_SOCKET = struct st_mysql_socket
```

Type: struct [`st_mysql_socket`](#st_mysql_socket)

Defined in psi/mysql_socket.h:99

An instrumented socket. `MYSQL_SOCKET` is a replacement for `my_socket`.

## Functions

| Return | Name | Description |
|--------|------|-------------|
| [`MYSQL_SOCKET`](api.md#mysql_socket) | [`mysql_socket_invalid`](#mysql_socket_invalid) `static` `inline` | MYSQL_SOCKET helper. Initialize instrumented socket. **See also**: mysql_socket_getfd |
| `void` | [`mysql_socket_set_address`](#mysql_socket_set_address) `static` `inline` | Set socket descriptor and address. |
| `void` | [`mysql_socket_set_thread_owner`](#mysql_socket_set_thread_owner) `static` `inline` | Set socket descriptor and address. |
| `my_socket` | [`mysql_socket_getfd`](#mysql_socket_getfd) `static` `inline` | MYSQL_SOCKET helper. Get socket descriptor. **See also**: mysql_socket_getfd |
| `void` | [`mysql_socket_setfd`](#mysql_socket_setfd) `static` `inline` | MYSQL_SOCKET helper. Set socket descriptor. **See also**: mysql_socket_setfd |
| `struct PSI_socket_locker *` | [`inline_mysql_start_socket_wait`](#inline_mysql_start_socket_wait) `static` `inline` | Instrumentation calls for MYSQL_START_SOCKET_WAIT. **See also**: [MYSQL_START_SOCKET_WAIT](api.md#mysql_start_socket_wait). |
| `void` | [`inline_mysql_end_socket_wait`](#inline_mysql_end_socket_wait) `static` `inline` | Instrumentation calls for MYSQL_END_SOCKET_WAIT. **See also**: [MYSQL_END_SOCKET_WAIT](api.md#mysql_end_socket_wait). |
| `void` | [`inline_mysql_socket_set_state`](#inline_mysql_socket_set_state) `static` `inline` | Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI_socket_state |
| `void` | [`inline_mysql_socket_register`](#inline_mysql_socket_register) `static` `inline` |  |
| [`MYSQL_SOCKET`](api.md#mysql_socket) | [`inline_mysql_socket_fd`](#inline_mysql_socket_fd) `static` `inline` | mysql_socket_fd |
| [`MYSQL_SOCKET`](api.md#mysql_socket) | [`inline_mysql_socket_socket`](#inline_mysql_socket_socket) `static` `inline` | mysql_socket_socket |
| `int` | [`inline_mysql_socket_bind`](#inline_mysql_socket_bind) `static` `inline` | mysql_socket_bind |
| `int` | [`inline_mysql_socket_getsockname`](#inline_mysql_socket_getsockname) `static` `inline` | mysql_socket_getsockname |
| `int` | [`inline_mysql_socket_connect`](#inline_mysql_socket_connect) `static` `inline` | mysql_socket_connect |
| `int` | [`inline_mysql_socket_getpeername`](#inline_mysql_socket_getpeername) `static` `inline` | mysql_socket_getpeername |
| `ssize_t` | [`inline_mysql_socket_send`](#inline_mysql_socket_send) `static` `inline` | mysql_socket_send |
| `ssize_t` | [`inline_mysql_socket_recv`](#inline_mysql_socket_recv) `static` `inline` | mysql_socket_recv |
| `ssize_t` | [`inline_mysql_socket_sendto`](#inline_mysql_socket_sendto) `static` `inline` | mysql_socket_sendto |
| `ssize_t` | [`inline_mysql_socket_recvfrom`](#inline_mysql_socket_recvfrom) `static` `inline` | mysql_socket_recvfrom |
| `int` | [`inline_mysql_socket_getsockopt`](#inline_mysql_socket_getsockopt) `static` `inline` | mysql_socket_getsockopt |
| `int` | [`inline_mysql_socket_setsockopt`](#inline_mysql_socket_setsockopt) `static` `inline` | mysql_socket_setsockopt |
| `int` | [`set_socket_nonblock`](#set_socket_nonblock) `static` `inline` | set_socket_nonblock |
| `int` | [`inline_mysql_sock_set_nonblocking`](#inline_mysql_sock_set_nonblocking) `static` `inline` | mysql_socket_set_nonblocking |
| `int` | [`inline_mysql_socket_listen`](#inline_mysql_socket_listen) `static` `inline` | mysql_socket_listen |
| [`MYSQL_SOCKET`](api.md#mysql_socket) | [`inline_mysql_socket_accept`](#inline_mysql_socket_accept) `static` `inline` | mysql_socket_accept |
| `int` | [`inline_mysql_socket_close`](#inline_mysql_socket_close) `static` `inline` | mysql_socket_close |
| `int` | [`inline_mysql_socket_shutdown`](#inline_mysql_socket_shutdown) `static` `inline` | mysql_socket_shutdown |

---

{#mysql_socket_invalid}

### mysql_socket_invalid

`static` `inline`

```cpp
static inline MYSQL_SOCKET mysql_socket_invalid()
```

Defined in psi/mysql_socket.h:115

MYSQL_SOCKET helper. Initialize instrumented socket. **See also**: mysql_socket_getfd 

**See also**: mysql_socket_setfd

---

{#mysql_socket_set_address}

### mysql_socket_set_address

`static` `inline`

```cpp
static inline void mysql_socket_set_address(MYSQL_SOCKET socket, const struct sockaddr * addr, socklen_t addr_len, MYSQL_SOCKET socket, const struct sockaddr * addr, socklen_t addr_len)
```

Defined in psi/mysql_socket.h:130

Set socket descriptor and address.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) | instrumented socket |
| `addr` | `const struct sockaddr *` | unformatted socket address |
| `addr_len` | `socklen_t` | length of socket address |
| `socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) | instrumented socket |
| `addr` | `const struct sockaddr *` | unformatted socket address |
| `addr_len` | `socklen_t` | length of socket address |

---

{#mysql_socket_set_thread_owner}

### mysql_socket_set_thread_owner

`static` `inline`

```cpp
static inline void mysql_socket_set_thread_owner(MYSQL_SOCKET socket, MYSQL_SOCKET socket)
```

Defined in psi/mysql_socket.h:153

Set socket descriptor and address.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) | instrumented socket |
| `socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) | instrumented socket |

---

{#mysql_socket_getfd}

### mysql_socket_getfd

`static` `inline`

```cpp
static inline my_socket mysql_socket_getfd(MYSQL_SOCKET mysql_socket, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql_socket.h:173

MYSQL_SOCKET helper. Get socket descriptor. **See also**: mysql_socket_getfd

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql_socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) | Instrumented socket |
| `mysql_socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) | Instrumented socket |

---

{#mysql_socket_setfd}

### mysql_socket_setfd

`static` `inline`

```cpp
static inline void mysql_socket_setfd(MYSQL_SOCKET * mysql_socket, my_socket fd, MYSQL_SOCKET * mysql_socket, my_socket fd)
```

Defined in psi/mysql_socket.h:185

MYSQL_SOCKET helper. Set socket descriptor. **See also**: mysql_socket_setfd

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mysql_socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) * | Instrumented socket |
| `fd` | `my_socket` | Socket descriptor |
| `mysql_socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) * | Instrumented socket |
| `fd` | `my_socket` | Socket descriptor |

---

{#inline_mysql_start_socket_wait}

### inline_mysql_start_socket_wait

`static` `inline`

```cpp
static inline struct PSI_socket_locker * inline_mysql_start_socket_wait(PSI_socket_locker_state * state, MYSQL_SOCKET mysql_socket, enum PSI_socket_operation op, size_t byte_count, const char * src_file, uint src_line, PSI_socket_locker_state * state, MYSQL_SOCKET mysql_socket, enum PSI_socket_operation op, size_t byte_count, const char * src_file, uint src_line)
```

Defined in psi/mysql_socket.h:266

Instrumentation calls for MYSQL_START_SOCKET_WAIT. **See also**: [MYSQL_START_SOCKET_WAIT](api.md#mysql_start_socket_wait).

---

{#inline_mysql_end_socket_wait}

### inline_mysql_end_socket_wait

`static` `inline`

```cpp
static inline void inline_mysql_end_socket_wait(struct PSI_socket_locker * locker, size_t byte_count, struct PSI_socket_locker * locker, size_t byte_count)
```

Defined in psi/mysql_socket.h:288

Instrumentation calls for MYSQL_END_SOCKET_WAIT. **See also**: [MYSQL_END_SOCKET_WAIT](api.md#mysql_end_socket_wait).

---

{#inline_mysql_socket_set_state}

### inline_mysql_socket_set_state

`static` `inline`

```cpp
static inline void inline_mysql_socket_set_state(MYSQL_SOCKET socket, enum PSI_socket_state state, MYSQL_SOCKET socket, enum PSI_socket_state state)
```

Defined in psi/mysql_socket.h:301

Set the state (IDLE, ACTIVE) of an instrumented socket. **See also**: PSI_socket_state

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) | the instrumented socket |
| `state` | `enum PSI_socket_state` | the new state |
| `socket` | [`MYSQL_SOCKET`](api.md#mysql_socket) | the instrumented socket |
| `state` | `enum PSI_socket_state` | the new state |

---

{#inline_mysql_socket_register}

### inline_mysql_socket_register

`static` `inline`

```cpp
static inline void inline_mysql_socket_register(const char * category, PSI_socket_info * info, int count, const char * category, PSI_socket_info * info, int count)
```

Defined in psi/mysql_socket.h:589

---

{#inline_mysql_socket_fd}

### inline_mysql_socket_fd

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_fd(PSI_socket_key key, int fd, PSI_socket_key key, int fd)
```

Defined in psi/mysql_socket.h:601

mysql_socket_fd

---

{#inline_mysql_socket_socket}

### inline_mysql_socket_socket

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_socket(PSI_socket_key key, int domain, int type, int protocol, PSI_socket_key key, int domain, int type, int protocol)
```

Defined in psi/mysql_socket.h:634

mysql_socket_socket

---

{#inline_mysql_socket_bind}

### inline_mysql_socket_bind

`static` `inline`

```cpp
static inline int inline_mysql_socket_bind(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, size_t len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, size_t len)
```

Defined in psi/mysql_socket.h:663

mysql_socket_bind

---

{#inline_mysql_socket_getsockname}

### inline_mysql_socket_getsockname

`static` `inline`

```cpp
static inline int inline_mysql_socket_getsockname(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len)
```

Defined in psi/mysql_socket.h:703

mysql_socket_getsockname

---

{#inline_mysql_socket_connect}

### inline_mysql_socket_connect

`static` `inline`

```cpp
static inline int inline_mysql_socket_connect(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, socklen_t len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const struct sockaddr * addr, socklen_t len)
```

Defined in psi/mysql_socket.h:741

mysql_socket_connect

---

{#inline_mysql_socket_getpeername}

### inline_mysql_socket_getpeername

`static` `inline`

```cpp
static inline int inline_mysql_socket_getpeername(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, struct sockaddr * addr, socklen_t * len)
```

Defined in psi/mysql_socket.h:779

mysql_socket_getpeername

---

{#inline_mysql_socket_send}

### inline_mysql_socket_send

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_send(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags)
```

Defined in psi/mysql_socket.h:817

mysql_socket_send

---

{#inline_mysql_socket_recv}

### inline_mysql_socket_recv

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_recv(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags)
```

Defined in psi/mysql_socket.h:858

mysql_socket_recv

---

{#inline_mysql_socket_sendto}

### inline_mysql_socket_sendto

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_sendto(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const struct sockaddr * addr, socklen_t addr_len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const SOCKBUF_T * buf, size_t n, int flags, const struct sockaddr * addr, socklen_t addr_len)
```

Defined in psi/mysql_socket.h:899

mysql_socket_sendto

---

{#inline_mysql_socket_recvfrom}

### inline_mysql_socket_recvfrom

`static` `inline`

```cpp
static inline ssize_t inline_mysql_socket_recvfrom(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, struct sockaddr * addr, socklen_t * addr_len, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, SOCKBUF_T * buf, size_t n, int flags, struct sockaddr * addr, socklen_t * addr_len)
```

Defined in psi/mysql_socket.h:940

mysql_socket_recvfrom

---

{#inline_mysql_socket_getsockopt}

### inline_mysql_socket_getsockopt

`static` `inline`

```cpp
static inline int inline_mysql_socket_getsockopt(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, SOCKBUF_T * optval, socklen_t * optlen, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, SOCKBUF_T * optval, socklen_t * optlen)
```

Defined in psi/mysql_socket.h:982

mysql_socket_getsockopt

---

{#inline_mysql_socket_setsockopt}

### inline_mysql_socket_setsockopt

`static` `inline`

```cpp
static inline int inline_mysql_socket_setsockopt(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, const SOCKBUF_T * optval, socklen_t optlen, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int level, int optname, const SOCKBUF_T * optval, socklen_t optlen)
```

Defined in psi/mysql_socket.h:1020

mysql_socket_setsockopt

---

{#set_socket_nonblock}

### set_socket_nonblock

`static` `inline`

```cpp
static inline int set_socket_nonblock(my_socket fd, my_socket fd)
```

Defined in psi/mysql_socket.h:1058

set_socket_nonblock

---

{#inline_mysql_sock_set_nonblocking}

### inline_mysql_sock_set_nonblocking

`static` `inline`

```cpp
static inline int inline_mysql_sock_set_nonblocking(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql_socket.h:1091

mysql_socket_set_nonblocking

---

{#inline_mysql_socket_listen}

### inline_mysql_socket_listen

`static` `inline`

```cpp
static inline int inline_mysql_socket_listen(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int backlog, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int backlog)
```

Defined in psi/mysql_socket.h:1131

mysql_socket_listen

---

{#inline_mysql_socket_accept}

### inline_mysql_socket_accept

`static` `inline`

```cpp
static inline MYSQL_SOCKET inline_mysql_socket_accept(const char * src_file, uint src_line, PSI_socket_key key, MYSQL_SOCKET socket_listen, struct sockaddr * addr, socklen_t * addr_len, const char * src_file, uint src_line, PSI_socket_key key, MYSQL_SOCKET socket_listen, struct sockaddr * addr, socklen_t * addr_len)
```

Defined in psi/mysql_socket.h:1169

mysql_socket_accept

---

{#inline_mysql_socket_close}

### inline_mysql_socket_close

`static` `inline`

```cpp
static inline int inline_mysql_socket_close(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket)
```

Defined in psi/mysql_socket.h:1250

mysql_socket_close

---

{#inline_mysql_socket_shutdown}

### inline_mysql_socket_shutdown

`static` `inline`

```cpp
static inline int inline_mysql_socket_shutdown(const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int how, const char * src_file, uint src_line, MYSQL_SOCKET mysql_socket, int how)
```

Defined in psi/mysql_socket.h:1291

mysql_socket_shutdown


## Class Definitions

{#st_mysql_socket}

### st_mysql_socket

```cpp
#include <mysql_socket.h>
```

```cpp
struct st_mysql_socket
```

Defined in psi/mysql_socket.h:73

An instrumented socket.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `my_socket` | [`fd`](#fd)  | The real socket descriptor. |
| `char` | [`is_unix_domain_socket`](#is_unix_domain_socket)  | Is this a Unix-domain socket? |
| `char` | [`is_extra_port`](#is_extra_port)  | Is this a socket opened for the extra port? |
| `unsigned short` | [`address_family`](#address_family)  | Address family of the socket. (See sa_family from struct sockaddr). |
| struct [`PSI_socket`](api.md#psi_socket) * | [`m_psi`](#m_psi-1)  | The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `MYSQL_SOCKET` interface. |

---

{#fd}

##### fd

```cpp
my_socket fd
```

Defined in psi/mysql_socket.h:76

The real socket descriptor.

---

{#is_unix_domain_socket}

##### is_unix_domain_socket

```cpp
char is_unix_domain_socket
```

Defined in psi/mysql_socket.h:79

Is this a Unix-domain socket?

---

{#is_extra_port}

##### is_extra_port

```cpp
char is_extra_port
```

Defined in psi/mysql_socket.h:82

Is this a socket opened for the extra port?

---

{#address_family}

##### address_family

```cpp
unsigned short address_family
```

Defined in psi/mysql_socket.h:85

Address family of the socket. (See sa_family from struct sockaddr).

---

{#m_psi-1}

##### m_psi

```cpp
struct PSI_socket * m_psi
```

Type: struct [`PSI_socket`](api.md#psi_socket) *

Defined in psi/mysql_socket.h:92

The instrumentation hook. Note that this hook is not conditionally defined, for binary compatibility of the `MYSQL_SOCKET` interface.

