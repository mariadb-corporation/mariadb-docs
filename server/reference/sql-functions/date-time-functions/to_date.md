---
hidden: true
---

# TO\_DATE

{% hint style="info" %}
This function is available from MariaDB 12.3.
{% endhint %}

## Syntax

```sql
TO_DATE(string_expression [DEFAULT string_expression ON CONVERSION ERROR],
        format_string [,NLS_FORMAT_STRING])
```

## Description

`TO_DATE` was added for Oracle support.

* `format_string` has the same format elements as [TO\_CHAR()](../string-functions/to_char.md), except a few elements that are not supported (see below). `TO_DATE()` returns a [datetime](../../data-types/date-and-time-data-types/datetime.md) value.
* The allowed separators are the same as for `TO_CHAR()`: space ( ), tab (`\t`), and any of `!`, `#`,`%`, `'`, `()`, `*`, `+`,`-`, `.`, `/`, `:`, `;`, `<=>`.
* `&` can be used if the next character is not a character in the `a-z` or `A-Z` range. `text` indicates a text string that is used verbatim in the format. You cannot use the double-quote (`"`) as a separator.
* `NLS_FORMAT_STRING` supports these options: `NLS_CALENDAR=GREGORIAN` and `NLS_DATE_LANGUAGE=`_`language`_, where _`language`_ can be one of the following:
  * All MariaDB short locales, like `en_AU`.
  * The following Oracle language names: ALBANIAN, AMERICAN, ARABIC, BASQUE, BELARUSIAN, BRAZILIAN PORTUGUESE, BULGARIAN, CANADIAN FRENCH, CATALAN, CROATIAN, CYRILLIC SERBIAN, CZECH, DANISH, DUTCH, ENGLISH, ESTONIAN, FINNISH, FRENCH, GERMAN, GREEK, HEBREW, HINDI, HUNGARIAN, ICELANDIC, INDONESIAN, ITALIAN, JAPANESE, KANNADA, KOREAN, LATIN AMERICAN SPANISH, LATVIAN, LITHUANIAN, MACEDONIAN, MALAY, MEXICAN SPANISH, NORWEGIAN, POLISH, PORTUGUESE, ROMANIAN, RUSSIAN, SIMPLIFIED CHINESE, SLOVAK, SLOVENIAN, SPANISH, SWAHILI, SWEDISH, TAMIL, THAI, TRADITIONAL CHINESE, TURKISH, UKRAINIAN, VIETNAMESE

### Supported Format Elements

* `AD` – Anno Domini ("in the year of the Lord")
* `AD_DOT` – Anno Domini ("in the year of the Lord")&#x20;
* `AM` – Meridian indicator (before midday)
* `AM_DOT` – Meridian indicator (before midday)
* `DAY` – Name of day
* `DD` – Day (1-31)
* `DDD` – Day of year (1-336)
* `DY` – Abbreviated name of day
* `FF[1-6]` – Fractional seconds
* `HH` – Hour (1-12)
* `HH12` – Hour (1-12)
* `HH24` – Hour (0-23)
* `MI` – Minutes (0-59)
* `MM` – Month (1-12)
* `MON` – Abbreviated name of month
* `MONTH` – Name of Month
* `PM` – Meridian indicator (after midday)
* `PM_DOT` – Meridian indicator (after midday)
* `RR` – 20th century dates in the 21st century. 2 digits in the `50-99` range are assumed starting from the year 2000, and `0-49` is assumed from 1900.&#x20;
* `RRRR` – 20th century dates in the 21st century. 4 digits
* `SS` – Seconds
* `SYYYY` – Signed 4-digit year; MariaDB only supports positive years
* `Y` – 1-digit year
* `YY` – 2-digit year
* `YYY` – 3-digit year
* `YYYY` – 4 digit year

{% hint style="info" %}
If no datetime is given, the current datetime is used. For example, if `'MM-DD HH-MM-SS'` is given, the current year is used. (This is Oracle behavior.)
{% endhint %}

### Unsupported Options

* `BC`, `D`, `DL`, `DS`, `E`, `EE`, `FM`, `FX`, `RM`, `SSSSS`, `TS`, `TZD`, `TZH`, `TZR`, `X`, and `SY BC` are not supported by MariaDB [datetime](../../data-types/date-and-time-data-types/datetime.md).
* Most other formats do not make sense in a MariaDB context, as we return  `datetime` with fractions, not as a string.
* `D` (day-of-week) is not supported as it is not clear how it would map to MariaDB. This element depends on the NLS territory of the session.
* `RR` only works with 2-digit years. (In Oracle, `RR` may also work with 4-digit years in some context, but the rules are not clear.)

### Extensions and Differences Compared to Oracle

* MariaDB supports `FF` (fractional seconds). If `FF[#]` is used, `TO_DATE`  returns a `datetime` with `#` of subseconds. If `FF` is not used, a `datetime` is returned. A warning (but no error) is issued if the string contains more digits than specified with `F(#]`.
* Names can be shortened to their unique prefixes. For example, both `January` and `Ja` work fine.
* No error is issued if the datetime string is shorter than `format_string` and the next unused character is not a number. This is useful to get a `datetime` from a mixed set of strings in `datetime` format. By contrast, Oracle gives an error if the `datetime` string is too short.
* MariaDB supports short locales as language names.
* `NLS_DATE_FORMAT` can use double-quote (`"`) and single-quote (`'`) for quoting.
* `NLS_DATE_FORMAT` must be a constant string. This is to ensure that the server knows which locale to use when executing the function.

## Examples

Convert a textual date and time to `DATE` format:

```sql
SELECT TO_DATE('February 5, 2026, 20:56','%Y-%m-%e')
+-----------------------------------------------+
| TO_DATE('February 5, 2026, 20:56','%Y-%m-%e') |
+-----------------------------------------------+
| 2026-02-05                                    |
+-----------------------------------------------+
```

