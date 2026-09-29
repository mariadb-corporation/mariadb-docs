---
description: >-
  ANSI SQL:2016 features that GridGain 9 supports out of the box, with the
  support level and any limitations for each feature and subfeature.
---

# Supported SQL Features

GridGain supports most of the major features of ANSI SQL 2016 standard out-of-the-box. The following table shows the features supported in GridGain:

| Feature ID | Feature Name | Subfeature ID | Subfeature Name | Support Level | Limitations |
|---|---|---|---|---|---|
| E011 | Numeric data types | E011 |  | Full |  |
| E011 | Numeric data types | E011-01 | INTEGER and SMALLINT data types | Full |  |
| E011 | Numeric data types | E011-02 | REAL, DOUBLE PRECISION, and FLOAT data types | Full |  |
| E011 | Numeric data types | E011-03 | DECIMAL and NUMERIC data types | Full | DEC and NUMERIC types are not supported |
| E011 | Numeric data types | E011-04 | Arithmetic operators | Full |  |
| E011 | Numeric data types | E011-05 | Numeric comparison | Full |  |
| E011 | Numeric data types | E011-06 | Implicit casting among the numeric data types | Full |  |
| E021 | Character data types | E021 |  | Full | CHARACTER type cannot be used in table definition |
| E021 | Character string types | E021-01 | CHARACTER data type | Full |  |
| E021 | Character string types | E021-02 | CHARACTER VARYING data type | Full |  |
| E021 | Character string types | E021-03 | Character literals | Full |  |
| E021 | Character string types | E021-04 | CHARACTER_LENGTH function | Full |  |
| E021 | Character string types | E021-05 | OCTET_LENGTH function | Full |  |
| E021 | Character string types | E021-06 | SUBSTRING function | Full |  |
| E021 | Character string types | E021-07 | Character concatenation | Full |  |
| E021 | Character string types | E021-08 | UPPER and LOWER functions | Full |  |
| E021 | Character string types | E021-09 | TRIM function | Full |  |
| E021 | Character string types | E021-10 | Implicit casting among the character string types | Full |  |
| E021 | Character string types | E021-11 | POSITION function | Full |  |
| E021 | Character string types | E021-12 | Character comparison | Full |  |
| E031 | Identifiers | E031 |  | Full |  |
| E031 | Identifiers | E031-01 | Delimited identifiers | Full |  |
| E031 | Identifiers | E031-02 | Lower case identifiers | Full |  |
| E031 | Identifiers | E031-03 | Trailing underscore | Full |  |
| E051 | Basic query specification | E051 |  | Full |  |
| E051 | Basic query specification | E051-01 | SELECT DISTINCT | Full |  |
| E051 | Basic query specification | E051-02 | GROUP BY clause | Full |  |
| E051 | Basic query specification | E051-04 | GROUP BY can contain columns not in &lt;select list&gt; | Full |  |
| E051 | Basic query specification | E051-05 | Select list items can be renamed | Full |  |
| E051 | Basic query specification | E051-06 | HAVING clause | Full |  |
| E051 | Basic query specification | E051-07 | Qualified * in select list | Full |  |
| E051 | Basic query specification | E051-08 | Correlation names in the FROM clause | Full |  |
| E051 | Basic query specification | E051-09 | Rename columns in the FROM clause | Full |  |
| E061 | Basic predicates and search conditions | E061 |  | Full |  |
| E061 | Basic predicates and search conditions | E061-01 | Comparison predicate | Full |  |
| E061 | Basic predicates and search conditions | E061-02 | BETWEEN predicate | Full |  |
| E061 | Basic predicates and search conditions | E061-03 | IN predicate with list of values | Full |  |
| E061 | Basic predicates and search conditions | E061-04 | LIKE predicate | Full |  |
| E061 | Basic predicates and search conditions | E061-05 | LIKE predicate ESCAPE clause | Full |  |
| E061 | Basic predicates and search conditions | E061-06 | NULL predicate | Full |  |
| E061 | Basic predicates and search conditions | E061-07 | Quantified comparison predicate | Full |  |
| E061 | Basic predicates and search conditions | E061-08 | EXISTS predicate | Full |  |
| E061 | Basic predicates and search conditions | E061-09 | Subqueries in comparison predicate | Full |  |
| E061 | Basic predicates and search conditions | E061-11 | Subqueries in IN predicate | Full |  |
| E061 | Basic predicates and search conditions | E061-12 | Subqueries in quantified comparison predicate | Full |  |
| E061 | Basic predicates and search conditions | E061-13 | Correlated subqueries | Full |  |
| E061 | Basic predicates and search conditions | E061-14 | Search condition | Full |  |
| E071 | Basic query expressions | E071 |  | Full |  |
| E071 | Basic query expressions | E071-01 | UNION DISTINCT table operator | Full |  |
| E071 | Basic query expressions | E071-02 | UNION ALL table operator | Full |  |
| E071 | Basic query expressions | E071-03 | EXCEPT DISTINCT table operator | Full |  |
| E071 | Basic query expressions | E071-05 | Columns combined via table operators need not have exactly the same data type | Full |  |
| E071 | Basic query expressions | E071-06 | Table operators in subqueries | Full |  |
| E091 | Set functions | E091 |  | Full |  |
| E091 | Set functions | E091-01 | AVG | Full |  |
| E091 | Set functions | E091-02 | COUNT | Full |  |
| E091 | Set functions | E091-03 | MAX | Full |  |
| E091 | Set functions | E091-04 | MIN | Full |  |
| E091 | Set functions | E091-05 | SUM | Full |  |
| E091 | Set functions | E091-06 | ALL quantifier | Full |  |
| E091 | Set functions | E091-07 | DISTINCT quantifier | Full |  |
| E101 | Basic data manipulation | E101 |  | Full |  |
| E101 | Basic data manipulation | E101-01 | INSERT statement | Full |  |
| E101 | Basic data manipulation | E101-03 | Searched UPDATE statement | Full |  |
| E101 | Basic data manipulation | E101-04 | Searched DELETE statement | Full |  |
| E111 | Single row SELECT statement | E111 |  | Full |  |
| E131 | Null value support (nulls in lieu of values) | E131 |  | Full |  |
| E141 | Basic integrity constraints | E141 |  | Partial | NOT NULL and PRIMARY KEY constraints. |
| E141 | Basic integrity constraints | E141-01 | NOT NULL constraints | Full |  |
| E141 | Basic integrity constraints | E141-03 | PRIMARY KEY constraints | Full |  |
| E141 | Basic integrity constraints | E141-07 | Column defaults | Partial | Literals, RAND_UUID function, CURRENT_TIMESTAMP + INTERVAL literal |
| E141 | Basic integrity constraints | E141-08 | NOT NULL inferred on PRIMARY KEY | Full |  |
| E151 | Transaction support | E151 |  | Partial |  |
| E151 | Transaction support | E151-01 | COMMIT statement | Partial | Only in SQL scripts. No options. |
| E151 | Transaction support | E151-02 | ROLLBACK statement | Partial | Only in SQL scripts. No options. Savepoints are not supported |
| E153 | Updatable queries with subqueries | E153 |  | Full |  |
| E161 | SQL comments using leading double minus | E161 |  | Full |  |
| F031 | Basic schema manipulation | F031 |  | Partial | CREATE TABLE, ALTER TABLE, DROP TABLE |
| F031 | Basic schema manipulation | F031-01 | CREATE TABLE statement to create persistent base tables | Partial | CREATE TABLE must always specify primary key |
| F031 | Basic schema manipulation | F031-04 | ALTER TABLE statement: ADD COLUMN clause | Full |  |
| F033 | ALTER TABLE statement: DROP COLUMN clause | F033 |  | Partial | DROP behaviour is not supported |
| F041 | Basic joined table | F041 |  | Full |  |
| F041 | Basic joined table | F041-01 | Inner join (but not necessarily the INNER keyword) | Full |  |
| F041 | Basic joined table | F041-02 | INNER keyword | Full |  |
| F041 | Basic joined table | F041-03 | LEFT OUTER JOIN | Full |  |
| F041 | Basic joined table | F041-04 | RIGHT OUTER JOIN | Full |  |
| F041 | Basic joined table | F041-05 | Outer joins can be nested | Full |  |
| F041 | Basic joined table | F041-07 | The inner table in a left or right outer join can also be used in an inner join | Full |  |
| F041 | Basic joined table | F041-08 | All comparison operators are supported (rather than just =) | Full |  |
| F051 | Basic date and time | F051 |  | Full |  |
| F051 | Basic date and time | F051-01 | DATE data type (including support of DATE literal) | Full |  |
| F051 | Basic date and time | F051-02 | TIME data type (including support of TIME literal) with fractional seconds precision of at least 0 | Partial | TIME WITH TIME ZONE type is not supported. Does not support sub-ms precision |
| F051 | Basic date and time | F051-03 | TIMESTAMP data type (including support of TIMESTAMP literal) with fractional seconds precision of at least 0 and 6 | Partial | TIMESTAMP WITH TIME ZONE is not supported. Does not support sub-ms precision |
| F051 | Basic date and time | F051-04 | Comparison predicate on DATE, TIME, and TIMESTAMP data types | Full |  |
| F051 | Basic date and time | F051-05 | Explicit CAST between datetime types and character string types | Full |  |
| F051 | Basic date and time | F051-06 | CURRENT_DATE | Full |  |
| F051 | Basic date and time | F051-07 | LOCALTIME | Full |  |
| F051 | Basic date and time | F051-08 | LOCALTIMESTAMP | Full |  |
| F052 | Intervals and datetime arithmetic | F052 |  | Full |  |
| F171 | Multiple schemas per user | F171 |  | Full |  |
| F201 | CAST function | F201 |  | Full |  |
| F221 | Explicit defaults | F221 |  | Full |  |
| F261 | CASE expression | F261 |  | Full |  |
| F261 | CASE expression | F261-01 | Simple CASE | Full |  |
| F261 | CASE expression | F261-02 | Searched CASE | Full |  |
| F261 | CASE expression | F261-03 | NULLIF | Full |  |
| F261 | CASE expression | F261-04 | COALESCE | Full |  |
| F302 | INTERSECT table operator | F302 |  | Full |  |
| F302 | INTERSECT table operator | F302-01 | INTERSECT DISTINCT table operator | Full |  |
| F302 | INTERSECT table operator | F302-02 | INTERSECT ALL table operator | Full |  |
| F304 | EXCEPT ALL table operator | F304 |  | Full |  |
| F311 | Schema definition statement | F311 |  | Partial |  |
| F311 | Schema definition statement | F311-01 | CREATE SCHEMA | Full | Schema elements are not supported |
| F381 | Extended schema manipulation | F381-01 | ALTER TABLE statement: ALTER COLUMN clause | Partial | Default can not be set to non-constant in most cases. See DDL docs |
| F391 | Long identifiers | F391 |  | Full | Up to 128 characters |
| F392 | Unicode escapes in identifiers | F392 |  | Partial | Partial support of unicode escapes |
| F401 | Extended joined table | F401 |  | Full |  |
| F401 | Extended joined table | F401-01 | NATURAL JOIN | Full |  |
| F401 | Extended joined table | F401-02 | FULL OUTER JOIN | Full |  |
| F401 | Extended joined table | F401-04 | CROSS JOIN | Full |  |
| F404 | Range variable for common column names | F404 |  | Full |  |
| F411 | Time zone specification | F411 |  | Full |  |
| F471 | Scalar subquery values | F471 |  | Full |  |
| F561 | Full value expressions | F561 |  | Full |  |
| F571 | Truth value tests | F571 |  | Partial | UNKNOWN is not supported |
| F591 | Derived tables | F591 |  | Full |  |
| F661 | Simple tables | F661 |  | Full |  |
| F781 | Self-referencing operations | F781 |  | Full |  |
| F850 | Top-level &lt;order by clause&gt; in &lt;query expression&gt; | F850 |  | Full |  |
| F851 | &lt;order by clause&gt; in subqueries | F851 |  | Full |  |
| F855 | Nested &lt;order by clause&gt; in &lt;query expression&gt; | F855 |  | Full |  |
| F861 | Top-level &lt;result offset clause&gt; in &lt;query expression&gt; | F861 |  | Full |  |
| F862 | &lt;result offset clause&gt; in subqueries | F862 |  | Full |  |
| F863 | Nested &lt;result offset clause&gt; in &lt;query expression&gt; | F863 |  | Full |  |
| T021 | BINARY and VARBINARY data types | T021 |  | Full | BINARY type cannot be used in table definition |
| T031 | BOOLEAN data type | T031 |  | Full |  |
| T071 | BIGINT data type | T071 |  | Full |  |
| T121 | WITH (excluding RECURSIVE) in query expression | T121 |  | Full |  |
| T122 | WITH (excluding RECURSIVE) in subquery | T122 |  | Full |  |
| T141 | SIMILAR predicate | T141 |  | Full |  |
| T151 | DISTINCT predicate | T151 |  | Full |  |
| T152 | DISTINCT predicate with negation | T152 |  | Full |  |
| T285 | Enhanced derived column names | T285 |  | Full |  |
| T312 | OVERLAY function | T312 |  | Full |  |
| T351 | Bracketed SQL comments (/*...*/ comments) | T351 |  | Full |  |
| T431 | Extended grouping capabilities | T431 |  | Full |  |
| T433 | Multiargument GROUPING function | T433 |  | Full |  |
| T434 | GROUP BY DISTINCT | T434 |  | Full |  |
| T441 | ABS and MOD functions | T441 |  | Full |  |
| T501 | Enhanced EXISTS predicate | T501 |  | Full |  |
| T551 | Optional key words for default syntax | T551 |  | Full |  |
| T621 | Enhanced numeric functions | T621 |  | Full |  |
| T622 | Trigonometric functions | T622 |  | Full |  |
| T623 | General logarithm functions | T623 |  | Full |  |
| T624 | Common logarithm functions | T624 |  | Full |  |
| T631 | IN predicate with one list element | T631 |  | Full |  |
| T828 | JSON_QUERY | T828 |  | Full |  |
| T829 | JSON_QUERY: array wrapper options | T829 |  | Full |  |
| T839 | Formatted cast of datetimes to/from character strings | T839 |  | Full |  |
