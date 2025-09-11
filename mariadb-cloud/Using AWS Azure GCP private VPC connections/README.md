# Using AWS/Azure/GCP private VPC connections

By default, connections to SkySQL cloud databases occur with TLS/SSL encryption and can be initiated only from allowlisted IP addresses.

Some customers have regulatory requirements or information security policies that prohibit database connections over the public internet, and result in a requirement for private connections.

SkySQL cloud databases can optionally be configured for private connections between your VPC (virtual private clouds) and SkySQL cloud databases:

- [AWS PrivateLink](<Setting up AWS Private Link.md>) is supported for SkySQL cloud databases on AWS
- [Azure PrivateLink](<Setting up Azure Private Link.md>) is supported for SkySQL cloud databases on Azure
- [Private Service Connect](<Setting up GCP Private Service Connect.md>) is supported for SkySQL cloud databases on GCP

