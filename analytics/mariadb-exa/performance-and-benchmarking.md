---
description: >-
  Performance tuning and benchmarking for MariaDB Exa: Debezium, Kafka
  Connect, and Exasol JDBC Sink parameters, plus CDC throughput up to 600 TPS
  and TPC-H benchmark results.
icon: bolt-lightning
---

# Performance & Benchmarking

## Performance Considerations

| Component        | Key Parameter                    | Description & Tuning Tips                                   |
| ---------------- | -------------------------------- | ----------------------------------------------------------- |
| Debezium         | max.batch.size, max.queue.size   | Increase to handle high write rates from MariaDB.           |
| Kafka Connect    | tasks.max, batch.size, linger.ms | Controls parallelism and batch commit latency.              |
| Exasol JDBC Sink | insert.mode=upsert or insert     | Choose depending on CDC requirements.                       |
| Exasol           | NUM\_NODES, DB\_RAM\_SIZE        | Scale based on dataset size and concurrency.                |
| Network          | 10 Gbps+ recommended             | Ensures low-latency data transfer between Kafka and Exasol. |

## Benchmarking

MariaDB Exa CDC has been tested and is expected to work in near real-time up to 600 TPS[^1] from the source MariaDB server side. MariaDB Exa has leading benchmark results for TPC-H[^2].

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: Transactions Per Second

[^2]: Transaction Processing Performance Council - Benchmark H. It is a decision support benchmark that consists of business-oriented ad-hoc queries and concurrent data modifications. This benchmark is used to illustrate decision support systems that examine large volumes of data, execute complex queries, and provide answers to critical business questions. The performance metric reported by TPC-H is called the TPC-H Composite Query-per-Hour Performance Metric, which reflects various aspects of a system's ability to process queries, including database size, single-stream query processing, and query throughput with multiple concurrent users.
