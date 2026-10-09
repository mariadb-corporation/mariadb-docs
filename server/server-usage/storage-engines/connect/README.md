---
description: The CONNECT storage engine.
---

# CONNECT

{% hint style="info" %}
CONNECT is a community contribution to MariaDB Server, developed and maintained by its contributor, Olivier Bertrand.
{% endhint %}

You can download a PDF version of the CONNECT documentation (1.7.0003):

{% file src="../../../.gitbook/assets/connect_1_7_03.pdf" %}


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
Reference for the system variables that configure the CONNECT storage engine.
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
