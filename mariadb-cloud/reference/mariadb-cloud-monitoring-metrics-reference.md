# MariaDB Cloud Monitoring Metrics Reference

|Panel Name|UI Tab|Scope|Panel Type|Description|
|---|---|---|---|---|
|Connections|status|service|table|This panel shows the number of used and aborted connections for each ES node along with the max_connections value|
|CPU Load|status|service|graph|This panel shows the CPU usage for each ES node during the selected time interval|
|Current SQL Commands|status|service|pie-chart|This panel shows the ratio between the types of SQL statements executed by the service during the selected time interval|
|Disk Size of Data|status|service|table|"This panel shows the amount of storage space used (as the usage percentage| actual size| and total size) by each ES node"|
|QPS|status|service|graph|This panel shows the queries per second (QPS) executed by the ES node during the selected time interval|
|Replicas lags|status|service|table|This panel shows average values for certain replication-related metadata to help determine if the replica ES nodes are currently lagging behind the primary ES node|
|Replicas status|status|service|table|This panel shows summarized values for certain replication-related metadata to help determine if any replica ES nodes encountered replication issues during the selected time interval|
|GTID Replication Position|lags|service|graph|This panel shows the Global Transaction ID (GTID) for each ES node during the selected time interval|
|Seconds Behind Primary|lags|service|graph|This panel shows the lag in seconds behind the primary in terms of the time of the transaction being replicated.|
|Exec Primary Log Position|lags|service|graph|This panel shows the position up to which the primary has processed in the current primary binary log file. |
|Read Primary Log Position|lags|service|graph|This panel shows the position up to which the I/O thread has read in the current primary binary log file.|
|MariaDB Client Thread Activity|queries|service|graph|This panel shows the number of client threads running on all ES nodes during the selected time interval|
|MariaDB QPS|queries|service|graph|This panel shows the number of queries per second (QPS) executed by all ES nodes during the selected time interval|
|MariaDB Slow Queries|queries|service|graph|This panel shows the number of slow queries executed by all ES nodes during the selected time interval|
|MariaDB Slow Queries|queries|service|graph|This panel shows the number of slow queries executed by all ES nodes during the selected time interval|
|Top Command Counters|queries|service|graph|This panel shows the top 30 statement types that were most frequently executed by all ES nodes during the selected time interval|
|Top Command Counters Hourly|queries|service|graph|This panel shows the top 30 statement types that were most frequently executed by all ES nodes in 1 hour intervals over the past 24 hours|
|MariaDB Aborted Connections|database|service|graph|This panel shows the number of connections aborted by the ES node during the selected time interval|
|MariaDB Open Tables|database|service|graph|This panel shows the number of tables opened by the database servers on all ES nodes during the selected time interval|
|MariaDB Service Connections|database|service|graph|This panel shows the number of clients connected to the ES node during the selected time interval|
|MariaDB Table Locks|database|service|graph|This panel shows the number of table locks requested by all ES nodes during the selected time interval|
|MariaDB Table Opened|database|service|graph|This panel shows the number of tables that have been opened by all ES nodes during the selected time interval|
|MaxScale Server Connections|database|service|graph|This panel shows the number of client connections open between the MaxScale node and each ES node during the selected time interval|
|MaxScale Service Connections|database|service|graph|This panel shows the number of clients connected to all MaxScale nodes during the selected time interval|
|CPU Load|system|service|graph|This panel shows the CPU usage for each ES node during the selected time interval|
|Disk Size of Data|system|service|graph|This panel shows the amount of storage space used by all ES nodes during the selected time interval|
|I/OActivity - Page In|system|service|graph|This panel shows the total number of bytes read from the ES node's file system during the selected time interval|
|I/O Activity - Page Out|system|service|graph|This panel shows the total number of bytes written to the ES node's file system during the selected time interval|
|IOPS - Page In|system|service|graph|This panel shows the total number of reads performed from the ES node's file system during the selected time interval|
|IOPS - Page Out|system|service|graph|This panel shows the total number of writes performed from the ES node's file system during the selected time interval|
|MariaDB Network Traffic|system|service|graph|This panel shows the amount of data sent and received over the network by the database servers on all ES nodes during the selected time interval|
|MariaDB Network Usage Hourly|system|service|graph|This panel shows the amount of data sent and received over the network per hour by the database servers on all ES nodes over the past 24 hours|
|Memory Usage|system|service|graph|This panel shows memory usage details for all ES nodes during the selected time interval|
|Network Errors|system|service|graph|This panel shows the number of network errors encountered by all ES nodes during the selected time interval|
|Network Packets Dropped|system|service|graph|This panel shows the number of network packets dropped by all ES nodes during the selected time interval|
|Network Traffic - Inbound|system|service|graph|This panel shows the amount of data received over the network by the operating systems on all ES nodes during the selected time interval|
|Network Traffic - Outbound|system|service|graph|This panel shows the amount of data sent over the network by the operating systems on all ES nodes during the selected time interval|
|Aborted Connections|status|server|singlestat|This panel shows the number of aborted connections for the ES node during the selected time interval|
|Buffer Pool Size of Total RAM|status|server|pie-chart|This panel shows the current size of the InnoDB buffer pool for the ES node in two units: the absolute size and the percentage of the server's usable memory|
|Connections|status|server|stat|This panel shows the number of clients connected to the MaxScale node|
|CPU Load|status|server|gauge|This panel shows the current CPU usage for the ES node|
|CPU Usage / Load|status|server|graph|This panel shows the CPU usage for the ES node during the selected time interval|
|QPS/|status|server|singlestat|This panel shows the number of queries per second (QPS) processed by the ES node during the selected time interval|
|Current SQL Commands|status|server|pie-chart|This panel shows the ratio between the types of SQL statements executed by the ES node during the selected time interval|
|I/O Activity|status|server|graph|This panel shows the total number of bytes written to or read from the ES node's file system during the selected time interval|
|InnoDB Data/sec|status|server|graph|This panel shows the number of bytes per second read and written by InnoDB during the selected time interval|
|Max Connections|status|server|graph|This panel shows the highest number of clients that were concurrently connected to the MaxScale node during the selected time interval|
|Max Connections|status|server|stat|This panel shows the highest number of clients that have ever been concurrently connected to the MaxScale node|
|Max Time in Queue|status|server|graph|This panel shows the longest time the MaxScale node waited for an I/O event during the selected time interval|
|Network Traffic|status|server|graph|This panel shows the amount of data sent and received over the network by the operating system on the ES node during the selected time interval|
|Memory Usage|status|server|gauge|This panel shows the current memory usage details for the ES node|
|Resident (RSS) memory|status|server|gauge|This panel shows the current resident set size (RSS) of the MaxScale process|
|RO Service Connections|status|server|singlestat|This panel shows the number of clients currently connected to the MaxScale node's read-only listener|
|Rows / sec|status|server|graph|This panel shows the total number of rows written and read per second by the ES node during the selected time interval|
|RW Service Connections|status|server|singlestat|This panel shows the number of clients currently connected to the MaxScale node's read-write listener|
|RW / sec|status|server|graph|This panel shows the number of read and write operations per second that were handled by the threads on the MaxScale node during the selected time interval|
|Database Server Connections|status|server|graph|This panel shows the number of client connections open between the MaxScale node and each ES node during the selected time interval|
|MaxScale Connections|status|server|graph|This panel shows the number of clients connected to the MaxScale node's listeners during the selected time interval|
|Stack size|status|server|gauge|This panel shows the current stack size of the MaxScale node|
|Threads|status|server|singlestat|This panel shows the number of threads currently used by the MaxScale node|
|RW/sec|status|server|graph|This panel shows the total number of queries that were actively being executed by the MaxScale node during the selected time interval|
|MaxScale Connections|status|server|graph|This panel shows the total number of connections created by the MaxScale node since the MaxScale node was started|
|Used Connections|status|server|pie-chart|This panel shows the current number of client connections as a percentage of the ES node's max_connections value|
|MariaDB Aborted Connections|database|server|graph|This panel shows the number of connections aborted by the ES node during the selected time interval|
|MariaDB Client Thread Activity|database|server|graph|This panel shows the number of client threads connected and running on the ES node during the selected time interval|
|MariaDB Connections|database|server|graph|This panel shows the number of client connections to the ES node during the selected time interval|
|MariaDB Open Files|database|server|graph|This panel shows the number of files opened by the database server on the ES node during the selected time interval|
|MariaDB Open Tables|database|server|graph|This panel shows the number of tables opened by the database server on the ES node during the selected time interval|
|MariaDB Opened Files / sec|database|server|graph|This panel shows the number of files opened per second by the database server on the ES node during the selected time interval|
|MariaDB Table Locks|database|server|graph|This panel shows the number of table locks requested by the ES node during the selected time interval|
|Temporary Objects Created|database|server|graph|This panel shows the number of temporary tables created by the ES node during the selected time interval|
|MariaDB Table Definition Cache|caches|server|graph|This panel shows how many table definitions were cached by the ES node during the selected time interval|
|MariaDB Table Open Cache Status|caches|server|graph|This panel shows the activity of the table open cache on the ES node during the selected time interval|
|MariaDB Thread Cache|caches|server|graph|This panel shows the number of threads created and cached for re-use on the ES node during the selected time interval|
|MariaDB Handlers / sec|queries|server|graph|This panel shows how many internal query handlers per second have been created by the ES node during the selected time interval|
|MariaDB QPS and Questions|queries|server|graph|This panel shows the number of queries and questions per second executed by the ES node during the selected time interval|
|MariaDB Slow Queries|queries|server|graph|This panel shows the number of slow queries executed by the ES node during the selected time interval|
|MariaDB Sorts|queries|server|graph|This panel shows the number of times the ES node has used certain algorithms to sort data during the selected time interval|
|MariaDB Handlers / sec|queries|server|graph|This panel shows the number of transaction-related handlers created by the ES node during the selected time interval|
|Top Command Counters|queries|server|graph|This panel shows the top 30 statement types that were most frequently executed by the ES node during the selected time interval|
|Top Command Counters Hourly|queries|server|graph|This panel shows the top 30 statement types that were most frequently executed by the ES node in 1 hour intervals over the past 24 hours|
|CPU Usage / Load|system|server|graph|This panel shows the CPU usage for the ES node during the selected time interval|
|Disk Size of Data|system|server|graph|This panel shows the amount of storage space used by the ES node during the selected time interval|
|Disk Size of Logs|system|server|graph|This panel shows the amount of storage space used by the server error logs during the selected time interval|
|I/O Activity|system|server|graph|This panel shows the total number of bytes written to or read from the ES node's file system during the selected time interval|
|InnoDB Data / sec|system|server|graph|This panel shows the number of bytes per second read and written by InnoDB during the selected time interval|
|IOPS|system|server|graph|This panel shows the number of input/output operations per second performed by the ES node during the selected time interval|
|MariaDB Memory Overview|system|server|graph|"This panel shows how much memory the ES node used for the InnoDB buffer pool| InnoDB log buffer| MyISAM key buffer| and query cache during the selected time interval"|
|MariaDB Network Traffic|system|server|graph|This panel shows the amount of data sent and received over the network by the database server on the ES node during the selected time interval|
|MariaDB Network Usage Hourly|system|server|graph|This panel shows the amount of data sent and received over the network per hour by the database server on the ES node over the past 24 hours|
|Memory Distribution|system|server|graph|This panel shows memory usage details for the ES node during the selected time interval|
|Network Errors|system|server|graph|This panel shows the number of network errors encountered by the ES node during the selected time interval|
|Network Packets Dropped|system|server|graph|This panel shows the number of network packets dropped by the ES node during the selected time interval|
|Network Traffic|system|server|graph|This panel shows the amount of data sent and received over the network by the operating system on the ES node during the selected time interval|
|Errors|performance|server|graph|This panel shows the number of errors encountered by threads on the MaxScale node during the selected time interval|
|MaxScale Descriptors|performance|server|graph|This panel shows the number of descriptors used by the MaxScale node during the selected time interval|
|MaxScale Hangups|performance|server|graph|This panel shows the number of client connections closed by the MaxScale node during the selected time interval|
|Memory Usage|performance|server|graph|This panel shows memory usage details for the MaxScale node during the selected time interval|
|MaxScale Modules|modules|server|table|This panel lists the modules installed on the MaxScale node|
