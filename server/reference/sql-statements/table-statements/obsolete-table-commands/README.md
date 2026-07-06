---
description: >-
  Browse documentation for removed table commands. This section covers obsolete
  statements like BACKUP TABLE and RESTORE TABLE.
---

# Obsolete Table Statements

{% columns %}
{% column %}
{% content-ref url="backup-table-removed.md" %}
[backup-table-removed.md](backup-table-removed.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documents the removed BACKUP TABLE statement, which unreliably copied MyISAM tables to a backup directory, and points to mysqldump and MariaDB Backup as replacements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="restore-table-removed.md" %}
[restore-table-removed.md](restore-table-removed.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documents the removed RESTORE TABLE statement, which unreliably restored MyISAM tables from a BACKUP TABLE backup directory, and points to mysqldump and other tools as replacements.
{% endcolumn %}
{% endcolumns %}
