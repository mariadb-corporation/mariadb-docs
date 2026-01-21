---
description: >-
  A detailed walkthrough for installing a specific legacy version of MariaDB
  (10.1.21) on CentOS 7 using individual RPM packages, including dependency
  resolution.
---

# MariaDB Installation via RPMs on CentOS 7

This guide provides the detailed steps for installing MariaDB 10.1.21 via individual RPM packages on CentOS 7. The process involves installing dependencies, then the main packages, and resolving potential conflicts as they appear.

The RPMs needed for the installation are available from the MariaDB website. The required packages for this guide are:

```
jemalloc-3.6.0-1.el7.x86_64.rpm
MariaDB-10.1.21-centos7-x86_64-client.rpm
MariaDB-10.1.21-centos7-x86_64-compat.rpm
galera-25.3.19-1.rhel7.el7.centos.x86_64.rpm
jemalloc-devel-3.6.0-1.el7.x86_64.rpm
MariaDB-10.1.21-centos7-x86_64-common.rpm
MariaDB-10.1.21-centos7-x86_64-server.rpm
```

#### Step-by-Step Installation

1\. Install Basic Dependencies

First, use yum to install some general system packages that may be required.

```bash
yum install rsync nmap lsof perl-DBI nmap-ncat
```

2\. Install MariaDB RPM Packages

Next, install the downloaded RPMs in sequence. Make sure to run these commands as a user with sufficient privileges (e.g., using sudo).

```bash
rpm -ivh jemalloc-3.6.0-1.el7.x86_64.rpm
rpm -ivh jemalloc-devel-3.6.0-1.el7.x86_64.rpm
rpm -ivh MariaDB-10.1.21-centos7-x86_64-common.rpm
rpm -ivh MariaDB-10.1.21-centos7-x86_64-compat.rpm
rpm -ivh MariaDB-10.1.21-centos7-x86_64-client.rpm
rpm -ivh galera-25.3.19-1.rhel7.el7.centos.x86_64.rpm
rpm -ivh MariaDB-10.1.21-centos7-x86_64-server.rpm
```

{% hint style="warning" %}
During this process, you may encounter errors related to dependencies or conflicts. The sections below describe these common issues and their solutions.
{% endhint %}

#### Troubleshooting Common Installation Errors and Warnings

**Error 1: Package Conflict with `mariadb-libs`**

{% tabs %}
{% tab title="Error Message" %}
While installing `mariadb-common`, you may encounter a conflict with an existing package.

```bash
# rpm -ivh MariaDB-10.1.21-centos7-x86_64-common.rpm 

warning: MariaDB-10.1.21-centos7-x86_64-common.rpm: Header V4 DSA/SHA1 Signature, key ID 1bb943db: NOKEY
error: Failed dependencies:
	mariadb-libs < 1:10.1.21-1.el7.centos conflicts with MariaDB-common-10.1.21-1.el7.centos.x86_64
```
{% endtab %}

{% tab title="Solution" %}
You must find and remove the conflicting `mariadb-libs` package.

```bash
# Search for the installed package
rpm -qa | grep mariadb-libs
# Expected output: mariadb-libs-5.5.52-1.el7.x86_64

# Remove the conflicting package (use the exact name from the command above)
rpm -ev --nodeps mariadb-libs-5.5.52-1.el7.x86_64
```

After removing it, you can run the `rpm -ivh MariaDB-10.1.21-centos7-x86_64-common.rpm` command again.
{% endtab %}
{% endtabs %}

**Error 2: Failed Dependency for Galera**

{% tabs %}
{% tab title="Error Message" %}
While installing the Galera package, the installation may fail due to a missing library.

```bash
# rpm -ivh galera-25.3.19-1.rhel7.el7.centos.x86_64.rpm 

error: Failed dependencies:
	libboost_program_options.so.1.53.0()(64bit) is needed by galera-25.3.19-1.rhel7.el7.centos.x86_64
```
{% endtab %}

{% tab title="Solution" %}
The required dependency `libboost_program_options` can be installed using yum.

```bash
yum install boost-devel.x86_64
```

After installing `boost-devel`, you can run the `rpm -ivh galera...` command again.
{% endtab %}
{% endtabs %}

**Warning: GPG Key `NOKEY`**

{% tabs %}
{% tab title="Warning Message" %}
You may also see a warning about a missing GPG key during the installation.

```
warning: galera-25.3.19-1.rhel7.el7.centos.x86_64.rpm: Header V4 DSA/SHA1 Signature, key ID 1bb943db: NOKEY
```
{% endtab %}

{% tab title="Solution" %}
This warning can be resolved by importing the official MariaDB GPG key.

```bash
rpm --import http://yum.mariadb.org/RPM-GPG-KEY-MariaDB
```
{% endtab %}
{% endtabs %}

#### Post-Installation

After all RPMs are successfully installed, the final step is to secure the server. This involves setting the root password, removing test databases, and disallowing remote root login.

```bash
# First, start the newly installed MariaDB service
systemctl start mariadb

# Now, run the security script and follow the prompts
mysql_secure_installation
```

***

_This page is licensed: CC BY-SA / Gnu FDL_
