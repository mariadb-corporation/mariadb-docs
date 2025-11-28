---
description: >-
  Return the substring matching a regex. This function extracts the actual part
  of the string that matches the given pattern.
---

# REGEXP\_SUBSTR

## Syntax

```sql
REGEXP_SUBSTR(subject,pattern)
```

## Description

Returns the part of the string `subject` that matches the regular expression `pattern`, or an empty string if `pattern` was not found.

The function follows the case sensitivity rules of the effective [collation](../../../data-types/string-data-types/character-sets/). Matching is performed case insensitively for case insensitive collations, and case sensitively for case sensitive collations and for binary data.

The collation case sensitivity can be overwritten using the (?i) and (?-i) PCRE flags.

MariaDB uses the [PCRE regular expression](pcre.md) library for enhanced regular expression performance, and `REGEXP_SUBSTR` was introduced as part of this enhancement.

The [default\_regex\_flags](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable addresses the remaining compatibilities between PCRE and the old regex library.

## Examples

```sql
SELECT REGEXP_SUBSTR('ab12cd','[0-9]+');
-> 12

SELECT REGEXP_SUBSTR(
  'See https://mariadb.org/en/foundation/ for details',
  'https?://[^/]*');
-> https://mariadb.org
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
