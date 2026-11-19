---
description: >-
  How to write cache filter rules in JSON that decide which results the cache
  stores and when it uses them, with qualified names and regexp matching.
---

# MaxScale Cache Rules

The cache filter's rules decide what is cached and when a cached result is used. The rules file is set with the [rules](cache-settings.md#rules) setting.

The caching rules are expressed as a JSON object or as an array of JSON objects.

There are two decisions to be made regarding the caching; in what circumstances should data be stored to the cache and in what circumstances should the data in the cache be used.

Expressed in JSON this looks as follows

```
{
    store: [ ... ],
    use: [ ... ]
}
```

or, in case an array is used, as

```
[
    {
        store: [ ... ],
        use: [ ... ]
    },
    { ... }
]
```

The `store` field specifies in what circumstances data should be stored to the cache and the `use` field specifies in what circumstances the data in the cache should be used. In both cases, the value is a JSON array containing objects.

If an array of rule objects is specified, then, when looking for a rule that matches, the `store` field of each object are evaluated in sequential order until a match is found. Then, the `use` field of that object is used when deciding whether data in the cache should be used.

## When to Store

By default, if no rules file have been provided or if the `store` field is missing from the object, the results of all queries will be stored to the cache, subject to `max_resultset_rows` and `max_resultset_size` cache filter parameters.

By providing a `store` field in the JSON object, the decision whether to store the result of a particular query to the cache can be controlled in a more detailed manner. The decision to cache the results of a query can depend upon

* the database,
* the table,
* the column, or
* the query itself.

Each entry in the `store` array is an object containing three fields,

```
{
    "attribute": <string>,
    "op": <string>
    "value": <string>
}
```

where,

* the attribute can be `database`, `table`, `column` or `query`,
* the op can be `=`, `!=`, `like` or `unlike`, and
* the value a string.

If _op_ is `=` or `!=` then _value_ is used as a string; if it is `like` or `unlike`, then _value_ is interpreted as a _pcre2_ regular expression. Note though that if _attribute_ is `database`, `table` or `column`, then the string is interpreted as a name, where a dot `.` denotes qualification or scoping.

The objects in the `store` array are processed in order. If the result of a comparison is _true_, no further processing will be made and the result of the query in question will be stored to the cache.

If the result of the comparison is _false_, then the next object is processed. The process continues until the array is exhausted. If there is no match, then the result of the query is not stored to the cache.

Note that as the query itself is used as the key, although the following queries

```
SELECT * FROM db1.tbl
```

and

```
USE db1;
SELECT * FROM tbl
```

target the same table and produce the same results, they will be cached separately. The same holds for queries like

```
SELECT * FROM tbl WHERE a = 2 AND b = 3;
```

and

```
SELECT * FROM tbl WHERE b = 3 AND a = 2;
```

as well. Although they conceptually are identical, there will be two cache entries.

Note that if a column has been specified in a rule, then a statement will match _irrespective_ of where that particular column appears. For instance, if a rule specifies that the result of statements referring to the column _a_ should be cached, then the following statement will match

```
SELECT a FROM tbl;
```

and so will

```
SELECT b FROM tbl WHERE a > 5;
```

### Qualified Names

When using `=` or `!=` in the rule object in conjunction with `database`,`table` and `column`, the provided string is interpreted as a name, that is, dot (`.`) denotes qualification or scope.

In practice that means that if _attribute_ is `database` then _value_ may not contain a dot, if _attribute_ is `table` then _value_ may contain one dot, used for separating the database and table names respectively, and if _attribute_ is `column` then _value_ may contain one or two dots, used for separating table and column names, or database, table and column names.

Note that if a qualified name is used as a _value_, then all parts of the name must be available for a match. MaxScale may not always be capable of deducing in what table a particular column is. If that is the case, then a value like `tbl.field` may not necessarily be a match even if the field is `field` and the table actually is `tbl`.

### Implication of the default database

If the rules concerns the `database`, then only if the statement refers to _no_ specific database, will the default database be considered.

### Regexp Matching

The string used for matching the regular expression contains as much information as there is available. For instance, in a situation like

```
USE somedb;
SELECT fld FROM tbl;
```

the string matched against the regular expression will be `somedb.tbl.fld`.

### Examples

Cache all queries targeting a particular database.

```
{
    "store": [
        {
            "attribute": "database",
            "op": "=",
            "value": "db1"
        }
    ]
}
```

Cache all queries _not_ targeting a particular table

```
{
    "store": [
        {
            "attribute": "table",
            "op": "!=",
            "value": "tbl1"
        }
    ]
}
```

That will exclude queries targeting table _tbl1_ irrespective of which database it is in. To exclude a table in a particular database, specify the table name using a qualified name.

```
{
    "store": [
        {
            "attribute": "table",
            "op": "!=",
            "value": "db1.tbl1"
        }
    ]
}
```

Cache all queries containing a WHERE clause

```
{
    "store": [
        {
            "attribute": "query",
            "op": "like",
            "value": ".*WHERE.*"
        }
    ]
}
```

Note that this will actually cause all queries that contain WHERE anywhere, to be cached.

## When to Use

By default, if no rules file have been provided or if the `use` field is missing from the object, all users may be returned data from the cache.

By providing a `use` field in the JSON object, the decision whether to use data from the cache can be controlled in a more detailed manner. The decision to use data from the cache can depend upon

* the user.

Each entry in the `use` array is an object containing three fields,

```
{
    "attribute": <string>,
    "op": <string>
    "value": <string>
}
```

where,

* the attribute can be `user`,
* the op can be `=`, `!=`, `like` or `unlike`, and
* the value a string.

If _op_ is `=` or `!=` then _value_ is interpreted as a MariaDB account string, that is, `%` means indicates wildcard, but if _op_ is `like` or`unlike` it is simply assumed _value_ is a pcre2 regular expression.

For instance, the following are equivalent:

```
{
    "attribute": "user",
    "op": "=",
    "value": "'bob'@'%'"
}

{
    "attribute": "user",
    "op": "like",
    "value": "bob@.*"
}
```

Note that if _op_ is `=` or `!=` then the usual assumptions apply, that is, a value of `bob` is equivalent with `'bob'@'%'`. If _like_ or _unlike_ is used, then no assumptions apply, but the string is used verbatim as a regular expression.

The objects in the `use` array are processed in order. If the result of a comparison is _true_, no further processing will be made and the data in the cache will be used, subject to the value of `ttl`.

If the result of the comparison is _false_, then the next object is processed. The process continues until the array is exhausted. If there is no match, then data in the cache will not be used.

Note that `use` is relevant only if the query is subject to caching, that is, if all queries are cached or if a query matches a particular rule in the `store` array.

### Examples

Use data from the cache for all users except `admin` (actually `'admin'@'%'`), regardless of what host the `admin` user comes from.

```
{
    "use": [
        {
            "attribute": "user",
            "op": "!=",
            "value": "admin"
        }
    ]
}
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
