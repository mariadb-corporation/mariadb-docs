---
description: >-
  Explore plugins in MariaDB Server. This section details how to extend database
  functionality, security, and performance by leveraging various loadable
  plugins, from authentication to storage engines.
---

# Plugins

{% columns %}
{% column %}
{% content-ref url="plugin-overview.md" %}
[plugin-overview.md](plugin-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB supports loading plugins at startup or runtime to extend functionality, including storage engines, security features, and logging capabilities, without rebuilding the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="information-on-plugins/list-of-plugins.md" %}
[list-of-plugins.md](information-on-plugins/list-of-plugins.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page lists the maturity level (Alpha, Beta, Gamma, Stable) of various MariaDB plugins, helping users determine which are suitable for production environments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-audit.md" %}
[mariadb-enterprise-audit.md](mariadb-enterprise-audit.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Enterprise Audit plugin logs detailed data access and configuration changes, offering advanced filtering to meet security and compliance requirements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin/" %}
[mariadb-audit-plugin](mariadb-audit-plugin/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete MariaDB Audit Plugin reference: server_audit activity logging, connection/query event tracking, file/syslog output, and compliance configuration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugins/" %}
[authentication-plugins](authentication-plugins/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the authentication plugins available in MariaDB, such as ed25519, GSSAPI, and PAM, which provide flexible and secure methods for user verification.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-replication-cluster-plugins/" %}
[mariadb-replication-cluster-plugins](mariadb-replication-cluster-plugins/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This section covers plugins specifically designed for high availability and clustering, including the wsrep_provider plugin used for Galera Cluster integration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="other-plugins/" %}
[other-plugins](other-plugins/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discover additional plugins that extend MariaDB Server functionality, such as the Disks, Feedback, and Query Response Time plugins, for specialized use cases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="password-validation-plugins/" %}
[password-validation-plugins](password-validation-plugins/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Password validation plugins, like simple_password_check and cracklib, enforce strong password policies by checking new passwords against defined complexity rules.
{% endcolumn %}
{% endcolumns %}
