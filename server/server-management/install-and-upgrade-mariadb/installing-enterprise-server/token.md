---
description: >-
  Instructions on how to retrieve and use a Customer Download Token to access
  MariaDB Enterprise Server packages and binaries.
---

# Customer Download Token

MariaDB Corporation customers can use a Customer Download Token to download MariaDB database products using command-line tools or automation. This page provides instructions on how to retrieve and use the Customer Download Token.

Alternatively, customers can download MariaDB database products using a web browser from the [MariaDB Enterprise Download page](https://mariadb.com/downloads/enterprise) without a Customer Download Token if they are logged in with their MariaDB ID.

## Retrieve Customer Download Token

MariaDB Corporation customers can retrieve their Customer Download Token through the MariaDB Customer Portal.

{% hint style="warning" %}
MariaDB Corporation's Customer Download Tokens are customer-specific. Protect the token as you would any security credential.
{% endhint %}

To retrieve the Customer Download Token for your account:

1. Navigate to the [Customer Download Token at the MariaDB Customer Portal](https://customers.mariadb.com/downloads/token/?_ga=2.92018202.1431602578.1740983101-1710706710.1737441288).
2. Log in using your [MariaDB ID](../installing-mariadb/mariadb-id-sign-up.md).
3. Copy the Customer Download Token.

## Use the Customer Download Token

MariaDB Corporation customers can use their Customer Download Token for multiple operations.

Choose the procedure for your desired operation and substitute your Customer Download Token for `CUSTOMER_DOWNLOAD_TOKEN`:

| Operation                                                                                             | Use Case                                                                                                                |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [Configure MariaDB Enterprise Repository](token.md#configure-mariadb-enterprise-repository)           | Install MariaDB database products using package managers on CentOS / RHEL (YUM), Debian / Ubuntu (APT), and SLES (ZYpp) |
| [Download Binary Files with CLI or Automation](token.md#download-binary-files)                        | Download binary files using command-line tools or automation                                                            |
| [Log In to MariaDB Enterprise Docker Registry](token.md#log-in-to-mariadb-enterprise-docker-registry) | Deploy using Docker                                                                                                     |

### Configure MariaDB Enterprise Repository

MariaDB Corporation provides the MariaDB Enterprise Repository to install MariaDB database products using package managers on CentOS / RHEL (YUM), Debian / Ubuntu (APT), and SLES (ZYpp).

The MariaDB Enterprise Repository is configured using the `mariadb_es_repo_setup` script, which requires the Customer Download Token to be provided via the `--token` option.

For additional information, see "[MariaDB Package Repository Setup and Usage](../installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md)".

### Download Binary Files

MariaDB Corporation provides an interface to download binary files using command-line tools or automation.

Binary files can be downloaded using command-line tools or automation from the MariaDB Download interface with the Customer Download Token. The URL is in the following format:

```
https://dlm.mariadb.com/CUSTOMER_DOWNLOAD_TOKEN/FILE
```

Download a binary file using the following procedure:

1. In your web browser, visit the MariaDB Download interface for the specific MariaDB database product:
   * MariaDB Enterprise Server
   * MariaDB MaxScale
   * MariaDB Xpand
2.  In your web browser, navigate to the binary file that you would like to download and copy the URL. For example, to download a binary tarball of MariaDB Enterprise Server 10.6.20-16 for RHEL 8 on x86\_64, the URL is:\\

    ```
    https://dlm.mariadb.com/FILE_ID/mariadb-enterprise-server/10.6.20-16/bintar-rhel-8-x86_64/mariadb-enterprise-10.6.20-16-rhel-8-x86_64.tar.gz
    ```

    \
    `FILE_ID` is an internal identifier that is different for each file.
3.  Extract the `FILE` path from the copied URL. For example, to download the file mentioned above, the FILE path is:\\

    ```
    FILE_ID/mariadb-enterprise-server/10.6.20-16/bintar-rhel-8-x86_64/mariadb-enterprise-10.6.20-16-rhel-8-x86_64.tar.gz
    ```
4.  Use your Customer Download Token and the FILE path to construct your customer-specific URL to download the file using command-line tools or automation.For example, to download the file mentioned above, the customer-specific URL is:\\

    ```
    https://dlm.mariadb.com/CUSTOMER_DOWNLOAD_TOKEN/FILE_ID/mariadb-enterprise-server/10.6.20-16/bintar-rhel-8-x86_64/mariadb-enterprise-10.6.20-16-rhel-8-x86_64.tar.gz
    ```
5. Use your customer-specific URL to download the file using command-line tools or automation:For example, to download the file mentioned above using `wget`:

```bash
wget https://dlm.mariadb.com/CUSTOMER_DOWNLOAD_TOKEN/FILE_ID/mariadb-enterprise-server/10.6.20-16/bintar-rhel-8-x86_64/mariadb-enterprise-10.6.20-16-rhel-8-x86_64.tar.gz
```

or using `curl`:

```bash
curl -LO https://dlm.mariadb.com/CUSTOMER_DOWNLOAD_TOKEN/FILE_ID/mariadb-enterprise-server/10.6.20-16/bintar-rhel-8-x86_64/mariadb-enterprise-10.6.20-16-rhel-8-x86_64.tar.gz
```

### Log in to MariaDB Enterprise Docker Registry

Docker is an open platform for developing, shipping, and running applications that allows you to separate your applications from your infrastructure. MariaDB Corporation provides the [MariaDB Enterprise Docker Registry](../../automated-mariadb-deployment-and-administration/docker-and-mariadb/mariadb-enterprise-docker-registry-for-mariadb-enterprise-server.md).

The MariaDB Enterprise Docker Registry provides Docker images for MariaDB Enterprise Server. The Docker images for MariaDB Enterprise Server are currently beta maturity, so they are not currently recommended for production.

For additional information, see "[Deploy MariaDB Enterprise Server with Docker](../../automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker.md)".

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
