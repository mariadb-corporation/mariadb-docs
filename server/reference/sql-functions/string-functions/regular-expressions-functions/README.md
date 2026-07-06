---
description: >-
  Learn about regular expression functions in MariaDB Server. This section
  details SQL functions for powerful pattern matching and manipulation of string
  data using regular expressions.
---

# Regular Expressions Functions

{% columns %}
{% column %}
{% content-ref url="regular-expressions-overview.md" %}
[regular-expressions-overview.md](regular-expressions-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Get an overview of regex usage. This page introduces the pattern matching capabilities and common metacharacters used in MariaDB regular expressions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pcre.md" %}
[pcre.md](pcre.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand MariaDB's regex support. This concept page explains the PCRE library integration, detailing supported syntax, character classes, and special characters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="regexp.md" %}
[regexp.md](regexp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete REGEXP operator reference: expr REGEXP/RLIKE pat syntax, 1/0/NULL return values, NOT REGEXP aliases, BINARY case-sensitivity, default_regex_flags.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../not-regexp.md" %}
[not-regexp.md](../not-regexp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Negated regular expression matching. This operator tests whether a string does NOT match a specified regular expression pattern.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="regexp_instr.md" %}
[regexp_instr.md](regexp_instr.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the index of a regex match. This function finds the starting position of the first substring that matches the given pattern.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="regexp_replace.md" %}
[regexp_replace.md](regexp_replace.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Replace regex matches in a string. This function substitutes occurrences of a pattern with a specified replacement string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="regexp_substr.md" %}
[regexp_substr.md](regexp_substr.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the substring matching a regex. This function extracts the actual part of the string that matches the given pattern.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rlike.md" %}
[rlike.md](rlike.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for REGEXP. This operator performs a regular expression match against a string argument.
{% endcolumn %}
{% endcolumns %}
