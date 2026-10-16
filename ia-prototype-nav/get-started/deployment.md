---
title: Deployment
description: >-
  Choose how much of the database you run yourself, then move MariaDB Server from a laptop experiment to a real server with packages, Docker, or Kubernetes.
icon: cloud-arrow-up
---

# Deployment

The `shop.products` table from the landing page works fine on a laptop. Before it holds real orders, decide how much of the database you want to look after yourself. It's the same MariaDB Server underneath every option, so your schema, SQL, and Python code carry over if you change your mind later.

## Decide Who Runs the Database

Each page explains what that option involves day to day, from patching to support.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MariaDB Community Server</strong></td><td>Run the open source server yourself, on hardware or cloud instances you already operate.</td><td><a href="readme/community-server.md">community-server.md</a></td></tr><tr><td><strong>MariaDB Enterprise Platform</strong></td><td>Run MariaDB Enterprise Server with MaxScale, clustering, and analytics, tested together and backed by a support contract.</td><td><a href="readme/enterprise-platform.md">enterprise-platform.md</a></td></tr><tr><td><strong>MariaDB Cloud</strong></td><td>Hand hardware, upgrades, backups, and failover to the managed service and keep your attention on the application.</td><td><a href="readme/cloud.md">cloud.md</a></td></tr></tbody></table>

## From a Laptop to a Real Server

If you run the server yourself, these three steps give you a current release, started as a service, with an application account that can't do more than it needs to.

{% stepper %}
{% step %}
### Add the MariaDB Package Repository

Distribution packages often lag a few releases behind. The `mariadb_repo_setup` script configures your package manager to install MariaDB Community Server from MariaDB's own repository. Download it, check it against the checksum published on the repository setup page (replace `<checksum>` below), and run it:

```bash
curl -LsSO https://r.mariadb.com/downloads/mariadb_repo_setup
echo "<checksum> mariadb_repo_setup" | sha256sum -c -
chmod +x mariadb_repo_setup
sudo ./mariadb_repo_setup
```

To stay on one release series, add `--mariadb-server-version="mariadb-11.8"`. Going with Docker or Kubernetes? Skip this step, because the images already carry the server. [MariaDB Package Repository Setup and Usage]({server}/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage) lists the checksums and every script option.
{% endstep %}

{% step %}
### Install and Start the Server

Pick the tab that matches where the server runs.

{% tabs %}
{% tab title="Debian / Ubuntu" %}
```bash
sudo apt update
sudo apt install mariadb-server mariadb-client mariadb-backup
sudo systemctl status mariadb
```

The package starts the `mariadb` service on install, so the status check confirms it's running.
{% endtab %}

{% tab title="RHEL family" %}
```bash
sudo dnf install MariaDB-server MariaDB-client MariaDB-backup
sudo systemctl enable --now mariadb
```

Packages from the MariaDB repository use capitalized names (`MariaDB-server`), unlike the distribution's own `mariadb-server`.
{% endtab %}

{% tab title="Docker" %}
```bash
docker run --detach --name mariadb \
  --publish 3306:3306 \
  --env MARIADB_ROOT_PASSWORD=changeme \
  --env MARIADB_DATABASE=shop \
  --env MARIADB_USER=app \
  --env MARIADB_PASSWORD=app-secret \
  --volume mariadb-data:/var/lib/mysql \
  mariadb:lts
```

