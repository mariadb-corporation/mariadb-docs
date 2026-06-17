---
name: mariadb-json-functions
description: "MariaDB JSON functions — complete catalog of JSON_*, JSON_ARRAY/OBJECT constructors and aggregates (JSON_ARRAYAGG, JSON_OBJECTAGG), extraction (JSON_EXTRACT, JSON_VALUE, JSON_QUERY, JSON_TABLE, ->, ->>), modification (JSON_SET, JSON_INSERT, JSON_REPLACE, JSON_REMOVE, JSON_ARRAY_APPEND, JSON_ARRAY_INSERT), merge variants (JSON_MERGE, JSON_MERGE_PATCH, JSON_MERGE_PRESERVE), validation (JSON_VALID, JSON_SCHEMA_VALID, IS JSON), introspection (JSON_TYPE, JSON_DEPTH, JSON_LENGTH, JSON_KEYS, JSON_CONTAINS, JSON_EQUALS), formatting (JSON_DETAILED/PRETTY, JSON_COMPACT, JSON_LOOSE, JSON_QUOTE, JSON_UNQUOTE), and JSON_TABLE for relational projection. Use when writing SQL that constructs, queries, or modifies JSON data in MariaDB."
---

# MariaDB JSON Functions

*Last updated: 2026-06-02*

Catalog of every built-in JSON function in MariaDB, with signature and a one-line semantic summary per entry. For a function not listed here, fall back to the canonical reference at `server/reference/sql-functions/special-functions/json-functions/`. For JSONPath syntax (used by `JSON_EXTRACT`, `JSON_QUERY`, `JSON_VALUE`, `JSON_TABLE`, etc.), see the JSONPath reference page in the same directory.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Functions with a `*(since X.Y)*` annotation are only available from that version onward; everything else is in every current LTS branch (10.6, 10.11, 11.4, 11.8).

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `CREATE TABLE t (j JSON)` and expects a binary JSON column type | MariaDB's `JSON` is an **alias for `LONGTEXT`** with an automatic `CHECK (JSON_VALID(j))` constraint — there's no binary JSON storage type. Operations parse the text at query time |
| `JSON_VALUE` and `JSON_QUERY` are interchangeable | They aren't. `JSON_VALUE` returns a **scalar** (or `NULL`); `JSON_QUERY` returns a **JSON object or array** (or `NULL`). Using the wrong one is a frequent bug. There's a dedicated "Differences between JSON_QUERY and JSON_VALUE" doc page if you need details |
| Using `JSON_EXTRACT` to read a scalar and getting `"value"` with the quotes | `JSON_EXTRACT` returns the JSON representation, including string quotes. Wrap in `JSON_UNQUOTE`, use the `->>` operator (which does both), or use `JSON_VALUE` |
| Treating `JSON_EXTRACT('[1,2,3]', '$[*]')` as returning a single value | When a path matches multiple values, the result is **autowrapped as a JSON array** — `[1, 2, 3]` here. Use specific paths (`$[0]`) for single-value extraction |
| Calling `JSON_TABLE(...)` in the `SELECT` list | `JSON_TABLE` is a **table function** — goes in the `FROM` clause (or as a derived table). It projects a JSON document into a relational form. Available since 10.6 |
| `SELECT j -> '$.x' FROM t` returning unquoted scalars | `->` is a shorthand for `JSON_EXTRACT` (still quoted). `->>` is `JSON_EXTRACT` + `JSON_UNQUOTE`. Use `->>` when you want raw scalar values |
| `JSON_OBJECT('a', 1, 'b', 2)` getting reordered output | Key order is preserved as written in MariaDB. Don't rely on the same behavior across other databases |
| Adding `CHECK (JSON_VALID(c))` on a `JSON`-typed column | The auto-constraint on the `JSON` alias type already does this — adding it again is redundant but harmless |
| `JSON_SCHEMA_VALID` returning a useful error when validation fails | It only returns `0` or `1`. There is no "what failed" diagnostic — use a dedicated JSON-schema tool if you need that. Available since 11.1 |
| Reaching for `JSON_PRETTY` | Works — it's an alias for `JSON_DETAILED` in MariaDB. Either spelling is fine; `JSON_DETAILED` is the canonical name |

