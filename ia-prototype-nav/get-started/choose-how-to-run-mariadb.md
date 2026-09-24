---
title: Choose How to Run MariaDB
description: >-
  Choose between MariaDB Server, MariaDB Enterprise Platform, and MariaDB
  Cloud by deciding how much of the database you want to run yourself.
icon: signs-post
---

# Choose How to Run MariaDB

MariaDB Server, MariaDB Enterprise Platform, and MariaDB Cloud run the same database. The SQL you write, the storage engines available to you, and most of this documentation apply to every one of them. What differs is who operates the database, and whether a support contract stands behind it.

The decision comes down to one question: who runs it?

**You run it, at no cost.** Choose **MariaDB Server**. It is the open source project, self managed, under no contract. Reach for it to build, to evaluate, or to run on infrastructure you already operate. It is also the server inside the other two, so the time you spend learning it carries forward.

**You run it, with support.** Choose **MariaDB Enterprise Platform**, the supported MariaDB product. You still operate the database, and you get a support contract, hardened builds, and the routing, clustering, analytics, and management components bundled and certified against each other. Reach for it when you run production yourself and want a tested topology and an escalation path. Note that MariaDB ColumnStore and MariaDB Exa require MariaDB Enterprise Server, so analytical workloads on those engines need MariaDB Enterprise Platform or MariaDB Cloud.

**Someone else runs it.** Choose **MariaDB Cloud**. You provision a database and the service handles hardware, updates, backups, and availability. Reach for it when you would rather build on the database than operate it, or when you need to scale without adding operations staff.

Moving between them later is a supported path, not a rebuild. Because all three run the same server and share the same client tools, you can prototype on MariaDB Server, launch on MariaDB Cloud, and adopt MariaDB Enterprise Platform afterward without rewriting the application.

Server, MariaDB Platform, and Cloud each have a starting page that states what running it involves. Read the one you are leaning toward before you commit.

## Compare Server, MariaDB Platform, and Cloud

{% content-ref url="explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/installing-mariadb-server-guide/" %}
[installing-mariadb-server-guide](explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/installing-mariadb-server-guide/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bplatform%7D/mariadb-platform-quickstart-guides/mariadb-overview-guide/" %}
[mariadb-overview-guide](explore-by-task/%7Bplatform%7D/mariadb-platform-quickstart-guides/mariadb-overview-guide/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bmariadb-cloud%7D/quickstart/using-the-portal/" %}
[using-the-portal](explore-by-task/%7Bmariadb-cloud%7D/quickstart/using-the-portal/)
{% endcontent-ref %}

## Choosing a Storage Engine?

{% content-ref url="explore-by-task/%7Bserver%7D/server-usage/storage-engines/choosing-the-right-storage-engine/" %}
[choosing-the-right-storage-engine](explore-by-task/%7Bserver%7D/server-usage/storage-engines/choosing-the-right-storage-engine/)
{% endcontent-ref %}
