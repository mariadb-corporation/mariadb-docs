---
description: >-
  MariaDB Exa deployment options and the production install order: configure
  MariaDB Server, install Exasol (local storage or AWS S3), then connect MariaDB
  MaxScale with CDC.
icon: wrench
---

# Deployment

In production, MariaDB Exa is deployed as a Massively Parallel Processing (MPP) cluster of nodes.

* Optional standby nodes for high availability.

Data is automatically distributed across nodes, using MariaDB Exa internal partitioning and replication for fault tolerance.

## Production Install

A complete MariaDB Exa deployment has three parts. Install and configure them in the following order.

1. [Install and configure MariaDB Server](deployment.md#id-1.-install-and-configure-mariadb-server)
2. [Install and configure Exasol](deployment.md#id-2.-install-and-configure-exasol) — local storage (single node) or AWS S3 (clustered)
3. [Install and configure MariaDB MaxScale with CDC](deployment.md#id-3.-install-and-configure-mariadb-maxscale-with-cdc)

### 1. Install and configure MariaDB Server

MariaDB Server is the transactional front end for the deployment. Install it and apply your baseline configuration first.

* [Installing MariaDB Server Guide](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/installing-mariadb-server-guide)
* [Configuring MariaDB with Option Files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files)

### 2. Install and configure Exasol

MariaDB Exa supports two deployment modes. Choose the one that fits your environment, then follow the steps below — the procedure is the same except where a step shows separate **Local storage** and **AWS S3** tabs.

* **Local storage (single node)** — the simplest install, using local disk on a single host. Suitable for development, evaluation, and smaller workloads.
* **AWS S3 (clustered)** — a multi-node cluster on AWS, deployed through CloudFormation with S3-backed storage and high availability (five nodes by default: four active plus one standby). Although written for AWS, the same C4 workflow applies to other clouds or on-premises by changing the arguments in `.ccc/config`.

{% hint style="info" %}
MariaDB Exa is powered by [Exasol](https://www.exasol.com/), and both modes use Exasol's C4 deployment tool. For upstream reference, see Exasol's [on-premise installation guide](https://docs.exasol.com/db/latest/administration/on-premise/installation.htm), [AWS deployment guide](https://docs.exasol.com/db/latest/administration/aws/installation/basic_deployment.htm), and [c4 parameter reference](https://docs.exasol.com/db/latest/administration/on-premise/c4/c4_parameters.htm).
{% endhint %}

**Prerequisites:**

{% tabs %}
{% tab title="Local storage" %}
* Ubuntu 22.04+ or RHEL 8+. Other Linux distributions might work, but are not tested or guaranteed.
* A static public IP address. Without one, the deployment will not work after a restart.
* Open ports: `8563` (default database port) and `8443` (admin UI).
{% endtab %}

{% tab title="AWS S3" %}
* An AWS key pair with permissions for CloudFormation, S3 buckets, EC2 instances, security groups, and subnets.
* Open ports: `8563` (default database port) and `8443` (admin UI).
{% endtab %}
{% endtabs %}

{% stepper %}
{% step %}
#### Prepare the jump host

The jump host runs the C4 installer and operates the cluster. For local storage, this can be the MaxScale machine; for AWS, launch a dedicated EC2 instance in the same VPC and subnet as Exasol.

{% tabs %}
{% tab title="Local storage" %}
SSH to the machine:

```bash
ssh ubuntu@<JUMPHOST_IP>
```
{% endtab %}

{% tab title="AWS S3" %}
In the AWS console, go to **EC2 → AMIs**, search the community images for an Ubuntu AMI (for example `ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-20250821`), and launch an EC2 instance as the jump host in the same VPC and subnet where Exasol will be deployed. Then SSH to it:

```bash
ssh ubuntu@<JUMPHOST_IP>
```

{% hint style="info" %}
You do not have to use this image, but it comes preloaded with some of the required packages.
{% endhint %}
{% endtab %}
{% endtabs %}

Update and install the required packages:

```bash
sudo apt update -y
sudo apt full-upgrade -y
sudo apt install rsync ssh uuid-runtime wget curl git python3-pip byacc flex zip unzip jq -y
sudo apt full-upgrade -y
sudo reboot now
```
{% endstep %}

{% step %}
#### Set up node access

{% tabs %}
{% tab title="Local storage" %}
On your jump host, create an SSH key pair and add the public key to the target instance where you will install Exasol.

```bash
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
```

Add the public key to `authorized_keys`:

```bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

Check the permissions:

```bash
ls -la ~/.ssh/
# if needed: chmod 400 ~/.ssh/<key>.pem
```

Check that SSH works from the jump host to the Exasol node:

```bash
ssh ubuntu@<EXASOL_NODE_IP>
```

{% hint style="info" %}
Confirm that port `20002` is open. You may also need to add the SSH public key to the target's root `authorized_keys`.
{% endhint %}
{% endtab %}

{% tab title="AWS S3" %}
Install and configure the AWS CLI, then verify access:

```bash
sudo apt install awscli -y
sudo snap install aws-cli --channel=v2/stable --classic
```

```bash
aws configure
aws s3 ls
```

Copy your EC2 key pair to the jump host and secure it:

```bash
scp <path>/<key>.pem ubuntu@<JUMPHOST_IP>:/home/ubuntu/
```

```bash
mv <key>.pem ~/.ssh/
chmod 400 ~/.ssh/<key>.pem
```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
#### Download the Exasol C4 installer

{% hint style="warning" %}
Run the C4 installer as a non-`root` user. Installing as `root` is known to cause path-related failures; rootless installs have proven reliable in practice (as of February 2026). Exasol's older docs still describe a root-based default, but their newer versions assume non-root — see Exasol's [rootless deployment](https://docs.exasol.com/db/latest/administration/on-premise/installation/install_rootless.htm) guide.
{% endhint %}

```bash
cd ~
wget https://x-up.s3.amazonaws.com/releases/c4/linux/x86_64/4.28.4/c4 -O c4
chmod +x c4
```

The latest installer is also available from the [Exasol Deployment Tool (c4) download page](https://downloads.exasol.com/exasol-deployment-tool-c4).
{% endstep %}

{% step %}
#### Create the C4 configuration

```bash
mkdir ~/.ccc
vi ~/.ccc/config
```

Paste the configuration for your deployment mode:

{% tabs %}
{% tab title="Local storage" %}
```ini
CCC_HOST_ADDRS=<HOST_PRIVATE_IP>
CCC_HOST_EXTERNAL_ADDRS=<HOST_PUBLIC_IP>
CCC_HOST_DATADISK=/dev/nvme1n1
CCC_HOST_IMAGE_USER=ubuntu
CCC_HOST_IMAGE_PASSWORD=
CCC_HOST_KEY_PAIR_FILE=id_rsa
CCC_PLAY_WORKING_COPY=@exasol-2025.1.8
CCC_PLAY_DATABASE_NAME=exa-analytics
CCC_PLAY_DB_PASSWORD="<DB_PASSWORD>"
CCC_PLAY_ADMIN_PASSWORD="<ADMIN_PASSWORD>"
CCC_ADMINUI_START_SERVER=true
CCC_HOST_CLEANUP=false
```

You must update the following values:

1.  `CCC_HOST_ADDRS` — your private IP address (a static public address is required):

    ```bash
    hostname -i
    ```
2.  `CCC_HOST_EXTERNAL_ADDRS` — your public IP address:

    ```bash
    ifconfig -a
    # or
    curl 'https://api.ipify.org?format=json'
    ```
3.  `CCC_HOST_DATADISK` — find the data disk with:

    ```bash
    lsblk
    ```
4.  `CCC_HOST_IMAGE_USER` — usually `ubuntu` or another default user that exists on both the jump host and the Exasol node:

    ```bash
    whoami
    ```
{% endtab %}

{% tab title="AWS S3" %}
```ini
CCC_USER_EMAIL=<your-email>
CCC_USER_USERNAME=<username>

# These become the root/admin passwords
CCC_PLAY_ADMIN_PASSWORD="<ADMIN_PASSWORD>"
CCC_PLAY_DB_PASSWORD="<DB_PASSWORD>"
CCC_USER_PASSWORD="<USER_PASSWORD>"

# AWS
CCC_AWS_PROFILE=default
CCC_AWS_REGION=us-west-2
CCC_AWS_KEY_PAIR=<key-pair-name>
CCC_AWS_KEY_PAIR_FILE=<key-pair-name>.pem
CCC_AWS_NO_MFA=true

# License
CCC_PLAY_LICENSE=@license:v8-byol

# Cluster topology
CCC_PLAY_ACCESS_NODE=false
CCC_PLAY_RESERVE_NODES=1

# Exasol database parameters
CCC_PLAY_DB_PARAMS='-parallelSessionTokenTimeout=0 -maxProcessHeapMemory=8192 -queryCacheSize=4096 -etlCheckCertsDefault=0 -etlJdbcJavaEnv=-Xmx2048M'

# Exasol version
CCC_PLAY_WORKING_COPY=@exasol-2025.1.2

# Instance type
CCC_AWS_INSTANCE_TYPE=r6idn.4xlarge

# Timeouts
CCC_USER_PS_REMOTE_TIMEOUT=10000
CCC_PLAY_TIMEOUT=60m

# Admin UI
CCC_ADMINUI_START_SERVER=true
CCC_ADMINUI_ADMIN_PASSWORD="<ADMIN_PASSWORD>"
```

Update `CCC_AWS_REGION`, `CCC_AWS_KEY_PAIR`, `CCC_AWS_KEY_PAIR_FILE`, and `CCC_AWS_INSTANCE_TYPE` for your AWS account. Use an analytics-oriented instance family such as `r6i`, `i4i`, or `r7i`.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Set strong, unique values for the password parameters and keep them secret. Do not commit real credentials to source control or share them in documentation.
{% endhint %}
{% endstep %}

{% step %}
#### Validate the environment

{% tabs %}
{% tab title="Local storage" %}
```bash
./c4 ps
```
{% endtab %}

{% tab title="AWS S3" %}
```bash
./c4 aws diag -i .ccc/config
./c4 ps
```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
#### Deploy the Exasol cluster

{% tabs %}
{% tab title="Local storage" %}
```bash
./c4 host play -i .ccc/config
```

View the logs on the target machine:

```bash
tail -f .ccc/play/local/*/main/11/data/logs/cored/exainit.log
```
{% endtab %}

{% tab title="AWS S3" %}
```bash
./c4 aws play -N 5 -T @exasol-2025.1.2 -i .ccc/config
```

* `-N 5` — five nodes total. With `CCC_PLAY_RESERVE_NODES=1`, this gives four active nodes plus one standby.
* For a single node, set `CCC_PLAY_RESERVE_NODES=0` and use `-N 1`.
*   For instance types that exist only in certain availability zones, add the applicable zone to the command:

    ```bash
    --enable-availability-zones "us-west-2b" --availability-zone us-west-2b
    ```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
#### Check the deployment stages

View the status from the jump host (for AWS, you can also monitor progress in AWS CloudFormation):

```bash
./c4 ps
```

| Stage | Meaning                                                                |
| ----- | ---------------------------------------------------------------------- |
| a     | Infrastructure resources are being allocated; nothing is reachable yet |
| b     | The host is booting and running startup scripts                        |
| c     | The cluster operating system (COS) service is running and reachable    |
| d     | The database is running and reachable                                  |

Wait until the deployment is complete. If you encounter errors that you cannot triage yourself, contact support.
{% endstep %}

{% step %}
#### Configure Exasol

On the target machine, use `CCC_PLAY_DB_PASSWORD` from `.ccc/config` (on the jump host) to check the connection to Exasol.

```bash
sudo apt install openjdk-21-jdk
```

```bash
sudo find / -name *exaplus*
```

```bash
exaplus -c 127.0.0.1/nocertcheck:8563 -u sys -p <DB_PASSWORD>
```

{% hint style="info" %}
To retrieve the password from the jump host: `cat .ccc/config | grep -i PLAY_DB`
{% endhint %}

Set `SQL_IDENTIFIER_COMPARISON` to be case insensitive:

```sql
ALTER SYSTEM SET SQL_IDENTIFIER_COMPARISON = 'IGNORE CASE';
```

Import the MariaDB helper functions / UDF from [mariadb-compat.sql](https://github.com/mariadb-corporation/exasol-mariadb-compat/blob/main/dist/mariadb-compat.sql):

```bash
exaplus -c 127.0.0.1/nocertcheck:8563 -u sys -p <DB_PASSWORD> -f mariadb-compat.sql
```
{% endstep %}

{% step %}
#### Upload the Exasol license

Each customer has their own license file.

Copy the license file:

```bash
scp <license_id>.exasol_license ubuntu@<JUMPHOST_IP>:/home/ubuntu/
```

Get `CLUSTER_ID` from the `play_id` column of `./c4 ps`, then upload the license:

```bash
cat <license_id>.exasol_license | ./c4 connect -s cos -i <CLUSTER_ID> -- \
  confd_client license_upload license: '\""{< -}\""'
```

Verify:

```bash
./c4 connect -t1.11/cos
confd_client license_info
```
{% endstep %}

{% step %}
#### Access the admin UI

Open the following in a browser:

```
https://<PUBLIC_IP>:8443/login
```

Use these credentials:

* **Username:** `admin`
* **Password:** the admin password you set (`CCC_PLAY_ADMIN_PASSWORD` for local storage, `CCC_ADMINUI_ADMIN_PASSWORD` for AWS S3).
{% endstep %}

{% step %}
#### Manage the cluster

Common C4 commands for day-to-day operation:

```bash
./c4 ps                # list deployments
./c4 connect -t1/cos   # connect to the cluster
```

Stop and start the database:

{% tabs %}
{% tab title="Local storage" %}
The database name comes from `CCC_PLAY_DATABASE_NAME`.

```bash
./c4 connect -t 1/cos
confd_client db_stop db_name: exa-analytics
confd_client db_start db_name: exa-analytics
```
{% endtab %}

{% tab title="AWS S3" %}
```bash
./c4 down <CLUSTER_ID>   # stop the cluster
./c4 up <CLUSTER_ID>     # start the cluster
```

Show database info:

```bash
confd_client db_info db_name: Exasol
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**AWS best practices:** deploy the jump host in the same VPC as Exasol and treat it as an admin bastion only (no workloads); use S3-backed storage for long-term data and snapshots; and keep at least one reserve node for high availability.
{% endhint %}
{% endstep %}
{% endstepper %}

### 3. Install and configure MariaDB MaxScale with CDC

MariaDB MaxScale uses the ExasolRouter to stream changes from MariaDB Server into Exasol via Change Data Capture (CDC).

* [MariaDB MaxScale ExasolRouter Tutorial](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-tutorials/mariadb-maxscale-exasolrouter)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
