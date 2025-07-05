# Information Schema plugins: SHOW and FLUSH statements

Information Schema plugins can support [SHOW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show) and [FLUSH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) statements.

## SHOW

`SHOW` statements support is enabled automatically. A plugin only needs to specify column names for the `SHOW` statement in the `old_name` member of the field declaration structure. Columns with the `old_name` set to 0 will be hidden from the `SHOW` statement. If all columns are hidden, the `SHOW` statement will not work for this plugin.

Note that `SHOW` statement is a user-friendly shortcut; it's easier to type and should be easier to view — if the Information Schema table contains many columns, the `SHOW` statement is supposed to display only most important columns and fit nicely on the 80x25 terminal screen.

Consider an example, [LOCALES plugin](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md):

```
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

While the [INFORMATION\_SCHEMA.LOCALES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-locales-table) table has 8 columns, the [SHOW LOCALES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-locales) statement will only display 4 of them:

```
MariaDB [test]> show locales;
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

To support the `FLUSH` statement a plugin must declare the `reset_table` callback. For example, in the [QUERY\_RESPONSE\_TIME](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/plugins/other-plugins/query-response-time-plugin.md) plugin:

```
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
