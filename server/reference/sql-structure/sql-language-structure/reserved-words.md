# Reserved Words

The following is a list of all reserved words in MariaDB.

Reserved words cannot be used as [Identifiers](identifier-names.md), unless they are quoted.

The definitive list of reserved words for each version can be found by examining the `sql/lex.h` and `sql/sql_yacc.yy` files.

## Reserved Words

| Keyword                           |
| --------------------------------- |
| ACCESSIBLE                        |
| ADD                               |
| ALL                               |
| ALTER                             |
| ANALYZE                           |
| AND                               |
| AS                                |
| ASC                               |
| ASENSITIVE                        |
| BEFORE                            |
| BETWEEN                           |
| BIGINT                            |
| BINARY                            |
| BLOB                              |
| BOTH                              |
| BY                                |
| CALL                              |
| CASCADE                           |
| CASE                              |
| CHANGE                            |
| CHAR                              |
| CHARACTER                         |
| CHECK                             |
| COLLATE                           |
| COLUMN                            |
| CONDITION                         |
| CONSTRAINT                        |
| CONTINUE                          |
| CONVERT                           |
| CREATE                            |
| CROSS                             |
| CURRENT\_DATE                     |
| CURRENT\_ROLE                     |
| CURRENT\_TIME                     |
| CURRENT\_TIMESTAMP                |
| CURRENT\_USER                     |
| CURSOR                            |
| DATABASE                          |
| DATABASES                         |
| DAY\_HOUR                         |
| DAY\_MICROSECOND                  |
| DAY\_MINUTE                       |
| DAY\_SECOND                       |
| DEC                               |
| DECIMAL                           |
| DECLARE                           |
| DEFAULT                           |
| DELAYED                           |
| DELETE                            |
| DELETE\_DOMAIN\_ID                |
| DESC                              |
| DESCRIBE                          |
| DETERMINISTIC                     |
| DISTINCT                          |
| DISTINCTROW                       |
| DIV                               |
| DO\_DOMAIN\_IDS                   |
| DOUBLE                            |
| DROP                              |
| DUAL                              |
| EACH                              |
| ELSE                              |
| ELSEIF                            |
| ENCLOSED                          |
| ESCAPED                           |
| EXCEPT                            |
| EXISTS                            |
| EXIT                              |
| EXPLAIN                           |
| FALSE                             |
| FETCH                             |
| FLOAT                             |
| FLOAT4                            |
| FLOAT8                            |
| FOR                               |
| FORCE                             |
| FOREIGN                           |
| FROM                              |
| FULLTEXT                          |
| GENERAL                           |
| GRANT                             |
| GROUP                             |
| HAVING                            |
| HIGH\_PRIORITY                    |
| HOUR\_MICROSECOND                 |
| HOUR\_MINUTE                      |
| HOUR\_SECOND                      |
| IF                                |
| IGNORE                            |
| IGNORE\_DOMAIN\_IDS               |
| IGNORE\_SERVER\_IDS               |
| IN                                |
| INDEX                             |
| INFILE                            |
| INNER                             |
| INOUT                             |
| INSENSITIVE                       |
| INSERT                            |
| INT                               |
| INT1                              |
| INT2                              |
| INT3                              |
| INT4                              |
| INT8                              |
| INTEGER                           |
| INTERSECT                         |
| INTERVAL                          |
| INTO                              |
| IS                                |
| ITERATE                           |
| JOIN                              |
| KEY                               |
| KEYS                              |
| KILL                              |
| LEADING                           |
| LEAVE                             |
| LEFT                              |
| LIKE                              |
| LIMIT                             |
| LINEAR                            |
| LINES                             |
| LOAD                              |
| LOCALTIME                         |
| LOCALTIMESTAMP                    |
| LOCK                              |
| LONG                              |
| LONGBLOB                          |
| LONGTEXT                          |
| LOOP                              |
| LOW\_PRIORITY                     |
| MASTER\_HEARTBEAT\_PERIOD         |
| MASTER\_SSL\_VERIFY\_SERVER\_CERT |
| MATCH                             |
| MAXVALUE                          |
| MEDIUMBLOB                        |
| MEDIUMINT                         |
| MEDIUMTEXT                        |
| MIDDLEINT                         |
| MINUTE\_MICROSECOND               |
| MINUTE\_SECOND                    |
| MOD                               |
| MODIFIES                          |
| NATURAL                           |
| NOT                               |
| NO\_WRITE\_TO\_BINLOG             |
| NULL                              |
| NUMERIC                           |
| OFFSET (> 10.6)                   |
| ON                                |
| OPTIMIZE                          |
| OPTION                            |
| OPTIONALLY                        |
| OR                                |
| ORDER                             |
| OUT                               |
| OUTER                             |
| OUTFILE                           |
| OVER                              |
| PAGE\_CHECKSUM                    |
| PARSE\_VCOL\_EXPR                 |
| PARTITION                         |
| PRECISION                         |
| PRIMARY                           |
| PROCEDURE                         |
| PURGE                             |
| RANGE                             |
| READ                              |
| READS                             |
| READ\_WRITE                       |
| REAL                              |
| RECURSIVE                         |
| REF\_SYSTEM\_ID                   |
| REFERENCES                        |
| REGEXP                            |
| RELEASE                           |
| RENAME                            |
| REPEAT                            |
| REPLACE                           |
| REQUIRE                           |
| RESIGNAL                          |
| RESTRICT                          |
| RETURN                            |
| RETURNING                         |
| REVOKE                            |
| RIGHT                             |
| RLIKE                             |
| ROW\_NUMBER (> 10.7)              |
| ROWS                              |
| SCHEMA                            |
| SCHEMAS                           |
| SECOND\_MICROSECOND               |
| SELECT                            |
| SENSITIVE                         |
| SEPARATOR                         |
| SET                               |
| SHOW                              |
| SIGNAL                            |
| SLOW                              |
| SMALLINT                          |
| SPATIAL                           |
| SPECIFIC                          |
| SQL                               |
| SQLEXCEPTION                      |
| SQLSTATE                          |
| SQLWARNING                        |
| SQL\_BIG\_RESULT                  |
| SQL\_CALC\_FOUND\_ROWS            |
| SQL\_SMALL\_RESULT                |
| SSL                               |
| STARTING                          |
| STATS\_AUTO\_RECALC               |
| STATS\_PERSISTENT                 |
| STATS\_SAMPLE\_PAGES              |
| STRAIGHT\_JOIN                    |
| TABLE                             |
| TERMINATED                        |
| THEN                              |
| TINYBLOB                          |
| TINYINT                           |
| TINYTEXT                          |
| TO                                |
| TRAILING                          |
| TRIGGER                           |
| TRUE                              |
| UNDO                              |
| UNION                             |
| UNIQUE                            |
| UNLOCK                            |
| UNSIGNED                          |
| UPDATE                            |
| USAGE                             |
| USE                               |
| USING                             |
| UTC\_DATE                         |
| UTC\_TIME                         |
| UTC\_TIMESTAMP                    |
| VALUES                            |
| VARBINARY                         |
| VARCHAR                           |
| VARCHARACTER                      |
| VARYING                           |
| VECTOR (> 11.6)                   |
| WHEN                              |
| WHERE                             |
| WHILE                             |
| WINDOW                            |
| WITH                              |
| WRITE                             |
| XOR                               |
| YEAR\_MONTH                       |
| ZEROFILL                          |

