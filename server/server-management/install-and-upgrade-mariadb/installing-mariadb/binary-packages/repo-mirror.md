---
description: >-
  Learn how to create and maintain local mirrors of MariaDB package repositories
  for secure or air-gapped deployments.
---

# Deploy with Local Package Repository Mirrors

MariaDB Corporation provides package repositories, including the MariaDB Enterprise Repository and the MariaDB Community Repository, that can be used to install MariaDB products using the operating system's package manager. Local mirrors of the package repositories can be used for local deployments.

Local package repository mirrors provide multiple benefits:

* MariaDB Corporation's official package repositories are the source for the local mirror.
* Tools provided by the operating system are used to create and maintain the local mirror.
* After a local mirror is created, the mirror can be used just like the MariaDB repositories to install MariaDB products using the operating system's package manager.

If you want to deploy MariaDB database products without using a local package repository mirror, [alternative deployment methods](../../deployment-general-installing-and-upgrading-instructions/deployment-methods.md) are available. Available deployment methods are component-specific.

## Use Cases

MariaDB database products can be deployed with local package repository mirrors to support use cases, such as:

* Install from the mirror on an air-gapped network that is not connected to the internet
* Remove packages from mirror for versions that are not used in the local environment
* Add packages to mirror for tools and clients that are used in the local environment
* Automatically install missing dependencies using a package manager

## Compatibility

The following MariaDB database products can be deployed using package repositories:

* MariaDB Community Server 10.6
* MariaDB Community Server 10.11
* MariaDB Community Server 11.4
* MariaDB Community Server 11.8
* MariaDB Community Server 12.3
* MariaDB Enterprise Server 10.6
* MariaDB Enterprise Server 11.4
* MariaDB Enterprise Server 11.8
* MariaDB MaxScale 23.02
* MariaDB MaxScale 23.08
* MariaDB MaxScale 24.02
* MariaDB MaxScale 25.01

## Operating System Package Managers

The package manager depends on the operating system:

| Operating System                          | Package Manager |
| ----------------------------------------- | --------------- |
| Debian 11                                 | APT             |
| Debian 12                                 | APT             |
| Debian 13                                 | APT             |
| Red Hat Enterprise Linux 8 (RHEL 8)       | DNF             |
| Red Hat Enterprise Linux 9 (RHEL 9)       | DNF             |
| Red Hat Enterprise Linux 10 (RHEL 10)     | DNF             |
| Rocky Linux 8                             | DNF             |
| Rocky Linux 9                             | DNF             |
| Rocky Linux 10                            | DNF             |
| SUSE Linux Enterprise Server 12 (SLES 12) | ZYpp            |
| SUSE Linux Enterprise Server 15 (SLES 15) | ZYpp            |
| Ubuntu 22.04 LTS (Jammy)                  | APT             |
| Ubuntu 24.04 LTS (Noble)                  | APT             |

## Create a Local Repository Mirror

Creating a local mirror of the MariaDB Enterprise Repository or the MariaDB Community Repository enables you to distribute MariaDB products to your servers from a local repository you support. Secure any such repository mirror to prevent outside access.

1. [Configure a MariaDB repository](../../mariadb-package-repository-setup-and-usage.md)
2. Set up a repository mirroring tool, for example:
   * YUM: `reposync`, available at: [23016](https://access.redhat.com/solutions/23016)
   * APT: `debmirror`, available at: [Setup#Debian\_Repository\_Mirroring\_Tools](https://wiki.debian.org/DebianRepository/Setup#Debian_Repository_Mirroring_Tools)
3. Secure the repository mirror to prevent outside access.

{% include "../../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
