# VECTOR

{% hint style="info" %}
`VECTOR` is available from MariaDB 11.7.1.
{% endhint %}

## Syntax

```bnf
VECTOR(N)
```

## Description

The `VECTOR` data type was added as part of the [vectors](../../sql-structure/vectors/) feature, which permits MariaDB Server to perform as a relational vector database. `N` represents the fixed number of dimensions of the vector up to a maximum of 16383. The `N` dimension will be determined by the embedding algorithm.

## Example

```sql
CREATE TABLE t1 (id INT AUTO_INCREMENT PRIMARY KEY, v VECTOR(5) NOT NULL,
 VECTOR INDEX (v));
```

## See Also

* [CREATE TABLE with Vectors](../../sql-structure/vectors/create-table-with-vectors.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
