---
description: >-
  Overview of GridGain Operator for Kubernetes: supported platforms, features,
  prerequisites, and supported GridGain and Apache Ignite versions.
---

# GridGain and Apache Ignite Operator for Kubernetes

{% hint style="warning" %}
The operator is under active development, the public API might be changed in future releases.
{% endhint %}

## Overview

GridGain Operator enables you to deploy and manage Apache Ignite and GridGain clusters in a Kubernetes environment. The automation that Kubernetes and GridGain Operator provide simplifies provisioning and minimizes the burden of operating and managing Apache Ignite clusters.

GridGain Operator can use any of the following certified Kubernetes platforms:

- Open-source Kubernetes
- Amazon Elastic Kubernetes Service (EKS)
- Google Kubernetes Engine (GKE)
- Microsoft Azure Kubernetes Service (AKS)

{% hint style="info" %}
[Instructor-led Developer Training - Apache Ignite and Kubernetes: Deployment and Orchestration Strategies](https://www.gridgain.com/products/services/training/apache-ignite-and-kubernetes-deployment-and-orchestration-strategies)

Join our free instructor-led training sessions to explore the best practices of using Kubernetes and Apache Ignite.
{% endhint %}

## Features

Deploying provides the following functionality:

- Automates GridGain cluster deployment
- Automates GridGain cluster management

For persistent volume storage, GridGain Operator uses default Kubernetes provisioners that are based on [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) (such as Google persistent disks, AWS EBS, and Azure disk storage)
Updating and upgrading provide automated rolling updates for configuration changes.

Scaling provides automatic scaling for new cluster nodes.

## Prerequisites

- A Kubernetes cluster that conforms to one of the supported environments
- Installed kubectl
- Access to the dockerhub.io

Supported GridGain and Apache Ignite versions:

- GridGain 8.7.20+
- Apache Ignite 2.9.0+

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
