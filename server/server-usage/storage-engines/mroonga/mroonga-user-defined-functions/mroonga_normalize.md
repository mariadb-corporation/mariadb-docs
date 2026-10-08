---
description: >-
  This UDF normalizes a given string using Groonga's normalizers, ensuring
  consistent text processing for accurate indexing and searching.
---

# mroonga\_normalize

## Syntax

```
mroonga_normalize(string[, normalizer_name])
```

## Description

`mroonga_normalize` is a [user-defined function](../../../user-defined-functions/) (UDF) included with the [Mroonga storage engine](../). It uses Groonga's normalizer to normalize text. See [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md) for details on creating this UDF if required.

Given a string, returns the normalized text.

See the [Groonga Normalizer Reference](https://groonga.org/docs/reference/normalizers.html) for details on the Groonga normalizers. The default if no normalizer is provided is `NormalizerAuto`.

## Examples

```sql
SELECT mroonga_normalize("ABぃ㍑");
+-------------------------------+
| mroonga_normalize("ABぃ㍑")   |
+-------------------------------+
| abぃリットル                  |
+-------------------------------+
```

## See Also

* [Creating Mroonga User-Defined Functions](creating-mroonga-user-defined-functions.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
