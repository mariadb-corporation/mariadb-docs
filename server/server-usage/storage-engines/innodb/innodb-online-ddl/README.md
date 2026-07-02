---
description: >-
  Perform online DDL operations with InnoDB in MariaDB Server. Learn how to
  alter tables without blocking read/write access, ensuring high availability
  for your applications.
---

# InnoDB Online DDL

{% columns %}
{% column %}
{% content-ref url="innodb-online-ddl-overview.md" %}
[innodb-online-ddl-overview.md](innodb-online-ddl-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to InnoDB's online DDL capabilities, detailing the ALGORITHM and LOCK clauses for controlling performance and concurrency during schema changes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md" %}
[innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md](innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about operations supported by the INPLACE algorithm, which rebuilds the table but allows concurrent DML, offering a balance between performance and availability.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-online-ddl-operations-with-the-instant-alter-algorithm.md" %}
[innodb-online-ddl-operations-with-the-instant-alter-algorithm.md](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discover the INSTANT algorithm, which modifies table metadata without rebuilding the table, enabling extremely fast schema changes like adding columns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-online-ddl-operations-with-the-nocopy-alter-algorithm.md" %}
[innodb-online-ddl-operations-with-the-nocopy-alter-algorithm.md](innodb-online-ddl-operations-with-the-nocopy-alter-algorithm.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the NOCOPY algorithm, which avoids rebuilding the clustered index for certain operations like adding secondary indexes, significantly reducing I/O.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="instant-add-column-for-innodb.md" %}
[instant-add-column-for-innodb.md](instant-add-column-for-innodb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A focused guide on the Instant ADD COLUMN feature, explaining how it works by modifying metadata and its advantages over traditional table-rebuilding methods.
{% endcolumn %}
{% endcolumns %}
