---
description: >-
  Plugin API reference: JSON Service. Generated from the MariaDB server headers
  by doxygen and moxygen.
---

# JSON Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Plugin Services`](./)

Exports JSON parsing methods for plugins to use.

Functions of the service: [json\_type](plugin_api_service_json.md#json_type) - returns the type of the JSON argument, and the parsed value if it's scalar (not object or array)

[json\_get\_array\_item](plugin_api_service_json.md#json_get_array_item) - expects JSON array as an argument, and returns the type of the element at index `n_item`. Returns [JSV\_NOTHING](plugin_api_service_json.md#json_types) type if the array is shorter than n\_item and the actual length of the array in value\_len. If successful, then `value` up till `value[value_len]` contains the array element at the desired index (n\_item).

[json\_get\_object\_key](plugin_api_service_json.md#json_get_object_key) - expects JSON object as an argument, searches for a key in the object, return it's type and stores its value in `value`. [JSV\_NOTHING](plugin_api_service_json.md#json_types) if no such key found, the number of keys in v\_len.

[json\_get\_object\_nkey](plugin_api_service_json.md#json_get_object_nkey) - expects JSON object as an argument. finds n\_key's key in the object, returns it's name, type and value. [JSV\_NOTHING](plugin_api_service_json.md#json_types) if object has less keys than n\_key.

## Classes

| Name                                                            | Description |
| --------------------------------------------------------------- | ----------- |
| [`json_service_st`](plugin_api_service_json.md#json_service_st) |             |

## Macros

| Name                                                                      | Description |
| ------------------------------------------------------------------------- | ----------- |
| [`json_type`](plugin_api_service_json.md#json_type)                       |             |
| [`json_get_array_item`](plugin_api_service_json.md#json_get_array_item)   |             |
| [`json_get_object_key`](plugin_api_service_json.md#json_get_object_key)   |             |
| [`json_get_object_nkey`](plugin_api_service_json.md#json_get_object_nkey) |             |
| [`json_escape_string`](plugin_api_service_json.md#json_escape_string)     |             |
| [`json_unescape_json`](plugin_api_service_json.md#json_unescape_json)     |             |

***

### json\_type

```cpp
#define json_type json_service->json_type
```

Defined in service\_json.h:93

***

### json\_get\_array\_item

```cpp
#define json_get_array_item json_service->json_get_array_item
```

Defined in service\_json.h:94

***

### json\_get\_object\_key

```cpp
#define json_get_object_key json_service->json_get_object_key
```

Defined in service\_json.h:95

***

### json\_get\_object\_nkey

```cpp
#define json_get_object_nkey json_service->json_get_object_nkey
```

Defined in service\_json.h:96

***

### json\_escape\_string

```cpp
#define json_escape_string json_service->json_escape_string
```

Defined in service\_json.h:97

***

### json\_unescape\_json

```cpp
#define json_unescape_json json_service->json_unescape_json
```

Defined in service\_json.h:98

## Enumerations

| Name                                                  | Description |
| ----------------------------------------------------- | ----------- |
| [`json_types`](plugin_api_service_json.md#json_types) |             |

***

### json\_types

```cpp
enum json_types
```

Defined in service\_json.h:59

| Value          | Description |
| -------------- | ----------- |
| `JSV_BAD_JSON` |             |
| `JSV_NOTHING`  |             |
| `JSV_OBJECT`   |             |
| `JSV_ARRAY`    |             |
| `JSV_STRING`   |             |
| `JSV_NUMBER`   |             |
| `JSV_TRUE`     |             |
| `JSV_FALSE`    |             |
| `JSV_NULL`     |             |

## Variables

| Return                                                                    | Name                                                      | Description |
| ------------------------------------------------------------------------- | --------------------------------------------------------- | ----------- |
| struct [`json_service_st`](plugin_api_service_json.md#json_service_st) \* | [`json_service`](plugin_api_service_json.md#json_service) |             |

***

### json\_service

```cpp
struct json_service_st * json_service
```

Type: struct [`json_service_st`](plugin_api_service_json.md#json_service_st) \*

Defined in service\_json.h:89

## Class Definitions

### json\_service\_st

```cpp
#include <service_json.h>
```

```cpp
struct json_service_st
```

Defined in service\_json.h:72

#### Public Attributes

| Return                                                        | Name                                                                        | Description |
| ------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------- |
| enum [`json_types`](plugin_api_service_json.md#json_types)(\* | [`json_type`](plugin_api_service_json.md#json_type-1)                       |             |
| enum [`json_types`](plugin_api_service_json.md#json_types)(\* | [`json_get_array_item`](plugin_api_service_json.md#json_get_array_item-1)   |             |
| enum [`json_types`](plugin_api_service_json.md#json_types)(\* | [`json_get_object_key`](plugin_api_service_json.md#json_get_object_key-1)   |             |
| enum [`json_types`](plugin_api_service_json.md#json_types)(\* | [`json_get_object_nkey`](plugin_api_service_json.md#json_get_object_nkey-1) |             |
| `int(*`                                                       | [`json_escape_string`](plugin_api_service_json.md#json_escape_string-1)     |             |
| `int(*`                                                       | [`json_unescape_json`](plugin_api_service_json.md#json_unescape_json-1)     |             |

***

#### json\_type

```cpp
enum json_types(* json_type)(const char *js, const char *js_end, const char **value, int *value_len)
```

Defined in service\_json.h:1

***

#### json\_get\_array\_item

```cpp
enum json_types(* json_get_array_item)(const char *js, const char *js_end, int n_item, const char **value, int *value_len)
```

Defined in service\_json.h:1

***

#### json\_get\_object\_key

```cpp
enum json_types(* json_get_object_key)(const char *js, const char *js_end, const char *key, const char **value, int *value_len)
```

Defined in service\_json.h:1

***

#### json\_get\_object\_nkey

```cpp
enum json_types(* json_get_object_nkey)(const char *js, const char *js_end, int nkey, const char **keyname, const char **keyname_end, const char **value, int *value_len)
```

Defined in service\_json.h:1

***

#### json\_escape\_string

```cpp
int(* json_escape_string)(const char *str, const char *str_end, char *json, char *json_end)
```

Defined in service\_json.h:85

***

#### json\_unescape\_json

```cpp
int(* json_unescape_json)(const char *json_str, const char *json_end, char *res, char *res_end)
```

Defined in service\_json.h:87
