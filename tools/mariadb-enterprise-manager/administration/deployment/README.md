---
description: >-
  Guidelines and instructions for deploying MariaDB Enterprise Manager,
  including network and firewall requirements for successful installation.
---

# Deployment

This section provides an overview of the deployment process for MariaDB Enterprise Manager, covering installation and upgrades for both the central server and the monitoring agents.

MariaDB Enterprise Manager is designed for a streamlined deployment experience. You can launch the main server with a single-line command for a quick start, and a UI-integrated helper tool simplifies the process of installing and registering agents on your monitored databases.

### Installing the Enterprise Manager Server

The Enterprise Manager Server is a Docker-based application installed on a dedicated host. The installation is handled by the installer script, which pulls the necessary container images and starts the application.

As a first step review the hardware, system, and network requirements:

* [Hardware and System Requirements](hardware-and-system-requirements.md)
* [Network and Firewall Requirements](network-and-firewall-requirements.md)

After confirming your hardware, system, and network are compliant, proceed with the installation instructions: [Installing MariaDB Enterprise Manager](installing-mariadb-enterprise-manager/)

### Installing Enterprise Manager Agents

To monitor a MariaDB Server and MaxScale host, [install agent](adding-databases/agent-installation-t-copy.md) on it. Then, use the Enterprise Manager UI to [add the database](adding-databases/) topology and generate the agent setup command. This command includes the correct metric labels for that host.

### Quick start

{% hint style="info" %}
You can quickly set up and launch MariaDB Enterprise Manager with a single-line command. This allows you to start exploring its capabilities without extensive configuration.

Enterprise Manager includes a helper tool, integrated in the UI, for adding agents. The helper prompts you to download a small (< 50M) binary and then provides command-line instructions to install and register agents, enabling quick and seamless addition of new MariaDB databases to Enterprise Manager.
{% endhint %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
