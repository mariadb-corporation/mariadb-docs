---
description: >-
  Overview of different deployment architectures (single-node, primary/replica)
  & methods, including manual installation via repositories or tarballs, and
  automated deployment with tools like Ansible.
---

# Deployment Methods

| Method                                                                                                                             | Typical use case                                                                                                     |
| ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [Binary Tarball](../installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md)                                      | Use in-house infrastructure and tooling to deploy pre-compiled MariaDB binaries from a compressed tar archive        |
| [Docker](../../automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker.md) | Use Docker and the MariaDB Enterprise Docker Registry to deploy in a container                                       |
| [Local Repository Mirror](../installing-mariadb/binary-packages/repo-mirror.md)                                                    | Use OS package manager to deploy standard OS packages from local mirror of MariaDB's repository                      |
| [Package Tarball](../installing-mariadb/binary-packages/package-tarballs.md)                                                       | Use OS package manager to deploy standard OS packages from a compressed tar archive without repository configuration |
| [Repository](../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md)                                  | Use OS package manager to deploy standard OS packages from MariaDB's repository                                      |

Available deployment methods are component-specific.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
