---
description: >-
  MariaDB Connector/Node.js pipelining dispatches queries in FIFO order
  without blocking on each response, improving throughput for high-volume
  workloads over high-latency connections.
---

# Connector/Node.js Pipelining

With traditional database drivers, queries issued from the application are sent one by one to the server, waiting on the results of the first query before sending the next. Communication with the server follows this synchronous request-response messaging pattern. While this may be sufficient for some applications, it isn't very efficient when you need to process a large volume of queries at the same time.

Node.js provides good support for asynchronous processing, which you can utilize with the MariaDB Connector using the Pipelining option.

## Using Pipelining

When Pipelining, the Connector uses an optimistic send, sending queries one after another, preserving the FIFO order. This is particularly efficient when the client is some distance from the server.

For instance, say you want to create a basket with three items.

```hs
connection.beginTransaction();
connection.query("INSERT INTO BASKET(customerId) values (?)", [1], (err, res) => {
  //must handle error if any
  const basketId = res.insertId;
  try {
    connection.query("INSERT INTO basket_item(basketId, itemId) VALUES (?, ?)", [basketId, 100]);
    connection.query("INSERT INTO basket_item(basketId, itemId) VALUES (?, ?)", [basketId, 101]);
    connection.query("INSERT INTO basket_item(basketId, itemId) VALUES (?, ?)", [basketId, 102], (err) => {
      //must handle error if any
      connection.commit();
    });
  } catch (err) {
    connection.rollback();
    //handle error
  }
});
```

## Network Exchanges

```mermaid
sequenceDiagram
    accTitle: Standard ping-pong versus pipelining request/response exchanges
    accDescr {
        In the standard ping-pong pattern, the connector sends one query and waits for
        its response before sending the next, so each INSERT and the COMMIT round-trip
        individually. With pipelining, the connector sends the three basket_item INSERT
        queries back to back without waiting, then receives their three responses in
        turn, before finally sending COMMIT and waiting for its response.
    }
    participant C as Connector
    participant D as Database

    Note over C,D: Standard "ping-pong"
    C->>D: send INSERT INTO BASKET
    D-->>C: INSERT INTO BASKET response
    C->>D: send INSERT INTO BASKET_ITEM
    D-->>C: INSERT INTO BASKET_ITEM response
    C->>D: send INSERT INTO BASKET_ITEM
    D-->>C: INSERT INTO BASKET_ITEM response
    C->>D: send INSERT INTO BASKET_ITEM
    D-->>C: INSERT INTO BASKET_ITEM response
    C->>D: send COMMIT
    D-->>C: COMMIT response

    Note over C,D: Pipelining
    C->>D: send INSERT INTO BASKET
    D-->>C: INSERT INTO BASKET response
    C->>D: send INSERT INTO BASKET_ITEM
    C->>D: send INSERT INTO BASKET_ITEM
    C->>D: send INSERT INTO BASKET_ITEM
    D-->>C: INSERT INTO BASKET_ITEM response
    D-->>C: INSERT INTO BASKET_ITEM response
    D-->>C: INSERT INTO BASKET_ITEM response
    C->>D: send COMMIT
    D-->>C: COMMIT response
```

_Standard ping-pong waits for each response before sending the next query; pipelining sends the basket_item queries back to back and receives their responses afterward._

Using the standard client-server protocol, the Connector communicates with the database following a request-response messaging pattern. The Connector sends a command, then doesn't send another until it receives a response from the input socket.

When using Pipelining, the Connector sends commands in bulk, reducing network latency. The catch is that the process is optimistic, meaning that if an error occurs on the first or second command, the following commands have already been sent to the database.


{% @marketo/form formId="4316" %}
