---
description: How to install MariaDB on systems that use the yum or dnf package managers
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

MariaDB provides two helpful scripts for setting up repositories, one for MariaDB Community Server named `mariadb_repo_setup`, and one for MariaDB Enterprise Server named `mariadb_es_repo_setup`.

See the [Using MariaDB Corporation's Repository Setup Scripts](../../../mariadb-package-repository-setup-and-usage.md#using-mariadb-corporations-repository-setup-scripts) section on the [MariaDB Package Repository Setup and Usage](../../../mariadb-package-repository-setup-and-usage.md) page for information on using these scripts.

### Using the MariaDB Foundation Repository Configuration Tool

Visit [https://mariadb.org/download/?t=repo-config](https://mariadb.org/download/?t=repo-config) and follow the instructions from there. It will ask for your Linux distribution, desired MariaDB version, and the mirror to use, and will show what files to edit and what commands to run to configure a repository.

### Pinning the MariaDB Repository to a Specific Minor Release

If you wish to pin your `yum` or `dnf` repository to a specific minor release, or if you would like to downgrade to a specific minor release, then you can configure a repository with the URL hard-coded to that specific minor release.

{% tabs %}
{% tab title="MariaDB Corporation repo setup scripts" %}
If you used [MariaDB Corporation's `mariadb_repo_setup` or `mariadb_es_repo_setup` scripts](../../../mariadb-package-repository-setup-and-usage.md) to generate your repository configuration, simply re-run the script and specify the full version number to use with the `--mariadb-server-version` option.

See [Pinning the Repository to a Specific Minor Release](../../../mariadb-package-repository-setup-and-usage.md#pinning-the-repository-to-a-specific-minor-release) on the [MariaDB Package Repository Setup and Usage](../../../mariadb-package-repository-setup-and-usage.md) page for details.

The full list of MariaDB Enterprise Server releases can be found on the [Enterprise Server - All Releases](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/all-releases) page.
{% endtab %}

{% tab title="MariaDB Foundation repo config tool" %}
If you used the [MariaDB Foundation's Repository Configuration tool](https://mariadb.org/download/?t=repo-config), then you need to update the repository file you created to include the full version number to use on the `baseurl` line.

By default the Foundation's tool configures repositories with just the main series of MariaDB, e.g. `mariadb-11.8`, and to pin to a specific version you need to specify the full version, for example `mariadb-11.8.6`.

The full list of MariaDB Community Server releases can be found on the [Community Server - All Releases](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/all-releases) page.

For example, to pin your repository to MariaDB 11.8.6 on RHEL/Alma/Rocky 8, 9, or 10, then you could use the following repository configuration in `/etc/yum.repos.d/MariaDB.repo`:

```ini
[mariadb]
name = MariaDB-11.8.6
baseurl= http://archive.mariadb.org/mariadb-11.8.6/yum/rhel/$releasever/$basearch
gpgkey= https://archive.mariadb.org/PublicKey
gpgcheck=1
```

After updating the repository configuration, it is a good idea to clean the repository metadata with:

```bash
sudo dnf clean all
```
{% endtab %}
{% endtabs %}

## Updating the MariaDB YUM repository to a New Major Release

MariaDB's `yum` repository can be updated to a new major release. How this is done depends on how you originally configured the repository.

### Updating the Major Release with the MariaDB Package Repository Setup Script

If you configured `yum` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../../mariadb-package-repository-setup-and-usage.md), then you can update the major release that the repository uses by running the script again.

### Updating the Major Release with the MariaDB Repository Configuration Tool

If you configured `yum` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/), then you can update the major release that the repository uses by updating the `yum` repository configuration file in-place. For example, if you wanted to change the repository from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/what-is-mariadb-106) to [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011), and if the repository configuration file was at `/etc/yum.repos.d/MariaDB.repo`, then you could execute the following:

```bash
sudo sed -i 's/10.6/10.11/' /etc/yum.repos.d/MariaDB.repo
```

After that, the repository should refer to [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011).

If the `yum` repository is pinned to a specific minor release, then the above `sed` command can result in an invalid repository configuration. In that case, the recommended options are:

* Edit the `MariaDB.repo` repository file manually.
* Or delete the `MariaDB.repo` repository file, and then install the repository of the new version with the more robust [MariaDB Package Repository setup script](../../../mariadb-package-repository-setup-and-usage.md).

## The MariaDB GPG Key

See the [GPG](../gpg.md) page for information on the various keys used by MariaDB.

## Installing MariaDB Packages with YUM/DNF

After the `dnf`/`yum` repository is configured, you can install MariaDB by executing the [dnf](https://www.man7.org/linux/man-pages/man8/dnf.8.html) or [yum](https://www.man7.org/linux/man-pages/man8/yum.8.html) command. The specific command that you would use would depend on which specific packages that you want to install.

### Installing the Most Common Packages

To Install the most common packages, execute the following command:

```bash
sudo dnf install MariaDB-server MariaDB-server-galera galera-4 MariaDB-client MariaDB-shared MariaDB-backup MariaDB-common
```

### Installing MariaDB Server

To Install MariaDB Server, execute the following command:

```bash
sudo dnf install MariaDB-server
```

### Installing MariaDB Galera Cluster with YUM

{% hint style="info" %}
Note for MariaDB 12.3 and later: Galera Cluster support is no longer included in the base `MariaDB-server` package. To enable cluster functionality, you must explicitly install the `MariaDB-server-galera` package. This package contains cluster-specific scripts, systemd bootstrap capability, and the `wsrep_info` plugin.
{% endhint %}

You need to install the `galera-4` package to obtain the [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) 4 wsrep provider library.

To install MariaDB Galera Cluster, you could execute the following command:

```bash
sudo dnf install MariaDB-server MariaDB-server-galera MariaDB-client galera-4
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
