# COM\_FIELD\_LIST

{% hint style="info" %}
This command is deprecated and not used by MariaDB connectors any more. Use the SQL statements [SHOW COLUMNS](../../sql-statements/administrative-sql-statements/show/show-columns.md) or [SELECT FROM INFORMATION\_SCHEMA.COLUMNS](../../system-tables/information-schema/information-schema-tables/information-schema-columns-table.md) instead.
{% endhint %}

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x04 : COM\_FIELD\_LIST header.
* [string<nul>](../protocol-data-types.md#null-terminated-strings) Table name.
* [string<eof>](../protocol-data-types.md#end-of-file-length-strings) Optional field list.

## Response

* zero or more [result set rows](../4-server-response-packets/resultset-row.md).
* [EOF packet](../4-server-response-packets/eof_packet.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
