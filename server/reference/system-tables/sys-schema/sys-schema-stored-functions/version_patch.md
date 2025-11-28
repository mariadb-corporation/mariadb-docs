---
description: >-
  This function returns the patch release version number of the MariaDB Server
  instance, such as the 4 in 10.6.4.
---

# version\_patch

{% include "../../../../.gitbook/includes/sys-schema-is-available-fro....md" %}

## Syntax

```
sys.version_patch()
```

## Description

`version_patch` is a [stored function](../../../../server-usage/stored-routines/stored-functions/) available with the [Sys Schema](../).

It returns the MariaDB Server patch release version.

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
* [version\_minor](version_minor.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
