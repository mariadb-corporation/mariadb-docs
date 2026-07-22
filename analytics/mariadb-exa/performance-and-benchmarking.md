---
description: >-
  Performance tuning and benchmarking for MariaDB Exa: the MaxScale CDC
  (binlogrouter) odbc_perf_* bulk-load parameters, plus CDC throughput up to
  600 TPS and TPC-H benchmark results.
icon: bolt-lightning
---

# Performance & Benchmarking

## Performance Considerations

MariaDB Exa keeps Exasol in sync through MaxScale CDC, which reads the MariaDB binary log with the `binlogrouter` module and bulk-loads batches into Exasol over the Exasol ODBC driver. The bulk-load pipeline's throughput is controlled by the `odbc_perf_*` parameters on the binlogrouter CDC service. The defaults suit most workloads; raise the batch size for more throughput, or lower `odbc_perf_ncycles` if memory use is high.

| Component | Key parameter | Default | Description & tuning tips |
| --------- | ------------- | ------- | ------------------------- |
| MaxScale CDC | `odbc_perf_batch_size` | 200 MB | Size in bytes of one ODBC batch over the wire. Raise for more throughput. |
| MaxScale CDC | `odbc_perf_max_buffered_rows` | 750,000 | Ceiling of buffered rows before a batch is sent. |
| MaxScale CDC | `odbc_perf_max_idle_rows` | 400,000 | Rows buffered before sending when the pipeline is otherwise idle. |
| MaxScale CDC | `odbc_perf_ncycles` | 4 | Maximum parallel ODBC cycles (also the maximum value). Lower it if memory use is high. |
| MaxScale CDC | `odbc_perf_nthreads` | 0 (unlimited) | Maximum threads used in ODBC processing. |
| Exasol | `NUM_NODES`, `DB_RAM_SIZE` | — | Scale based on dataset size and concurrency. |
| Network | 10 Gbps+ recommended | — | Ensures low-latency data transfer between MaxScale and Exasol. |

{% hint style="info" %}
These parameters are set on the `binlogrouter` CDC service. For the full CDC setup, see the [MariaDB MaxScale Exasolrouter Tutorial](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-tutorials/mariadb-maxscale-exasolrouter).
{% endhint %}

## Benchmarking

MariaDB Exa CDC has been tested and is expected to work in near real-time up to 600 TPS[^1] from the source MariaDB server side. MariaDB Exa has leading benchmark results for TPC-H[^2].

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: Transactions Per Second

[^2]: Transaction Processing Performance Council - Benchmark H. It is a decision support benchmark that consists of business-oriented ad-hoc queries and concurrent data modifications. This benchmark is used to illustrate decision support systems that examine large volumes of data, execute complex queries, and provide answers to critical business questions. The performance metric reported by TPC-H is called the TPC-H Composite Query-per-Hour Performance Metric, which reflects various aspects of a system's ability to process queries, including database size, single-stream query processing, and query throughput with multiple concurrent users.