## Exceptions

Some keywords are exceptions for historical reasons, and are permitted as unquoted identifiers. These include:

| Keyword                                                             |
| ------------------------------------------------------------------- |
| ACTION                                                              |
| [BIT](../../data-types/numeric-data-types/bit.md)                   |
| [DATE](../../data-types/date-and-time-data-types/date.md)           |
| [ENUM](../../data-types/string-data-types/enum.md)                  |
| NO                                                                  |
| [TEXT](../../data-types/string-data-types/text.md)                  |
| [TIME](../../data-types/date-and-time-data-types/time.md)           |
| [TIMESTAMP](../../data-types/date-and-time-data-types/timestamp.md) |

## Oracle Mode

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), there are a number of extra reserved words:

| Keyword          |
| ---------------- |
| BODY             |
| ELSIF            |
| GOTO             |
| HISTORY          |
| MINUS (> 10.6.0) |
| OTHERS           |
| PACKAGE          |
| PERIOD           |
| RAISE            |
| ROWNUM           |
| ROWTYPE          |
| SYSDATE          |
| SYSTEM           |
| SYSTEM\_TIME     |
| VERSIONING       |
| WITHOUT          |

## Function Names

If the `IGNORE_SPACE` [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) flag is set, function names become reserved words.

## See Also

* [Information Schema KEYWORDS Table](../../system-tables/information-schema/information-schema-tables/information-schema-keywords-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
