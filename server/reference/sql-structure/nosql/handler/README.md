---
description: >-
  Explore the HANDLER statement in MariaDB Server for direct table access. This
  section details how to bypass the SQL optimizer for low-level row operations,
  useful for specific NoSQL-like interactions.
---

# HANDLER

{% columns %}
{% column %}
{% content-ref url="handler-commands.md" %}
[handler-commands.md](handler-commands.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Access storage engine interfaces directly for key lookups and key or table scans with the HANDLER statement's OPEN, READ, and CLOSE commands.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="handler-for-memory-tables.md" %}
[handler-for-memory-tables.md](handler-for-memory-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use HANDLER commands efficiently with MEMORY/HEAP tables, including creating BTREE keys for range scans and the limitations of HASH keys, BTREE keys, and table scans.
{% endcolumn %}
{% endcolumns %}
