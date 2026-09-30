---
description: >-
  Control who can connect to a GridGain cluster and what they may do — authentication mechanisms, permission-based authorization, custom authenticators, and multi-tenant isolation.
---

# Authentication and Authorization

This section groups the following topics:

{% columns %}
{% column %}
{% content-ref url="../authentication.md" %}
[Authentication](../authentication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure authentication for a GridGain cluster: Ignite passcode, GridGain passcode, certificate, JAAS, composite, Control Center OpenID, and LDAP/AD authentication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../authorization-permissions.md" %}
[Authorization and Permissions](../authorization-permissions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain authorization: the permission string format, the defaultAllow property, the full list of supported permissions, and how to scope them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../custom-authenticators.md" %}
[Implementing Custom Authenticator](../custom-authenticators.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Implement a custom GridGain authenticator, illustrated with a file-based ACL provider for PasscodeAuthenticator.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../multi-tenancy.md" %}
[Multi-Tenancy](../multi-tenancy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Isolate tenant data in GridGain by creating per-tenant caches and assigning per-cache security permissions.
{% endcolumn %}
{% endcolumns %}
