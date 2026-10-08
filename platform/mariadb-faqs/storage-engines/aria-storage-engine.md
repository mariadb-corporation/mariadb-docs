# Aria Storage Engine

* Q: What is the Aria storage engine in MariaDB?\
  A: Aria is a storage engine developed by the MariaDB team. It was originally conceived as a more modern, crash-safe (though not fully transactional by default) alternative and successor to the older MyISAM storage engine. MariaDB uses Aria for some of its internal system tables, and it is also available for use with user-created tables.
* Q: What are the main features and characteristics of the Aria storage engine?\
  A: Aria offers significantly better crash recovery capabilities compared to MyISAM. It supports multiple page sizes for data storage, various row formats to optimize for different data types, and can be faster than InnoDB for certain types of read-heavy queries and full table scans. Aria also provides transactional capabilities if explicitly enabled at table creation using the TRANSACTIONAL=1 option.
* Q: When might one choose to use the Aria storage engine over InnoDB for user tables?\
  A: While InnoDB is generally the preferred choice for tables requiring full transactional support and data integrity, Aria might be considered for specific scenarios. These include read-heavy workloads where full ACID guarantees are not strictly necessary, internal application tables, or situations where features like page checksums are desired without the full overhead of InnoDB's transactional mechanisms (unless TRANSACTIONAL=1 is explicitly set). MariaDB itself leverages Aria for handling complex queries that require on-disk internal temporary tables, which can improve performance for such specific operations.
* Q: Is the Aria storage engine fully ACID compliant by default?\
  A: By default, the Aria storage engine is designed primarily for crash safety rather than full ACID compliance in the same way as InnoDB. However, Aria tables can be made transactional by creating them with the TRANSACTIONAL=1 table option. This makes them more ACID-compliant, but with different performance characteristics and operational considerations compared to InnoDB tables.
* Q: Where is the Aria storage engine used by default within MariaDB Server?\
  A: MariaDB Server utilizes the Aria storage engine for its on-disk internal temporary tables. These temporary tables are often created when processing complex queries (e.g., those involving GROUP BY, ORDER BY, or UNION operations on large datasets). Using Aria for this purpose can offer performance benefits for such operations compared to using MyISAM (which was the default for this in older MySQL versions).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
