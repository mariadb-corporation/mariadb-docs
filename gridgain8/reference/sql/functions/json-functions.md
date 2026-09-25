---
description: >-
  Reference of the SQL JSON functions supported by GridGain — IS_JSON,
  JSON_ARRAY, JSON_MODIFY, JSON_OBJECT, JSON_QUERY, and JSON_VALUE.
---

# JSON Functions

{% hint style="warning" %}
JSON functions are only available in GridGain Enterprise and Ultimate Editions.
{% endhint %}

{% hint style="info" %}
You must [enable the 'gridgain-sql' module](../../../gridgain8-usage/setup.md#enabling-modules).
{% endhint %}

## IS_JSON

### Description

Checks if the string contains valid JSON content.

```sql
IS_JSON ( string [, json_type_constraint] )
```

### Parameters

- `string` - the string to check
- `json_type_constraint` - the JSON content type to check for; possible values:
  - `VALUE`
  - `ARRAY`
  - `OBJECT`
  - `SCALAR`

### Example

Check 'years' for JSON objects:

```sql
SELECT IS_JSON('{"years":[1999, 2011, 2022]}');
```

## JSON_ARRAY

### Description

Creates a JSON array from the specified expressions.

```sql
JSON_ARRAY ( [ <json_array_value> [,...n] ])
```

### Parameters

`json_array_value` - the value of an element in the JSON array

### Example

Create a JSON array out of the elements: 'example', 1, and 4.2:

```sql
SELECT JSON_ARRAY('example', 1, 4.2)
```

## JSON_MODIFY

### Description

Updates the value of a property and returns the updated JSON string.

```sql
JSON_MODIFY ( expression , json_path , newValue )
```

### Parameters

- `expression` - the name of a variable or a column that contains JSON text
- `path` - JSON path that specifies an object or an array to extract
- `newValue` - the new value to assign to the specified property

### Example

Change Bristol to London in the 'info' JSON string.

```sql
//Initial JSON
//{"info":{"type":1,"address":{"town":"Bristol","country":"England"},"tags":["Sport","Water polo"]}}

SELECT JSON_MODIFY(J, '$.info.address.town', 'London') FROM TEST;

//Updated JSON
//{"info":{"type":1,"address":{"town":"London","country":"England"},"tags":["Sport","Water polo"]}}
```

## JSON_OBJECT

### Description

Creates a JSON object based on the specified expression.

```sql
JSON_OBJECT ( [ <json_key_value> [,...n] ])
```

### Parameters

`json_key_value` - an expression that defines the value of the JSON key: `(key1, value1, key2, value2...)`

### Example

Create a JSON object:

```sql
select JSON_OBJECT(SELECT * FROM (select * from VALUES (1), (2), (3), (4), (5), (6), (7)) as t limit 4)
```

## JSON_QUERY

### Description

Extracts an object or an array from a JSON string.

{% hint style="info" %}
To extract a scalar value from a JSON string (instead of an object or array), use the [JSON_VALUE](#json_value) function.
{% endhint %}

```sql
JSON_QUERY ( expression , path )
```

### Parameters

- `expression` - the name of a variable or a column that contains JSON text
- `path` - JSON path that specifies the object or array to extract

### Example

Extract the 'info' object:

```sql
select JSON_QUERY('{"info":{"address":[{"town":"Paris"},{"town":"London"}]}}','$.info.address')
```

## JSON_VALUE

### Description

Extracts a scalar value from a JSON string.

{% hint style="info" %}
To extract an object or array (instead of the scalar value), see [JSON_QUERY](#json_query).
{% endhint %}

```sql
JSON_VALUE( expression , path )
```

### Parameters

- `expression` - the name of a variable or a column that contains JSON text
- `path` - JSON path that specifies the value to extract

### Example

Extract the 'town' value from the 'info' JSON string.

```sql
select JSON_VALUE('{"info":{"address":[{"town":"Paris"},{"town":"London"}]}}','$.info.address[0].town')
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
