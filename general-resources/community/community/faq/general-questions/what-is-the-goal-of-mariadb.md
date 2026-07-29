# What is the Goal of MariaDB?

To provide a [community](../../README.md) developed, stable, and [always Free](../licensing-questions/mariadb-licenses.md) DBMS that is, on the user level, broadly compatible with MySQL.

We strive for interoperability with both our own, and our upstream, communities.

Until [MariaDB 5.5]({release-notes}/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), MariaDB was kept up to date with the latest MySQL release from the same branch.\
For example [MariaDB 5.1.47]({release-notes}/community-server/old-releases/5.1/5.1.47) was up to date with MySQL 5.1.47, and so on.

We did a merge from the main MySQL branch for every new MySQL release or when\
there was some critical bugfix applied to the main branch.

Since [MariaDB 10.0]({release-notes}/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0), MariaDB includes backported features from MySQL as well as entirely new features not found anywhere else, but does not necessarily include all MySQL features.

We strive to keep our main trees as free from bugs as possible. It should be\
reasonably safe to pull from our trees at any time.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
