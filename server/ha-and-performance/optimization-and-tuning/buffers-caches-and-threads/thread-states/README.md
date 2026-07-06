---
description: >-
  Understand MariaDB Server thread states. This section explains the different
  states a thread can be in, helping you monitor and troubleshoot query
  execution and server performance.
---

# Thread States

{% columns %}
{% column %}
{% content-ref url="delayed-insert-connection-thread-states.md" %}
[delayed-insert-connection-thread-states.md](delayed-insert-connection-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists the thread states for the connection thread that processes INSERT DELAYED statements, as shown by SHOW PROCESSLIST and related tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="delayed-insert-handler-thread-states.md" %}
[delayed-insert-handler-thread-states.md](delayed-insert-handler-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists the thread states for the handler thread that inserts the results of INSERT DELAYED statements, as shown by SHOW PROCESSLIST and related tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="event-scheduler-thread-states.md" %}
[event-scheduler-thread-states.md](event-scheduler-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists the thread states related to event scheduling and execution, as shown by SHOW PROCESSLIST and related tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="galera-cluster-thread-states.md" %}
[galera-cluster-thread-states.md](galera-cluster-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists the Galera Cluster-specific thread states shown in SHOW PROCESSLIST during cluster operations, such as certification, flow control, and Total Order Isolation DDL waits.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="general-thread-states.md" %}
[general-thread-states.md](general-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documents the major general thread states shown by SHOW PROCESSLIST and related tables, with links to the more specific state lists for replication, the query cache, and other subsystems.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="master-thread-states.md" %}
[master-thread-states.md](master-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists the thread states related to replication primary (master) threads, as shown by SHOW PROCESSLIST and related tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="query-cache-thread-states.md" %}
[query-cache-thread-states.md](query-cache-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists the thread states related to the query cache, as shown by SHOW PROCESSLIST and related tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replica-io-thread-states.md" %}
[replica-io-thread-states.md](replica-io-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists the replica I/O thread states shown by Slave_IO_State in SHOW REPLICA STATUS and by SHOW PROCESSLIST and related tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="slave-connection-thread-states.md" %}
[slave-connection-thread-states.md](slave-connection-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists the thread states for connection threads on a replication replica, as shown by SHOW PROCESSLIST and related tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="slave-sql-thread-states.md" %}
[slave-sql-thread-states.md](slave-sql-thread-states.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists the replica SQL thread states shown by Slave_SQL_State in SHOW REPLICA STATUS and by SHOW PROCESSLIST and related tables, including parallel replication states.
{% endcolumn %}
{% endcolumns %}
