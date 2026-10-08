---
description: >-
  This page outlines the key enhancements in FederatedX over the original
  Federated engine, including support for transactions and a refactored
  codebase. This storage engine has been deprecated.
---

# Differences Between FederatedX and Federated

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

The main differences are:

## New features in FederatedX

* Transactions (beta feature)
* Supports partitions (alpha feature)
* New class structure which allows developers to write connection classes for other RDBMSs without having to modify base classes for FederatedX

## Different behavior

* FederatedX is statically compiled into MariaDB by default.
* When you create a table with FederatedX, the connection are tested. The `CREATE` will fail if MariaDB can't connect to the remote host or if the remote table doesn't exist.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
