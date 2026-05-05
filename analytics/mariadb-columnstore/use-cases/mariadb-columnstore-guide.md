---
description: >-
  MariaDB ColumnStore is a columnar storage engine ported from InfiniDB 4.6.7,
  designed for petabyte-scale analytics with linear scalability, columnar
  compression, and partitioning.
---

# About MariaDB ColumnStore

MariaDB ColumnStore is a columnar storage engine that utilizes a massively parallel distributed data architecture. It's a columnar storage system built by porting InfiniDB 4.6.7 to MariaDB and released under the GPL license.

[MariaDB 10.5.4 ](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1054-release-notes)is available as a storage engine for MariaDB Server. Before then, it is available as a separate download.

{% hint style="info" %}
Release notes and other documentation for ColumnStore is also available in the Enterprise docs section of the MariaDB website. For example:

* [ColumnStore 23.10 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/23.10)
* [ColumnStore 23.02 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/23.02)
* [ColumnStore 22.08 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/22.08)
* [ColumnStore 6 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/old-releases/mariadb-columnstore-6-release-notes)
* [ColumnStore 5.6 Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore/old-releases/mariadb-columnstore-5-6-release-notes)
* [Deployment Instructions](../architecture/columnstore-architectural-overview.md#mariadb-enterprise-columnstore)
{% endhint %}

It is designed for big data scaling to process petabytes of data, linear scalability, and exceptional performance with real-time response to analytical queries. It leverages the I/O benefits of columnar storage, compression, just-in-time projection, and horizontal and vertical partitioning to deliver tremendous performance when analyzing large data sets.

Links:

* [MariaDB Columnstore Blogs](https://mariadb.com/resources/blog/tag/columnstore/).
* A Google Group exists for MariaDB ColumnStore that can be used to discuss ideas and issues and communicate with the community: Send email to mariadb-columnstore@googlegroups.com or use the [forum interface](https://groups.google.com/forum/#!forum/mariadb-columnstore)
* Bugs can be reported in MariaDB Jira: [jira.mariadb.org](https://jira.mariadb.org) (see [Reporting Bugs](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/reporting-bugs)). Please file bugs under the MCOL project and include the output from the [support utility](../management/system-troubleshooting-mariadb-columnstore.md) if possible.

MariaDB ColumnStore is released under the GPL license.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
