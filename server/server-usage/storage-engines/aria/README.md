---
description: >-
  Learn about the Aria storage engine in MariaDB Server. Understand its
  features, advantages, and use cases, particularly for crash-safe operations
  and transactional workloads.
---

# Aria

{% columns %}
{% column %}
{% content-ref url="aria-storage-engine.md" %}
[aria-storage-engine.md](aria-storage-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An overview of Aria, a storage engine designed as a crash-safe alternative to MyISAM, featuring transactional capabilities and improved caching.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-group-commit.md" %}
[aria-group-commit.md](aria-group-commit.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about Aria's group commit functionality, which improves performance by batching commit operations to the transaction log.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-status-variables.md" %}
[aria-status-variables.md](aria-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A list of status variables specific to the Aria engine, providing metrics on page cache usage, transaction log syncs, and other internal operations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-storage-formats.md" %}
[aria-storage-formats.md](aria-storage-formats.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the different row formats supported by Aria, particularly the default PAGE format which enables crash safety and better concurrency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-system-variables.md" %}
[aria-system-variables.md](aria-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A comprehensive list of system variables for configuring Aria, including buffer sizes, log settings, and recovery options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-two-step-deadlock-detection.md" %}
[aria-two-step-deadlock-detection.md](aria-two-step-deadlock-detection.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains Aria's deadlock detection mechanism, which uses a two-step process with configurable search depths and timeouts to resolve conflicts.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria-faq.md" %}
[aria-faq.md](aria-faq.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Frequently asked questions about the Aria storage engine, covering its history, comparison with MyISAM, and key features like crash safety.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="the-aria-name.md" %}
[the-aria-name.md](the-aria-name.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A brief history of the naming of the Aria storage engine, explaining its origins as "Maria" and the reasons for the eventual name change.
{% endcolumn %}
{% endcolumns %}
