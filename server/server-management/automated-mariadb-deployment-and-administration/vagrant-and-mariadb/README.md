---
description: >-
  Vagrant is an open source tool to quickly setup machines that can be used for
  development and testing. They can be local virtual machines, Docker
  containers, AWS EC2 instances, and so on
---

# Vagrant and MariaDB

{% columns %}
{% column %}
{% content-ref url="creating-a-vagrantfile.md" %}
[creating-a-vagrantfile.md](creating-a-vagrantfile.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide on creating and configuring a `Vagrantfile` to define the characteristics of a MariaDB virtual machine, including box selection and provisioning steps.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vagrant-overview-for-mariadb-users.md" %}
[vagrant-overview-for-mariadb-users.md](vagrant-overview-for-mariadb-users.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to Vagrant's workflow and terminology for database administrators, explaining how it simplifies the creation of reproducible MariaDB development environments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vagrant-security-concerns.md" %}
[vagrant-security-concerns.md](vagrant-security-concerns.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discusses security considerations when using Vagrant with MariaDB, such as default insecure keys, port forwarding risks, and ensuring production-grade settings are not used in dev boxes.
{% endcolumn %}
{% endcolumns %}
