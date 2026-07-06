---
description: >-
  Optimizer trace, which records how the optimizer builds a query's execution
  plan.
---

# Optimizer Trace

{% columns %}
{% column %}
{% content-ref url="basic-optimizer-trace-example.md" %}
[basic-optimizer-trace-example.md](basic-optimizer-trace-example.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Shows a complete optimizer trace example, from enabling optimizer_trace to reading the resulting JSON from INFORMATION_SCHEMA.OPTIMIZER_TRACE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="how-to-collect-large-optimizer-traces.md" %}
[how-to-collect-large-optimizer-traces.md](how-to-collect-large-optimizer-traces.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to collect large optimizer traces by raising max_allowed_packet and optimizer_trace_max_mem_size.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-trace-for-developers.md" %}
[optimizer-trace-for-developers.md](optimizer-trace-for-developers.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provides guidelines for server developers on what and how to write to the optimizer trace, including keeping the JSON valid.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-trace-guide.md" %}
[optimizer-trace-guide.md](optimizer-trace-guide.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guides you through reading the JSON optimizer trace, using a simple query to illustrate the join_preparation and join_optimization steps.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-trace-overview.md" %}
[optimizer-trace-overview.md](optimizer-trace-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduces optimizer trace, which produces a JSON document of the optimizer's decisions for SELECT/UPDATE/DELETE queries, its system variables, and the INFORMATION_SCHEMA.OPTIMIZER_TRACE table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-trace-resources.md" %}
[optimizer-trace-resources.md](optimizer-trace-resources.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Links to external optimizer trace resources, including a MariaDB Fest 2020 walkthrough talk and the opttrace processing tool.
{% endcolumn %}
{% endcolumns %}
