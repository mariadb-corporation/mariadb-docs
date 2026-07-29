# EQUALS

## Syntax

```bnf
Equals(g1,g2)
```

From [MariaDB 10.2.3](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.3):

```sql
MBREQUALS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether _`g1`_ is spatially equal to _`g2`_.

EQUALS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_EQUALS()](equals.md) uses object shapes.

From [MariaDB 10.2.3](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.3), `MBREQUALS` is a synonym for `Equals`.

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
