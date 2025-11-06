# Information Schema COLLATIONS Table

The [Information Schema](../) `COLLATIONS` table contains a list of supported [collations](../../../data-types/string-data-types/character-sets/).

It contains the following columns:

| Column               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| COLLATION\_NAME      | Name of the collation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| CHARACTER\_SET\_NAME | Associated character set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ID                   | Collation id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IS\_DEFAULT          | Whether the collation is the character set's default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| IS\_COMPILED         | Whether the collation is compiled into the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SORTLEN              | Sort length, used for determining the memory used to sort strings in this collation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PAD\_ATTRIBUTE       | <p>Determines whether or not trailing spaces are regarded as normal characters. See <a href="information-schema-collations-table.md#no-pad-collations">below</a>.<br>Available from MariaDB 12.1.</p>                                                                                                                                                                                                                                                                                                                                                          |
| COMMENT              | <p>For utf8mb4_0900 collations, contains the corresponding alias collation.</p><p>From <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-5-release-notes">MariaDB 11.4.5</a>, <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-2-release-notes">MariaDB 11.7.2</a>, <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-8-series/mariadb-11-8-1-release-notes">MariaDB 11.8.1</a>.</p> |

The [SHOW COLLATION](../../../sql-statements/administrative-sql-statements/show/show-collation.md) statement returns the same results and both can be reduced in a similar way.

{% tabs %}
{% tab title="Current" %}
The following two statements return the same results:

```sql
SHOW COLLATION WHERE Charset LIKE 'utf8mb3';
```

```sql
SELECT * FROM information_schema.COLLATIONS 
WHERE CHARACTER_SET_NAME LIKE 'utf8mb3';
```
{% endtab %}

{% tab title="< 10.5" %}
The following two statements return the same results:

```sql
SHOW COLLATION WHERE Charset LIKE 'utf8';
```

```sql
SELECT * FROM information_schema.COLLATIONS 
WHERE CHARACTER_SET_NAME LIKE 'utf8';
```
{% endtab %}
{% endtabs %}

## NO PAD Collations

`NO PAD` collations regard trailing spaces as normal characters. You can get a list of all `NO PAD` collations as follows:

{% tabs %}
{% tab title="Current" %}
```sql
SELECT collation_name FROM information_schema.COLLATIONS
WHERE pad_attribute = "NO PAD";  
+------------------------------+
| collation_name               |
+------------------------------+
| big5_chinese_nopad_ci        |
| big5_nopad_bin               |
...
```
{% endtab %}

{% tab title="< 12.1" %}
```sql
SELECT collation_name FROM information_schema.COLLATIONS
WHERE collation_name LIKE "%nopad%";  
+------------------------------+
| collation_name               |
+------------------------------+
| big5_chinese_nopad_ci        |
| big5_nopad_bin               |
...
```
{% endtab %}
{% endtabs %}

In comparisons, `NO PAD` collations evaluate to `0` (`FALSE`). Example:

```sql
SELECT 'a ' = 'a'; 
+------------+ 
| 'a ' = 'a' | 
+------------+
|          0 | 
+------------+
```

## PAD SPACE Collations

&#x20;`PAD SPACE` collations pad strings to equal lengths in comparisons, so that the comparison evaluates to `1` (`TRUE`). Example:

```sql
SELECT 'a ' = 'a'; 
+------------+ 
| 'a ' = 'a' | 
+------------+
|          1 | 
+------------+
```

## Example

```sql
SELECT * FROM information_schema.COLLATIONS;
+------------------------------+--------------------+------+------------+-------------+---------+
| COLLATION_NAME               | CHARACTER_SET_NAME | ID   | IS_DEFAULT | IS_COMPILED | SORTLEN |
+------------------------------+--------------------+------+------------+-------------+---------+
| big5_chinese_ci              | big5               |    1 | Yes        | Yes         |       1 |
| big5_bin                     | big5               |   84 |            | Yes         |       1 |
| big5_chinese_nopad_ci        | big5               | 1025 |            | Yes         |       1 |
| big5_nopad_bin               | big5               | 1108 |            | Yes         |       1 |
| dec8_swedish_ci              | dec8               |    3 | Yes        | Yes         |       1 |
| dec8_bin                     | dec8               |   69 |            | Yes         |       1 |
| dec8_swedish_nopad_ci        | dec8               | 1027 |            | Yes         |       1 |
| dec8_nopad_bin               | dec8               | 1093 |            | Yes         |       1 |
| cp850_general_ci             | cp850              |    4 | Yes        | Yes         |       1 |
| cp850_bin                    | cp850              |   80 |            | Yes         |       1 |
...
```

## See Also

* [Setting Character Sets and Collations](../../../data-types/string-data-types/character-sets/setting-character-sets-and-collations.md) - specifying the character set at the server, database, table and column levels
* [Supported Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md) - full list of supported characters sets and collations.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
