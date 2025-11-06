# Private VPC Connections

Some customers may have regulatory requirements or information security policies that prohibit the default database connections over the public internet.

MariaDB Cloud services can optionally be configured for private connections using cloud provider-specific features - See [Using Private VPC Connections](<Private VPC connections.md>) for details on how to set this up.

By default, client traffic to MariaDB Cloud services may transit the public internet and is protected with TLS/SSL and a firewall configured by IP allowlist.
