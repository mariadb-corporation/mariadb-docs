---
description: >-
  The MariaDB Jupyter Kernel is an open-source Jupyter kernel that enables
  running MariaDB SQL directly in notebooks, with support for
  autocompletion, magic commands, and charting.
---

# About the MariaDB Jupyter Kernel

The MariaDB Jupyter Kernel is an Open-Source kernel for [Jupyter](https://jupyter.org) which enables users to run MariaDB in a [Jupyter](https://jupyter.org) notebook.

Notebooks can be run in a variety of environments, ranging from your local computer for testing purposes via [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) to complex [Zero to JupyterHub Kubernetes systems](https://zero-to-jupyterhub.readthedocs.io/en/latest/) running in the cloud.

The [mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel) project is agnostic about the complexity of your [Jupyter](https://jupyter.org) infrastructure, it can run on any of them thanks to the way [Jupyter](https://jupyter.org) designed its kernel machinery. As long as MariaDB is installed on the host running the kernel and there is MariaDB Server running somewhere, things should work out as expected.

## Motivation

We created the [mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel) project with some simple goals in mind:

* Help existing MariaDB users have an alternative to the classical [mariadb command-line client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mysql-command-line-client) based on Jupyter.
* Bring MariaDB Server to Jupyter and Python users who would like to use our Open-Source database for handling their datasets.

If you would love to be able to run SQL against MariaDB data from Jupyter notebooks or you want to run a training program and help your employees learn SQL, if you are a teacher and you’d love to use Jupyter for your SQL classes or you are a data scientist trying to quickly chart or explore your datasets, you should take a look at this project.

## Contents

### [Installation](mariadb-jupyter-kernel-installation.md)

* [Quick Installation Steps](mariadb-jupyter-kernel-installation.md#quick-installation-steps)
* [Complete Installation Steps](mariadb-jupyter-kernel-installation.md#complete-installation-steps)
* [Platforms Coverage](mariadb-jupyter-kernel-installation.md#platforms-coverage)

### [Configuring the kernel](configuring-the-mariadb-jupyter-kernel.md)

* [Config File Location](configuring-the-mariadb-jupyter-kernel.md#config-file-location)
* [Config Example](configuring-the-mariadb-jupyter-kernel.md#config-example)
* [The Full List of JSON Options](configuring-the-mariadb-jupyter-kernel.md#the-full-list-of-json-options)

### [Using the Kernel](./)

* [General Usage Information](using-the-kernel/general-mariadb-jupyter-kernel-usage-information.md)
* [SQL Autocompletion and Introspection](using-the-kernel/sql-autocompletion-and-introspection.md)
* [Magic Commands](using-the-kernel/mariadb-jupyter-kernel-magic-commands.md)
* [Restrictions and Limitations](using-the-kernel/mariadb-jupyter-kernel-restrictions-and-limitations.md)

### [Main Components and Architecture](the-mariadb-jupyter-kernel-main-components-and-architecture.md)

* [Architecture](the-mariadb-jupyter-kernel-main-components-and-architecture.md#architecture)
* [Components](the-mariadb-jupyter-kernel-main-components-and-architecture.md#components)
  * [MariaDBKernel](the-mariadb-jupyter-kernel-main-components-and-architecture.md#mariadbkernel)
  * [ClientConfig](the-mariadb-jupyter-kernel-main-components-and-architecture.md#clientconfig)
  * [MariaDBClient](the-mariadb-jupyter-kernel-main-components-and-architecture.md#mariadbclient)
  * [MariaDBServer](the-mariadb-jupyter-kernel-main-components-and-architecture.md#mariadbserver)
  * [CodeParser](the-mariadb-jupyter-kernel-main-components-and-architecture.md#codeparser)
  * [MagicFactory](the-mariadb-jupyter-kernel-main-components-and-architecture.md#magicfactory)
  * [MariaMagic](the-mariadb-jupyter-kernel-main-components-and-architecture.md#mariamagic)
  * [LineMagic](the-mariadb-jupyter-kernel-main-components-and-architecture.md#linemagic)
  * [CellMagic](the-mariadb-jupyter-kernel-main-components-and-architecture.md#cellmagic)
  * [LSMagic](the-mariadb-jupyter-kernel-main-components-and-architecture.md#lsmagic)
  * [Line](the-mariadb-jupyter-kernel-main-components-and-architecture.md#line)
  * [DF](the-mariadb-jupyter-kernel-main-components-and-architecture.md#df)
  * [Bar](the-mariadb-jupyter-kernel-main-components-and-architecture.md#bar)
  * [Pie](the-mariadb-jupyter-kernel-main-components-and-architecture.md#pie)
  * [Delimiter](the-mariadb-jupyter-kernel-main-components-and-architecture.md#delimiter)

### [Extending the Kernel](contributing-to-the-mariadb-jupyter-kernel-project.md)

### [Changelog](changes-in-mariadb-jupyter-kernel.md)

* [v0.2.2](changes-in-mariadb-jupyter-kernel.md#v020-02-november-2021)
* [v0.1.1](changes-in-mariadb-jupyter-kernel.md#v011-29-march-2021)
* [v0.1.0 First release!](changes-in-mariadb-jupyter-kernel.md#v010-11-january-2021)

{% @marketo/form formId="4316" %}
