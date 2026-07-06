---
description: >-
  Details the APIs and processes for extending MariaDB functionality through
  custom plugins, such as authentication, logging, or specialized server
  enhancements.
---

# Plugin Development

{% hint style="info" %}
This section contains background information, mostly aimed at engineers developing MariaDB features.
{% endhint %}

{% columns %}
{% column %}
{% content-ref url="development-writing-plugins-for-mariadb.md" %}
[development-writing-plugins-for-mariadb.md](development-writing-plugins-for-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A comprehensive guide on the basic structure and necessary components for creating a new plugin from scratch.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="encryption-plugin-api.md" %}
[encryption-plugin-api.md](encryption-plugin-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details the API used to develop encryption plugins for protecting data at rest, including key management and encryption schemes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="audit-plugin-development.md" %}
[audit-plugin-development.md](audit-plugin-development.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provides instructions for developing plugins that track and log server activity for security and compliance monitoring.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="authentication-plugin-development.md" %}
[authentication-plugin-development.md](authentication-plugin-development.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details how to implement custom authentication methods, allowing users to connect using external credentials or protocols.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="information-schema-plugins-show-and-flush-statements.md" %}
[information-schema-plugins-show-and-flush-statements.md](information-schema-plugins-show-and-flush-statements.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to create plugins that expose internal server data through virtual tables in the Information Schema.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-and-cluster-plugin-development.md" %}
[replication-and-cluster-plugin-development.md](replication-and-cluster-plugin-development.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Focuses on building plugins that interact with the server's replication stream or manage cluster-level synchronization.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="password-validation-plugin-development.md" %}
[password-validation-plugin-development.md](password-validation-plugin-development.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Implementation guide specifically for developers creating logic to intercept and validate password changes in the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="storage-engines-storage-engine-development/" %}
[storage-engines-storage-engine-development](storage-engines-storage-engine-development/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A dedicated resource for engineers to learn how to build or modify storage engines, detailing the pluggable API and data handling at the physical level.
{% endcolumn %}
{% endcolumns %}
