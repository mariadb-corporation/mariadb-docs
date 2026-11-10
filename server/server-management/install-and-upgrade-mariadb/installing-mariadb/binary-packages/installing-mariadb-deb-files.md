---
description: >-
  Complete .deb installation guide: add repo via mariadb_repo_setup, import GPG
  keys, apt install mariadb-server galera-4, and APT configuration.
---

# Installing MariaDB .deb Files

## Installing MariaDB with APT

On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant `.deb` packages from MariaDB's repository using [apt](https://manpages.ubuntu.com/manpages/noble/man8/apt.8.html), [aptitude](https://manpages.ubuntu.com/manpages/noble/man8/aptitude-curses.8.html), or another package manager.

This page walks you through the simple installation steps using `apt`.

### Adding the MariaDB APT repository

MariaDB provides APT repositories for the following Linux distributions:

* Debian 11 (Bullseye)
* Debian 12 (Bookworm)
* Debian 13 (Trixie)
* Debian Unstable (Sid)
* Ubuntu 22.04 (Jammy)
* Ubuntu 24.04 (Noble)

#### Using the MariaDB Package Repository Setup Script

If you want to install MariaDB with `apt`, then you can configure `apt` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../mariadb-package-repository-setup-and-usage.md).

MariaDB Corporation provides a MariaDB Package Repository for several Linux distributions that use `apt` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](../../../../clients-and-utilities/), [client libraries](../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../reference/plugins/), and [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md). The MariaDB Package Repository setup script automatically configures your system to install packages from the MariaDB Package Repository.

To use the script, execute the following command:

```bash
curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
```

Note that this script also configures a repository for MariaDB MaxScale and a repository for MariaDB Tools, which only contains [Percona XtraBackup](../../../../server-usage/backup-and-restore/mariadb-backup/README.md) and its dependencies.

See [MariaDB Package Repository Setup and Usage](../../mariadb-package-repository-setup-and-usage.md) for more information.

#### Using the MariaDB Repository Configuration Tool

If you want to install MariaDB with `apt`, then you can configure `apt` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://mariadb.org/download/?t=repo-config).

The MariaDB Foundation provides a MariaDB repository for several Linux distributions that use `apt-get` to manage packages. This repository contains software packages related to MariaDB Server, including the server itself, [clients and utilities](../../../../clients-and-utilities/README.md), [client libraries](../../../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../../../reference/plugins/), and [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/README.md). The MariaDB Repository Configuration Tool can easily generate the appropriate commands to add the repository for your distribution.

There are several ways to add the repository. Whichever you choose, first download the signing key to a keyring file, so that `apt` can verify the packages:

```bash
sudo apt-get install curl
sudo mkdir -p /etc/apt/keyrings
sudo curl -o /etc/apt/keyrings/mariadb-keyring.pgp 'https://mariadb.org/mariadb_release_signing_key.pgp'
```

The repository examples below refer to this file with `signed-by`. See [GPG](gpg.md) for the key's fingerprint.

**Executing add-apt-repository**

