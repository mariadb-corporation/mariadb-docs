---
description: >-
  PyGridGain 1.5.0 adds support for Python 3.11, 3.12, and 3.13, vector search
  through the VECTOR index type, and disables SSL by default.
hidden: true
---

# PyGridGain 1.5.0 Release Notes

## New Features

PyGridGain 1.5.0 provides access to new features and improvements.

### Support for Python 3.11, 3.12 and 3.13

You can now use Python  3.11, 3.12 and 3.13 to work with GridGain. Pre-built packages for Python  3.11, 3.12 and 3.13 were added into the package.

### Support for Vector Search

In this release, you can create vector indexes for caches by setting index type to `IndexType.VECTOR`, and later use these indexes to perform vector search on the database. Below is the example of performing a vector query:

```python
query_vector = # Get from your model
cursor = cache.vector(type_name=Article.type_name, field='vector_field', clause_vector=query_vector, k=1)
```

### SSL  Disabled by Default

Starting from this release, SSL is disabled by default, and must be enabled manually.

## Improvements and Fixed Issues

| Issue ID | Description |
|---|---|
| GG-41858 | Updated supported Python versions to 3.9-3.12. |
| GG-41069 | Added support for VECTOR index type. |
| GG-37476 | Updated tzlocal library version to 4.3.1. |
| GG-35312 | SSL is no longer automatically enabled when authentication is used. |

## Installation and Upgrade Information

To upgrade an existing package, use the following command:

```shell
pip install --upgrade pygridgain
```

To install the latest version of a package:

```shell
pip install pygridgain
```

To install a specific version:

```shell
pip install pygridgain==1.5.0
```

## Previous Releases

- [PyGridGain 1.4.0](release-notes_python-1.4.0.md)
- [PyGridGain 1.3.1](release-notes_python-1.3.1.md)
- [PyGridGain 1.2.0](release-notes_python-1.2.0.md)

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
