---
description: >-
  Read and write data in GridGain 9 — the Table API, tables from Java classes, SQL, transactions, continuous queries, data streaming, and data archiving.
---

# Data Access

{% columns %}
{% column %}
{% content-ref url="../table-api.md" %}
[Table API](../table-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Execute table operations in GridGain 9 with RecordView and KeyValueView, map user objects to table tuples, run criterion queries, and use the partition API.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../tables-from-java-classes.md" %}
[Tables from Java Classes](../tables-from-java-classes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create tables, zones, and indexes directly from Java POJOs using the GridGain 9 catalog API, with annotation-based and builder-based examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../sql/" %}
[Working with SQL](../sql/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Work with SQL in GridGain 9 through the Apache Calcite-based SQL engine, the Java SQL API, and the ODBC driver.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../transactions.md" %}
[Transactions](../transactions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Perform explicit and implicit transactions in GridGain 9 — lifecycle, isolation, read-only transactions, timeouts, labels, and runInTransaction.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../continuous-queries.md" %}
[Continuous Queries](../continuous-queries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Monitor data modifications in a GridGain 9 table with continuous queries — subscribers, watermarks, dedicated executors, remote filters, and event types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-streaming.md" %}
[Data Streaming](../data-streaming.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Load large volumes of data into a GridGain 9 cluster with the Data Streamer API, configure batching and flushing, use receivers, and track failed entries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-archiving.md" %}
[Data Archiving](../data-archiving.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How data archiving in GridGain 9 removes aged data from primary storage after moving it to secondary storage for HTAP workloads.
{% endcolumn %}
{% endcolumns %}
