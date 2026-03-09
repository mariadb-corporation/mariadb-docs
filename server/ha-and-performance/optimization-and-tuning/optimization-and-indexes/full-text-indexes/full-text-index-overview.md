---
description: >-
  Definitive full-text index guide: MATCH() AGAINST syntax, FULLTEXT index
  creation, NATURAL/BOOLEAN/QUERY EXPANSION modes, stopwords,
  ft_min_word_length.
---

# Full-Text Index Overview

MariaDB has support for full-text indexing and searching:

* A full-text index in MariaDB is an index of type FULLTEXT, and it allows more options when searching for portions of text from a field.
* Full-text indexes can be used only with [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/), [Aria](../../../../server-usage/storage-engines/aria/), [InnoDB](../../../../server-usage/storage-engines/innodb/) and [Mroonga](../../../../server-usage/storage-engines/mroonga/) tables, and can be created only for [CHAR](../../../../reference/data-types/string-data-types/char.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), or [TEXT](../../../../reference/data-types/string-data-types/text.md) columns.
* [Partitioned tables](../../../../server-usage/partitioning-tables/) cannot contain fulltext indexes, even if the storage engine supports them.
* A FULLTEXT index definition can be given in the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement when a\
  table is created, or added later using [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) or [CREATE INDEX](../../../../reference/sql-statements/data-definition/create/create-index.md).
* For large data sets, it is much faster to load your data into a table that\
  has no FULLTEXT index and then create the index after that, than to load data\
  into a table that has an existing FULLTEXT index.

Full-text searching is performed using [MATCH() ... AGAINST](../../../../reference/sql-functions/string-functions/match-against.md) syntax. MATCH() takes a comma-separated list that names the columns to be searched. AGAINST takes a string to search for, and an optional modifier that indicates what type of search to perform. The search string must be a literal string, not a variable or a column name.

```sql
MATCH (col1,col2,...) AGAINST (expr [search_modifier])
```

## Excluded Results

