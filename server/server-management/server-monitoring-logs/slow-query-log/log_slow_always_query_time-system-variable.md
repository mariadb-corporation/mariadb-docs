---
description: >-
  Documentation for the `log_slow_always_query_time` variable, which forces
  queries executed by a specific function or user to be logged regardless of
  their execution time.
---

# log\_slow\_always\_query\_time System Variable

* Description: Queries slower than log\_slow\_always\_query\_time are not affected by [log\_slow\_rate\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_rate_limit) or [log\_slow\_min\_examined\_row\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_min_examined_row_limit). Query will be logged to the [slow query log](./) if the execution time of the query is longer than [log\_slow\_query\_time](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time) and log\_slow\_always\_query\_time. The argument will be treated as a decimal value with microsecond precision.
* Command line: `--log-slow-always-query-time=num`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric (double)`
* Default Value: `31536000.000000`
* Range: `0` to `31536000`
* Introduced: [MariaDB 11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
