---
title: Deployment
description: >-
  Get MariaDB running on real infrastructure. Install from packages, deploy on
  Kubernetes with the operator, or run it as a managed cloud service.
icon: cloud-arrow-up
---

# Deployment

Deployment is the step between a database that works on your laptop and one that serves an application in production. How you deploy depends on where the database runs. You can install it from packages on a server you manage, run it on Kubernetes through the MariaDB Enterprise Operator, or let MariaDB Cloud run it for you. This page collects the starting point for each path, so you can pick the one that matches your infrastructure rather than reading three sets of instructions to find the one that applies.

The most direct route is to install the server from the MariaDB package repository onto a machine you control. The installation guide covers the supported operating systems and the steps to get a running server, and the package repository guide covers configuring that repository so installs and upgrades come from a known, verifiable source. Setting up the repository first is worth the few extra minutes, because it is what lets you upgrade cleanly later instead of reinstalling from scratch.

If you run workloads on Kubernetes, you deploy the database as part of the cluster rather than on a separate machine. The MariaDB Enterprise Operator provisions and manages MariaDB as a set of custom resources, so the database is described in the same manifests as the rest of your application and reconciled the same way. The Helm guide installs the operator on a standard Kubernetes cluster, and the OpenShift guide covers the platform specific steps for a Red Hat OpenShift cluster, which differ enough to warrant their own path.

If you would rather not run servers at all, MariaDB Cloud provisions and operates the database for you. The portal quickstart takes you from an account to a running database in a few steps, with the hardware, patching, and backups handled by the service. If your infrastructure is on Amazon and you want a managed MariaDB there instead, the Amazon RDS guide covers running the database on that platform.

Once you run more than one server, the next need is a way to see and manage them together. Enterprise Manager gives you a single console to monitor and administer a fleet of servers, which is the point where deployment turns into operations.

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
