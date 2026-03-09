---
description: >-
  Reference for the DROP CATALOG statement, used to remove a catalog and all its
  associated databases and users.
---

# DROP CATALOG

{% include "../../../.gitbook/includes/catalogs.md" %}

## Syntax

```bnf
DROP CATALOG catalog_name
```

## Description

Deletes a [catalog](./).

Limitations:

* `DROP CATALOG` can only be performed by a super user in the 'def' catalog.
* The current catalog cannot be dropped.
* The 'def' catalog cannot be dropped.

When dropping a catalog, all databases and files within that catalog will be deleted.

## See Also

* [CREATE CATALOG](create-catalog.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
