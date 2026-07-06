---
description: >-
  An overview of automation tools and strategies for deploying MariaDB,
  comparing systems like Ansible, Puppet, and Kubernetes, and discussing
  "Infrastructure as Code" principles.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
---

# Automated Deployment & Administration

{% columns %}
{% column %}
{% content-ref url="why-to-automate-mariadb-deployments-and-management.md" %}
[why-to-automate-mariadb-deployments-and-management.md](why-to-automate-mariadb-deployments-and-management.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the benefits of automating database deployment and management, such as consistency, scalability, and the adoption of Infrastructure as Code principles.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="a-comparison-between-automation-systems.md" %}
[a-comparison-between-automation-systems.md](a-comparison-between-automation-systems.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compares different automation tools like Ansible and Puppet, highlighting differences in their architecture (agentless vs. agent-based) and code structure to help users choose the right tool.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="automating-mariadb-tasks-with-events.md" %}
[automating-mariadb-tasks-with-events.md](automating-mariadb-tasks-with-events.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes how to use the MariaDB Event Scheduler to automate recurring SQL tasks directly within the database server, similar to cron jobs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="automating-upgrades-with-mariadborg-downloads-rest-api.md" %}
[automating-upgrades-with-mariadborg-downloads-rest-api.md](automating-upgrades-with-mariadborg-downloads-rest-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide on using the MariaDB Downloads REST API to programmatically retrieve information about software versions, facilitating automated upgrade scripts.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="hashicorp-vault-and-mariadb.md" %}
[hashicorp-vault-and-mariadb.md](hashicorp-vault-and-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discusses the integration of HashiCorp Vault with MariaDB for managing secrets, including using MariaDB as a storage backend for Vault.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="orchestrator-overview.md" %}
[orchestrator-overview.md](orchestrator-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to Orchestrator, a tool for managing MySQL and MariaDB replication topologies, providing high availability and automated failover capabilities.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ansible-and-mariadb/" %}
[ansible-and-mariadb](ansible-and-mariadb/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provides general information and resources for using Ansible to automate the deployment and configuration of MariaDB servers using playbooks.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="automated-mariadb-deployment-and-administration-puppet-and-mariadb/" %}
[automated-mariadb-deployment-and-administration-puppet-and-mariadb](automated-mariadb-deployment-and-administration-puppet-and-mariadb/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
General information and hints on how to automate MariaDB deployments and configuration with Puppet, an open source tool for deployment, configuration, and operations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="docker-and-mariadb/" %}
[docker-and-mariadb](docker-and-mariadb/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discusses running MariaDB in Docker containers, covering the benefits of isolation and ease of deployment for development and testing environments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="kubernetes-and-mariadb/" %}
[kubernetes-and-mariadb](kubernetes-and-mariadb/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
General information and hints on deploying MariaDB Kubernetes (K8s) containers, an open source container orchestration system which automates deployments, horizontal scaling, configuration, and operat
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vagrant-and-mariadb/" %}
[vagrant-and-mariadb](vagrant-and-mariadb/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Vagrant is an open source tool to quickly setup machines that can be used for development and testing. They can be local virtual machines, Docker containers, AWS EC2 instances, and so on
{% endcolumn %}
{% endcolumns %}
