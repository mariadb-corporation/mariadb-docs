---
description: >-
  Learn about arithmetic operators in MariaDB Server SQL. This section details
  how to perform mathematical calculations like addition, subtraction,
  multiplication, and division within your queries.
---

# Arithmetic Operators

{% columns %}
{% column %}
{% content-ref url="addition-operator.md" %}
[addition-operator.md](addition-operator.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Add two operands with the + operator, calculating integer results at BIGINT precision and letting the highest-precision operand determine the result type for real or string values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subtraction-operator.md" %}
[subtraction-operator.md](subtraction-operator.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Subtract one operand from another with the - operator, which also serves as the unary minus for changing sign, computing integer results at BIGINT precision.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="multiplication-operator.md" %}
[multiplication-operator.md](multiplication-operator.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Multiply two operands with the * operator.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="division-operator.md" %}
[division-operator.md](division-operator.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Divide operands with the / operator, returning NULL on division by zero and controlling decimal digits with the div_precision_increment system variable.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="modulo-operator.md" %}
[modulo-operator.md](modulo-operator.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the remainder of N divided by M with the % modulo operator.
{% endcolumn %}
{% endcolumns %}
