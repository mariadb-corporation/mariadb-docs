---
description: >-
  Options for deploying GridGain on Amazon Web Services, including manual EC2
  installation and multi-availability-zone setups.
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
{% content-ref url="multiple-availability-zone-aws.md" %}
[Multiple Availability Zones](multiple-availability-zone-aws.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to deploy GridGain across multiple AWS availability zones using EKS auto scaling groups and an affinity backup filter.
{% endcolumn %}
{% endcolumns %}
