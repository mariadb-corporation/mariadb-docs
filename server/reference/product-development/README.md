---
description: >-
  Provides background information and high-level resources aimed at engineers
  developing new MariaDB features and contributing to the ecosystem.
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
---

# Product Development

{% hint style="info" %}
This section contains background information, mostly aimed at engineers developing MariaDB features.
{% endhint %}

{% columns %}
{% column %}
{% content-ref url="mariadb-quality-development-rules.md" %}
[mariadb-quality-development-rules.md](mariadb-quality-development-rules.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Outlines strict quality standards for new features, including requirements for design specifications, testability, and mandatory Worklog quality checklists.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="uploading-package-to-ppa.md" %}
[uploading-package-to-ppa.md](uploading-package-to-ppa.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Provides instructions for developers to upload MariaDB source packages to a Personal Package Archive (PPA) using tools like dput for Ubuntu-based distributions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="server-development/mariadb-fault-finding/" %}
[mariadb-fault-finding](server-development/mariadb-fault-finding/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Offers deep-dive technical guides for diagnosing server issues, including trace file generation, debugger usage, and analyzing core dumps or memory usage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="plugin-development/" %}
[plugin-development](plugin-development/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Details the APIs and processes for extending MariaDB functionality through custom plugins, such as authentication, logging, or specialized server enhancements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="server-development/" %}
[server-development](server-development/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Covers foundational engineering topics, including the server roadmap, GitHub collaboration workflows, and quality assurance protocols for core contributions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-internals/" %}
[mariadb-internals](mariadb-internals/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Explores the low-level architecture of MariaDB, documenting source code internals, merging procedures, and how to use internal APIs in external programs.
{% endcolumn %}
{% endcolumns %}
