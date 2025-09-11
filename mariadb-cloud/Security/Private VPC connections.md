# Private VPC connections

Some customers may have regulatory requirements or information security policies which prohibit the default database connections over the public internet.

SkySQL services can optionally be configured for private connections using cloud provider-specific features - See [Using Private VPC Connections](<../../Using AWS GCP private VPC connections/>) for details on how to set this up. 

By default, client traffic to SkySQL services may transit the public internet and is protected with TLS/SSL and a firewall configured by IP allowlist.