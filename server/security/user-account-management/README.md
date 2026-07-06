---
description: >-
  Master user account management in MariaDB Server. This section covers
  creating, modifying, and revoking user privileges to ensure secure and
  controlled access to your databases.
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
  tags:
    visible: true
---

# User Account Management

{% columns %}
{% column %}
{% content-ref url="roles/" %}
[roles](roles/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Manage roles in MariaDB Server for streamlined user access control. This section explains how to create, assign, and manage roles to simplify privilege management and enhance security.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="account-locking.md" %}
[account-locking.md](account-locking.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to lock and unlock user accounts using CREATE USER and ALTER USER statements to prevent login access without deleting the account.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-from-mariadb-10-4.md" %}
[authentication-from-mariadb-10-4.md](authentication-from-mariadb-10-4.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details the authentication changes introduced in MariaDB 10.4, including multiple authentication plugins per user, the mysql.global_priv table, and the default unix_socket authentication for root.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="incrementing-of-the-access_denied_errors-status-variable.md" %}
[incrementing-of-the-access_denied_errors-status-variable.md](incrementing-of-the-access_denied_errors-status-variable.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes the conditions that trigger the access_denied_errors status variable, such as failed logins, invalid privileges, or missing SSL requirements, aiding in security monitoring.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="user-password-expiry.md" %}
[user-password-expiry.md](user-password-expiry.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guide to configuring password expiration policies, including setting global lifetimes via default_password_lifetime or per-user limits, and handling expired password connections.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="catalogs/" %}
[catalogs](catalogs/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to Catalogs, a multi-tenancy feature for isolating database objects and users, planned for future MariaDB releases.
{% endcolumn %}
{% endcolumns %}
