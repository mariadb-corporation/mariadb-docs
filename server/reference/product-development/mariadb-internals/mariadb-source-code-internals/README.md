---
description: >-
  Serves as the main landing page for articles detailing the low-level source
  code architecture and internal logic of the MariaDB server.
---

# MariaDB Source Code Internals

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

{% columns %}
{% column %}
{% content-ref url="stored-procedure-internals.md" %}
[stored-procedure-internals.md](stored-procedure-internals.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explores the internal implementation and execution flow of stored procedures, including how they are parsed and stored by the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-memory-usage.md" %}
[connect-memory-usage.md](connect-memory-usage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provides a technical breakdown of how the server allocates and manages memory for each client connection and thread.
{% endcolumn %}
{% endcolumns %}
