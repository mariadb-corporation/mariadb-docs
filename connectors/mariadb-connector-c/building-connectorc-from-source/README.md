---
description: >-
  Build MariaDB Connector/C from source. Download the package from MariaDB
  downloads or get the latest development version from the Connector/C GitHub
  repository.
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

# Building Connector/C From Source

{% columns %}
{% column %}
{% content-ref url="compiling-connectorc.md" %}
[compiling-connectorc.md](compiling-connectorc.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compile MariaDB Connector/C after configuration using CMake on Windows or Unix. Supports Visual Studio builds and GNU make, with both IDE and command-line build options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration-settings-for-building-connectorc.md" %}
[configuration-settings-for-building-connectorc.md](configuration-settings-for-building-connectorc.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure the MariaDB Connector/C build via CMake options including build type, TLS/SSL backend, install prefix, and client plugins such as authentication and connection handlers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="prerequisites-for-building-connectorc-from-source.md" %}
[prerequisites-for-building-connectorc-from-source.md](prerequisites-for-building-connectorc-from-source.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Building MariaDB Connector/C from source requires CMake, a C compiler, and TLS/SSL libraries. Windows needs Visual Studio; Linux and macOS need gcc, with optional Curl or Kerberos.
{% endcolumn %}
{% endcolumns %}
