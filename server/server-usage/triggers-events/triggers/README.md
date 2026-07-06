---
description: >-
  Automate actions in MariaDB Server with triggers. Learn how to create and
  manage triggers that execute automatically before or after data modifications,
  ensuring data integrity and business logic enfo
---

# Triggers

{% columns %}
{% column %}
{% content-ref url="trigger-overview.md" %}
[trigger-overview.md](trigger-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete MariaDB triggers overview: BEFORE/AFTER INSERT/UPDATE/DELETE timing, CREATE TRIGGER syntax, FOLLOWS|PRECEDES ordering, and DROP/SHOW TRIGGERS.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="create-trigger.md" %}
[create-trigger.md](create-trigger.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete CREATE TRIGGER reference: OR REPLACE, DEFINER, IF NOT EXISTS, FOLLOWS/PRECEDES options for BEFORE/AFTER INSERT, UPDATE, or DELETE triggers rules.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="trigger-limitations.md" %}
[trigger-limitations.md](trigger-limitations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the constraints of triggers, such as the prohibition of statements that return result sets or explicitly start/commit transactions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="triggers-and-implicit-locks.md" %}
[triggers-and-implicit-locks.md](triggers-and-implicit-locks.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how triggers can cause implicit locks on referenced tables during the execution of a statement, potentially affecting concurrency.
{% endcolumn %}
{% endcolumns %}
