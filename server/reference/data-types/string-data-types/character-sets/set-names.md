---
description: >-
  Configure the character set and collation for the current connection. This
  ensures the server correctly interprets data sent by the client application.
---

# SET NAMES

## Syntax

```sql
SET NAMES {'charset_name'
    [COLLATE 'collation_name'] | DEFAULT}
```

## Description

Sets the [character\_set\_client](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client), [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection), [character\_set\_results](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_results) and, implicitly, the [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) session system variables to the specified character set and collation.

This determines which [character set](./) the client will use to send statements to the server, and the server will use for sending results back to the client.

`ucs2`, `utf16`, `utf16le` and `utf32` are not valid character sets for `SET NAMES`, as they cannot be used as client character sets.

The collation clause is optional. If not defined (or if `DEFAULT` is specified), the [default collation for the character set](supported-character-sets-and-collations.md) will be used.

Quotes are optional for the character set or collation clauses.

## Examples

{% tabs %}
{% tab title="Current" %}
`utf8mb4` is the default for the affected variables:

```sql
SET NAMES DEFAULT;                

SELECT VARIABLE_NAME, SESSION_VALUE 
    FROM INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE 
    VARIABLE_NAME LIKE 'character_set_con%' OR 
    VARIABLE_NAME LIKE 'character_set_cl%' OR 
    VARIABLE_NAME LIKE 'character_set_re%' OR 
    VARIABLE_NAME LIKE 'collation_c%';
+--------------------------+-----------------------+
| VARIABLE_NAME            | SESSION_VALUE         |
+--------------------------+-----------------------+
| CHARACTER_SET_RESULTS    | utf8mb4               |
| CHARACTER_SET_CONNECTION | utf8mb4               |
| CHARACTER_SET_CLIENT     | utf8mb4               |
| COLLATION_CONNECTION     | utf8mb4_uca1400_ai_ci |
+--------------------------+-----------------------+
```
{% endtab %}

{% tab title="< 11.8" %}
The `utf8` [character set](./) (and related collations) is an alias for `utf8mb3` , rather than the other way around. [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114) added the [character\_set\_collations](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_collations) variable, so the `SELECT` query is more specific in this example:

```sql
SELECT VARIABLE_NAME, SESSION_VALUE 
    FROM INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE 
    VARIABLE_NAME LIKE 'character_set_con%' OR 
    VARIABLE_NAME LIKE 'character_set_cl%' OR 
    VARIABLE_NAME LIKE 'character_set_re%' OR 
    VARIABLE_NAME LIKE 'collation_c%';
+--------------------------+--------------------+
| VARIABLE_NAME            | SESSION_VALUE      |
+--------------------------+--------------------+
| CHARACTER_SET_RESULTS    | utf8mb3            |
| CHARACTER_SET_CONNECTION | utf8mb3            |
| CHARACTER_SET_CLIENT     | utf8mb3            |
| COLLATION_CONNECTION     | utf8mb3_general_ci |
+--------------------------+--------------------+

SET NAMES utf8mb4;

SELECT VARIABLE_NAME, SESSION_VALUE 
    FROM INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE 
    VARIABLE_NAME LIKE 'character_set_con%' OR 
    VARIABLE_NAME LIKE 'character_set_cl%' OR 
    VARIABLE_NAME LIKE 'character_set_re%' OR 
    VARIABLE_NAME LIKE 'collation_c%';
+--------------------------+--------------------+
| VARIABLE_NAME            | SESSION_VALUE      |
+--------------------------+--------------------+
| CHARACTER_SET_RESULTS    | utf8mb4            |
| CHARACTER_SET_CONNECTION | utf8mb4            |
| CHARACTER_SET_CLIENT     | utf8mb4            |
| COLLATION_CONNECTION     | utf8mb4_general_ci |
+--------------------------+--------------------+
```
{% endtab %}

{% tab title="< 10.6" %}
The utf8 [character set](./) (and related collation) is the default for the given variables:

```sql
SELECT VARIABLE_NAME, SESSION_VALUE 
  FROM INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE 
  VARIABLE_NAME LIKE 'character_set_c%' OR 
  VARIABLE_NAME LIKE 'character_set_re%' OR 
  VARIABLE_NAME LIKE 'collation_c%';
+--------------------------+-----------------+
| VARIABLE_NAME            | SESSION_VALUE   |
+--------------------------+-----------------+
| CHARACTER_SET_RESULTS    | utf8            |
| CHARACTER_SET_CONNECTION | utf8            |
| CHARACTER_SET_CLIENT     | utf8            |
| COLLATION_CONNECTION     | utf8_general_ci |
+--------------------------+-----------------+

SET NAMES big5;

SELECT VARIABLE_NAME, SESSION_VALUE 
  FROM INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE 
  VARIABLE_NAME LIKE 'character_set_c%' OR 
  VARIABLE_NAME LIKE 'character_set_re%' OR 
  VARIABLE_NAME LIKE 'collation_c%';
+--------------------------+-----------------+
| VARIABLE_NAME            | SESSION_VALUE   |
+--------------------------+-----------------+
| CHARACTER_SET_RESULTS    | big5            |
| CHARACTER_SET_CONNECTION | big5            |
| CHARACTER_SET_CLIENT     | big5            |
| COLLATION_CONNECTION     | big5_chinese_ci |
+--------------------------+-----------------+

SET NAMES 'latin1' COLLATE 'latin1_bin';

SELECT VARIABLE_NAME, SESSION_VALUE 
  FROM INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE 
  VARIABLE_NAME LIKE 'character_set_c%' OR 
  VARIABLE_NAME LIKE 'character_set_re%' OR 
  VARIABLE_NAME LIKE 'collation_c%';
+--------------------------+---------------+
| VARIABLE_NAME            | SESSION_VALUE |
+--------------------------+---------------+
| CHARACTER_SET_RESULTS    | latin1        |
| CHARACTER_SET_CONNECTION | latin1        |
| CHARACTER_SET_CLIENT     | latin1        |
| COLLATION_CONNECTION     | latin1_bin    |
+--------------------------+---------------+

SET NAMES DEFAULT;

SELECT VARIABLE_NAME, SESSION_VALUE 
  FROM INFORMATION_SCHEMA.SYSTEM_VARIABLES WHERE 
  VARIABLE_NAME LIKE 'character_set_c%' OR 
  VARIABLE_NAME LIKE 'character_set_re%' OR 
  VARIABLE_NAME LIKE 'collation_c%';
+--------------------------+-------------------+
| VARIABLE_NAME            | SESSION_VALUE     |
+--------------------------+-------------------+
| CHARACTER_SET_RESULTS    | latin1            |
| CHARACTER_SET_CONNECTION | latin1            |
| CHARACTER_SET_CLIENT     | latin1            |
| COLLATION_CONNECTION     | latin1_swedish_ci |
+--------------------------+-------------------+
```
{% endtab %}
{% endtabs %}

## See Also

* [SET CHARACTER SET](set-character-set.md)
* [Setting Character Sets and Collations](setting-character-sets-and-collations.md)
* [Character Sets and Collations](./)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
