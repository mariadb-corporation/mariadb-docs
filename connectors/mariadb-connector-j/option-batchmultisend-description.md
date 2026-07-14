---
description: >-
  useBatchMultiSend enables bulk batch execution in MariaDB Connector/J,
  grouping executeBatch calls into multi-query packets to reduce round-trips
  between client and server.
---

# Option useBatchMultiSend Description

### Definition

Since 1.5.0, the "useBatchMultiSend" option permits sending queries by batch. If disabled, queries are sent one by one, waiting for the result before sending the next one. If enabled, queries will be sent by batch corresponding to the value of the useBatchMultiSendNumber option (default 100). Results will be read after a while, avoiding a lot of network latency when the client and the server aren't on the same host. This option is only used for JDBC executeBatch(). This option is particularly efficient when the client is distant from the server.

Here is a benchmark using a client and server on 2 different hosts (ping of 0.350 ms between 2 hosts):

![use\_batch\_multi\_send](../.gitbook/assets/use_batch_multi_send.png)

### Standard client-server protocol

By default, the driver interacts with the server using a request–response messaging pattern.

![standard](../.gitbook/assets/standard.png)

Once the driver sends data, it will remain blocked until data becomes available from the input socket.

### Batch multi-send communication

JDBC permits batching.\
Example:

```java
PreparedStatement preparedStatement = connection.prepareStatement("INSERT INTO test(data1, data2) VALUES (?, ?)");
    for (int i = 0; i < 3; i++) {
        preparedStatement.setInt(1, i);
        preparedStatement.setString(2, "value" + i);
        preparedStatement.addBatch();
    }
    preparedStatement.executeBatch();
```

When the `useBatchMultiSend` option is turned off, batches are processed sequentially, sending each item individually using the traditional request–response messaging pattern.\
Below is an example with a prepared statement (`useServerPrepStmts` enabled):

![standard\_batch](../.gitbook/assets/standard_batch.png)

Same example with "useBatchMultiSend" enabled. Requests are sent in bulk, saving network latency:

![bulk\_batch](../.gitbook/assets/bulk_batch.png)

Advantages:

* a lot more efficient.

Inconvenient:

* If an error occurs and "continueBatchOnError" is disabled (default enabled), some other data may have already been sent and executed.

**Bulk split**

Data is sent in batches, with each batch size determined by the `useBatchMultiSendNumber` value.\
Once the first send command is issued, reads begin asynchronously. The driver waits until all results for the current batch are received before sending the next batch.

{% @marketo/form formId="4316" %}
