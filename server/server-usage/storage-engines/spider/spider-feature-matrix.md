# Spider Feature Matrix

Not complete yet - still being updated

F(_) Federation only , P(_)partioning only .\
Spider column is for SpiderForMySQL found on the Spider web sIte.

| Feature                                                                                              | Spider | 10.0  |
| ---------------------------------------------------------------------------------------------------- | ------ | ----- |
| Clustering and High Availability                                                                     |        |       |
| Commit, Rollback transactions on multiple backend                                                    | Yes    | Yes   |
| Multiplexing to a number of replicas using xa protocol 2PC                                           | Yes    | Yes   |
| Split brain resolution based on a majority decision, failed node is remove from the list of replicas | Yes    | Yes   |
| Enable a failed backend to re enter the cluster transparently                                        | No     | No    |
| Synchronize DDL to backend, table modification, schema changes                                       | No     | No    |
| Synchronize DDL to other Spider                                                                      | No     | No    |
| GTID tracking per table on XA error                                                                  | No     | Yes   |
| Transparent partitioning                                                                             | No     | No    |
| Covered by generic SQL test case                                                                     | Yes    | Yes   |
| Heterogenous Backends                                                                                |        |       |
| MariaDB and MySQL database backend                                                                   | Yes    | Yes   |
| Oracle database backend, if build from source against the client library 'ORACLE\_HOME'              | Yes    | Yes   |
| Local table attachment                                                                               | Yes    | Yes   |
| Performance                                                                                          |        |       |
| Index Condition Pushdown                                                                             | No     | No    |
| Engine Condition Pushdown                                                                            | Yes    | Yes   |
| Concurrent backend scan                                                                              | Yes    | No    |
| Concurrent partition scan                                                                            | Yes    | No    |
| Batched key access                                                                                   | Yes    | Yes   |
| Block hash join                                                                                      | No     | Yes   |
| HANDLER backend propagation                                                                          | Yes    | Yes   |
| HANDLER backend translation from SQL                                                                 | Yes    | Yes   |
| HANDLER OPEN cache per connection                                                                    | No     | Yes   |
| HANDLER use prepared statement                                                                       | No     | Yes   |
| HANDLER\_SOCKET protocol backend propagation                                                         | Yes    | Yes   |
| HANDLER\_SOCKET backend translation from SQL                                                         | No     | No    |
| Map reduce for ORDER BY ... LIMIT                                                                    | Yes    | Yes   |
| Map reduce for MAX & MIN & SUM                                                                       | Yes    | Yes   |
| Map reduce for some GROUP BY                                                                         | Yes    | Yes   |
| Batch multiple WRITES in auto commit to reduce network round trip                                    | Yes    | Yes   |
| Relaxing backend consistency                                                                         | Yes    | Yes   |
| Execution Control                                                                                    |        |       |
| Configuration at table and partition level, settings can change per data collection                  | Yes    | Yes   |
| Configurable empty result set on errors. For API that does not have transactions replay              | Yes    | Yes   |
| Query Cache tuning per table of the on remote backend                                                | Yes    | Yes   |
| Index Hint per table imposed on remote backend                                                       | Yes    | Yes   |
| SSL connections to remote backend connections                                                        | Yes    | Yes   |
| Table definition discovery from remote backend                                                       | Yes    | F(\*) |
| Direct SQL execution to backend via UDF                                                              | Yes    | Yes   |
| Table re synchronization between backends via UDF                                                    | Yes    | Yes   |
| Maintain Index and Table Statistics of remote backends                                               | Yes    | Yes   |
| Can use Independent Index and Table Statistics                                                       | No     | Yes   |
| Maintain local or remote table increments                                                            | Yes    | Yes   |
| LOAD DATA INFILE translate to bulk inserting                                                         | Yes    | Yes   |
| Performance Schema Probes                                                                            | Yes    | Yes   |
| Load Balance Reads to replicate weight control                                                       | Yes    | Yes   |
| Fine tuning tcp timeout, connections retry                                                           | Yes    | Yes   |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
