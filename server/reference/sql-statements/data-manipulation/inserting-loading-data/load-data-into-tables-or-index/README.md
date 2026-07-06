---
description: >-
  Bulk load data efficiently. This section covers commands like LOAD DATA INFILE
  and LOAD XML for high-speed data import from text or XML files.
---

# LOAD Data into Tables or Index

{% columns %}
{% column %}
{% content-ref url="load-data-infile.md" %}
[load-data-infile.md](load-data-infile.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Import rows into a table at high speed from a text file, with control over field and line formatting, column mapping, and duplicate handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="load-index.md" %}
[load-index.md](load-index.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Preload table indexes into the key cache. This command, used for MyISAM tables, loads index blocks into memory to warm up the cache and improve subsequent query performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="load-xml.md" %}
[load-xml.md](load-xml.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Read data from an XML file into a table. This command parses XML content, mapping elements and attributes to table columns for direct data import.
{% endcolumn %}
{% endcolumns %}
