---
description: >-
  The ANSI SQL:2016 features that GridGain 9 does not support, listed by feature
  ID with alternatives where available.
---

# Unsupported SQL Features

GridGain does not support the following ANSI SQL 2016 features.

| Feature ID | Feature Name | Subfeature ID | Subfeature Name | Alternative |
|---|---|---|---|---|
| B011 | Embedded Ada | B011 |  |  |
| B012 | Embedded C | B012 |  |  |
| B013 | Embedded COBOL | B013 |  |  |
| B014 | Embedded Fortran | B014 |  |  |
| B015 | Embedded MUMPS | B015 |  |  |
| B016 | Embedded Pascal | B016 |  |  |
| B017 | Embedded PL/I | B017 |  |  |
| B031 | Basic dynamic SQL | B031 |  |  |
| B032 | Extended dynamic SQL | B032 |  |  |
| B032 | Extended dynamic SQL | B032-01 | `<describe input statement>` |  |
| B033 | Untyped SQL-invoked function arguments | B033 |  |  |
| B034 | Dynamic specification of cursor attributes | B034 |  |  |
| B035 | Non-extended descriptor names | B035 |  |  |
| B041 | Extensions to embedded SQL exception declarations | B041 |  |  |
| B051 | Enhanced execution rights | B051 |  |  |
| B111 | Module language Ada | B111 |  |  |
| B112 | Module language C | B112 |  |  |
| B113 | Module language COBOL | B113 |  |  |
| B114 | Module language Fortran | B114 |  |  |
| B115 | Module language MUMPS | B115 |  |  |
| B116 | Module language Pascal | B116 |  |  |
| B117 | Module language PL/I | B117 |  |  |
| B121 | Routine language Ada | B121 |  |  |
| B122 | Routine language C | B122 |  |  |
| B123 | Routine language COBOL | B123 |  |  |
| B124 | Routine language Fortran | B124 |  |  |
| B125 | Routine language MUMPS | B125 |  |  |
| B126 | Routine language Pascal | B126 |  |  |
| B127 | Routine language PL/I | B127 |  |  |
| B128 | Routine language SQL | B128 |  |  |
| B200 | Polymorphic table functions | B200 |  |  |
| B201 | More than one PTF generic table parameter | B201 |  |  |
| B202 | PTF Copartitioning | B202 |  |  |
| B203 | More than one copartition specification | B203 |  |  |
| B204 | PRUNE WHEN EMPTY | B204 |  |  |
| B205 | Pass-through columns | B205 |  |  |
| B206 | PTF descriptor parameters | B206 |  |  |
| B207 | Cross products of partitionings | B207 |  |  |
| B208 | PTF component procedure interface | B208 |  |  |
| B209 | PTF extended names | B209 |  |  |
| B211 | Module language Ada: VARCHAR and NUMERIC support | B211 |  |  |
| B221 | Routine language Ada: VARCHAR and NUMERIC support | B221 |  |  |
| E081 | Basic Privileges | E081 |  | [RBAC statements](../../../security/authentication.md#basic-authentication) |
| E081 | Basic Privileges | E081-01 | SELECT privilege | [RBAC statements](../../../security/authentication.md#basic-authentication) |
| E081 | Basic Privileges | E081-02 | DELETE privilege | [RBAC statements](../../../security/authentication.md#basic-authentication) |
| E081 | Basic Privileges | E081-03 | INSERT privilege at the table level | [RBAC statements](../../../security/authentication.md#basic-authentication) |
| E081 | Basic Privileges | E081-04 | UPDATE privilege at the table level | [RBAC statements](../../../security/authentication.md#basic-authentication) |
| E081 | Basic Privileges | E081-05 | UPDATE privilege at the column level |  |
| E081 | Basic Privileges | E081-06 | REFERENCES privilege at the table level |  |
| E081 | Basic Privileges | E081-07 | REFERENCES privilege at the column level |  |
| E081 | Basic Privileges | E081-08 | WITH GRANT OPTION |  |
| E081 | Basic Privileges | E081-09 | USAGE privilege |  |
| E081 | Basic Privileges | E081-10 | EXECUTE privilege |  |
| E121 | Basic cursor support | E121 |  |  |
| E121 | Basic cursor support | E121-01 | DECLARE CURSOR |  |
| E121 | Basic cursor support | E121-02 | ORDER BY columns need not be in select list |  |
| E121 | Basic cursor support | E121-03 | Value expressions in ORDER BY clause |  |
| E121 | Basic cursor support | E121-04 | OPEN statement |  |
| E121 | Basic cursor support | E121-06 | Positioned UPDATE statement |  |
| E121 | Basic cursor support | E121-07 | Positioned DELETE statement |  |
| E121 | Basic cursor support | E121-08 | CLOSE statement |  |
| E121 | Basic cursor support | E121-10 | FETCH statement implicit NEXT |  |
| E121 | Basic cursor support | E121-17 | WITH HOLD cursors |  |
| E141 | Basic integrity constraints | E141-02 | UNIQUE constraints of NOT NULL columns |  |
| E141 | Basic integrity constraints | E141-04 | Basic FOREIGN KEY constraint with the NO ACTION default for both referential delete action and referential update action |  |
| E141 | Basic integrity constraints | E141-06 | CHECK constraints |  |
| E141 | Basic integrity constraints | E141-10 | Names in a foreign key can be specified in any order |  |
| E152 | Basic SET TRANSACTION statement | E152 |  |  |
| E152 | Basic SET TRANSACTION statement | E152-01 | SET TRANSACTION statement: ISOLATION LEVEL SERIALIZABLE clause |  |
| E152 | Basic SET TRANSACTION statement | E152-02 | SET TRANSACTION statement: READ ONLY and READ WRITE clauses |  |
| E171 | SQLSTATE support | E171 |  | JDBC error codes, ODBC error codes |
| E182 | Host language binding | E182 |  |  |
| F021 | Basic information schema | F021 |  |  |
| F021 | Basic information schema | F021-01 | COLUMNS view |  |
| F021 | Basic information schema | F021-02 | TABLES view |  |
| F021 | Basic information schema | F021-03 | VIEWS view |  |
| F021 | Basic information schema | F021-04 | TABLE_CONSTRAINTS view |  |
| F021 | Basic information schema | F021-05 | REFERENTIAL_CONSTRAINTS view |  |
| F021 | Basic information schema | F021-06 | CHECK_CONSTRAINTS view |  |
| F031 | Basic schema manipulation | F031-02 | CREATE VIEW statement |  |
| F031 | Basic schema manipulation | F031-03 | GRANT statement | [RBAC statements](../../../security/authentication.md#basic-authentication) |
| F031 | Basic schema manipulation | F031-13 | DROP TABLE statement: RESTRICT clause |  |
| F031 | Basic schema manipulation | F031-16 | DROP VIEW statement: RESTRICT clause |  |
| F031 | Basic schema manipulation | F031-19 | REVOKE statement: RESTRICT clause |  |
| F032 | CASCADE drop behavior | F032 |  |  |
| F034 | Extended REVOKE statement | F034 |  |  |
| F034 | Extended REVOKE statement | F034-01 | REVOKE statement performed by other than the owner of a schema object |  |
| F034 | Extended REVOKE statement | F034-02 | REVOKE statement: GRANT OPTION FOR clause |  |
| F034 | Extended REVOKE statement | F034-03 | REVOKE statement to revoke a privilege that the grantee has WITH GRANT OPTION |  |
| F053 | OVERLAPS predicate | F053 |  |  |
| F054 | TIMESTAMP in DATE type precedence list | F054 |  |  |
| F081 | UNION and EXCEPT in views | F081 |  |  |
| F111 | Isolation levels other than SERIALIZABLE | F111 |  |  |
| F111 | Isolation levels other than SERIALIZABLE | F111-01 | READ UNCOMMITTED isolation level |  |
| F111 | Isolation levels other than SERIALIZABLE | F111-02 | READ COMMITTED isolation level |  |
| F111 | Isolation levels other than SERIALIZABLE | F111-03 | REPEATABLE READ isolation level |  |
| F121 | Basic diagnostics management | F121 |  |  |
| F121 | Basic diagnostics management | F121-01 | GET DIAGNOSTICS statement |  |
| F121 | Basic diagnostics management | F121-02 | SET TRANSACTION statement: DIAGNOSTICS SIZE clause |  |
| F122 | Enhanced diagnostics management | F122 |  |  |
| F123 | All diagnostics | F123 |  |  |
| F131 | Grouped operations | F131 |  |  |
| F131 | Grouped operations | F131-01 | WHERE, GROUP BY, and HAVING clauses supported in queries with grouped views |  |
| F131 | Grouped operations | F131-02 | Multiple tables supported in queries with grouped views |  |
| F131 | Grouped operations | F131-03 | Set functions supported in queries with grouped views |  |
| F131 | Grouped operations | F131-04 | Subqueries with GROUP BY and HAVING clauses and grouped views |  |
| F131 | Grouped operations | F131-05 | Single row SELECT with GROUP BY and HAVING clauses and grouped views |  |
| F181 | Multiple module support | F181 |  |  |
| F191 | Referential delete actions | F191 | FK is not a priority right now |  |
| F200 | TRUNCATE TABLE statement | F200 |  |  |
| F202 | TRUNCATE TABLE: identity column restart option | F202 |  |  |
| F222 | INSERT statement: DEFAULT VALUES clause | F222 |  |  |
| F231 | Privilege tables | F231 |  |  |
| F231 | Privilege tables | F231-01 | TABLE_PRIVILEGES view |  |
| F231 | Privilege tables | F231-02 | COLUMN_PRIVILEGES view |  |
| F231 | Privilege tables | F231-03 | USAGE_PRIVILEGES view |  |
| F251 | Domain support | F251 |  |  |
| F262 | Extended CASE expression | F262 |  |  |
| F263 | Comma-separated predicates in simple CASE expression | F263 |  |  |
| F271 | Compound character literals | F271 |  |  |
| F281 | LIKE enhancements | F281 |  |  |
| F291 | UNIQUE predicate | F291 |  |  |
| F301 | CORRESPONDING in query expressions | F301 |  |  |
| F311 | Schema definition statement | F311-02 | CREATE TABLE for persistent base tables |  |
| F311 | Schema definition statement | F311-03 | CREATE VIEW |  |
| F311 | Schema definition statement | F311-04 | CREATE VIEW: WITH CHECK OPTION |  |
| F311 | Schema definition statement | F311-05 | GRANT statement |  |
| F312 | MERGE statement | F312 |  |  |
| F313 | Enhanced MERGE statement | F313 |  |  |
| F314 | MERGE statement with DELETE branch | F314 |  |  |
| F321 | User authorization | F321 |  |  |
| F341 | Usage tables | F341 |  |  |
| F361 | Subprogram support | F361 |  |  |
| F381 | Extended schema manipulation | F381 |  |  |
| F381 | Extended schema manipulation | F381-02 | ALTER TABLE statement: ADD CONSTRAINT clause |  |
| F381 | Extended schema manipulation | F381-03 | ALTER TABLE statement: DROP CONSTRAINT clause |  |
| F382 | Alter column data type | F382 |  |  |
| F383 | Set column not null clause | F383 |  |  |
| F384 | Drop identity property clause | F384 |  |  |
| F385 | Drop column generation expression clause | F385 |  |  |
| F386 | Set identity column generation clause | F386 |  |  |
| F393 | Unicode escapes in literals | F393 |  |  |
| F394 | Optional normal form specification | F394 |  |  |
| F402 | Named column joins for LOBs, arrays, and multisets | F402 |  |  |
| F403 | Partitioned joined tables | F403 |  |  |
| F421 | National character | F421 |  |  |
| F431 | Read-only scrollable cursors | F431 |  |  |
| F431 | Read-only scrollable cursors | F431-01 | FETCH with explicit NEXT |  |
| F431 | Read-only scrollable cursors | F431-02 | FETCH FIRST |  |
| F431 | Read-only scrollable cursors | F431-03 | FETCH LAST |  |
| F431 | Read-only scrollable cursors | F431-04 | FETCH PRIOR |  |
| F431 | Read-only scrollable cursors | F431-05 | FETCH ABSOLUTE |  |
| F431 | Read-only scrollable cursors | F431-06 | FETCH RELATIVE |  |
| F441 | Extended set function support | F441 |  |  |
| F442 | Mixed column references in set functions | F442 |  |  |
| F451 | Character set definition | F451 |  |  |
| F461 | Named character sets | F461 |  |  |
| F481 | Expanded NULL predicate | F481 |  |  |
| F491 | Constraint management | F491 |  |  |
| F492 | Optional table constraint enforcement | F492 |  |  |
| F501 | Features and conformance views | F501 |  |  |
| F501 | Features and conformance views | F501-01 | SQL_FEATURES view |  |
| F501 | Features and conformance views | F501-02 | SQL_SIZING view |  |
| F502 | Enhanced documentation tables | F502 |  |  |
| F521 | Assertions | F521 |  |  |
| F531 | Temporary tables | F531 |  |  |
| F555 | Enhanced seconds precision | F555 |  |  |
| F611 | Indicator data types | F611 |  |  |
| F641 | Row and table constructors | F641 |  |  |
| F651 | Catalog name qualifiers | F651 |  |  |
| F671 | Subqueries in CHECK | F671 |  |  |
| F672 | Retrospective check constraints | F672 |  |  |
| F673 | Reads SQL-data routine invocations in CHECK constraints | F673 |  |  |
| F690 | Collation support | F690 |  |  |
| F692 | Extended collation support | F692 |  |  |
| F693 | SQL-session and client module collations | F693 |  |  |
| F695 | Translation support | F695 |  |  |
| F696 | Additional translation documentation | F696 |  |  |
| F701 | Referential update actions | F701 |  |  |
| F711 | ALTER domain | F711 |  |  |
| F721 | Deferrable constraints | F721 |  |  |
| F731 | INSERT column privileges | F731 |  |  |
| F741 | Referential MATCH types | F741 |  |  |
| F751 | View CHECK enhancements | F751 |  |  |
| F761 | Session management | F761 |  |  |
| F762 | CURRENT_CATALOG | F762 |  |  |
| F763 | CURRENT_SCHEMA | F763 |  |  |
| F771 | Connection management | F771 |  |  |
| F791 | Insensitive cursors | F791 |  |  |
| F801 | Full set function | F801 |  |  |
| F812 | Basic flagging | F812 |  |  |
| F813 | Extended flagging | F813 |  |  |
| F821 | Local table references | F821 |  |  |
| F831 | Full cursor update | F831 |  |  |
| F831 | Full cursor update | F831-01 | Updatable scrollable cursors |  |
| F831 | Full cursor update | F831-02 | Updatable ordered cursors |  |
| F841 | LIKE_REGEX predicate | F841 |  |  |
| F842 | OCCURRENCES_REGEX function | F842 |  |  |
| F843 | POSITION_REGEX function | F843 |  |  |
| F844 | SUBSTRING_REGEX function | F844 |  |  |
| F845 | TRANSLATE_REGEX function | F845 |  |  |
| F846 | Octet support in regular expression operators | F846 |  |  |
| F847 | Nonconstant regular expressions | F847 |  |  |
| F852 | `Top-level <order by clause> in views` | F852 |  |  |
| F856 | `Nested <fetch first clause> in <query expression>` | F856 |  |  |
| F857 | `Top-level <fetch first clause> in <query expression>` | F857 |  |  |
| F858 | `<fetch first clause> in subqueries` | F858 |  |  |
| F859 | `Top-level <fetch first clause> in views` | F859 |  |  |
| F860 | `<fetch first row count> in <fetch first clause>` | F860 |  |  |
| F864 | `Top-level <result offset clause> in views` | F864 |  |  |
| F865 | `dynamic <offset row count> in <result offset clause>` | F865 |  |  |
| F866 | FETCH FIRST clause: PERCENT option | F866 |  |  |
| F867 | FETCH FIRST clause: WITH TIES option | F867 |  |  |
| M001 | Datalinks | M001 |  |  |
| M002 | Datalinks via SQL/CLI | M002 |  |  |
| M003 | Datalinks via Embedded SQL | M003 |  |  |
| M004 | Foreign data support | M004 |  |  |
| M005 | Foreign schema support | M005 |  |  |
| M006 | GetSQLString routine | M006 |  |  |
| M007 | TransmitRequest | M007 |  |  |
| M009 | GetOpts and GetStatistics routines | M009 |  |  |
| M010 | Foreign data wrapper support | M010 |  |  |
| M011 | Datalinks via Ada | M011 |  |  |
| M012 | Datalinks via C | M012 |  |  |
| M013 | Datalinks via COBOL | M013 |  |  |
| M014 | Datalinks via Fortran | M014 |  |  |
| M015 | Datalinks via M | M015 |  |  |
| M016 | Datalinks via Pascal | M016 |  |  |
| M017 | Datalinks via PL/I | M017 |  |  |
| M018 | Foreign data wrapper interface routines in Ada | M018 |  |  |
| M019 | Foreign data wrapper interface routines in C | M019 |  |  |
| M020 | Foreign data wrapper interface routines in COBOL | M020 |  |  |
| M021 | Foreign data wrapper interface routines in Fortran | M021 |  |  |
| M022 | Foreign data wrapper interface routines in MUMPS | M022 |  |  |
| M023 | Foreign data wrapper interface routines in Pascal | M023 |  |  |
| M024 | Foreign data wrapper interface routines in PL/I | M024 |  |  |
| M030 | SQL-server foreign data support | M030 |  |  |
| M031 | Foreign data wrapper general routines | M031 |  |  |
| R010 | Row pattern recognition: FROM clause | R010 |  |  |
| R020 | Row pattern recognition: WINDOW clause | R020 |  |  |
| R030 | Row pattern recognition: full aggregate support | R030 |  |  |
| S011 | Distinct data types | S011 |  |  |
| S011 | Distinct data types | S011-01 | USER_DEFINED_TYPES view |  |
| S023 | Basic structured types | S023 |  |  |
| S024 | Enhanced structured types | S024 |  |  |
| S025 | Final structured types | S025 |  |  |
| S026 | Self-referencing structured types | S026 |  |  |
| S027 | Create method by specific method name | S027 |  |  |
| S028 | Permutable UDT options list | S028 |  |  |
| S041 | Basic reference types | S041 |  |  |
| S043 | Enhanced reference types | S043 |  |  |
| S051 | Create table of type | S051 |  |  |
| S071 | SQL paths in function and type name resolution | S071 |  |  |
| S081 | Subtables | S081 |  |  |
| S091 | Basic array support | S091 |  |  |
| S091 | Basic array support | S091-01 | Arrays of built-in data types |  |
| S091 | Basic array support | S091-02 | Arrays of distinct types |  |
| S091 | Basic array support | S091-03 | Array expressions |  |
| S092 | Arrays of user-defined types | S092 |  |  |
| S094 | Arrays of reference types | S094 |  |  |
| S095 | Array constructors by query | S095 |  |  |
| S096 | Optional array bounds | S096 |  |  |
| S097 | Array element assignment | S097 |  |  |
| S098 | ARRAY_AGG | S098 |  |  |
| S111 | ONLY in query expressions | S111 |  |  |
| S151 | Type predicate | S151 |  |  |
| S161 | Subtype treatment | S161 |  |  |
| S162 | Subtype treatment for references | S162 |  |  |
| S201 | SQL-invoked routines on arrays | S201 |  |  |
| S201 | SQL-invoked routines on arrays | S201-01 | Array parameters |  |
| S201 | SQL-invoked routines on arrays | S201-02 | Array as result type of functions |  |
| S202 | SQL-invoked routines on multisets | S202 |  |  |
| S211 | User-defined cast functions | S211 |  |  |
| S231 | Structured type locators | S231 |  |  |
| S232 | Array locators | S232 |  |  |
| S233 | Multiset locators | S233 |  |  |
| S241 | Transform functions | S241 |  |  |
| S242 | Alter transform statement | S242 |  |  |
| S251 | User-defined orderings | S251 |  |  |
| S261 | Specific type method | S261 |  |  |
| S271 | Basic multiset support | S271 |  |  |
| S272 | Multisets of user-defined types | S272 |  |  |
| S274 | Multisets of reference types | S274 |  |  |
| S275 | Advanced multiset support | S275 |  |  |
| S281 | Nested collection types | S281 |  |  |
| S291 | Unique constraint on entire row | S291 |  |  |
| S301 | Enhanced UNNEST | S301 |  |  |
| S401 | Distinct types based on array types | S401 |  |  |
| S402 | Distinct types based on distinct types | S402 |  |  |
| S403 | ARRAY_MAX_CARDINALITY | S403 |  |  |
| S404 | TRIM_ARRAY | S404 |  |  |
| T011 | Timestamp in Information Schema | T011 |  |  |
| T022 | Advanced support for BINARY and VARBINARY data types | T022 |  |  |
| T023 | Compound binary literal | T023 |  |  |
| T024 | Spaces in binary literals | T024 |  |  |
| T041 | Basic LOB data type support | T041 |  |  |
| T041 | Basic LOB data type support | T041-01 | BLOB data type |  |
| T041 | Basic LOB data type support | T041-02 | CLOB data type |  |
| T041 | Basic LOB data type support | T041-03 | POSITION, LENGTH, LOWER, TRIM, UPPER, and SUBSTRING functions for LOB data types |  |
| T041 | Basic LOB data type support | T041-04 | Concatenation of LOB data types |  |
| T041 | Basic LOB data type support | T041-05 | LOB locator: non-holdable |  |
| T042 | Extended LOB data type support | T042 |  |  |
| T043 | Multiplier T | T043 |  |  |
| T044 | Multiplier P | T044 |  |  |
| T051 | Row types | T051 |  |  |
| T053 | Explicit aliases for all-fields reference | T053 |  |  |
| T061 | UCS support | T061 |  |  |
| T076 | DECFLOAT data type | T076 |  |  |
| T101 | Enhanced nullability determination | T101 |  |  |
| T111 | Updatable joins, unions, and columns | T111 |  |  |
| T131 | Recursive query | T131 |  |  |
| T132 | Recursive query in subquery | T132 |  |  |
| T171 | LIKE clause in table definition | T171 |  |  |
| T172 | AS subquery clause in table definition | T172 |  |  |
| T173 | Extended LIKE clause in table definition | T173 |  |  |
| T174 | Identity columns | T174 |  |  |
| T175 | Generated columns | T175 |  |  |
| T176 | Sequence generator support | T176 |  |  |
| T177 | Sequence generator support: simple restart option | T177 |  |  |
| T178 | Identity columns:  simple restart option | T178 |  |  |
| T180 | System-versioned tables | T180 |  |  |
| T181 | Application-time period tables | T181 |  |  |
| T191 | Referential action RESTRICT | T191 |  |  |
| T201 | Comparable data types for referential constraints | T201 |  |  |
| T211 | Basic trigger capability | T211 |  |  |
| T211 | Basic trigger capability | T211-01 | Triggers activated on UPDATE, INSERT, or DELETE of one base table |  |
| T211 | Basic trigger capability | T211-02 | BEFORE triggers |  |
| T211 | Basic trigger capability | T211-03 | AFTER triggers |  |
| T211 | Basic trigger capability | T211-04 | FOR EACH ROW triggers |  |
| T211 | Basic trigger capability | T211-05 | Ability to specify a search condition that must be true before the trigger is invoked |  |
| T211 | Basic trigger capability | T211-06 | Support for run-time rules for the interaction of triggers and constraints |  |
| T211 | Basic trigger capability | T211-07 | TRIGGER privilege |  |
| T211 | Basic trigger capability | T211-08 | Multiple triggers for the same event are executed in the order in which they were created in the catalog |  |
| T212 | Enhanced trigger capability | T212 |  |  |
| T213 | INSTEAD OF triggers | T213 |  |  |
| T231 | Sensitive cursors | T231 |  |  |
| T241 | START TRANSACTION statement | T241 |  |  |
| T251 | SET TRANSACTION statement: LOCAL option | T251 |  |  |
| T261 | Chained transactions | T261 |  |  |
| T271 | Savepoints | T271 |  |  |
| T272 | Enhanced savepoint management | T272 |  |  |
| T281 | SELECT privilege with column granularity | T281 |  |  |
| T301 | Functional dependencies | T301 |  |  |
| T321 | Basic SQL-invoked routines | T321 |  |  |
| T321 | Basic SQL-invoked routines | T321-01 | User-defined functions with no overloading |  |
| T321 | Basic SQL-invoked routines | T321-02 | User-defined stored procedures with no overloading |  |
| T321 | Basic SQL-invoked routines | T321-03 | Function invocation |  |
| T321 | Basic SQL-invoked routines | T321-04 | CALL statement |  |
| T321 | Basic SQL-invoked routines | T321-05 | RETURN statement |  |
| T321 | Basic SQL-invoked routines | T321-06 | ROUTINES view |  |
| T321 | Basic SQL-invoked routines | T321-07 | PARAMETERS view |  |
| T322 | Declared data type attributes | T322 |  |  |
| T323 | Explicit security for external routines | T323 |  |  |
| T324 | Explicit security for SQL routines | T324 |  |  |
| T325 | Qualified SQL parameter references | T325 |  |  |
| T326 | Table functions | T326 |  |  |
| T331 | Basic roles | T331 |  |  |
| T332 | Extended roles | T332 |  |  |
| T341 | Overloading of SQL-invoked functions and procedures | T341 |  |  |
| T432 | Nested and concatenated GROUPING SETS | T432 |  |  |
| T461 | Symmetric BETWEEN predicate | T461 |  |  |
| T471 | Result sets return value | T471 |  |  |
| T472 | DESCRIBE CURSOR | T472 |  |  |
| T491 | LATERAL derived table | T491 |  |  |
| T495 | Combined data change and retrieval | T495 |  |  |
| T502 | Period predicates | T502 |  |  |
| T511 | Transaction counts | T511 |  |  |
| T521 | Named arguments in CALL statement | T521 |  |  |
| T522 | Default values for IN parameters of SQL-invoked procedures | T522 |  |  |
| T523 | Default values for INOUT parameters of SQL-invoked procedures | T523 |  |  |
| T524 | Named arguments in routine invocations other than a CALL statement | T524 |  |  |
| T525 | Default values for parameters of SQL-invoked functions | T525 |  |  |
| T561 | Holdable locators | T561 |  |  |
| T571 | Array-returning external SQL-invoked functions | T571 |  |  |
| T572 | Multiset-returning external SQL-invoked functions | T572 |  |  |
| T581 | Regular expression substring function | T581 |  |  |
| T591 | UNIQUE constraints of possibly null columns | T591 |  |  |
| T601 | Local cursor references | T601 |  |  |
| T611 | Elementary OLAP operations | T611 |  |  |
| T612 | Advanced OLAP operations | T612 |  |  |
| T613 | Sampling | T613 |  |  |
| T614 | NTILE function | T614 |  |  |
| T615 | LEAD and LAG functions | T615 |  |  |
| T616 | Null treatment option for LEAD and LAG functions | T616 |  |  |
| T617 | FIRST_VALUE and LAST_VALUE function | T617 |  |  |
| T618 | NTH_VALUE function | T618 |  |  |
| T619 | Nested window functions | T619 |  |  |
| T620 | WINDOW clause: GROUPS option | T620 |  |  |
| T625 | LISTAGG | T625 |  |  |
| T641 | Multiple column assignment | T641 |  |  |
| T651 | SQL-schema statements in SQL routines | T651 |  |  |
| T652 | SQL-dynamic statements in SQL routines | T652 |  |  |
| T653 | SQL-schema statements in external routines | T653 |  |  |
| T654 | SQL-dynamic statements in external routines | T654 |  |  |
| T655 | Cyclically dependent routines | T655 |  |  |
| T811 | Basic SQL/JSON constructor functions | T811 |  |  |
| T812 | SQL/JSON: JSON_OBJECTAGG | T812 |  |  |
| T813 | SQL/JSON: JSON_ARRAYAGG with ORDER BY | T813 |  |  |
| T814 | Colon in JSON_OBJECT or JSON_OBJECTAGG | T814 |  |  |
| T821 | Basic SQL/JSON query operators | T821 |  |  |
| T822 | SQL/JSON: IS JSON WITH UNIQUE KEYS predicate | T822 |  |  |
| T823 | SQL/JSON: PASSING clause | T823 |  |  |
| T824 | JSON_TABLE: specific PLAN clause | T824 |  |  |
| T825 | SQL/JSON: ON EMPTY and ON ERROR clauses | T825 |  |  |
| T826 | General value expression in ON ERROR or ON EMPTY clauses | T826 |  |  |
| T827 | JSON_TABLE: sibling NESTED COLUMNS clauses | T827 |  |  |
| T830 | Enforcing unique keys in SQL/JSON constructor functions | T830 |  |  |
| T831 | SQL/JSON path language: strict mode | T831 |  |  |
| T832 | SQL/JSON path language: item method | T832 |  |  |
| T833 | SQL/JSON path language: multiple subscripts | T833 |  |  |
| T834 | SQL/JSON path language: wildcard member accessor | T834 |  |  |
| T835 | SQL/JSON path language: filter expressions | T835 |  |  |
| T836 | SQL/JSON path language: starts with predicate | T836 |  |  |
| T837 | SQL/JSON path language: regex_like predicate | T837 |  |  |
| T838 | JSON_TABLE: PLAN DEFAULT clause | T838 |  |  |
| X010 | XML type | X010 |  |  |
| X011 | Arrays of XML type | X011 |  |  |
| X012 | Multisets of XML type | X012 |  |  |
| X013 | Distinct types of XML type | X013 |  |  |
| X014 | Attributes of XML type | X014 |  |  |
| X015 | Fields of XML type | X015 |  |  |
| X016 | Persistent XML values | X016 |  |  |
| X020 | XMLConcat | X020 |  |  |
| X025 | XMLCast | X025 |  |  |
| X030 | XMLDocument | X030 |  |  |
| X031 | XMLElement | X031 |  |  |
| X032 | XMLForest | X032 |  |  |
| X034 | XMLAgg | X034 |  |  |
| X035 | XMLAgg: ORDER BY option | X035 |  |  |
| X036 | XMLComment | X036 |  |  |
| X037 | XMLPI | X037 |  |  |
| X038 | XMLText | X038 |  |  |
| X040 | Basic table mapping | X040 |  |  |
| X041 | Basic table mapping: nulls absent | X041 |  |  |
| X042 | Basic table mapping: null as nil | X042 |  |  |
| X043 | Basic table mapping: table as forest | X043 |  |  |
| X044 | Basic table mapping: table as element | X044 |  |  |
| X045 | Basic table mapping: with target namespace | X045 |  |  |
| X046 | Basic table mapping: data mapping | X046 |  |  |
| X047 | Basic table mapping: metadata mapping | X047 |  |  |
| X048 | Basic table mapping: base64 encoding of binary strings | X048 |  |  |
| X049 | Basic table mapping: hex encoding of binary strings | X049 |  |  |
| X050 | Advanced table mapping | X050 |  |  |
| X051 | Advanced table mapping: nulls absent | X051 |  |  |
| X052 | Advanced table mapping: null as nil | X052 |  |  |
| X053 | Advanced table mapping: table as forest | X053 |  |  |
| X054 | Advanced table mapping: table as element | X054 |  |  |
| X055 | Advanced table mapping: with target namespace | X055 |  |  |
| X056 | Advanced table mapping: data mapping | X056 |  |  |
| X057 | Advanced table mapping: metadata mapping | X057 |  |  |
| X058 | Advanced table mapping: base64 encoding of binary strings | X058 |  |  |
| X059 | Advanced table mapping: hex encoding of binary strings | X059 |  |  |
| X060 | XMLParse: character string input and CONTENT option | X060 |  |  |
| X061 | XMLParse: character string input and DOCUMENT option | X061 |  |  |
| X065 | XMLParse: BLOB input and CONTENT option | X065 |  |  |
| X066 | XMLParse: BLOB input and DOCUMENT option | X066 |  |  |
| X068 | XMLSerialize: BOM | X068 |  |  |
| X069 | XMLSerialize: INDENT | X069 |  |  |
| X070 | XMLSerialize: character string serialization and CONTENT option | X070 |  |  |
| X071 | XMLSerialize: character string serialization and DOCUMENT option | X071 |  |  |
| X072 | XMLSerialize: character string serialization | X072 |  |  |
| X073 | XMLSerialize: BLOB serialization and CONTENT option | X073 |  |  |
| X074 | XMLSerialize: BLOB serialization and DOCUMENT option | X074 |  |  |
| X075 | XMLSerialize: BLOB serialization | X075 |  |  |
| X076 | XMLSerialize: VERSION | X076 |  |  |
| X077 | XMLSerialize: explicit ENCODING option | X077 |  |  |
| X078 | XMLSerialize: explicit XML declaration | X078 |  |  |
| X080 | Namespaces in XML publishing | X080 |  |  |
| X081 | Query-level XML namespace declarations | X081 |  |  |
| X082 | XML namespace declarations in DML | X082 |  |  |
| X083 | XML namespace declarations in DDL | X083 |  |  |
| X084 | XML namespace declarations in compound statements | X084 |  |  |
| X085 | Predefined namespace prefixes | X085 |  |  |
| X086 | XML namespace declarations in XMLTable | X086 |  |  |
| X090 | XML document predicate | X090 |  |  |
| X091 | XML content predicate | X091 |  |  |
| X096 | XMLExists | X096 |  |  |
| X100 | Host language support for XML: CONTENT option | X100 |  |  |
| X101 | Host language support for XML: DOCUMENT option | X101 |  |  |
| X110 | Host language support for XML: VARCHAR mapping | X110 |  |  |
| X111 | Host language support for XML: CLOB mapping | X111 |  |  |
| X112 | Host language support for XML: BLOB mapping | X112 |  |  |
| X113 | Host language support for XML: STRIP WHITESPACE option | X113 |  |  |
| X114 | Host language support for XML: PRESERVE WHITESPACE option | X114 |  |  |
| X120 | XML parameters in SQL routines | X120 |  |  |
| X121 | XML parameters in external routines | X121 |  |  |
| X131 | Query-level XMLBINARY clause | X131 |  |  |
| X132 | XMLBINARY clause in DML | X132 |  |  |
| X133 | XMLBINARY clause in DDL | X133 |  |  |
| X134 | XMLBINARY clause in compound statements | X134 |  |  |
| X135 | XMLBINARY clause in subqueries | X135 |  |  |
| X141 | IS VALID predicate: data-driven case | X141 |  |  |
| X142 | IS VALID predicate: ACCORDING TO clause | X142 |  |  |
| X143 | IS VALID predicate: ELEMENT clause | X143 |  |  |
| X144 | IS VALID predicate: schema location | X144 |  |  |
| X145 | IS VALID predicate outside check constraints | X145 |  |  |
| X151 | IS VALID predicate with DOCUMENT option | X151 |  |  |
| X152 | IS VALID predicate with CONTENT option | X152 |  |  |
| X153 | IS VALID predicate with SEQUENCE option | X153 |  |  |
| X155 | IS VALID predicate: NAMESPACE without ELEMENT clause | X155 |  |  |
| X157 | IS VALID predicate: NO NAMESPACE with ELEMENT clause | X157 |  |  |
| X160 | Basic Information Schema for registered XML Schemas | X160 |  |  |
| X161 | Advanced Information Schema for registered XML Schemas | X161 |  |  |
| X170 | XML null handling options | X170 |  |  |
| X171 | NIL ON NO CONTENT option | X171 |  |  |
| X181 | XML(DOCUMENT(UNTYPED)) type | X181 |  |  |
| X182 | XML(DOCUMENT(ANY)) type | X182 |  |  |
| X190 | XML(SEQUENCE) type | X190 |  |  |
| X191 | XML(DOCUMENT(XMLSCHEMA)) type | X191 |  |  |
| X192 | XML(CONTENT(XMLSCHEMA)) type | X192 |  |  |
| X200 | XMLQuery | X200 |  |  |
| X201 | XMLQuery: RETURNING CONTENT | X201 |  |  |
| X202 | XMLQuery: RETURNING SEQUENCE | X202 |  |  |
| X203 | XMLQuery: passing a context item | X203 |  |  |
| X204 | XMLQuery: initializing an XQuery variable | X204 |  |  |
| X205 | XMLQuery: EMPTY ON EMPTY option | X205 |  |  |
| X206 | XMLQuery: NULL ON EMPTY option | X206 |  |  |
| X211 | XML 1.1 support | X211 |  |  |
| X221 | XML passing mechanism BY VALUE | X221 |  |  |
| X222 | XML passing mechanism BY REF | X222 |  |  |
| X231 | XML(CONTENT(UNTYPED)) type | X231 |  |  |
| X232 | XML(CONTENT(ANY)) type | X232 |  |  |
| X241 | RETURNING CONTENT in XML publishing | X241 |  |  |
| X242 | RETURNING SEQUENCE in XML publishing | X242 |  |  |
| X251 | Persistent XML values of XML(DOCUMENT(UNTYPED)) type | X251 |  |  |
| X252 | Persistent XML values of XML(DOCUMENT(ANY)) type | X252 |  |  |
| X253 | Persistent XML values of XML(CONTENT(UNTYPED)) type | X253 |  |  |
| X254 | Persistent XML values of XML(CONTENT(ANY)) type | X254 |  |  |
| X255 | Persistent XML values of XML(SEQUENCE) type | X255 |  |  |
| X256 | Persistent XML values of XML(DOCUMENT(XMLSCHEMA)) type | X256 |  |  |
| X257 | Persistent XML values of XML(CONTENT(XMLSCHEMA)) type | X257 |  |  |
| X260 | XML type: ELEMENT clause | X260 |  |  |
| X261 | XML type: NAMESPACE without ELEMENT clause | X261 |  |  |
| X263 | XML type: NO NAMESPACE with ELEMENT clause | X263 |  |  |
| X264 | XML type: schema location | X264 |  |  |
| X271 | XMLValidate: data-driven case | X271 |  |  |
| X272 | XMLValidate: ACCORDING TO clause | X272 |  |  |
| X273 | XMLValidate: ELEMENT clause | X273 |  |  |
| X274 | XMLValidate: schema location | X274 |  |  |
| X281 | XMLValidate with DOCUMENT option | X281 |  |  |
| X282 | XMLValidate with CONTENT option | X282 |  |  |
| X283 | XMLValidate with SEQUENCE option | X283 |  |  |
| X284 | XMLValidate: NAMESPACE without ELEMENT clause | X284 |  |  |
| X286 | XMLValidate: NO NAMESPACE with ELEMENT clause | X286 |  |  |
| X300 | XMLTable | X300 |  |  |
| X301 | XMLTable: derived column list option | X301 |  |  |
| X302 | XMLTable: ordinality column option | X302 |  |  |
| X303 | XMLTable: column default option | X303 |  |  |
| X304 | XMLTable: passing a context item | X304 |  |  |
| X305 | XMLTable: initializing an XQuery variable | X305 |  |  |
| X400 | Name and identifier mapping | X400 |  |  |
| X410 | Alter column data type: XML type | X410 |  |  |
