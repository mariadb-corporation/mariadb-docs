---
description: >-
  Comprehensive guide to installing MariaDB using `yum` or `dnf` on RHEL,
  CentOS, and Fedora, covering repository configuration, GPG key import, and
  package installation.
---

# Installing MariaDB with yum/dnf

On RHEL, CentOS, Fedora, and other similar Linux RPM based distributions, these provide MariaDB packages. These are supported by those distributions. If you have a particular need for a later version than what is in the distribution, then MariaDB provides repositories for them.

Using repositories rather than installing RPM allows for an ease of update when a new release is made. It is highly recommended to install the relevant [RPM packages](./) from MariaDB's\
repository using [yum](https://en.wikipedia.org/wiki/Yum_\(software\)) or [dnf](https://en.wikipedia.org/wiki/DNF_\(software\)). Centos 7 still uses `yum`, most others use `dnf`, and SUSE/openSUSE use `zypper`.

This page walks you through the simple installation steps using `dnf` and `yum`.

## Adding the MariaDB YUM repository

We currently have YUM/DNF repositories for the following Linux distributions, and for the versions that are in standard (not extended) support:

* Red Hat Enterprise Linux (RHEL)
* CentOS
* Fedora
* openSUSE
* SUSE

### Using the MariaDB Package Repository Setup Script

If you want to install MariaDB with `yum`, then you can configure `yum` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../mariadb-package-repository-setup-and-usage.md).

MariaDB Corporation provides a MariaDB Package Repository for several Linux distributions that use `yum` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md), [client libraries](../../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../../reference/plugins/), and [mariadb-backup](../../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md). The MariaDB Package Repository setup script automatically configures your system to install packages from the MariaDB Package Repository.

To use the script, execute the following command:

```bash
curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
```

{% hint style="info" %}
The script also configures a repository for [MariaDB MaxScale](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-use-cases/maxscale-overview) and a repository for MariaDB Tools, which currently only contains [Percona XtraBackup](../../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) and its dependencies.

See [MariaDB Package Repository Setup and Usage](../mariadb-package-repository-setup-and-usage.md) for more information.
{% endhint %}

### Using the MariaDB Repository Configuration Tool

If you want to install MariaDB with `yum`, then you can configure `yum` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).

The MariaDB Foundation provides a MariaDB repository for several Linux distributions that use `yum` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](../../../../../clients-and-utilities/), [client libraries](../../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../../reference/plugins/), and [mariadb-backup](../../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md). The MariaDB Repository Configuration Tool can easily generate the appropriate configuration file to add the repository for your distribution.

Once you have the appropriate repository configuration section for your distribution, add it to a file named `MariaDB.repo` under `/etc/yum.repos.d/`.

For example, if you wanted to use the repository to install [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106) on RHEL (any version), then you could use the following `yum` repository configuration in `/etc/yum.repos.d/MariaDB.repo`:

```ini
[mariadb]
name = MariaDB
baseurl = https://rpm.mariadb.org/10.6/rhel/$releasever/$basearch
gpgkey= https://rpm.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
```

The example file above includes a `gpgkey` line to automatically fetch the\
GPG public key that is used to verify the digital signatures of the packages in our repositories. This allows the `yum`, `dnf`, and `rpm` utilities to verify the integrity of the packages that they install.

### Pinning the MariaDB Repository to a Specific Minor Release

If you wish to pin the `yum` repository to a specific minor release, or if you would like to do a `yum downgrade` to a specific minor release, then you can create a `yum` repository configuration with a `baseurl` option set to that specific minor release.

For example, if you wanted to pin your repository to [MariaDB 10.8.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-8-release-notes) on CentOS 7, then you could use the following `yum` repository configuration in `/etc/yum.repos.d/MariaDB.repo`:

```ini
[mariadb]
name = MariaDB-10.8.8
baseurl= http://archive.mariadb.org/mariadb-10.8.8/yum/centos/$releasever/$basearch
gpgkey= https://archive.mariadb.org/PublicKey
gpgcheck=1
```

To change an existing repository configuration, you may execute the following command:

```bash
sudo yum clean all
```

## Updating the MariaDB YUM repository to a New Major Release

MariaDB's `yum` repository can be updated to a new major release. How this is done depends on how you originally configured the repository.

### Updating the Major Release with the MariaDB Package Repository Setup Script

If you configured `yum` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../mariadb-package-repository-setup-and-usage.md), then you can update the major release that the repository uses by running the script again.

### Updating the Major Release with the MariaDB Repository Configuration Tool

If you configured `yum` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/), then you can update the major release that the repository uses by updating the `yum` repository configuration file in-place. For example, if you wanted to change the repository from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106) to [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), and if the repository configuration file was at `/etc/yum.repos.d/MariaDB.repo`, then you could execute the following:

```bash
sudo sed -i 's/10.6/10.11/' /etc/yum.repos.d/MariaDB.repo
```

After that, the repository should refer to [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011).

If the `yum` repository is pinned to a specific minor release, then the above `sed` command can result in an invalid repository configuration. In that case, the recommended options are:

* Edit the `MariaDB.repo` repository file manually.
* Or delete the `MariaDB.repo` repository file, and then install the repository of the new version with the more robust [MariaDB Package Repository setup script](../mariadb-package-repository-setup-and-usage.md).

## The MariaDB GPG Key

See the [GPG](../gpg.md) page for information on the various keys used by MariaDB.

## Installing MariaDB Packages with YUM/DNF

