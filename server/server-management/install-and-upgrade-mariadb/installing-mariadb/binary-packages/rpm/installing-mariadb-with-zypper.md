# Installing MariaDB with zypper

On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM packages](./) from MariaDB's\
repository using [zypper](https://en.wikipedia.org/wiki/ZYpp).

This page walks you through the simple installation steps using `zypper`.

## Adding the MariaDB ZYpp repository

We currently have ZYpp repositories for the following Linux distributions:

* SUSE Linux Enterprise Server (SLES) 12
* SUSE Linux Enterprise Server (SLES) 15
* OpenSUSE 15
* OpenSUSE 42

### Using the MariaDB Package Repository Setup Script

If you want to install MariaDB with `zypper`, then you can configure `zypper` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../mariadb-package-repository-setup-and-usage.md).

MariaDB Corporation provides a MariaDB Package Repository for several Linux distributions that use `zypper` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](../../../../../clients-and-utilities/), [client libraries](../../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../../reference/plugins/), and [mariadb-backup](../../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/). The MariaDB Package Repository setup script automatically configures your system to install packages from the MariaDB Package Repository.

To use the script, execute the following command:

```
curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
```

Note that this script also configures a repository for [MariaDB MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) and a repository for MariaDB Tools, which currently only contains [Percona XtraBackup](../../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) and its dependencies.

See [MariaDB Package Repository Setup and Usage](../mariadb-package-repository-setup-and-usage.md) for more information.

### Using the MariaDB Repository Configuration Tool

If you want to install MariaDB with `zypper`, then you can configure `zypper` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).

The MariaDB Foundation provides a MariaDB repository for several Linux distributions that use `zypper` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](../../../../../clients-and-utilities/), [client libraries](../../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../../reference/plugins/), and [mariadb-backup](../../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/). The MariaDB Repository Configuration Tool can easily generate the appropriate commands to add the repository for your distribution.

For example, if you wanted to use the repository to install [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) on SLES 15, then you could use the following commands to add the MariaDB `zypper` repository:

```
sudo zypper addrepo --gpgcheck --refresh https://yum.mariadb.org/10.6/sles/15/x86_64 mariadb
sudo zypper --gpg-auto-import-keys refresh
```

### Pinning the MariaDB Repository to a Specific Minor Release

If you wish to pin the `zypper` repository to a specific minor release, or if you would like to downgrade to a specific minor release, then\
you can create a `zypper` repository with the URL hard-coded to that specific minor release.

The MariaDB Foundation archives repositories of old minor releases at the following URL:

*

So if you can't find the repository of a specific minor release at `yum.mariadb.org`, then it would be a good idea to check the archive.

For example, if you wanted to pin your repository to [MariaDB 10.6.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-21-release-notes) on SLES 15, then you could use the following commands to add the MariaDB `zypper` repository:

```
sudo zypper removerepo mariadb
sudo zypper addrepo --gpgcheck --refresh https://yum.mariadb.org/10.6.21/sles/15/x86_64 mariadb
```

## Updating the MariaDB ZYpp repository to a New Major Release

MariaDB's `zypper` repository can be updated to a new major release. How this is done depends on how you originally configured the repository.

### Updating the Major Release with the MariaDB Package Repository Setup Script

If you configured `zypper` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../mariadb-package-repository-setup-and-usage.md), then you can update the major release that the repository uses by running the script again.

### Updating the Major Release with the MariaDB Repository Configuration Tool

If you configured `zypper` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/), then you can update the major release that the repository uses by removing the repository for the old version and adding the repository for the new version.

First, you can remove the repository for the old version by executing the following command:

```
sudo zypper removerepo mariadb
```

After that, you can add the repository for the new version. For example, if you wanted to use the repository to install [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) on SLES 15, then you could use the following commands to add the MariaDB `zypper` repository:

```
sudo zypper addrepo --gpgcheck --refresh https://yum.mariadb.org/10.6/sles/15/x86_64 mariadb
sudo zypper --gpg-auto-import-keys refresh
```

After that, the repository should refer to [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106).

## Importing the MariaDB GPG Public Key

Before MariaDB can be installed, you also have to import the GPG public key that is used to verify the digital signatures of the packages in our repositories. This allows the `zypper` and `rpm` utilities to verify the integrity of the packages that they install.

The id of our GPG public key is `0xcbcb082a1bb943db`. The short form of the id\
is `0x1BB943DB`. The full key fingerprint is:

```
1993 69E5 404B D5FC 7D2F E43B CBCB 082A 1BB9 43DB
```

