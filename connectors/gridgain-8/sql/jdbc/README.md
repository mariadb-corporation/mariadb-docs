---
hidden: true
description: >-
  Overview of the GridGain JDBC drivers for processing distributed data with
  standard SQL, covering the JDBC Thin Driver and the JDBC Client Driver.
---

# JDBC Driver

GridGain is shipped with JDBC drivers that allow processing of distributed data using standard SQL statements like `SELECT`, `INSERT`, `UPDATE`, or `DELETE` directly from the JDBC side.

Two drivers are supported:

- [JDBC Thin Driver](jdbc-driver.md) — the default, lightweight driver. It connects to one of the cluster nodes and forwards all queries to it for execution.
- [JDBC Client Driver](jdbc-client-driver.md) — interacts with the cluster by means of a client node.
