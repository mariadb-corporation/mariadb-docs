# Agent Installation

{% hint style="warning" %}
To install `mema-agent`, you need to setup [MariaDB Enterprise Repository - "MariaDB Tools"](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#repositories)
{% endhint %}

The `mema-agent` is a small application that must be installed on every server you wish to monitor with MariaDB Enterprise Manager, including MariaDB Server nodes and MaxScale nodes.

This guide covers the recommended installation method using a package manager.

### Prerequisite: Create the Local Monitor User

Before installing the agent on a MariaDB Server host, you must create a local user that the agent will use to connect to the database and collect metrics.

Log in to your MariaDB Server and run the following:

{% code title="Create monitor user" %}
```sql
CREATE USER 'monitor'@'localhost' IDENTIFIED BY '<password>';
GRANT SELECT, PROCESS, REPLICATION CLIENT, RELOAD, REPLICA MONITOR, REPLICATION MASTER ADMIN ON *.* TO 'monitor'@'localhost';
```
{% endcode %}

_Replace `<password>` with a secure password. You will need these credentials later when linking the agent in the Enterprise Manager UI._

### Installation via Package Manager (Recommended)

This method uses your OS's native package manager (`dnf`, `apt`, `zypper`) to install the agent from the MariaDB Enterprise repository.

#### Step 1: Configure the MariaDB Enterprise Repository

If you haven't already configured the MariaDB Enterprise repository on the server, follow these steps.

{% stepper %}
{% step %}
#### Get your Customer Download Token

* Navigate to the [MariaDB Customer Portal](https://customers.mariadb.com/downloads/token/) and log in.
* Copy your **Customer Download Token**. You will need this for the script.
{% endstep %}

{% step %}
#### Download the repository setup script

In your server's terminal, download the official setup script:

```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
```
{% endstep %}

{% step %}
#### Run the script

Make the script executable, then run it with your download token:

{% code title="# Make script executable and run" %}
```bash
chmod +x mariadb_es_repo_setup
sudo ./mariadb_es_repo_setup --token="YOUR_TOKEN_HERE" --apply
```
{% endcode %}

_Replace `YOUR_TOKEN_HERE` with the token you copied from the Customer Portal._
{% endstep %}
{% endstepper %}

#### Step 2: Install the Agent Package

Once the repository is configured, use your system's package manager to install the agent.

{% tabs %}
{% tab title="Red Hat / Rocky / CentOS" %}
```bash
sudo dnf install mema-agent
```
{% endtab %}

{% tab title="Debian / Ubuntu" %}
```bash
sudo apt-get install mema-agent
```
{% endtab %}
{% endtabs %}

The agent is now installed and running as a service.

### Next Steps: Linking the Agent 🔗

After the agent is installed, it is running but not yet configured or linked to your MariaDB Enterprise Manager server.

The final step is to link the agent, which is done from the Enterprise Manager UI. Please refer to the ["Adding Databases to MariaDB Enterprise Manager" guide](./#adding-databases-to-mariadb-enterprise-manager) for the specific steps to generate the linking command.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
