---
description: >-
  Learn about logical operators in MariaDB Server SQL. This section details
  operators like AND, OR, and NOT used to combine or negate conditions,
  essential for complex filtering and data selection.
---

# Logical Operators

{% columns %}
{% column %}
{% content-ref url="and.md" %}
[and.md](and.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Evaluate logical AND with AND or &&, returning 1 when all operands are non-zero and not NULL, 0 when any operand is 0, and NULL otherwise.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="not.md" %}
[not.md](not.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Negate an operand with logical NOT or !, returning 1 for 0, 0 for non-zero values, and NULL for NULL, with precedence affected by the HIGH_NOT_PRECEDENCE SQL_MODE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="or.md" %}
[or.md](or.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Evaluate logical OR with OR or ||, returning 1 when any operand is non-zero and handling NULL operands per SQL logic; || concatenates strings under PIPES_AS_CONCAT.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="xor.md" %}
[xor.md](xor.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Evaluate exclusive OR with XOR, returning NULL if either operand is NULL and otherwise 1 when an odd number of operands is non-zero.
{% endcolumn %}
{% endcolumns %}
