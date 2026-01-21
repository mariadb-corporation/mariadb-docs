---
description: >-
  The Information Schema DISKS table, created by the DISKS plugin, displays
  metadata such as total and available space for disks on the system.
---

# Information Schema DISKS Table

{% hint style="warning" %}
The plugin only works on Linux.
{% endhint %}

## Description

The `DISKS` table is created when the [DISKS](../../../plugins/other-plugins/disks-plugin.md) plugin is enabled, and shows metadata about disks on the system.

{% tabs %}
{% tab title="Current" %}
This plugin requires the [FILE privilege](../../../sql-statements/account-management-sql-statements/grant.md).
{% endtab %}

{% tab title="< 10.4.7 / 10.3.17 / 10.2.26 / 10.1.41" %}
{% hint style="danger" %}
This plugin does **not** check [user privileges](../../../sql-statements/account-management-sql-statements/grant.md). When it is enabled, **any** user can query the `INFORMATION_SCHEMA.DISKS` table and see all the information it provides.
{% endhint %}
{% endtab %}
{% endtabs %}

The table contains the following columns:

| Column    | Description                                         |
| --------- | --------------------------------------------------- |
| DISK      | Name of the disk itself.                            |
| PATH      | Mount point of the disk.                            |
| TOTAL     | Total space in KiB.                                 |
| USED      | Used amount of space in KiB.                        |
| AVAILABLE | Amount of space in KiB available to non-root users. |

Note that as the amount of space available to root (OS user) may be more that what is available to non-root users, 'available' + 'used' may be less than 'total'.

All paths to which a particular disk has been mounted are reported. The rationale is that someone might want to take different action e.g. depending on which disk is relevant for a particular path. This leads to the same disk being reported multiple times.

## Example

```sql
SELECT * FROM information_schema.DISKS;

+-----------+-------+----------+---------+-----------+
| Disk      | Path  | Total    | Used    | Available |
+-----------+-------+----------+---------+-----------+
| /dev/vda1 | /     | 26203116 | 2178424 |  24024692 |
| /dev/vda1 | /boot | 26203116 | 2178424 |  24024692 |
| /dev/vda1 | /etc  | 26203116 | 2178424 |  24024692 |
+-----------+-------+----------+---------+-----------+
```

## See Also

* [Disks Plugin](../../../plugins/other-plugins/disks-plugin.md) for details on installing, options
* [Plugin Overview](../../../plugins/plugin-overview.md) for details on managing plugins.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
