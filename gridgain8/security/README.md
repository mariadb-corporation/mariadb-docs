---
description: >-
  Overview of GridGain security features, including encrypted communications,
  authentication, authorization, and auditing.
icon: shield-halved
---

# Security and Auditing

GridGain's security features allow you to perform security activities, such as encrypting communications, configuring authentication and authorization methods, and performing audits. For example, you can secure the communications between cluster nodes by using SSL/TLS encryption.
What is more, GridGain provides a convenient and flexible way for managing user roles and permissions. For example, Control Center allows to share its features between team members using the [Teams]({tools}/control-center/profile/teams) functionality.

{% hint style="info" %}
Some of the security features explained in this topic are the features of the GridGain Enterprise and Ultimate editions.
{% endhint %}

The GridGain security functionality includes the following features:

{% columns %}
{% column %}
{% content-ref url="ssl-tls.md" %}
[SSL/TLS](ssl-tls.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure SSL/TLS encryption for GridGain cluster nodes and clients, enable client certificate authentication, and manage certificates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication.md" %}
[Authentication](authentication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure authentication for a GridGain cluster: Ignite passcode, GridGain passcode, certificate, JAAS, composite, Control Center OpenID, and LDAP/AD authentication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authorization-permissions.md" %}
[Authorization and Permissions](authorization-permissions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain authorization: the permission string format, the defaultAllow property, the full list of supported permissions, and how to scope them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="multi-tenancy.md" %}
[Multi-Tenancy](multi-tenancy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Isolate tenant data in GridGain by creating per-tenant caches and assigning per-cache security permissions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="securing-data-deserial.md" %}
[Securing Data Deserialization](securing-data-deserial.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Restrict deserialization in GridGain with the IGNITE_MARSHALLER_WHITELIST and IGNITE_MARSHALLER_BLACKLIST system properties.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tde.md" %}
[Transparent Data Encryption](tde.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Transparent Data Encryption in GridGain: encrypt data at rest per cache, generate a master key, and rotate master and cache keys.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="securing-jmx.md" %}
[Securing JMX](securing-jmx.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Secure the JMX server that GridGain nodes start, by disabling remote JMX or enabling password authentication and SSL.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="auditing-events.md" %}
[Auditing](auditing-events.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain's event-based auditing to track user actions and export event information to an external system.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="custom-authenticators.md" %}
[Implementing Custom Authenticator](custom-authenticators.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Implement a custom GridGain authenticator, illustrated with a file-based ACL provider for PasscodeAuthenticator.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cluster-hardening.md" %}
[Cluster Hardening](cluster-hardening.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Harden a GridGain 8 cluster by preventing SQL injection with parameterized queries and switching to Spring 6.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cve.md" %}
[Security Vulnerabilities (CVE)](cve.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Full list of CVEs fixed across all GridGain 8 versions, with published dates, CVSS base scores, and the releases that contain each fix.
{% endcolumn %}
{% endcolumns %}
