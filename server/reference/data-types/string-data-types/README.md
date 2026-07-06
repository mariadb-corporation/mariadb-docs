---
description: >-
  Store text and binary data. This section covers character types like CHAR,
  VARCHAR, and TEXT, as well as binary types like BLOB and BINARY.
---

# String Data Types

{% columns %}
{% column %}
{% content-ref url="blob-and-text-data-types.md" %}
[blob-and-text-data-types.md](blob-and-text-data-types.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of large object types. This page compares BLOB (binary) and TEXT (character) types, explaining their storage and usage differences.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binary.md" %}
[binary.md](binary.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Fixed-length binary string type. This type stores a fixed number of bytes, padding with zero bytes if the data is shorter.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="blob.md" %}
[blob.md](blob.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Variable-length binary large object. BLOB columns can store binary data up to 65,535 bytes, suitable for images or other non-text files.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="char.md" %}
[char.md](char.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Fixed-length character string type. CHAR columns store strings of a specified length (0 to 255), padding with spaces if necessary.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="character.md" %}
[character.md](character.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Fixed-length character string type. CHARACTER columns store strings of a specified length (0 to 255), padding with spaces if necessary.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="char-byte.md" %}
[char-byte.md](char-byte.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Fixed-length binary string type. This type stores a fixed number of bytes, padding with zero bytes if the data is shorter.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="char-varying.md" %}
[char-varying.md](char-varying.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
CHAR VARYING is a synonym for the VARCHAR string data type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="clob.md" %}
[clob.md](clob.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
In Oracle mode, CLOB is an alias for the LONGTEXT data type used to store large text objects.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="enum.md" %}
[enum.md](enum.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete ENUM type reference: ENUM('v1','v2') syntax, CHARACTER SET/COLLATE options, NULL/empty string defaults, and numeric index sorting guidelines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="inet4.md" %}
[inet4.md](inet4.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
IPv4 address data type. Stores IPv4 addresses as 4-byte binary strings for efficient storage and retrieval.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="inet6.md" %}
[inet6.md](inet6.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
IPv6 address data type. Stores IPv6 addresses as 16-byte binary strings, also supporting IPv4 addresses via mapping.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="json.md" %}
[json.md](json.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete JSON Data Type data type guide for MariaDB. Complete reference for syntax, valid values, storage requirements, and range limits for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="long-and-long-varchar.md" %}
[long-and-long-varchar.md](long-and-long-varchar.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
LONG and LONG VARCHAR are compatibility synonyms for the MEDIUMTEXT string data type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="long-char-varying.md" %}
[long-char-varying.md](long-char-varying.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
LONG CHAR VARYING is a compatibility synonym for the MEDIUMTEXT string data type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="long-character-varying.md" %}
[long-character-varying.md](long-character-varying.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
LONG CHARACTER VARYING is a compatibility synonym for the MEDIUMTEXT string data type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="long-varbinary.md" %}
[long-varbinary.md](long-varbinary.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
LONG VARBINARY is a compatibility synonym for the MEDIUMBLOB binary data type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="long-varchar.md" %}
[long-varchar.md](long-varchar.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
LONG VARCHAR is a compatibility synonym for the MEDIUMTEXT string data type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="long-varcharacter.md" %}
[long-varcharacter.md](long-varcharacter.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
LONG VARCHARACTER is a compatibility synonym for the MEDIUMTEXT string data type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="longblob.md" %}
[longblob.md](longblob.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Very large binary object. A LONGBLOB column can store up to 4GB of binary data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="longtext.md" %}
[longtext.md](longtext.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete LONGTEXT type reference: 4GB (2^32-1) storage limit, CHARACTER SET/COLLATE syntax, max_allowed_packet constraints, and JSON/CLOB aliases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mediumblob.md" %}
[mediumblob.md](mediumblob.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Medium-sized binary object. A MEDIUMBLOB column can store up to 16MB of binary data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mediumtext.md" %}
[mediumtext.md](mediumtext.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Medium-sized character string. A MEDIUMTEXT column can store up to 16MB of text data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="national-char.md" %}
[national-char.md](national-char.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NATIONAL CHAR is a synonym for the CHAR data type that uses the predefined utf8mb3 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="national-char-varying.md" %}
[national-char-varying.md](national-char-varying.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NATIONAL CHAR VARYING is a synonym for VARCHAR that uses the predefined utf8 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="national-character-varying.md" %}
[national-character-varying.md](national-character-varying.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NATIONAL CHARACTER VARYING is a synonym for VARCHAR using the predefined utf8 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="national-character.md" %}
[national-character.md](national-character.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NATIONAL CHARACTER is a synonym for the CHAR data type using the predefined utf8 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="national-varchar.md" %}
[national-varchar.md](national-varchar.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NATIONAL VARCHAR is a synonym for the VARCHAR data type using the predefined utf8 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="national-varcharacter.md" %}
[national-varcharacter.md](national-varcharacter.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NATIONAL VARCHARACTER is a synonym for VARCHAR using the predefined utf8 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="nchar.md" %}
[nchar.md](nchar.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NCHAR is a synonym for the fixed-length CHAR string data type using the utf8mb3 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="nchar-varchar.md" %}
[nchar-varchar.md](nchar-varchar.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NCHAR VARCHAR is a synonym for the VARCHAR string data type using the utf8 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="nchar-varcharacter.md" %}
[nchar-varcharacter.md](nchar-varcharacter.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NCHAR VARCHARACTER is a synonym for VARCHAR using the utf8 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="nchar-varying.md" %}
[nchar-varying.md](nchar-varying.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
NCHAR VARYING is a synonym for the VARCHAR string data type using the utf8 character set.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="raw.md" %}
[raw.md](raw.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
In Oracle mode, RAW is a variable-length binary data type synonymous with VARBINARY.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="row.md" %}
[row.md](row.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
ROW is a data type used in stored programs to store a complete row of data from a cursor or table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="set-data-type.md" %}
[set-data-type.md](set-data-type.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
String object with zero or more values from a predefined list. A SET column can store multiple values selected from a list of permitted strings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="text.md" %}
[text.md](text.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete TEXT type reference: TEXT(M) syntax, 65,535 byte maximum, 2-byte length prefix, DEFAULT value support, and indexing constraints rules.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tinyblob.md" %}
[tinyblob.md](tinyblob.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Very small binary object. A TINYBLOB column can store up to 255 bytes of binary data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tinytext.md" %}
[tinytext.md](tinytext.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Very small character string. A TINYTEXT column can store up to 255 characters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="uuid-data-type.md" %}
[uuid-data-type.md](uuid-data-type.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Official UUID data type reference: 128-bit storage optimization, CAST from CHAR/VARCHAR/BINARY types, RFC4122 string format, and UUIDv6/v7 support.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="varbinary.md" %}
[varbinary.md](varbinary.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Variable-length binary string type. VARBINARY columns store binary strings of variable length up to a specified maximum.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="varchar.md" %}
[varchar.md](varchar.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete VARCHAR reference: VARCHAR(M) syntax, length limits (0-65532 per row), CHARACTER SET/COLLATE options, indexing rules, and trailing spaces.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="varchar2.md" %}
[varchar2.md](varchar2.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Variable-length character string type. VARCHAR2 columns store strings of variable length up to a specified maximum (up to 65,535).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="varcharacter.md" %}
[varcharacter.md](varcharacter.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Variable-length character string type. VARCHARACTER columns store strings of variable length up to a specified maximum (up to 65,535).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="xmltype.md" %}
[xmltype.md](xmltype.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The XMLTYPE data type, available from MariaDB 12.3, for storing XML data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="character-sets/" %}
[character-sets](character-sets/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about character sets in MariaDB Server. This section details how different character sets and collations impact string storage, comparison, and sorting within your database.
{% endcolumn %}
{% endcolumns %}
