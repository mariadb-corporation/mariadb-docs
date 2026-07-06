---
description: >-
  Learn about prepared statements in MariaDB Server. This section details how to
  use them for efficient and secure execution of repetitive SQL queries,
  preventing SQL injection vulnerabilities.
---

# Prepared Statements

{% columns %}
{% column %}
{% content-ref url="deallocate-drop-prepare.md" %}
[deallocate-drop-prepare.md](deallocate-drop-prepare.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Release a prepared statement to free resources. This command removes the statement definition and its name from the current session.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="execute-statement.md" %}
[execute-statement.md](execute-statement.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Run a previously prepared statement. This command executes the statement using the specified name, optionally supplying input parameters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="execute-immediate.md" %}
[execute-immediate.md](execute-immediate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Prepare and run a dynamic SQL statement in one step. This command simplifies the process by combining the PREPARE and EXECUTE operations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="prepare-statement.md" %}
[prepare-statement.md](prepare-statement.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Parse and optimize a SQL statement for later use. This command assigns a name to the statement, enabling efficient execution with parameters.
{% endcolumn %}
{% endcolumns %}
