---
title: MariaDB Platform
description: >-
  Install MariaDB Enterprise Server, put MariaDB MaxScale in front of it, and find the MariaDB Enterprise Platform components for routing, clustering, analytics, and management.
icon: layer-group
---

# MariaDB Platform

MariaDB Enterprise Platform is MariaDB Enterprise Server plus a set of components that MariaDB tests together. MariaDB MaxScale routes queries, Galera Cluster replicates synchronously, ColumnStore and Exa handle analytics, and GridGain adds in-memory caching. MariaDB Enterprise Manager and the MariaDB Enterprise Kubernetes Operator cover day-to-day operations. The landing page ended with a Python script that queries the `shop.products` table on one MariaDB Community Server. Here you swap that server for MariaDB Enterprise Server and put MaxScale between it and your application, which is the core of most MariaDB Enterprise Platform deployments.

## Run MariaDB Enterprise Server Behind MaxScale

These steps build a single-node test setup on Debian or Ubuntu. On RHEL, Rocky Linux, or AlmaLinux, use `dnf install` in place of `apt install`.

{% stepper %}
{% step %}
### Install MariaDB Enterprise Server

Copy your Customer Download Token from [the customer download page](https://customers.mariadb.com/downloads/token/). The `mariadb_es_repo_setup` script uses the token to configure the MariaDB Enterprise Server, MaxScale, and Enterprise Tools repositories in one pass.

```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
chmod +x mariadb_es_repo_setup
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-server-version="11.8"

sudo apt update
sudo apt install mariadb-server mariadb-backup
```

[MariaDB Package Repository Setup and Usage]({server}/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage) shows how to verify the script's checksum before you run it, and lists the other options it takes.
{% endstep %}

{% step %}
### Put MaxScale in Front

Install MaxScale from the repository that the script configured with `sudo apt install maxscale`. Then open the `mariadb` client with `sudo mariadb` and create an account that MaxScale uses to monitor the server and read user accounts:

```sql
CREATE USER 'maxscale' IDENTIFIED BY 'maxscale_passwd';
GRANT ALL PRIVILEGES ON *.* TO 'maxscale';
```

The broad grant keeps the test setup short. Next, give the `/etc/maxscale.cnf` file a server, a monitor, a read/write split service, and a listener on port 4006:

```ini
[server1]
type=server
address=127.0.0.1
port=3306

[MariaDB-Monitor]
type=monitor
module=mariadbmon
servers=server1
user=maxscale
password=maxscale_passwd
monitor_interval=2s

[Read-Write-Service]
type=service
router=readwritesplit
cluster=MariaDB-Monitor
user=maxscale
password=maxscale_passwd

[Read-Write-Listener]
type=listener
service=Read-Write-Service
port=4006
```

The [MaxScale beginner guide]({maxscale}/maxscale-quickstart-guides/maxscale-beginner-guide) explains each section and adds replicas to the service.
{% endstep %}

{% step %}
### Check the Topology

Start MaxScale and ask the `maxctrl` command-line client which servers it sees:

```bash
sudo systemctl start maxscale
maxctrl list servers

mariadb -h127.0.0.1 -P4006 -umaxscale -p -e "SELECT @@server_id"
```

The `server1` row should show the state `Master, Running`. If it shows `Down`, the log at `/var/log/maxscale/maxscale.log` says why. Your application now connects to port 4006, so point the Python script from the landing page at that port and an account whose host pattern allows connections from MaxScale. Once you add replicas, the [ReadWriteSplit router]({maxscale}/reference/maxscale-routers/maxscale-readwritesplit) sends reads to them and keeps writes on the primary.
{% endstep %}
{% endstepper %}

## Get Your Bearings

Read how the components fit together, then set up security before real data arrives.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Platform Overview</strong></td><td>The MariaDB Enterprise Platform components and how they work together.</td><td><a href="{platform}/mariadb-platform-quickstart-guides/mariadb-overview-guide">mariadb-overview-guide</a></td></tr><tr><td><strong>Best Practices</strong></td><td>Backups, change management, and the habits that keep a production deployment healthy.</td><td><a href="{platform}/mariadb-platform-quickstart-guides/mariadb-best-practices-guide">mariadb-best-practices-guide</a></td></tr><tr><td><strong>Security</strong></td><td>Lock down accounts, network access, and encryption from the start.</td><td><a href="{platform}/mariadb-platform-quickstart-guides/security">security</a></td></tr></tbody></table>

## Route and Scale

Galera Cluster behind MaxScale is a common production topology, because MaxScale turns a failed node into a routing change.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MaxScale Quickstart</strong></td><td>Route queries, split reads from writes, and handle failover in front of your servers.</td><td><a href="{maxscale}/maxscale-quickstart-guides/maxscale-beginner-guide">maxscale-beginner-guide</a></td></tr><tr><td><strong>Galera Cluster Quickstart</strong></td><td>Set up synchronous replication where every node can take writes.</td><td><a href="{galera}/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide">mariadb-galera-cluster-guide</a></td></tr><tr><td><strong>Kubernetes Operator</strong></td><td>Run MariaDB Enterprise Server and MaxScale on Kubernetes as custom resources.</td><td><a href="{tools}/mariadb-enterprise-operator/installation/helm">helm</a></td></tr></tbody></table>

## Analyze and Manage

ColumnStore and Exa run on MariaDB Enterprise Server, and MariaDB Enterprise Manager watches the whole deployment.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>ColumnStore Quickstart</strong></td><td>Answer analytical queries from a columnar storage engine next to your transactional tables.</td><td><a href="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide">mariadb-columnstore-guide</a></td></tr><tr><td><strong>Deploy MariaDB Exa</strong></td><td>Spread the largest analytical workloads across a cluster.</td><td><a href="{analytics}/mariadb-exa/deployment">deployment</a></td></tr><tr><td><strong>MariaDB Enterprise Manager</strong></td><td>Monitor and administer your servers and MaxScale instances from one console.</td><td><a href="{tools}/mariadb-enterprise-manager">mariadb-enterprise-manager</a></td></tr></tbody></table>
