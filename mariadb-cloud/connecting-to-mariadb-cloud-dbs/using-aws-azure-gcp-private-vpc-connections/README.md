---
icon: network-wired
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# Using VPC Connections

{% hint style="info" %}
Private VPC connections are secure, private networking mechanisms that enable communication between virtual private clouds (VPCs) or between VPCs and external services without traversing the public internet. These connections are designed to maintain data privacy and security by routing traffic entirely within the cloud provider's private network infrastructure.
{% endhint %}

By default, connections to MariaDB Cloud databases occur with TLS/SSL encryption and can be initiated only from allowlisted IP addresses.

Some customers have regulatory requirements or information security policies that prohibit database connections over the public internet, resulting in a requirement for private connections.

MariaDB Cloud cloud databases can optionally be configured for private connections between your VPC (virtual private clouds) and MariaDB Cloud databases:

* [AWS PrivateLink](setting-up-aws-private-link.md) is supported for MariaDB Cloud databases on AWS
* [Azure PrivateLink](setting-up-azure-private-link.md) is supported for MariaDB Cloud databases on Azure
* [Private Service Connect](setting-up-gcp-private-service-connect.md) is supported for MariaDB Cloud databases on GCP
