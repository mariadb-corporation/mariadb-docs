---
description: >-
  ColumnStore compression mode is set via infinidb_compression_type at
  instance or session scope, controlling whether new tables and added columns
  use snappy compression by default.
---

# ColumnStore Compression Mode

MariaDB ColumnStore has the ability to compress data and this is controlled through a compression mode. This compression mode may be set as a default for the instance or set at the session level.

To set the compression mode at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.

```sql
set infinidb_compression_type = n
```

where n is:

1. 0 = Compression is turned off. Any subsequent table create statements run will have compression turned off for that table unless any statement overrides have been performed. Any `ALTER` statements run to add a column will have compression turned off for that column unless any statement override has been performed.
2. 1 = Compression is turned on. Any subsequent table create statements run will have compression turned on for that table unless any statement overrides have been performed. Any `ALTER` statements run to add a column will have compression turned on for that column unless any statement override has been performed. ColumnStore uses snappy compression in this mode.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
