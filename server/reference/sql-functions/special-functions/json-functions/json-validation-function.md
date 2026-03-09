# JSON Validation Function

## IS JSON

Test whether a JSON expression includes valid data.

### Syntax

```
<expr> IS [ NOT ] JSON
       [ { VALUE | ARRAY | OBJECT | SCALAR } ]
       [ { WITH | WITHOUT } UNIQUE [ KEYS ] ]
```

### Description

The `IS JSON` is a variant of IS predicate that checks whether an expression contains valid JSON data, with optional constraints on JSON type (VALUE, ARRAY, OBJECT, SCALAR) and key uniqueness.

### Example

```
SELECT '{"a": 42}' IS JSON OBJECT;
```

**Output**

```
+----------------------------+
| '{"a": 42}' IS JSON OBJECT | 
+----------------------------+
|                           1| 
+----------------------------+
```

## See Also

* [IS JSON (Comparison Operator)](../../../sql-structure/operators/comparison-operators/is-json.md) for details, including syntax and examples.

