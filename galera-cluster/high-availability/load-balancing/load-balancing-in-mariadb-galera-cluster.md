# Load Balancing in MariaDB Galera Cluster

While a client application can connect directly to any node in a MariaDB Galera Cluster, this is not a practical approach for a production environment. A direct connection creates a single point of failure and does not allow the application to take advantage of the cluster's high availability and read-scaling capabilities.

A load balancer or database proxy is an essential component that sits between your application and the cluster. Its primary responsibilities are:

* Provide a Single Endpoint: Your application connects to the load balancer's virtual IP address, not to the individual database nodes.
* Health Checks: The load balancer constantly monitors the health of each cluster node (e.g., is it `Synced`? is it up or down?).
* Traffic Routing: It intelligently distributes incoming client connections and queries among the healthy nodes in the cluster.
* Automatic Failover: If a node fails, the load balancer automatically stops sending traffic to it, providing seamless failover for your application.

### 2. Recommended Load Balancer: MariaDB MaxScale

For MariaDB Galera Cluster, the recommended load balancer is MariaDB MaxScale. Unlike a generic TCP proxy, MaxScale is a database-aware proxy that understands the Galera Cluster protocol. This allows it to make intelligent routing decisions based on the real-time state of the cluster nodes.

### 3. Common Routing Strategies

A database-aware proxy like MaxScale can be configured to use several different routing strategies.

#### Read-Write Splitting (Recommended)

This is the most common and highly recommended strategy for general-purpose workloads.

* How it Works: The load balancer is configured to send all write operations (`INSERT`, `UPDATE`, `DELETE`) to a single, designated primary node. All read operations (`SELECT`) are then distributed across the remaining available nodes.
* Advantages:
  * Minimizes Transaction Conflicts: By directing all writes to one node, you significantly reduce the chance of two nodes trying to modify the same row at the same time, which would lead to deadlocks and transaction rollbacks.
  * Maximizes Read Scalability: It fully utilizes the other nodes in the cluster for scaling out read-intensive workloads.

#### Read Connection Load Balancing

In this simpler strategy, the load balancer distributes all connections evenly across all available nodes.

* How it Works: Each new connection is sent to the next available node in a round-robin fashion.
* Disadvantages: This approach can easily lead to transaction conflicts if your application sends writes to multiple nodes simultaneously. It is generally only suitable for applications that are almost exclusively read-only.

### 4. Other Load Balancing Solutions

While MariaDB MaxScale is the recommended solution, other proxies and load balancers can also be used with Galera Cluster, including:

* ProxySQL: Another popular open-source, database-aware proxy.
* HAProxy: A very common and reliable TCP load balancer. When used with Galera, HAProxy is typically configured with a simple TCP health check or a custom script to determine node availability.
* Cloud Load Balancers: Cloud providers like AWS (ELB/NLB), Google Cloud, and Azure offer native load balancing services that can be used to distribute traffic across a Galera Cluster.
