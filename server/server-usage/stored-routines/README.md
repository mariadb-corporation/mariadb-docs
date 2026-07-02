---
description: >-
  Automate tasks in MariaDB Server with stored routines. Learn to create and
  manage stored procedures and functions for enhanced database efficiency and
  code reusability.
---

# Stored Routines

{% columns %}
{% column %}
{% content-ref url="stored-procedures/" %}
[stored-procedures](stored-procedures/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Master stored procedures in MariaDB Server. This section covers creating, executing, and managing these powerful routines to encapsulate complex logic and improve application performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="stored-functions/" %}
[stored-functions](stored-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Utilize stored functions in MariaDB Server. This section details creating, using, and managing user-defined functions to extend SQL capabilities and streamline data manipulation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binary-logging-of-stored-routines.md" %}
[binary-logging-of-stored-routines.md](binary-logging-of-stored-routines.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
When binary logging is enabled, stored routines may require special handling (like SUPER privileges) if they are non-deterministic, to ensure consistent replication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="stored-routine-limitations.md" %}
[stored-routine-limitations.md](stored-routine-limitations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Stored routines have specific restrictions, such as prohibiting certain SQL statements (e.g., LOAD DATA) and disallowing result sets in functions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dbms_output.md" %}
[dbms_output.md](dbms_output.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The DBMS_OUTPUT plugin provides Oracle-compatible output buffering functions (like PUT_LINE), allowing stored procedures to send messages to the client.
{% endcolumn %}
{% endcolumns %}
