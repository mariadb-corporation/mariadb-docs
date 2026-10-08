---
description: >-
  Register a primary/replica or Galera topology managed by MaxScale in
  Enterprise Manager and link the monitoring agent on every server in the
  topology.
hidden: true
---

# Add a Database with MaxScale

{% hint style="warning" %}
To install `mema-agent`, you need to setup [MariaDB Enterprise Repository - "MariaDB Enterprise Tools"](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage#repositories)
{% endhint %}

Use this method to add a complete primary/replica or Galera cluster that is managed by one or more MaxScale instances.

{% stepper %}
{% step %}
**Prepare all servers in the topology**

Perform these actions on every server in the topology: the MaxScale instance(s) and each backend MariaDB Server attached.

* Install the Agent package on all servers.

```bash
# For Red Hat/CentOS/Rocky
sudo dnf install -y mema-agent
```

```bash
# For Debian/Ubuntu
sudo apt install -y mema-agent
```

* Create a Local Agent user on each backend MariaDB Server:

```sql
CREATE USER 'monitor'@'localhost' IDENTIFIED BY '<password>';
GRANT PROCESS, BINLOG MONITOR, REPLICA MONITOR, REPLICATION MASTER ADMIN ON *.* TO 'monitor'@'localhost';
```

Replace `<password>` with a secure password.
{% endstep %}

{% step %}
**Register the MaxScale instance in the UI 🖥️**

1. Begin the Add Database process:
   * If this is your first time and no databases are present, you'll be on the "Add Database" screen to begin with.
   * If you already have other databases, click the **+ Add Database** button.
2. Select the **Database with MaxScale** option.
3. Provide the connection details for your MaxScale instance (IP address, API port `8989`, and its admin credentials).
4. Click **Add**. Enterprise Manager will connect to MaxScale and automatically discover all backend MariaDB servers it manages.
{% endstep %}

{% step %}
**Link all agents 🔗**

You must link the agent on every server in the topology to Enterprise Manager. The UI will show the MaxScale instance and discovered backend servers marked as "Not Registered."

For each server in the list (start with the MaxScale instance, then each MariaDB server):

1.  Click the three-dot menu (⋮) and select **Metrics configuration**.

    <figure><img src="../../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>
2.  The UI will generate a unique setup command for that specific server with the username and password you provide. Copy the command.

    <figure><img src="../../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>
3. On that specific server, paste and run the command in the terminal.

Repeat this process for every server in the topology. Once all agents are linked, the dashboard will begin showing the health of the entire topology.
{% endstep %}
{% endstepper %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
