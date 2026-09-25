GridGain clients come in several different flavors, each with various capabilities. [JDBC]({connectors}/sql/jdbc/jdbc-driver) and [ODBC]({connectors}/sql/odbc/odbc-driver) drivers are useful for SQL-only applications and SQL-based tools. [HTTP REST client](../../reference/rest-api/README.md) is useful to communicate with cluster over HTTP and HTTPS. Thick and thin clients go beyond SQL capabilities and support many more APIs. Finally, ORM frameworks like [Spring](https://ignite.apache.org/docs/latest/extensions-and-integrations/spring/spring-boot) Data or [Hibernate](https://ignite.apache.org/docs/latest/extensions-and-integrations/hibernate-l2-cache) are also integrated with GridGain and can be used as an access point to your cluster.

Let's review the difference between thick and thin clients by comparing their capabilities.

**Thick** clients (client nodes) join the cluster via an internal protocol, receive all of the cluster-wide updates such as topology changes, are aware of data distribution, and can direct a query/operation to a server node that owns a required data set. Plus, thick clients support all of the GridGain APIs.

[**Thin** clients]({connectors}/thin-clients/getting-started-with-thin-clients) (lightweight clients) connect to the cluster via binary protocol with a well-defined message format. This type of client supports a more limited set of APIs but in return:

- Makes it easy to enable programming language support for GridGain and Ignite. Java, .NET, C++, Python, Node.JS, and PHP are supported out of the box.
- Doesn't have any dependencies on JVM. For instance, .NET and C++ _thick_ clients have a richer feature set but start and use JVM internally.
- Requires at least one port opened on the cluster end. Note that more ports need to be opened if partition-awareness is used for a thin client.

{% hint style="info" %}
The ODBC driver uses a protocol similar to the thin client's. As for the JDBC driver, it comes in two flavors - a thick version of the driver that utilizes a Java thick client internally and a thin counterpart, based on the thin client's protocol.
{% endhint %}
