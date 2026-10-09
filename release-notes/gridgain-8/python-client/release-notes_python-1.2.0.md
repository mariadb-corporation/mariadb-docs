---
description: >-
  PyGridGain 1.2.0 adds SSL/TLS certificates with passwords, improves the SQL
  API, introduces the AuthenticationError class, and deprecates the SqlQuery API.
hidden: true
---

# PyGridGain 1.2.0 Release Notes

## New Features

PyGridGain 1.2.0 provides access to new features and improvements.

### SSL/TLS Certificates with Passwords

Starting this version, SSL/TLS certificates with passwords are supported. Use `ssl_keyfile_password` argument of client class to specify it upon creation: Client(ssl_keyfile_password=password)

```python
client = Client(use_ssl=True, ssl_keyfile=keyfile, ssl_keyfile_password='my_password')
client.connect('127.0.0.1', 10800)
```

## Changes in Behavior

### Changes in SQL API

Added `cache` argument to Client.sql that can be used to infer schema for SQL query. If this argument is used, `schema` argument is ignored.
Also, default SQL page size increased from 1 to 1024 which provides significant performance improvement when fetching SQL results.

### New Error Type for Authentication Failure

Python thin client now returns a more clear error message on authentication failure. There is also a new error class - AuthenticationError, which makes it simpler to handle authentication errors.

### SqlQuery API

Starting this version, the simplified version of SQL API - SqlQuery API is deprecated. It is recommended to use SqlFieldsQuery instead.

{% tabs %}
{% tab title="Deprecated" %}
```python
cache = client.get_cache('SomeCache')
result = cache.select_row('field > 42')
for k, v in result:
	print(f'{k}: {v}')
```
{% endtab %}

{% tab title="Use instead" %}
```shell
result = client.sql('select key, value from TableName where field > 42', cache='SomeCache')
for k, v in result:
	print(f'{k}: {v}')
```
{% endtab %}
{% endtabs %}

## Improvements and Fixed Issues

| Issue ID | Description |
|---|---|
| GG-32662 | SSL/TLS certificates with passwords are now supported. Use `ssl_keyfile_password` argument of client class to specify it upon creation: Client(ssl_keyfile_password=password). |
| GG-32661 | Fixed bug causing SQL API to return fields in the wrong order. |
| GG-32601 | The SqlQuery API is now deprecated. Use SqlFieldsQuery instead. |
| GG-32600 | Fixed issue causing implicit creation of a new cache when SQL API was used with a name of non-existing cache. |
| GG-32404 | Python thin client now returns a more clear error message on authentication failure. Also, added the AuthenticationError error class to help user handle similar issues. |
| GG-31727 | Fixed issue that prevented Python from working correctly with objects created using other platforms and clients. |
| GG-31694 | Fixed issue that could cause client freezing when client was getting objects with null fields from cache. |
| GG-28235 | Default SQL result set page size was increased from 1 to 1024. Page size of 1 was causing poor performance when fetching multiple rows using SQL. |
| GG-27755 | Fixed issue causing boolean value to be returned as ints. |
| GG-32415 | Python thin client now returns the time zone-independent values while working with date/time types (when used with latest server release). |

## Installation and Upgrade Information

To upgrade an existing package, use the following command:

```shell
pip install --upgrade pygridgain
```

To install the latest version of a package:

```shell
pip install pygridgain
```

To install a specific version:

```shell
pip install pygridgain==1.2.0
```

### Known Limitations

#### Argument `schema` of `Client.sql` Call in pygridgain-1.2.0 and Later

In PyGridGain earlier than 1.2.0 version, the `schema` argument of the `Client.sql` API call is treated as a cache name and implicitly creates cache with such a name if it is not present. In particular, when the `schema` argument was not specified by user, the "PUBLIC" schema was used by default, which could led to the creation of a cache with "PUBLIC" name. Presently, the cache is not created implicitly. In some cases, this can cause the "Cache does not exists" errors after upgrading to a newer version.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
