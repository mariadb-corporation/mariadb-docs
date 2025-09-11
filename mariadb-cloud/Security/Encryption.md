# Encryption

## **Data-in-Transit Encryption**
SkySQL features data-in-transit encryption by default.

### Client-to-Server
By default, SkySQL services feature data-in-transit encryption for client connections:
-TLS 1.2 and TLS 1.3 are supported. SSL/TLS certificates and encryption settings are not customer-configurable.

For information on how to connect with TLS, see ["Connect and Query"](<../../Connecting to Sky DBs/>).

The "Disable SSL/TLS" option may be appropriate for some customers when also using AWS PrivateLink or GCP VPC Peering.

### Server-to-Server
SkySQL services perform server-to-server communication between MariaDB MaxScale, MariaDB Server, and SkySQL infrastructure.

By default, these server-to-server communications are protected with data-in-transit encryption:

For SkySQL Services on AWS, see "[Encryption in transit(AWS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit)". SkySQL uses configurations which feature automatic in-transit encryption.

For SkySQL Services on GCP, see "[Encryption in transit (GCP)](https://cloud.google.com/docs/security/encryption-in-transit#encryption_in_transit_by_default)". SkySQL uses encryption by default.

For SkySQL Services on Azure, see "[Encryption in transit (Azure)](https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-overview#encryption-of-data-in-transit)". SkySQL uses encryption by default.

## **Data-at-Rest Encryption**
SkySQL features transparent data-at-rest encryption.

SkySQL Services on AWS use [Amazon EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html).

SkySQL Services on GCP benefits from [encryption by default](https://cloud.google.com/security/encryption-at-rest/default-encryption).

SkySQL Services on Azure use [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview).

