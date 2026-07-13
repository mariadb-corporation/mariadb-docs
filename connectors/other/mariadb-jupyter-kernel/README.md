---
description: >-
  The MariaDB Jupyter Kernel lets you run MariaDB directly in Jupyter notebooks.
  Execute SQL, visualize results with magic commands, and integrate with Python
  for data analysis.
icon: link
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

# The MariaDB Jupyter kernel

{% columns %}
{% column %}
{% content-ref url="mariadb-juypter-kernel-guide.md" %}
[mariadb-juypter-kernel-guide.md](mariadb-juypter-kernel-guide.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Jupyter Kernel is an open-source Jupyter kernel that enables running MariaDB SQL directly in notebooks, with support for autocompletion, magic commands, and charting.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="changes-in-mariadb-jupyter-kernel.md" %}
[changes-in-mariadb-jupyter-kernel.md](changes-in-mariadb-jupyter-kernel.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Release history for the MariaDB Jupyter Kernel, covering SQL autocompletion, code introspection, multi-notebook server management, and other fixes from v0.1.0 onward.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-the-mariadb-jupyter-kernel.md" %}
[configuring-the-mariadb-jupyter-kernel.md](configuring-the-mariadb-jupyter-kernel.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Jupyter Kernel reads connection settings from a JSON config file, supporting options for host, port, credentials, server binary paths, and auto-start behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="contributing-to-the-mariadb-jupyter-kernel-project.md" %}
[contributing-to-the-mariadb-jupyter-kernel-project.md](contributing-to-the-mariadb-jupyter-kernel-project.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Contributing guide for the MariaDB Jupyter Kernel project, covering how to set up a development environment, run tests, format code, and add new magic commands.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-jupyter-kernel-installation.md" %}
[mariadb-jupyter-kernel-installation.md](mariadb-jupyter-kernel-installation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install the MariaDB Jupyter Kernel via pip using either a quick setup for existing environments or a complete Miniconda-based setup, with platform support notes for Linux and macOS.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="the-mariadb-jupyter-kernel-main-components-and-architecture.md" %}
[the-mariadb-jupyter-kernel-main-components-and-architecture.md](the-mariadb-jupyter-kernel-main-components-and-architecture.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Jupyter Kernel architecture and component reference, describing how MariaDBKernel, MariaDBClient, CodeParser, MagicFactory, and related classes interact at runtime.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-the-kernel/README.md" %}
[using-the-kernel](using-the-kernel/README.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
General usage information for the MariaDB Jupyter Kernel, including available features and magic commands.
{% endcolumn %}
{% endcolumns %}
