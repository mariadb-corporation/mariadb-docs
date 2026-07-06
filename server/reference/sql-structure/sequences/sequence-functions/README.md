---
description: >-
  Learn about sequence functions in MariaDB Server. This section details SQL
  functions for retrieving the next or current value from a sequence, crucial
  for generating unique identifiers.
---

# SEQUENCE Functions

{% columns %}
{% column %}
{% content-ref url="lastval.md" %}
[lastval.md](lastval.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
LASTVAL is a synonym for PREVIOUS VALUE FOR, returning the most recent value generated from a sequence in the current connection.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="next-value-for-sequence_name.md" %}
[next-value-for-sequence_name.md](next-value-for-sequence_name.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Generate the next value of a sequence with NEXT VALUE FOR (ANSI SQL), NEXTVAL() (PostgreSQL), or sequence_name.nextval in Oracle mode.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="nextval.md" %}
[nextval.md](nextval.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NEXTVAL is a synonym for NEXT VALUE FOR, generating the next value of a sequence.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="previous-value-for-sequence_name.md" %}
[previous-value-for-sequence_name.md](previous-value-for-sequence_name.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Get the most recent value generated from a sequence in the current connection with PREVIOUS VALUE FOR (DB2), LASTVAL() (PostgreSQL), or sequence_name.currval in Oracle mode.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setval.md" %}
[setval.md](setval.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set the next value returned by a sequence with SETVAL(), a PostgreSQL-compatible function extended with is_used and round arguments that never lowers the sequence below its current value.
{% endcolumn %}
{% endcolumns %}
