---
description: >-
  Manage InnoDB tablespaces in MariaDB Server. Understand their role in data
  organization, performance, and recovery, including file-per-table and shared
  tablespaces.
---

# InnoDB Tablespaces

{% columns %}
{% column %}
{% content-ref url="innodb-file-per-table-tablespaces.md" %}
[innodb-file-per-table-tablespaces.md](innodb-file-per-table-tablespaces.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to configure InnoDB to store each table in its own .ibd file, enabling features like table compression and easier space reclamation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-system-tablespaces.md" %}
[innodb-system-tablespaces.md](innodb-system-tablespaces.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page explains the InnoDB system tablespace (ibdata1), which stores the data dictionary, doublewrite buffer, and undo logs, and how to resize it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-temporary-tablespaces.md" %}
[innodb-temporary-tablespaces.md](innodb-temporary-tablespaces.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page explains how InnoDB manages temporary tablespaces for non-compressed temporary tables, including configuration and sizing options.
{% endcolumn %}
{% endcolumns %}
