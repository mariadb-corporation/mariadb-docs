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

{% content-ref url="{maxscale}/maxscale-quickstart-guides" %}
[Quickstart Guides]({maxscale}/maxscale-quickstart-guides)
{% endcontent-ref %}

{% content-ref url="{maxscale}/maxscale-architecture" %}
[MaxScale Architecture]({maxscale}/maxscale-architecture)
{% endcontent-ref %}

{% content-ref url="{maxscale}/maxscale-management" %}
[MaxScale Management]({maxscale}/maxscale-management)
{% endcontent-ref %}

{% content-ref url="{maxscale}/maxscale-security" %}
[MaxScale Security]({maxscale}/maxscale-security)
{% endcontent-ref %}

{% content-ref url="{maxscale}/maxscale-use-cases" %}
[MaxScale Use Cases]({maxscale}/maxscale-use-cases)
{% endcontent-ref %}

{% content-ref url="{maxscale}/mariadb-maxscale-tutorials" %}
[Tutorials]({maxscale}/mariadb-maxscale-tutorials)
{% endcontent-ref %}

{% content-ref url="{maxscale}/reference" %}
[Reference]({maxscale}/reference)
{% endcontent-ref %}

{% content-ref url="{maxscale}/documentation-no-longer-available" %}
[Documentation No Longer Available]({maxscale}/documentation-no-longer-available)
{% endcontent-ref %}

{% content-ref url="{maxscale}/maxscale-old-versions" %}
[Old MaxScale Versions]({maxscale}/maxscale-old-versions)
{% endcontent-ref %}
