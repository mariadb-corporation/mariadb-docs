---
icon: shield-halved
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

# Security

MariaDB Cloud prioritizes security, offering comprehensive protection at every level. This includes encryption in transit and at rest, encrypted storage, secure compute, and robust authentication and authorization mechanisms. It also adheres to key security standards, such as SOC2, GDPR, and ISO/IEC 27001. For more information, refer to the sections below.

## Managing Portal Users

Manage team access to your MariaDB Cloud services through role-based permissions, user invitations, removals, and modifications within the Portal's User Management console.

{% content-ref url="Managing Portal Users.md" %}
[Managing Portal Users.md](<Managing Portal Users.md>)
{% endcontent-ref %}

## Configuring Firewall

Control network access to your MariaDB Cloud services by configuring IP allowlists that specify which IPv4 addresses or IPv4 netblocks can connect to your service. All other traffic is blocked by default.

{% content-ref url="Configuring Firewall.md" %}
[Configuring Firewall.md](<Configuring Firewall.md>)
{% endcontent-ref %}

## Encryption

Protect your data both in transit using TLS 1.2 and TLS 1.3 (for both client and server connections) and at rest through transparent disk encryption by the underlying cloud providers.

{% content-ref url="Encryption.md" %}
[Encryption.md](Encryption.md)
{% endcontent-ref %}

## Managing API Keys

Generate and manage API keys for secure programmatic access to your MariaDB Cloud services using the Portal's interface or the Swagger-based APIs.

{% content-ref url="Managing API keys.md" %}
[Managing API keys.md](<Managing API keys.md>)
{% endcontent-ref %}

## Private VPC Connections

Use cloud-native solutions like AWS PrivateLink, GCP VPC Peering, or Azure Private Link to configure private network connections to MariaDB Cloud services to comply with regulatory or security requirements.

{% content-ref url="Private VPC connections.md" %}
[Private VPC connections.md](<Private VPC connections.md>)
{% endcontent-ref %}

## Portal Single Sign-On

Use your MariaDB Cloud ID credentials or approved social login options like Google, GitHub, or LinkedIn, or business Google G Suite to log in to the MariaDB Cloud Portal. These alternatives provide convenient Single Sign-On (SSO) without involving additional business configuration.

{% content-ref url="Portal Single Sign-On.md" %}
[Portal Single Sign-On.md](<Portal Single Sign-On.md>)
{% endcontent-ref %}



