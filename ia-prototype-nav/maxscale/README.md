---
title: MaxScale
description: >-
  MariaDB MaxScale is a database proxy that routes queries, balances
  reads across replicas, and hides failover from your application.
icon: code-branch
---

# MaxScale

MariaDB MaxScale is a database proxy. It sits between your application and your MariaDB servers, accepts connections as though it were the database, and decides which server behind it should answer each query. The application connects to one address and keeps connecting to it while the topology behind changes.

Three jobs follow from that position. MaxScale routes queries, sending writes to the primary and reads to replicas, so read capacity scales by adding replicas rather than by changing application code. It balances those reads across available servers. And it absorbs failover: when a node is lost or promoted, MaxScale reroutes, so the application sees a brief pause instead of a connection error.

**Install and connect.** MaxScale installs from the MariaDB package repository. Configuration is a single file that declares your servers, a monitor that watches their state, and one or more services that define the routing. Once it runs, point your application's connection string at MaxScale instead of at the database.

**Configure the routing you need.** The common setup is read/write splitting, which needs a monitor for the cluster type you run and a router service. Secure the proxy as carefully as the database, because every connection now passes through it and it holds credentials for the servers behind it.

**Understand how it decides.** The concepts pages cover how MaxScale tracks server state, how it classifies a statement as a read or a write, and where that classification can be wrong, which is the detail that matters when a query lands on the wrong server.

Install MaxScale, configure a read/write split against a test cluster, and confirm your application reconnects through it.

{% content-ref url="maxscale-quickstart-guides/README.md" %}
[Quickstart Guides](maxscale-quickstart-guides/README.md)
{% endcontent-ref %}

{% content-ref url="maxscale-architecture/README.md" %}
[MaxScale Architecture](maxscale-architecture/README.md)
{% endcontent-ref %}

{% content-ref url="maxscale-management/README.md" %}
[MaxScale Management](maxscale-management/README.md)
{% endcontent-ref %}

{% content-ref url="maxscale-security/README.md" %}
[MaxScale Security](maxscale-security/README.md)
{% endcontent-ref %}

{% content-ref url="maxscale-use-cases/README.md" %}
[MaxScale Use Cases](maxscale-use-cases/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-maxscale-tutorials/README.md" %}
[Tutorials](mariadb-maxscale-tutorials/README.md)
{% endcontent-ref %}

{% content-ref url="reference/README.md" %}
[Reference](reference/README.md)
{% endcontent-ref %}

{% content-ref url="documentation-no-longer-available.md" %}
[Documentation No Longer Available](documentation-no-longer-available.md)
{% endcontent-ref %}

{% content-ref url="maxscale-old-versions/README.md" %}
[Old MaxScale Versions](maxscale-old-versions/README.md)
{% endcontent-ref %}
