---
description: >-
  Troubleshoot InnoDB issues in MariaDB Server. Find solutions and best
  practices for common problems, ensuring your InnoDB-based applications run
  smoothly and efficiently.
---

# InnoDB Troubleshooting

{% columns %}
{% column %}
{% content-ref url="innodb-troubleshooting-overview.md" %}
[innodb-troubleshooting-overview.md](innodb-troubleshooting-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A starting point for diagnosing InnoDB issues, recommending checks on error logs, deadlocks, and table integrity using various tools.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-data-dictionary-troubleshooting.md" %}
[innodb-data-dictionary-troubleshooting.md](innodb-data-dictionary-troubleshooting.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to resolve inconsistencies between the InnoDB internal data dictionary and the file system, such as orphan .frm or .ibd files.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-recovery-modes.md" %}
[innodb-recovery-modes.md](innodb-recovery-modes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the different `innodb_force_recovery` levels, which allow you to start the server in read-only modes to recover data after a crash.
{% endcolumn %}
{% endcolumns %}
