---
title: Deployment
description: >-
  Decide how much of the database you want to run yourself, then install MariaDB from packages, run it in containers or on Kubernetes, or launch it on MariaDB Cloud.
icon: cloud-arrow-up
---

# Deployment

Where MariaDB runs in production mostly depends on how much of the database you want to look after. Some teams run MariaDB Community Server on machines they already manage. Others want MariaDB Enterprise Platform, with tested components and a support contract behind it. Still others would rather MariaDB Cloud handled the hardware, upgrades, and backups.

It's the same server in all three, so your schema and SQL carry over if you change your mind. Plenty of teams prototype on MariaDB Server, launch on MariaDB Cloud, and adopt MariaDB Enterprise Platform later without touching application code.

## Ways to Run MariaDB

Each page covers what running that option involves day to day.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MariaDB Server</strong></td><td>Run the open source server yourself, on hardware or cloud instances you already operate.</td><td><a href="readme/community-server.md">community-server.md</a></td></tr><tr><td><strong>MariaDB Enterprise Platform</strong></td><td>Run MariaDB Enterprise Server with MaxScale, clustering, and analytics, tested together and covered by a support contract.</td><td><a href="readme/enterprise-platform.md">enterprise-platform.md</a></td></tr><tr><td><strong>MariaDB Cloud</strong></td><td>Let the service handle hardware, upgrades, backups, and failover while you work on the application.</td><td><a href="readme/cloud.md">cloud.md</a></td></tr></tbody></table>

## Install and Run

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Install From Packages</strong></td><td>Install MariaDB Server on Linux, Windows, or macOS.</td><td><a href="{server}/mariadb-quickstart-guides/installing-mariadb-server-guide">installing-mariadb-server-guide</a></td></tr><tr><td><strong>MariaDB Package Repository</strong></td><td>Set up the repository so installs and upgrades come from a known, current source.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage">mariadb-package-repository-setup-and-usage</a></td></tr><tr><td><strong>Run in Docker</strong></td><td>Run the official MariaDB image, with volumes and configuration for real use.</td><td><a href="{server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/installing-and-using-mariadb-via-docker">installing-and-using-mariadb-via-docker</a></td></tr><tr><td><strong>Kubernetes With Helm</strong></td><td>Install the MariaDB Enterprise Kubernetes Operator and manage MariaDB as custom resources.</td><td><a href="{tools}/mariadb-enterprise-operator/installation/helm">helm</a></td></tr><tr><td><strong>Kubernetes on OpenShift</strong></td><td>Install the operator on OpenShift, where the security context and steps differ.</td><td><a href="{tools}/mariadb-enterprise-operator/installation/openshift">openshift</a></td></tr><tr><td><strong>Launch on MariaDB Cloud</strong></td><td>Start a Serverless or Provisioned database from the MariaDB Cloud portal.</td><td><a href="{mariadb-cloud}/quickstart/using-the-portal">using-the-portal</a></td></tr></tbody></table>

## Automate and Scale Out

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MariaDB Cloud With Terraform</strong></td><td>Provision and manage MariaDB Cloud databases as infrastructure as code.</td><td><a href="{mariadb-cloud}/quickstart/launch-db-using-the-terraform-provider">launch-db-using-the-terraform-provider</a></td></tr><tr><td><strong>MariaDB on Amazon RDS</strong></td><td>What to expect when you run MariaDB Server on Amazon RDS.</td><td><a href="{server}/server-management/install-and-upgrade-mariadb/mariadb-on-amazon-rds">mariadb-on-amazon-rds</a></td></tr><tr><td><strong>MariaDB Enterprise Manager</strong></td><td>Monitor and administer many servers from one console, where deployment hands off to operations.</td><td><a href="{tools}/mariadb-enterprise-manager">mariadb-enterprise-manager</a></td></tr></tbody></table>
