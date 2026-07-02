---
description: >-
  Learn about cursors in MariaDB Server's programmatic compound statements. This
  section details how to iterate over result sets row-by-row within stored
  procedures and functions.
---

# Cursors

{% columns %}
{% column %}
{% content-ref url="cursor-overview.md" %}
[cursor-overview.md](cursor-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduces cursors in MariaDB stored programs, which are non-scrollable, read-only, and asensitive, and are declared, opened, fetched from, and closed to process result rows sequentially.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="close.md" %}
[close.md](close.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
CLOSE closes a previously opened cursor, raising an error if it was not open; if not closed explicitly, a cursor closes at the end of its enclosing compound statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="declare-cursor.md" %}
[declare-cursor.md](declare-cursor.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
DECLARE CURSOR declares a named cursor for a SELECT or, from MariaDB 12.3, a prepared statement name, optionally with parameters, for use within a stored program.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="fetch.md" %}
[fetch.md](fetch.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
FETCH retrieves the next row from an open cursor into local variables and advances the cursor, raising a No Data condition (SQLSTATE 02000) when no more rows remain.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="open.md" %}
[open.md](open.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
OPEN opens a previously declared cursor and executes its associated query, optionally binding variables or expressions, so that rows can be fetched.
{% endcolumn %}
{% endcolumns %}