The [rpm](https://linux.die.net/man/8/rpm) utility can be used to import this key. For example:

```
sudo rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
```

Once the GPG public key is imported, you are ready to install packages from the repository.

## Installing MariaDB Packages with ZYpp

After the `zypper` repository is configured, you can install MariaDB by executing the [zypper](https://en.opensuse.org/SDB:Zypper_manual_\(plain\)) command. The specific command that you would use would depend on which specific packages that you want to install.

### Installing the Most Common Packages with ZYpp

To Install the most common packages, execute the following command:

```
sudo zypper install MariaDB-server galera-4 MariaDB-client MariaDB-shared MariaDB-backup MariaDB-common
```

### Installing MariaDB Server with ZYpp

To Install MariaDB Server, execute the following command:

```
sudo zypper install MariaDB-server
```

### Installing MariaDB Galera Cluster with ZYpp

The process to install MariaDB Galera Cluster with the MariaDB `zypper` repository is practically the same as installing standard MariaDB Server.

Galera Cluster support has been included in the standard MariaDB Server packages, so you will need to install the `MariaDB-server` package, as you normally would.

You also need to install the `galera-4` package to obtain the [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4 wsrep provider library.

To install MariaDB Galera Cluster, you could execute the following command:

```
sudo zypper install MariaDB-server MariaDB-client galera-4
```

If you haven't yet imported the MariaDB GPG public key, then `zypper` will prompt you to\
import it after it downloads the packages, but before it prompts you to install them.

See [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) for more information on MariaDB Galera Cluster.

### Installing MariaDB Clients and Client Libraries with ZYpp

[MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) has been included as the client library. However, the package name for the client library has not been changed.

To Install the clients and client libraries, execute the following command:

```
sudo zypper install MariaDB-client MariaDB-shared
```

### Installing mariadb-backup with ZYpp

To install [mariadb-backup](../../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/), execute the following command:

```
sudo zypper install MariaDB-backup
```

### Installing Plugins with ZYpp

Some [plugins](../../../../../reference/plugins/) may also need to be installed.

For example, to install the [cracklib\_password\_check](../../../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin, execute the following command:

```
sudo zypper install MariaDB-cracklib-password-check
```

### Installing Debug Info Packages with ZYpp

The MariaDB `zypper` repository also contains [debuginfo](https://en.opensuse.org/openSUSE:Packaging_guidelines#Debuginfo) packages. These package may be needed when [debugging a problem](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/how-to-produce-a-full-stack-trace-for-mariadbd).

#### Installing Debug Info for the Most Common Packages with ZYpp

To install [debuginfo](https://en.opensuse.org/openSUSE:Packaging_guidelines#Debuginfo) for the most common packages, execute the following command:

```
sudo zypper install MariaDB-server-debuginfo MariaDB-client-debuginfo MariaDB-shared-debuginfo MariaDB-backup-debuginfo MariaDB-common-debuginfo
```

#### Installing Debug Info for MariaDB Server with ZYpp

To install [debuginfo](https://en.opensuse.org/openSUSE:Packaging_guidelines#Debuginfo) for MariaDB Server, execute the following command:

```
sudo zypper install MariaDB-server-debuginfo
```

#### Installing Debug Info for MariaDB Clients and Client Libraries with ZYpp

[MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) has been included as the client library. However, the package name for the client library has not been changed.

To install [debuginfo](https://en.opensuse.org/openSUSE:Packaging_guidelines#Debuginfo) for the clients and client libraries, execute the following command:

```
sudo zypper install MariaDB-client-debuginfo MariaDB-shared-debuginfo
```

#### Installing Debug Info for mariadb-backup with ZYpp

To install [debuginfo](https://en.opensuse.org/openSUSE:Packaging_guidelines#Debuginfo) for [mariadb-backup](../../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/), execute the following command:

```
sudo zypper install MariaDB-backup-debuginfo
```

#### Installing Debug Info for Plugins with ZYpp

For some [plugins](../../../../../reference/plugins/), [debuginfo](https://en.opensuse.org/openSUSE:Packaging_guidelines#Debuginfo) may also need to be installed.

For example, to install [debuginfo](https://en.opensuse.org/openSUSE:Packaging_guidelines#Debuginfo) for the [cracklib\_password\_check](../../../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin, execute the following command:

```
sudo zypper install MariaDB-cracklib-password-check-debuginfo
```

### Installing Older Versions from the Repository

The MariaDB `zypper` repository contains the last few versions of MariaDB. To show what versions are available, use the following command:

```
zypper search --details MariaDB-server
```

In the output you will see the available versions.

To install an older version of a package instead of the latest version we just\
need to specify the package name, a dash, and then the version number. And we\
only need to specify enough of the version number for it to be unique from the\
other available versions.

However, when installing an older version of a package, if `zypper` has to install dependencies, then it will automatically choose to install the latest versions of those packages. To ensure that all MariaDB packages are on the same version in this scenario, it is necessary to specify them all.

The packages that the MariaDB-server package depend on are: MariaDB-client,\
MariaDB-shared, and MariaDB-common. Therefore, to install [MariaDB 10.6.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-21-release-notes) from this `zypper`\
repository, we would do the following:

```
sudo zypper install MariaDB-server-10.6.21 MariaDB-client-10.6.21 MariaDB-shared-10.6.21 MariaDB-backup-10.6.21 MariaDB-common-10.6.21
```

The rest of the install and setup process is as normal.

## After Installation

After the installation is complete, you can [start MariaDB](../../../../starting-and-stopping-mariadb/).

If you are using [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/), then keep in mind that the first node will have to be [bootstrapped](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/getting-started-with-mariadb-galera-cluster#bootstrapping-a-new-cluster).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
