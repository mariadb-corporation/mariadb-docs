---
description: >-
  Optimize MariaDB Server performance by refining your data structure. This
  section covers schema design, data types, and normalization techniques to
  improve query efficiency and storage utilization.
---

# Optimizing Data Structure

{% columns %}
{% column %}
{% content-ref url="numeric-vs-string-fields.md" %}
[numeric-vs-string-fields.md](numeric-vs-string-fields.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Why choosing numeric over string columns, where possible, improves storage size and comparison speed.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizing-memory-tables.md" %}
[optimizing-memory-tables.md](optimizing-memory-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimizing MEMORY-engine tables, including choosing between B-tree and hash indexes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizing-string-and-character-fields.md" %}
[optimizing-string-and-character-fields.md](optimizing-string-and-character-fields.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimizing string and character columns, including matching character sets and collations for faster comparisons.
{% endcolumn %}
{% endcolumns %}
