---
description: >-
  Deploy and manage GridGain 9 clusters on Kubernetes with the GridGain
  Kubernetes Operator.
---

# Kubernetes Operator

The GridGain Kubernetes Operator automates the deployment and lifecycle management of GridGain 9 clusters on Kubernetes through the `GridGain9Cluster` custom resource. This section covers installing the operator, configuring clusters, and managing persistence, networking, security, monitoring, and upgrades.

{% hint style="warning" %}
Kubernetes operator is an experimental feature. The configuration may change in a subsequent release.
{% endhint %}

Start with the [Overview](overview.md) for a description of the operator and its managed resources, or jump to the [Quick Start](quick-start.md) to deploy your first cluster.

{% columns %}
{% column %}
{% content-ref url="overview.md" %}
[Overview](overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of the GridGain Kubernetes Operator, the GridGain9Cluster custom resource, and the Kubernetes objects it manages.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="quick-start.md" %}
[Quick Start](quick-start.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install the GridGain Kubernetes Operator, deploy a three-node GridGain 9 cluster, and verify it using the CLI tool.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration.md" %}
[Cluster Configuration](configuration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure cluster-level and node-level settings, environment variables, JVM tuning, resources, and high availability for GridGain 9 clusters managed by the Kubernetes Operator.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="persistence.md" %}
[Persistence and Storage](persistence.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure persistent storage, storage classes, existing PVCs, additional volumes, volume permissions, and storage profiles for GridGain 9 clusters on Kubernetes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="networking.md" %}
[Services and Networking](networking.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure the default headless service and custom ClusterIP, NodePort, and LoadBalancer services for GridGain 9 clusters managed by the Kubernetes Operator.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="security.md" %}
[Security](security.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure authentication, SSL/TLS encryption, and pod and container security contexts for GridGain 9 clusters managed by the Kubernetes Operator.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="monitoring.md" %}
[Monitoring](monitoring.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Expose GridGain 9 cluster metrics through JMX and integrate with Prometheus when running clusters with the Kubernetes Operator.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="upgrades-and-rollbacks.md" %}
[Upgrades and Rollbacks](upgrades-and-rollbacks.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Perform rolling upgrades and automatic or manual rollbacks of GridGain 9 clusters with the Kubernetes Operator, and inspect the related status fields.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="crd-reference.md" %}
[CRD Reference](crd-reference.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete field reference for the GridGain9Cluster custom resource definition, covering all spec and status fields organized by functional area.
{% endcolumn %}
{% endcolumns %}
