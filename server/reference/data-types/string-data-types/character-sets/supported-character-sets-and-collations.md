---
description: >-
  View a comprehensive list of the character sets and collations available in
  MariaDB database, including their default properties and maximum lengths.
---

# Supported Character Sets and Collations

## Character Sets

You can see which character sets are available in a particular version by running the [SHOW CHARACTER SET](../../../sql-statements/administrative-sql-statements/show/show-character-set.md) statement or by querying the [Information Schema CHARACTER\_SETS Table](../../../system-tables/information-schema/information-schema-tables/information-schema-character_sets-table.md).

{% tabs %}
{% tab title="Current" %}
It is possible to change the default collation associated with a character set. See [Changing Default Collation](setting-character-sets-and-collations.md#changing-default-collation).
{% endtab %}

{% tab title="< 11.2" %}
It is **not** possible to change the default collation associated with a character set. See [Changing Default Collation](setting-character-sets-and-collations.md#changing-default-collation)
{% endtab %}
{% endtabs %}

MariaDB supports the following character sets:

| Charset  | Description                 | Default collation                                                                                                                                                                                                                                                                                                                                        | Maxlen                                                                               |
| -------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| armscii8 | ARMSCII-8 Armenian          | armscii8\_general\_ci                                                                                                                                                                                                                                                                                                                                    | 1                                                                                    |
| ascii    | US ASCII                    | ascii\_general\_ci                                                                                                                                                                                                                                                                                                                                       | 1                                                                                    |
| big5     | Big5 Traditional Chinese    | big5\_chinese\_ci                                                                                                                                                                                                                                                                                                                                        | 2                                                                                    |
| binary   | Binary pseudo charset       | binary                                                                                                                                                                                                                                                                                                                                                   | 1                                                                                    |
| cp1250   | Windows Central European    | cp1250\_general\_ci                                                                                                                                                                                                                                                                                                                                      | 1                                                                                    |
| cp1251   | Windows Cyrillic            | cp1251\_general\_ci                                                                                                                                                                                                                                                                                                                                      | 1                                                                                    |
| cp1256   | Windows Arabic              | cp1256\_general\_ci                                                                                                                                                                                                                                                                                                                                      | 1                                                                                    |
| cp1257   | Windows Baltic              | cp1257\_general\_ci                                                                                                                                                                                                                                                                                                                                      | 1                                                                                    |
| cp850    | DOS West European           | cp850\_general\_ci                                                                                                                                                                                                                                                                                                                                       | 1                                                                                    |
| cp852    | DOS Central European        | cp852\_general\_ci                                                                                                                                                                                                                                                                                                                                       | 1                                                                                    |
| cp866    | DOS Russian                 | cp866\_general\_ci                                                                                                                                                                                                                                                                                                                                       | 1                                                                                    |
| cp932    | SJIS for Windows Japanese   | cp932\_japanese\_ci                                                                                                                                                                                                                                                                                                                                      | 2                                                                                    |
| dec8     | DEC West European           | dec8\_swedish\_ci                                                                                                                                                                                                                                                                                                                                        | 1                                                                                    |
| eucjpms  | UJIS for Windows Japanese   | eucjpms\_japanese\_ci                                                                                                                                                                                                                                                                                                                                    | 3                                                                                    |
| euckr    | EUC-KR Korean               | euckr\_korean\_ci                                                                                                                                                                                                                                                                                                                                        | 2                                                                                    |
| gb2312   | GB2312 Simplified Chinese   | gb2312\_chinese\_ci                                                                                                                                                                                                                                                                                                                                      | 2                                                                                    |
| gbk      | GBK Simplified Chinese      | gbk\_chinese\_ci                                                                                                                                                                                                                                                                                                                                         | 2                                                                                    |
| geostd8  | GEOSTD8 Georgian            | geostd8\_general\_ci                                                                                                                                                                                                                                                                                                                                     | 1                                                                                    |
| greek    | ISO 8859-7 Greek            | greek\_general\_ci                                                                                                                                                                                                                                                                                                                                       | 1                                                                                    |
| hebrew   | ISO 8859-8 Hebrew           | hebrew\_general\_ci                                                                                                                                                                                                                                                                                                                                      | 1                                                                                    |
| hp8      | HP West European            | hp8\_english\_ci                                                                                                                                                                                                                                                                                                                                         | 1                                                                                    |
| keybcs2  | DOS Kamenicky Czech-Slovak  | keybcs2\_general\_ci                                                                                                                                                                                                                                                                                                                                     | 1                                                                                    |
| koi8r    | KOI8-R Relcom Russian       | koi8r\_general\_ci                                                                                                                                                                                                                                                                                                                                       | 1                                                                                    |
| koi8u    | KOI8-U Ukrainian            | koi8u\_general\_ci                                                                                                                                                                                                                                                                                                                                       | 1                                                                                    |
| latin1   | cp1252 West European        | latin1\_swedish\_ci                                                                                                                                                                                                                                                                                                                                      | 1                                                                                    |
| latin2   | ISO 8859-2 Central European | latin2\_general\_ci                                                                                                                                                                                                                                                                                                                                      | 1                                                                                    |
| latin5   | ISO 8859-9 Turkish          | latin5\_turkish\_ci                                                                                                                                                                                                                                                                                                                                      | 1                                                                                    |
| latin7   | ISO 8859-13 Baltic          | latin7\_general\_ci                                                                                                                                                                                                                                                                                                                                      | 1                                                                                    |
| macce    | Mac Central European        | macce\_general\_ci                                                                                                                                                                                                                                                                                                                                       | 1                                                                                    |
| macroman | Mac West European           | macroman\_general\_ci                                                                                                                                                                                                                                                                                                                                    | 1                                                                                    |
| sjis     | Shift-JIS Japanese          | sjis\_japanese\_ci                                                                                                                                                                                                                                                                                                                                       | 2                                                                                    |
| swe7     | 7bit Swedish                | swe7\_swedish\_ci                                                                                                                                                                                                                                                                                                                                        | 1                                                                                    |
| tis620   | TIS620 Thai                 | tis620\_thai\_ci                                                                                                                                                                                                                                                                                                                                         | 1                                                                                    |
| ucs2     | UCS-2 Unicode               | <p>ucs2_general_ci (&#x3C;= MariaDB 11.4)<br>ucs2_uca1400_ai_ci (>=<a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115">MariaDB 11.5</a>)</p>                                                                                                          | 2                                                                                    |
| ujis     | EUC-JP Japanese             | ujis\_japanese\_ci                                                                                                                                                                                                                                                                                                                                       | 3                                                                                    |
| utf8     | UTF-8 Unicode               | utf8\_general\_ci                                                                                                                                                                                                                                                                                                                                        | 3/4 (see [OLD\_MODE](../../../../server-management/variables-and-modes/old_mode.md)) |
| utf16    | UTF-16 Unicode              | <p>utf16_general_ci (&#x3C;= <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114">MariaDB 11.4</a>)<br>utf16_uca1400_ai_ci (>=<a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115">MariaDB 11.5</a>)</p> | 4                                                                                    |
| utf16le  | UTF-16LE Unicode            | utf16le\_general\_ci                                                                                                                                                                                                                                                                                                                                     | 4                                                                                    |
| utf32    | UTF-32 Unicode              | utf32\_general\_ci (<= [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114)) utf32\_uca1400\_ai\_ci (>=[MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115))                                 | 4                                                                                    |
| utf8mb3  | UTF-8 Unicode               | utf8mb3\_general\_ci (<= [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114)) utf8mb3\_uca1400\_ai\_ci (>=[MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115))                             | 3                                                                                    |
| utf8mb4  | UTF-8 Unicode               | utf8mb4\_general\_ci (<= [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114)) utf8mb4\_uca1400\_ai\_ci (>=[MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115))                             | 4                                                                                    |

{% hint style="warning" %}
Note that the [Mroonga Storage Engine](../../../../server-usage/storage-engines/mroonga/) only supports a limited number of character sets. See [Mroonga's available character sets](../../../../server-usage/storage-engines/mroonga/about-mroonga.md#available-character-sets).
{% endhint %}

## Collations

MariaDB supports the following collations (from [MariaDB 11.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.5)):

```sql
SELECT collation_name, character_set_name as cs_name, id, is_default AS def, is_compiled AS com, 
  sortlen, comment FROM information_schema.collations ORDER BY collation_name;
+--------------------------------+----------+------+------+-----+---------+--------------------------------------------------+
| collation_name                 | cs_name  | id   | def  | com | sortlen | comment                                          |
+--------------------------------+----------+------+------+-----+---------+--------------------------------------------------+
| armscii8_bin                   | armscii8 |   64 |      | Yes |       1 | ARMSCII-8 Armenian                               |
| armscii8_general_ci            | armscii8 |   32 | Yes  | Yes |       1 | ARMSCII-8 Armenian                               |
| armscii8_general_nopad_ci      | armscii8 | 1056 |      | Yes |       1 | ARMSCII-8 Armenian                               |
| armscii8_nopad_bin             | armscii8 | 1088 |      | Yes |       1 | ARMSCII-8 Armenian                               |
| ascii_bin                      | ascii    |   65 |      | Yes |       1 | US ASCII                                         |
| ascii_general_ci               | ascii    |   11 | Yes  | Yes |       1 | US ASCII                                         |
| ascii_general_nopad_ci         | ascii    | 1035 |      | Yes |       1 | US ASCII                                         |
| ascii_nopad_bin                | ascii    | 1089 |      | Yes |       1 | US ASCII                                         |
| big5_bin                       | big5     |   84 |      | Yes |       1 | Big5 Traditional Chinese                         |
| big5_chinese_ci                | big5     |    1 | Yes  | Yes |       1 | Big5 Traditional Chinese                         |
| big5_chinese_nopad_ci          | big5     | 1025 |      | Yes |       1 |                                                  |
| big5_nopad_bin                 | big5     | 1108 |      | Yes |       1 |                                                  |
| binary                         | binary   |   63 | Yes  | Yes |       1 | Binary pseudo charset                            |
| cp1250_bin                     | cp1250   |   66 |      | Yes |       1 | Windows Central European                         |
| cp1250_croatian_ci             | cp1250   |   44 |      | Yes |       1 | Windows Central European                         |
| cp1250_czech_cs                | cp1250   |   34 |      | Yes |       2 | Windows Central European                         |
| cp1250_general_ci              | cp1250   |   26 | Yes  | Yes |       1 | Windows Central European                         |
| cp1250_general_nopad_ci        | cp1250   | 1050 |      | Yes |       1 | Windows Central European                         |
| cp1250_nopad_bin               | cp1250   | 1090 |      | Yes |       1 | Windows Central European                         |
| cp1250_polish_ci               | cp1250   |   99 |      | Yes |       1 | Windows Central European                         |
| cp1251_bin                     | cp1251   |   50 |      | Yes |       1 | Windows Cyrillic                                 |
| cp1251_bulgarian_ci            | cp1251   |   14 |      | Yes |       1 | Windows Cyrillic                                 |
| cp1251_general_ci              | cp1251   |   51 | Yes  | Yes |       1 | Windows Cyrillic                                 |
| cp1251_general_cs              | cp1251   |   52 |      | Yes |       1 | Windows Cyrillic                                 |
| cp1251_general_nopad_ci        | cp1251   | 1075 |      | Yes |       1 | Windows Cyrillic                                 |
| cp1251_nopad_bin               | cp1251   | 1074 |      | Yes |       1 | Windows Cyrillic                                 |
| cp1251_ukrainian_ci            | cp1251   |   23 |      | Yes |       1 | Windows Cyrillic                                 |
| cp1256_bin                     | cp1256   |   67 |      | Yes |       1 | Windows Arabic                                   |
| cp1256_general_ci              | cp1256   |   57 | Yes  | Yes |       1 | Windows Arabic                                   |
| cp1256_general_nopad_ci        | cp1256   | 1081 |      | Yes |       1 | Windows Arabic                                   |
| cp1256_nopad_bin               | cp1256   | 1091 |      | Yes |       1 | Windows Arabic                                   |
| cp1257_bin                     | cp1257   |   58 |      | Yes |       1 | Windows Baltic                                   |
| cp1257_general_ci              | cp1257   |   59 | Yes  | Yes |       1 | Windows Baltic                                   |
| cp1257_general_nopad_ci        | cp1257   | 1083 |      | Yes |       1 | Windows Baltic                                   |
| cp1257_lithuanian_ci           | cp1257   |   29 |      | Yes |       1 | Windows Baltic                                   |
| cp1257_nopad_bin               | cp1257   | 1082 |      | Yes |       1 | Windows Baltic                                   |
| cp850_bin                      | cp850    |   80 |      | Yes |       1 | DOS West European                                |
| cp850_general_ci               | cp850    |    4 | Yes  | Yes |       1 | DOS West European                                |
| cp850_general_nopad_ci         | cp850    | 1028 |      | Yes |       1 | DOS West European                                |
| cp850_nopad_bin                | cp850    | 1104 |      | Yes |       1 | DOS West European                                |
| cp852_bin                      | cp852    |   81 |      | Yes |       1 | DOS Central European                             |
| cp852_general_ci               | cp852    |   40 | Yes  | Yes |       1 | DOS Central European                             |
| cp852_general_nopad_ci         | cp852    | 1064 |      | Yes |       1 | DOS Central European                             |
| cp852_nopad_bin                | cp852    | 1105 |      | Yes |       1 | DOS Central European                             |
| cp866_bin                      | cp866    |   68 |      | Yes |       1 | DOS Russian                                      |
| cp866_general_ci               | cp866    |   36 | Yes  | Yes |       1 | DOS Russian                                      |
| cp866_general_nopad_ci         | cp866    | 1060 |      | Yes |       1 | DOS Russian                                      |
| cp866_nopad_bin                | cp866    | 1092 |      | Yes |       1 | DOS Russian                                      |
| cp932_bin                      | cp932    |   96 |      | Yes |       1 | SJIS for Windows Japanese                        |
| cp932_japanese_ci              | cp932    |   95 | Yes  | Yes |       1 | SJIS for Windows Japanese                        |
| cp932_japanese_nopad_ci        | cp932    | 1119 |      | Yes |       1 |                                                  |
| cp932_nopad_bin                | cp932    | 1120 |      | Yes |       1 |                                                  |
| dec8_bin                       | dec8     |   69 |      | Yes |       1 | DEC West European                                |
| dec8_nopad_bin                 | dec8     | 1093 |      | Yes |       1 | DEC West European                                |
| dec8_swedish_ci                | dec8     |    3 | Yes  | Yes |       1 | DEC West European                                |
| dec8_swedish_nopad_ci          | dec8     | 1027 |      | Yes |       1 | DEC West European                                |
| eucjpms_bin                    | eucjpms  |   98 |      | Yes |       1 | UJIS for Windows Japanese                        |
| eucjpms_japanese_ci            | eucjpms  |   97 | Yes  | Yes |       1 | UJIS for Windows Japanese                        |
| eucjpms_japanese_nopad_ci      | eucjpms  | 1121 |      | Yes |       1 |                                                  |
| eucjpms_nopad_bin              | eucjpms  | 1122 |      | Yes |       1 |                                                  |
| euckr_bin                      | euckr    |   85 |      | Yes |       1 | EUC-KR Korean                                    |
| euckr_korean_ci                | euckr    |   19 | Yes  | Yes |       1 | EUC-KR Korean                                    |
| euckr_korean_nopad_ci          | euckr    | 1043 |      | Yes |       1 |                                                  |
| euckr_nopad_bin                | euckr    | 1109 |      | Yes |       1 |                                                  |
| gb2312_bin                     | gb2312   |   86 |      | Yes |       1 | GB2312 Simplified Chinese                        |
| gb2312_chinese_ci              | gb2312   |   24 | Yes  | Yes |       1 | GB2312 Simplified Chinese                        |
| gb2312_chinese_nopad_ci        | gb2312   | 1048 |      | Yes |       1 |                                                  |
| gb2312_nopad_bin               | gb2312   | 1110 |      | Yes |       1 |                                                  |
| gbk_bin                        | gbk      |   87 |      | Yes |       1 | GBK Simplified Chinese                           |
| gbk_chinese_ci                 | gbk      |   28 | Yes  | Yes |       1 | GBK Simplified Chinese                           |
| gbk_chinese_nopad_ci           | gbk      | 1052 |      | Yes |       1 |                                                  |
| gbk_nopad_bin                  | gbk      | 1111 |      | Yes |       1 |                                                  |
| geostd8_bin                    | geostd8  |   93 |      | Yes |       1 | GEOSTD8 Georgian                                 |
| geostd8_general_ci             | geostd8  |   92 | Yes  | Yes |       1 | GEOSTD8 Georgian                                 |
| geostd8_general_nopad_ci       | geostd8  | 1116 |      | Yes |       1 | GEOSTD8 Georgian                                 |
| geostd8_nopad_bin              | geostd8  | 1117 |      | Yes |       1 | GEOSTD8 Georgian                                 |
| greek_bin                      | greek    |   70 |      | Yes |       1 | ISO 8859-7 Greek                                 |
| greek_general_ci               | greek    |   25 | Yes  | Yes |       1 | ISO 8859-7 Greek                                 |
| greek_general_nopad_ci         | greek    | 1049 |      | Yes |       1 | ISO 8859-7 Greek                                 |
| greek_nopad_bin                | greek    | 1094 |      | Yes |       1 | ISO 8859-7 Greek                                 |
| hebrew_bin                     | hebrew   |   71 |      | Yes |       1 | ISO 8859-8 Hebrew                                |
| hebrew_general_ci              | hebrew   |   16 | Yes  | Yes |       1 | ISO 8859-8 Hebrew                                |
| hebrew_general_nopad_ci        | hebrew   | 1040 |      | Yes |       1 | ISO 8859-8 Hebrew                                |
| hebrew_nopad_bin               | hebrew   | 1095 |      | Yes |       1 | ISO 8859-8 Hebrew                                |
| hp8_bin                        | hp8      |   72 |      | Yes |       1 | HP West European                                 |
| hp8_english_ci                 | hp8      |    6 | Yes  | Yes |       1 | HP West European                                 |
| hp8_english_nopad_ci           | hp8      | 1030 |      | Yes |       1 | HP West European                                 |
| hp8_nopad_bin                  | hp8      | 1096 |      | Yes |       1 | HP West European                                 |
| keybcs2_bin                    | keybcs2  |   73 |      | Yes |       1 | DOS Kamenicky Czech-Slovak                       |
| keybcs2_general_ci             | keybcs2  |   37 | Yes  | Yes |       1 | DOS Kamenicky Czech-Slovak                       |
| keybcs2_general_nopad_ci       | keybcs2  | 1061 |      | Yes |       1 | DOS Kamenicky Czech-Slovak                       |
| keybcs2_nopad_bin              | keybcs2  | 1097 |      | Yes |       1 | DOS Kamenicky Czech-Slovak                       |
| koi8r_bin                      | koi8r    |   74 |      | Yes |       1 | KOI8-R Relcom Russian                            |
| koi8r_general_ci               | koi8r    |    7 | Yes  | Yes |       1 | KOI8-R Relcom Russian                            |
| koi8r_general_nopad_ci         | koi8r    | 1031 |      | Yes |       1 | KOI8-R Relcom Russian                            |
| koi8r_nopad_bin                | koi8r    | 1098 |      | Yes |       1 | KOI8-R Relcom Russian                            |
| koi8u_bin                      | koi8u    |   75 |      | Yes |       1 | KOI8-U Ukrainian                                 |
| koi8u_general_ci               | koi8u    |   22 | Yes  | Yes |       1 | KOI8-U Ukrainian                                 |
| koi8u_general_nopad_ci         | koi8u    | 1046 |      | Yes |       1 | KOI8-U Ukrainian                                 |
| koi8u_nopad_bin                | koi8u    | 1099 |      | Yes |       1 | KOI8-U Ukrainian                                 |
| latin1_bin                     | latin1   |   47 |      | Yes |       1 | cp1252 West European                             |
| latin1_danish_ci               | latin1   |   15 |      | Yes |       1 | cp1252 West European                             |
| latin1_general_ci              | latin1   |   48 |      | Yes |       1 | cp1252 West European                             |
| latin1_general_cs              | latin1   |   49 |      | Yes |       1 | cp1252 West European                             |
| latin1_german1_ci              | latin1   |    5 |      | Yes |       1 | cp1252 West European                             |
| latin1_german2_ci              | latin1   |   31 |      | Yes |       2 | cp1252 West European                             |
| latin1_nopad_bin               | latin1   | 1071 |      | Yes |       1 |                                                  |
| latin1_spanish_ci              | latin1   |   94 |      | Yes |       1 | cp1252 West European                             |
| latin1_swedish_ci              | latin1   |    8 | Yes  | Yes |       1 | cp1252 West European                             |
| latin1_swedish_nopad_ci        | latin1   | 1032 |      | Yes |       1 |                                                  |
| latin2_bin                     | latin2   |   77 |      | Yes |       1 | ISO 8859-2 Central European                      |
| latin2_croatian_ci             | latin2   |   27 |      | Yes |       1 | ISO 8859-2 Central European                      |
| latin2_czech_cs                | latin2   |    2 |      | Yes |       4 | ISO 8859-2 Central European                      |
| latin2_general_ci              | latin2   |    9 | Yes  | Yes |       1 | ISO 8859-2 Central European                      |
| latin2_general_nopad_ci        | latin2   | 1033 |      | Yes |       1 | ISO 8859-2 Central European                      |
| latin2_hungarian_ci            | latin2   |   21 |      | Yes |       1 | ISO 8859-2 Central European                      |
| latin2_nopad_bin               | latin2   | 1101 |      | Yes |       1 | ISO 8859-2 Central European                      |
| latin5_bin                     | latin5   |   78 |      | Yes |       1 | ISO 8859-9 Turkish                               |
| latin5_nopad_bin               | latin5   | 1102 |      | Yes |       1 | ISO 8859-9 Turkish                               |
| latin5_turkish_ci              | latin5   |   30 | Yes  | Yes |       1 | ISO 8859-9 Turkish                               |
| latin5_turkish_nopad_ci        | latin5   | 1054 |      | Yes |       1 | ISO 8859-9 Turkish                               |
| latin7_bin                     | latin7   |   79 |      | Yes |       1 | ISO 8859-13 Baltic                               |
| latin7_estonian_cs             | latin7   |   20 |      | Yes |       1 | ISO 8859-13 Baltic                               |
| latin7_general_ci              | latin7   |   41 | Yes  | Yes |       1 | ISO 8859-13 Baltic                               |
| latin7_general_cs              | latin7   |   42 |      | Yes |       1 | ISO 8859-13 Baltic                               |
| latin7_general_nopad_ci        | latin7   | 1065 |      | Yes |       1 | ISO 8859-13 Baltic                               |
| latin7_nopad_bin               | latin7   | 1103 |      | Yes |       1 | ISO 8859-13 Baltic                               |
| macce_bin                      | macce    |   43 |      | Yes |       1 | Mac Central European                             |
| macce_general_ci               | macce    |   38 | Yes  | Yes |       1 | Mac Central European                             |
| macce_general_nopad_ci         | macce    | 1062 |      | Yes |       1 | Mac Central European                             |
| macce_nopad_bin                | macce    | 1067 |      | Yes |       1 | Mac Central European                             |
| macroman_bin                   | macroman |   53 |      | Yes |       1 | Mac West European                                |
| macroman_general_ci            | macroman |   39 | Yes  | Yes |       1 | Mac West European                                |
| macroman_general_nopad_ci      | macroman | 1063 |      | Yes |       1 | Mac West European                                |
| macroman_nopad_bin             | macroman | 1077 |      | Yes |       1 | Mac West European                                |
| sjis_bin                       | sjis     |   88 |      | Yes |       1 | Shift-JIS Japanese                               |
| sjis_japanese_ci               | sjis     |   13 | Yes  | Yes |       1 | Shift-JIS Japanese                               |
| sjis_japanese_nopad_ci         | sjis     | 1037 |      | Yes |       1 |                                                  |
| sjis_nopad_bin                 | sjis     | 1112 |      | Yes |       1 |                                                  |
| swe7_bin                       | swe7     |   82 |      | Yes |       1 | 7bit Swedish                                     |
| swe7_nopad_bin                 | swe7     | 1106 |      | Yes |       1 | 7bit Swedish                                     |
| swe7_swedish_ci                | swe7     |   10 | Yes  | Yes |       1 | 7bit Swedish                                     |
| swe7_swedish_nopad_ci          | swe7     | 1034 |      | Yes |       1 | 7bit Swedish                                     |
| tis620_bin                     | tis620   |   89 |      | Yes |       1 | TIS620 Thai                                      |
| tis620_nopad_bin               | tis620   | 1113 |      | Yes |       1 |                                                  |
| tis620_thai_ci                 | tis620   |   18 | Yes  | Yes |       4 | TIS620 Thai                                      |
| tis620_thai_nopad_ci           | tis620   | 1042 |      | Yes |       4 |                                                  |
| uca1400_ai_ci                  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_ai_cs                  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_as_ci                  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_as_cs                  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_croatian_ai_ci         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_croatian_ai_cs         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_croatian_as_ci         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_croatian_as_cs         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_croatian_nopad_ai_ci   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_croatian_nopad_ai_cs   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_croatian_nopad_as_ci   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_croatian_nopad_as_cs   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_czech_ai_ci            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_czech_ai_cs            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_czech_as_ci            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_czech_as_cs            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_czech_nopad_ai_ci      | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_czech_nopad_ai_cs      | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_czech_nopad_as_ci      | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_czech_nopad_as_cs      | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_danish_ai_ci           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_danish_ai_cs           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_danish_as_ci           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_danish_as_cs           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_danish_nopad_ai_ci     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_danish_nopad_ai_cs     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_danish_nopad_as_ci     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_danish_nopad_as_cs     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_esperanto_ai_ci        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_esperanto_ai_cs        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_esperanto_as_ci        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_esperanto_as_cs        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_esperanto_nopad_ai_ci  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_esperanto_nopad_ai_cs  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_esperanto_nopad_as_ci  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_esperanto_nopad_as_cs  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_estonian_ai_ci         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_estonian_ai_cs         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_estonian_as_ci         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_estonian_as_cs         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_estonian_nopad_ai_ci   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_estonian_nopad_ai_cs   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_estonian_nopad_as_ci   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_estonian_nopad_as_cs   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_german2_ai_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_german2_ai_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_german2_as_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_german2_as_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_german2_nopad_ai_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_german2_nopad_ai_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_german2_nopad_as_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_german2_nopad_as_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_hungarian_ai_ci        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_hungarian_ai_cs        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_hungarian_as_ci        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_hungarian_as_cs        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_hungarian_nopad_ai_ci  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_hungarian_nopad_ai_cs  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_hungarian_nopad_as_ci  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_hungarian_nopad_as_cs  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_icelandic_ai_ci        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_icelandic_ai_cs        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_icelandic_as_ci        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_icelandic_as_cs        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_icelandic_nopad_ai_ci  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_icelandic_nopad_ai_cs  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_icelandic_nopad_as_ci  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_icelandic_nopad_as_cs  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_latvian_ai_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_latvian_ai_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_latvian_as_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_latvian_as_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_latvian_nopad_ai_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_latvian_nopad_ai_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_latvian_nopad_as_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_latvian_nopad_as_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_lithuanian_ai_ci       | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_lithuanian_ai_cs       | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_lithuanian_as_ci       | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_lithuanian_as_cs       | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_lithuanian_nopad_ai_ci | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_lithuanian_nopad_ai_cs | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_lithuanian_nopad_as_ci | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_lithuanian_nopad_as_cs | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_nopad_ai_ci            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_nopad_ai_cs            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_nopad_as_ci            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_nopad_as_cs            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_persian_ai_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_persian_ai_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_persian_as_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_persian_as_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_persian_nopad_ai_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_persian_nopad_ai_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_persian_nopad_as_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_persian_nopad_as_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_polish_ai_ci           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_polish_ai_cs           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_polish_as_ci           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_polish_as_cs           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_polish_nopad_ai_ci     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_polish_nopad_ai_cs     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_polish_nopad_as_ci     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_polish_nopad_as_cs     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_romanian_ai_ci         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_romanian_ai_cs         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_romanian_as_ci         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_romanian_as_cs         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_romanian_nopad_ai_ci   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_romanian_nopad_ai_cs   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_romanian_nopad_as_ci   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_romanian_nopad_as_cs   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_roman_ai_ci            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_roman_ai_cs            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_roman_as_ci            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_roman_as_cs            | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_roman_nopad_ai_ci      | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_roman_nopad_ai_cs      | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_roman_nopad_as_ci      | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_roman_nopad_as_cs      | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_sinhala_ai_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_sinhala_ai_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_sinhala_as_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_sinhala_as_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_sinhala_nopad_ai_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_sinhala_nopad_ai_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_sinhala_nopad_as_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_sinhala_nopad_as_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovak_ai_ci           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovak_ai_cs           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovak_as_ci           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovak_as_cs           | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovak_nopad_ai_ci     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovak_nopad_ai_cs     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovak_nopad_as_ci     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovak_nopad_as_cs     | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovenian_ai_ci        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovenian_ai_cs        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovenian_as_ci        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovenian_as_cs        | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovenian_nopad_ai_ci  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovenian_nopad_ai_cs  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovenian_nopad_as_ci  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_slovenian_nopad_as_cs  | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish2_ai_ci         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish2_ai_cs         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish2_as_ci         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish2_as_cs         | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish2_nopad_ai_ci   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish2_nopad_ai_cs   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish2_nopad_as_ci   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish2_nopad_as_cs   | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish_ai_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish_ai_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish_as_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish_as_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish_nopad_ai_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish_nopad_ai_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish_nopad_as_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_spanish_nopad_as_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_swedish_ai_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_swedish_ai_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_swedish_as_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_swedish_as_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_swedish_nopad_ai_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_swedish_nopad_ai_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_swedish_nopad_as_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_swedish_nopad_as_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_turkish_ai_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_turkish_ai_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_turkish_as_ci          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_turkish_as_cs          | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_turkish_nopad_ai_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_turkish_nopad_ai_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_turkish_nopad_as_ci    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_turkish_nopad_as_cs    | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_vietnamese_ai_ci       | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_vietnamese_ai_cs       | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_vietnamese_as_ci       | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_vietnamese_as_cs       | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_vietnamese_nopad_ai_ci | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_vietnamese_nopad_ai_cs | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_vietnamese_nopad_as_ci | NULL     | NULL | NULL | Yes |       8 |                                                  |
| uca1400_vietnamese_nopad_as_cs | NULL     | NULL | NULL | Yes |       8 |                                                  |
| ucs2_bin                       | ucs2     |   90 |      | Yes |       1 | UCS-2 Unicode                                    |
| ucs2_croatian_ci               | ucs2     |  640 |      | Yes |       8 |                                                  |
| ucs2_croatian_mysql561_ci      | ucs2     |  149 |      | Yes |       8 |                                                  |
| ucs2_czech_ci                  | ucs2     |  138 |      | Yes |       8 |                                                  |
| ucs2_danish_ci                 | ucs2     |  139 |      | Yes |       8 |                                                  |
| ucs2_esperanto_ci              | ucs2     |  145 |      | Yes |       8 |                                                  |
| ucs2_estonian_ci               | ucs2     |  134 |      | Yes |       8 |                                                  |
| ucs2_general_ci                | ucs2     |   35 | Yes  | Yes |       1 | UCS-2 Unicode                                    |
| ucs2_general_mysql500_ci       | ucs2     |  159 |      | Yes |       1 |                                                  |
| ucs2_general_nopad_ci          | ucs2     | 1059 |      | Yes |       1 |                                                  |
| ucs2_german2_ci                | ucs2     |  148 |      | Yes |       8 |                                                  |
| ucs2_hungarian_ci              | ucs2     |  146 |      | Yes |       8 |                                                  |
| ucs2_icelandic_ci              | ucs2     |  129 |      | Yes |       8 |                                                  |
| ucs2_latvian_ci                | ucs2     |  130 |      | Yes |       8 |                                                  |
| ucs2_lithuanian_ci             | ucs2     |  140 |      | Yes |       8 |                                                  |
| ucs2_myanmar_ci                | ucs2     |  641 |      | Yes |       8 |                                                  |
| ucs2_nopad_bin                 | ucs2     | 1114 |      | Yes |       1 |                                                  |
| ucs2_persian_ci                | ucs2     |  144 |      | Yes |       8 |                                                  |
| ucs2_polish_ci                 | ucs2     |  133 |      | Yes |       8 |                                                  |
| ucs2_romanian_ci               | ucs2     |  131 |      | Yes |       8 |                                                  |
| ucs2_roman_ci                  | ucs2     |  143 |      | Yes |       8 |                                                  |
| ucs2_sinhala_ci                | ucs2     |  147 |      | Yes |       8 |                                                  |
| ucs2_slovak_ci                 | ucs2     |  141 |      | Yes |       8 |                                                  |
| ucs2_slovenian_ci              | ucs2     |  132 |      | Yes |       8 |                                                  |
| ucs2_spanish2_ci               | ucs2     |  142 |      | Yes |       8 |                                                  |
| ucs2_spanish_ci                | ucs2     |  135 |      | Yes |       8 |                                                  |
| ucs2_swedish_ci                | ucs2     |  136 |      | Yes |       8 |                                                  |
| ucs2_thai_520_w2               | ucs2     |  642 |      | Yes |       4 |                                                  |
| ucs2_turkish_ci                | ucs2     |  137 |      | Yes |       8 |                                                  |
| ucs2_unicode_520_ci            | ucs2     |  150 |      | Yes |       8 |                                                  |
| ucs2_unicode_520_nopad_ci      | ucs2     | 1174 |      | Yes |       8 |                                                  |
| ucs2_unicode_ci                | ucs2     |  128 |      | Yes |       8 |                                                  |
| ucs2_unicode_nopad_ci          | ucs2     | 1152 |      | Yes |       8 |                                                  |
| ucs2_vietnamese_ci             | ucs2     |  151 |      | Yes |       8 |                                                  |
| ujis_bin                       | ujis     |   91 |      | Yes |       1 | EUC-JP Japanese                                  |
| ujis_japanese_ci               | ujis     |   12 | Yes  | Yes |       1 | EUC-JP Japanese                                  |
| ujis_japanese_nopad_ci         | ujis     | 1036 |      | Yes |       1 |                                                  |
| ujis_nopad_bin                 | ujis     | 1115 |      | Yes |       1 |                                                  |
| utf16le_bin                    | utf16le  |   62 |      | Yes |       1 | UTF-16LE Unicode                                 |
| utf16le_general_ci             | utf16le  |   56 | Yes  | Yes |       1 | UTF-16LE Unicode                                 |
| utf16le_general_nopad_ci       | utf16le  | 1080 |      | Yes |       1 | UTF-16LE Unicode                                 |
| utf16le_nopad_bin              | utf16le  | 1086 |      | Yes |       1 | UTF-16LE Unicode                                 |
| utf16_bin                      | utf16    |   55 |      | Yes |       1 | UTF-16 Unicode                                   |
| utf16_croatian_ci              | utf16    |  672 |      | Yes |       8 |                                                  |
| utf16_croatian_mysql561_ci     | utf16    |  122 |      | Yes |       8 |                                                  |
| utf16_czech_ci                 | utf16    |  111 |      | Yes |       8 |                                                  |
| utf16_danish_ci                | utf16    |  112 |      | Yes |       8 |                                                  |
| utf16_esperanto_ci             | utf16    |  118 |      | Yes |       8 |                                                  |
| utf16_estonian_ci              | utf16    |  107 |      | Yes |       8 |                                                  |
| utf16_general_ci               | utf16    |   54 | Yes  | Yes |       1 | UTF-16 Unicode                                   |
| utf16_general_nopad_ci         | utf16    | 1078 |      | Yes |       1 | UTF-16 Unicode                                   |
| utf16_german2_ci               | utf16    |  121 |      | Yes |       8 |                                                  |
| utf16_hungarian_ci             | utf16    |  119 |      | Yes |       8 |                                                  |
| utf16_icelandic_ci             | utf16    |  102 |      | Yes |       8 |                                                  |
| utf16_latvian_ci               | utf16    |  103 |      | Yes |       8 |                                                  |
| utf16_lithuanian_ci            | utf16    |  113 |      | Yes |       8 |                                                  |
| utf16_myanmar_ci               | utf16    |  673 |      | Yes |       8 |                                                  |
| utf16_nopad_bin                | utf16    | 1079 |      | Yes |       1 | UTF-16 Unicode                                   |
| utf16_persian_ci               | utf16    |  117 |      | Yes |       8 |                                                  |
| utf16_polish_ci                | utf16    |  106 |      | Yes |       8 |                                                  |
| utf16_romanian_ci              | utf16    |  104 |      | Yes |       8 |                                                  |
| utf16_roman_ci                 | utf16    |  116 |      | Yes |       8 |                                                  |
| utf16_sinhala_ci               | utf16    |  120 |      | Yes |       8 |                                                  |
| utf16_slovak_ci                | utf16    |  114 |      | Yes |       8 |                                                  |
| utf16_slovenian_ci             | utf16    |  105 |      | Yes |       8 |                                                  |
| utf16_spanish2_ci              | utf16    |  115 |      | Yes |       8 |                                                  |
| utf16_spanish_ci               | utf16    |  108 |      | Yes |       8 |                                                  |
| utf16_swedish_ci               | utf16    |  109 |      | Yes |       8 |                                                  |
| utf16_thai_520_w2              | utf16    |  674 |      | Yes |       4 |                                                  |
| utf16_turkish_ci               | utf16    |  110 |      | Yes |       8 |                                                  |
| utf16_unicode_520_ci           | utf16    |  123 |      | Yes |       8 |                                                  |
| utf16_unicode_520_nopad_ci     | utf16    | 1147 |      | Yes |       8 |                                                  |
| utf16_unicode_ci               | utf16    |  101 |      | Yes |       8 |                                                  |
| utf16_unicode_nopad_ci         | utf16    | 1125 |      | Yes |       8 |                                                  |
| utf16_vietnamese_ci            | utf16    |  124 |      | Yes |       8 |                                                  |
| utf32_bin                      | utf32    |   61 |      | Yes |       1 | UTF-32 Unicode                                   |
| utf32_croatian_ci              | utf32    |  736 |      | Yes |       8 |                                                  |
| utf32_croatian_mysql561_ci     | utf32    |  181 |      | Yes |       8 |                                                  |
| utf32_czech_ci                 | utf32    |  170 |      | Yes |       8 |                                                  |
| utf32_danish_ci                | utf32    |  171 |      | Yes |       8 |                                                  |
| utf32_esperanto_ci             | utf32    |  177 |      | Yes |       8 |                                                  |
| utf32_estonian_ci              | utf32    |  166 |      | Yes |       8 |                                                  |
| utf32_general_ci               | utf32    |   60 | Yes  | Yes |       1 | UTF-32 Unicode                                   |
| utf32_general_nopad_ci         | utf32    | 1084 |      | Yes |       1 | UTF-32 Unicode                                   |
| utf32_german2_ci               | utf32    |  180 |      | Yes |       8 |                                                  |
| utf32_hungarian_ci             | utf32    |  178 |      | Yes |       8 |                                                  |
| utf32_icelandic_ci             | utf32    |  161 |      | Yes |       8 |                                                  |
| utf32_latvian_ci               | utf32    |  162 |      | Yes |       8 |                                                  |
| utf32_lithuanian_ci            | utf32    |  172 |      | Yes |       8 |                                                  |
| utf32_myanmar_ci               | utf32    |  737 |      | Yes |       8 |                                                  |
| utf32_nopad_bin                | utf32    | 1085 |      | Yes |       1 | UTF-32 Unicode                                   |
| utf32_persian_ci               | utf32    |  176 |      | Yes |       8 |                                                  |
| utf32_polish_ci                | utf32    |  165 |      | Yes |       8 |                                                  |
| utf32_romanian_ci              | utf32    |  163 |      | Yes |       8 |                                                  |
| utf32_roman_ci                 | utf32    |  175 |      | Yes |       8 |                                                  |
| utf32_sinhala_ci               | utf32    |  179 |      | Yes |       8 |                                                  |
| utf32_slovak_ci                | utf32    |  173 |      | Yes |       8 |                                                  |
| utf32_slovenian_ci             | utf32    |  164 |      | Yes |       8 |                                                  |
| utf32_spanish2_ci              | utf32    |  174 |      | Yes |       8 |                                                  |
| utf32_spanish_ci               | utf32    |  167 |      | Yes |       8 |                                                  |
| utf32_swedish_ci               | utf32    |  168 |      | Yes |       8 |                                                  |
| utf32_thai_520_w2              | utf32    |  738 |      | Yes |       4 |                                                  |
| utf32_turkish_ci               | utf32    |  169 |      | Yes |       8 |                                                  |
| utf32_unicode_520_ci           | utf32    |  182 |      | Yes |       8 |                                                  |
| utf32_unicode_520_nopad_ci     | utf32    | 1206 |      | Yes |       8 |                                                  |
| utf32_unicode_ci               | utf32    |  160 |      | Yes |       8 |                                                  |
| utf32_unicode_nopad_ci         | utf32    | 1184 |      | Yes |       8 |                                                  |
| utf32_vietnamese_ci            | utf32    |  183 |      | Yes |       8 |                                                  |
| utf8mb3_bin                    | utf8mb3  |   83 |      | Yes |       1 | UTF-8 Unicode                                    |
| utf8mb3_croatian_ci            | utf8mb3  |  576 |      | Yes |       8 |                                                  |
| utf8mb3_croatian_mysql561_ci   | utf8mb3  |  213 |      | Yes |       8 |                                                  |
| utf8mb3_czech_ci               | utf8mb3  |  202 |      | Yes |       8 |                                                  |
| utf8mb3_danish_ci              | utf8mb3  |  203 |      | Yes |       8 |                                                  |
| utf8mb3_esperanto_ci           | utf8mb3  |  209 |      | Yes |       8 |                                                  |
| utf8mb3_estonian_ci            | utf8mb3  |  198 |      | Yes |       8 |                                                  |
| utf8mb3_general_ci             | utf8mb3  |   33 | Yes  | Yes |       1 | UTF-8 Unicode                                    |
| utf8mb3_general_mysql500_ci    | utf8mb3  |  223 |      | Yes |       1 |                                                  |
| utf8mb3_general_nopad_ci       | utf8mb3  | 1057 |      | Yes |       1 |                                                  |
| utf8mb3_german2_ci             | utf8mb3  |  212 |      | Yes |       8 |                                                  |
| utf8mb3_hungarian_ci           | utf8mb3  |  210 |      | Yes |       8 |                                                  |
| utf8mb3_icelandic_ci           | utf8mb3  |  193 |      | Yes |       8 |                                                  |
| utf8mb3_latvian_ci             | utf8mb3  |  194 |      | Yes |       8 |                                                  |
| utf8mb3_lithuanian_ci          | utf8mb3  |  204 |      | Yes |       8 |                                                  |
| utf8mb3_myanmar_ci             | utf8mb3  |  577 |      | Yes |       8 |                                                  |
| utf8mb3_nopad_bin              | utf8mb3  | 1107 |      | Yes |       1 |                                                  |
| utf8mb3_persian_ci             | utf8mb3  |  208 |      | Yes |       8 |                                                  |
| utf8mb3_polish_ci              | utf8mb3  |  197 |      | Yes |       8 |                                                  |
| utf8mb3_romanian_ci            | utf8mb3  |  195 |      | Yes |       8 |                                                  |
| utf8mb3_roman_ci               | utf8mb3  |  207 |      | Yes |       8 |                                                  |
| utf8mb3_sinhala_ci             | utf8mb3  |  211 |      | Yes |       8 |                                                  |
| utf8mb3_slovak_ci              | utf8mb3  |  205 |      | Yes |       8 |                                                  |
| utf8mb3_slovenian_ci           | utf8mb3  |  196 |      | Yes |       8 |                                                  |
| utf8mb3_spanish2_ci            | utf8mb3  |  206 |      | Yes |       8 |                                                  |
| utf8mb3_spanish_ci             | utf8mb3  |  199 |      | Yes |       8 |                                                  |
| utf8mb3_swedish_ci             | utf8mb3  |  200 |      | Yes |       8 |                                                  |
| utf8mb3_thai_520_w2            | utf8mb3  |  578 |      | Yes |       4 |                                                  |
| utf8mb3_turkish_ci             | utf8mb3  |  201 |      | Yes |       8 |                                                  |
| utf8mb3_unicode_520_ci         | utf8mb3  |  214 |      | Yes |       8 |                                                  |
| utf8mb3_unicode_520_nopad_ci   | utf8mb3  | 1238 |      | Yes |       8 |                                                  |
| utf8mb3_unicode_ci             | utf8mb3  |  192 |      | Yes |       8 |                                                  |
| utf8mb3_unicode_nopad_ci       | utf8mb3  | 1216 |      | Yes |       8 |                                                  |
| utf8mb3_vietnamese_ci          | utf8mb3  |  215 |      | Yes |       8 |                                                  |
| utf8mb4_0900_ai_ci             | utf8mb4  |  255 |      | Yes |       8 | Alias for utf8mb4_uca1400_nopad_ai_ci            |
| utf8mb4_0900_as_ci             | utf8mb4  |  305 |      | Yes |       8 | Alias for utf8mb4_uca1400_nopad_as_ci            |
| utf8mb4_0900_as_cs             | utf8mb4  |  278 |      | Yes |       8 | Alias for utf8mb4_uca1400_nopad_as_cs            |
| utf8mb4_0900_bin               | utf8mb4  |  309 |      | Yes |       1 | Alias for utf8mb4_bin                            |
| utf8mb4_bin                    | utf8mb4  |   46 |      | Yes |       1 | UTF-8 Unicode                                    |
| utf8mb4_croatian_ci            | utf8mb4  |  608 |      | Yes |       8 |                                                  |
| utf8mb4_croatian_mysql561_ci   | utf8mb4  |  245 |      | Yes |       8 |                                                  |
| utf8mb4_cs_0900_ai_ci          | utf8mb4  |  266 |      | Yes |       8 | Alias for utf8mb4_uca1400_czech_nopad_ai_ci      |
| utf8mb4_cs_0900_as_cs          | utf8mb4  |  289 |      | Yes |       8 | Alias for utf8mb4_uca1400_czech_nopad_as_cs      |
| utf8mb4_czech_ci               | utf8mb4  |  234 |      | Yes |       8 |                                                  |
| utf8mb4_danish_ci              | utf8mb4  |  235 |      | Yes |       8 |                                                  |
| utf8mb4_da_0900_ai_ci          | utf8mb4  |  267 |      | Yes |       8 | Alias for utf8mb4_uca1400_danish_nopad_ai_ci     |
| utf8mb4_da_0900_as_cs          | utf8mb4  |  290 |      | Yes |       8 | Alias for utf8mb4_uca1400_danish_nopad_as_cs     |
| utf8mb4_de_pb_0900_ai_ci       | utf8mb4  |  256 |      | Yes |       8 | Alias for utf8mb4_uca1400_german2_nopad_ai_ci    |
| utf8mb4_de_pb_0900_as_cs       | utf8mb4  |  279 |      | Yes |       8 | Alias for utf8mb4_uca1400_german2_nopad_as_cs    |
| utf8mb4_eo_0900_ai_ci          | utf8mb4  |  273 |      | Yes |       8 | Alias for utf8mb4_uca1400_esperanto_nopad_ai_ci  |
| utf8mb4_eo_0900_as_cs          | utf8mb4  |  296 |      | Yes |       8 | Alias for utf8mb4_uca1400_esperanto_nopad_as_cs  |
| utf8mb4_esperanto_ci           | utf8mb4  |  241 |      | Yes |       8 |                                                  |
| utf8mb4_estonian_ci            | utf8mb4  |  230 |      | Yes |       8 |                                                  |
| utf8mb4_es_0900_ai_ci          | utf8mb4  |  263 |      | Yes |       8 | Alias for utf8mb4_uca1400_spanish_nopad_ai_ci    |
| utf8mb4_es_0900_as_cs          | utf8mb4  |  286 |      | Yes |       8 | Alias for utf8mb4_uca1400_spanish_nopad_as_cs    |
| utf8mb4_es_trad_0900_ai_ci     | utf8mb4  |  270 |      | Yes |       8 | Alias for utf8mb4_uca1400_spanish2_nopad_ai_ci   |
| utf8mb4_es_trad_0900_as_cs     | utf8mb4  |  293 |      | Yes |       8 | Alias for utf8mb4_uca1400_spanish2_nopad_as_cs   |
| utf8mb4_et_0900_ai_ci          | utf8mb4  |  262 |      | Yes |       8 | Alias for utf8mb4_uca1400_estonian_nopad_ai_ci   |
| utf8mb4_et_0900_as_cs          | utf8mb4  |  285 |      | Yes |       8 | Alias for utf8mb4_uca1400_estonian_nopad_as_cs   |
| utf8mb4_general_ci             | utf8mb4  |   45 | Yes  | Yes |       1 | UTF-8 Unicode                                    |
| utf8mb4_general_nopad_ci       | utf8mb4  | 1069 |      | Yes |       1 | UTF-8 Unicode                                    |
| utf8mb4_german2_ci             | utf8mb4  |  244 |      | Yes |       8 |                                                  |
| utf8mb4_hr_0900_ai_ci          | utf8mb4  |  275 |      | Yes |       8 | Alias for utf8mb4_uca1400_croatian_nopad_ai_ci   |
| utf8mb4_hr_0900_as_cs          | utf8mb4  |  298 |      | Yes |       8 | Alias for utf8mb4_uca1400_croatian_nopad_as_cs   |
| utf8mb4_hungarian_ci           | utf8mb4  |  242 |      | Yes |       8 |                                                  |
| utf8mb4_hu_0900_ai_ci          | utf8mb4  |  274 |      | Yes |       8 | Alias for utf8mb4_uca1400_hungarian_nopad_ai_ci  |
| utf8mb4_hu_0900_as_cs          | utf8mb4  |  297 |      | Yes |       8 | Alias for utf8mb4_uca1400_hungarian_nopad_as_cs  |
| utf8mb4_icelandic_ci           | utf8mb4  |  225 |      | Yes |       8 |                                                  |
| utf8mb4_is_0900_ai_ci          | utf8mb4  |  257 |      | Yes |       8 | Alias for utf8mb4_uca1400_icelandic_nopad_ai_ci  |
| utf8mb4_is_0900_as_cs          | utf8mb4  |  280 |      | Yes |       8 | Alias for utf8mb4_uca1400_icelandic_nopad_as_cs  |
| utf8mb4_latvian_ci             | utf8mb4  |  226 |      | Yes |       8 |                                                  |
| utf8mb4_la_0900_ai_ci          | utf8mb4  |  271 |      | Yes |       8 | Alias for utf8mb4_uca1400_roman_nopad_ai_ci      |
| utf8mb4_la_0900_as_cs          | utf8mb4  |  294 |      | Yes |       8 | Alias for utf8mb4_uca1400_roman_nopad_as_cs      |
| utf8mb4_lithuanian_ci          | utf8mb4  |  236 |      | Yes |       8 |                                                  |
| utf8mb4_lt_0900_ai_ci          | utf8mb4  |  268 |      | Yes |       8 | Alias for utf8mb4_uca1400_lithuanian_nopad_ai_ci |
| utf8mb4_lt_0900_as_cs          | utf8mb4  |  291 |      | Yes |       8 | Alias for utf8mb4_uca1400_lithuanian_nopad_as_cs |
| utf8mb4_lv_0900_ai_ci          | utf8mb4  |  258 |      | Yes |       8 | Alias for utf8mb4_uca1400_latvian_nopad_ai_ci    |
| utf8mb4_lv_0900_as_cs          | utf8mb4  |  281 |      | Yes |       8 | Alias for utf8mb4_uca1400_latvian_nopad_as_cs    |
| utf8mb4_myanmar_ci             | utf8mb4  |  609 |      | Yes |       8 |                                                  |
| utf8mb4_nopad_bin              | utf8mb4  | 1070 |      | Yes |       1 | UTF-8 Unicode                                    |
| utf8mb4_persian_ci             | utf8mb4  |  240 |      | Yes |       8 |                                                  |
| utf8mb4_pl_0900_ai_ci          | utf8mb4  |  261 |      | Yes |       8 | Alias for utf8mb4_uca1400_polish_nopad_ai_ci     |
| utf8mb4_pl_0900_as_cs          | utf8mb4  |  284 |      | Yes |       8 | Alias for utf8mb4_uca1400_polish_nopad_as_cs     |
| utf8mb4_polish_ci              | utf8mb4  |  229 |      | Yes |       8 |                                                  |
| utf8mb4_romanian_ci            | utf8mb4  |  227 |      | Yes |       8 |                                                  |
| utf8mb4_roman_ci               | utf8mb4  |  239 |      | Yes |       8 |                                                  |
| utf8mb4_ro_0900_ai_ci          | utf8mb4  |  259 |      | Yes |       8 | Alias for utf8mb4_uca1400_romanian_nopad_ai_ci   |
| utf8mb4_ro_0900_as_cs          | utf8mb4  |  282 |      | Yes |       8 | Alias for utf8mb4_uca1400_romanian_nopad_as_cs   |
| utf8mb4_sinhala_ci             | utf8mb4  |  243 |      | Yes |       8 |                                                  |
| utf8mb4_sk_0900_ai_ci          | utf8mb4  |  269 |      | Yes |       8 | Alias for utf8mb4_uca1400_slovak_nopad_ai_ci     |
| utf8mb4_sk_0900_as_cs          | utf8mb4  |  292 |      | Yes |       8 | Alias for utf8mb4_uca1400_slovak_nopad_as_cs     |
| utf8mb4_slovak_ci              | utf8mb4  |  237 |      | Yes |       8 |                                                  |
| utf8mb4_slovenian_ci           | utf8mb4  |  228 |      | Yes |       8 |                                                  |
| utf8mb4_sl_0900_ai_ci          | utf8mb4  |  260 |      | Yes |       8 | Alias for utf8mb4_uca1400_slovenian_nopad_ai_ci  |
| utf8mb4_sl_0900_as_cs          | utf8mb4  |  283 |      | Yes |       8 | Alias for utf8mb4_uca1400_slovenian_nopad_as_cs  |
| utf8mb4_spanish2_ci            | utf8mb4  |  238 |      | Yes |       8 |                                                  |
| utf8mb4_spanish_ci             | utf8mb4  |  231 |      | Yes |       8 |                                                  |
| utf8mb4_sv_0900_ai_ci          | utf8mb4  |  264 |      | Yes |       8 | Alias for utf8mb4_uca1400_swedish_nopad_ai_ci    |
| utf8mb4_sv_0900_as_cs          | utf8mb4  |  287 |      | Yes |       8 | Alias for utf8mb4_uca1400_swedish_nopad_as_cs    |
| utf8mb4_swedish_ci             | utf8mb4  |  232 |      | Yes |       8 |                                                  |
| utf8mb4_thai_520_w2            | utf8mb4  |  610 |      | Yes |       4 |                                                  |
| utf8mb4_tr_0900_ai_ci          | utf8mb4  |  265 |      | Yes |       8 | Alias for utf8mb4_uca1400_turkish_nopad_ai_ci    |
| utf8mb4_tr_0900_as_cs          | utf8mb4  |  288 |      | Yes |       8 | Alias for utf8mb4_uca1400_turkish_nopad_as_cs    |
| utf8mb4_turkish_ci             | utf8mb4  |  233 |      | Yes |       8 |                                                  |
| utf8mb4_unicode_520_ci         | utf8mb4  |  246 |      | Yes |       8 |                                                  |
| utf8mb4_unicode_520_nopad_ci   | utf8mb4  | 1270 |      | Yes |       8 |                                                  |
| utf8mb4_unicode_ci             | utf8mb4  |  224 |      | Yes |       8 |                                                  |
| utf8mb4_unicode_nopad_ci       | utf8mb4  | 1248 |      | Yes |       8 |                                                  |
| utf8mb4_vietnamese_ci          | utf8mb4  |  247 |      | Yes |       8 |                                                  |
| utf8mb4_vi_0900_ai_ci          | utf8mb4  |  277 |      | Yes |       8 | Alias for utf8mb4_uca1400_vietnamese_nopad_ai_ci |
| utf8mb4_vi_0900_as_cs          | utf8mb4  |  300 |      | Yes |       8 | Alias for utf8mb4_uca1400_vietnamese_nopad_as_cs |
+--------------------------------+----------+------+------+-----+---------+--------------------------------------------------+
550 rows in set (0.005 sec)
```

:information\_source: The UCA-14.0.0 collations were added in [MariaDB 10.10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/mariadb-10101-release-notes).

:information\_source: Before [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.1), the `utf8mb3*` collations listed above were named `utf8*`.

:information\_source: [MariaDB 11.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.5) added UCA-9.0.0 collations, as well as a Comment column to `information_schema.collations`, to make it clear that the UCA-9.0.0 collations are mapped to the UCA-14.0.0 collations. The UCA-9.0.0 collations have mainly been added to make it easy to replicate from MySQL 8.0 to MariaDB 11.4.5 and newer.

{% hint style="info" %}
Note that some of the collations are used with several different character sets. In this case, the `Charset` and `Id` columns are `NULL`.
{% endhint %}

You can find all combinations of the supported character set and collation in the [information\_schema.COLLATION\_CHARACTER\_SET\_APPLICABILITY](../../../system-tables/information-schema/information-schema-tables/information-schema-collation_character_set_applicability-table.md) table.

## Case Sensitivity

A '`ci`' at the end of a collation name indicates the collation is case-insensitive. A '`cs`' at the end of a\
collation name indicates the collation is case sensitive.

## NO PAD Collations

`NO PAD` collations regard trailing spaces as normal characters. You can get a list of all of these by querying the [Information Schema COLLATIONS Table](../../../system-tables/information-schema/information-schema-tables/information-schema-collations-table.md) as follows:

```sql
SELECT collation_name FROM information_schema.COLLATIONS
WHERE collation_name LIKE "%nopad%";  
+------------------------------+
| collation_name               |
+------------------------------+
| big5_chinese_nopad_ci        |
| big5_nopad_bin               |
...
```

## Accent Insensitivity

An accent insensitive collation is one where the accented and unaccented versions of a letter are considered to be identical for sorting purposes.

:information\_source: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010) added the accent insensitivity flag, and new collations are marked with '\_ai' or '\_as' in the name to indicate this, for example:

```sql
...
| uca1400_spanish2_ai_ci         |
| uca1400_spanish2_ai_cs         |
| uca1400_spanish2_as_ci         |
| uca1400_spanish2_as_cs         |
...
```

## Changes

* [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010) added 184 UCA-14.0.0 collations. Unicode-14.0.0 was released in September 2021. They contain 939 [built-in contractions](https://www.unicode.org/Public/UCA/14.0.0/allkeys.txt). Old collations based on UCA-4.0.0 and UCA-5.2.0 did not support built-in contractions. This is a step towards better Unicode Collation Algorithm compliance. With built-in contractions, some languages (e.g., Thai) won't need specific collations and will just work with the default "root" collation.
* [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.1) changed the `utf8` character set by default to be an alias for utf8mb3 rather than the other way around. It can be set to imply `utf8mb4` by changing the value of the [old\_mode](../../../../server-management/variables-and-modes/old_mode.md) system variable.
* [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes) added 88 `NO PAD` collations.
* [MariaDB 10.1.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10115-release-notes) added the `utf8_thai_520_w2`, `utf8mb4_thai_520_w2`, `ucs2_thai_520_w2`, `utf16_thai_520_w2` and `utf32_thai_520_w2` collations.
* [MariaDB 10.0.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1007-release-notes) added the `utf8_myanmar_ci`, `ucs2_myanmar_ci`, `utf8mb4_myanmar_ci`, `utf16_myanmar_ci` and `utf32_myanmar_ci` collations.
* [MariaDB 10.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes) added the `utf8_german2_ci`, `utf8mb4_german2_ci`, `ucs2_german2_ci`, `utf16_german2_ci` and `utf32_german2_ci` collations.
* [MariaDB 5.1.41](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-1-series/mariadb-5141-release-notes) added a Croatian collation patch from [Alexander Barkov](https://www.collation-charts.org/) to fix some problems with the Croatian character set and `LIKE` queries. This patch added `utf8_croatian_ci` and `ucs2_croatian_ci` collations to MariaDB.

## See Also

* [Information Schema CHARACTER\_SETS Table](../../../system-tables/information-schema/information-schema-tables/information-schema-character_sets-table.md)
* [Information Schema COLLATIONS Table](../../../system-tables/information-schema/information-schema-tables/information-schema-collations-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
