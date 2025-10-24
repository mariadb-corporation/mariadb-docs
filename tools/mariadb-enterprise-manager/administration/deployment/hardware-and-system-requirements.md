# Hardware and System Requirements

This guide outlines the system and hardware requirements for deploying the Enterprise Manager Server and the Enterprise Manager Agent.

## Enterprise Manager Server 🖥️

The Enterprise Manager Server is the central component that hosts the UI and stores monitoring data.

### Hardware Sizing Guide

<table><thead><tr><th>Monitored Servers</th><th width="138.78125">CPU</th><th width="146.59375">Memory (RAM)</th><th>Storage (SSD)</th></tr></thead><tbody><tr><td><strong>50</strong></td><td>4 cores</td><td>8 GB</td><td>200 GB</td></tr><tr><td><strong>200</strong></td><td>16 cores</td><td>32 GB</td><td>800 GB</td></tr><tr><td><strong>500+</strong></td><td>48 cores</td><td>96 GB</td><td>2000 GB</td></tr></tbody></table>

{% hint style="info" %}
Tip: Adjust storage size depending on your requirements for metrics retention.
{% endhint %}

### System Requirements

* CPU Architecture: x86-64
* Operating System: 64-bit Linux with Docker support.
* Software: Docker Engine and Docker Compose must be installed.

## Enterprise Manager Agent🕵

The agent must be installed on each [MariaDB Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/basics-guide#connecting-to-mariadb-server) and [MaxScale](../../../mariadb-enterprise-operator/topologies/maxscale.md) instance you wish to monitor. Below are the supported operating systems.

### Supported Platforms for MariaDB Server

| MariaDB Server Version | Supported OS (x86\_64, ARM64)                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------- |
| **10.6, 11.4, 11.8**   | <p>RHEL/Rocky/AlmaLinux/Oracle Linux 8, 9, 10 </p><p>Ubuntu LTS 22.04, 24.04 </p><p>Debian 11, 12, 13</p> |

### Supported Platforms for MariaDB MaxScale

| MaxScale Version                                              | Supported OS (x86\_64, ARM64)                                                                |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **23.02\***, **23.08\***, **24.02\***, **25.01\***, **25.10** | <p>RHEL/Rocky/AlmaLinux 8, 9, 10 </p><p>Ubuntu LTS 22.04, 24.04 </p><p>Debian 11, 12, 13</p> |

\* Monitoring and Single Sign-On(SSO) are only supported for MaxScale versions 25.10 and Above

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
