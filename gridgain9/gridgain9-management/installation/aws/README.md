---
description: >-
  Deploy GridGain 9 on Amazon Web Services using the GridGain 9 AMI or the
  GridGain Terraform module.
---

# AWS

This section describes how to deploy GridGain 9 on Amazon Web Services. You can launch the preinstalled GridGain 9 AMI directly, or provision a full cluster and its supporting infrastructure with the GridGain Terraform module.

{% columns %}
{% column %}
{% content-ref url="gridgain-ami.md" %}
[GridGain 9 AMI](gridgain-ami.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Launch GridGain 9 on AWS from the preinstalled AMI, including instance sizing, security groups, IAM roles, and node discovery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="terraform.md" %}
[Terraform Deployment](terraform.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provision a GridGain 9 cluster and its supporting AWS infrastructure with the GridGain Terraform module.
{% endcolumn %}
{% endcolumns %}
