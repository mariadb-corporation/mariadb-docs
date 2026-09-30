---
description: >-
  Install and start GridGain — system requirements, the binary distribution,
  starting a node with default or custom configuration, and deployment options.
---

# Installation and Upgrade

This chapter explains system requirements for running GridGain, how to install GridGain, and how to start a GridGain node.

Since GridGain is built on top of Apache Ignite, GridGain reuses Ignite's system properties, environment properties, startup scripts, etc. wherever possible.

## Prerequisites

{% include "../../.gitbook/includes/gg8-prereqs.md" %}

If you use Java version 11 or later, see [Running GridGain with Java 11 or later](#running-gridgain-with-java-11-or-later) for details.

## Running GridGain with Java 11 or Later

{% include "../../.gitbook/includes/gg8-java9.md" %}

## Installation

{% include "../../.gitbook/includes/gg8-installggqsg.md" %}

## Starting a GridGain Node

You can start a GridGain node from the command line using the default configuration or by passing a custom configuration file. You can start as many nodes as you like and they will all automatically discover each other.

### With Default Configuration

To start a GridGain node with the default configuration, open the command shell and, assuming you are in GridGain installation directory, run this from the command line:

{% tabs %}
{% tab title="Unix" %}
```shell
$ bin/ignite.sh
```
{% endtab %}

{% tab title="Windows" %}
```shell
$ bin\ignite.bat
```
{% endtab %}
{% endtabs %}

You will see output similar to this:

```
[02:49:12] Ignite node started OK (id=ab5d18a6)
[02:49:12] Topology snapshot [ver=1, nodes=1, CPUs=8, heap=1.0GB]
```

By default, `ignite.sh|bat` starts a node with the default configuration file: `config/default-config.xml`.

### With Custom Configuration

To start a GridGain node with a custom configuration file, open the command shell and, assuming you are in `IGNITE_HOME` (the GridGain installation folder), pass the configuration file as a parameter to `ignite.sh|bat` as follows:

{% tabs %}
{% tab title="Unix" %}
```shell
$ bin/ignite.sh examples/config/example-ignite.xml
```
{% endtab %}

{% tab title="Windows" %}
```shell
$ bin\ignite.bat examples\config\example-ignite.xml
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
If you pass a custom configuration file, and you are using Java 11 or higher, you may want to include some extra parameters. See [Running GridGain with Java 11 or later](#running-gridgain-with-java-11-or-later).
{% endhint %}

{% hint style="info" %}
The path to the configuration file can be absolute, or relative to either `IGNITE_HOME` (GridGain installation folder) or `META-INF` folder in your classpath.
{% endhint %}

You will see output similar to this:

```
[02:49:12] Ignite node started OK (id=ab5d18a6)
[02:49:12] Topology snapshot [ver=1, nodes=1, CPUs=8, heap=1.0GB]
```

Congratulations! You've just launched your first GridGain cluster.

{% columns %}
{% column %}
{% content-ref url="deployment-modes.md" %}
[Deployment Modes](deployment-modes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An overview of GridGain deployment modes: cluster modes (in-memory data grid, system of record, heterogeneous) and application modes (client-server, embedded).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-on-zos.md" %}
[Installation on z/OS](installing-on-zos.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
System requirements, installation steps, configuration, and startup guidance for running GridGain on z/OS.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-using-docker.md" %}
[Installing Using Docker](installing-using-docker.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to run GridGain in Docker: pulling the image, running in-memory and persistent clusters, providing configuration and license files, and enabling modules.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installing-using-zip.md" %}
[Installing Using ZIP Archive](installing-using-zip.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to install GridGain from the ZIP archive distribution, including prerequisites and software identification.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aws/" %}
[AWS](aws/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Options for deploying GridGain on Amazon Web Services, including prebuilt AMIs, manual EC2 installation, Terraform, and multi-availability-zone setups.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="azure/" %}
[Microsoft Azure](azure/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Options for deploying GridGain on Microsoft Azure.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="kubernetes/" %}
[Installation and Upgrade](kubernetes/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy and manage GridGain clusters on Kubernetes, including managed services such as Amazon EKS, Azure AKS, Google GKE, and RedHat OpenShift.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="operator/" %}
[GridGain Operator](operator/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain Operator for Kubernetes automates the deployment and management of GridGain and Apache Ignite clusters in a Kubernetes environment.
{% endcolumn %}
{% endcolumns %}
