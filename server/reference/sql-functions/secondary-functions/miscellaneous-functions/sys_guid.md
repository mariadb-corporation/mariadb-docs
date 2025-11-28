---
description: >-
  Generate a UUID without hyphens. This Oracle-compatible function returns a
  globally unique identifier as a 32-character hexadecimal string.
---

# SYS\_GUID

{% hint style="info" %}
`SYS_GUID` is available from MariaDB [10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes).
{% endhint %}

The `SYS_GUID` function was introduced to enhance Oracle compatibility. Similar functionality can be achieved with the [UUID](uuid.md) function.

## Syntax

```sql
SYS_GUID()
```

## Description

Returns a 16-byte globally unique identifier (GUID), similar to the [UUID](uuid.md) function, but without the `-` character.

## Example

```sql
SELECT SYS_GUID();
+----------------------------------+
| SYS_GUID()                       |
+----------------------------------+
| 2C574E45BA2811EBB265F859713E4BE4 |
+----------------------------------+
```

## See Also

* [UUID](uuid.md)
* [UUID\_SHORT](uuid_short.md)
* [UUID data type](../../../data-types/string-data-types/uuid-data-type.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

