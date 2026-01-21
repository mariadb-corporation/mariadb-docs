# Adding Databases

{% hint style="warning" %}
To install `mema-agent`, you need to setup [MariaDB Enterprise Repository - "MariaDB Tools"](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#repositories)
{% endhint %}

This guide outlines the two primary methods for registering and monitoring your database topologies in MariaDB Enterprise Manager: adding a standalone server directly or adding a full topology via its MaxScale instance.

## Option 1: Adding a Standalone Server or Topology (Without MaxScale)

Use this method for a single MariaDB Server or to manually define a Primary/Replica or Galera cluster.

{% stepper %}
{% step %}
#### Prepare your server(s)

First, perform these actions **on each MariaDB Server** you plan to add.

1. Install the Agent package.

```bash
# For Red Hat/CentOS/Rocky
sudo dnf install -y mema-agent
```

```bash
# For Debian/Ubuntu
sudo apt install -y mema-agent
```

2. Create the Enterprise Manager user (allows the Enterprise Manager server to connect remotely):

```sql
CREATE USER 'monitor'@'<Enterprise_Manager_IP>' IDENTIFIED BY '<password>';
GRANT REPLICA MONITOR ON *.* TO 'monitor'@'<Enterprise_Manager_IP>';
```

Replace `<Enterprise_Manager_IP>` with the IP of your Enterprise Manager server and `<password>` with a secure password.

3. Create the Local Agent user (required for the agent to collect detailed metrics from the local database instance):

```sql
CREATE USER 'monitor'@'localhost' IDENTIFIED BY '<password>';
GRANT PROCESS, BINLOG MONITOR, REPLICA MONITOR, REPLICATION MASTER ADMIN ON *.* TO 'monitor'@'localhost';
```

Replace `<password>` with a secure password.
{% endstep %}

{% step %}
#### Register in the UI

1. Go to your MariaDB Enterprise Manager web interface (for example `https://<Enterprise_Manager_IP>:8090`).
2. Log in with user who has `edit` permission.
3. Begin the Add Database process:
   * If this is your first time and no databases are present, you'll be on the "Add Database" screen automatically.
   * If you already have other databases, click the **+ Add Database** button.
4.  Ensure the **Database without MaxScale** option is selected.\\

    <figure><img src="../../../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>
5. Fill in the connection details for your first server using the Enterprise Manager User (`'monitor'@'<Enterprise_Manager_IP>'`).
{% endstep %}

{% step %}
#### Standalone server or a Topology

To add a Standalone Server: Click **Add** and proceed to the next step (4).

To create a Topology:

1.  Click the Plus icon (+) to add another server.\\

    <figure><img src="../../../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>
2. Fill in the connection details for the second server in your topology and click **Confirm**. Repeat for all nodes in your topology.
3.  Once all nodes are added, select the Topology Type (e.g., Primary/Replica — default — or Galera Cluster) and click **Confirm**.\\

    <figure><img src="../../../../.gitbook/assets/image (36) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To convert an existing standalone server into a topology of multiple servers: click the three-dot menu (⋮) next to the server, choose **Edit**, and click the Plus icon (+). Then follow the same steps to add nodes.

<img src="../../../../.gitbook/assets/image (38).png" alt="" data-size="original">
{% endhint %}
{% endstep %}

{% step %}
#### Link the Agent(s) 🔗

For each server added, link its agent:

1.  Find the server in the inventory list, click the three-dot menu (⋮), and select **Install Agent**.\\

    <figure><img src="../../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>
2.  Enter the credentials for the Local Agent User (`'monitor'@'localhost'`) to generate a setup command.\\

    <figure><img src="../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>
3. Copy the command and run it on that server's terminal to link the agent.
{% endstep %}
{% endstepper %}

## Option 2: Adding a Topololgy (With MaxScale)

Use this method to add a complete primary/replica or Galera cluster that is managed by one or more MaxScale instances.

{% stepper %}
{% step %}
#### Prepare all servers in the topology

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
#### Register the MaxScale instance in the UI 🖥️

1. Begin the Add Database process:
   * If this is your first time and no databases are present, you'll be on the "Add Database" screen to begin with.
   * If you already have other databases, click the **+ Add Database** button.
2. Select the **Database with MaxScale** option.
3. Provide the connection details for your MaxScale instance (IP address, API port `8989`, and its admin credentials).
4. Click **Add**. Enterprise Manager will connect to MaxScale and automatically discover all backend MariaDB servers it manages.
{% endstep %}

{% step %}
#### Link all a 🔗

You must link the agent on every server in the topology to Enterprise Manager. The UI will show the MaxScale instance and discovered backend servers marked as "Not Registered."

For each server in the list (start with the MaxScale instance, then each MariaDB server):

1.  Click the three-dot menu (⋮) and select **Install Agent**.\\

    <figure><img src="../../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>
2.  The UI will generate a unique setup command for that specific server with the username and password you provide. Copy the command.\\

    <figure><img src="../../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>
3. On that specific server, paste and run the command in the terminal.

Repeat this process for every server in the topology. Once all agents are linked, the dashboard will begin showing the health of the entire topology.
{% endstep %}
{% endstepper %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
