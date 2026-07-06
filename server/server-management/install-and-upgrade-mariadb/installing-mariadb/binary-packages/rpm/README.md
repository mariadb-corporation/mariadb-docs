---
description: >-
  Install and manage MariaDB Server using RPM packages. This section provides
  detailed instructions for deploying and upgrading MariaDB on RPM-based Linux
  distributions.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
---

# Installing MariaDB RPM Files

{% columns %}
{% column %}
{% content-ref url="about-the-mariadb-rpm-files.md" %}
[about-the-mariadb-rpm-files.md](about-the-mariadb-rpm-files.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provides an overview of the RPM packages available for MariaDB, listing the various RPMs such as server, client, backup, and shared libraries, and explaining their contents and dependencies.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="yum.md" %}
[yum.md](yum.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to install MariaDB on systems that use the yum or dnf package managers
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-with-zypper.md" %}
[installing-mariadb-with-zypper.md](installing-mariadb-with-zypper.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Detailed steps for installing MariaDB on SLES and OpenSUSE using the `zypper` package manager, including repository configuration and package installation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="checking-mariadb-rpm-package-signatures.md" %}
[checking-mariadb-rpm-package-signatures.md](checking-mariadb-rpm-package-signatures.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions on how to verify the integrity of MariaDB RPM packages using GPG signatures, including importing the public key and running `rpm --checksig`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-with-the-rpm-tool.md" %}
[installing-mariadb-with-the-rpm-tool.md](installing-mariadb-with-the-rpm-tool.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to installing MariaDB using the low-level `rpm` command, suitable for situations where package managers like `yum` or `dnf` are not available or preferred.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-for-directadmin-using-rpms.md" %}
[mariadb-for-directadmin-using-rpms.md](mariadb-for-directadmin-using-rpms.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Specific instructions for installing MariaDB RPMs on servers running the DirectAdmin control panel, including necessary configuration edits to prevent conflicts.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-installation-version-10121-via-rpms-on-centos-7.md" %}
[mariadb-installation-version-10121-via-rpms-on-centos-7.md](mariadb-installation-version-10121-via-rpms-on-centos-7.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A detailed walkthrough for installing a specific legacy version of MariaDB (10.1.21) on CentOS 7 using individual RPM packages, including dependency resolution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="troubleshooting-mariadb-installs-on-rhel-centos.md" %}
[troubleshooting-mariadb-installs-on-rhel-centos.md](troubleshooting-mariadb-installs-on-rhel-centos.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Solutions for common installation issues on RHEL and CentOS, such as conflicts with existing MySQL installations and handling configuration file backups (.rpmsave).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="why-source-rpms-srpms-arent-packaged-for-some-platforms.md" %}
[why-source-rpms-srpms-arent-packaged-for-some-platforms.md](why-source-rpms-srpms-arent-packaged-for-some-platforms.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the limitations in providing Source RPMs (SRPMs) for certain platforms due to CMake version requirements and build system dependencies.
{% endcolumn %}
{% endcolumns %}
