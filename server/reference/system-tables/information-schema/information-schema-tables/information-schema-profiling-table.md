---
description: >-
  The Information Schema PROFILING table provides statement resource usage
  details, such as CPU time and block operations, when profiling is enabled.
---

# Information Schema PROFILING Table

The [Information Schema](../) `PROFILING` table contains information about statement resource usage. Profiling information is only recorded if the [profiling](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#profiling) session variable is set to `1`.

It contains the following columns:

| Column Name          | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| QUERY\_ID            | Query\_ID.                                                                  |
| SEQ                  | Sequence number showing the display order for rows with the same QUERY\_ID. |
| STATE                | Profiling state.                                                            |
| DURATION             | Time in seconds that the statement has been in the current state.           |
| CPU\_USER            | User CPU usage in seconds.                                                  |
| CPU\_SYSTEM          | System CPU usage in seconds.                                                |
| CONTEXT\_VOLUNTARY   | Number of voluntary context switches.                                       |
| CONTEXT\_INVOLUNTARY | Number of involuntary context switches.                                     |
| BLOCK\_OPS\_IN       | Number of block input operations.                                           |
| BLOCK\_OPS\_OUT      | Number of block output operations.                                          |
| MESSAGES\_SENT       | Number of communications sent.                                              |
| MESSAGES\_RECEIVED   | Number of communications received.                                          |
| PAGE\_FAULTS\_MAJOR  | Number of major page faults.                                                |
| PAGE\_FAULTS\_MINOR  | Number of minor page faults.                                                |
| SWAPS                | Number of swaps.                                                            |
| SOURCE\_FUNCTION     | Function in the source code executed by the profiled state.                 |
| SOURCE\_FILE         | File in the source code executed by the profiled state.                     |
| SOURCE\_LINE         | Line in the source code executed by the profiled state.                     |

It contains similar information to the [SHOW PROFILE](../../../sql-statements/administrative-sql-statements/show/show-profile.md) and [SHOW PROFILES](../../../sql-statements/administrative-sql-statements/show/show-profiles.md) statements.

Profiling is enabled per session. When a session ends, its profiling information is lost.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
