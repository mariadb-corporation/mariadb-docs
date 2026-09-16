---
description: >-
  Overview of the GridGain Kubernetes Operator, the GridGain9Cluster custom
  resource, and the Kubernetes objects it manages.
---

# GridGain Kubernetes Operator

{% hint style="warning" %}
Kubernetes operator is an experimental feature. The configuration may change in a subsequent release.
{% endhint %}

## Overview

The GridGain Kubernetes Operator automates the deployment and lifecycle management of GridGain 9 clusters on Kubernetes. It introduces a custom resource called `GridGain9Cluster` that can be used to describe the desired state of a GridGain cluster. The operator watches for these resources and continuously reconciles the desired state with the actual state, creating and managing the underlying Kubernetes objects on your behalf.

The operator runs as a Deployment named `gridgain9-controller-manager` in the `gridgain9-system` namespace.

## The GridGain9Cluster Resource

The custom resource belongs to the API group `gridgain-9.gridgain.com`, and has the `v1` version. Two short names are also registered for convenience: `gg9` and `gg9cluster`. The resource is namespaced, so you deploy GridGain clusters into specific Kubernetes namespaces.

## Managed Resources

For each `GridGain9Cluster` resource, the operator creates and manages several Kubernetes objects. The full set of permissions is defined in the `gridgain9-manager-role` ClusterRole and includes:

- **StatefulSet** — runs the GridGain nodes as an ordered, stable set of pods;
- **Services** — a headless service for inter-node discovery plus any user-defined services;
- **ConfigMaps** — holds GridGain node and cluster configuration files;
- **Secrets** — manages license data and configuration content provided inline;
- **PersistentVolumeClaims** — provides durable storage when persistence is enabled;
- **PodDisruptionBudgets** — protects availability during voluntary disruptions;
- **Jobs** — handles cluster initialization tasks such as applying the license.

## Key Ports

GridGain 9 uses three network ports by default:

| Port | Protocol | Purpose |
| --- | --- | --- |
| 10300 | REST API | Cluster management, health checks, and the REST endpoint used by liveness and readiness probes. |
| 10800 | Client connector | Used by applications connecting to the cluster through JDBC, ODBC, or thin client drivers. |
| 3344 | Internal network | Inter-node communication and cluster discovery. The headless service exposes this port so that nodes can find each other via DNS. |

## Role-Based Access Control

The operator ships with several `ClusterRoles` to support different access levels:

- `gridgain9-manager-role` — used by the operator itself; grants full control over the resources listed above.
- `gridgain9-leader-election-role` — used by the operator for leader election when running multiple replicas for high availability.
- `gridgain9-gridgain9cluster-admin-role` — grants wildcard access to `GridGain9Cluster` resources and read access to their status.
- `gridgain9-gridgain9cluster-editor-role` — grants create, read, update, and delete access to `GridGain9Cluster` resources.
- `gridgain9-gridgain9cluster-viewer-role` — grants read-only access to `GridGain9Cluster` resources and their status.
- `gridgain9-metrics-auth-role` — grants access to create token reviews and subject access reviews for metrics authentication.
- `gridgain9-metrics-reader` — grants read access to the operator metrics endpoint.

Assign the editor or viewer roles to teams that need to manage or inspect clusters without full operator privileges.

For more information about securing your clusters, see [Security](security.md) documentation.
