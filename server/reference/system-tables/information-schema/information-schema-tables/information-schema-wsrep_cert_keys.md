---
description: >-
  The Information Schema WSREP_CERT_KEYS table displays the certification keys
  for transactions currently being processed by the Galera Cluster.
---

# Information Schema WSREP\_CERT\_KEYS

{% hint style="info" %}
This table is used in [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/).
{% endhint %}

{% hint style="info" %}
This table is available as of MariaDB Enterprise Server 11.8.
{% endhint %}

The Wsrep certification keys, the primary keys of changed rows, are collected into a write set for Galera Cluster's certification-based replication. The write set is used to ensure data consistency by detecting conflicting transactions before they commit. The `WSREP_CERT_INFO` plugin exposes wsrep certification keys in two information schema tables: `WSREP_CERT_KEYS` (this table), and `WSREP_CERT_KEYS_HISTORY`.

There are several key types.

## Exclusive

The Exclusive key type is used when a transaction inserts, updates, or deletes a row. Example:

```sql
CREATE TABLE parent (f1 TINYINT PRIMARY KEY, f2 TINYINT)engine=innodb;
START TRANSACTION; 
INSERT INTO parent VALUES (1, 3); 
SELECT * FROM INFORMATION_SCHEMA.WSREP_CERT_KEYS; 
COMMIT; 
+--------+-----------------------------+-----------+
| THD_ID | KEY_STRING                  | KEY_TYPE  |
+--------+-----------------------------+-----------+
|      9 | 74657374 706172656E74 0001  | exclusive |
+--------+-----------------------------+-----------+
1 row in set (0.001 sec)
```

## Reference

The Reference key type is used when a `FOREIGN KEY` constraint is defined with referenced table key tpe set as `REFERENCE`. In the example, `706172656E74` is a hexadecimal value for 'parent'. Example:

```sql
CREATE TABLE parent (f1 TINYINT PRIMARY KEY, f2 TINYINT) engine=innodb;
CREATE TABLE child (f1 TINYINT PRIMARY KEY, f2 TINYINT, FOREIGN KEY (f2) REFERENCES parent(f1)) engine=innodb;
 
START TRANSACTION;
INSERT INTO parent VALUES (1, 2);
SELECT KEY_STRING, KEY_TYPE FROM INFORMATION_SCHEMA.WSREP_CERT_KEYS;
+-----------------------------+-----------+
| KEY_STRING                  | KEY_TYPE  |
+-----------------------------+-----------+
| 74657374 706172656E74 0001  | exclusive |
+-----------------------------+-----------+
1 row in set (0.001 sec)
COMMIT; 
 
START TRANSACTION; 
INSERT INTO child VALUES (10, 1);
MariaDB [test]> SELECT KEY_STRING, KEY_TYPE FROM INFORMATION_SCHEMA.WSREP_CERT_KEYS;
+-----------------------------+-----------+
| KEY_STRING                  | KEY_TYPE  |
+-----------------------------+-----------+
| 74657374 706172656E74 0001  | exclusive |
| 74657374 706172656E74 0001  | reference |
| 74657374 6368696C64 000A    | exclusive |
+-----------------------------+-----------+
3 rows in set (0.000 sec)
COMMIT;
```

## Update

The Update key type is used when a transaction updates a row and `wsrep_protocol_version` is greater than 4. Otherwise, the Exclusive key type is used. Example:

```sql
CREATE TABLE parent (f1 TINYINT PRIMARY KEY, f2 TINYINT)engine=innodb;
update parent set f2=1;
 
SELECT KEY_STRING, KEY_TYPE FROM INFORMATION_SCHEMA.WSREP_CERT_KEYS;
+-----------------------------+----------+
| KEY_STRING                  | KEY_TYPE |
+-----------------------------+----------+
| 74657374 706172656E74 0001  | update   |
+-----------------------------+----------+
1 row in set (0.001 sec)
```

## Shared

This key type is used when a referenced table update happens, and `wsrep_protocol_version` is smaller than 4.