## Functions

The list below is **auto-generated** from `server/reference/sql-functions/special-functions/json-functions/` by `_extractors/extract_function_category.py`. Regenerate when the doc tree changes.


### JSON_ARRAY
`JSON_ARRAY([value[, value2] ...])`  
Returns a JSON array containing the listed values.

### JSON_ARRAYAGG
`JSON_ARRAYAGG(column_or_expression)`  
`JSON_ARRAYAGG` returns a JSON array containing an element for each value in a given set of JSON or SQL values. *(since 10.5)*

### JSON_ARRAY_APPEND
`JSON_ARRAY_APPEND(json_doc, path, value[, path, value] ...)`  
Appends values to the end of the specified arrays within a JSON document, returning the result, or `NULL` if any of the arguments are `NULL`.

### JSON_ARRAY_INSERT
`JSON_ARRAY_INSERT(json_doc, path, value[, path, value] ...)`  
Inserts a value into a JSON document, returning the modified document, or `NULL` if any of the arguments are `NULL`.

### JSON_ARRAY_INTERSECT
`JSON_ARRAY_INTERSECT(arr1, arr2)`  
Finds intersection between two json arrays and returns an array of items found in both array. *(since 11.2)*

### JSON_COMPACT
`JSON_COMPACT(json_doc)`  
Removes all unnecessary spaces so the json document is as short as possible.

### JSON_CONTAINS
`JSON_CONTAINS(json_doc, val[, path])`  
Returns whether or not the specified value is found in the given JSON document or, optionally, at the specified path within the document.

### JSON_CONTAINS_PATH
`JSON_CONTAINS_PATH(json_doc, return_arg, path[, path] ...)`  
Indicates whether the given JSON document contains data at the specified path or paths.

### JSON_DEPTH
`JSON_DEPTH(json_doc)`  
Returns the maximum depth of the given JSON document, or `NULL` if the argument is null.

### JSON_DETAILED
`JSON_DETAILED(json_doc[, tab_size])`  
Represents JSON in the most understandable way emphasizing nested structures.

### JSON_EQUALS
`JSON_EQUALS(json1, json2)`  
Checks if there is equality between two json objects. *(since 10.7)*

### JSON_EXISTS
`JSON_EXISTS(json_doc, json_path)`  
Determines whether `json_doc` has an element pointed to by path `json_path`.

### JSON_EXTRACT
`JSON_EXTRACT(json_doc, path[, path] ...)`  
Extracts data from a JSON document.

### JSON_INSERT
`JSON_INSERT(json_doc, path, val[, path, val] ...)`  
Inserts data into a JSON document, returning the resulting document or `NULL` if either of the _json_doc_ or _path_ arguments are null.

### JSON_KEYS
`JSON_KEYS(json_doc[, path])`  
Returns the keys as a JSON array from the top-level value of a JSON object or, if the optional path argument is provided, the top-level keys from the path.

### JSON_KEY_VALUE
`JSON_KEY_VALUE(obj, json_path)`  
`JSON_KEY_VALUE` extracts key/value pairs from a JSON object. *(since 11.2)*

### JSON_LENGTH
`JSON_LENGTH(json_doc[, path])`  
Returns the length of a JSON document, or, if the optional path argument is given, the length of the value within the document specified by the path.

### JSON_LOOSE
`JSON_LOOSE(json_doc)`  
Adds spaces to a JSON document to make it look more readable.

### JSON_MERGE
`JSON_MERGE(json_doc, json_doc[, json_doc] ...)`  
Merges the given JSON documents.

### JSON_MERGE_PATCH
`JSON_MERGE_PATCH(json_doc, json_doc[, json_doc] ...)`  
Merges the given JSON documents, returning the merged result, or `NULL` if any argument is `NULL`.

### JSON_MERGE_PRESERVE
`JSON_MERGE_PRESERVE(json_doc, json_doc[, json_doc] ...)`  
Merges the given JSON documents, returning the merged result, or `NULL` if any argument is `NULL`.

### JSON_NORMALIZE
`JSON_NORMALIZE(json)`  
Recursively sorts keys and removes spaces, allowing comparison of json documents for equality. *(since 10.7)*

