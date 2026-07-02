---
description: >-
  Explore the MyISAM storage engine in MariaDB Server. Understand its
  characteristics, including suitability for read-heavy workloads, and its role
  in specific use cases.
---

# MyISAM

{% columns %}
{% column %}
{% content-ref url="myisam-overview.md" %}
[myisam-overview.md](myisam-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A detailed overview of the MyISAM storage engine, including its file structure, features, and limitations compared to newer engines like Aria.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myisam-index-storage-space.md" %}
[myisam-index-storage-space.md](myisam-index-storage-space.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page explains how MyISAM stores and compresses indexes, detailing space usage for different key types and compression strategies.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myisam-storage-formats.md" %}
[myisam-storage-formats.md](myisam-storage-formats.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the three storage formats supported by MyISAM: FIXED (static), DYNAMIC (variable length), and COMPRESSED (read-only).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myisam-system-variables.md" %}
[myisam-system-variables.md](myisam-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A reference for system variables that configure MyISAM behavior, such as key cache sizes, recovery modes, and concurrent insert settings.
{% endcolumn %}
{% endcolumns %}
