---
description: >-
  Learn commands for query analysis. This section covers ANALYZE TABLE and
  EXPLAIN, used to view execution plans and optimize query performance.
---

# ANALYZE and EXPLAIN Statements

{% columns %}
{% column %}
{% content-ref url="analyze-format-json.md" %}
[analyze-format-json.md](analyze-format-json.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Gain deep insight into query execution with JSON-formatted analysis. This command combines optimizer estimates with actual runtime statistics for precise performance tuning.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="analyze-formatjson-examples.md" %}
[analyze-formatjson-examples.md](analyze-formatjson-examples.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Review practical examples of ANALYZE FORMAT=JSON output. Learn to identify performance bottlenecks by comparing estimated costs against actual execution metrics.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="analyze-interpreting-rows-and-filtered-members.md" %}
[analyze-interpreting-rows-and-filtered-members.md](analyze-interpreting-rows-and-filtered-members.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the r_rows and r_filtered fields in analysis output. Learn how these actual runtime counters compare to the optimizer's rows and filtered estimates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="analyze-statement.md" %}
[analyze-statement.md](analyze-statement.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn to use the ANALYZE statement to execute a query and produce a performance report. This command reveals how close the optimizer's plan was to the actual execution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="explain-analyze.md" %}
[explain-analyze.md](explain-analyze.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the historical context of EXPLAIN ANALYZE in MariaDB. Learn how this syntax maps to the modern ANALYZE statement for profiling query execution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="explain-format-json.md" %}
[explain-format-json.md](explain-format-json.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Get comprehensive query plans in JSON format. This output provides detailed optimizer data, including costs and attached conditions, not found in the tabular view.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="explain.md" %}
[explain.md](explain.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete EXPLAIN statement reference: SELECT/UPDATE/DELETE syntax, EXTENDED and PARTITIONS options, FORMAT=JSON output, EXPLAIN FOR CONNECTION usage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-buffer-update-algorithm.md" %}
[using-buffer-update-algorithm.md](using-buffer-update-algorithm.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the 'Using buffer' strategy for UPDATE operations. Learn how MariaDB prevents infinite update loops when modifying indexed columns during a range scan.
{% endcolumn %}
{% endcolumns %}
