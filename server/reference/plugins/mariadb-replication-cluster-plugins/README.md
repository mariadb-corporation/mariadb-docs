---
description: >-
  This section covers plugins specifically designed for high availability and
  clustering, including the wsrep_provider plugin used for Galera Cluster
  integration.
---

# MariaDB Replication & Cluster Plugins

{% columns %}
{% column %}
{% content-ref url="wsrep_info-plugin.md" %}
[wsrep_info-plugin.md](wsrep_info-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The WSREP_INFO plugin adds the WSREP_MEMBERSHIP and WSREP_STATUS tables to the Information Schema, providing detailed insights into Galera Cluster membership and status.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="wsrep_provider.md" %}
[wsrep_provider.md](wsrep_provider.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The wsrep_provider plugin exposes Galera Cluster provider options as individual system variables, allowing for easier configuration and validation of cluster settings.
{% endcolumn %}
{% endcolumns %}
