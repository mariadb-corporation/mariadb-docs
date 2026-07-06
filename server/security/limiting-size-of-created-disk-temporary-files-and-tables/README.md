---
description: >-
  The ability to limit the size of created disk temporary files and tables was
  introduced in MariaDB 11.5.
---

# Limiting Size of Created Disk Temporary Files and Tables

{% columns %}
{% column %}
{% content-ref url="limiting-size-of-created-disk-temporary-files-and-tables-overview.md" %}
[limiting-size-of-created-disk-temporary-files-and-tables-overview.md](limiting-size-of-created-disk-temporary-files-and-tables-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of the feature introduced in MariaDB 11.5 to limit disk space used by temporary files and internal on-disk temporary tables to prevent disk exhaustion.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="max_tmp_session_space_usage-system-variable.md" %}
[max_tmp_session_space_usage-system-variable.md](max_tmp_session_space_usage-system-variable.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documentation for the system variable that restricts the maximum total size of temporary files and tables allowed for an individual user session.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="max_tmp_total_space_usage-system-variable.md" %}
[max_tmp_total_space_usage-system-variable.md](max_tmp_total_space_usage-system-variable.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the global system variable that defines the maximum cumulative disk space all user connections can consume for temporary files and tables.
{% endcolumn %}
{% endcolumns %}
