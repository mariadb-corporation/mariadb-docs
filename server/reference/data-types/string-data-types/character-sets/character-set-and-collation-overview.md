---
description: >-
  Learn the core concepts of character sets and collations in MariaDB, including
  how they define string storage and sorting rules.
---

# Character Set and Collation Overview

## What are Character Sets and Collations?

A character set is a set of characters, while a collation comprises the rules for comparing and sorting a particular character set.

For example, a subset of a character set could consist of the letters `A`, `B` and `C`. A default collation could define these as appearing in an ascending order of `A, B, C`.

If we consider different case characters, more complexity is added. A binary collation would evaluate the characters `A` and `a` differently, ordering them in a particular way. A case-insensitive collation would evaluate `A` and `a` equivalently, while the German phone book collation evaluates the characters `ue` and `ü` equivalently.

A character set can have many collations associated with it, while each collation is only associated with one character set. In MariaDB, the character set name is always part of the collation name. For example, the `latin1_german1_ci` collation applies only to the `latin1` character set. Each character set also has one default collation. The `latin1` default collation is `latin1_swedish_ci`.

As an example, by default, the character `y` comes between `x` and `z`, while in Lithuanian, it's sorted between `i` and `k`. Similarly, the German phone book order is different to the German dictionary order, so while they share the same character set, the collation is different.

## Viewing Character Sets and Collations

{% tabs %}
{% tab title="Current" %}
The default character set is `utf8mb4` and the default collation is `utf8mb4_uca1400_ai_ci`.\
This may differ in some distros, see for example [Differences in MariaDB in Debian](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md).
{% endtab %}

{% tab title="< 11.6" %}
The default [character set](./) is `latin1` and the default collation is `latin1_swedish_ci`.\
This may differ in some distros, see for example [Differences in MariaDB in Debian](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/troubleshooting-installation-issues/installation-issues-on-debian-and-ubuntu/differences-in-mariadb-in-debian-and-ubuntu.md).
{% endtab %}
{% endtabs %}

You can view a full list of character sets and collations supported by MariaDB at [Supported Character Sets and Collations](supported-character-sets-and-collations.md), or see what's supported on your server with the [SHOW CHARACTER SET](../../../sql-statements/administrative-sql-statements/show/show-character-set.md) and [SHOW COLLATION](../../../sql-statements/administrative-sql-statements/show/show-collation.md) commands.

By default, `A` comes before `Z`, so the following evaluates to true:

```sql
SELECT "A" < "Z";
+-----------+
| "A" < "Z" |
+-----------+
|         1 |
+-----------+
```

By default, comparisons are case-insensitive:

```sql
SELECT "A" < "a", "A" = "a";
+-----------+-----------+
| "A" < "a" | "A" = "a" |
+-----------+-----------+
|         0 |         1 |
+-----------+-----------+
```

## Changing Character Sets and Collations

Character sets and collations can be set from the server level right down to the column level, as well as for client-server communication.

For example, `ue` and `ü` are by default evaluated differently.

```sql
SELECT 'Mueller' = 'Müller';
+----------------------+
| 'Müller' = 'Mueller' |
+----------------------+
|                    0 |
+----------------------+
```

By using the [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable to change the connection character set to `latin1_german2_ci`, or German phone book, the same two characters will evaluate as equivalent.

```sql
SET collation_connection = latin1_german2_ci;

SELECT 'Mueller' = 'Müller';
+-----------------------+
| 'Mueller' = 'Müller'  |
+-----------------------+
|                     1 |
+-----------------------+
```

See [Setting Character Sets and Collations](setting-character-sets-and-collations.md) for more.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
