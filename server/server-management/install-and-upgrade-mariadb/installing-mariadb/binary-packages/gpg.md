# GPG

The MariaDB project signs their MariaDB packages for Debian, Ubuntu, Fedora, and Red Hat. This page documents information about the keys that we use and have used.

## MariaDB Community Server Debian / Ubuntu key

Our MariaDB Community Server repositories for Debian "Sid" and the Ubuntu 16.04 and beyond "Xenial" use the following GPG signing key. As detailed in [MDEV-9781](https://jira.mariadb.org/browse/MDEV-9781), APT 1.2.7 (and later) prefers SHA2 GPG keys and now prints warnings when a repository is signed using a SHA1 key like our previous GPG key. We have created a SHA2 key for use with these.

Information about this key:

* The short Key ID is: `0xC74CD1D8`
* The long Key ID is: `0xF1656F24C74CD1D8`
* The full fingerprint of the key is: `177F 4010 FE56 CA33 3630 0305 F165 6F24 C74C D1D8`
* The key can be added on Debian-based systems using the following command:

```bash
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
```

* Usage of the `apt-key` command is deprecated in the latest versions of Debian and Ubuntu, and the replacement method is to download the keyring file to the `/etc/apt/trusted.gpg.d/` directory. This can be done with the following:

```bash
sudo curl -LsSo /etc/apt/trusted.gpg.d/mariadb-keyring-2019.gpg https://supplychain.mariadb.com/mariadb-keyring-2019.gpg
```

## MariaDB Community Server RPM / Source Keys

{% tabs %}
{% tab title="2023+" %}
Beginning in 2023 we migrated the key used to sign our `yum/dnf/zypper` repositories and to sign our source code and binary tarballs to the same key we use for Debian and Ubuntu.

Key ID and Fingerprint information is in the [MariaDB Community Server Debian/Ubuntu Key section](gpg.md#mariadb-community-server-debian-ubuntu-key), above.

The key can be imported on RPM-based systems using the following command:

```bash
sudo rpm --import https://supplychain.mariadb.com/MariaDB-Server-GPG-KEY
```

or

```bash
sudo rpmkeys --import https://supplychain.mariadb.com/MariaDB-Server-GPG-KEY
```
{% endtab %}

{% tab title="Pre-2023" %}
The GPG Key ID of the MariaDB signing key we used for `yum/dnf/zypper` repositories and to sign our source code tarballs until the end of 2022 was `0xCBCB082A1BB943DB`. The short form of the id is `0x1BB943DB` and the full key fingerprint is:

```bash
1993 69E5 404B D5FC 7D2F E43B CBCB 082A 1BB9 43DB
```

This key was used by the `yum/dnf/zypper` repositories for RedHat, CentOS, Fedora, openSUSE, and SLES.

If you configure the mariadb.org rpm repositories using the repository configuration tool then your package manager will prompt you to import the key the first time you install a package from the repository.

You can also import the key directly using the following command:

```bash
sudo rpmkeys --import https://supplychain.mariadb.com/MariaDB-Server-GPG-KEY-2010
```
{% endtab %}
{% endtabs %}

## MariaDB Enterprise GPG Keys

{% tabs %}
{% tab title="RHEL 7/8/9, Debian, Ubuntu" %}
Information about the key we use on most platforms for MariaDB Enterprise Server releases:

* The short Key ID is: `0xE3C94F49`
* The long Key ID is: `0xCE1A3DD5E3C94F49`
* The full fingerprint of the key is: `4C47 0FFF EFC4 D3DC 5977 8655 CE1A 3DD5 E3C9 4F49`&#x20;

The key can be added on Debian-based systems using the following command:

```bash
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xCE1A3DD5E3C94F49
```

* Usage of the `apt-key` command is deprecated in the latest versions of Debian and Ubuntu, and the replacement method is to download the keyring file to the `/etc/apt/trusted.gpg.d/` directory. This can be done with the following:

```bash
sudo curl -LsSo /etc/apt/trusted.gpg.d/mariadb-keyring-2019.gpg https://supplychain.mariadb.com/mariadb-keyring-2019.gpg
```

The key can be imported on RPM-based systems using the following command:

```bash
sudo rpm --import https://supplychain.mariadb.com/MariaDB-Enterprise-GPG-KEY
```

or

```bash
sudo rpmkeys --import https://supplychain.mariadb.com/MariaDB-Enterprise-GPG-KEY
```
{% endtab %}

{% tab title="RHEL 10+" %}
For RHEL, AlmaLinux, Rocky, and Oracle Linux 10 and above, there are new requirements around GPG keys used to sign rpm packages. For these distributions we have created a different GPG key for our Enterprise Server releases for these distributions.

Information on this key:

* The short Key ID is: `0x8C27D14E`
* The long Key ID is: `0x5D87FACA8C27D14E`
* The full fingerprint of the key is: `BB2A 36F3 6C3B 4D37 3BAC 328A 5D87 FACA 8C27 D14E`

The key can be imported on RPM-based systems using the following command:

```bash
sudo rpm --import https://supplychain.mariadb.com/MariaDB-Enterprise-GPG-KEY-2025
```

or

```bash
sudo rpmkeys --import https://supplychain.mariadb.com/MariaDB-Enterprise-GPG-KEY-2025
```
{% endtab %}
{% endtabs %}



## Configuring Repositories

See the [this page](mariadb-package-repository-setup-and-usage.md) for details on using the `mariadb_repo_setup`  and `mariadb_es_repo_setup` scripts to configure repositories that use these keys.

See the [details](https://downloads.mariadb.org/mariadb/repositories/) on configuring MariaDB Foundation repositories that use these keys.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
