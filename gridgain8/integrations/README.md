---
description: >-
  Integrate GridGain 8 with third-party systems and frameworks, including Apache
  Kafka, Oracle GoldenGate, the Data Lake Accelerator, Apache Spark, geospatial
  SQL, and AI frameworks.
icon: wrench
---

# Integrations

You can combine GridGain 8 with third-party solutions to improve performance or to combine GridGain's strengths with the adaptability provided by other platforms. For example, you can permanently store data received from Apache Kafka, replicate data with Oracle GoldenGate, or accelerate access to a data lake. After you configure your clusters, use an extension to simplify connecting to a third-party solution.

- [Kafka Connector](kafka/README.md) — stream data between GridGain and Apache Kafka with the Certified Kafka Connector.
- [Oracle GoldenGate](oracle-goldengate/README.md) — replicate data into GridGain with the GridGain GoldenGate handler.
- [Data Lake Accelerator](data-lake-accelerator/README.md) — load and synchronize data between GridGain and a data lake.
- [GridGain for Spark](spark/README.md) — share GridGain data with Apache Spark through IgniteContext, IgniteRDD, and GridGain DataFrames.
- [Geospatial SQL Capabilities](geospatial-sql.md) — query and index geometry data types with spatial SQL.
- [AI Integration](ai/README.md) — use GridGain as a vector store and feature store with LangChain, Langflow, and Feast.
- [Apache Ignite Extensions](apache-ignite-extensions.md) — streaming extension modules from Apache Ignite that work with GridGain.

{% columns %}
{% column %}
{% content-ref url="kafka/" %}
[Kafka Connector](kafka/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Stream data between GridGain 8 and Apache Kafka with the Certified Kafka Connector — quick start, architecture, data schema, configuration, and monitoring.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="oracle-goldengate/" %}
[Oracle GoldenGate](oracle-goldengate/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Replicate data into GridGain 8 using Oracle GoldenGate — the GridGain handler, the data source operation handler, and conflict resolution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-lake-accelerator/" %}
[Data Lake Accelerator](data-lake-accelerator/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Load and synchronize data between GridGain 8 and a data lake using Hive, Spark, and Apache Sqoop, and run cross-database queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spark/" %}
[GridGain for Spark](spark/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Share GridGain 8 data with Apache Spark through IgniteContext and IgniteRDD, use GridGain DataFrames, and test with the Spark shell.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="geospatial-sql.md" %}
[Geospatial SQL Capabilities](geospatial-sql.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Query and index geometry data types such as points, lines, and polygons in GridGain 8 using spatial SQL and the GEOMETRY type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ai/" %}
[AI Integration](ai/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain 8 as a vector store and feature store with popular AI and LLM frameworks — LangChain, Langflow, and Feast.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="apache-ignite-extensions.md" %}
[Apache Ignite Extensions](apache-ignite-extensions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Streaming extension modules from the Apache Ignite Extensions project that can be used with GridGain 8.
{% endcolumn %}
{% endcolumns %}

## Apache Ignite Integrations

GridGain is compatible with Apache Ignite integrations. Below is a list of popular integrations you can use in your projects:

- [Spring](https://ignite.apache.org/docs/latest/extensions-and-integrations/spring/spring-boot)
- [Spark](https://ignite.apache.org/docs/latest/extensions-and-integrations/ignite-for-spark/overview)
- [Hibernate L2 Cache](https://ignite.apache.org/docs/latest/extensions-and-integrations/hibernate-l2-cache)
- [MyBatis L2 Cache](https://ignite.apache.org/docs/latest/extensions-and-integrations/mybatis-l2-cache)
- [Cassandra](https://ignite.apache.org/docs/latest/extensions-and-integrations/cassandra/overview)
