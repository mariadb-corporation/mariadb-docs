---
description: >-
  This packet type in the binary protocol transfers result set row data in a
  compact binary format, determined by the column types returned in metadata.
---

# PACKET\_BINDATA

In contrast to the text protocol, the binary protocol transfers data according to the format of the field types returned in `PACKET_METADATA`.

| Field type                                                     | Representation                                                                     |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| MYSQL\_TYPE\_BIT                                               | str\_LEC                                                                           |
| MYSQL\_TYPE\_BLOB                                              | str\_LEC                                                                           |
| MYSQL\_TYPE\_DATE MYSQL\_TYPE\_DATETIME MYSQL\_TYPE\_TIMESTAMP | int\_11 (default)int\_7 (no microseconds)int\_4 (no time values)int\_0 (no values) |
| MYSQL\_TYPE\_DECIMAL                                           | str\_LEC                                                                           |
| MYSQL\_TYPE\_DOUBLE                                            | int\_8                                                                             |
| MYSQL\_TYPE\_ENUM                                              | str\_LEC                                                                           |
| MYSQL\_TYPE\_FLOAT                                             | int\_4                                                                             |
| MYSQL\_TYPE\_GEOMETRY                                          | str\_LEC                                                                           |
| MYSQL\_TYPE\_INT24                                             | int\_4                                                                             |
| MYSQL\_TYPE\_JSON                                              | str\_LEC                                                                           |
| MYSQL\_TYPE\_LONGLONG                                          | int\_8                                                                             |
| MYSQL\_TYPE\_LONG\_BLOB                                        | str\_LEC                                                                           |
| MYSQL\_TYPE\_LONG                                              | int\_4                                                                             |
| MYSQL\_TYPE\_MEDIUM\_BLOB                                      | str\_LEC                                                                           |
| MYSQL\_TYPE\_NEWDECIMAL                                        | str\_LEC                                                                           |
| MYSQL\_TYPE\_NULL                                              | stored in bitmap                                                                   |
| MYSQL\_TYPE\_SET                                               | str\_LEC                                                                           |
| MYSQL\_TYPE\_STRING                                            | str\_LEC                                                                           |
| MYSQL\_TYPE\_SHORT                                             | int\_2                                                                             |
| MYSQL\_TYPE\_TINY\_BLOB                                        | str\_LEC                                                                           |
| MYSQL\_TYPE\_TINY                                              | int\_1                                                                             |
| MYSQL\_TYPE\_VARCHAR                                           | str\_LEC                                                                           |
| MYSQL\_TYPE\_VAR\_STRING                                       | str\_LEC                                                                           |
| MYSQL\_TYPE\_YEAR                                              | int\_4                                                                             |

## Fields

```c
(column_count + 7)/8   null bitmap
while (!eof) {
  for (i=0; i < column_count; i++)
  {
    data (length depends on the data type)
  }
}
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
