---
description: >-
  The mutex_instances table lists all active mutexes (mutual exclusions)
  instrumented by the Performance Schema, showing their locked state.
---

# Performance Schema mutex\_instances Table

## Description

The `mutex_instances` table lists all mutexes that the Performance Schema seeing while the server is executing.

A mutex is a code mechanism for ensuring that threads can only access resources one at a time. A second thread attempting to access a resource will find it protected by a mutex, and will wait for it to be unlocked.

The [performance\_schema\_max\_mutex\_instances](../performance-schema-system-variables.md#performance_schema_max_mutex_instances) system variable specifies the maximum number of instrumented mutex instances.

| Column                  | Description                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------ |
| NAME                    | Instrument name associated with the mutex.                                           |
| OBJECT\_INSTANCE\_BEGIN | Memory address of the instrumented mutex.                                            |
| LOCKED\_BY\_THREAD\_ID  | The THREAD\_ID of the locking thread if a thread has a mutex locked, otherwise NULL. |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
