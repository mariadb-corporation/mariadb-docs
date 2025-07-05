# Installing MariaDB .deb Files

## Installing MariaDB with APT

On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant `.deb` packages from MariaDB's\
repository using [apt](https://manpages.ubuntu.com/manpages/bionic/man8/apt.8.html), [aptitude](https://manpages.ubuntu.com/manpages/bionic/man8/aptitude-curses.8.html), [Ubuntu Software Center](https://help.ubuntu.com/community/UbuntuSoftwareCenter), [Synaptic Package Manager](https://help.ubuntu.com/community/SynapticHowto), or another package\
manager.

This page walks you through the simple installation steps using `apt`.

### Adding the MariaDB APT repository

We currently have APT repositories for the following Linux distributions:

* Debian 10 (Buster)
* Debian 11 (Bullseye)
* Debian 12 (Bookworm)
* Debian Unstable (Sid)
* Ubuntu 18.04 LTS (Bionic)
* Ubuntu 20.04 LTS (Focal)
* Ubuntu 22.04 (Jammy)
* Ubuntu 22.10 (Kinetic)
* Ubuntu 23.04 (Lunar)

#### Using the MariaDB Package Repository Setup Script

If you want to install MariaDB with `apt`, then you can configure `apt` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](mariadb-package-repository-setup-and-usage.md).

MariaDB Corporation provides a MariaDB Package Repository for several Linux distributions that use `apt` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md), [client libraries](../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../reference/plugins/), and [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/). The MariaDB Package Repository setup script automatically configures your system to install packages from the MariaDB Package Repository.

To use the script, execute the following command:

```
curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
```

Note that this script also configures a repository for [MariaDB MaxScale](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/maxscale/README.md) and a repository for MariaDB Tools, which currently only contains [Percona XtraBackup](../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) and its dependencies.

See [MariaDB Package Repository Setup and Usage](mariadb-package-repository-setup-and-usage.md) for more information.

#### Using the MariaDB Repository Configuration Tool

If you want to install MariaDB with `apt`, then you can configure `apt` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://mariadb.org/download/?t=repo-config).

The MariaDB Foundation provides a MariaDB repository for several Linux distributions that use `apt-get` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md), [client libraries](../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../reference/plugins/), and [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/). The MariaDB Repository Configuration Tool can easily generate the appropriate commands to add the repository for your distribution.

There are several ways to add the repository.

**Executing add-apt-repository**

