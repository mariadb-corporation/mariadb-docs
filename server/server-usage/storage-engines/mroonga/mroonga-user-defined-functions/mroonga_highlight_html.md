---
description: >-
  Highlight keywords within a text string using HTML tags, making it easy to
  display search results with matched terms emphasized.
---

# mroonga\_highlight\_html

## Syntax

```
mroonga_highlight_html(text[[, query AS query]])

mroonga_highlight_html(text[[, keyword1, ..., keywordN]])
```

## Description

`mroonga_highlight_html` is a [user-defined function](../../../user-defined-functions/) (UDF) included with the [Mroonga storage engine](../). It highlights the specified keywords in the target text. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.

The optional parameter can either be one or more _keywords_, or a Groonga _query_.

The function highlights the specified keywords in the target text by surrounding each keyword with `<span class="keyword">...</span>`, and escaping special HTML characters such as `<` and `>`.

Returns highlighted HTML.

## Examples

```sql
SELECT mroonga_highlight_html('<p>MariaDB includes the Mroonga storage engine</p>.') 
  AS highlighted_html;
+-----------------------------------------------------------------+
| highlighted_html                                                |
+-----------------------------------------------------------------+
| &lt;p&gt;MariaDB includes the Mroonga storage engine&lt;/p&gt;. |
+-----------------------------------------------------------------+
```

Highlighting the words `MariaDB` and `Mroonga` in a given text:

```sql
SELECT mroonga_highlight_html('MariaDB includes the Mroonga storage engine.', 'MariaDB', 'Mroonga') 
  AS highlighted_html;
+--------------------------------------------------------------------------------------------------------+
| highlighted_html                                                                                       |
+--------------------------------------------------------------------------------------------------------+
| <span class="keyword">MariaDB</span> includes the <span class="keyword">Mroonga</span> storage engine. |
+--------------------------------------------------------------------------------------------------------+
```

The same outcome, formulated as a Groonga query:

```sql
SELECT mroonga_highlight_html('MariaDB includes the Mroonga storage engine.', 'MariaDB OR Mroonga' 
  AS query) AS highlighted_text;
+--------------------------------------------------------------------------------------------------------+
| highlighted_text                                                                                       |
+--------------------------------------------------------------------------------------------------------+
| <span class="keyword">MariaDB</span> includes the <span class="keyword">Mroonga</span> storage engine. |
+--------------------------------------------------------------------------------------------------------+
```

## See Also

* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
