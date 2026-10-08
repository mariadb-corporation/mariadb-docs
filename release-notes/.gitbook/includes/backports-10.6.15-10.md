---
title: backports-10.6.15-10
---

* [JSON\_OVERLAPS()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps) has been backported. ([MENT-1853](https://jira.mariadb.org/browse/MENT-1853))
  * The `JSON_OVERLAPS()` function can be used to compare two JSON documents to determine if they have any key-value pairs or array elements in common.

```sql
SELECT JSON_OVERLAPS('{"A": 1, "B": {"C":2}}', '{"A": 2, "B": {"C":2}}') AS is_overlap;
```

```
+---------------------+
| is_overlap          |
+---------------------+
| 1                   |
+---------------------+
```

* [JSON\_SCHEMA\_VALID()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid) has been backported. ([MENT-1796](https://jira.mariadb.org/browse/MENT-1796))
  * The `JSON_SCHEMA_VALID()` function can be used to validate a JSON document against a JSON schema, as documented by the [JSON Schema Draft 2020.](https://json-schema.org/draft/2020-12/release-notes)
  * This function can also be used in a `CHECK` constraint to verify that JSON documents are only stored in the database if they include required items and that the values are within a given range and length.
