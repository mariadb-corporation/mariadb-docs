---
description: >-
  Update and distribute MariaDB ColumnStore configuration files: edit
  Columnstore.xml on PM1, then run mcsadmin distributeconfigfile to propagate
  changes to other nodes.
---

# ColumnStore Configuration File Update and Distribution

In case where an entry in the MariaDB ColumnStore's configuration needs to be updated and distributed, this can be done from the command line from Performance Module #1. All changes made to MariaDB ColumnStore's configuration file need to be applied on PM1.

{% hint style="info" %}
`mcsadmin distributeconfigfile` only needs to be run if the system is active. If the system is down, then just make the change, and when the system is started, the update will get distributed.
{% endhint %}

Here is an example:

```sql
/usr/local/mariadb/columnstore/bin/configxml.sh setconfig SystemConfig SystemName mcs-1
mcsadmin distributeconfigfile
```

In the cases where MariaDB ColumnStore's configuration files get out of sync with the PM1 copy, run the following to get MariaDB ColumnStore's configuration file redistribute to the other nodes.

To do this run the following on PM1:

```sql
mscadmin distributeconfigfile
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
