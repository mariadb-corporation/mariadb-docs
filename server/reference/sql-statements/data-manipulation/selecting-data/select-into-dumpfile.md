---
description: >-
  Export a single row to a file without formatting. This statement writes raw
  binary data, such as BLOBs, directly to a file on the server.
---

# SELECT INTO DUMPFILE

## Syntax

```sql
SELECT ... INTO DUMPFILE 'file_path'
```

## Description

`SELECT ... INTO DUMPFILE` is a [SELECT](select.md) clause which writes the resultset into a single unformatted row, without any separators, in a file. The results will not be returned to the client.

_file\_path_ can be an absolute path, or a relative path starting from the data directory. It can only be specified as a [string literal](../../../sql-structure/sql-language-structure/string-literals.md), not as a variable. However, the statement can be dynamically composed and executed as a prepared statement to work around this limitation.

This statement is binary-safe and so is particularly useful for writing [BLOB](../../../data-types/string-data-types/blob.md) values to file. It can be used, for example, to copy an image or an audio document from the database to a file.

The file must not exist. It cannot be overwritten. A user needs the [FILE](../../account-management-sql-statements/grant.md#global-privileges) privilege to run this statement. Also, MariaDB needs permission to write files in the specified location. If the [secure\_file\_priv](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_file_priv) system variable is set to a non-empty directory name, the file can only be written to that directory.

{% tabs %}
{% tab title="Current" %}
The [character\_set\_filesystem](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem) system variable has controlled interpretation of file names that are given as literal strings.
{% endtab %}

{% tab title="< 5.1" %}
The [character\_set\_filesystem](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_filesystem) system variable does not have controlled interpretation of file names that are given as literal strings.
{% endtab %}
{% endtabs %}

## Example

```sql
SELECT _utf8'Hello world!' INTO DUMPFILE '/tmp/world';

SELECT LOAD_FILE('/tmp/world') AS world;
+--------------+
| world        |
+--------------+
| Hello world! |
+--------------+
```

## See Also

* [SELECT](select.md)
* [LOAD\_FILE()](../../../sql-functions/string-functions/load_file.md)
* [SELECT INTO Variable](../../programmatic-compound-statements/selectinto.md)
* [SELECT INTO OUTFILE](select-into-outfile.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
