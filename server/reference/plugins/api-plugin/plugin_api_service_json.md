---
description: >-
  Plugin API reference: JSON Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# JSON Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Plugin Services`](plugin_api_services.md)

Exports JSON parsing methods for plugins to use.

Functions of the service: [json_type](#json_type) - returns the type of the JSON argument, and the parsed value if it's scalar (not object or array)

[json_get_array_item](#json_get_array_item) - expects JSON array as an argument, and returns the type of the element at index `n_item`. Returns [JSV_NOTHING](#json_types) type if the array is shorter than n_item and the actual length of the array in value_len. If successful, then `value` up till `value[value_len]` contains the array element at the desired index (n_item).

[json_get_object_key](#json_get_object_key) - expects JSON object as an argument, searches for a key in the object, return it's type and stores its value in `value`. [JSV_NOTHING](#json_types) if no such key found, the number of keys in v_len.

[json_get_object_nkey](#json_get_object_nkey) - expects JSON object as an argument. finds n_key's key in the object, returns it's name, type and value. [JSV_NOTHING](#json_types) if object has less keys than n_key.

## Classes

| Name | Description |
|------|-------------|
| [`json_service_st`](#json_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`json_type`](#json_type)  |  |
| [`json_get_array_item`](#json_get_array_item)  |  |
| [`json_get_object_key`](#json_get_object_key)  |  |
| [`json_get_object_nkey`](#json_get_object_nkey)  |  |
| [`json_escape_string`](#json_escape_string)  |  |
| [`json_unescape_json`](#json_unescape_json)  |  |

---

### json_type

```cpp
#define json_type json_service->json_type
```

Defined in service_json.h:93

---

### json_get_array_item

```cpp
#define json_get_array_item json_service->json_get_array_item
```

Defined in service_json.h:94

---

### json_get_object_key

```cpp
#define json_get_object_key json_service->json_get_object_key
```

Defined in service_json.h:95

---

### json_get_object_nkey

```cpp
#define json_get_object_nkey json_service->json_get_object_nkey
```

Defined in service_json.h:96

---

### json_escape_string

```cpp
#define json_escape_string json_service->json_escape_string
```

Defined in service_json.h:97

---

### json_unescape_json

```cpp
#define json_unescape_json json_service->json_unescape_json
```

Defined in service_json.h:98

## Enumerations

| Name | Description |
|------|-------------|
| [`json_types`](#json_types)  |  |

---

### json_types

```cpp
enum json_types
```

Defined in service_json.h:59

| Value | Description |
|-------|-------------|
| `JSV_BAD_JSON` |  |
| `JSV_NOTHING` |  |
| `JSV_OBJECT` |  |
| `JSV_ARRAY` |  |
| `JSV_STRING` |  |
| `JSV_NUMBER` |  |
| `JSV_TRUE` |  |
| `JSV_FALSE` |  |
| `JSV_NULL` |  |
## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`json_service_st`](#json_service_st) * | [`json_service`](#json_service)  |  |

---

### json_service

```cpp
struct json_service_st * json_service
```

Type: struct [`json_service_st`](#json_service_st) *

Defined in service_json.h:89


## Class Definitions



### json_service_st

```cpp
#include <service_json.h>
```

```cpp
struct json_service_st
```

Defined in service_json.h:72

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| enum [`json_types`](#json_types)(* | [`json_type`](#json_type-1)  |  |
| enum [`json_types`](#json_types)(* | [`json_get_array_item`](#json_get_array_item-1)  |  |
| enum [`json_types`](#json_types)(* | [`json_get_object_key`](#json_get_object_key-1)  |  |
| enum [`json_types`](#json_types)(* | [`json_get_object_nkey`](#json_get_object_nkey-1)  |  |
| `int(*` | [`json_escape_string`](#json_escape_string-1)  |  |
| `int(*` | [`json_unescape_json`](#json_unescape_json-1)  |  |

---

#### json_type

```cpp
enum json_types(* json_type)(const char *js, const char *js_end, const char **value, int *value_len)
```

Defined in service_json.h:1

---

#### json_get_array_item

```cpp
enum json_types(* json_get_array_item)(const char *js, const char *js_end, int n_item, const char **value, int *value_len)
```

Defined in service_json.h:1

---

#### json_get_object_key

```cpp
enum json_types(* json_get_object_key)(const char *js, const char *js_end, const char *key, const char **value, int *value_len)
```

Defined in service_json.h:1

---

#### json_get_object_nkey

```cpp
enum json_types(* json_get_object_nkey)(const char *js, const char *js_end, int nkey, const char **keyname, const char **keyname_end, const char **value, int *value_len)
```

Defined in service_json.h:1

---

#### json_escape_string

```cpp
int(* json_escape_string)(const char *str, const char *str_end, char *json, char *json_end)
```

Defined in service_json.h:85

---

#### json_unescape_json

```cpp
int(* json_unescape_json)(const char *json_str, const char *json_end, char *res, char *res_end)
```

Defined in service_json.h:87

