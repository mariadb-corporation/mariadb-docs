---
description: >-
  Complete guide to MariaDB package repositories. Complete setup instructions
  for APT, YUM, Zypper with GPG keys and configurations for production use.
---

# MariaDB Package Repository Setup and Usage

## Overview

If you are looking to set up MariaDB Server, it is often easiest to use a repository. MariaDB Corporation provides two convenient shell scripts to configure access to their MariaDB Package Repositories:

* `mariadb_es_repo_setup` for MariaDB Enterprise Server, which can be downloaded from:
  * [https://dlm.mariadb.com/enterprise-release-helpers/mariadb\_es\_repo\_setup](https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup)
* `mariadb_repo_setup` for MariaDB Community Server, which can be downloaded from:
  * [https://r.mariadb.com/downloads/mariadb\_repo\_setup](https://r.mariadb.com/downloads/mariadb_repo_setup)

{% hint style="info" %}
### Using the MariaDB Foundation's Repository Configuration Tool

Another option for MariaDB Community Server is to use the MariaDB Foundation's repository configuration tool. Visit [https://mariadb.org/download/?t=repo-config](https://mariadb.org/download/?t=repo-config) and follow the instructions from there. It will ask for your Linux distribution, desired MariaDB version, and the mirror to use, and will show what files to edit and what commands to run to configure a Community Server repository.
{% endhint %}

## Using MariaDB Corporation's Repository Setup Scripts

MariaDB Corporation provides two convenient shell scripts that will automatically configure the appropriate repositories for you. These scripts are:

* `mariadb_es_repo_setup` for MariaDB Enterprise Server
* `mariadb_repo_setup` for MariaDB Community Server

### Download and Verify the Script

The scripts can be downloaded and verified in the following ways:

{% tabs %}
{% tab title="mariadb_es_repo_setup" %}
Download the script:

```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
```

Verify the checksum of the script:

```bash
echo "${checksum} mariadb_es_repo_setup" | sha256sum -c -
```
{% endtab %}

{% tab title="mariadb_repo_setup" %}
Download the script:

```bash
curl -LsSO https://r.mariadb.com/downloads/mariadb_repo_setup
```

Verify the checksum of the script:

```bash
echo "${checksum} mariadb_repo_setup" | sha256sum -c -
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Checksums of the various releases of the MariaDB Corporation's repository setup scripts can be found in the [Versions](mariadb-package-repository-setup-and-usage.md#versions) section at the bottom of this page. Substitute `${checksum}` in the example above with the checksum of the version of the script you are using.

The version number is a date and can be found by running the script with the `--version` option, or by opening the script in a text editor and looking at line 4, `version="..."`.
{% endhint %}

### Prerequisites

For the scripts to work, the `curl` package needs to be installed on your system. Additionally, on Debian and Ubuntu, the `apt-transport-https` package needs to be installed. The script will check if these are installed and let you know before it attempts to create the repository configuration on your system.

They can be installed on your system as follows:

{% tabs %}
{% tab title="RHEL / Rocky / Alma" %}
```bash
sudo dnf install curl
```
{% endtab %}

{% tab title="Debian / Ubuntu" %}
```bash
sudo apt update
sudo apt install curl apt-transport-https
```
{% endtab %}

{% tab title="SLES" %}
```bash
sudo zypper install curl
```
{% endtab %}
{% endtabs %}

### Run the Script

After the script you are using is downloaded, you need to run it with `root` user permissions. This is normally accomplished by using the `sudo` command:

{% tabs %}
{% tab title="mariadb_es_repo_setup" %}
Retrieve your customer downloads token:

1. Navigate to [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and log in
2. Copy the Customer Download Token
3. Substitute your token for `${token}` when running the `mariadb_es_repo_setup` script, below
4. Set the script to be executable:

```bash
chmod +x mariadb_es_repo_setup
```

5. Run the script:

```bash
sudo ./mariadb_es_repo_setup --token="${token}" --apply
```
{% endtab %}

{% tab title="mariadb_repo_setup" %}
1. Set the script to be executable:

```bash
chmod +x mariadb_repo_setup
```

2. Run the script:

```bash
sudo ./mariadb_repo_setup
```
{% endtab %}
{% endtabs %}

## Repositories

The script will set up different repositories in a single [repository configuration file](mariadb-package-repository-setup-and-usage.md#platform-specific-behavior).

{% tabs %}
{% tab title="mariadb_es_repo_setup default repositories" %}
The default repositories set up by `mariadb_es_repo_setup` are:

* MariaDB Enterprise Server Repository
  * Debug packages via the `main/debug` component _(Ubuntu only)_
* MariaDB Enterprise MaxScale Repository
* MariaDB Enterprise Tools Repository
{% endtab %}

{% tab title="mariadb_repo_setup default repositories" %}
The default repositories set up by `mariadb_repo_setup` are:

* MariaDB Community Server Repository
  * Debug packages via the `main/debug` component _(Ubuntu only)_
* MariaDB MaxScale Repository
{% endtab %}
{% endtabs %}

{% hint style="info" %}
On Ubuntu, MariaDB Server debug packages are provided through an additional `main/debug` component in the MariaDB Server repository configuration, which the script enables automatically. Other Linux distributions include the debug packages in the main repository. Debug packages should normally only be installed for specific purposes under the direction of a qualified support engineer.
{% endhint %}

{% hint style="info" %}
The **Tools** repository is no longer configured by default. If you need it, run the script with the `--include-tools` option.
{% endhint %}

### MariaDB Community Server Repository

The **MariaDB Community Server** repository contains software packages related to MariaDB Community Server, including: the server itself, [clients and utilities](../../clients-and-utilities/), [client libraries](../../clients-and-utilities/server-client-software/client-libraries/), [plugins](../../reference/plugins/), and [mariadb-backup](../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md).

{% hint style="info" %}
The binaries in MariaDB Corporation's **MariaDB Community Server Repository** are identical to the binaries in the MariaDB Foundation's MariaDB Repository that is configured with the [MariaDB Foundation's Repository Configuration Tool](https://mariadb.org/download/?t=repo-config).
{% endhint %}

By default, the mariadb_repo_setup script will configure the repository of the latest stable version of MariaDB Community Server.

If you would like to stick to a specific release series, see [--mariadb-server-version](mariadb-package-repository-setup-and-usage.md#mariadb-server-version), below.

If you do not want to configure the **MariaDB Repository** on your system, for example, if you are setting up a server just running MariaDB MaxScale, then you can use the `--skip-server` option to prevent the script from configuring the server repository.

#### Output an example MariaDB Server repository configuration

To output just the MariaDB repository configuration to standard output (stdout), do the following:

{% tabs %}
{% tab title="Output an example Enterprise Server repo" %}
To display an example MariaDB Enterprise Server repository configuration, you can run the `mariadb_es_repo_setup` script with the following options:

```bash
./mariadb_es_repo_setup --token=$token --skip-check-installed --skip-enterprise-tools --skip-tools --skip-maxscale --verbose
```

{% hint style="info" %}
For more verbose output, use the `--verbose` option (`mariadb_es_repo_setup` only)
{% endhint %}
{% endtab %}

{% tab title="Output an example Community Server repo" %}
To display an example MariaDB Community Server repository configuration, you can run the `mariadb_repo_setup` script with the following options:

```bash
./mariadb_repo_setup --skip-check-installed --skip-tools --skip-maxscale --write-to-stdout
```
{% endtab %}
{% endtabs %}

You may also want to use the `--os-type`, `--os-version`, and `--arch` options if you are running the script on a machine running a different operating system and/or processor architecture than the machine the configuration will be used on. If you want to specify a specific MariaDB version or series, then also use the `--mariadb-server-version` option.

Descriptions for all of these options are found in the [Options](mariadb-package-repository-setup-and-usage.md#options) section, below.

### MariaDB MaxScale Repository

{% hint style="warning" %}
**Note**

MaxScale releases, as of 2025-12-09, are now signed with a new key. The `mariadb_repo_setup` and `mariadb_es_repo_setup` scripts have been updated to automatically install the new key, but for existing repositories, you'll need to do the following.

On Debian and Ubuntu:

```
curl -LsSO https://supplychain.mariadb.com/mariadb-keyring-2025.gpg
sudo mv mariadb-keyring-2025.gpg /etc/apt/trusted.gpg.d/
sudo apt update
```

On RHEL & friends:

```
sudo rpm --import https://supplychain.mariadb.com/MariaDB-Enterprise-GPG-KEY-2025
```
{% endhint %}

The **MariaDB MaxScale Repository** contains software packages related to [MariaDB MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/).

By default, the script will configure your system to install from the repository of the _latest_ GA version of MariaDB MaxScale. When a new major GA release occurs, the repository will automatically switch to the new version. If instead you would like to stay on a particular version, you will need to manually edit the [repository configuration file](mariadb-package-repository-setup-and-usage.md#platform-specific-behavior) and change '`latest`' to the version you want (e.g., '`6.1`') or run the MariaDB Package Repository setup script again, specifying the particular version or series you want.

Older versions of the MariaDB Package Repository setup script would configure a specific MariaDB MaxScale series in the repository (i.e., `24.02`), so if you used the script in the past to set up your repository and want MariaDB MaxScale to automatically use the latest GA version, then change `24.02` or whatever version it is set to in the repository configuration to `latest`. Or download the current version of the setup script and re-run it to set up the repository again.

The script can configure your system to install from the repository of an older version of MariaDB MaxScale if you use the `--mariadb-maxscale-version` option. For example, `--mariadb-maxscale-version=25.01`.

If you do not want to configure the **MariaDB MaxScale Repository** on your system, then you can use the `--skip-maxscale` option to prevent the setup script from configuring it.

### MariaDB Enterprise Repositories

The `mariadb_es_repo_setup` script configures the MariaDB Enterprise repositories. These are hosted on the MariaDB customer download server (`dlm.mariadb.com`) and require a valid customer download token, which you supply with the `--token` option (see [Run the Script](mariadb-package-repository-setup-and-usage.md#run-the-script) for how to retrieve your token).

By default, `mariadb_es_repo_setup` configures three Enterprise repositories: MariaDB Enterprise Server, MariaDB Enterprise Tools, and MariaDB Enterprise MaxScale. It can also configure the [Unsupported repository](mariadb-package-repository-setup-and-usage.md#the-mariadb-enterprise-unsupported-repository) on request.

#### MariaDB Enterprise Server Repository

The **MariaDB Enterprise Server** repository contains the same types of packages as the Community Server repository described above — the server, clients and utilities, client libraries, plugins, and `mariadb-backup` — but as the MariaDB Enterprise Server builds rather than the Community builds. The packages are served from `https://dlm.mariadb.com/repo/<token>/mariadb-enterprise-server/<version>/`.

To configure a different release series, or to pin a specific release, use the [`--mariadb-server-version`](mariadb-package-repository-setup-and-usage.md#mariadb-server-version) option. To skip this repository, use the `--skip-server` option.

#### MariaDB Enterprise Tools Repository

The **MariaDB Enterprise Tools** repository contains additional tools for use with MariaDB Enterprise. The packages are served from `https://dlm.mariadb.com/repo/<token>/enterprise-tools/<version>/`.

By default, the script configures the latest version of the Enterprise Tools. To configure a different version, use the `--mariadb-enterprise-tools-version` option. To skip this repository, use the `--skip-enterprise-tools` option.

#### MariaDB Enterprise MaxScale Repository

The **MariaDB Enterprise MaxScale** repository contains [MariaDB MaxScale](mariadb-package-repository-setup-and-usage.md#mariadb-maxscale-repository) packages. The packages are served from `https://dlm.mariadb.com/repo/<token>/maxscale-enterprise/<version>/`.

`mariadb_es_repo_setup` configures the latest stable MariaDB MaxScale Enterprise release series by default. To configure a different version, use the [`--mariadb-maxscale-version`](mariadb-package-repository-setup-and-usage.md#mariadb-maxscale-version) option. To skip this repository, use the `--skip-maxscale` option.

### The MariaDB Enterprise Unsupported Repository

In addition to its default repositories, the `mariadb_es_repo_setup` script can configure a **MariaDB Enterprise Server Unsupported** repository. This repository contains unsupported storage engines and other supplemental packages, such as the CONNECT storage engine.

The Unsupported repository is _not_ configured by default. To include it, add the `--include-unsupported` option when you run the script:

```bash
sudo ./mariadb_es_repo_setup --token="${token}" --include-unsupported --apply
```

Once the repository is configured, you can install its packages using your platform's package manager, as described in [Installing Packages With the MariaDB Package Repository](mariadb-package-repository-setup-and-usage.md#installing-packages-with-the-mariadb-package-repository).

{% hint style="warning" %}
Packages in the Unsupported repository are not covered by MariaDB Enterprise support. Only install them if you understand the implications.
{% endhint %}

## Supported Distributions

The MariaDB Package Repository setup script is designed for Linux distributions that meet MariaDB's current platform support policy. Supported platforms may vary over time and can differ across different MariaDB release series.

For a comprehensive and current list of supported platforms, refer to:

* [MariDB Engineering Policy](https://mariadb.com/engineering-policies/)
* The [MariaDB Downloads](https://mariadb.com/downloads/) page for your specific version

If the setup script does not support your distribution, you can install MariaDB using the MariaDB Foundation's [Repository Configuration Tool](https://mariadb.org/download/?t=repo-config) or check your distribution's [native repositories](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb) for MariaDB packages.

## Options

To provide options to the script, you must tell your script to expect them by executing bash with the options `-s --`, for example:

```
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --help
```

| Option                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--apply`                     | `mariadb_es_repo_setup` only. Write the repository configuration to the appropriate file, import the GPG public keys used by the repositories, and update the package cache. The default behavior of `mariadb_es_repo_setup` is to output the repository configuration to stdout. See [--apply and --write-to-stdout](mariadb-package-repository-setup-and-usage.md#apply-and-write-to-stdout) for more information on this option                         |
| `--arch=`                     | Override detection of the CPU architecture. Acceptable values are `x86_64`, `aarch64`, `amd64`, and `arm64`. If you use this option, the script skips its own CPU architecture detection. |
| `--help`                      | Display a usage message and exit                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `--include-tools`             | Include the 'Tools' repository. This repository is no longer configured by default, so use this option to add it. |
| `--include-unsupported`       | `mariadb_es_repo_setup` only. Include the 'Unsupported' repository, which contains unsupported storage engines (such as the CONNECT engine) and other supplemental packages. This repository is not configured by default. See [The Unsupported Repository](mariadb-package-repository-setup-and-usage.md#the-mariadb-enterprise-unsupported-repository) for more information on this option |
| `--list`                      | On Debian and Ubuntu, write the older one-line `/etc/apt/sources.list.d/mariadb.list` format instead of the default Deb822 `mariadb.sources` format |
| `--mariadb-server-version=`   | Override the default MariaDB Server version. See [--mariadb-server-version](mariadb-package-repository-setup-and-usage.md#mariadb-server-version) for more information on this option                                                                                                                                                                                                                                                                      |
| `--mariadb-maxscale-version=` | Override the default MariaDB MaxScale version. See [--mariadb-maxscale-version](mariadb-package-repository-setup-and-usage.md#mariadb-maxscale-version) for more information on this option                                                                                                                                                                                                                                                                |
| `--mariadb-enterprise-tools-version=` | `mariadb_es_repo_setup` only. Override the default MariaDB Enterprise Tools version. By default, the script uses the latest version. |
| `--os-type=`                  | Override detection of OS type. Acceptable values include `debian`, `ubuntu`, `rhel`, and `sles`. See [--ostype and --os-version](mariadb-package-repository-setup-and-usage.md#os-type-and-os-version) for more information on this option                                                                                                                                                                                                                 |
| `--os-version=`               | Override detection of OS version. Acceptable values depend on the OS type you specify, including: `8`, `9`, or `10` for RHEL; `bookworm` or `trixie` for Debian; and `jammy` or `noble` for Ubuntu. See [--ostype and --os-version](mariadb-package-repository-setup-and-usage.md#os-type-and-os-version) for more information on this option                                                                                                              |
| `--skip-key-import`           | Skip importing GPG signing keys, _**not recommended**_                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--skip-maxscale`             | Skip the 'MaxScale' repository                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--skip-server`               | Skip the 'MariaDB Server' repository (either Community or Enterprise depending on the script you are using)                                                                                                                                                                                                                                                                                                                                                |
| `--skip-tools`                | Skip the 'Tools' repository                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `--skip-enterprise-tools`     | Skip the 'Enterprise Tools" repository (`mariadb_es_repo_setup` only)                                                                                                                                                                                                                                                                                                                                                                                      |
| `--skip-verify`               | Skip verification of MariaDB Server versions. Use with caution, as this can lead to an invalid [repository configuration file](mariadb-package-repository-setup-and-usage.md#platform-specific-behavior) being created, sometimes useful for testing                                                                                                                                                                                                       |
| `--skip-check-installed`      | Skip tests for required prerequisites for this script, useful if generating the config on a different machine                                                                                                                                                                                                                                                                                                                                              |
| `--skip-eol-check`            | Skip tests for versions that are past their EOL date                                                                                                                                                                                                                                                                                                                                                                                                       |
| `--skip-os-eol-check`         | Skip tests for operating system versions past the EOL date                                                                                                                                                                                                                                                                                                                                                                                                 |
| `--skip-xpand`                | `mariadb_es_repo_setup` only. Skip the 'Xpand' instructions. RHEL/CentOS 7 only. |
| `--token`                     | `mariadb_es_repo_setup` only. Your MariaDB Enterprise Repository token. This is required for `mariadb_es_repo_setup` to work. The token is not required for `mariadb_repo_setup` or for MariaDB Community Server repositories. See [Run the Script: mariadb\_es\_repo\_setup](mariadb-package-repository-setup-and-usage.md#mariadb_es_repo_setup-1) for more information.                                                                                 |
| `--verbose`                   | `mariadb_es_repo_setup` only. Be more verbose when running by displaying \[info] messages about what the script is doing. `mariadb_repo_setup` always runs in verbose mode, so it does not have this option.                                                                                                                                                                                                                                               |
| `--version`                   | Output the script version and exit |
| `--write-to-stdout`           | `mariadb_repo_setup` only. Write output to stdout instead of to the OS's [repository configuration file](mariadb-package-repository-setup-and-usage.md#platform-specific-behavior). This will also skip importing GPG public keys and updating the package cache on platforms where that behavior exists. See [--apply and --write-to-stdout](mariadb-package-repository-setup-and-usage.md#apply-and-write-to-stdout) for more information on this option |

### `--mariadb-server-version`

By default, the script will configure your system to install from the repository of the latest GA version of MariaDB. If a new major GA release occurs and you would like to upgrade to it, then you will need to either manually edit the [repository configuration file](mariadb-package-repository-setup-and-usage.md#platform-specific-behavior) to point to the new version or run the script again.

The script can also configure your system to install from the repository of a different version of MariaDB by using the `--mariadb-server-version` option.

#### Usage Example

{% tabs %}
{% tab title="MariaDB Enterprise Server" %}
With `mariadb_es_repo_setup` for MariaDB Enterprise Server, to configure your system to install from the MariaDB Enterprise Server 11.8 repository you would do:

```bash
./mariadb_es_repo_setup --token=$token --mariadb-server-version="11.8"
```

To specify a specific MariaDB Enterprise Server release, you need to put in the full version number, e.g. for MariaDB Enterprise Server 11.8.5-2:

```bash
./mariadb_es_repo_setup --token=$token --mariadb-server-version="11.8.5-2"
```

For more details see [Pinning the Repository to a Specific Minor Release](mariadb-package-repository-setup-and-usage.md#mariadb-enterprise-server-2)
{% endtab %}

{% tab title="MariaDB Community Server" %}
With mariadb\_repo\_setup for MariaDB Community Server, the string `mariadb-` has to be prepended to the version number. For example, to configure your system to install from the repository of MariaDB 11.8, that would be:

```bash
./mariadb_repo_setup --mariadb-server-version="mariadb-11.8"
```

To specify a specific MariaDB Community Server release, you need to put in the full version number, e.g. for MariaDB Community Server 11.8.5:

```bash
./mariadb_repo_setup --mariadb-server-version="mariadb-11.8.5"
```

For more details see [Pinning the Repository to a Specific Minor Release](mariadb-package-repository-setup-and-usage.md#mariadb-community-server-2)
{% endtab %}
{% endtabs %}

#### Current Supported Major Versions

{% tabs %}
{% tab title="MariaDB Enterprise Server" %}
The following MariaDB Enterprise Server versions are currently supported:

* `10.6`
* `11.4`
* `11.8` (default)
{% endtab %}

{% tab title="MariaDB Community Server" %}
The following MariaDB Community Server versions are currently supported:

* `mariadb-10.6`
* `mariadb-10.11`
* `mariadb-11.4`
* `mariadb-11.8`
* `mariadb-11.rolling`
* `mariadb-11.rc`
* `mariadb-12.1`
* `mariadb-12.2`
* `mariadb-12.rolling` (default)
* `mariadb-12.rc`
{% endtab %}
{% endtabs %}

#### Pinning the Repository to a Specific Minor Release

{% tabs %}
{% tab title="MariaDB Enterprise Server" %}
If you want to pin the repository of a specific minor release, such as [MariaDB Enterprise Server 11.8.5-2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.8/11.8.5-2), then you need to specify the full release version number, e.g. `11.8.5-2`. This may be helpful if you want to avoid automatic upgrades. However, avoiding upgrades is not recommended, since minor maintenance releases may contain important bug fixes and fixes for security vulnerabilities.

{% hint style="info" %}
Note: MariaDB Enterprise Server version numbers include a '_release_' suffix that differs from MariaDB Community Server version numbers, e.g. `-2` for MariaDB Enterprise Server `11.8.5-2` whereas the equivalent MariaDB Community Server release is just `11.8.5`. This suffix is required when specifying the full Enterprise Server version number.

To see a list of all MariaDB Enterprise Server releases, see the [Enterprise Server - All Releases](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/all-releases) page. The Version column in the tables on that page list the version numbers of every MariaDB Enterprise Server release.
{% endhint %}

See the [Usage Example - MariaDB Enterprise Server](mariadb-package-repository-setup-and-usage.md#mariadb-enterprise-server) section above for an example of pinning the repository to a specific version.
{% endtab %}

{% tab title="MariaDB Community Server" %}
If you want to pin the repository of a specific minor release, such as [MariaDB Community Server 11.8.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.5), then you need to specify the complete release version, e.g. `mariadb-11.8.5`. This may be helpful if you want to avoid upgrades. However, avoiding upgrades is not recommended, since minor maintenance releases may contain important bug fixes and fixes for security vulnerabilities.

{% hint style="info" %}
To see a list of all MariaDB Community Server releases, see the [Community Server - All Releases](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/all-releases) page. The Version column in the tables on that page list the version numbers of every MariaDB Community Server release.
{% endhint %}

See the [Usage Example - MariaDB Community Server](mariadb-package-repository-setup-and-usage.md#mariadb-community-server) section above for an example of pinning the repository to a specific version.
{% endtab %}
{% endtabs %}

### `--mariadb-maxscale-version`

By default, the script will configure your system to install from the repository of the latest GA version of MariaDB MaxScale.

If you would like to pin the repository to a specific version of MariaDB MaxScale, then you will need\
to either manually edit the [repository configuration file](mariadb-package-repository-setup-and-usage.md#platform-specific-behavior) to point to the desired version or use the `--mariadb-maxscale-version` option.

For example, to configure your system to install from the repository of MariaDB MaxScale 6.1, that would be:

```bash
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --mariadb-maxscale-version="6.1"
```

The following MariaDB MaxScale versions are currently supported:

* MaxScale 25.10
* MaxScale 25.01
* MaxScale 24.02
* MaxScale 23.08
* MaxScale 23.02
* MaxScale 22.08

The special identifiers `latest` (for the latest GA release) and `beta` (for the latest beta release) are also supported. By default, the `mariadb_repo_setup` script uses `latest` as the version.

### `--os-type` and `--os-version`

If you want to run this script on an unsupported OS that you believe to be package-compatible with an OS that is supported, then you can use the `--os-type` and `--os-version` options to override the script's OS detection. If you use either option, then you must use both options.

The supported values for `--os-type` are:

* `rhel`
* `debian`
* `ubuntu`
* `sles`

If you use a non-supported value, then the script will fail, just as it would fail if you ran the script on an unsupported OS.

The supported values for `--os-version` are entirely dependent on the OS type.

For Red Hat Enterprise Linux (RHEL): `8`, `9`, and `10` are valid options.

For Debian and Ubuntu, the version must be specified as the codename of the specific release. For example, Debian 13 must be specified as `trixie`, and Ubuntu 24.04 must be specified as `noble`.

These options can be useful if your distribution is a fork of another distribution. As an example, Pop!\_OS 24.04 LTS is based on and is fully compatible with Ubuntu 24.04 LTS (noble). Therefore, if you are using Pop!\_OS, then you can configure your system to install from the repository of Ubuntu 24.04 LTS (noble) by specifying `--os-type=ubuntu`` ``--os-version=noble` to the MariaDB Package Repository setup script.

For example, to manually set the `--os-type` and `--os-version` to RHEL 10, you could do:

```bash
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --os-type=rhel --os-version=10
```

### `--apply` and `--write-to-stdout`

The `mariadb_repo_setup` and `mariadb_es_repo_setup` scripts generally behave the same but there are some key differences. One of the major ones relates to the options `--apply` and `--write-to-stdout`.

The `--apply` option is only for `mariadb_es_repo_setup`. It directs the script to apply the changes to the system, including creating the [repository configuration file](mariadb-package-repository-setup-and-usage.md#platform-specific-behavior), importing the repository GPG keys, and updating the package cache. `mariadb_repo_setup` does this by default, so it does not have the `--apply` option and instead has the `--write-to-stdout` option to flip the behavior.

The `--write-to-stdout` option is only for `mariadb_repo_setup`. It will prevent the script from modifying anything on the system. The repository configuration will not be written to the [repository configuration file](mariadb-package-repository-setup-and-usage.md#platform-specific-behavior), GPG keys will not be imported, and the package cache will not be updated. Instead, the repository configuration will be printed to standard output (stdout). This allows the configuration to be reviewed, redirected elsewhere, consumed by another script, or used in some other way. `mariadb_es_repo_setup` does this by default, so it does not have the `--write-to-stdout` option, and instead has the `--apply` option to flip the behavior.

The `--write-to-stdout` option automatically enables `--skip-key-import`.

For example:

```bash
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash -s -- --write-to-stdout
```

Both scripts will ignore unknown options so it is safe to, for example, always pass `--apply` to both scripts so that their behavior is the same.

## Platform-Specific Behavior

Locations of the repository configuration file the scripts will create on various Linux distributions and other tasks the scripts do on those distributions.

{% tabs %}
{% tab title="RHEL" %}
**Platform-Specific Behavior on RHEL and equivalents**

On Red Hat Enterprise Linux (RHEL) and equivalents, the MariaDB Package Repository setup script performs the following tasks:

1. Creates a repository configuration file at `/etc/yum.repos.d/mariadb.repo`
2. Imports the GPG public key used to verify the signature of MariaDB software packages with `rpm --import` from `supplychain.mariadb.com`
{% endtab %}

{% tab title="Debian / Ubuntu" %}
**Platform-Specific Behavior on Debian and Ubuntu**

On Debian and Ubuntu, the MariaDB Package Repository setup script performs the following tasks:

1. Creates a repository configuration file at `/etc/apt/sources.list.d/mariadb.list`
2. Creates a package preferences file at `/etc/apt/preferences.d/mariadb-enterprise.pref`, which gives packages from MariaDB repositories a higher priority than packages from OS and other repositories, which can help avoid conflicts. It looks like the following:

```ini
Package: *
Pin: origin downloads.mariadb.com
Pin-Priority: 1000
```

1. Imports the GPG public key used to verify the signature of MariaDB software package
2. Updates the package cache with package definitions from the MariaDB Package Repository with `apt update`
{% endtab %}

{% tab title="SLES" %}
**Platform-Specific Behavior on SLES**

On SUSE Linux Enterprise Server (SLES), the MariaDB Package Repository setup script performs the following tasks:

1. Creates a repository configuration file at `/etc/zypp/repos.d/mariadb.repo`
2. Imports the GPG public key used to verify the signature of MariaDB software packages with `rpm --import` from `supplychain.mariadb.com`
{% endtab %}
{% endtabs %}

## Installing Packages With the MariaDB Package Repository

After setting up the MariaDB Package Repository, you can install the software packages in the supported repositories.

{% tabs %}
{% tab title="RHEL" %}
**Installing Packages on RHEL and equivalents**

To install MariaDB on Red Hat Enterprise Linux (RHEL) and equivalents, see the instructions in the [Installing MariaDB Packages with YUM](installing-mariadb/binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum). For example:

```bash
sudo dnf install MariaDB-server MariaDB-client MariaDB-backup
```

To install MariaDB MaxScale on Red Hat Enterprise Linux (RHEL) and equivalents, see the instructions at [MariaDB MaxScale Installation Guide](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/other-maxscale-versions/mariadb-maxscale-mariadb-maxscale-23/maxscale-23-getting-started/mariadb-maxscale-23-mariadb-maxscale-installation-guide). For example:

```bash
sudo dnf install maxscale
```
{% endtab %}

{% tab title="Debian / Ubuntu" %}
**Installing Packages on Debian and Ubuntu**

To install MariaDB on Debian and Ubuntu, see the instructions at [Installing MariaDB Packages with APT](installing-mariadb/binary-packages/installing-mariadb-deb-files.md#installing-mariadb-packages-with-apt). For example:

```bash
sudo apt install mariadb-server mariadb-client mariadb-backup galera-4
```

To install MariaDB MaxScale on Debian and Ubuntu, see the instructions at [MariaDB MaxScale Installation & Configuration](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/deployment/installation-and-configuration). For example:

```bash
sudo apt install maxscale
```
{% endtab %}

{% tab title="SLES" %}
**Installing Packages on SLES**

To install MariaDB on SUSE Linux Enterprise Server (SLES), see the instructions at [Installing MariaDB Packages with ZYpp](installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp). For example:

```bash
sudo zypper install MariaDB-server MariaDB-client MariaDB-backup
```

To install MariaDB MaxScale on SUSE Linux Enterprise Server (SLES), see the instructions at [MariaDB MaxScale Installation Guide](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/other-maxscale-versions/mariadb-maxscale-mariadb-maxscale-23/maxscale-23-getting-started/mariadb-maxscale-23-mariadb-maxscale-installation-guide). For example:

```bash
sudo zypper install maxscale
```
{% endtab %}
{% endtabs %}

## Versions

The version number of each script is a date, which you can find by running the script with the `--version` option, or by opening the script in a text editor and looking at line 4, `version="..."`. The tables below list the released versions of each script and their `sha256sum` checksums.

{% hint style="info" %}
For the list of changes made in each version, see the changelogs:

* [mariadb\_repo\_setup Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/tools/mariadb-repo-setup-changelog)
* [mariadb\_es\_repo\_setup Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/tools/mariadb-es-repo-setup-changelog)
{% endhint %}

{% tabs %}
{% tab title="mariadb_es_repo_setup" %}
**mariadb\_es\_repo\_setup Versions**

| Version    | sha256sum                                                          |
| ---------- | ------------------------------------------------------------------ |
| 2026-06-30 | `f1baa2eb7af306bc17ede4659e207348f23851b47391415b6e4358a51ac45f28` |
| 2026-04-30 | `704beacaf236155a69eec63b06987007ba612c7f665dd76cfb384b68fccff8af` |
| 2025-12-10 | `62a28aa1f060b4055751d93a88bc11c5556c2b23103c6a6287a8fcb0a4b8a13f` |
| 2025-10-22 | `1f584ffd368d18c64b8820bf6cd9b1114dda11a0ecf9524be3c967a3a5be941b` |
| 2025-09-08 | `c33b022c2cc325fa50be62eae070ea0bdcaf85367f840accac7acaeea1e8a972` |
| 2025-06-04 | `4d483b4df193831a0101d3dfa7fb3e17411dda7fc06c31be4f9e089c325403c0` |
| 2025-01-16 | `99ea6c55dbf32bfc42cdcd05c892aebc5e51b06f4c72ec209031639d6e7db9fe` |
| 2025-01-07 | `b98c6436e01ff33d7e88513edd7b77a965c4500d6d52ee3f106a198a558927af` |
| 2024-11-19 | `97e5ef25b4c4a4bd70b30da46b1eae0b57db2f755ef820a28d254e902ab5a879` |
| 2024-11-13 | `0c181ada4e7a4cd1d7688435c478893502675b880be2b918af7d998e239eb325` |
| 2024-09-20 | `c12da6a9baa57eab7fa685aa24bf76e6929a8c67f4cd244835520c0181007753` |
| 2024-09-09 | `733f247c626d965304b678b62a4b86eb4bb8bf956f98a241b6578dedc6ca4020` |
| 2024-06-12 | `b96fcd684a84bbe1080b6276f424537fc9d9c11ebe243ad8b9a45dd459f6ee4f` |
| 2023-07-27 | `f8eb9c1b59ccfd979d27e39798d2f2a98447dd29e2149ce92bf606aab4493ad9` |
| 2023-03-13 | `8dfef0ec98eb03a4455df07b33107a6d4601425c9df0ab5749b8f10bf3abdcbb` |
| 2022-10-26 | `3f4a9d1c507a846a598e95d6223871aade69a9955276455324e7cc5f54a87021` |
| 2022-09-12 | `713a8f78ea7bab3eccfb46dc14e61cd54c5cf5a08acb5c320ef5370d375e48bd` |
| 2022-06-14 | `cfcd35671125d657a212d92b93be7b1f4ad2fda58dfa8b5ab4b601bf3afa4eae` |
| 2022-03-11 | `53efddb84ea12efa7d521499a7474065bd4a60c721492d0e72b4336192f4033f` |
| 2021-12-13 | `5feb2aac767c512cc9e2af674d1aef42df0b775ba2968fffa8700eb42702bd44` |
| 2021-10-13 | `4f266ff758fe15eeb9b8b448a003eb53e93f3064baf1acb789dd39de4f534b1d` |
| 2021-09-14 | `b741361ea3a0a9fcaa30888a63ff3a8a4021882f126cf4ef26cf616493a29315` |
| 2021-08-26 | `a49347a4e36f99c5b248403ed9fb9b33a2f07f5e24605a694b1b1e24d7199f28` |
| 2021-06-29 | `99e768b24ae430b37dec7cb69cdd625396630dba18f5e1588ee24d3d8bb97064` |
| 2021-06-14 | `ec08f8ede524f568b3766795ad8ca1a0d0ac4db355a18c3d85681d7f9c0f8c09` |
| 2021-05-04 | `bf67a231c477fba0060996a83b197c29617b6193e1167f6f062216ae13c716c7` |
| 2021-03-15 | `99c7f4a3473a397d824d5f591274c2a4f5ebf6dc292eea154800bbaca04ddc7e` |
| 2021-02-12 | `c78db828709d94876406a0ea346f13fbc38e73996795903f40e3c21385857dd4` |
| 2020-12-16 | `c01fa97aed71ca0cd37cba7036ff80ab40efed4cc261c890aa2aa11cd8ab4e2f` |
| 2020-12-15 | `e42f1f16f2c78a3de0e73dcc2a9081e2f771b3161f4f4ceecb13ea788d84673b` |
| 2020-12-14 | `4aaf495606633a47c55ea602829e67e702aec0a5c6ff6b1af90709c19ee9f322` |
| 2020-10-07 | `93fa0df3d6491a791f5d699158dcfe3e6ce20c45ddc2f534ed2f5eac6468ff0a` |
| 2020-09-08 | `eeebe9e08dffb8a4e820cc0f673afe437621060129169ea3db0790eb649dbe9b` |
| 2020-07-16 | `957bc29576e8fd320fa18e35fa49b5733f3c8eeb4ca06792fb1f05e089c810ff` |
{% endtab %}

{% tab title="mariadb_repo_setup" %}
**mariadb\_repo\_setup Versions**

| Version    | sha256sum                                                          |
| ---------- | ------------------------------------------------------------------ |
| 2026-06-30 | `7325ac7755809ca3312b446bd832542421699298f25b701f9a111bb42df0c7c1` |
| 2026-04-23 | `96d4ce68b93dc10afc6189bb01a90043bebbd2b8bdc1b62065e12c87a0757b25` |
| 2025-12-10 | `73f4ab14ccc3ceb8c03bb283dd131a3235cfc28086475f43e9291d2060d48c97` |
| 2025-11-18 | `7a3e1610fee91347e198214e3672a6d3932ccbbf67905d9e892e9255baaec292` |
| 2025-08-07 | `923eea378be2c129adb4d191f01162c1fe5473f1114d7586f096b5f6b9874efe` |
| 2025-02-13 | `c4a0f3dade02c51a6a28ca3609a13d7a0f8910cccbb90935a2f218454d3a914a` |
| 2024-11-14 | `ceaa5bd124c4d10a892c384e201bb6e0910d370ebce235306d2e4b860ed36560` |
| 2024-08-14 | `6083ef1974d11f49d42ae668fb9d513f7dc2c6276ffa47caed488c4b47268593` |
| 2024-05-30 | `26e5bf36846003c4fe455713777a4e4a613da0df3b7f74b6dad1cb901f324a84` |
| 2024-02-16 | `30d2a05509d1c129dd7dd8430507e6a7729a4854ea10c9dcf6be88964f3fdc25` |
| 2023-11-21 | `2d7291993f1b71b5dc84cc1d23a65a5e01e783aa765c2bf5ff4ab62814bb5da1` |
| 2023-08-21 | `935944a2ab2b2a48a47f68711b43ad2d698c97f1c3a7d074b34058060c2ad21b` |
| 2023-08-14 | `f5ba8677ad888cf1562df647d3ee843c8c1529ed63a896bede79d01b2ecc3c1d` |
| 2023-06-09 | `3a562a8861fc6362229314772c33c289d9096bafb0865ba4ea108847b78768d2` |
| 2023-02-16 | `ad125f01bada12a1ba2f9986a21c59d2cccbe8d584e7f55079ecbeb7f43a4da4` |
| 2022-11-17 | `367a80b01083c34899958cdd62525104a3de6069161d309039e84048d89ee98b` |
| 2022-08-22 | `733cf126b03f73050e242102592658913d10829a5bf056ab77e7f864b3f8de1f` |
| 2022-08-15 | `f99e1d560bd72a3a23f64eaede8982d5494407cafa8f995de45fb9a7274ebc5c` |
| 2022-06-14 | `d4e4635eeb79b0e96483bd70703209c63da55a236eadd7397f769ee434d92ca8` |
| 2022-02-08 | `b9e90cde27affc2a44f9fc60e302ccfcacf71f4ae02071f30d570e6048c28597` |
| 2022-01-18 | `c330d2755e18e48c3bba300a2898b0fc8ad2d3326d50b64e02fe65c67b454599` |
{% endtab %}
{% endtabs %}

{% include "../../.gitbook/includes/license-cc-by-sa-gnu-fdl.md" %}

{% @marketo/form formId="4316" %}
