---
description: >-
  Map strings to a specific character set. This command updates the character
  set for the client, results, and connection to ensure correct data encoding.
---

# SET CHARACTER SET

## Syntax

```sql
SET {CHARACTER SET | CHARSET}
    {charset_name | DEFAULT}
```

## Description

Sets the [character\_set\_client](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) and [character\_set\_results](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_results) session system variables to the specified character set and [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) to the value of [collation\_database](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_database), which implicitly sets [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) to the value of [character\_set\_database](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_database).

This maps all strings sent between the current client and the server with the given mapping.

## Example

```sql
SHOW VARIABLES LIKE 'character_set\_%';
+--------------------------+--------+
| Variable_name            | Value  |
+--------------------------+--------+
| character_set_client     | utf8   |
| character_set_connection | utf8   |
| character_set_database   | latin1 |
| character_set_filesystem | binary |
| character_set_results    | utf8   |
| character_set_server     | latin1 |
| character_set_system     | utf8   |
+--------------------------+--------+

SHOW VARIABLES LIKE 'collation%';
+----------------------+-------------------+
| Variable_name        | Value             |
+----------------------+-------------------+
| collation_connection | utf8_general_ci   |
| collation_database   | latin1_swedish_ci |
| collation_server     | latin1_swedish_ci |
+----------------------+-------------------+

SET CHARACTER SET utf8mb4;

SHOW VARIABLES LIKE 'character_set\_%';
+--------------------------+---------+
| Variable_name            | Value   |
+--------------------------+---------+
| character_set_client     | utf8mb4 |
| character_set_connection | latin1  |
| character_set_database   | latin1  |
| character_set_filesystem | binary  |
| character_set_results    | utf8mb4 |
| character_set_server     | latin1  |
| character_set_system     | utf8    |
+--------------------------+---------+

SHOW VARIABLES LIKE 'collation%';
+----------------------+-------------------+
| Variable_name        | Value             |
+----------------------+-------------------+
| collation_connection | latin1_swedish_ci |
| collation_database   | latin1_swedish_ci |
| collation_server     | latin1_swedish_ci |
+----------------------+-------------------+
```

## See Also

* [Setting Character Sets and Collations](setting-character-sets-and-collations.md)
* [SET NAMES](set-names.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
