# Identifier Names

Databases, tables, indexes, columns, aliases, views, stored routines, triggers, events, variables, partitions, tablespaces, savepoints, labels, users, roles, are collectively known as identifiers, and have certain rules for naming.

Identifiers may be quoted using the backtick character - \`\`\`. Quoting is optional for identifiers that don't contain special characters, or for identifiers that are not [reserved words](reserved-words.md). If the `ANSI_QUOTES` [SQL\_MODE](../../../server-management/variables-and-modes/sql-mode.md) flag is set, double quotes (`"`) can also be used to quote identifiers. If the [MSSQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/compatibility-and-differences/sql_modemssql) flag is set, square brackets (`[` and `]`) can be used for quoting.

Even when using reserved words as names, [fully qualified names](identifier-qualifiers.md) do not need to be quoted. For example, `test.select` has only one possible meaning, so it is correctly parsed even without quotes.

### Unquoted

The following characters are valid, and allow identifiers to be unquoted:

* ASCII: \[0-9,a-z,A-Z$\_] (numerals 0-9, basic Latin letters, both lowercase and uppercase, dollar sign, underscore)
* Extended: U+0080 .. U+FFFF

### Quoted

The following characters are valid, but identifiers using them must be quoted:

* ASCII: U+0001 .. U+007F (full Unicode Basic Multilingual Plane (BMP) except for U+0000)
* Extended: U+0080 .. U+FFFF
* Identifier quotes can themselves be used as part of an identifier, as long as they are quoted.

### Further Rules

There are a number of other rules for identifiers:

* Identifiers are stored as Unicode (UTF-8)
* Identifiers may or may not be case-sensitive. See [Indentifier Case-sensitivity](identifier-case-sensitivity.md).
* Database, table and column names can't end with space characters
* Identifier names may begin with a numeral, but can't only contain numerals unless quoted.
* An identifier starting with a numeral, followed by an 'e', may be parsed as a floating point number, and needs to be quoted.
* Identifiers are not permitted to contain the ASCII NUL character (U+0000) and supplementary characters (U+10000 and higher).
* Names such as 5e6, 9e are not prohibited, but it's strongly recommended not to use them, as they could lead to ambiguity in certain contexts, being treated as a number or expression.
* User variables cannot be used as part of an identifier, or as an identifier in an SQL statement.

### Quote Character

The regular quote character is the backtick character - \`\`\`, but if the `ANSI_QUOTES` [SQL\_MODE](../../../server-management/variables-and-modes/sql-mode.md) option is specified, a regular double quote - `"` may be used as well.

The backtick character can be used as part of an identifier. In that case the identifier needs to be quoted. The quote character can be the backtick, but in that case, the backtick in the name must be escaped with another backtick.

### Maximum Length

* Databases, tables, columns, indexes, constraints, stored routines, triggers, events, views, tablespaces, servers and log file groups have a maximum length of 64 characters.
* Compound statement [labels](../../sql-statements/programmatic-compound-statements/labels.md) have a maximum length of 16 characters
* Aliases have a maximum length of 256 characters, except for column aliases in [CREATE VIEW](../../../server-usage/views/create-view.md) statements, which are checked against the maximum column length of 64 characters (not the maximum alias length of 256 characters).
* Users have a maximum length of 80 characters.
* [Roles](../../../security/user-account-management/roles/) have a maximum length of 128 characters.
* Multi-byte characters do not count extra towards the character limit.

### Multiple Identifiers

MariaDB allows the column name to be used on its own if the reference will be unambiguous, or the table name to be used with the column name, or all three of the database, table and column names. A period is used to separate the identifiers, and the period can be surrounded by spaces.

### Examples

Using the period to separate identifiers:

```
CREATE TABLE t1 (i int);

INSERT INTO t1(i) VALUES (10);

SELECT i FROM t1;
+------+
| i    |
+------+
|   10 |
+------+

SELECT t1.i FROM t1;
+------+
| i    |
+------+
|   10 |
+------+

SELECT test.t1.i FROM t1;
+------+
| i    |
+------+
|   10 |
+------+
```

The period can be separated by spaces:

```
SELECT test . t1 . i FROM t1;
+------+
| i    |
+------+
|   10 |
+------+
```

Resolving ambiguity:

```
CREATE TABLE t2 (i int);

SELECT i FROM t1 LEFT JOIN t2 ON t1.i=t2.i;
ERROR 1052 (23000): Column 'i' in field list is ambiguous

SELECT t1.i FROM t1 LEFT JOIN t2 ON t1.i=t2.i;
+------+
| i    |
+------+
|   10 |
+------+
```

Creating a table with characters that require quoting:

```
CREATE TABLE 123% (i int);
ERROR 1064 (42000): You have an error in your SQL syntax; 
  check the manual that corresponds to your MariaDB server version for the right syntax 
  to use near '123% (i int)' at line 1

CREATE TABLE `123%` (i int);
Query OK, 0 rows affected (0.85 sec)

CREATE TABLE `TABLE` (i int);
Query OK, 0 rows affected (0.36 sec)
```

Using double quotes as a quoting character:

```
CREATE TABLE "SELECT" (i int);
ERROR 1064 (42000): You have an error in your SQL syntax; 
  check the manual that corresponds to your MariaDB server version for the right syntax 
  to use near '"SELECT" (i int)' at line 1

SET sql_mode='ANSI_QUOTES';
Query OK, 0 rows affected (0.03 sec)

CREATE TABLE "SELECT" (i int);
Query OK, 0 rows affected (0.46 sec)
```

Using an identifier quote as part of an identifier name:

```
SHOW VARIABLES LIKE 'sql_mode';
+---------------+-------------+
| Variable_name | Value       |
+---------------+-------------+
| sql_mode      | ANSI_QUOTES |
+---------------+-------------+

CREATE TABLE "fg`d" (i int);
Query OK, 0 rows affected (0.34 sec)
```

Creating the table named `*` (Unicode number: U+002A) requires quoting.

```
CREATE TABLE `*` (a INT);
```

Floating point ambiguity:

```
CREATE TABLE 8984444cce5d (x INT);
Query OK, 0 rows affected (0.38 sec)

CREATE TABLE 8981e56cce5d (x INT);
ERROR 1064 (42000): You have an error in your SQL syntax; 
  check the manual that corresponds to your MariaDB server version for the right syntax 
  to use near '8981e56cce5d (x INT)' at line 1

CREATE TABLE `8981e56cce5d` (x INT);
Query OK, 0 rows affected (0.39 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
