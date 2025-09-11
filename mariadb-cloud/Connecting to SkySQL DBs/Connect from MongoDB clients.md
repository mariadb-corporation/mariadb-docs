# Connect from MongoDB clients

The NoSQL protocol module allows a MariaDB server or cluster to execute transactions for applications using MongoDB client libraries, transparently converting MongoDB API calls into the equivalent SQL. The MariaDB responses are then converted into the format expected by the MongoDB® client library and application.

For detailed information on supported commands, see "[NoSQL Protocol Module](https://mariadb.com/kb/en/mariadb-maxscale-2208-nosql-protocol-module/)" in MariaDB MaxScale documentation.

💡 IMPORTANT - this feature is supported by the MariaDB advanced proxy - Maxscale. And, maxscale is only started when using the SkySQL Replicated topology. i.e. will not work when using a Standalone MariaDB server.

## Enable Support for NoSQL

1. When [launching](<../Portal features/Launch page.md>) Mariadb Server With Replica(s), after defining the service name, expand the "Additional options" section.
2. Check the "Enable support for NoSQL" checkbox.

## Available Clients

Connect to the NoSQL interface using a MongoDB client library or compatible application. [Documentation on official MongoDB libraries](https://www.mongodb.com/docs/drivers/) is available from MongoDB.

[Documentation on installing `mongosh` (the MongoDB Shell)](https://www.mongodb.com/docs/mongodb-shell/install/) is available from MongoDB.

## Connection Parameters

From the Dashboard, the details needed to connect to your SkySQL service can be seen by clicking on the "CONNECT" button for the desired service.

The "NoSQL port" is the TCP port used to connect to the NoSQL interface.

The [firewall](<../Security/Configuring Firewall.md>) must be configured to allowlist the client's IP address or netblock before connections can occur.

See the "Connecting using Mongosh" section of the Connect page for an example `mongosh` command-line, authentication instructions, and instructions to change the default password.
