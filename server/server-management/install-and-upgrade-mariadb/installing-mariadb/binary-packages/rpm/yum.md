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

MariaDB Corporation provides a MariaDB Package Repository for several Linux distributions that use `yum` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md), [client libraries](../../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../../reference/plugins/), and [mariadb-backup](../../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/). The MariaDB Package Repository setup script automatically configures your system to install packages from the MariaDB Package Repository.

To use the script, execute the following command:

```
curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
```

Note that this script also configures a repository for [MariaDB MaxScale](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/maxscale/README.md) and a repository for MariaDB Tools, which currently only contains [Percona XtraBackup](../../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) and its dependencies.

See [MariaDB Package Repository Setup and Usage](../mariadb-package-repository-setup-and-usage.md) for more information.

### Using the MariaDB Repository Configuration Tool

If you want to install MariaDB with `yum`, then you can configure `yum` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).

The MariaDB Foundation provides a MariaDB repository for several Linux distributions that use `yum` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md), [client libraries](../../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../../reference/plugins/), and [mariadb-backup](../../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/). The MariaDB Repository Configuration Tool can easily generate the appropriate configuration file to add the repository for your distribution.

Once you have the appropriate repository configuration section for your distribution, add it to a file named `MariaDB.repo` under `/etc/yum.repos.d/`.

For example, if you wanted to use the repository to install [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) on RHEL (any version), then you could use the following `yum` repository configuration in `/etc/yum.repos.d/MariaDB.repo`:

```
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

The MariaDB Foundation archives repositories all releases is at the following URL:

*

Note this isn't configured as a highly available server. For that purpose please use the main mirrors.

For example, if you wanted to pin your repository to [MariaDB 10.8.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-8-release-notes) on CentOS 7, then you could use the following `yum` repository configuration in `/etc/yum.repos.d/MariaDB.repo`:

```
[mariadb]
name = MariaDB-10.8.8
baseurl= http://archive.mariadb.org/mariadb-10.8.8/yum/centos/$releasever/$basearch
gpgkey= https://archive.mariadb.org/PublicKey
gpgcheck=1
```

Note that if you change an existing repository configuration, then you may need to execute the following:

```
sudo yum clean all
```

## Updating the MariaDB YUM repository to a New Major Release

MariaDB's `yum` repository can be updated to a new major release. How this is done depends on how you originally configured the repository.

### Updating the Major Release with the MariaDB Package Repository Setup Script

If you configured `yum` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../mariadb-package-repository-setup-and-usage.md), then you can update the major release that the repository uses by running the script again.

### Updating the Major Release with the MariaDB Repository Configuration Tool

If you configured `yum` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/), then you can update the major release that the repository uses by updating the `yum` repository configuration file in-place. For example, if you wanted to change the repository from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) to [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/what-is-mariadb-1011), and if the repository configuration file was at `/etc/yum.repos.d/MariaDB.repo`, then you could execute the following:

```
sudo sed -i 's/10.6/10.11/' /etc/yum.repos.d/MariaDB.repo
```

After that, the repository should refer to [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/what-is-mariadb-1011).

If the `yum` repository is pinned to a specific minor release, then the above `sed` command can result in an invalid repository configuration. In that case, the recommended options are:

* Edit the `MariaDB.repo` repository file manually.
* Or delete the `MariaDB.repo` repository file, and then install the repository of the new version with the more robust [MariaDB Package Repository setup script](../mariadb-package-repository-setup-and-usage.md).

## Importing the MariaDB GPG Public Key

Before MariaDB can be installed, you also have to import the GPG public key that is used to verify the digital signatures of the packages in our repositories. This allows the `yum`, `dnf` and `rpm` utilities to verify the integrity of the packages that they install.

The id of our GPG public key is:

* short form: `0xC74CD1D8`
* long form: `0xF1656F24C74CD1D8`
* full fingerprint: `177F 4010 FE56 CA33 3630 0305 F165 6F24 C74C D1D8`

`yum` should prompt you to import the GPG public key the first time that you install a package from MariaDB's repository. However, if you like, the [rpm](https://linux.die.net/man/8/rpm) utility can be used to manually import this key instead. For example:

```
sudo rpm --import https://supplychain.mariadb.com/MariaDB-Server-GPG-KEY
```

Once the GPG public key is imported, you are ready to install packages from the repository.

### Old Key

For releases before 2023 an older SHA1 based GPG key was used.

The id of this older GPG public key was `0xcbcb082a1bb943db`. The short form was `0x1BB943DB`. The full key fingerprint was:

```
1993 69E5 404B D5FC 7D2F E43B CBCB 082A 1BB9 43DB
```

## Installing MariaDB Packages with YUM/DNF

After the `dnf`/`yum` repository is configured, you can install MariaDB by executing the [dnf](https://www.man7.org/linux/man-pages/man8/dnf.8.html) or [yum](https://www.man7.org/linux/man-pages/man8/yum.8.html) command. The specific command that you would use would depend on which specific packages that you want to install.

### Installing the Most Common Packages

To Install the most common packages, execute the following command:

```
sudo dnf install MariaDB-server galera-4 MariaDB-client MariaDB-shared MariaDB-backup MariaDB-common
```

### Installing MariaDB Server

To Install MariaDB Server, execute the following command:

```
sudo dnf install MariaDB-server
```

### Installing MariaDB Galera Cluster with YUM

The process to install MariaDB Galera Cluster with the MariaDB `yum` repository is practically the same as installing standard MariaDB Server.

You need to install the `galera-4` package to obtain the [Galera](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md) 4 wsrep provider library.

To install MariaDB Galera Cluster, you could execute the following command:

```
sudo yum install MariaDB-server MariaDB-client galera-4
```

If you haven't yet imported the MariaDB GPG public key, then `yum` will prompt you to\
import it after it downloads the packages, but before it prompts you to install them.

See [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md) for more information on MariaDB Galera Cluster.

### Installing MariaDB Clients and Client Libraries with YUM

[MariaDB Connector/C](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/about-mariadb-connector-c/README.md) has been included as the client library (staticly linked). However, the package name for the client library has not been changed.

To Install the clients and client libraries, execute the following command:

```
sudo yum install MariaDB-client MariaDB-shared
```

If you want compile your own programs against [MariaDB Connector/C](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/about-mariadb-connector-c/README.md), execute the following command:

```
sudo yum install MariaDB-devel
```

### Installing mariadb-backup with YUM

To install [mariadb-backup](../../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/), execute the following command:

```
sudo yum install MariaDB-backup
```

### Installing Plugins with YUM

Some [plugins](../../../../../reference/plugins/) may also need to be installed.

For example, to install the [cracklib\_password\_check](../../../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin, execute the following command:

```
sudo yum install MariaDB-cracklib-password-check
```

### Installing Debug Info Packages with YUM

The MariaDB `yum` repository also contains [debuginfo](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/developing_c_and_cpp_applications_in_rhel_9/debugging-applications_developing-applications#debuginfo-packages_enabling-debugging-with-debugging-information) packages. These package may be needed when [debugging a problem](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/how-to-produce-a-full-stack-trace-for-mariadbd).

#### Installing Debug Info for the Most Common Packages with YUM

To install [debuginfo](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/developing_c_and_cpp_applications_in_rhel_9/debugging-applications_developing-applications#debuginfo-packages_enabling-debugging-with-debugging-information) for the most common packages, execute the following command:

```
sudo yum install MariaDB-server-debuginfo MariaDB-client-debuginfo MariaDB-shared-debuginfo MariaDB-backup-debuginfo MariaDB-common-debuginfo
```

All packages have their debuginfo by appending `-debuginfo` to the package name.

#### Installing Debug Info for MariaDB Server with YUM

To install [debuginfo](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/developing_c_and_cpp_applications_in_rhel_9/debugging-applications_developing-applications#debuginfo-packages_enabling-debugging-with-debugging-information) for MariaDB Server, execute the following command:

```
sudo yum install MariaDB-server-debuginfo
```

### Installing Older Versions from the Repository

The MariaDB `yum` repository contains the last few versions of MariaDB. To show what versions are available, use the following command:

```
yum list --showduplicates MariaDB-server
```

The output shows the available versions. For example:

```
$ yum list --showduplicates MariaDB-server
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: centos.mirrors.ovh.net
 * extras: centos.mirrors.ovh.net
 * updates: centos.mirrors.ovh.net
