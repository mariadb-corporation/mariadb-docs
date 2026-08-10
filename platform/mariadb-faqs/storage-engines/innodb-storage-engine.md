# InnoDB Storage Engine

* Q: What is the InnoDB storage engine in MariaDB?\
  A: InnoDB is the default and most widely used general-purpose storage engine in MariaDB. It is a transactional storage engine, meaning it provides full ACID (Atomicity, Consistency, Isolation, Durability) compliance. Key features include row-level locking for high concurrency, support for foreign keys to enforce relational integrity, and robust crash recovery capabilities.
* Q: What are the main benefits and advantages of using the InnoDB storage engine?\
  A: The primary benefits of using InnoDB include ensuring data integrity and consistency through its ACID properties, delivering good performance for applications with concurrent read and write operations (thanks to row-level locking), providing automatic crash recovery to protect data against server failures, and supporting foreign key constraints for maintaining data relationships.
* Q: When is InnoDB the recommended storage engine to use in MariaDB?\
  A: InnoDB is the recommended storage engine for the vast majority of applications, particularly those that require transactions (e.g., financial systems, e-commerce), high levels of concurrency, and strong data integrity guarantees. It is exceptionally well-suited for OLTP (Online Transaction Processing) systems.
* Q: How does the InnoDB storage engine handle crash recovery and ensure data durability?\
  A: InnoDB employs several mechanisms for crash recovery and durability. It uses a transaction log (often called the redo log) to record changes before they are written to the main data files, and a doublewrite buffer to prevent data corruption from partial page writes during crashes. In the event of an unexpected server shutdown or crash, InnoDB can automatically use these logs to recover committed transactions and roll back any uncommitted ones, ensuring the database is restored to a consistent state.
* Q: Is the InnoDB storage engine open source and free to use?\
  A: Yes, InnoDB is an open-source storage engine. It is included as a core and integral part of MariaDB Community Server and is free to use under the terms of its open-source license.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
