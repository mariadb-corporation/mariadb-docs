---
description: The CONNECT storage engine has been deprecated.
---

# CONNECT Security

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

The use of the CONNECT engine requires the [FILE](../../../reference/sql-statements/account-management-sql-statements/grant.md#file) privilege for ["outward"](connect-table-types/inward-and-outward-tables.md#outward-tables) tables. This should not be an important restriction. The use of CONNECT "outward" tables on a remote server seems of limited interest without knowing the files existing on it and must be protected anyway. On the other hand, using it on the local client machine is not an issue because it is always possible to create locally a user with the `FILE` privilege.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
