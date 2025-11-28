# Install MariaDB Connector/C

MariaDB Connector/C supports several Linux distributions and Microsoft Windows.

## Configure Package Repository (Linux)

To install MariaDB Connector/C on Linux using APT, YUM, or ZYpp, you must configure your system to use either the ES Package Repository or the CS Package Repository.

If your system is already configured to use one of these package repositories, you can skip to [install MariaDB Connector/C](install-mariadb-connector-c.md#installation).

Choose a package repository to configure:

| **Package Repository**                                                        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ES Package Repository](install-mariadb-connector-c.md#es-package-repository) | <ul><li>MariaDB Enterprise Server package repository</li><li>Available to customers of MariaDB Corporation</li><li>Available for APT, YUM, and ZYpp on supported Linux distributions</li><li>Configured with the <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage">mariadb_es_repo_setup</a> utility</li></ul> |
| [CS Package Repository](install-mariadb-connector-c.md#cs-package-repository) | <ul><li>MariaDB Community Server package repository</li><li>Publicly available</li><li>Available for APT, YUM, and ZYpp on supported Linux distributions</li><li>Configured with the <a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage">mariadb_repo_setup</a> utility</li></ul>                                |

### ES Package Repository

MariaDB Connector/C is available from the same package repository as MariaDB Enterprise Server.

To configure the ES package repository:

1.  Install `curl`.

    Install via APT on Debian, Ubuntu:

    ```bash
    sudo apt install curl
    ```

    Install via YUM on CentOS, RHEL, Rocky Linux:

    ```bash
    sudo yum install curl
    ```

    Install via ZYpp on SLES:

    ```bash
    sudo zypper install curl
    ```
2.  Download the [mariadb\_es\_repo\_setup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) utility, validate its checksum, and ensure that its permissions allow it to be executed:

    ```
    $ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
    ```

    ```
    $ echo "${checksum}  mariadb_es_repo_setup" \
        | sha256sum -c -
    ```

    ```
    $ chmod +x mariadb_es_repo_setup
    ```

    1. Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the [Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#versions) section at the bottom of the [MariaDB Package Repository Setup and Usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) page. Subsitute `${checksum}` in the example above with the latest checksum. 
3. Retrieve your Customer Download Token at [Customer Download Token at the MariaDB Customer Portal](https://customers.mariadb.com/downloads/token/) and substitute your token for `CUSTOMER_DOWNLOAD_TOKEN` in the following step.
4.  Configure the ES package repository using the [mariadb\_es\_repo\_setup](http://localhost:8000/docs/server/ref/repo/cli/mariadb_es_repo_setup/) utility:

    ```bash
    sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
       --mariadb-server-version="10.6"
    ```

    * All major releases of ES contain the same version of MariaDB Connector/C.
    * By default, the [mariadb\_es\_repo\_setup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) utility will configure your system to use the package repository for ES 10.6.
    * To configure your system to use the ES package repository for a specific major release, use the [--mariadb-server-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#mariadb-server-version) option.
5. [Install MariaDB Connector/C](install-mariadb-connector-c.md#installation-via-package-repository-linux) using the package repository.

### CS Package Repository

MariaDB Connector/C is available from the same package repository as MariaDB Community Server.

To configure the CS package repository:

1.  Install `curl`.

    Install via APT on Debian, Ubuntu:

    ```
    $ sudo apt install curl
    ```

    Install via YUM on CentOS, RHEL, Rocky Linux:

    ```
    $ sudo yum install curl
    ```

    Install via ZYpp on SLES:

    ```
    $ sudo zypper install curl
    ```
2.  Download the [mariadb\_repo\_setup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) utility, validate its checksum, and ensure that its permissions allow it to be executed:

    ```bash
    curl -LsSO https://r.mariadb.com/downloads/mariadb_repo_setup
    ```

    ```bash
    echo "${checksum} mariadb_repo_setup" \
        | sha256sum -c -
    ```

    ```bash
    chmod +x mariadb_repo_setup
    ```

    1. Checksums of the various releases of the `mariadb_repo_setup` script can be found in the [Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#versions) section at the bottom of the [MariaDB Package Repository Setup and Usage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) page. Subsitute `${checksum}` in the example above with the latest checksum. 
3.  Configure the CS package repository using the [mariadb\_repo\_setup](http://localhost:8000/docs/server/ref/repo/cli/mariadb_repo_setup/) utility:

    ```bash
    sudo ./mariadb_repo_setup \
       --mariadb-server-version="mariadb-10.6"
    ```

    * All major releases of CS contain the same version of MariaDB Connector/C.
    * By default, the [mariadb\_repo\_setup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) utility will configure your system to use the package repository for CS 10.6.
    * To configure your system to use the CS package repository for a specific major release, use the [--mariadb-server-version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#mariadb-server-version) option.
4. [Install MariaDB Connector/C](install-mariadb-connector-c.md#installation-via-package-repository-linux) using the package repository.

## Installation

### Installation via Package Repository (Linux)

On supported Linux distributions, MariaDB Connector/C can be installed using APT, YUM, or ZYpp if the system is configured to use the [ES Package Repository](install-mariadb-connector-c.md#es-package-repository) or the [CS Package Repository](install-mariadb-connector-c.md#cs-package-repository).

#### Install on CentOS, RHEL, Rocky Linux

To install MariaDB Connector/C on CentOS, RHEL, and Rocky Linux, you can use YUM if you have the [ES Package Repository](install-mariadb-connector-c.md#es-package-repository) or [CS Package Repository](install-mariadb-connector-c.md#cs-package-repository) configured.

Install MariaDB Connector/C and package dependencies:

```bash
sudo yum install MariaDB-shared MariaDB-devel
```

#### Install on Debian, Ubuntu

To install MariaDB Connector/C on Debian and Ubuntu, you can use APT if you have the [ES Package Repository](install-mariadb-connector-c.md#es-package-repository) or [CS Package Repository](install-mariadb-connector-c.md#cs-package-repository) configured.

Install MariaDB Connector/C and package dependencies:

```bash
sudo apt install libmariadb3 libmariadb-dev
```

#### Install on SLES

To install MariaDB Connector/C on SLES, you can use ZYpp if you have the [ES Package Repository](install-mariadb-connector-c.md#es-package-repository) or [CS Package Repository](install-mariadb-connector-c.md#cs-package-repository) configured.

Install MariaDB Connector/C and package dependencies:

```bash
sudo zypper install MariaDB-shared MariaDB-devel
```

### Install via Binary Tarball (Linux)

MariaDB Connector/C can be installed on supported Linux distributions via a binary tarball package:

1. Go to the [MariaDB Connector/C download page](https://mariadb.com/downloads/connectors/connectors-data-access/c-connector)
2. Ensure the "Product" dropdown reads "C connector."
3. In the "Version" dropdown, select the version you want to download.
4. In the "OS" dropdown, select your Linux distribution.
5. Click on the "Download" button to download the binary tarball package.

### Install via MSI (Windows)

MariaDB Connector/C can be installed on Microsoft Windows via an MSI package:

1. Go to the [MariaDB Connector/C download page](https://mariadb.com/downloads/connectors/connectors-data-access/c-connector)
2. Ensure the "Product" dropdown reads "C connector."
3. In the "Version" dropdown, select the version you want to download.
4. In the "OS" dropdown, select either "MS Windows (64-bit)" or "MS Windows (32-bit)", depending on whether you need a 64-bit or 32-bit connector.
5. Click on the "Download" button to download the MSI package.
6. When the MSI package finishes downloading, run it and follow the on-screen instructions.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
