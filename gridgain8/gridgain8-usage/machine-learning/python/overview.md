---
hidden: true
description: >-
  Overview of the GridGain ML Python client library (ggml), its prerequisites, and installation options.
---

# Overview

The GridGain ML client library, written in Python 3, is abbreviated as ggml.

The GridGain ML client library provides user applications the ability to work with GridGain ML functionality using Py4J as an integration mechanism.

## Prerequisites

- Python 3.4 or above (3.6 is tested)
- IGNITE_HOME environment variable with path to Apache Ignite
- Access to an Ignite instance and permission to create a new cache or to get an existing cache

## Installation

### End Users

If you want to use ggml in your project, you may install it from PyPI:

{% code title="Shell" %}
```shell
$ pip install ggml
```
{% endcode %}

### Developer

If you want to run tests or examples, or build documentation, clone the whole repository:

{% code title="Shell" %}
```shell
$ git clone git@github.com:apache/ignite.git
$ cd ignite/modules/ml/python
$ pip install -e .
```
{% endcode %}

This will install the repository version of ggml into your environment in "develop" or "editable" mode. You can read more about editable installs in the pip manual.

## Getting Started

Get started [using GridGain ML](using-python-ml.md).

Read the [GGML API documentation](https://machine-learning-python-api.readthedocs.io/readme.html).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
