---
icon: rabbit
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# Quickstart Guides

This space offers step-by-step instructions for quickly deploying, configuring, and managing MariaDB Cloud databases using various methods and tools. Whether you prefer to use web-based portal, REST APIs, infrastructure-as-code tools like Terraform, or Python scripts, these methods will help you to walk through the complete process, from initial setup and connecting to the first database, to deployment, monitoring, and scaling of cloud database instances.

## Using the Portal

This page explains how to deploy a MariaDB Cloud service using the web-based MariaDB Cloud Portal interface with just a few clicks. It includes account creation, launching Serverless or Provisioned services, monitoring & scaling databases, and performing basic management operations.

{% content-ref url="using-the-portal.md" %}
[using-the-portal.md](using-the-portal.md)
{% endcontent-ref %}

## Launch DB Using REST API

On this page, you can learn how to programmatically deploy and manage MariaDB Cloud databases using the DBaaS REST API. It demonstrates how to generate an API key, create a service through HTTP requests, obtain connection credentials, and manage the lifecycle of database services.

{% content-ref url="launch-db-using-the-rest-api.md" %}
[launch-db-using-the-rest-api.md](launch-db-using-the-rest-api.md)
{% endcontent-ref %}

## Launch DB Using Terraform Provider

This page describes how to deploy and manage MariaDB Cloud instances using the Terraform Provider for infrastructure-as-code automation and version-controlled database environments. It covers creating Terraform configuration files, specifying service specifications, and running deployment plans.

{% content-ref url="launch-db-using-the-terraform-provider.md" %}
[launch-db-using-the-terraform-provider.md](launch-db-using-the-terraform-provider.md)
{% endcontent-ref %}

## Launch DB Using Python

This page shows how to use Python scripts to connect to the MariaDB Cloud and launch a database service using simple API calls for creating and managing services. It offers scripts for creating services, monitoring status, obtaining security credentials, and testing connections.

{% content-ref url="launch-db-using-python.md" %}
[launch-db-using-python.md](launch-db-using-python.md)
{% endcontent-ref %}

