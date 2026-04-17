---
description: >-
  Overview of different deployment architectures (single-node, primary/replica)
  & methods, including manual installation via repositories or tarballs, and
  automated deployment with tools like Ansible.
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

# Deployment Methods

## Overview of Deployment Methods

The most common way users acquire MariaDB is through Linux Distribution Repositories, as many prioritize the stability of native OS packaging. MariaDB’s Official Repositories follow closely, favored by those needing the latest features. Containerized deployments (Docker) and Cloud/Managed Services represent a significant and growing portion of the user base, reflecting a shift toward automated and outsourced infrastructure. Finally, a smaller group uses Direct Downloads (Tarballs/MSI) or Source Builds for specialized environments.

## Comparison of Installation Methods

<table data-header-hidden="false" data-header-sticky><thead><tr><th>Method</th><th>Pros</th><th>Cons</th></tr></thead><tbody><tr><td>Linux Distro Repos<br>(<a href="../installing-mariadb/binary-packages/installing-mariadb-deb-files.md">deb</a>, <a href="../installing-mariadb/binary-packages/rpm/">rpm</a>, <a href="../installing-mariadb/binary-packages/installing-mariadb-on-macos-using-homebrew.md">macOS</a>)</td><td>High stability; seamless OS integration; managed security updates.</td><td>Often contains older versions; slower feature rollout.</td></tr><tr><td><a href="../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md">MariaDB Repos</a>,<br><a href="../installing-mariadb/binary-packages/repo-mirror.md">Local Repository Mirror</a></td><td>Latest stable releases; direct support for new features.</td><td>Requires manual repo setup; potential dependency versioning issues.</td></tr><tr><td><a href="../../automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker.md">Docker</a> / <a href="../../automated-mariadb-deployment-and-administration/docker-and-mariadb/">Containers</a></td><td>Excellent isolation; high portability; ideal for microservices.</td><td>Networking/storage complexity; requires container expertise.</td></tr><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd/">Cloud / Managed</a></td><td>Minimal maintenance; automated backups/scaling; high availability.</td><td>Higher long-term cost; less control over configuration; vendor lock-in.</td></tr><tr><td><a href="../../../mariadb-quickstart-guides/installing-mariadb-server-guide.md#for-windows">Windows MSI</a></td><td>GUI-driven; handles service registration and basic security setup.</td><td>Limited to Windows; harder to automate at scale than CLI.</td></tr><tr><td><a href="../installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md">Binary Tarballs</a> / <a href="../installing-mariadb/binary-packages/package-tarballs.md">Package Tarballs</a></td><td>OS independent; allows multiple versions on one host; no root required.</td><td>Manual dependency management; requires manual path configuration.</td></tr><tr><td><a href="../installing-mariadb/compiling-mariadb-from-source/">Source Code</a></td><td>Maximum optimization for hardware; custom feature selection.</td><td>Extremely time-consuming; requires compilation expertise.</td></tr></tbody></table>

## See Also

[Where Do Users Get MariaDB Server From?](https://mariadb.org/where-do-users-get-mariadb-server-from/) • Blog • 2026 • 4 minutes

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
