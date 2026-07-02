---
description: The CONNECT storage engine.
---

# CONNECT

You can download a PDF version of the CONNECT documentation (1.7.0003):

{% file src="../../../.gitbook/assets/connect_1_7_03.pdf" %}

| Connect Version   | Introduced                                                                                                                                                                                                                                                                                                                                                                                                                                             | Maturity |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| Connect 1.07.0002 | [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.9), [MariaDB 10.4.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.18), [MariaDB 10.3.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.28), [MariaDB 10.2.36](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.36)   | Stable   |
| Connect 1.07.0001 | [MariaDB 10.4.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.12), [MariaDB 10.3.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.22), [MariaDB 10.2.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.31), [MariaDB 10.1.44](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.44) | Stable   |
| Connect 1.06.0010 | [MariaDB 10.4.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.8), [MariaDB 10.3.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.18), [MariaDB 10.2.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.27)                                                                                                                 | Stable   |
| Connect 1.06.0007 | [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.6), [MariaDB 10.2.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.14), [MariaDB 10.1.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.33)                                                                                                                 | Stable   |
| Connect 1.06.0005 | [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.3), [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.10), [MariaDB 10.1.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.29)                                                                                                                 | Stable   |
| Connect 1.06.0004 | [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.2), [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.9), [MariaDB 10.1.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.28)                                                                                                                   | Stable   |
| Connect 1.06.0001 | [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.1), [MariaDB 10.2.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.8), [MariaDB 10.1.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.24)                                                                                                                   | Beta     |
| Connect 1.05.0003 | [MariaDB 10.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.0), [MariaDB 10.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.5), [MariaDB 10.1.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.22)                                                                                                                   | Stable   |
| Connect 1.05.0001 | [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4), [MariaDB 10.1.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.21)                                                                                                                                                                                                                               | Stable   |
| Connect 1.04.0008 | [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.2), [MariaDB 10.1.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.17)                                                                                                                                                                                                                               | Stable   |
| Connect 1.04.0006 | [MariaDB 10.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.0), [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.13),                                                                                                                                                                                                                              | Stable   |
| Connect 1.04.0005 | [MariaDB 10.1.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.10)                                                                                                                                                                                                                                                                                                                                           | Beta     |
| Connect 1.04.0003 | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                             | Beta     |

The CONNECT storage engine enables MariaDB to access external local or remote data (MED). This is done by defining tables based on different data types, in particular files in various formats, data extracted from other DBMS or products (such as Excel or MongoDB) via ODBC or JDBC, or data retrieved from the environment (for example DIR, WMI, and MAC tables)

This storage engine supports table partitioning, MariaDB virtual columns and permits defining _special_ columns such as `ROWID`, `FILEID`, and `SERVID`.

No precise definition of maturity exists. Because CONNECT handles many table types, each type has a different maturity depending on whether it is old and well-tested, less well-tested or newly implemented. This is indicated for all data types.

{% columns %}
{% column %}
{% content-ref url="introduction-to-the-connect-engine.md" %}
[introduction-to-the-connect-engine.md](introduction-to-the-connect-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-connect/" %}
[using-connect](using-connect/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-the-connect-storage-engine.md" %}
[installing-the-connect-storage-engine.md](installing-the-connect-storage-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-create-table-options.md" %}
[connect-create-table-options.md](connect-create-table-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-data-types.md" %}
[connect-data-types.md](connect-data-types.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-table-types/" %}
[connect-table-types](connect-table-types/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-security.md" %}
[connect-security.md](connect-security.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-system-variables.md" %}
[connect-system-variables.md](connect-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine has been deprecated.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-adding-the-rest-feature-as-a-library-called-by-an-oem-table.md" %}
[connect-adding-the-rest-feature-as-a-library-called-by-an-oem-table.md](connect-adding-the-rest-feature-as-a-library-called-by-an-oem-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-compiling-json-udfs-in-a-separate-library.md" %}
[connect-compiling-json-udfs-in-a-separate-library.md](connect-compiling-json-udfs-in-a-separate-library.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-making-the-getrest-library.md" %}
[connect-making-the-getrest-library.md](connect-making-the-getrest-library.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-oem-table-example.md" %}
[connect-oem-table-example.md](connect-oem-table-example.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="current-status-of-the-connect-handler.md" %}
[current-status-of-the-connect-handler.md](current-status-of-the-connect-handler.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="json-sample-files.md" %}
[json-sample-files.md](json-sample-files.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}
