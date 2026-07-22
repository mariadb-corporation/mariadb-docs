---
description: >-
  Monitoring MariaDB Exa: the MaxScale log and maxctrl, the Exasol GUI,
  EXA_STATISTICS and EXA_ALL_SESSIONS tables, and Grafana/Prometheus
  integration for cross-stack metrics.
icon: telescope
---

# Monitoring and Observability

Explore essential tools and techniques for monitoring and optimizing data systems and workflows:

* **MaxScale CDC log:** Watch the MaxScale log (`/var/log/maxscale/maxscale.log`) with info logging enabled for the binlogrouter CDC service to track batch application and replication lag. The CDC service persists its GTID position, so it resumes from where it stopped after a restart.
* **`maxctrl`:** Inspect service and listener state, and enable debug/info logging (`maxctrl alter maxscale log_info true`) to see SmartRouter routing decisions and CDC progress.
* **Exasol GUI:** Monitor cluster health, node status, and I/O throughput.
* **SQL Auditing:** Use Exasol system tables (EXA\_STATISTICS, EXA\_ALL\_SESSIONS) for query profiling.
* **Grafana / Prometheus Integration:** Collect metrics across MaxScale, MariaDB, and Exasol.
* **MariaDB Enterprise Manager:** Review operational statistics and metrics covering all MariaDB products except MariaDB Exa.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
