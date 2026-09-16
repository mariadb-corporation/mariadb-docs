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

## Get Started

{% content-ref url="get-started/install-maxscale.md" %}
[install-maxscale.md](get-started/install-maxscale.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-maxscale.md" %}
[connect-to-maxscale.md](get-started/connect-to-maxscale.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/maxscale-tutorial.md" %}
[maxscale-tutorial.md](tutorials/maxscale-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-maxscale.md" %}
[configure-maxscale.md](how-to-guides/configure-maxscale.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-maxscale.md" %}
[secure-maxscale.md](how-to-guides/secure-maxscale.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-maxscale.md" %}
[what-is-maxscale.md](overview/what-is-maxscale.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-maxscale-works.md" %}
[how-maxscale-works.md](concepts/how-maxscale-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/maxscale-reference.md" %}
[maxscale-reference.md](reference/maxscale-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/maxscale-releases.md" %}
[maxscale-releases.md](release-notes/maxscale-releases.md)
{% endcontent-ref %}
