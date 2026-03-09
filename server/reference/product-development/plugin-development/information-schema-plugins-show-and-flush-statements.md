---
description: >-
  Explains how to create plugins that expose internal server data through
  virtual tables in the Information Schema.
---

# Information Schema Plugins: SHOW and FLUSH Statements

{% include "../../../.gitbook/includes/this-page-contains-backgrou....md" %}

Information Schema plugins support [SHOW](../../sql-statements/administrative-sql-statements/show/) and [FLUSH](../../sql-statements/administrative-sql-statements/flush-commands/flush.md) statements.

## SHOW

`SHOW` statement support is enabled by default. A plugin only has to specify column names for the `SHOW` statement in the `old_name` member of the field declaration structure. Columns with the `old_name` set to `0` are hidden from the `SHOW` statement. If all columns are hidden, the `SHOW` statement doesn't work for this plugin.

Note that `SHOW`` `_`statement`_ is a user-friendly shortcut – it's easier to type and view. If the Information Schema table contains many columns, the `SHOW` statement is supposed to display only the most important columns, so that the output fits nicely on the 80x25 terminal screen.

Consider an example, the [LOCALES plugin](../../data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md):

```c
static ST_FIELD_INFO locale_info_locale_fields_info[]=
{
  {"ID", 4, MYSQL_TYPE_LONGLONG, 0, 0, "Id", 0},
  {"NAME", 255, MYSQL_TYPE_STRING, 0, 0, "Name", 0},
  {"DESCRIPTION", 255,  MYSQL_TYPE_STRING, 0, 0, "Description", 0},
  {"MAX_MONTH_NAME_LENGTH", 4, MYSQL_TYPE_LONGLONG, 0, 0, 0, 0},
  {"MAX_DAY_NAME_LENGTH", 4, MYSQL_TYPE_LONGLONG, 0, 0, 0, 0},
  {"DECIMAL_POINT", 2, MYSQL_TYPE_STRING, 0, 0, 0, 0},
  {"THOUSAND_SEP", 2, MYSQL_TYPE_STRING, 0, 0, 0, 0},
  {"ERROR_MESSAGE_LANGUAGE", 64, MYSQL_TYPE_STRING, 0, 0, "Error_Message_Language", 0},
  {0, 0, MYSQL_TYPE_STRING, 0, 0, 0, 0}
};
```

While the [INFORMATION\_SCHEMA.LOCALES](../../system-tables/information-schema/information-schema-tables/information-schema-locales-table.md) table has 8 columns, the [SHOW LOCALES](../../sql-statements/administrative-sql-statements/show/show-locales.md) statement only displays 4 of them:

```sql
MariaDB [test]> SHOW LOCALES;
+-----+-------+-------------------------------------+------------------------+
| Id  | Name  | Description                         | Error_Message_Language |
+-----+-------+-------------------------------------+------------------------+
|   0 | en_US | English - United States             | english                |
|   1 | en_GB | English - United Kingdom            | english                |
|   2 | ja_JP | Japanese - Japan                    | japanese               |
|   3 | sv_SE | Swedish - Sweden                    | swedish                |
...
```

## FLUSH

To support the `FLUSH` statement, a plugin must declare the `reset_table` callback. For example, in the [QUERY\_RESPONSE\_TIME](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/plugins/other-plugins/query-response-time-plugin.md) plugin:

```c
static int query_response_time_info_init(void *p)
{
  ST_SCHEMA_TABLE *i_s_query_response_time= (ST_SCHEMA_TABLE *) p;
  i_s_query_response_time->fields_info= query_response_time_fields_info;
  i_s_query_response_time->fill_table= query_response_time_fill;
  i_s_query_response_time->reset_table= query_response_time_flush;
  query_response_time_init();
  return 0;
}
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
