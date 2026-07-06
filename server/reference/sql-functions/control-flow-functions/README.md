---
description: >-
  Learn about control flow functions in MariaDB Server. This section details SQL
  functions like IF, CASE, and NULLIF, which enable conditional logic within
  your queries and stored routines.
---

# Control Flow Functions

{% columns %}
{% column %}
{% content-ref url="case-operator.md" %}
[case-operator.md](case-operator.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Implement conditional logic in SQL queries. This operator evaluates conditions and returns a specific value when the first true condition is met.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="decode_oracle.md" %}
[decode_oracle.md](decode_oracle.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compare a value against a list of conditions. This Oracle-compatible function returns a corresponding result when a match is found, or a default value otherwise.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="if-function.md" %}
[if-function.md](if-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete IF() function reference: IF(expr1,expr2,expr3) conditional syntax, TRUE/NULL evaluation rules, return type context (numeric/string), and examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ifnull.md" %}
[ifnull.md](ifnull.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Replace NULL values with a fallback. This function returns the first argument if it's not NULL; otherwise, it returns the specified replacement value.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="nullif.md" %}
[nullif.md](nullif.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compare two expressions and return NULL if they are equal. If the expressions differ, the function returns the first expression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="nvl.md" %}
[nvl.md](nvl.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for IFNULL. This Oracle-compatible function returns the first argument if it is not NULL, or the second argument if the first is NULL.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="nvl2.md" %}
[nvl2.md](nvl2.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return values based on NULL status. This function returns the second argument if the first is not NULL, and the third argument if the first is NULL.
{% endcolumn %}
{% endcolumns %}
