# Error 1075: Incorrect table definition; there can be only one auto column and it must be defined as

| Error Code | SQLSTATE | Error                | Description                                                                                   |
| ---------- | -------- | -------------------- | --------------------------------------------------------------------------------------------- |
| 1075       | 42000    | ER\_WRONG\_AUTO\_KEY | Incorrect table definition; there can be only one auto column and it must be defined as a key |

## Possible Causes and Solutions

There can only be one [AUTO\_INCREMENT](../../data-types/auto_increment.md) column per table, and the column must be defined as a [key](../../../mariadb-quickstart-guides/mariadb-indexes-guide.md). Not adhering to either of these restrictions will result in this error. For example:

```
CREATE OR REPLACE TABLE animals (
    id1 MEDIUMINT NOT NULL AUTO_INCREMENT,
    id2 TINYINT NOT NULL AUTO_INCREMENT,
    name CHAR(30) NOT NULL,
    PRIMARY KEY (id1),
    KEY (id2)
);
ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key


CREATE OR REPLACE TABLE animals (
    id1 MEDIUMINT NOT NULL AUTO_INCREMENT,
    name CHAR(30) NOT NULL
);
ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key


CREATE OR REPLACE TABLE animals (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name CHAR(30) NOT NULL,
    PRIMARY KEY (id)
);
Query OK, 0 rows affected (0.017 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
