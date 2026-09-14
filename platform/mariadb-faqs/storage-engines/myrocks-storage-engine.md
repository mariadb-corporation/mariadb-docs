# MyRocks Storage Engine

* Q: What is the MyRocks storage engine in MariaDB?\
  A: MyRocks is a storage engine available for MariaDB (and also for MySQL). It integrates RocksDB, which is a high-performance, embeddable, persistent key-value store developed by Facebook, based on a log-structured merge-tree (LSM-tree) architecture. MyRocks is specifically designed for high write performance, excellent data compression, and efficient utilization of flash storage (SSDs).
* Q: What are the key benefits and advantages of using the MyRocks storage engine?\
  A: MyRocks generally offers significantly better data compression ratios compared to InnoDB, which can lead to substantial storage cost savings. It also typically exhibits lower write amplification, a critical factor for improving the endurance and lifespan of SSDs, and can provide higher overall throughput for write-intensive workloads.
* Q: When is MyRocks a suitable storage engine choice for MariaDB?\
  A: MyRocks is particularly well-suited for database workloads that are predominantly write-heavy, require high levels of data compression to manage storage footprint, or are running on flash storage where minimizing write amplification and maximizing I/O efficiency are important. Common use cases include social media feeds, Internet of Things (IoT) data ingestion, real-time bidding systems, and extensive logging systems.
* Q: Does the MyRocks storage engine support ACID transactions?\
  A: Yes, the MyRocks storage engine supports ACID transactions, ensuring data integrity for transactional operations. It typically supports common isolation levels such as READ COMMITTED and REPEATABLE READ.
* Q: Is the MyRocks storage engine available in MariaDB Community Server?\
  A: Yes, MyRocks is available as a pluggable storage engine that can be installed and used with MariaDB Community Server, allowing users to leverage its benefits for specific tables or workloads.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
