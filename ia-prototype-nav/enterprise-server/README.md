---
title: Server
description: >-
  MariaDB Enterprise Server is the hardened, supported build of MariaDB
  Server, and the database at the core of MariaDB Enterprise Platform.
icon: database
---

# Server

MariaDB Enterprise Server is the build of MariaDB Server that ships under a support contract as part of MariaDB Enterprise Platform. It is the same database and the same SQL as MariaDB Community Server. What differs is how it is built, tested, maintained, and supported.

Three differences matter in practice. Enterprise Server is released on a maintenance schedule with security and correctness fixes backported to supported versions, so you can stay on a version rather than chase releases. Its builds are certified against specific versions of MaxScale, Galera Cluster, and the other Platform components, which is what makes the bundle a tested topology rather than a combination you validate yourself. And some features are exclusive to it, including MariaDB ColumnStore, MariaDB Exa, and the Non-Blocking Operations feature of Galera Cluster.

Because the SQL surface is shared, most of the MariaDB Server documentation applies here without change. Use this space for what is specific to Enterprise Server: the release and support model, the hardened defaults, and the features that are not in Community Server.

**Install and connect.** Installation uses the Enterprise package repository, which requires a customer token. Once installed, connect with the `mariadb` client and confirm the server and its version before configuring anything.

**Configure and secure it.** The guides here cover the configuration and security baselines expected of a supported deployment, which are stricter than the Community Server defaults.

**Understand the release model.** The concepts and reference pages cover how versions are maintained, how long each is supported, and what a backport does and does not include, which is what you need to plan an upgrade window.

Confirm which Enterprise Server version your support agreement covers, then install from the Enterprise repository.

{% content-ref url="{server}/mariadb-quickstart-guides" %}
[Quickstart Guides]({server}/mariadb-quickstart-guides)
{% endcontent-ref %}

{% content-ref url="{server}/server-usage" %}
[Server Usage]({server}/server-usage)
{% endcontent-ref %}

{% content-ref url="{server}/server-management" %}
[Server Management]({server}/server-management)
{% endcontent-ref %}

{% content-ref url="{server}/security" %}
[Security]({server}/security)
{% endcontent-ref %}

{% content-ref url="{server}/architecture" %}
[Architecture]({server}/architecture)
{% endcontent-ref %}

{% content-ref url="{server}/clients-and-utilities" %}
[Clients & Utilities]({server}/clients-and-utilities)
{% endcontent-ref %}

{% content-ref url="{server}/ha-and-performance" %}
[HA & Performance]({server}/ha-and-performance)
{% endcontent-ref %}

{% content-ref url="{server}/reference" %}
[Reference]({server}/reference)
{% endcontent-ref %}
