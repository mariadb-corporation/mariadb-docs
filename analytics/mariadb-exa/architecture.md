---
description: >-
  MariaDB Exa architecture: a multi-stage pipeline streaming changes from
  MariaDB Enterprise Server through Debezium and Kafka into Exasol for near
  real-time analytics on operational data.
icon: house-blank
---

# Architecture

## Overview

A typical integration stack looks like this:

1. MariaDB Server generates binary log events.
2. Debezium captures row changes into Kafka topics.
3. Kafka Connect JDBC Sink writes the data into Exasol using its JDBC driver.
4. Exasol runs ad-hoc or scheduled analytic queries on the data.

## Data Flow

The integration between MariaDB Enterprise Server, MaxScale, and MariaDB Exa enables near real-time analytics on operational data. The architecture can be viewed as a multi-stage data pipeline:

{% stepper %}
{% step %}
**Source (Operational Layer)**

MariaDB Enterprise Server handles transactional workloads (OLTP). Changes are continuously recorded in the binary log (binlog).
{% endstep %}

{% step %}
**Change Capture (Integration Layer)**

[Debezium](https://debezium.io/) monitors the MariaDB binary logs and streams change events (inserts, updates, deletes) into Apache Kafka topics. Each table is represented as a topic (for instance, `dbserver1.tpcc.customer`).
{% endstep %}

{% step %}
**Data Delivery (Sink Layer)**

Kafka Connect’s JDBC Sink Connector consumes these topics and writes data into MariaDB Exa via the Exasol JDBC driver. This process supports batching and compaction depending on connector configuration.
{% endstep %}

{% step %}
**Analytics (Consumption Layer)**

Analysts or BI[^1] tools (like Tableau, Power BI, or Looker) connect to Exasol using standard JDBC/ODBC interfaces to perform high-speed, ad-hoc analytics, aggregations, and joins over the continuously updated dataset.
{% endstep %}
{% endstepper %}

## MaxScale Integration

When using MariaDB MaxScale, the architecture can include:

* **Load Balancing / Query Routing:** MaxScale can manage read/write separation, and route analytics queries directly to MariaDB Exa in hybrid configurations.
* **Security & Auditing:** MaxScale handles SSL termination, connection pooling, and authentication, reducing load on backend servers.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: Business Intelligence