One way to add an `apt` repository is by using the [add-apt-repository](https://manpages.ubuntu.com/manpages/bionic/man1/add-apt-repository.1.html) command. This command will add the repository configuration to `/etc/apt/sources.list`.

For example, if you wanted to use the repository to install [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) on Ubuntu 18.04 LTS (Bionic), then you could use the following commands to add the MariaDB `apt` repository:

```
sudo apt-get install software-properties-common
sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.6/ubuntu bionic main'
```

And then you would have to update the package cache by executing the following command:

```
sudo apt update
```

**Creating a Source List File**

Another way to add an `apt` repository is by creating a [source list](https://manpages.ubuntu.com/manpages/bionic/man5/sources.list.5.html) file in `/etc/apt/sources.list.d/`.

For example, if you wanted to use the repository to install [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) on Ubuntu 18.04 LTS (Bionic), then you could create the `MariaDB.list` file in `/etc/apt/sources.list.d/` with the following contents to add the MariaDB `apt` repository:

```
# MariaDB 10.6 repository list - created 2019-01-27 09:50 UTC
# http://downloads.mariadb.org/mariadb/repositories/
deb [arch=amd64,arm64,ppc64el] http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.6/ubuntu bionic main
deb-src http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.6/ubuntu bionic main
```

And then you would have to update the package cache by executing the following command:

```
sudo apt update
```

**Using Ubuntu Software Center**

Another way to add an `apt` repository is by using [Ubuntu Software Center](https://help.ubuntu.com/community/UbuntuSoftwareCenter).

You can do this by going to the **Software Sources** window. This window can be opened either by navigating to **Edit** > **Software Sources** or by navigating to **System** > **Administration** > **Software Sources**.

Once the **Software Sources** window is open, go to the **Other Software** tab, and click the **Add** button. At that point, you can input the repository information provided by the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).

See [here](https://help.ubuntu.com/community/UbuntuSoftwareCenter#Managing_software_sources) for more information.

**Using Synaptic Package Manager**

Another way to add an `apt` repository is by using [Synaptic Package Manager](https://help.ubuntu.com/community/SynapticHowto).

You can do this by going to the **Software Sources** window. This window can be opened either by navigating to **System** > **Administrator** > **Software Sources** or by navigating to **Settings** > **Repositories**.

Once the **Software Sources** window is open, go to the **Other Software** tab, and click the **Add** button. At that point, you can input the repository information provided by the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).

See [here](https://help.ubuntu.com/community/SynapticHowto#Managing_Repositories) for more information.

#### Pinning the MariaDB Repository to a Specific Minor Release

If you wish to pin the `apt` repository to a specific minor release, or if you would like to downgrade to a specific minor release, then you can create a `apt` repository with the URL hard-coded to that specific minor release.

The MariaDB Foundation archives repositories of old minor releases at the following URL:

*

Archives are only of the distros and architectures supported at the time of release. For example, [MariaDB 10.6.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-21-release-notes) exists for Ubuntu `bionic, focal, jammy, kinetic,` and #lunar`is obtained looking in [dists](https://archive.mariadb.org/mariadb-10.6.21/repo/ubuntu/dists).`

For example, if you wanted to pin your repository to [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1059-release-notes) on Ubuntu 20.04 LTS (Focal), then you would have to first remove any existing MariaDB repository source list file from `/etc/apt/sources.list.d/`. And then you could use the following commands to add the MariaDB `apt-get` repository:

```
sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el,s390x] http://archive.mariadb.org/mariadb-10.5.9/repo/ubuntu/ focal main main/debug'
```

Ensure you have the [signing key installed](installing-mariadb-deb-files.md#Importing_the_MariaDB_GPG_Public_Key).

Ubuntu Xenial and older will need:

```
sudo apt-get install -y apt-transport-https
```

And then you would have to update the package cache by executing the following command:

```
sudo apt update
```

### Updating the MariaDB APT repository to a New Major Release

MariaDB's `apt` repository can be updated to a new major release. How this is done depends on how you originally configured the repository.

#### Updating the Major Release with the MariaDB Package Repository Setup Script

If you configured `apt` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](mariadb-package-repository-setup-and-usage.md), then you can update the major release that the repository uses by running the script again.

#### Updating the Major Release with the MariaDB Repository Configuration Tool

If you configured `apt` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/), then you can update the major release in various ways, depending on how you originally added the repository.

**Updating a Repository with add-apt-repository**

If you added the `apt` repository by using the [add-apt-repository](https://manpages.ubuntu.com/manpages/bionic/man1/add-apt-repository.1.html) command, then you can update the major release that the repository uses by using the [add-apt-repository](https://manpages.ubuntu.com/manpages/bionic/man1/add-apt-repository.1.html) command again.

First, look for the repository string for the old version in `/etc/apt/sources.list`.

And then, you can remove the repository for the old version by executing the [add-apt-repository](https://manpages.ubuntu.com/manpages/bionic/man1/add-apt-repository.1.html) command and providing the `--remove` option. For example, if you wanted to remove a [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) repository, then you could do so by executing something like the following:

```
sudo add-apt-repository --remove 'deb [arch=amd64,arm64,ppc64el] http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.6/ubuntu bionic main'
```

After that, you can add the repository for the new version with the [add-apt-repository](https://manpages.ubuntu.com/manpages/bionic/man1/add-apt-repository.1.html) command. For example, if you wanted to use the repository to install [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106) on Ubuntu 18.04 LTS (Bionic), then you could use the following commands to add the MariaDB `apt` repository:

```
sudo apt-get install software-properties-common
sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.6/ubuntu bionic main'
```

And then you would have to update the package cache by executing the following command:

```
sudo apt update
```

After that, the repository should refer to [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106).

**Updating a Source List File**

If you added the `apt` repository by creating a [source list](https://manpages.ubuntu.com/manpages/bionic/man5/sources.list.5.html) file in `/etc/apt/sources.list.d/`, then you can update the major release that the repository uses by updating the source list file in-place. For example, if you wanted to change the repository from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105) to [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106), and if the source list file was at `/etc/apt/sources.list.d/MariaDB.list`, then you could execute the following:

```
sudo sed -i 's/10.5/10.6/' /etc/apt/sources.list.d/MariaDB.list
```

And then you would have to update the package cache by executing the following command:

```
sudo apt update
```

After that, the repository should refer to [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/what-is-mariadb-106).

### Importing the MariaDB GPG Public Key

Before MariaDB can be installed, you also have to import the GPG public key that is used to verify the digital signatures of the packages in our repositories. This allows the `apt` utility to verify the integrity of the packages that it installs.

* Prior to Debian 9 (Stretch), and Debian Unstable (Sid), and Ubuntu 16.04 LTS (Xenial), the id of our GPG public key is `0xcbcb082a1bb943db`. The full key fingerprint is:

```
1993 69E5 404B D5FC 7D2F E43B CBCB 082A 1BB9 43DB
```

The [apt-key](https://manpages.ubuntu.com/manpages/bionic/man8/apt-key.8.html) utility can be used to import this key. For example:

```
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
```

* Starting with Debian 9 (Stretch) and Ubuntu 16.04 LTS (Xenial), the id of our GPG public key is `0xF1656F24C74CD1D8`. The full key fingerprint is:

```
177F 4010 FE56 CA33 3630  0305 F165 6F24 C74C D1D8
```

The [apt-key](https://manpages.ubuntu.com/manpages/bionic/man8/apt-key.8.html) utility can be used to import this key. For example:

```
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
```

Starting with Debian 9 (Stretch), the [dirmngr](https://manpages.debian.org/stretch/dirmngr/dirmngr.8.en.html) package needs to be installed before the GPG public key can be imported. To install it, execute: `sudo apt install dirmngr`

If you are unsure which GPG public key you need, then it is perfectly safe to import both keys.

The command used to import the GPG public key is the same on both Debian and Ubuntu. For example:

```
$ sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
Executing: gpg --ignore-time-conflict --no-options --no-default-keyring --secret-keyring /tmp/tmp.ASyOPV87XC --trustdb-name /etc/apt/trustdb.gpg --keyring /etc/apt/trusted.gpg --primary-keyring /etc/apt/trusted.gpg --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
gpg: requesting key 1BB943DB from hkp server keyserver.ubuntu.com
gpg: key 1BB943DB: "MariaDB Package Signing Key <package-signing-key@mariadb.org>" imported
gpg: no ultimately trusted keys found
gpg: Total number processed: 1
gpg:               imported: 1
```

Once the GPG public key is imported, you are ready to install packages from the repository.

### Installing MariaDB Packages with APT

After the `apt` repository is configured, you can install MariaDB by executing the [apt-get](https://manpages.ubuntu.com/manpages/bionic/man8/apt-get.8.html) command. The specific command that you would use would depend on which specific packages that you want to install.

#### Installing the Most Common Packages with APT

To Install the most common packages, first you would have to update the package cache by executing the following command:

```
sudo apt update
```

To Install the most common packages, execute the following command:

```
sudo apt-get install mariadb-server galera-4 mariadb-client libmariadb3 mariadb-backup mariadb-common
```

#### Installing MariaDB Server with APT

To Install MariaDB Server, first you would have to update the package cache by executing the following command:

```
sudo apt update
```

Then, execute the following command:

```
sudo apt-get install mariadb-server
```

#### Installing MariaDB Galera Cluster with APT

The process to install MariaDB Galera Cluster with the MariaDB `apt-get` repository is practically the same as installing standard MariaDB Server.

Galera Cluster support is included in the standard MariaDB Server packages, so you will need to install the `mariadb-server` package, as you normally would.

You also need to install the `galera-4` package to obtain the [Galera](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md) 4 wsrep provider library.

To install MariaDB Galera Cluster, first you would have to update the package cache by executing the following command:

```
sudo apt update
```

To install MariaDB Galera Cluster, you could execute the following command:

```
sudo apt-get install mariadb-server mariadb-client galera-4
```

MariaDB Galera Cluster also has a separate package that can be installed on arbitrator nodes. The package is called `galera-arbitrator-4`. This package should be installed on whatever node you want to serve as the arbitrator. It can either run on a separate server that is not acting as a cluster node, which is the recommended configuration, or it can run on a server that is also acting as an existing cluster node.

To install the arbitrator package, you could execute the following command:

```
sudo apt-get install galera-arbitrator-4
```

<>

See [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md) for more information on MariaDB Galera Cluster.

#### Installing MariaDB Clients and Client Libraries with APT

[MariaDB Connector/C](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/about-mariadb-connector-c/README.md) is included as the client library.

To Install the clients and client libraries, first you would have to update the package cache by executing the following command:

```
sudo apt update
```

Then, execute the following command:

```
sudo apt-get install mariadb-client libmariadb3
```

#### Installing mariadb-backup with APT

To install [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/), first you would have to update the package cache by executing the following command:

```
sudo apt update
```

Then, execute the following command:

```
sudo apt-get install mariadb-backup
```

#### Installing Plugins with APT

Some [plugins](../../../../reference/plugins/) may also need to be installed.

For example, to install the [cracklib_password_check](../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin, first you would have to update the package cache by executing the following command:

```
sudo apt update
```

Then, execute the following command:

```
sudo apt-get install mariadb-cracklib-password-check
```

#### Installing Older Versions from the Repository

The MariaDB `apt` repository contains the last few versions of MariaDB. To show what versions are available, use the [apt-cache](https://manpages.ubuntu.com/manpages/bionic/man8/apt-cache.8.html) command:

```
sudo apt-cache showpkg mariadb-server
```

In the output you will see the available versions.

To install an older version of a package instead of the latest version we just\
need to specify the package name, an equal sign, and then the version number.

However, when installing an older version of a package, if `apt-get` has to install dependencies, then it will automatically choose to install the latest versions of those packages. To ensure that all MariaDB packages are on the same version in this scenario, it is necessary to specify them all. Therefore, to install [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103). from this `apt` repository, we would do the following:

```
sudo apt-get install mariadb-server=10.6.21-1 mariadb-client=10.6.21-1 libmariadb3=10.6.21-1 mariadb-backup=10.6.21-1 mariadb-common=10.6.21-1
```

The rest of the install and setup process is as normal.

## Installing MariaDB with dpkg

While it is not recommended, it is possible to download and install the`.deb` packages manually. However, it is generally recommended to use a package manager like `apt-get`.

A tarball that contains the `.deb` packages can be downloaded from the following URL:

* [downloads.mariadb.com](https://downloads.mariadb.com)

For example, to install the [MariaDB 10.6.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-21-release-notes) `.deb` packages on Ubuntu 18.04 LTS (Bionic), you could execute the following:

```
sudo apt-get update
sudo apt-get install libdbi-perl libdbd-mysql-perl psmisc libaio1 socat
wget https://downloads.mariadb.com/MariaDB/mariadb-10.6.21/repo/ubuntu/mariadb-10.6.21-ubuntu-bionic-amd64-debs.tar
tar -xvf mariadb-10.6.21-ubuntu-bionic-amd64-debs.tar
cd mariadb-10.6.21-ubuntu-bionic-amd64-debs/
sudo dpkg --install ./mariadb-common*.deb \
   ./mysql-common*.deb \
   ./mariadb-client*.deb \
   ./libmariadb3*.deb \
   ./libmysqlclient18*.deb 
sudo dpkg --install ./mariadb-server*.deb \
   ./mariadb-backup*.deb \
   ./galera-4*.deb
```

## After Installation

After the installation is complete, you can start MariaDB.

If you are using [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md), then keep in mind that the first node will have to be [bootstrapped](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/getting-started-with-mariadb-galera-cluster#bootstrapping-a-new-cluster).

## Available DEB Packages

The available DEB packages depend on the specific MariaDB release series.

### Available DEB Packages

For MariaDB, the following DEBs are available:

| Package Name                           | Description                                                                                                                                                                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Package Name                           | Description                                                                                                                                                                                                                                        |
| galera-4                               | The WSREP provider for [Galera](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md) 4.                                                                                                                            |
| libmariadb3                            | Dynamic client libraries.                                                                                                                                                                                                                          |
| libmariadb-dev                         | Development headers and static libraries.                                                                                                                                                                                                          |
| libmariadbclient18                     | Virtual package to satisfy external depends                                                                                                                                                                                                        |
| libmysqlclient18                       | Virtual package to satisfy external depends                                                                                                                                                                                                        |
| mariadb-backup                         | [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/)                                                                                                                                                            |
| mariadb-client                         | Client tools like [mariadb CLI](../../../../clients-and-utilities/mariadb-client/), [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md), and others.                                               |
| mariadb-client-core                    | Core client tools                                                                                                                                                                                                                                  |
| mariadb-common                         | Character set files and /etc/my.cnf                                                                                                                                                                                                                |
| mariadb-plugin-connect                 | The [CONNECT](../../../../server-usage/storage-engines/connect/) storage engine.                                                                                                                                                                   |
| mariadb-plugin-cracklib-password-check | The [cracklib\_password\_check](../../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin.                                                                                           |
| mariadb-plugin-gssapi-client           | The client-side component of the [gssapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) authentication plugin.                                                                                             |
| mariadb-plugin-gssapi-server           | The server-side component of the [gssapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) authentication plugin.                                                                                             |
| mariadb-plugin-rocksdb                 | The [MyRocks](../../../../server-usage/storage-engines/myrocks/) storage engine.                                                                                                                                                                   |
| mariadb-plugin-spider                  | The [SPIDER](../../../../server-usage/storage-engines/spider/) storage engine.                                                                                                                                                                     |
| mariadb-plugin-tokudb                  | The [TokuDB](../../../../server-usage/storage-engines/tokudb/) storage engine.                                                                                                                                                                     |
| mariadb-server                         | The server and server tools, like [myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) and [mariadb-hotcopy](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-hotcopy.md) are here. |
| mariadb-server-core                    | The core server.                                                                                                                                                                                                                                   |
| mariadb-test                           | mysql-client-test executable, and mysql-test framework with the tests.                                                                                                                                                                             |
| mariadb-test-data                      | MariaDB database regression test suite - data files                                                                                                                                                                                                |

<>

## Actions Performed by DEB Packages

### Users and Groups Created

When the `mariadb-server` DEB package is installed, it will create a user and group named `mysql`, if they do not already exist.

## See Also

* [Differences in MariaDB in Debian](../troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md)
* [Installing MariaDB .deb Files with Ansible](automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
