# Error 4206: Cannot determine distance type for VEC\_DISTANCE, index is not found

| Error Code | SQLSTATE | Error                   | Description                                                          |
| ---------- | -------- | ----------------------- | -------------------------------------------------------------------- |
| 4206       |          | ER\_VEC\_DISTANCE\_TYPE | Cannot determine distance type for VEC\_DISTANCE, index is not found |

## Possible Causes and Solutions

### Table is Built Without a Vector Index

```
CREATE OR REPLACE TABLE v (id INT PRIMARY KEY, v VECTOR(5) NOT NULL);

INSERT INTO v VALUES                                              
    (1, x'e360d63ebe554f3fcdbc523f4522193f5236083d'),
    (2, x'f511303f72224a3fdd05fe3eb22a133ffae86a3f'),
    (3,x'f09baa3ea172763f123def3e0c7fe53e288bf33e'),
    (4,x'b97a523f2a193e3eb4f62e3f2d23583e9dd60d3f'),
    (5,x'f7c5df3e984b2b3e65e59d3d7376db3eac63773e'),
    (6,x'de01453ffa486d3f10aa4d3fdd66813c71cb163f'),
    (7,x'76edfc3e4b57243f10f8423fb158713f020bda3e'),
    (8,x'56926c3fdf098d3e2c8c5e3d1ad4953daa9d0b3e'),
    (9,x'7b713f3e5258323f80d1113d673b2b3f66e3583f'),
    (10,x'6ca1d43e9df91b3fe580da3e1c247d3f147cf33e');

SELECT id FROM v ORDER BY VEC_DISTANCE(v, x'6ca1d43e9df91b3fe580da3e1c247d3f147cf33e');          
ERROR 4206 (HY000): Cannot determine distance type for VEC_DISTANCE, index is not found
```

To solve, add a vector index to the table:

```
ALTER TABLE v ADD VECTOR INDEX(v);

SELECT id FROM v ORDER BY VEC_DISTANCE(v, x'6ca1d43e9df91b3fe580da3e1c247d3f147cf33e');
+----+
| id |
+----+
| 10 |
|  7 |
|  3 |
|  9 |
|  2 |
|  1 |
|  5 |
|  4 |
|  6 |
|  8 |
+----+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