One way to add an `apt` repository is by using the [add-apt-repository](https://manpages.ubuntu.com/manpages/noble/man1/add-apt-repository.1.html) command, which writes the repository line to a source list file in `/etc/apt/sources.list.d/`.

For example, if you wanted to use the repository to install [MariaDB 11.8]({release-notes}/community-server/11.8/what-is-mariadb-118) on Ubuntu 24.04 LTS (Noble), then you could use the following commands to add the MariaDB `apt` repository:

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository 'deb [signed-by=/etc/apt/keyrings/mariadb-keyring.pgp] https://deb.mariadb.org/11.8/ubuntu noble main'
```

And then you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

**Creating a Source List File**

Another way to add an `apt` repository is by creating a [source list](https://manpages.ubuntu.com/manpages/noble/man5/sources.list.5.html) file in `/etc/apt/sources.list.d/`. The MariaDB Repository Configuration Tool generates a file in the Deb822 format, which current Debian and Ubuntu releases support.

For example, if you wanted to use the repository to install [MariaDB 11.8]({release-notes}/community-server/11.8/what-is-mariadb-118) on Ubuntu 24.04 LTS (Noble), then you could create the `mariadb.sources` file in `/etc/apt/sources.list.d/` with the following contents to add the MariaDB `apt` repository:

```
# MariaDB 11.8 repository list
# https://mariadb.org/download/?t=repo-config
X-Repolib-Name: MariaDB
Types: deb
URIs: https://deb.mariadb.org/11.8/ubuntu
Suites: noble
Components: main
Signed-By: /etc/apt/keyrings/mariadb-keyring.pgp
```

`deb.mariadb.org` redirects requests to a MariaDB mirror. To use a specific mirror instead, put the mirror URL that the MariaDB Repository Configuration Tool shows in `URIs`.

And then you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

#### Pinning the MariaDB Repository to the repository of a Specific Minor Release

If you wish to pin the `apt` repository to a specific minor release, or if you would like to downgrade to a specific minor release, then you can create an `apt` repository with the URL hard-coded to that specific minor release.

{% tabs %}
{% tab title="MariaDB Corporation repo setup scripts" %}
If you used [MariaDB Corporation's `mariadb_repo_setup` or `mariadb_es_repo_setup` scripts](../../mariadb-package-repository-setup-and-usage.md) to generate your repository configuration, simply re-run the script and specify the full version number to use with the `--mariadb-server-version` option.

See [Pinning the Repository to a Specific Minor Release](../../mariadb-package-repository-setup-and-usage.md#pinning-the-repository-to-a-specific-minor-release) on the [MariaDB Package Repository Setup and Usage](../../mariadb-package-repository-setup-and-usage.md) page for details.

The full list of MariaDB Enterprise Server releases can be found on the [Enterprise Server - All Releases](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/all-releases) page.
{% endtab %}

{% tab title="MariaDB Foundation repo config tool" %}
If you used the [MariaDB Foundation's Repository Configuration tool](https://mariadb.org/download/?t=repo-config), then you need to update the repository file you created to include the full version number. By default the Foundation's tool configures repositories with just the main series of MariaDB, e.g. `mariadb-11.8`, and to pin to a specific version you need to specify the full version, for example `mariadb-11.8.6`. The full list of MariaDB Community Server releases can be found on the [Community Server - All Releases](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/all-releases) page.

Archives are only of the distros and architectures supported at the time of release. For example, MariaDB Community Server 11.8.9 exists for Ubuntu `jammy`, `noble`, and `resolute`. To see which distributions are available for a release, look in the `dists` folder of its [Debian](https://archive.mariadb.org/mariadb-11.8.9/repo/debian/dists/) or [Ubuntu](https://archive.mariadb.org/mariadb-11.8.9/repo/ubuntu/dists/) repository.

For example, if you wanted to pin your repository to MariaDB Community Server 11.8.9 on Ubuntu 24.04 LTS (Noble), then you would have to first remove any existing MariaDB repository source list file from `/etc/apt/sources.list.d/`. And then you could use the following command to add the MariaDB `apt` repository:

```bash
sudo add-apt-repository 'deb [signed-by=/etc/apt/keyrings/mariadb-keyring.pgp] https://archive.mariadb.org/mariadb-11.8.9/repo/ubuntu/ noble main main/debug'
```

Ensure you have the [signing key installed](installing-mariadb-deb-files.md#importing-the-mariadb-gpg-public-key).

And then you would have to update the package cache by executing the following command:

```bash
sudo apt update
```
{% endtab %}
{% endtabs %}

### Updating the MariaDB APT repository to a New Major Release

MariaDB's `apt` repository can be updated to a new major release. How this is done depends on how you originally configured the repository.

#### Updating the Major Release with the MariaDB Package Repository Setup Script

If you configured `apt` to install from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](../../mariadb-package-repository-setup-and-usage.md), then you can update the major release that the repository uses by running the script again.

#### Updating the Major Release with the MariaDB Foundation's Repository Configuration Tool

If you configured `apt` to install from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://mariadb.org/download/?t=repo-config), then you can update the major release in various ways, depending on how you originally added the repository.

**Updating a Repository with add-apt-repository**

If you added the `apt` repository by using the [add-apt-repository](https://manpages.ubuntu.com/manpages/noble/man1/add-apt-repository.1.html) command, then you can update the major release that the repository uses by using the [add-apt-repository](https://manpages.ubuntu.com/manpages/noble/man1/add-apt-repository.1.html) command again.

First, look for the repository line for the old version in the files in `/etc/apt/sources.list.d/` (or, on older systems, in `/etc/apt/sources.list`).

And then, you can remove the repository for the old version by executing the [add-apt-repository](https://manpages.ubuntu.com/manpages/noble/man1/add-apt-repository.1.html) command and providing the `--remove` option. For example, if you wanted to remove a MariaDB 11.4 repository, then you could do so by executing something like the following:

```bash
sudo add-apt-repository --remove 'deb [signed-by=/etc/apt/keyrings/mariadb-keyring.pgp] https://deb.mariadb.org/11.4/ubuntu noble main'
```

After that, you can add the repository for the new version with the [add-apt-repository](https://manpages.ubuntu.com/manpages/noble/man1/add-apt-repository.1.html) command. For example, if you wanted to use the repository to install [MariaDB 11.8]({release-notes}/community-server/11.8/what-is-mariadb-118) on Ubuntu 24.04 LTS (Noble), then you could use the following commands to add the MariaDB `apt` repository:

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository 'deb [signed-by=/etc/apt/keyrings/mariadb-keyring.pgp] https://deb.mariadb.org/11.8/ubuntu noble main'
```

And then you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

After that, the repository should refer to [MariaDB 11.8]({release-notes}/community-server/11.8/what-is-mariadb-118) and you can [upgrade to the new version of MariaDB](installing-mariadb-deb-files.md#upgrading-to-a-new-version-of-mariadb).

**Updating a Source List File**

If you added the `apt` repository by creating a [source list](https://manpages.ubuntu.com/manpages/noble/man5/sources.list.5.html) file in `/etc/apt/sources.list.d/`, then you can update the major release that the repository uses by updating the source list file in-place. For example, if you wanted to change the repository from MariaDB 11.4 to [MariaDB 11.8]({release-notes}/community-server/11.8/what-is-mariadb-118), and if the source list file was at `/etc/apt/sources.list.d/mariadb.sources`, then you could execute the following:

```bash
sudo sed -i 's/11\.4/11.8/g' /etc/apt/sources.list.d/mariadb.sources
```

And then you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

After that, the repository should refer to MariaDB 11.8 and you can [upgrade to the new version of MariaDB](installing-mariadb-deb-files.md#upgrading-to-a-new-version-of-mariadb).

### Importing the MariaDB GPG Public Key

Before MariaDB can be installed, you also have to import the GPG public key that is used to verify the digital signatures of the packages in our repositories. This allows the `apt` utility to verify the integrity of the packages that it installs.

For **MariaDB Community Server**, see the [MariaDB Community Server Debian / Ubuntu key](gpg.md#mariadb-community-server-debian-ubuntu-key) section of the [GPG](gpg.md) page for details on how to import the key used by those repositories on your Debian or Ubuntu system.

For **MariaDB Enterprise Server**, see the [MariaDB Enterprise GPG Keys](gpg.md#mariadb-enterprise-gpg-keys) section of the [GPG](gpg.md) page for details on how to import the key used by those repositories on your Debian or Ubuntu system.

{% hint style="info" %}
If you import the key from a keyserver (for example, with `gpg --recv-keys`), the [dirmngr](https://manpages.debian.org/trixie/dirmngr/dirmngr.8.en.html) package must be installed first. To install it, execute: `sudo apt install dirmngr`. Downloading the keyring file with `curl`, as shown above, doesn't need it.
{% endhint %}

Once the GPG public key is imported, you are ready to install packages from the repository.

### Installing MariaDB Packages with APT

After the `apt` repository is configured, you can install MariaDB by executing the [apt-get](https://manpages.ubuntu.com/manpages/noble/man8/apt-get.8.html) command. The specific command that you would use would depend on which specific packages that you want to install.

#### Installing the Most Common Packages with APT

To Install the most common packages, first you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

To Install the most common packages, execute the following command:

```bash
sudo apt-get install mariadb-server mariadb-server-galera galera-4 mariadb-client libmariadb3 mariadb-backup mariadb-common
```

#### Installing MariaDB Server with APT

To Install MariaDB Server, first you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

Then, execute the following command:

```bash
sudo apt-get install mariadb-server
```

#### Installing MariaDB Galera Cluster with APT

The process to install MariaDB Galera Cluster with the MariaDB `apt-get` repository is practically the same as installing standard MariaDB Server.

Galera Cluster support is included in the standard MariaDB Server packages, so you will need to install the `mariadb-server` package, as you normally would.

You also need to install the `galera-4` package to obtain the [Galera](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/mariadb-galera-cluster-usage-guide) 4 wsrep provider library.

To install MariaDB Galera Cluster, first you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

To install MariaDB Galera Cluster, you could execute the following command:

```bash
sudo apt-get install mariadb-server mariadb-client galera-4
```

MariaDB Galera Cluster also has a separate package that can be installed on arbitrator nodes. The package is called `galera-arbitrator-4`. This package should be installed on whatever node you want to serve as the arbitrator. It can either run on a separate server that is not acting as a cluster node, which is the recommended configuration, or it can run on a server that is also acting as an existing cluster node.

To install the arbitrator package, you could execute the following command:

```bash
sudo apt install galera-arbitrator-4
```

See [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) for more information on MariaDB Galera Cluster.

#### Installing MariaDB Clients and Client Libraries with APT

MariaDB Connector/C is included as the client library.

To Install the clients and client libraries, first you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

Then, execute the following command:

```bash
sudo apt-get install mariadb-client libmariadb3
```

#### Installing mariadb-backup with APT

To install [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md), first you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

Then, execute the following command:

```bash
sudo apt-get install mariadb-backup
```

#### Installing Plugins with APT

Some [plugins](../../../../reference/plugins/) may also need to be installed.

For example, to install the [cracklib\_password\_check](../../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin, first you would have to update the package cache by executing the following command:

```bash
sudo apt update
```

Then, execute the following command:

```bash
sudo apt-get install mariadb-cracklib-password-check
```

### Installing Older Versions from the Repository

The MariaDB `apt` repository contains the last few versions of MariaDB. To show what versions are available, use the [apt-cache](https://manpages.ubuntu.com/manpages/noble/man8/apt-cache.8.html) command:

```bash
sudo apt-cache showpkg mariadb-server
```

There will be a lot of output, but in the "Provides" section at the end of the output you will see the available versions. For example:

```
Package: mariadb-server
Versions: 
1:12.1.2+maria~ubu2404 (/var/lib/apt/lists/dlm.mariadb.com_repo_mariadb-server_12.rolling_repo_ubuntu_dists_noble_main_binary-amd64_Packages)
 Description Language:
 ...<extra-output-snipped>...
 Provides: 
1:12.1.2+maria~ubu2404 - virtual-mysql-server (= ) default-mysql-server (= ) 
1:12.0.2+maria~ubu2404 - virtual-mysql-server (= ) default-mysql-server (= ) 
1:10.11.13-0ubuntu0.24.04.1 - virtual-mysql-server (= ) 
1:10.11.7-2ubuntu2 - virtual-mysql-server (= ) 
```

In the above example there are four versions available, two from the MariaDB repositories, and two from the Ubuntu repositories. The versions from MariaDB have "maria" in the version number, and the versions from Ubuntu have "ubuntu" in the version number.

To install an older version of a package instead of the latest version we just need to specify the package name, an equal sign, and then the complete version number. From the example above, the complete version number for MariaDB 12.0.2 is: `1:12.0.2+maria~ubu2404`

However, when installing an older version of a package, `apt` will automatically choose to install the latest versions of any dependencies, which doesn't work for dependencies of the `mariadb-server` package like `mariadb-client` and `mariadb-server-core`.

<pre class="language-bash"><code class="lang-bash"><strong>sudo apt install mariadb-server=1:12.0.2+maria~ubu2404
</strong></code></pre>

```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 mariadb-client : Breaks: mariadb-server (< 1:12.1.2+maria~ubu2404) but 1:12.0.2+maria~ubu2404 is to be installed
 mariadb-server-core : Breaks: mariadb-server (< 1:12.1.2+maria~ubu2404) but 1:12.0.2+maria~ubu2404 is to be installed
E: Unable to correct problems, you have held broken packages.
```

To ensure that all MariaDB packages are on the same version in this scenario, it is necessary to specify them all. Therefore, to install the 12.0.2 version of the `mariadb-server` package from this `apt` repository, we would do the following (using a variable to hold the version number, and putting each package on its own line so things are cleaner):

```bash
ver="1:12.0.2+maria~ubu2404"
sudo apt install \
  mariadb-server=${ver} \
  mariadb-client=${ver} \
  mariadb-server-core=${ver} \
  mariadb-client-core=${ver}
```

For MariaDB Enterprise, version numbers are similar, but have an extra point. For example, MariaDB Enterprise Server 11.8.5-2 for Ubuntu 24.04 Noble has the version number: `1:11.8.5.2+maria~ubu2404` .

The rest of the install and setup process is as normal.

## Installing MariaDB with dpkg

While it is not recommended, it is possible to download and install the`.deb` packages manually. However, it is generally recommended to use a package manager like `apt-get`.

A tarball that contains the `.deb` packages can be downloaded from the [MariaDB downloads page](https://mariadb.com/downloads/community/community-server/). Choose the version, your distribution, and the DEB package type, then copy the download link.

For example, to install the [MariaDB 11.8.9]({release-notes}/community-server/11.8/11.8.9) `.deb` packages on Ubuntu 24.04 LTS (Noble), you could execute the following, with `<download-url>` replaced by the link you copied:

```bash
sudo apt-get update
sudo apt-get install libdbi-perl libconfig-inifiles-perl psmisc socat rsync lsof gawk libaio1t64 liburing2
wget -O mariadb-11.8.9-ubuntu-noble-amd64-debs.tar '<download-url>'
tar -xvf mariadb-11.8.9-ubuntu-noble-amd64-debs.tar
cd mariadb-11.8.9-ubuntu-noble-amd64-debs/
sudo dpkg --install ./mariadb-common*.deb \
   ./mysql-common*.deb \
   ./mariadb-client*.deb \
   ./libmariadb3*.deb \
   ./libmysqlclient18*.deb 
sudo dpkg --install ./mariadb-server*.deb \
   ./mariadb-backup*.deb \
   ./galera-4*.deb
```

If `dpkg` reports missing dependencies, install them with `sudo apt-get install -f`, which also completes the configuration of the MariaDB packages.

## After Installation

After the installation is complete, you can start MariaDB.

If you are using [MariaDB Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/mariadb-galera-cluster-usage-guide), then keep in mind that the first node will have to be [bootstrapped](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster#bootstrapping-a-new-cluster).

## Upgrading to a new version of MariaDB

After updating your repository configuration to move from the repository of one version of MariaDB to a newer version, as per the previous instructions, you will need to upgrade the MariaDB packages, this is done with:

```bash
sudo apt upgrade mariadb-server
```

Alternatively you can also run the following to installing the new version:

```bash
sudo apt install mariadb-server galera-4
```

The reason for specifying the `galera-4` package is to ensure the correct updated version of Galera is installed along with the new server version, replacing the versions that were there before.

## Available DEB Packages

The available DEB packages depend on the specific MariaDB release series.

### Available DEB Packages

For MariaDB, the following DEBs are available:

| Package Name                             | Description                                                                                                                                                                                                                                        |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `galera-4`                               | The WSREP provider for [Galera](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/mariadb-galera-cluster-usage-guide) 4.                                                                                                                       |
| `libmariadb3`                            | Dynamic client libraries.                                                                                                                                                                                                                          |
| `libmariadb-dev`                         | Development headers and static libraries.                                                                                                                                                                                                          |
| `libmariadbclient18`                     | Virtual package to satisfy external depends                                                                                                                                                                                                        |
| `libmysqlclient18`                       | Virtual package to satisfy external depends                                                                                                                                                                                                        |
| `mariadb-backup`                         | [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md)                                                                                                                                            |
| `mariadb-client`                         | Client tools like [mariadb CLI](../../../../clients-and-utilities/mariadb-client/), [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md), and others.                                               |
| `mariadb-client-core`                    | Core client tools                                                                                                                                                                                                                                  |
| `mariadb-common`                         | Character set files and /etc/my.cnf                                                                                                                                                                                                                |
| `mariadb-plugin-connect`                 | The [CONNECT](../../../../server-usage/storage-engines/connect/) storage engine.                                                                                                                                                                   |
| `mariadb-plugin-cracklib-password-check` | The [cracklib\_password\_check](../../../../reference/plugins/password-validation-plugins/cracklib-password-check-plugin.md) password validation plugin.                                                                                           |
| `mariadb-plugin-gssapi-client`           | The client-side component of the [gssapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) authentication plugin.                                                                                             |
| `mariadb-plugin-gssapi-server`           | The server-side component of the [gssapi](../../../../reference/plugins/authentication-plugins/authentication-plugin-gssapi.md) authentication plugin.                                                                                             |
| `mariadb-plugin-rocksdb`                 | The [MyRocks](../../../../server-usage/storage-engines/myrocks/) storage engine.                                                                                                                                                                   |
| `mariadb-plugin-spider`                  | The [SPIDER](../../../../server-usage/storage-engines/spider/) storage engine.                                                                                                                                                                     |
| `mariadb-server`                         | The server and server tools, like [myisamchk](../../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) and [mariadb-hotcopy](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-hotcopy.md) are here. |
| `mariadb-server-galera`                  | Required for MariaDB Cluster (Galera) functionality. Includes cluster-specific scripts, systemd bootstrap logic, and the `wsrep_info` plugin.                                                                                                      |
| `mariadb-server-core`                    | The core server.                                                                                                                                                                                                                                   |
| `mariadb-test`                           | mysql-client-test executable, and mysql-test framework with the tests.                                                                                                                                                                             |
| `mariadb-test-data`                      | MariaDB database regression test suite - data files                                                                                                                                                                                                |

## Actions Performed by DEB Packages

### Users and Groups Created

When the `mariadb-server` DEB package is installed, it will create a user and group named `mysql`, if they do not already exist.

## See Also

* [Differences in MariaDB in Debian](../troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md)
* [Installing MariaDB .deb Files with Ansible](../../../automated-mariadb-deployment-and-administration/ansible-and-mariadb/installing-mariadb-deb-files-with-ansible.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
