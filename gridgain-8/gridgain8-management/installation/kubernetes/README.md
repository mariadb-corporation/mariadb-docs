---
description: >-
  Deploy and manage GridGain clusters on Kubernetes, including managed services
  such as Amazon EKS, Azure AKS, Google GKE, and RedHat OpenShift.
---

# Installation and Upgrade

This section describes how to deploy a GridGain cluster on Kubernetes, both on generic Kubernetes and on managed platforms such as Amazon EKS, Microsoft Azure AKS, Google GKE, and RedHat OpenShift.

{% columns %}
{% column %}
{% content-ref url="amazon-eks-deployment.md" %}
[Amazon EKS Deployment](amazon-eks-deployment.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A step-by-step guide to deploying a GridGain cluster on Amazon Elastic Kubernetes Service (EKS) using the eksctl command-line tool.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="azure-deployment.md" %}
[Azure Kubernetes Service Deployment](azure-deployment.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A step-by-step guide to deploying a GridGain cluster on Microsoft Azure Kubernetes Service (AKS) using the Azure portal.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gke-deployment.md" %}
[Google Kubernetes Engine](gke-deployment.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to deploy a GridGain cluster on Google Kubernetes Engine (GKE) using the gcloud command-line tool.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="openshift-deployment.md" %}
[RedHat OpenShift Deployment](openshift-deployment.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to deploy a GridGain cluster on RedHat OpenShift using the oc command-line tool.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="helm-deployment.md" %}
[Helm Deployment](helm-deployment.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to deploy a GridGain cluster on Kubernetes using the GridGain Helm chart, including custom configuration, license, authentication, and volumes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="generic-configuration.md" %}
[Generic Configuration](generic-configuration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A generic, step-by-step guide to deploying and managing GridGain server nodes on Kubernetes using a StatefulSet, covering configuration, licensing, probes, activation, scaling, and connectivity.
{% endcolumn %}
{% endcolumns %}