The `mariadb-data` volume keeps the data directory when you replace the container. On first start, the image creates the `shop` database and gives the `app` user full privileges on it. [Docker Official Image Environment Variables]({server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/mariadb-server-docker-official-image-environment-variables) lists the rest.
{% endtab %}

{% tab title="Kubernetes" %}
The MariaDB Enterprise Kubernetes Operator is part of MariaDB Enterprise Platform, and it pulls images with your customer credentials. Set those up first, then install the operator from its two Helm charts:

```bash
helm repo add mariadb-enterprise-operator https://operator.mariadb.com
helm install mariadb-enterprise-operator-crds \
  mariadb-enterprise-operator/mariadb-enterprise-operator-crds
helm install mariadb-enterprise-operator \
  mariadb-enterprise-operator/mariadb-enterprise-operator \
  -f values.yaml
```

The `values.yaml` file names the `mariadb-enterprise` pull secret. Next, store the database password in a Kubernetes `Secret`, then describe the server as a `MariaDB` custom resource and apply it with `kubectl apply -f mariadb.yaml`:

```bash
kubectl create secret generic mariadb --from-literal=password=app-secret
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
  rootPasswordSecretKeyRef:
    name: mariadb
    key: password
  imagePullSecrets:
    - name: mariadb-enterprise
  username: app
  passwordSecretKeyRef:
    name: mariadb
    key: password
  database: shop
  storage:
    size: 1Gi
  replicas: 1
```

[Install the operator with Helm]({tools}/mariadb-enterprise-operator/installation/helm) covers `values.yaml`, and the [standalone topology]({tools}/mariadb-enterprise-operator/topologies/standalone) page covers the rest of the `MariaDB` resource.
{% endtab %}
{% endtabs %}

[The installation guide]({server}/mariadb-quickstart-guides/installing-mariadb-server-guide) also covers Windows and macOS.
{% endstep %}

{% step %}
### Secure It and Create an Application User

On a package install, run the `mariadb-secure-installation` script. It walks you through setting a root password, removing root accounts reachable from other hosts, removing anonymous users, and dropping the `test` database.

```bash
sudo mariadb-secure-installation
```

Then connect with `sudo mariadb` and create an account for the application, limited to the `shop` database and to the subnet your application servers use:

```sql
CREATE USER 'app'@'10.0.0.%' IDENTIFIED BY 'app-secret';
GRANT SELECT, INSERT, UPDATE, DELETE ON shop.* TO 'app'@'10.0.0.%';
```

The Docker and Kubernetes tabs already created the `app` user, so there you only narrow its privileges if you need to. [CREATE USER]({server}/reference/sql-statements/account-management-sql-statements/create-user) and [GRANT]({server}/reference/sql-statements/account-management-sql-statements/grant) cover host patterns, roles, and TLS requirements.
{% endstep %}
{% endstepper %}

## Go Further With Your Install

Each of these pages picks up where a tab above stops.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Install From Packages</strong></td><td>Install MariaDB Server on Linux, Windows, or macOS, and check the service afterward.</td><td><a href="{server}/mariadb-quickstart-guides/installing-mariadb-server-guide">installing-mariadb-server-guide</a></td></tr><tr><td><strong>Run in Docker</strong></td><td>Run the official MariaDB image with volumes, configuration files, and initialization scripts.</td><td><a href="{server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/installing-and-using-mariadb-via-docker">installing-and-using-mariadb-via-docker</a></td></tr><tr><td><strong>Container Cheat Sheet</strong></td><td>Common <code>docker run</code> patterns for networks, users, and mounted configuration.</td><td><a href="{server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/mariadb-container-cheat-sheet">mariadb-container-cheat-sheet</a></td></tr><tr><td><strong>Kubernetes With Helm</strong></td><td>Install, upgrade, and remove the MariaDB Enterprise Kubernetes Operator charts.</td><td><a href="{tools}/mariadb-enterprise-operator/installation/helm">helm</a></td></tr><tr><td><strong>Kubernetes on OpenShift</strong></td><td>Install the operator on OpenShift, where the security context and steps differ.</td><td><a href="{tools}/mariadb-enterprise-operator/installation/openshift">openshift</a></td></tr><tr><td><strong>Launch on MariaDB Cloud</strong></td><td>Start a Serverless or Provisioned database from the MariaDB Cloud portal.</td><td><a href="{mariadb-cloud}/quickstart/using-the-portal">using-the-portal</a></td></tr></tbody></table>

## Automate and Manage at Scale

Once one server works, script the next ones and watch them from one place.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MariaDB Cloud With Terraform</strong></td><td>Provision and change MariaDB Cloud databases as infrastructure as code.</td><td><a href="{mariadb-cloud}/quickstart/launch-db-using-the-terraform-provider">launch-db-using-the-terraform-provider</a></td></tr><tr><td><strong>MariaDB on Amazon RDS</strong></td><td>What to expect when you run MariaDB Server on Amazon RDS.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/mariadb-on-amazon-rds">mariadb-on-amazon-rds</a></td></tr><tr><td><strong>MariaDB Enterprise Manager</strong></td><td>Monitor and administer many servers from one console, where deployment hands off to operations.</td><td><a href="{tools}/mariadb-enterprise-manager">mariadb-enterprise-manager</a></td></tr></tbody></table>
