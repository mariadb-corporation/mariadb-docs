---
description: >-
  Explore the authentication plugins available in MariaDB, such as ed25519,
  GSSAPI, and PAM, which provide flexible and secure methods for user
  verification.
---

# Authentication Plugins

{% columns %}
{% column %}
{% content-ref url="pluggable-authentication-overview.md" %}
[pluggable-authentication-overview.md](pluggable-authentication-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Pluggable authentication allows MariaDB to use various authentication methods, enabling external validation, different hashing algorithms, and role-based access control.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-caching_sha2_password.md" %}
[authentication-plugin-caching_sha2_password.md](authentication-plugin-caching_sha2_password.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MySQL-compatible caching_sha2_password authentication plugin, for migrating MySQL users to MariaDB without changing their passwords (migration use; PARSEC is recommended otherwise).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-ed25519.md" %}
[authentication-plugin-ed25519.md](authentication-plugin-ed25519.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The ed25519 authentication plugin provides high-security password authentication using the Elliptic Curve Digital Signature Algorithm, a modern alternative to SHA-1.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-gssapi.md" %}
[authentication-plugin-gssapi.md](authentication-plugin-gssapi.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete GSSAPI authentication setup: Kerberos/SSPI single sign-on, INSTALL SONAME 'auth_gssapi', gssapi_keytab_path/principal_name, CREATE USER syntax.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-mysql_native_password.md" %}
[authentication-plugin-mysql_native_password.md](authentication-plugin-mysql_native_password.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete Authentication Plugin - mysql_native_password guide for MariaDB. Complete reference documentation for implementation, configuration, and usage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-mysql_old_password.md" %}
[authentication-plugin-mysql_old_password.md](authentication-plugin-mysql_old_password.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This plugin provides backward compatibility for pre-4.1 clients using an older, insecure password hashing algorithm and should not be used for new installations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-named-pipe.md" %}
[authentication-plugin-named-pipe.md](authentication-plugin-named-pipe.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The named_pipe authentication plugin allows Windows users connecting via named pipes to authenticate using their operating system credentials without a password.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-parsec.md" %}
[authentication-plugin-parsec.md](authentication-plugin-parsec.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
PARSEC is a modern, secure authentication plugin that uses salted passwords and elliptic curve cryptography to prevent replay attacks and secure user credentials.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-sha-256.md" %}
[authentication-plugin-sha-256.md](authentication-plugin-sha-256.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The SHA-256 authentication plugin uses the SHA-256 hashing algorithm for password storage, offering stronger security than the default SHA-1 method.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-unix-socket.md" %}
[authentication-plugin-unix-socket.md](authentication-plugin-unix-socket.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Official Unix socket authentication: OS user login via SO_PEERCRED/uid matching, CREATE USER IDENTIFIED VIA unix_socket, and unix_socket force modes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-with-pluggable-authentication-modules-pam/" %}
[authentication-with-pluggable-authentication-modules-pam](authentication-with-pluggable-authentication-modules-pam/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about authentication with Pluggable Authentication Modules (PAM) in MariaDB Server. This section details how to integrate MariaDB with PAM for centralized and flexible user authentication.
{% endcolumn %}
{% endcolumns %}
