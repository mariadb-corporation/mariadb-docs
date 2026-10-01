---
description: >-
  Secure a GridGain 9 cluster with SSL/TLS encryption, user authentication,
  role-based authorization, row-level security, and data encryption at rest.
icon: shield-halved
---

# Security and Authentication

This section describes how to secure a GridGain 9 cluster. It covers encrypting communication with SSL/TLS, authenticating users, controlling access with role-based authorization and row-level security, issuing JWT tokens, the full list of user permissions and roles, and encrypting data at rest with transparent data encryption.

{% columns %}
{% column %}
{% content-ref url="ssl-tls.md" %}
[SSL/TLS](ssl-tls.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure SSL/TLS encryption between GridGain 9 cluster nodes and the clients that connect to them, including keystores, truststores, and mutual TLS.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication.md" %}
[Authentication](authentication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Enable and configure user authentication on a GridGain 9 cluster, using either basic authentication or an LDAP authentication provider.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="role-based-authorization.md" %}
[Role-Based Authorization](role-based-authorization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain 9 uses a flat role-based access control (RBAC) model that grants privileges to roles and assigns roles to users to manage cluster access.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="row-level-security.md" %}
[Row-Level Security](row-level-security.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Row-level security (RLS) restricts access to individual rows of a GridGain 9 table based on user roles, enforced by the database through security policies.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="jwt-authentication.md" %}
[JWT Authentication](jwt-authentication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain 9 supports JWT authentication for REST users, letting them obtain, use, and revoke JSON Web Tokens to authenticate to the cluster.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="user-permissions-and-roles.md" %}
[User Permissions and Roles](user-permissions-and-roles.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for GridGain 9 user privileges, listing every action and object, the protected built-in roles, and the object permission hierarchy.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transparent-data-encryption.md" %}
[Transparent Data Encryption](transparent-data-encryption.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Encrypt GridGain 9 data at rest with transparent data encryption (TDE), using a Java keystore or AWS KMS key encryption key provider.
{% endcolumn %}
{% endcolumns %}
