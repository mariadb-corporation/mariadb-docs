---
description: >-
  Understand InnoDB's architecture for MariaDB Enterprise Server. This section
  details its components and their interactions, focusing on performance,
  scalability, and reliability for enterprise workloa
---

# InnoDB Architecture for MariaDB Enterprise Server

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-server-innodb-background-thread-pool.md" %}
[mariadb-enterprise-server-innodb-background-thread-pool.md](mariadb-enterprise-server-innodb-background-thread-pool.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page details the dedicated thread pool in MariaDB Enterprise Server that manages InnoDB background tasks, improving scalability and performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-server-innodb-io-threads.md" %}
[mariadb-enterprise-server-innodb-io-threads.md](mariadb-enterprise-server-innodb-io-threads.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the specialized I/O threads in MariaDB Enterprise Server's InnoDB engine that handle asynchronous read and write operations efficiently.
{% endcolumn %}
{% endcolumns %}
