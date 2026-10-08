---
title: backports-10.5.26-20
---

* The JSON functions JSON\_ARRAY\_INTERSECT, JSON\_OBJECT\_TO ARRAY, and JSON\_FILTER\_KEYS have been backported from later MariaDB Community Server Release Series to enhance the JSON function coverage in this MariaDB Enterprise Server release series. (MENT-1897)
* The new JSON function JSON\_ARRAY\_INTERSECT(, ) is used to find the intersection between two JSON arrays

Example:

```sql
SET @array1= '[1,2,3]';
SET @array2= '[1,2,4]';
SELECT json_array_intersect(@array1, @array2) AS result;
```

```
+--------+
| result |
+--------+
| [1, 2] |
+--------+
```

```sql
SET @json1= '[[1,2,3],[4,5,6],[1,1,1]]';
SET @json2= '[[1,2,3],[4,5,6],[1,3,2]]';
SELECT json_array_intersect(@json1, @json2) AS result;
```

```
+------------------------+
| result                 |
+------------------------+
| [[1, 2, 3], [4, 5, 6]] |
+------------------------+
```

* The new JSON function JSON\_OBJECT\_TO\_ARRAY(\<json\_doc>) is used to convert all JSON objects found in a JSON document to JSON arrays where each item in the outer array represents a single key-value pair from the object. Example:

```sql
SET @json1= '{ "a" : [1,2,3] , "b": {"key1": "val1", "key2": {"key3": "val3"}} }';
SELECT JSON_OBJECT_TO_ARRAY(@json1) AS result;
```

```
+-----------------------------------------------------------------------+
| result                                                                |
+-----------------------------------------------------------------------+
| [["a", [1, 2, 3]], ["b", {"key1": "val1", "key2": {"key3": "val3"}}]] |
+-----------------------------------------------------------------------+
```

Resulting arrays can be compared using JSON\_ARRAY\_INTERSECT():

```sql
SET @json1='{"a":[1,2,3],"b":{"key1":"val1","key2":{"key3":"val3"}}}';
SET @json2='{"a":[1,2,3]}';
SELECT JSON_OBJECT_TO_ARRAY(@json1) INTO @array1;
SELECT JSON_OBJECT_TO_ARRAY(@json2) INTO @array2;
SELECT JSON_ARRAY_INTERSECT(@array1,@array2) AS result;
```

```
+--------------------+
| result             |
+--------------------+
| [["a", [1, 2, 3]]] |
+--------------------+
```

* The new JSON function JSON\_OBJECT\_FILTER\_KEYS(\<json\_doc>,\<array\_keys>) returns key/value pairs from a JSON string for keys defined in \<array\_keys>.\
  Example:

```sql
SET @json1= '{ "a": 1, "b": 2, "c": 3}';
SELECT JSON_OBJECT_FILTER_KEYS (@json1, ' ["b", "c"] ') AS result;
```

```
+------------------+
| result           |
+------------------+
| {"b": 2, "c": 3} |
+------------------+
```

By using JSON\_ARRAY\_INTERSECT() and JSON\_KEY() as arguments for JSON\_OBJECT\_FILTER\_KEYS(), a comparison of two JSON strings is possible where only the same keys are compared, not the key/value pairs.\
Example (only show key/value pairs of json1 where the key exists in json2):

```sql
SET @json1= '{ "a": 1, "b": 2, "c": 3}';
SET @json2= '{"b" : 10, "c": 20, "d": 30}';
SELECT JSON_OBJECT_FILTER_KEYS (@json1, json_array_intersect(json_keys(@json1), json_keys(@json2))) AS result;
```

```
+------------------+
| result           |
+------------------+
| {"b": 2, "c": 3} |
+------------------+
```

* The new JSON function JSON\_KEY\_VALUE(\<json\_doc>,\<json\_path>) extracts key/value pairs from a JSON object. The JSON path parameter is used to only return key/value pairs for matching JSON objects. (MENT-1896)

Example:

```sql
SELECT JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]');
```

```
+-----------------------------------------------------------------------------+
| JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]') |
+-----------------------------------------------------------------------------+
| [{"key": "key1", "value": "val1"}, {"key": "key2", "value": "val2"}]        |
+-----------------------------------------------------------------------------+
```

The function JSON\_KEY\_VALUE() can be used as an argument to JSON\_TABLE(), which allows adding the key to a result set.\
Example:

```sql
SELECT jt.* FROM JSON_TABLE(
JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]'),'$[*]'
COLUMNS (
k VARCHAR(20) PATH '$.KEY',
v VARCHAR(20) PATH '$.value',
id FOR ORDINALITY )) AS jt;
```

```
+------+------+------+
| k    | v    | id   |
+------+------+------+
| key1 | val1 |    1 |
| key2 | val2 |    2 |
+------+------+------+
```
