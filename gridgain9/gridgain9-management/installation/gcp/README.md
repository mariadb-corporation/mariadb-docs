---
description: >-
  Deploy GridGain 9 on Google Cloud Platform using the GridGain 9 GCP OS image
  or the GridGain Terraform module.
---

# GCP

This section describes how to deploy GridGain 9 on Google Cloud Platform. You can launch the preinstalled GridGain 9 OS image directly, or provision a full cluster and its supporting infrastructure with the GridGain Terraform module.

{% columns %}
{% column %}
{% content-ref url="gridgain-image.md" %}
[GridGain 9 GCP OS Image](gridgain-image.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Launch GridGain 9 on Google Cloud Platform from the preinstalled OS image, including instance sizing, OS Login, IAM roles, firewall rules, and discovery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="terraform.md" %}
[Terraform Deployment](terraform.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provision a GridGain 9 cluster and its supporting GCP infrastructure with the GridGain Terraform module.
{% endcolumn %}
{% endcolumns %}
