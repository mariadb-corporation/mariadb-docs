---
description: >-
  Compile MariaDB Server with extra modules and options. This section details
  how to customize your build from source, enabling specific features or
  optimizations for your deployment.
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
---

# Compiling MariaDB with Extra Modules/Options

{% columns %}
{% column %}
{% content-ref url="specifying-which-plugins-to-build.md" %}
[specifying-which-plugins-to-build.md](specifying-which-plugins-to-build.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to use CMake options like `PLUGIN_xxx` to control which plugins are built statically, dynamically, or not at all during compilation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-mariadb-with-tcmalloc-or-jemalloc.md" %}
[using-mariadb-with-tcmalloc-or-jemalloc.md](using-mariadb-with-tcmalloc-or-jemalloc.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions on building and configuring MariaDB to use alternative memory allocators like TCMalloc or jemalloc for improved performance and profiling.
{% endcolumn %}
{% endcolumns %}
