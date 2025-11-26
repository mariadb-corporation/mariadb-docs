---
description: >-
  Sets the current role for the session. Learn how to enable none, or a
  specific role to change your current privileges dynamically.
---

# SET ROLE

## Syntax

```
SET ROLE { role | NONE }
```

## Description

{% hint style="info" %}
Only one role can be current at a time. Executing `SET ROLE` replaces the current role; it does not add to a list of current roles. This is SQL Standard compliant behavior which differs from MySQL, where you may have several current roles at a time.
{% endhint %}

The `SET ROLE` statement switches the current role for the session, enabling its associated permissions. To have no current role, set `NONE`.

If a role that doesn't exist, or to which the user has not been assigned, is specified, an `ERROR 1959 (OP000): Invalid role specification` error occurs.

An automatic SET ROLE is implicitly performed when a user connects if that user has been assigned a default role. See [SET DEFAULT ROLE](set-default-role.md).

## Example

```sql
--Checking the current role status
SELECT CURRENT_ROLE;
```

{% code title="No role active" %}
```
+--------------+
| CURRENT_ROLE |
+--------------+
| NULL         |
+--------------+
```
{% endcode %}

```sql
--Setting the staff role, and verifying the switch
SET ROLE staff;
SELECT CURRENT_ROLE;
```

{% code title="'staff' role is active for the session" %}
```
+--------------+
| CURRENT_ROLE |
+--------------+
| staff        |
+--------------+
```
{% endcode %}

```sql
--switching to 'admin' role, and verifying the switch
SET ROLE admin;
SELECT CURRENT_ROLE;
```

{% code title="'staff' role is no longer active" %}
```
+--------------+
| CURRENT_ROLE |
+--------------+
| admin        |
+--------------+
```
{% endcode %}

```sql
--Removing the active role
SET ROLE NONE;
SELECT CURRENT_ROLE();
```

```
+----------------+
| CURRENT_ROLE() |
+----------------+
| NULL           |
+----------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
