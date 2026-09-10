---
title: Deployment
description: >-
  Get MariaDB running where your application lives. Install from packages, run
  it on Kubernetes with the operator, or launch it as a managed cloud service.
icon: cloud-arrow-up
---

# Deployment

Take MariaDB from your laptop to real infrastructure. Where you deploy is your call: install it straight onto servers you manage, run it on Kubernetes as part of your cluster, or let MariaDB Cloud run it for you. Pick the path that matches where your application already lives, and start there.

Every path runs the same MariaDB, so the database behaves the same whether it sits on a virtual machine, in a container, or behind the managed service. What differs is who handles the machines and the upgrades, and how much of that you want to own. Match that to your team and your infrastructure, and the rest follows.

**Install from packages.** The direct route is to install the server from the MariaDB package repository onto a machine you control. Set up the repository first so your installs and upgrades come from a known, verifiable source, then install the server with the platform commands in the guide. This is the path most self managed deployments take, and it is the foundation the others build on.

**Run it on Kubernetes.** If your workloads run on Kubernetes, deploy the database the same way you deploy everything else. The MariaDB Enterprise Operator provisions and manages MariaDB as custom resources, described in your manifests and reconciled by the cluster. Install the operator with Helm on a standard cluster, or follow the OpenShift path for a Red Hat cluster, where the steps differ enough to warrant their own guide.

**Launch it managed.** If you would rather not run servers at all, let MariaDB Cloud provision and operate the database. The portal quickstart gets you to a running database in a few steps. Already on Amazon and want a managed MariaDB there? The Amazon RDS guide covers that route.

**Manage the fleet.** Once you run more than one server, Enterprise Manager gives you a single console to monitor and administer them, which is where deployment turns into operations.

Choose the path that fits your infrastructure, and you will have MariaDB running where you need it.

## Install from packages

{% content-ref url="{server}/mariadb-quickstart-guides/installing-mariadb-server-guide" %}
[Install MariaDB Server]({server}/mariadb-quickstart-guides/installing-mariadb-server-guide)
{% endcontent-ref %}

{% content-ref url="{server}/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage" %}
[Package Repository Setup and Usage]({server}/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage)
{% endcontent-ref %}

## Deploy on Kubernetes

{% content-ref url="{tools}/mariadb-enterprise-operator/installation/helm" %}
[Install the Operator with Helm]({tools}/mariadb-enterprise-operator/installation/helm)
{% endcontent-ref %}

{% content-ref url="{tools}/mariadb-enterprise-operator/installation/openshift" %}
[Install the Operator on OpenShift]({tools}/mariadb-enterprise-operator/installation/openshift)
{% endcontent-ref %}

## Run it as a managed service

{% content-ref url="{mariadb-cloud}/quickstart/using-the-portal" %}
[Launch MariaDB Cloud Using the Portal]({mariadb-cloud}/quickstart/using-the-portal)
{% endcontent-ref %}

{% content-ref url="{server}/server-management/install-and-upgrade-mariadb/mariadb-on-amazon-rds" %}
[MariaDB on Amazon RDS]({server}/server-management/install-and-upgrade-mariadb/mariadb-on-amazon-rds)
{% endcontent-ref %}

## Manage a fleet

{% content-ref url="{tools}/mariadb-enterprise-manager" %}
[MariaDB Enterprise Manager]({tools}/mariadb-enterprise-manager)
{% endcontent-ref %}
