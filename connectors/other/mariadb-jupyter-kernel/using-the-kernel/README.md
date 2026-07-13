---
description: General usage information, available features, available magic commands
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Using the MariaDB Jupyter Kernel

{% columns %}
{% column %}
{% content-ref url="general-mariadb-jupyter-kernel-usage-information.md" %}
[general-mariadb-jupyter-kernel-usage-information.md](general-mariadb-jupyter-kernel-usage-information.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
General usage guide for the MariaDB Jupyter Kernel, explaining how to open a notebook, select the kernel, try it via MyBinder, and work with sample notebooks on GitHub.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-jupyter-kernel-magic-commands.md" %}
[mariadb-jupyter-kernel-magic-commands.md](mariadb-jupyter-kernel-magic-commands.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Magic commands reference for the MariaDB Jupyter Kernel, covering `lsmagic`, line/bar/pie plot commands, `df` export, `load`, and the delimiter cell magic.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-jupyter-kernel-restrictions-and-limitations.md" %}
[mariadb-jupyter-kernel-restrictions-and-limitations.md](mariadb-jupyter-kernel-restrictions-and-limitations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Known restrictions of the MariaDB Jupyter Kernel include one SQL statement per cell, single line magic per cell, no mixing of magic and SQL, and required semicolon delimiters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-autocompletion-and-introspection.md" %}
[sql-autocompletion-and-introspection.md](sql-autocompletion-and-introspection.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Jupyter Kernel provides TAB-triggered SQL autocompletion for keywords, databases, tables, columns, and user accounts, plus SHIFT-TAB introspection for schema and function docs.
{% endcolumn %}
{% endcolumns %}
