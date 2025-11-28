---
description: >-
  Verify the validity of a view's algorithm. This statement checks if the view
  definition is correct and references existing tables.
---

# CHECK VIEW

## Syntax

```sql
CHECK VIEW view_name
```

## Description

The `CHECK VIEW` statement checks whether the view algorithm is correct. It is run as part of [mariadb-upgrade](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md), and should not normally be required in regular use.

## See Also

* [REPAIR VIEW](repair-view.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
