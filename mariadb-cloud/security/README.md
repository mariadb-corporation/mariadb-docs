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

{% content-ref url="managing-portal-users.md" %}
[managing-portal-users.md](managing-portal-users.md)
{% endcontent-ref %}

## Configuring Firewall

Control network access to your MariaDB Cloud services by configuring IP allowlists that specify which IPv4 addresses or IPv4 netblocks can connect to your service. All other traffic is blocked by default.

{% content-ref url="configuring-firewall.md" %}
[configuring-firewall.md](configuring-firewall.md)
{% endcontent-ref %}

## Encryption

Protect your data both in transit using TLS 1.2 and TLS 1.3 (for both client and server connections) and at rest through transparent disk encryption by the underlying cloud providers.

{% content-ref url="encryption.md" %}
[encryption.md](encryption.md)
{% endcontent-ref %}

## Managing API Keys

Generate and manage API keys for secure programmatic access to your MariaDB Cloud services using the Portal's interface or the Swagger-based APIs.

{% content-ref url="managing-api-keys.md" %}
[managing-api-keys.md](managing-api-keys.md)
{% endcontent-ref %}

## Private VPC Connections

Use cloud-native solutions like AWS PrivateLink, GCP VPC Peering, or Azure Private Link to configure private network connections to MariaDB Cloud services to comply with regulatory or security requirements.

{% content-ref url="private-vpc-connections.md" %}
[private-vpc-connections.md](private-vpc-connections.md)
{% endcontent-ref %}

## Portal Single Sign-On

Use your MariaDB Cloud ID credentials or approved social login options like Google, GitHub, or LinkedIn, or business Google G Suite to log in to the MariaDB Cloud Portal. These alternatives provide convenient Single Sign-On (SSO) without involving additional business configuration.

{% content-ref url="portal-single-sign-on.md" %}
[portal-single-sign-on.md](portal-single-sign-on.md)
{% endcontent-ref %}



