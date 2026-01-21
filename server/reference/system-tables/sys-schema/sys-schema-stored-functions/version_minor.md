---
description: >-
  This function returns the minor version number of the MariaDB Server instance,
  such as the 6 in 10.6.4.
---

# version\_minor

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.version_minor()
```

## Description

`version_minor` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It returns the MariaDB Server minor release version.

## Examples

```sql
SELECT VERSION(),
 sys.version_major() AS major, 
 sys.version_minor() AS minor,
 sys.version_patch() AS patch;
+----------------+-------+-------+-------+
| VERSION()      | major | minor | patch |
+----------------+-------+-------+-------+
| 10.8.2-MariaDB |    10 |     8 |     2 |
+----------------+-------+-------+-------+
```

## See Also

* [version\_major](version_major.md)
* [version\_patch](version_patch.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
