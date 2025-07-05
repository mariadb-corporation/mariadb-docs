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

* MariaDB ColumnStore 5 (included with MariaDB Community Server 10.5)
* MariaDB ColumnStore 6 (included with MariaDB Community Server 10.6)
* MariaDB Community Server 10.2
* MariaDB Community Server 10.3
* MariaDB Community Server 10.4
* MariaDB Community Server 10.5 (excluding ColumnStore 5)
* MariaDB Community Server 10.6 (excluding ColumnStore 6)
* MariaDB Enterprise ColumnStore 5 (included with MariaDB Enterprise Server 10.5)
* MariaDB Enterprise ColumnStore 6 (included with MariaDB Enterprise Server 10.6)
* MariaDB Enterprise Server 10.2
* MariaDB Enterprise Server 10.3
* MariaDB Enterprise Server 10.4
* MariaDB Enterprise Server 10.5
* MariaDB Enterprise Server 10.6
* MariaDB Enterprise Server 11.4
* MariaDB MaxScale 2.4
* MariaDB MaxScale 2.5
* MariaDB MaxScale 6
* MariaDB MaxScale 22.08

## Operating System Package Managers

The package manager depends on the operating system:

| Operating System                          | Package Manager |
| ----------------------------------------- | --------------- |
| Operating System                          | Package Manager |
| CentOS 7                                  | YUM             |
| Debian 9                                  | APT             |
| Debian 10                                 | APT             |
| Debian 11                                 | APT             |
| Red Hat Enterprise Linux 7 (RHEL 7)       | YUM             |
| Red Hat Enterprise Linux 8 (RHEL 8)       | YUM             |
| Rocky Linux 8                             | YUM             |
| SUSE Linux Enterprise Server 12 (SLES 12) | ZYpp            |
| SUSE Linux Enterprise Server 15 (SLES 15) | ZYpp            |
| Ubuntu 18.04 LTS (Bionic Beaver)          | APT             |
| Ubuntu 20.04 LTS (Focal Fossa)            | APT             |

## Create a Local Repository Mirror

Creating a local mirror of the MariaDB Enterprise Repository or the MariaDB Community Repository enables you to distribute MariaDB products to your servers from a local repository you support. Secure any such repository mirror to prevent outside access.

1. [Configure a MariaDB repository.](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/getting-installing-and-upgrading-mariadb/binary-packages/repo/README.md#configure-mariadb-repository)
2. Set up a repository mirroring tool, for example:

* For YUM: `reposync`, available at: [23016](https://access.redhat.com/solutions/23016)
* For APT: `debmirror`, available at: [Setup#Debian\_Repository\_Mirroring\_Tools](https://wiki.debian.org/DebianRepository/Setup#Debian_Repository_Mirroring_Tools)

1. Secure the repository mirror to prevent outside access.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
