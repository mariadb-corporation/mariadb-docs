---
description: >-
  Explains the Transaction Coordinator Log (tc.log), used to maintain
  consistency in distributed transactions (XA) across multiple storage engines
  or servers.
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

# Transaction Coordinator Log

{% columns %}
{% column %}
{% content-ref url="transaction-coordinator-log-overview.md" %}
[transaction-coordinator-log-overview.md](transaction-coordinator-log-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the purpose of the Transaction Coordinator (TC) log (`tc.log`), which maintains consistency for XA transactions that affect multiple storage engines, and how to configure it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="heuristic-recovery-with-the-transaction-coordinator-log.md" %}
[heuristic-recovery-with-the-transaction-coordinator-log.md](heuristic-recovery-with-the-transaction-coordinator-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes the process of heuristic recovery using the TC log to resolve "in-doubt" transactions that may occur after a server crash during a 2-phase commit.
{% endcolumn %}
{% endcolumns %}
