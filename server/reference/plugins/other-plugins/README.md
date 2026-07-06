---
description: >-
  Discover additional plugins that extend MariaDB Server functionality, such as
  the Disks, Feedback, and Query Response Time plugins, for specialized use
  cases.
---

# Other Plugins

{% columns %}
{% column %}
{% content-ref url="disks-plugin.md" %}
[disks-plugin.md](disks-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Disks plugin adds the DISKS table to the Information Schema, providing metadata about the system's disk storage and usage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="feedback-plugin.md" %}
[feedback-plugin.md](feedback-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Feedback plugin collects and sends anonymous server usage and configuration data to MariaDB to help improve the software.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="inet4.md" %}
[inet4.md](inet4.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The inet4 plugin provides the INET4 data type, allowing for efficient native storage and manipulation of IPv4 addresses as 4-byte binary strings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="metadata-lock-info-plugin.md" %}
[metadata-lock-info-plugin.md](metadata-lock-info-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This plugin creates the METADATA_LOCK_INFO table in the Information Schema, allowing users to view active metadata locks and their owners.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql_json.md" %}
[mysql_json.md](mysql_json.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MYSQL_JSON plugin provides a JSON data type alias for compatibility, ensuring that tables created with the MySQL JSON type can be read by MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mhnsw.md" %}
[mhnsw.md](mhnsw.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mhnsw plugin implements the Hierarchical Navigable Small World algorithm, enabling high-performance approximate nearest neighbor search for vector data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="online_alter_log.md" %}
[online_alter_log.md](online_alter_log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The online_alter_log plugin provides logging capabilities for online ALTER TABLE operations, helping administrators monitor and debug schema changes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="query-cache-information-plugin.md" %}
[query-cache-information-plugin.md](query-cache-information-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This plugin exposes the contents of the query cache via the QUERY_CACHE_INFO table in the Information Schema, aiding in performance analysis.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="query-response-time-plugin.md" %}
[query-response-time-plugin.md](query-response-time-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Query Response Time plugin collects and displays the distribution of query execution times, helping to identify performance bottlenecks.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="user-variables-plugin.md" %}
[user-variables-plugin.md](user-variables-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The User Variables plugin adds the USER_VARIABLES table to the Information Schema, allowing users to inspect defined user variables and their values.
{% endcolumn %}
{% endcolumns %}
