---
title: Deployment
description: >-
  Get MariaDB running where your application lives. Install from packages, run
  it on Kubernetes with the operator, or launch it as a managed cloud service.
icon: cloud-arrow-up
---

# Deployment

Deploying MariaDB means choosing where the database runs and who maintains the machines under it. You can install it onto servers you manage, run it on Kubernetes alongside the rest of your workloads, or let MariaDB Cloud operate it. All three run the same server, so the database behaves the same on a virtual machine, in a container, or behind the managed service.

What changes between the paths is the operational surface you own: the host, the operating system patches, the upgrade windows, and the failover drill. Match that to your team and to where your application already runs.

**Install from packages.** The direct route is to install MariaDB Server from the MariaDB package repository onto a machine you control. Configure the repository first so installs and upgrades come from a known, verifiable source, then install the server using the commands for your platform. Most self managed deployments take this path, and it is the foundation the others build on.

**Run it on Kubernetes.** The MariaDB Enterprise Operator provisions and manages MariaDB Enterprise Server and MaxScale as custom resources, declared in your manifests and reconciled by the cluster. Install the operator with Helm on a standard cluster. OpenShift has its own guide, because the security context and install steps differ.

**Launch it managed.** MariaDB Cloud provisions and operates the database for you. The portal quickstart reaches a running database in a few steps. To run a managed MariaDB Server on Amazon instead, the Amazon RDS guide covers that route and its differences.

**Manage more than one.** Once you operate a fleet, Enterprise Manager gives you one console for monitoring and administering the servers, which is where deployment hands off to operations.

Choose the path that matches your existing infrastructure, then install the server and confirm you can connect to it.

## Install From Packages

{% content-ref url="explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/installing-mariadb-server-guide/" %}
[installing-mariadb-server-guide](explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/installing-mariadb-server-guide/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage/" %}
[mariadb-package-repository-setup-and-usage](explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage/)
{% endcontent-ref %}

## Deploy on Kubernetes

{% content-ref url="explore-by-task/%7Btools%7D/mariadb-enterprise-operator/installation/helm/" %}
[helm](explore-by-task/%7Btools%7D/mariadb-enterprise-operator/installation/helm/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Btools%7D/mariadb-enterprise-operator/installation/openshift/" %}
[openshift](explore-by-task/%7Btools%7D/mariadb-enterprise-operator/installation/openshift/)
{% endcontent-ref %}

## Run It as a Managed Service

{% content-ref url="explore-by-task/%7Bmariadb-cloud%7D/quickstart/using-the-portal/" %}
[using-the-portal](explore-by-task/%7Bmariadb-cloud%7D/quickstart/using-the-portal/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/mariadb-on-amazon-rds/" %}
[mariadb-on-amazon-rds](explore-by-task/%7Bserver%7D/server-management/install-and-upgrade-mariadb/mariadb-on-amazon-rds/)
{% endcontent-ref %}

## Manage a Fleet

{% content-ref url="explore-by-task/%7Btools%7D/mariadb-enterprise-manager/" %}
[mariadb-enterprise-manager](explore-by-task/%7Btools%7D/mariadb-enterprise-manager/)
{% endcontent-ref %}
