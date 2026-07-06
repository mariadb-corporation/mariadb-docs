---
description: >-
  Learn about authentication with Pluggable Authentication Modules (PAM) in
  MariaDB Server. This section details how to integrate MariaDB with PAM for
  centralized and flexible user authentication.
---

# Authentication with Pluggable Authentication Modules (PAM)

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-pam.md" %}
[authentication-plugin-pam.md](authentication-plugin-pam.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The PAM authentication plugin delegates password validation to the operating system's PAM framework, enabling integration with LDAP, Kerberos, and other services.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-pam-authentication-and-user-mapping-with-ldap-authentication.md" %}
[configuring-pam-authentication-and-user-mapping-with-ldap-authentication.md](configuring-pam-authentication-and-user-mapping-with-ldap-authentication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn to configure the PAM plugin to authenticate users via LDAP and map LDAP groups to MariaDB accounts using the pam_user_map module.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-pam-authentication-and-user-mapping-with-unix-authentication.md" %}
[configuring-pam-authentication-and-user-mapping-with-unix-authentication.md](configuring-pam-authentication-and-user-mapping-with-unix-authentication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide shows how to authenticate database users using local Unix accounts and map Unix groups to MariaDB users with the PAM plugin.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="user-and-group-mapping-with-pam.md" %}
[user-and-group-mapping-with-pam.md](user-and-group-mapping-with-pam.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The pam_user_map PAM module allows administrators to map external PAM users and groups to specific MariaDB accounts for flexible authorization management.
{% endcolumn %}
{% endcolumns %}
