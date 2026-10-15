---
description: >-
  Install MariaDB Shell on Linux, macOS, or Windows with an installation script
  or from a release package.
icon: download
---

# Installation

MariaDB Shell is distributed as self-contained packages on the [GitHub releases page](https://github.com/mariadb-corporation/mariadb-shell/releases). Each package includes the Python runtime and the built-in plugins, so it has no other runtime dependencies. You don't need administrator privileges: by default, everything installs into your home directory.

The installation scripts detect your platform, download the matching package, verify its SHA-256 checksum, and create the `mariadb-shell` and `msh` commands. If you prefer to control each step, download and unpack a package manually.

For the list of supported operating systems and architectures, see [Supported Platforms](../about-mariadb-shell.md#supported-platforms).

{% columns %}
{% column %}
{% content-ref url="linux-and-macos.md" %}
[linux-and-macos.md](linux-and-macos.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install, upgrade, and remove MariaDB Shell with the `install.sh` script.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="windows.md" %}
[windows.md](windows.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install, upgrade, and remove MariaDB Shell with the `install.ps1` PowerShell script.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="manual-installation.md" %}
[manual-installation.md](manual-installation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Download a release package, verify it against `SHA256SUMS`, and unpack it yourself.
{% endcolumn %}
{% endcolumns %}