Available Packages
MariaDB-server.x86_64   10.3.10-1.el7.centos    mariadb
MariaDB-server.x86_64   10.3.11-1.el7.centos    mariadb
MariaDB-server.x86_64   10.3.12-1.el7.centos    mariadb
mariadb-server.x86_64   1:5.5.60-1.el7_5         base
```

The MariaDB `yum` repository in this example contains [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes), [MariaDB 10.3.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10311-release-notes), and [MariaDB 10.3.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10312-release-notes). The CentOS base `yum` repository also contains [MariaDB 5.5.60](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5560-release-notes).

To install an older version of a package instead of the latest version we just\
need to specify the package name, a dash, and then the version number. And we\
only need to specify enough of the version number for it to be unique from the\
other available versions.

However, when installing an older version of a package, if `yum` has to install dependencies, then it will automatically choose to install the latest versions of those packages. To ensure that all MariaDB packages are on the same version in this scenario, it is necessary to specify them all.

The packages that the MariaDB-server package depend on are: MariaDB-client,\
MariaDB-shared, and MariaDB-common. Therefore, to install [MariaDB 10.3.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10311-release-notes) from this `yum`\
repository, we would do the following:

```
sudo yum install MariaDB-server-10.3.11 MariaDB-client-10.3.11 MariaDB-shared-10.3.11 MariaDB-backup-10.3.11 MariaDB-common-10.3.11
```

The rest of the install and setup process is as normal.

## After Installation

After the installation is complete, you can [start MariaDB](../../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).

If you are using [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md), then keep in mind that the first node will have to be [bootstrapped](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/getting-started-with-mariadb-galera-cluster#bootstrapping-a-new-cluster).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