### JSON_OBJECT
`JSON_OBJECT([key, value[, key, value] ...])`  
Returns a JSON object containing the given key/value pairs.

### JSON_OBJECTAGG
`JSON_OBJECTAGG(key, value)`  
`JSON_OBJECTAGG` returns a JSON object containing key-value pairs. *(since 10.5)*

### JSON_OBJECT_FILTER_KEYS
`JSON_OBJECT_FILTER_KEYS(obj, array_keys)`  
`JSON_OBJECT_FILTER_KEYS` returns a JSON object with keys from the object that are also present in the array as string. *(since 11.2)*

### JSON_OBJECT_TO_ARRAY
`JSON_OBJECT_TO_ARRAY(Obj)`  
It is used to convert all JSON objects found in a JSON document to JSON arrays where each item in the outer array represents a single key-value pair from the object. *(since 11.2)*

### JSON_OVERLAPS
`JSON_OVERLAPS(json_doc1, json_doc2)`  
`JSON_OVERLAPS()` compares two json documents and returns true if they have at least one common\ key-value pair between two objects, array element common between two arrays, or array element common with scalar if one of the arguments is a scalar and other is an array. *(since 10.9)*

### JSON_PRETTY
Alias for `JSON_DETAILED`. *(since 10.10.3)*

### JSON_QUERY
`JSON_QUERY(json_doc, path)`  
Given a JSON document, returns an object or array specified by the path.

### JSON_QUOTE
`JSON_QUOTE(json_value)`  
Quotes a string as a JSON value, usually for producing valid JSON string literals for inclusion in JSON documents.

### JSON_REMOVE
`JSON_REMOVE(json_doc, path[, path] ...)`  
Removes data from a JSON document returning the result, or `NULL` if any of the arguments are null.

### JSON_REPLACE
`JSON_REPLACE(json_doc, path, val[, path, val] ...)`  
Replaces existing values in a JSON document, returning the result, or `NULL` if any of the arguments are `NULL`.

### JSON_SCHEMA_VALID
`JSON_SCHEMA_VALID(schema, json);`  
`JSON_SCHEMA_VALID` allows MariaDB to support JSON schema validation. *(since 11.1)*

### JSON_SEARCH
`JSON_SEARCH(json_doc, return_arg, search_str[, escape_char[, path] ...])`  
Returns the path to the given string within a JSON document, or `NULL` if any of _json_doc_, _search_str_ or a path argument is `NULL`; if the search string is not found, or if no path exists within the document.

### JSON_SET
`JSON_SET(json_doc, path, val[, path, val] ...)`  
Updates or inserts data into a JSON document, returning the result, or `NULL` if any of the arguments are `NULL` or the optional path fails to find an object.

### JSON_TABLE
`JSON_TABLE(json_doc,`  
`JSON_TABLE` can be used in contexts where a table reference can be used; in the `FROM` clause of a SELECT statement, and in multi-table UPDATE/DELETE statements. *(since 10.6)*

### JSON_TYPE
`JSON_TYPE(json_val)`  
Returns the type of a JSON value (as a string), or `NULL` if the argument is null.

### JSON_UNQUOTE
`JSON_UNQUOTE(val)`  
Unquotes a JSON value, returning a string, or `NULL` if the argument is null.

### JSON_VALID
`JSON_VALID(value)`  
Indicates whether the given value is a valid JSON document or not.

### JSON_VALUE
`JSON_VALUE(json_doc, path)`  
Given a JSON document, returns the scalar specified by the path.


## Related Operators (Not Covered Above)

- **`->`** — Shorthand for `JSON_EXTRACT(json_doc, path)`
- **`->>`** — Shorthand for `JSON_UNQUOTE(JSON_EXTRACT(json_doc, path))`
- **`IS [NOT] JSON`** — Test whether a value parses as valid JSON. See the operator reference for the full form

## See Also

- **`mariadb-create-table`** — declaring `JSON`-typed columns (alias for `LONGTEXT` with auto `CHECK`)
- **`mariadb-select`** — `JSON_TABLE` in the `FROM` clause for relational projection of JSON documents
- Canonical reference: `server/reference/sql-functions/special-functions/json-functions/` (41 pages); JSONPath syntax at `…/jsonpath-expressions.md`
