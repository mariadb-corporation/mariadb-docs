---
description: >-
  A step-by-step guide to deploying a GridGain cluster on Amazon Elastic
  Kubernetes Service (EKS) using the eksctl command-line tool.
---

# Amazon EKS Deployment

This page is a step-by-step guide on how to deploy a GridGain cluster on Amazon EKS.

{% hint style="info" %}
This guide covers the provider-specific steps. It builds on the shared [Generic Kubernetes Instruction](generic-configuration.md), which explains the concepts, prerequisites, and configuration common to all Kubernetes deployments.
{% endhint %}
In this guide, we will use the `eksctl` command line tool to create a Kubernetes cluster.
Please follow [this guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) to install the required resources and get familiar with the tool.

## Creating an Amazon EKS Cluster

First of all, you need to create an Amazon EKS cluster that will provide resources for our Kubernetes pods.
You can create a cluster using the following command:

```shell
eksctl create cluster --name gridgaincluster --nodes 2 --nodes-min 1 --nodes-max 4
```

Check the [EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) for the full list of options.
The provisioning of a cluster can take up to 15 minutes.
Check the status of the cluster using the following command:

```shell
$ eksctl get cluster -n gridgaincluster
NAME            VERSION STATUS  CREATED                 VPC                     SUBNETS                                                                                                 SECURITYGROUPS
gridgaincluster 1.14    ACTIVE  2019-12-16T09:57:09Z    vpc-0ebf4a6ee3de12c63   subnet-00fa7e85aaebcd54d,subnet-06134ae545a5cc04c,subnet-063d9fdb481e727d2,subnet-0a087062ddc47c341     sg-06a6800a67ea95528
```

When the status of the cluster becomes ACTIVE, you can start creating Kubernetes resources.

Verify that your `kubectl` is configured correctly:

```shell
$ kubectl get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   6m49s
```

## Kubernetes Configuration

The namespace, service, cluster role, ConfigMap, and node configuration file are the same for every Kubernetes deployment. Follow the [Generic Kubernetes Instruction](generic-configuration.md#kubernetes-configuration) to create these resources.
<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
