---
description: >-
  Extend Mroonga's functionality in MariaDB Server with user-defined functions.
  Learn how to create custom functions to enhance full-text search and data
  processing capabilities.
---

# Mroonga User-Defined Functions

{% columns %}
{% column %}
{% content-ref url="creating-mroonga-user-defined-functions.md" %}
[creating-mroonga-user-defined-functions.md](creating-mroonga-user-defined-functions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions on how to manually create Mroonga's UDFs if they were not automatically installed, ensuring full functionality.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="last_insert_grn_id.md" %}
[last_insert_grn_id.md](last_insert_grn_id.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This UDF returns the unique ID assigned by Groonga for the last inserted record, useful for tracking internal record identifiers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mroonga_command.md" %}
[mroonga_command.md](mroonga_command.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Execute raw Groonga commands directly from MariaDB using this UDF, allowing for advanced administration and inspection of the Groonga database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mroonga_escape.md" %}
[mroonga_escape.md](mroonga_escape.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This function escapes special characters in a string to make it safe for use in Mroonga full-text search queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mroonga_highlight_html.md" %}
[mroonga_highlight_html.md](mroonga_highlight_html.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Highlight keywords within a text string using HTML tags, making it easy to display search results with matched terms emphasized.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mroonga_normalize.md" %}
[mroonga_normalize.md](mroonga_normalize.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This UDF normalizes a given string using Groonga's normalizers, ensuring consistent text processing for accurate indexing and searching.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mroonga_snippet.md" %}
[mroonga_snippet.md](mroonga_snippet.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This function extracts a snippet of text surrounding a keyword from a document, providing necessary context for search result displays.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mroonga_snippet_html.md" %}
[mroonga_snippet_html.md](mroonga_snippet_html.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Similar to mroonga_snippet, this function generates HTML-formatted snippets, automatically wrapping matched keywords in tags for web display.
{% endcolumn %}
{% endcolumns %}