After the `dnf`/`yum` repository is configured, you can install MariaDB by executing the [dnf](https://www.man7.org/linux/man-pages/man8/dnf.8.html) or [yum](https://www.man7.org/linux/man-pages/man8/yum.8.html) command. The specific command that you would use would depend on which specific packages that you want to install.

### Installing the Most Common Packages

To Install the most common packages, execute the following command:

```bash
sudo dnf install MariaDB-server galera-4 MariaDB-client MariaDB-shared MariaDB-backup MariaDB-common
```

### Installing MariaDB Server

To Install MariaDB Server, execute the following command:

```bash
sudo dnf install MariaDB-server
```

### Installing MariaDB Galera Cluster with YUM

The process to install MariaDB Galera Cluster with the MariaDB `yum` repository is practically the same as installing standard MariaDB Server.

You need to install the `galera-4` package to obtain the [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4 wsrep provider library.

To install MariaDB Galera Cluster, you could execute the following command:

```bash
sudo dnf install MariaDB-server MariaDB-client galera-4
```

If you haven't yet imported the MariaDB GPG public key, then `yum` will prompt you to\
import it after it downloads the packages, but before it prompts you to install them.

See [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) for more information on MariaDB Galera Cluster.

### Installing MariaDB Clients and Client Libraries with YUM

[MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/mariadb-connector-c-guide) has been included as the client library (staticly linked). However, the package name for the client library has not been changed.

To Install the clients and client libraries, execute the following command:

```bash
sudo dnf install MariaDB-client MariaDB-shared
```

If you want compile your own programs against MariaDB Connector/C, execute the following command:

```bash
sudo dnf install MariaDB-devel
```

### Installing mariadb-backup with YUM

To install [mariadb-backup](../../../../../server-usage/backup-and-restore/mariadb-backup/), execute the following command:

```bash
sudo yum install MariaDB-backup
```

### Installing Plugins with YUM

Some [plugins](../../../../../reference/plugins/) may also need to be installed.

For example, to install the [cracklib\_password\_check](../../../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin, execute the following command:

```bash
sudo dnf install MariaDB-cracklib-password-check
```

### Installing Debug Info Packages with YUM

The MariaDB `yum` repository also contains [debuginfo](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/developing_c_and_cpp_applications_in_rhel_9/debugging-applications_developing-applications#debuginfo-packages_enabling-debugging-with-debugging-information) packages. These package may be needed when [debugging a problem](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/yt4NDbw3wL7QsDjQtA0H).

#### Installing Debug Info for the Most Common Packages with YUM

To install [debuginfo](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/developing_c_and_cpp_applications_in_rhel_9/debugging-applications_developing-applications#debuginfo-packages_enabling-debugging-with-debugging-information) for the most common packages, execute the following command:

```bash
sudo dnf install MariaDB-server-debuginfo MariaDB-client-debuginfo MariaDB-shared-debuginfo MariaDB-backup-debuginfo MariaDB-common-debuginfo
```

All packages have their debuginfo by appending `-debuginfo` to the package name.

#### Installing Debug Info for MariaDB Server with YUM

To install [debuginfo](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/developing_c_and_cpp_applications_in_rhel_9/debugging-applications_developing-applications#debuginfo-packages_enabling-debugging-with-debugging-information) for MariaDB Server, execute the following command:

```bash
sudo dnf install MariaDB-server-debuginfo
```

### Installing Older Versions from the Repository

The MariaDB `yum` repository contains the last few versions of MariaDB. To show what versions are available, use the following command:

```bash
sudo dnf list --showduplicates MariaDB-server
```

The output shows the available versions. For example:

```bash
sudo dnf list --showduplicates MariaDB-server
Last metadata expiration check: 0:01:42 ago on Fri 12 Dec 2025 03:47:20 PM UTC.
Available Packages
MariaDB-server.x86_64  11.8.2-1.el8                               mariadb-main
MariaDB-server.x86_64  12.0.2-1.el8                               mariadb-main
MariaDB-server.x86_64  12.1.2-1.el8                               mariadb-main
mariadb-server.x86_64  3:10.3.39-1.module+el8.8.0+1452+2a7eab68   appstream
```

The MariaDB repository in this example contains MariaDB 12.1.2, 12.0.2, and 11.8.2; and the appstream repository contains MariaDB 10.3.39.

To install an older version of a package instead of the latest version we just need to specify the package name, a dash, and then the version number. And we only need to specify enough of the version number for it to be unique from the other available versions.

However, when installing an older version of a package, if dependencies need to be installed, then it will automatically choose to install the latest versions of those packages, which can sometimes break those dependencies. To ensure that all MariaDB packages are on the same version in this scenario, it is necessary to specify them all.

The MariaDB packages that the `MariaDB-server` package depend on are: `MariaDB-client`, `MariaDB-shared`, and `MariaDB-common`. Therefore, to install MariaDB 12.0.2 from this `yum`\
repository, we could do the following (putting the version in a variable and each package on its own line so things are cleaner):

```bash
ver=12.0.2
sudo dnf install \
  MariaDB-server-${ver} \
  MariaDB-client-${ver} \
  MariaDB-shared-${ver} \
  MariaDB-common-${ver}
```

For MariaDB Enterprise it is necessary to specify the release part of the version number as well, but with an underscore (\_) instead of a dash (-), as that is how dnf/yum see the version number. For example, for MariaDB Enterprise Server 11.8.5-2 you would specify the version as `11.8.5_2`. For example:

```bash
ver=11.8.5_2
sudo dnf install \
  MariaDB-server-${ver} \
  MariaDB-client-${ver} \
  MariaDB-shared-${ver} \
  MariaDB-common-${ver}
```

The rest of the install and setup process is as normal.

## After Installation

After the installation is complete, you can [start MariaDB](../../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md) with:

```bash
sudo systemctl start mariadb 
```

If you are using [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/), then keep in mind that the first node will have to be [bootstrapped](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#bootstrapping-a-new-cluster).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
