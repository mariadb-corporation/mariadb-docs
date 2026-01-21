---
description: 'Step 1: Prepare ColumnStore Nodes'
---

# Step 1: Prepare ColumnStore Nodes

## Overview

This page details step 1 of the 9-step procedure "[Multnode Localstorage](./)".

This step prepares systems to host MariaDB Enterprise Server and MariaDB Enterprise ColumnStore.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Optimize Linux Kernel Parameters

MariaDB Enterprise ColumnStore performs best with Linux kernel optimizations.

On each server to host an Enterprise ColumnStore node, optimize the kernel:

1. Set the relevant kernel parameters in a sysctl configuration file. To ensure proper change management, use an Enterprise ColumnStore-specific configuration file.\
   \
   Create `a /etc/sysctl.d/90-mariadb-enterprise-columnstore.conf file`:

```systemd
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

2. Use the sysctl command to set the kernel parameters at runtime

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
$ sudo getenforce
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

## Temporarily Configure Firewall for Installation

MariaDB Enterprise ColumnStore requires the following TCP ports:

<table><thead><tr><th width="160">TCP Ports</th><th>Description</th></tr></thead><tbody><tr><td>3306</td><td>Port used for MariaDB Client traffic</td></tr><tr><td>8600-8630</td><td>Port range used for inter-node communication</td></tr><tr><td>8640</td><td>Port used by CMAPI</td></tr><tr><td>8700</td><td>Port used for inter-node communication</td></tr><tr><td>8800</td><td>Port used for inter-node communication</td></tr></tbody></table>

The firewall should be temporarily disabled on each Enterprise ColumnStore node during installation.

The firewall will be configured and re-enabled later in this deployment procedure.

The steps to disable the firewall depend on the specific firewall used by the operating system.

### CentOS / RHEL Stop firewalld

1. Check if the firewalld service is running:

```bash
$ sudo systemctl status firewalld
```

2. If the firewalld service is running, stop it:

```bash
$ sudo systemctl stop firewalld
```

Firewalld will be configured and re-enabled later in this deployment procedure.

### Ubuntu Stop UFW

1. Check if the UFW service is running:

```bash
$ sudo ufw status verbose
```

2. If the UFW service is running, stop it:

```bash
$ sudo ufw disable
```

UFW will be configured and re-enabled later in this deployment procedure.

### Configure the AWS Security Group

To install Enterprise ColumnStore on Amazon Web Services (AWS), the security group must be modified prior to installation.

Enterprise ColumnStore requires all internal communications to be open between Enterprise ColumnStore nodes. Therefore, the security group should allow all protocols and all ports to be open between the Enterprise ColumnStore nodes and the MaxScale proxy.

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

## Configure DNS

MariaDB Enterprise ColumnStore requires all nodes to have host names that are resolvable on all other nodes. If your infrastructure does not configure DNS centrally, you may need to configure static DNS entries in the /etc/hosts file of each server.

On each Enterprise ColumnStore node, edit the /etc/hosts file to map host names to the IP address of each Enterprise ColumnStore node:

```sql
192.0.2.1     mcs1
192.0.2.2     mcs2
192.0.2.3     mcs3
192.0.2.100   mxs1
```

Replace the IP addresses with the addresses in your own environment.

## Next Step

Navigation in the procedure "Deploy ColumnStore Shared Local Storage Topology".

This page was step 1 of 9.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
