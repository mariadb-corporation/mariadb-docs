# Error 1068: Multiple primary key defined

| Error Code | SQLSTATE | Error                  | Description                  |
| ---------- | -------- | ---------------------- | ---------------------------- |
| 1068       | 42000    | ER\_MULTIPLE\_PRI\_KEY | Multiple primary key defined |

## Possible Causes and Solutions

No more than one [primary key](../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#primary-key) can be defined per table. Attempting to define more in a single table will result in this error. For example:

```
CREATE TABLE t1(
    c1 INT NOT NULL AUTO_INCREMENT, 
    c2 INT NOT NULL, 
    PRIMARY KEY(c1),
    PRIMARY KEY(c2)
);
ERROR 1068 (42000): Multiple primary key defined

CREATE TABLE t1(
    c1 INT NOT NULL AUTO_INCREMENT, 
    c2 INT NOT NULL, 
    PRIMARY KEY(c1)
);
```

It's also possible that this error results from a mistaken attempt to define a multi-part primary key. This is an example of the correct definition for such a key.

```
CREATE TABLE t1(
    c1 INT NOT NULL AUTO_INCREMENT, 
    c2 INT NOT NULL, 
    PRIMARY KEY(c1, c2)
);
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
