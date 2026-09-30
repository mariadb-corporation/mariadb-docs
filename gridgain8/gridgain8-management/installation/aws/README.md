---
description: >-
  Options for deploying GridGain on Amazon Web Services, including prebuilt AMIs,
  manual EC2 installation, Terraform, and multi-availability-zone setups.
---

# AWS

This section describes the options for deploying GridGain on Amazon Web Services (AWS).

{% columns %}
{% column %}
{% content-ref url="manual-install-on-ec2.md" %}
[Manual Install on Amazon EC2](manual-install-on-ec2.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A step-by-step guide to running a GridGain cluster on Amazon EC2: launching instances, configuring security groups, discovery, and connecting clients.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gridgain-marketplace-ami.md" %}
[GridGain AMI](gridgain-marketplace-ami.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to select, obtain, and launch the GridGain AMI from AWS Marketplace, provide a license, configure IAM roles, and set up node discovery on EC2.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gridgain-ami.md" %}
[Legacy GridGain AMI](gridgain-ami.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to obtain and launch the legacy GridGain AMI with GridGain Enterprise Edition preinstalled on Amazon EC2.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="terraform.md" %}
[Terraform Deployment](terraform.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to provision a GridGain cluster on AWS using the GridGain Terraform AWS module and the GridGain Marketplace AMI.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="multiple-availability-zone-aws.md" %}
[Multiple Availability Zones](multiple-availability-zone-aws.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to deploy GridGain across multiple AWS availability zones using EKS auto scaling groups and an affinity backup filter.
{% endcolumn %}
{% endcolumns %}
