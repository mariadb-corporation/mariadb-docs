---
description: >-
  Explore InnoDB row formats in MariaDB Server. Understand different formats
  like Compact, Dynamic, and Compressed, and how they impact storage efficiency
  and performance for your data.
---

# InnoDB Row Formats

{% columns %}
{% column %}
{% content-ref url="innodb-row-formats-overview.md" %}
[innodb-row-formats-overview.md](innodb-row-formats-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An overview of the four InnoDB row formats (REDUNDANT, COMPACT, DYNAMIC, COMPRESSED), comparing their storage efficiency and feature support.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-compact-row-format.md" %}
[innodb-compact-row-format.md](innodb-compact-row-format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Detailed information on the COMPACT row format, which reduces storage space by roughly 20% compared to REDUNDANT, handling NULLs and variable-length columns efficiently.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-compressed-row-format.md" %}
[innodb-compressed-row-format.md](innodb-compressed-row-format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the COMPRESSED row format, which compresses data and index pages using algorithms like zlib to minimize storage footprint at the cost of CPU.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-dynamic-row-format.md" %}
[innodb-dynamic-row-format.md](innodb-dynamic-row-format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The DYNAMIC row format, default in modern MariaDB versions, optimizes storage for large BLOB/TEXT columns by storing them on separate overflow pages.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-redundant-row-format.md" %}
[innodb-redundant-row-format.md](innodb-redundant-row-format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Information on the legacy REDUNDANT row format, primarily maintained for backward compatibility with older MySQL versions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="troubleshooting-row-size-too-large-errors-with-innodb.md" %}
[troubleshooting-row-size-too-large-errors-with-innodb.md](troubleshooting-row-size-too-large-errors-with-innodb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete InnoDB row size troubleshooting: innodb_strict_mode, ALTER TABLE ROW_FORMAT=DYNAMIC, VARCHAR/VARBINARY(256) overflow, and BLOB/TEXT solutions.
{% endcolumn %}
{% endcolumns %}
