---
description: 'Step 1: Prepare Systems for Enterprise ColumnStore Nodes'
---

# Step 1: Prepare Systems for Enterprise ColumnStore Nodes

## Overview

This page details step 1 of a 5-step procedure for deploying [Single-Node Enterprise ColumnStore with Local storage](./).

This step prepares the system to host MariaDB Enterprise Server and MariaDB Enterprise ColumnStore.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Optimize Linux Kernel Parameters

MariaDB Enterprise ColumnStore performs best with Linux kernel optimizations.

On each server to host an Enterprise ColumnStore node, optimize the kernel:

1. Set the relevant kernel parameters in a sysctl configuration file. To ensure proper change management, use an Enterprise ColumnStore-specific configuration file.

Create a `/etc/sysctl.d/90-mariadb-enterprise-columnstore.conf` file:

```editorconfig
# minimize swapping
vm.swappiness = 1

# Increase the TCP max buffer size
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216

# Increase the TCP buffer limits
# min, default, and max number of bytes to use
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216

# don't cache ssthresh from previous connection
net.ipv4.tcp_no_metrics_save = 1

# for 1 GigE, increase this to 2500
# for 10 GigE, increase this to 30000
net.core.netdev_max_backlog = 2500
```

2. Use the `sysctl` command to set the kernel parameters at runtime

```bash
$ sudo sysctl --load=/etc/sysctl.d/90-mariadb-enterprise-columnstore.conf
```

## Temporarily Configure Linux Security Modules (LSM)

The Linux Security Modules (LSM) should be temporarily disabled on each Enterprise ColumnStore node during installation.

The LSM will be configured and re-enabled later in this deployment procedure.

The steps to disable the LSM depend on the specific LSM used by the operating system.

### CentOS / RHEL Stop SELinux

SELinux must be set to permissive mode before installing MariaDB Enterprise ColumnStore.

To set SELinux to permissive mode:

1. Set SELinux to permissive mode:

```bash
$ sudo setenforce permissive
```

2. Set SELinux to permissive mode by setting SELINUX=permissive in /etc/selinux/config.

For example, the file will usually look like this after the change:

```systemd
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=permissive
# SELINUXTYPE= can take one of three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected.
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
```

3. Confirm that SELinux is in permissive mode:

```bash
sudo getenforce
Permissive
```

SELinux will be configured and re-enabled later in this deployment procedure. This configuration is not persistent. If you restart the server before configuring and re-enabling SELinux later in the deployment procedure, you must reset the enforcement to permissive mode.

### Debian / Ubuntu AppArmor

AppArmor must be disabled before installing MariaDB Enterprise ColumnStore.

1. Disable AppArmor:

```bash
$ sudo systemctl disable apparmor
```

2. Reboot the system.
3. Confirm that no AppArmor profiles are loaded using aa-status:

```bash
$ sudo aa-status
```

```sql
apparmor module is loaded.
0 profiles are loaded.
0 profiles are in enforce mode.
0 profiles are in complain mode.
0 processes have profiles defined.
0 processes are in enforce mode.
0 processes are in complain mode.
0 processes are unconfined but have a profile defined.
```

AppArmor will be configured and re-enabled later in this deployment procedure.

## Configure Character Encoding

When using MariaDB Enterprise ColumnStore, it is recommended to set the system's locale to UTF-8.

1. On RHEL 8, install additional dependencies:

```bash
$ sudo yum install glibc-locale-source glibc-langpack-en
```

2. Set the system's locale to en\_US.UTF-8 by executing localedef:

```bash
$ sudo localedef -i en_US -f UTF-8 en_US.UTF-8
```

## Next Step

Navigation in the Single-Node Enterprise ColumnStore topology with Local storage deployment procedure:

This page was step 1 of 5.

[Next: Step 2: Install MariaDB Enterprise ColumnStore.](step-2-install-enterprise-columnstore.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
