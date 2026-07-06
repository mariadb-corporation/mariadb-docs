---
description: >-
  Utilize stored functions in MariaDB Server. This section details creating,
  using, and managing user-defined functions to extend SQL capabilities and
  streamline data manipulation.
---

# Stored Functions

{% columns %}
{% column %}
{% content-ref url="stored-function-overview.md" %}
[stored-function-overview.md](stored-function-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A Stored Function is a set of SQL statements that can be called by name, accepts parameters, and returns a single value, enhancing SQL with custom logic.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="stored-aggregate-functions.md" %}
[stored-aggregate-functions.md](stored-aggregate-functions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Stored Aggregate Functions allow users to create custom aggregate functions that process a sequence of rows and return a single summary result.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="stored-routine-privileges.md" %}
[stored-routine-privileges.md](stored-routine-privileges.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page explains the privileges required to create, alter, execute, and drop stored routines, including the automatic grants for creators.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-function.md" %}
[drop-function.md](drop-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The DROP FUNCTION statement removes a stored function from the database, deleting its definition and associated privileges.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="stored-function-limitations.md" %}
[stored-function-limitations.md](stored-function-limitations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page details the restrictions on stored functions, such as the inability to return result sets or use transaction control statements.
{% endcolumn %}
{% endcolumns %}
