---
description: >-
  Discover JSON_NORMALIZE in MariaDB. This function recursively sorts keys and
  removes spaces from a JSON document, enabling reliable equality comparisons
  and unique constraints on JSON data.
---

# JSON\_NORMALIZE

{% hint style="info" %}
`JSON_NORMALIZE` is available from MariaDB 10.7.
{% endhint %}

## Syntax

```sql
JSON_NORMALIZE(json)
```

## Description

Recursively sorts keys and removes spaces, allowing comparison of json documents for equality.

## Examples

We may wish our application to use the database to enforce a unique constraint on the JSON contents, and we can do so using the `JSON_NORMALIZE` function in combination with a unique key.

For example, if we have a table with a JSON column:

```sql
CREATE TABLE t1 (
 id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
 val JSON,
 /* other columns here */
 PRIMARY KEY (id)
);
```

Add a unique constraint using JSON\_NORMALIZE like this:

```sql
ALTER TABLE t1
   ADD COLUMN jnorm JSON AS (JSON_NORMALIZE(val)) VIRTUAL,
   ADD UNIQUE KEY (jnorm);
```

We can test this by first inserting a row as normal:

```sql
INSERT INTO t1 (val) VALUES ('{"name":"alice","color":"blue"}');
```

And then seeing what happens with a different string which would produce the same JSON object:

```sql
INSERT INTO t1 (val) VALUES ('{ "color": "blue", "name": "alice" }');
ERROR 1062 (23000): Duplicate entry '{"color":"blue","name":"alice"}' for key 'jnorm'
```

## See Also

* [JSON\_EQUALS](json_equals.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
