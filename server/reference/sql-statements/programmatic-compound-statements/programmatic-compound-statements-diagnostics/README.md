---
description: >-
  Learn about diagnostics in programmatic compound statements. This section
  covers error handling and information retrieval within stored procedures and
  functions for effective debugging.
---

# Diagnostics

{% columns %}
{% column %}
{% content-ref url="diagnostics-area.md" %}
[diagnostics-area.md](diagnostics-area.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes the diagnostics area that holds statement and condition information about errors, warnings, and notes produced by an SQL statement, including its properties and how it is populated and cleared.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="get-diagnostics.md" %}
[get-diagnostics.md](get-diagnostics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GET DIAGNOSTICS copies statement and condition information from the diagnostics area into user or local variables, reading properties such as NUMBER, RETURNED_SQLSTATE, MYSQL_ERRNO, and MESSAGE_TEXT.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sqlstate.md" %}
[sqlstate.md](sqlstate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains SQLSTATE, the five-character code identifying SQL error conditions by class and subclass, including the standard success, warning, and not-found classes and how they map to handler keywords.
{% endcolumn %}
{% endcolumns %}
