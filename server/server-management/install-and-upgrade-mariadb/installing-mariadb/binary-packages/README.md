---
description: >-
  Provides details on using MariaDB binary packages (tarballs, RPMs, DEBs) for
  installation, including repository configuration scripts.
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

# MariaDB Binary Packages

{% columns %}
{% column %}
{% content-ref url="gpg.md" %}
[gpg.md](gpg.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Information about the GPG keys used to sign MariaDB packages and repositories, including how to import them for verification.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-deb-files.md" %}
[installing-mariadb-deb-files.md](installing-mariadb-deb-files.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete .deb installation guide: add repo via mariadb_repo_setup, import GPG keys, apt install mariadb-server galera-4, and APT configuration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rpm/" %}
[rpm](rpm/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install and manage MariaDB Server using RPM packages. This section provides detailed instructions for deploying and upgrading MariaDB on RPM-based Linux distributions. width: default title: visible: true description: visible: true tableOfContents: visible: true outline: visible: true pagination: visible: false metadata: visible: true tags: visible: true
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-alongside-mysql.md" %}
[installing-mariadb-alongside-mysql.md](installing-mariadb-alongside-mysql.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for installing MariaDB on the same server as an existing MySQL installation, useful for migration testing or running multiple versions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-binary-tarballs.md" %}
[installing-mariadb-binary-tarballs.md](installing-mariadb-binary-tarballs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to installing MariaDB from pre-compiled binary tarballs on Linux, allowing for flexible installation paths and multiple versions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-msi-packages-on-windows.md" %}
[installing-mariadb-msi-packages-on-windows.md](installing-mariadb-msi-packages-on-windows.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete MariaDB installation guide. Complete setup instructions for Linux, Windows, and macOS with configuration and verification for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-on-macos-using-homebrew.md" %}
[installing-mariadb-on-macos-using-homebrew.md](installing-mariadb-on-macos-using-homebrew.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to install MariaDB Server on macOS using the Homebrew package manager, including starting the service and securing the installation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-server-pkg-packages-on-macos.md" %}
[installing-mariadb-server-pkg-packages-on-macos.md](installing-mariadb-server-pkg-packages-on-macos.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to install MariaDB Server on macOS. This is possible using Homebrew.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-windows-zip-packages.md" %}
[installing-mariadb-windows-zip-packages.md](installing-mariadb-windows-zip-packages.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for manually installing MariaDB on Windows from a ZIP archive, useful for portable installations or advanced configuration needs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="package-tarballs.md" %}
[package-tarballs.md](package-tarballs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the benefits and use cases for deploying MariaDB using package tarballs (containing RPMs or DEBs) for offline or custom installations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="repo-mirror.md" %}
[repo-mirror.md](repo-mirror.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to create and maintain local mirrors of MariaDB package repositories for secure or air-gapped deployments.
{% endcolumn %}
{% endcolumns %}
