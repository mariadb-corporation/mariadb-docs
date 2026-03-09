# IS JSON

## Syntax

```
<expr> IS [ NOT ] JSON
       [ { VALUE | ARRAY | OBJECT | SCALAR } ]
       [ { WITH | WITHOUT } UNIQUE [ KEYS ] ]
```

## Description

The `IS JSON` predicate checks whether a given string expression evaluates to valid JSON data in accordance with the SQL:2016 standard (based on RFC 8259).&#x20;

The predicate returns:

* `1`  (**TRUE**) if the JSON expression is valid and satisfies any type constraint that is specified (e.g., `OBJECT`, `ARRAY`)
* `0` (**FALSE**) if the expression is not valid JSON or does not match the  specified type constraints
* &#x20;`NULL` (**UNKNOWN**) if the JSON expression itself evaluates to `NULL`

When the value is invalid JSON, the predicate does not show errors. Any valid JSON value is accepted since VALUE is considered when no type constraint is mentioned.

### Type Constraints

To limit the permitted top-level JSON value, use the optional type constraints listed below:

| Type     | Description                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| `VALUE`  | Any valid JSON value (object, array, number, string, `true`, `false`, `null`) |
| `ARRAY`  | Only JSON arrays (e.g., `[1,2,3]`                                             |
| `OBJECT` | Only JSON objects (e.g., {"key": "value"} = {"a": "42"})                      |
| `SCALAR` | A JSON scalar value (strings, numbers, Boolean, or `null`)                    |

### Unique Keys

The object keys must be unique in order to use `WITH UNIQUE KEYS` option. `WITHOUT UNIQUE KEYS`, duplicate keys are accepted.&#x20;

### Notes

* JSON Validation is based on RFC 8259.
* JSON literal names must be all lowercase: `true`, `false`, `null`.
* Other literal names are not permitted.
* `IS JSON` works in in generated columns, CHECK constraints, and DEFAULT expressions.

### Examples

* **Basic JSON Validation**

```
SELECT '"abc"' IS JSON;
```

**Output**

```
+-----------------+
| '"abc"' IS JSON | 
+-----------------+
|                1| 
+-----------------+
```

* **Type-specific Checking**

{% code fullWidth="true" %}
```
SELECT ''{"a": "42"}' IS JSON OBJECT, '42' IS JSON SCALAR, '[1,2,3]' IS JSON ARRAY;
```
{% endcode %}

**Output**

```
+----------------------------+-----------------------+--------------------------+
| '{"a": "42"}' IS JSON OBJECT |  '42' IS JSON SCALAR  | '[1,2,3]' IS JSON ARRAY  |
+----------------------------+-----------------------+--------------------------+
|                           1|                      1|                         1|
+----------------------------+-----------------------+--------------------------+
```

* **NULL Handling**

```
SELECT 'NULL' IS JSON;
```

**Output**

```
+-----------------+
| 'NULL' IS JSON  | 
+-----------------+
|                0| 
+-----------------+
```

* **JSON Literal Names**

```
SELECT 'null' IS JSON, 'NULL' IS JSON;
```

**Output**

```
+-----------------+--------------+
| 'null' IS JSON  | NULL IS JSON |
+-----------------+--------------+
|                1|          NULL|
+-----------------+--------------+
```

* **Negation with `IS NOT JSON`**

```
SELECT 'invalid' IS NOT JSON;
```

**Output**

```
+------------------------+
| 'invalid' IS NOT JSON  | 
+------------------------+
|                       1| 
+------------------------+
```

* **Unique Keys Validation**

```
SELECT '{"a": 42, "a":1}' IS JSON;
```

**Output**

```
+-----------------------------+
| '{"a": 42, "a":1}' IS JSON  | 
+-----------------------------+
|                            1| 
+-----------------------------+
```

**With Unique Keys (reject duplicates)**

```
SELECT '{"a": 42, "a":1}' IS JSON WITH UNIQUE KEYS;
```

**Output**

```
+----------------------------------------------+
| '{"a": 42, "a":1}' IS JSON WITH UNIQUE KEYS  | 
+----------------------------------------------+
|                                             0| 
+----------------------------------------------+
```

## **See Also**

* [IS Operator](is.md)
* [JSON\_VALID()](../../../sql-functions/special-functions/json-functions/json_valid.md)
* [JSON Data Type](../../../data-types/string-data-types/json.md)
* [JSON\_TYPE](../../../sql-functions/special-functions/json-functions/json_type.md)
