---
description: >-
  This section covers SQL commands for creating, altering, and dropping stored
  procedures and functions, essential for programmatic database logic.
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
---

# Stored Routine Statements

{% columns %}
{% column %}
{% content-ref url="call.md" %}
[call.md](call.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Invoke a stored procedure. This statement executes a previously created stored procedure, optionally passing parameters and returning results.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="do.md" %}
[do.md](do.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Execute expressions without returning a result set. This statement runs functions or expressions, often used for side effects like releasing locks.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../server-usage/stored-routines/stored-procedures/create-procedure.md" %}
[create-procedure.md](../../../server-usage/stored-routines/stored-procedures/create-procedure.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define a new stored procedure, specifying its name, parameters (`IN`, `OUT`, `INOUT`), and the SQL statements it executes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../server-usage/stored-routines/stored-procedures/alter-procedure.md" %}
[alter-procedure.md](../../../server-usage/stored-routines/stored-procedures/alter-procedure.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Modify the characteristics of an existing stored procedure, such as its security context or comment, without changing its logic.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../server-usage/stored-routines/stored-procedures/drop-procedure.md" %}
[drop-procedure.md](../../../server-usage/stored-routines/stored-procedures/drop-procedure.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove a stored procedure and its associated privileges from the database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../server-usage/stored-routines/stored-functions/drop-function.md" %}
[drop-function.md](../../../server-usage/stored-routines/stored-functions/drop-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove a stored function from the database, deleting its definition and associated privileges.
{% endcolumn %}
{% endcolumns %}
