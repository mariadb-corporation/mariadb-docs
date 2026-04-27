# Step 1: Install MariaDB Enterprise Server

## Overview

This page details step 1 of the 6-step procedure "[Deploy Galera Cluster Topology](./)".

This step installs MariaDB Enterprise Server.

MariaDB Enterprise Server installations support MariaDB Enterprise Cluster, powered by Galera. MariaDB Enterprise Cluster uses the Galera Enterprise 4 wsrep provider plugin.

MariaDB Enterprise Cluster requires an odd number of 3 or more nodes. Nodes must meet requirements.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Retrieve Download Token

MariaDB Corporation provides package repositories for CentOS / RHEL (YUM) and Debian / Ubuntu (APT). A download token is required to access the MariaDB Enterprise Repository.

Customer Download Tokens are customer-specific and are available through the MariaDB Customer Portal.

To retrieve the token for your account:

1. Navigate to [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/).
2. Log in.
3. Copy the Customer Download Token.

Substitute your token for `CUSTOMER_DOWNLOAD_TOKEN` when configuring the package repositories.

## Set Up Repository

1. On each Enterprise ColumnStore node, install the prerequisites for downloading the software from the Web.\
   Install on CentOS / RHEL (YUM):

```bash
$ sudo yum install curl
```

Install on Debian / Ubuntu (APT):

```bash
$ sudo apt install curl apt-transport-https
```

2. On each Enterprise ColumnStore node, configure package repositories and specify Enterprise Server:

```bash
$ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
```

```bash
$ echo "${checksum}  mariadb_es_repo_setup" \
       | sha256sum -c -
```

```bash
$ chmod +x mariadb_es_repo_setup
```

```bash
$ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
      --skip-maxscale \
      --skip-tools \
      --mariadb-server-version="11.4"
```

_Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._

## Install Enterprise Server

1. On each Enterprise Cluster node, install MariaDB Enterprise Server and MariaDB Enterprise Backup.

Install via CentOS / RHEL (YUM):

```bash
$ sudo yum install MariaDB-server MariaDB-backup
```

Install via Debian / Ubuntu (APT):

```bash
$ sudo apt update

$ sudo apt install mariadb-server mariadb-backup
```

Install via SLES (ZYpp):

```bash
$ sudo zypper install MariaDB-server MariaDB-backup
```

## Next Step

Navigation in the procedure "Deploy Galera Cluster Topology":

This page was step 1 of 6.

Next: Step 2: Start and Configure MariaDB Enterprise Server

{% include "../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
