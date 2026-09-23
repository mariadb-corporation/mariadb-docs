---
description: >-
  GridGain 9 uses Apache Calcite as its SQL engine, providing distributed,
  transactional, standard-adherent SQL with advanced query optimization.
---

# Introduction

GridGain 9 uses Apache Calcite as an SQL engine of choice. Apache Calcite is a dynamic data management framework, which mainly serves for mediating between applications and one or more data storage locations and data processing engines. For more information on Apache Calcite, see the [Calcite documentation](https://calcite.apache.org/docs/).

GridGain 9 SQL engine has the following advantages:

- **SQL Optimized for Distributed Environments**: GridGain 9 distributed queries are not limited to a single map-reduce phase, allowing more complex data gathering;
- **Transactional SQL**: All tables in GridGain 9 support SQL transactions with transactional guarantees;
- **Cluster-wide System Views**: [System views](../../reference/monitoring/system-views.md) in GridGain 9 provide cluster-wide information, dynamically updated;
- **Multi-Index Queries**: With GridGain 9, you can perform queries that use multiple indexes at the same time to speed up queries;
- **Standard-Adherent SQL**: GridGain 9 SQL closely adheres to modern SQL standard;
- **Improved optimization algorithms**: SQL in GridGain 9 optimizes queries by repeatedly applying planner rules to a relational expression;
- **High overall performance**: GridGain 9 offers high levels of execution flexibility, as well as high efficiency in terms of both memory and CPU consumption.
