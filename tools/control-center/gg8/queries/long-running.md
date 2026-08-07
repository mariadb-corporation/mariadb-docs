---
description: >-
  Using Control Center to localize and debug long-running SQL queries on
  GridGain 8 clusters.
---

# Debugging Running SQL Queries with Control Center

One of the issues you can encounter when running GridGain is a long query execution. You can see this from logs, but Control Center provides extra tools to help you localize the issue.

{% embed url="https://www.youtube.com/watch?v=t9K5Of8u8Vg" %}

When debugging the issue, navigate to the **Queries** tab and its **Running queries** screen. Here you can stop the long running queries to restore cluster functionality. This will not last, as the same issue is likely to happen again, but will allow your service to continue working while you look for a solution.

After that you can switch to the **Query Statistics** screen. Here you can see which queries execute consistently slow. Click **Explain** to dive deeper into query execution process.

In distributed systems, queries are executed in 2 phases:

- **Map** - invoked on each node to process data locally;
- **Reduce** - invoked on the query coordinator node and aggregate data from other nodes.

For example, one of possible reasons is that SQL uses `scan` instead of `index`. In this case, you can create a secondary index and speed up query execution dramatically.
