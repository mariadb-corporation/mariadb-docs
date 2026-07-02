---
description: >-
  Provides general information and resources for using Ansible to automate the
  deployment and configuration of MariaDB servers using playbooks.
---

# Ansible and MariaDB

{% columns %}
{% column %}
{% content-ref url="ansible-overview-for-mariadb-users.md" %}
[ansible-overview-for-mariadb-users.md](ansible-overview-for-mariadb-users.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to core Ansible concepts such as inventories, playbooks, and roles, with specific examples of how to structure them for MariaDB deployments like Galera Clusters and replicas.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="deploying-docker-containers-with-ansible.md" %}
[deploying-docker-containers-with-ansible.md](deploying-docker-containers-with-ansible.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to use Ansible's Docker modules to automate the deployment and configuration of MariaDB containers, serving as an alternative to Docker Compose.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="deploying-to-remote-servers-with-ansible.md" %}
[deploying-to-remote-servers-with-ansible.md](deploying-to-remote-servers-with-ansible.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to executing Ansible commands and playbooks on remote servers via SSH, covering basic connectivity tests (ping) and the application of roles to specific host groups.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="existing-ansible-modules-and-roles-for-mariadb.md" %}
[existing-ansible-modules-and-roles-for-mariadb.md](existing-ansible-modules-and-roles-for-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Lists and describes the standard Ansible modules available for managing MariaDB, such as `mysql_db`, `mysql_user`, and `mysql_variables`, highlighting their idempotent nature.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-mariadb-deb-files-with-ansible.md" %}
[installing-mariadb-deb-files-with-ansible.md](installing-mariadb-deb-files-with-ansible.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Detailed instructions for automating the installation of MariaDB on Debian/Ubuntu systems, including tasks for adding repositories, importing GPG keys, and installing packages.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="managing-secrets-in-ansible.md" %}
[managing-secrets-in-ansible.md](managing-secrets-in-ansible.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Best practices for handling sensitive information like database passwords and SSH keys within Ansible, recommending the use of `ansible-vault` to encrypt secrets.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="running-mariadb-tzinfo-to-sql-with-ansible.md" %}
[running-mariadb-tzinfo-to-sql-with-ansible.md](running-mariadb-tzinfo-to-sql-with-ansible.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Demonstrates how to automate the loading of time zone data into MariaDB using the `mysql_tzinfo_to_sql` utility, with techniques to ensure the task is idempotent.
{% endcolumn %}
{% endcolumns %}