* Partial words are excluded.
* Words less than 4 (MyISAM) or 3 (InnoDB) characters in length will not be stored in the fulltext index. This value can be adjusted by changing the [ft\_min\_word\_length](../../system-variables/server-system-variables.md#ft_min_word_len) system variable (or, for [InnoDB](../../../../server-usage/storage-engines/innodb/), [innodb\_ft\_min\_token\_size](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_ft_min_token_size)).
* Words longer than 84 characters in length will also not be stored in the fulltext index. This values can be adjusted by changing the [ft\_max\_word\_length](../../system-variables/server-system-variables.md#ft_max_word_len) system variable (or, for [InnoDB](../../../../server-usage/storage-engines/innodb/), [innodb\_ft\_max\_token\_size](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)).
* Stopwords are a list of common words such as "once" or "then" that do not reflect in the search results unless IN BOOLEAN MODE is used. The stopword list for MyISAM/Aria tables and InnoDB tables can differ. See [stopwords](full-text-index-stopwords.md) for details and a full list, as well as for details on how to change the default list.
* For MyISAM/Aria fulltext indexes only, if a word appears in more than half the rows, it is also excluded from the results of a fulltext search.
* For InnoDB indexes, only committed rows appear - modifications from the current transaction do not apply.

## Relevance

MariaDB calculates a relevance for each result, based on a number of factors, including the number of words in the index, the number of unique words in a row, the total number of words in both the index and the result, and the weight of the word. In English, 'cool' will be weighted less than 'dandy', at least at present! The relevance can be returned as part of a query simply by using the MATCH function in the field list.

## Types of Full-Text search

### IN NATURAL LANGUAGE MODE

IN NATURAL LANGUAGE MODE is the default type of full-text search, and the keywords can be omitted. There are no special operators, and searches consist of one or more comma-separated keywords.

Searches are returned in descending order of relevance.

### IN BOOLEAN MODE

Boolean search permits the use of a number of special operators:

| Operator | Description                                                                                                                                                                                                                                                 |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| +        | The word is mandatory in all rows returned.                                                                                                                                                                                                                 |
| -        | The word cannot appear in any row returned.                                                                                                                                                                                                                 |
| <        | The word that follows has a lower relevance than other words, although rows containing it will still match                                                                                                                                                  |
| >        | The word that follows has a higher relevance than other words.                                                                                                                                                                                              |
| ()       | Used to group words into subexpressions.                                                                                                                                                                                                                    |
| \~       | The word following contributes negatively to the relevance of the row (which is different to the '-' operator, which specifically excludes the word, or the '<' operator, which still causes the word to contribute positively to the relevance of the row. |
| \*       | The wildcard, indicating zero or more characters. It can only appear at the end of a word.                                                                                                                                                                  |
| "        | Anything enclosed in the double quotes is taken as a whole (so you can match phrases, for example).                                                                                                                                                         |

Searches are not returned in order of relevance, and nor does the 50% limit apply. Stopwords and word minimum and maximum lengths still apply as usual.

### WITH QUERY EXPANSION

A query expansion search is a modification of a natural language search. The search string is used to perform a regular natural language search. Then, words from the most relevant rows returned by the search are added to the search string and the search is done again. The query returns the rows from the second search. The IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION or WITH QUERY EXPANSION modifier specifies a query expansion search. It can be useful when relying on implied knowledge within the data, for example that MariaDB is a database.

## Examples

Creating a table, and performing a basic search:

```sql
CREATE TABLE ft_myisam(copy TEXT,FULLTEXT(copy)) ENGINE=MyISAM;

INSERT INTO ft_myisam(copy) VALUES ('Once upon a time'),
  ('There was a wicked witch'), ('Who ate everybody up');

SELECT * FROM ft_myisam WHERE MATCH(copy) AGAINST('wicked');
+--------------------------+
| copy                     |
+--------------------------+
| There was a wicked witch |
+--------------------------+
```

Multiple words:

```sql
SELECT * FROM ft_myisam WHERE MATCH(copy) AGAINST('wicked,witch');
+---------------------------------+
| copy                            |
+---------------------------------+
| There was a wicked witch        |
+---------------------------------+
```

Since 'Once' is a [stopword](full-text-index-stopwords.md), no result is returned:

```sql
SELECT * FROM ft_myisam WHERE MATCH(copy) AGAINST('Once');
Empty set (0.00 sec)
```

Inserting the word 'wicked' into more than half the rows excludes it from the results:

```sql
INSERT INTO ft_myisam(copy) VALUES ('Once upon a wicked time'),
  ('There was a wicked wicked witch'), ('Who ate everybody wicked up');

SELECT * FROM ft_myisam WHERE MATCH(copy) AGAINST('wicked');
Empty set (0.00 sec)
```

Using IN BOOLEAN MODE to overcome the 50% limitation:

```sql
SELECT * FROM ft_myisam WHERE MATCH(copy) AGAINST('wicked' IN BOOLEAN MODE);
+---------------------------------+
| copy                            |
+---------------------------------+
| There was a wicked witch        |
| Once upon a wicked time         |
| There was a wicked wicked witch |
| Who ate everybody wicked up     |
+---------------------------------+
```

Returning the relevance:

```sql
SELECT copy,MATCH(copy) AGAINST('witch') AS relevance 
  FROM ft_myisam WHERE MATCH(copy) AGAINST('witch');
+---------------------------------+--------------------+
| copy                            | relevance          |
+---------------------------------+--------------------+
| There was a wicked witch        | 0.6775632500648499 |
| There was a wicked wicked witch | 0.5031757950782776 |
+---------------------------------+--------------------+
```

WITH QUERY EXPANSION. In the following example, 'MariaDB' is always associated with the word 'database', so it is returned when query expansion is used, even though not explicitly requested.

```sql
CREATE TABLE ft2(copy TEXT,FULLTEXT(copy)) ENGINE=MyISAM;

INSERT INTO ft2(copy) VALUES
 ('MySQL vs MariaDB database'),
 ('Oracle vs MariaDB database'), 
 ('PostgreSQL vs MariaDB database'),
 ('MariaDB overview'),
 ('Foreign keys'),
 ('Primary keys'),
 ('Indexes'),
 ('Transactions'),
 ('Triggers');

SELECT * FROM ft2 WHERE MATCH(copy) AGAINST('database');
+--------------------------------+
| copy                           |
+--------------------------------+
| MySQL vs MariaDB database      |
| Oracle vs MariaDB database     |
| PostgreSQL vs MariaDB database |
+--------------------------------+
3 rows in set (0.00 sec)

SELECT * FROM ft2 WHERE MATCH(copy) AGAINST('database' WITH QUERY EXPANSION);
+--------------------------------+
| copy                           |
+--------------------------------+
| MySQL vs MariaDB database      |
| Oracle vs MariaDB database     |
| PostgreSQL vs MariaDB database |
| MariaDB overview               |
+--------------------------------+
4 rows in set (0.00 sec)
```

Partial word matching with IN BOOLEAN MODE:

```sql
SELECT * FROM ft2 WHERE MATCH(copy) AGAINST('Maria*' IN BOOLEAN MODE);
+--------------------------------+
| copy                           |
+--------------------------------+
| MySQL vs MariaDB database      |
| Oracle vs MariaDB database     |
| PostgreSQL vs MariaDB database |
| MariaDB overview               |
+--------------------------------+
```

Using boolean operators

```sql
SELECT * FROM ft2 WHERE MATCH(copy) AGAINST('+MariaDB -database' 
  IN BOOLEAN MODE);
+------------------+
| copy             |
+------------------+
| MariaDB overview |
+------------------+
```

## See Also

* For simpler searches of a substring in text columns, see the [LIKE](../../../../reference/sql-functions/string-functions/like.md) operator.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
