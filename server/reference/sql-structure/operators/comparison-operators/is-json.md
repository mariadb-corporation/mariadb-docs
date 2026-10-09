---
description: >-
  Test whether a value is valid JSON, optionally of a given type (value,
  array, object, or scalar) and with unique keys. Available from MariaDB
  12.3.
---

# IS JSON

{% hint style="info" %}
This predicate is available from MariaDB 12.3.
{% endhint %}

## Syntax

```bnf
<expr> IS [ NOT ] JSON
       [ { VALUE | ARRAY | OBJECT | SCALAR } ]
       [ { WITH | WITHOUT } UNIQUE [ KEYS ] ]
```

## Description

The `IS JSON` predicate checks whether a given string expression evaluates to valid JSON data in accordance with the SQL:2016 standard (based on RFC 8259).

The predicate returns:

* `1` (**TRUE**) if the JSON expression is valid and satisfies any type constraint that is specified (for example, `OBJECT` or `ARRAY`)
* `0` (**FALSE**) if the expression is not valid JSON or does not match the specified type constraint
* `NULL` (**UNKNOWN**) if the JSON expression itself evaluates to `NULL`

When the value is invalid JSON, the predicate does not show errors. When no type constraint is given, `VALUE` is used, so any valid JSON value is accepted.

### Type Constraints

To limit the permitted top-level JSON value, use one of these optional type constraints:

| Type     | Description                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| `VALUE`  | Any valid JSON value (object, array, number, string, `true`, `false`, `null`) |
| `ARRAY`  | Only JSON arrays (for example, `[1,2,3]`)                                     |
| `OBJECT` | Only JSON objects (for example, `{"a": "42"}`)                                |
| `SCALAR` | A JSON scalar value (strings, numbers, Boolean, or `null`)                    |

### Unique Keys

With `WITH UNIQUE KEYS`, a value is valid only if no object in it has a duplicate key, at any level of nesting. Separate objects can still use the same key names. With `WITHOUT UNIQUE KEYS`, which is the default, duplicate keys are accepted.

### Notes

* JSON validation is based on RFC 8259.
* JSON literal names must be all lowercase: `true`, `false`, `null`.
* Other literal names are not permitted.
* `IS JSON` works in generated columns, CHECK constraints, and DEFAULT expressions.

## Examples

### Basic JSON Validation

```sql
SELECT '"abc"' IS JSON;
+-----------------+
| '"abc"' IS JSON |
+-----------------+
|               1 |
+-----------------+
```

### Type-Specific Checking

```sql
SELECT '{"a": "42"}' IS JSON OBJECT, '42' IS JSON SCALAR, '[1,2,3]' IS JSON ARRAY;
+------------------------------+---------------------+-------------------------+
| '{"a": "42"}' IS JSON OBJECT | '42' IS JSON SCALAR | '[1,2,3]' IS JSON ARRAY |
+------------------------------+---------------------+-------------------------+
|                            1 |                   1 |                       1 |
+------------------------------+---------------------+-------------------------+
```

A value of a different type returns `0`:

```sql
SELECT '[1,2,3]' IS JSON OBJECT;
+--------------------------+
| '[1,2,3]' IS JSON OBJECT |
+--------------------------+
|                        0 |
+--------------------------+
```

### NULL Handling

```sql
SELECT NULL IS JSON;
+--------------+
| NULL IS JSON |
+--------------+
|         NULL |
+--------------+
```

### JSON Literal Names

The lowercase literal `null` is valid JSON. The uppercase string `'NULL'` is not:

```sql
SELECT 'null' IS JSON, 'NULL' IS JSON;
+----------------+----------------+
| 'null' IS JSON | 'NULL' IS JSON |
+----------------+----------------+
|              1 |              0 |
+----------------+----------------+
```

### Negation with IS NOT JSON

```sql
SELECT 'invalid' IS NOT JSON;
+-----------------------+
| 'invalid' IS NOT JSON |
+-----------------------+
|                     1 |
+-----------------------+
```

### Unique Keys Validation

Duplicate keys are accepted by default:

```sql
SELECT '{"a": 42, "a": 1}' IS JSON;
+-----------------------------+
| '{"a": 42, "a": 1}' IS JSON |
+-----------------------------+
|                           1 |
+-----------------------------+
```

`WITH UNIQUE KEYS` rejects them:

```sql
SELECT '{"a": 42, "a": 1}' IS JSON WITH UNIQUE KEYS;
+----------------------------------------------+
| '{"a": 42, "a": 1}' IS JSON WITH UNIQUE KEYS |
+----------------------------------------------+
|                                            0 |
+----------------------------------------------+
```

## See Also

* [IS Operator](is.md)
* [JSON\_VALID()](../../../sql-functions/special-functions/json-functions/json_valid.md)
* [JSON Data Type](../../../data-types/string-data-types/json.md)
* [JSON\_TYPE](../../../sql-functions/special-functions/json-functions/json_type.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
