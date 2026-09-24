---
title: MariaDB Platform
description: >-
  Get started with MariaDB Enterprise Platform: supported MariaDB with routing,
  clustering, and analytics for production. Understand it, route and scale it,
  add analytics.
icon: layer-group
---

# MariaDB Platform

MariaDB Enterprise Platform is MariaDB Enterprise Server plus the components a production deployment needs, bundled, version certified against each other, and covered by a support contract. You still operate it. What the Platform provides is a tested set of parts rather than an assembly you validate yourself.

The components address distinct problems. MaxScale routes queries, balances reads, and hides failover from the application. Galera Cluster and Raft Cluster replicate data across nodes and handle failover. ColumnStore and Exa run columnar analytics, and both require MariaDB Enterprise Server. GridGain provides in-memory caching and acceleration. Enterprise Manager and the Enterprise Operator manage fleets and Kubernetes deployments.

What the contract adds is concrete: component versions certified to work together, security fixes maintained across the whole stack, hardened builds, and an escalation path when a production system is failing.

**Get your bearings.** Read the platform overview to see what is included and which components your workload actually needs, so you deploy what you will use. Pick up the operational conventions early from the best practices guide, and set the security baseline before real data lands.

**Route and scale.** Most production topologies rest on two components together. Galera Cluster keeps a synchronous copy of the data on every node, so any node can accept writes. MaxScale sits in front and routes around a node that is gone. A Galera cluster behind MaxScale turns a node failure into a routing event.

**Add analytics when reporting starts to hurt.** When analytical queries begin competing with transactional ones, ColumnStore answers them from a columnar engine in the same platform, reading your operational data without an export.

Start with the platform overview, then follow the component that solves your next problem.

## Understand the Platform

{% content-ref url="../start-with-a-product/%7Bplatform%7D/mariadb-platform-quickstart-guides/mariadb-overview-guide/" %}
[mariadb-overview-guide](../start-with-a-product/%7Bplatform%7D/mariadb-platform-quickstart-guides/mariadb-overview-guide/)
{% endcontent-ref %}

{% content-ref url="../start-with-a-product/%7Bplatform%7D/mariadb-platform-quickstart-guides/mariadb-best-practices-guide/" %}
[mariadb-best-practices-guide](../start-with-a-product/%7Bplatform%7D/mariadb-platform-quickstart-guides/mariadb-best-practices-guide/)
{% endcontent-ref %}

{% content-ref url="../start-with-a-product/%7Bplatform%7D/mariadb-platform-quickstart-guides/security/" %}
[security](../start-with-a-product/%7Bplatform%7D/mariadb-platform-quickstart-guides/security/)
{% endcontent-ref %}

## Route and Scale

{% content-ref url="../start-with-a-product/%7Bmaxscale%7D/maxscale-quickstart-guides/maxscale-beginner-guide/" %}
[maxscale-beginner-guide](../start-with-a-product/%7Bmaxscale%7D/maxscale-quickstart-guides/maxscale-beginner-guide/)
{% endcontent-ref %}

{% content-ref url="../start-with-a-product/%7Bgalera%7D/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide/" %}
[mariadb-galera-cluster-guide](../start-with-a-product/%7Bgalera%7D/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide/)
{% endcontent-ref %}

## Run Analytics in Place

{% content-ref url="../start-with-a-product/%7Banalytics%7D/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide/" %}
[mariadb-columnstore-guide](../start-with-a-product/%7Banalytics%7D/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide/)
{% endcontent-ref %}
