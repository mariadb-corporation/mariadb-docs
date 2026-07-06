---
description: >-
  General information and hints on how to automate MariaDB deployments and
  configuration with Puppet, an open source tool for deployment, configuration,
  and operations.
---

# Puppet and MariaDB

{% columns %}
{% column %}
{% content-ref url="puppet-overview-for-mariadb-users.md" %}
[puppet-overview-for-mariadb-users.md](puppet-overview-for-mariadb-users.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to Puppet's architecture (agent-master vs. standalone), concepts like manifests and catalogs, and how it can be used for configuration management of MariaDB servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="deploying-docker-containers-with-puppet.md" %}
[deploying-docker-containers-with-puppet.md](deploying-docker-containers-with-puppet.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to managing Docker container lifecycles using Puppet's `docker` resource type, covering image pulling, container execution, and upgrades for MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="existing-puppet-modules-for-mariadb.md" %}
[existing-puppet-modules-for-mariadb.md](existing-puppet-modules-for-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists available Puppet modules for MariaDB from the Puppet Forge and GitHub, noting that while no official module exists, community and generic MySQL modules are often used.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="puppet-hiera-configuration-system.md" %}
[puppet-hiera-configuration-system.md](puppet-hiera-configuration-system.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to use Hiera, Puppet's hierarchical key/value lookup tool, to separate MariaDB configuration data from code and manage environment-specific settings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bolt-examples.md" %}
[bolt-examples.md](bolt-examples.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Demonstrates how to use Bolt, an orchestration tool in the Puppet ecosystem, to run ad-hoc commands, scripts, and tasks on remote MariaDB servers without a permanent agent.
{% endcolumn %}
{% endcolumns %}
