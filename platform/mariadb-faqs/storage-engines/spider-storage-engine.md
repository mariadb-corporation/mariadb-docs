# Spider Storage Engine

* Q: What is the Spider storage engine in MariaDB?\
  A: Spider is a specialized storage engine available for MariaDB that enables data sharding, also known as horizontal partitioning. It allows a single MariaDB instance (acting as the "Spider node" or proxy) to present data that is physically distributed across multiple backend MariaDB servers as if it were stored in a single, unified table on the Spider node.
* Q: How does the Spider storage engine work to achieve data sharding?\
  A: The Spider node contains special "Spider tables" whose definitions include information about how the data is partitioned (e.g., by range, list, or hash) and which remote backend MariaDB servers hold each specific partition or shard of the data. When a query is executed against a Spider table, the Spider engine determines which backend servers need to be accessed to satisfy the query, forwards the appropriate parts of the query to those remote servers, and then aggregates the results before returning them to the client.
* Q: What are the main use cases and benefits of using the Spider storage engine?\
  A: The Spider storage engine is primarily used for scaling out very large databases that have exceeded the capacity or performance limits of a single database server. It allows for the distribution of both data storage and query load across multiple backend servers, which is beneficial for applications requiring massive horizontal scalability for both storage capacity and query performance. It can also improve query performance by parallelizing operations across shards.
* Q: Does the Spider storage engine support transactions across distributed shards?\
  A: Yes, the Spider storage engine has support for XA (eXtended Architecture) transactions. This enables it to manage and coordinate distributed transactions across multiple backend MariaDB servers, which is crucial for maintaining data consistency in sharded database environments.
* Q: Is the Spider storage engine available in MariaDB Community Server?\
  A: Yes, the Spider storage engine is available as a pluggable engine within MariaDB Community Server, allowing users to implement database sharding solutions.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
