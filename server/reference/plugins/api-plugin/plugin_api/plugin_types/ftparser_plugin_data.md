---
description: >-
  Plugin API reference: Full-Text Parser Plugin. Generated from the MariaDB
  server headers by doxygen and moxygen.
---

# Full-Text Parser Plugin

> [`Plugin API`](../) / [`Plugin Types`](./)

API for Full-text parser plugin. ([MYSQL\_FTPARSER\_PLUGIN](./#mysql_ftparser_plugin))

## Classes

| Name                                                                                       | Description                                 |
| ------------------------------------------------------------------------------------------ | ------------------------------------------- |
| [`st_mysql_ftparser_boolean_info`](ftparser_plugin_data.md#st_mysql_ftparser_boolean_info) | Structure for boolean mode search.          |
| [`st_mysql_ftparser_param`](ftparser_plugin_data.md#st_mysql_ftparser_param)               | An argument of the full-text parser plugin. |
| [`st_mysql_ftparser`](ftparser_plugin_data.md#st_mysql_ftparser)                           |                                             |

## Macros

| Name                                                                                           | Description        |
| ---------------------------------------------------------------------------------------------- | ------------------ |
| [`MYSQL_FTPARSER_INTERFACE_VERSION`](ftparser_plugin_data.md#mysql_ftparser_interface_version) |                    |
| [`MYSQL_FTFLAGS_NEED_COPY`](ftparser_plugin_data.md#mysql_ftflags_need_copy)                   | Needs a copy flag. |

***

### MYSQL\_FTPARSER\_INTERFACE\_VERSION

```cpp
#define MYSQL_FTPARSER_INTERFACE_VERSION 0x0100
```

Defined in plugin\_ftparser.h:31

***

### MYSQL\_FTFLAGS\_NEED\_COPY

```cpp
#define MYSQL_FTFLAGS_NEED_COPY 1
```

Defined in plugin\_ftparser.h:159

Needs a copy flag.

The following flag means that buffer with a string (document, word) may be overwritten by the caller before the end of the parsing (that is before [st\_mysql\_ftparser::deinit()](ftparser_plugin_data.md#deinit) call). If one needs the string to survive between two successive calls of the parsing function, she needs to save a copy of it. The flag may be set by MySQL before calling [st\_mysql\_ftparser::parse()](ftparser_plugin_data.md#parse), or it may be set by a plugin before calling [st\_mysql\_ftparser\_param::mysql\_parse()](ftparser_plugin_data.md#mysql_parse) or [st\_mysql\_ftparser\_param::mysql\_add\_word()](ftparser_plugin_data.md#mysql_add_word).

## Enumerations

| Name                                                               | Description                                                                        |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| [`enum_ftparser_mode`](ftparser_plugin_data.md#enum_ftparser_mode) | Parsing modes. Set in [MYSQL\_FTPARSER\_PARAM::mode](ftparser_plugin_data.md#mode) |
| [`enum_ft_token_type`](ftparser_plugin_data.md#enum_ft_token_type) | Token types for boolean mode searching                                             |

***

### enum\_ftparser\_mode

```cpp
enum enum_ftparser_mode
```

Defined in plugin\_ftparser.h:34

Parsing modes. Set in [MYSQL\_FTPARSER\_PARAM::mode](ftparser_plugin_data.md#mode)

| Value                              | Description                |
| ---------------------------------- | -------------------------- |
| `MYSQL_FTPARSER_SIMPLE_MODE`       | Fast and simple mode.      |
| `MYSQL_FTPARSER_WITH_STOPWORDS`    | Parse with stopwords mode. |
| `MYSQL_FTPARSER_FULL_BOOLEAN_INFO` | Parse in boolean mode.     |

***

### enum\_ft\_token\_type

```cpp
enum enum_ft_token_type
```

Defined in plugin\_ftparser.h:82

Token types for boolean mode searching

Used for the type member of MYSQL\_FTPARSER\_BOOLEAN\_INFO struct.

| Value                  | Description                                       |
| ---------------------- | ------------------------------------------------- |
| `FT_TOKEN_EOF`         | End of data.                                      |
| `FT_TOKEN_WORD`        | Regular word.                                     |
| `FT_TOKEN_LEFT_PAREN`  | Left parenthesis (start of group/sub-expression). |
| `FT_TOKEN_RIGHT_PAREN` | Right parenthesis (end of group/sub-expression).  |
| `FT_TOKEN_STOPWORD`    | Stopword.                                         |

## Typedefs

| Return                                                                                            | Name                                                                                 | Description                                 |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------- |
| struct [`st_mysql_ftparser_boolean_info`](ftparser_plugin_data.md#st_mysql_ftparser_boolean_info) | [`MYSQL_FTPARSER_BOOLEAN_INFO`](ftparser_plugin_data.md#mysql_ftparser_boolean_info) | Structure for boolean mode search.          |
| struct [`st_mysql_ftparser_param`](ftparser_plugin_data.md#st_mysql_ftparser_param)               | [`MYSQL_FTPARSER_PARAM`](ftparser_plugin_data.md#mysql_ftparser_param)               | An argument of the full-text parser plugin. |

***

### MYSQL\_FTPARSER\_BOOLEAN\_INFO

```cpp
using MYSQL_FTPARSER_BOOLEAN_INFO = struct st_mysql_ftparser_boolean_info
```

Type: struct [`st_mysql_ftparser_boolean_info`](ftparser_plugin_data.md#st_mysql_ftparser_boolean_info)

Defined in plugin\_ftparser.h:145

Structure for boolean mode search.

This structure is used in boolean search mode only. It conveys boolean-mode metadata to the MySQL search engine for every word in the search query. A valid instance of this structure must be filled in by the plugin parser and passed as an argument in the call to mysql\_add\_word (the callback function in the MYSQL\_FTPARSER\_PARAM structure) when a query is parsed in boolean mode.

***

### MYSQL\_FTPARSER\_PARAM

```cpp
using MYSQL_FTPARSER_PARAM = struct st_mysql_ftparser_param
```

Type: struct [`st_mysql_ftparser_param`](ftparser_plugin_data.md#st_mysql_ftparser_param)

Defined in plugin\_ftparser.h:231

An argument of the full-text parser plugin.

This structure is filled in by MySQL server and passed to the parsing function of the plugin as an in/out parameter.

## Class Definitions

### st\_mysql\_ftparser\_boolean\_info

```cpp
#include <plugin_ftparser.h>
```

```cpp
struct st_mysql_ftparser_boolean_info
```

Defined in plugin\_ftparser.h:102

Structure for boolean mode search.

This structure is used in boolean search mode only. It conveys boolean-mode metadata to the MySQL search engine for every word in the search query. A valid instance of this structure must be filled in by the plugin parser and passed as an argument in the call to mysql\_add\_word (the callback function in the MYSQL\_FTPARSER\_PARAM structure) when a query is parsed in boolean mode.

#### Public Attributes

| Return                                                                  | Name                                                     | Description                                                                                        |
| ----------------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| enum [`enum_ft_token_type`](ftparser_plugin_data.md#enum_ft_token_type) | [`type`](ftparser_plugin_data.md#type)                   | The token type. Should be one of the enum\_ft\_token\_type values.                                 |
| `int`                                                                   | [`yesno`](ftparser_plugin_data.md#yesno)                 | Whether the word must be present for a match to occur                                              |
| `int`                                                                   | [`weight_adjust`](ftparser_plugin_data.md#weight_adjust) | A weighting factor that determines how much a match for the word counts.                           |
| `char`                                                                  | [`wasign`](ftparser_plugin_data.md#wasign)               | The sign of the word's weight in the query.                                                        |
| `char`                                                                  | [`trunc`](ftparser_plugin_data.md#trunc)                 | Corresponds to the `*` operator in the default setting of the `ft_boolean_syntax` system variable. |
| `char`                                                                  | [`prev`](ftparser_plugin_data.md#prev)                   | Parser state. Must be removed.                                                                     |
| `char *`                                                                | [`quot`](ftparser_plugin_data.md#quot)                   | Parser state. Must be removed.                                                                     |

***

#### type

```cpp
enum enum_ft_token_type type
```

Type: enum [`enum_ft_token_type`](ftparser_plugin_data.md#enum_ft_token_type)

Defined in plugin\_ftparser.h:105

The token type. Should be one of the enum\_ft\_token\_type values.

***

#### yesno

```cpp
int yesno
```

Defined in plugin\_ftparser.h:117

Whether the word must be present for a match to occur

* `>0` Must be present
* `<0` Must not be present
* `0` Neither; the word is optional but its presence increases the relevance

With the default settings of the `ft_boolean_syntax` system variable, `>0` corresponds to the '+' operator, `<0` corresponds to the '-' operator, and `0` means neither operator was used.

***

#### weight\_adjust

```cpp
int weight_adjust
```

Defined in plugin\_ftparser.h:125

A weighting factor that determines how much a match for the word counts.

Positive values increase, negative - decrease the relative word's importance in the query.

***

#### wasign

```cpp
char wasign
```

Defined in plugin\_ftparser.h:135

The sign of the word's weight in the query.

If it's non-negative the match for the word will increase document relevance, if it's negative - decrease (the word becomes a "noise word", the less of it the better).

***

#### trunc

```cpp
char trunc
```

Defined in plugin\_ftparser.h:140

Corresponds to the `*` operator in the default setting of the `ft_boolean_syntax` system variable.

***

#### prev

```cpp
char prev
```

Defined in plugin\_ftparser.h:142

Parser state. Must be removed.

***

#### quot

```cpp
char * quot
```

Defined in plugin\_ftparser.h:144

Parser state. Must be removed.

### st\_mysql\_ftparser\_param

```cpp
#include <plugin_ftparser.h>
```

```cpp
struct st_mysql_ftparser_param
```

Defined in plugin\_ftparser.h:167

An argument of the full-text parser plugin.

This structure is filled in by MySQL server and passed to the parsing function of the plugin as an in/out parameter.

#### Public Attributes

| Return                                                                  | Name                                                       | Description                                                                                                                                             |
| ----------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `int(*`                                                                 | [`mysql_parse`](ftparser_plugin_data.md#mysql_parse)       | A pointer to the built-in parser implementation of the server.                                                                                          |
| `int(*`                                                                 | [`mysql_add_word`](ftparser_plugin_data.md#mysql_add_word) | A server callback to add a new word.                                                                                                                    |
| `void *`                                                                | [`ftparser_state`](ftparser_plugin_data.md#ftparser_state) | A generic pointer.                                                                                                                                      |
| `void *`                                                                | [`mysql_ftparam`](ftparser_plugin_data.md#mysql_ftparam)   | This is set by the server.                                                                                                                              |
| `const struct charset_info_st *`                                        | [`cs`](ftparser_plugin_data.md#cs)                         | Information about the character set of the document or query string.                                                                                    |
| `const char *`                                                          | [`doc`](ftparser_plugin_data.md#doc)                       | A pointer to the document or query string to be parsed.                                                                                                 |
| `int`                                                                   | [`length`](ftparser_plugin_data.md#length)                 | Length of the document or query string, in bytes.                                                                                                       |
| `unsigned int`                                                          | [`flags`](ftparser_plugin_data.md#flags)                   | Flags for the parser. **See also**: [MYSQL\_FTFLAGS\_NEED\_COPY](ftparser_plugin_data.md#mysql_ftflags_need_copy)                                       |
| enum [`enum_ftparser_mode`](ftparser_plugin_data.md#enum_ftparser_mode) | [`mode`](ftparser_plugin_data.md#mode)                     | The parsing mode. With boolean operators, with stopwords, or nothing. **See also**: [enum\_ftparser\_mode](ftparser_plugin_data.md#enum_ftparser_mode). |

***

#### mysql\_parse

```cpp
int(* mysql_parse)(struct st_mysql_ftparser_param *, const char *doc, int doc_len)
```

Defined in plugin\_ftparser.h:179

A pointer to the built-in parser implementation of the server.

It's set by the server and can be used by the parser plugin to invoke the MySQL default parser. If plugin's role is to extract textual data from .doc, .pdf or .xml content, it might extract plaintext from the content, and then pass the text to the default MySQL parser to be parsed.

***

#### mysql\_add\_word

```cpp
int(* mysql_add_word)(struct st_mysql_ftparser_param *, const char *word, int word_len, MYSQL_FTPARSER_BOOLEAN_INFO *boolean_info)
```

Defined in plugin\_ftparser.h:192

A server callback to add a new word.

When parsing a document, the server sets this to point at a function that adds the word to MySQL full-text index. When parsing a search query, this function will add the new word to the list of words to search for. The boolean\_info argument can be NULL for all cases except when mode is MYSQL\_FTPARSER\_FULL\_BOOLEAN\_INFO. A plugin can replace this callback to post-process every parsed word before passing it to the original add\_word function.

***

#### ftparser\_state

```cpp
void * ftparser_state
```

Defined in plugin\_ftparser.h:201

A generic pointer.

The plugin can set it to point to information to be used internally for its own purposes.

***

#### mysql\_ftparam

```cpp
void * mysql_ftparam
```

Defined in plugin\_ftparser.h:209

This is set by the server.

It is used by MySQL functions called via [mysql\_parse()](ftparser_plugin_data.md#mysql_parse) and [mysql\_add\_word()](ftparser_plugin_data.md#mysql_add_word) callback. The plugin should not modify it.

***

#### cs

```cpp
const struct charset_info_st * cs
```

Defined in plugin\_ftparser.h:213

Information about the character set of the document or query string.

***

#### doc

```cpp
const char * doc
```

Defined in plugin\_ftparser.h:217

A pointer to the document or query string to be parsed.

***

#### length

```cpp
int length
```

Defined in plugin\_ftparser.h:221

Length of the document or query string, in bytes.

***

#### flags

```cpp
unsigned int flags
```

Defined in plugin\_ftparser.h:225

Flags for the parser. **See also**: [MYSQL\_FTFLAGS\_NEED\_COPY](ftparser_plugin_data.md#mysql_ftflags_need_copy)

***

#### mode

```cpp
enum enum_ftparser_mode mode
```

Type: enum [`enum_ftparser_mode`](ftparser_plugin_data.md#enum_ftparser_mode)

Defined in plugin\_ftparser.h:230

The parsing mode. With boolean operators, with stopwords, or nothing. **See also**: [enum\_ftparser\_mode](ftparser_plugin_data.md#enum_ftparser_mode).

### st\_mysql\_ftparser

```cpp
#include <plugin_ftparser.h>
```

```cpp
struct st_mysql_ftparser
```

Defined in plugin\_ftparser.h:241

#### Public Attributes

| Return  | Name                                                             | Description |
| ------- | ---------------------------------------------------------------- | ----------- |
| `int`   | [`interface_version`](ftparser_plugin_data.md#interface_version) |             |
| `int(*` | [`parse`](ftparser_plugin_data.md#parse)                         |             |
| `int(*` | [`init`](ftparser_plugin_data.md#init)                           |             |
| `int(*` | [`deinit`](ftparser_plugin_data.md#deinit)                       |             |

***

#### interface\_version

```cpp
int interface_version
```

Defined in plugin\_ftparser.h:243

***

#### parse

```cpp
int(* parse)(MYSQL_FTPARSER_PARAM *param)
```

Defined in plugin\_ftparser.h:244

***

#### init

```cpp
int(* init)(MYSQL_FTPARSER_PARAM *param)
```

Defined in plugin\_ftparser.h:245

***

#### deinit

```cpp
int(* deinit)(MYSQL_FTPARSER_PARAM *param)
```

Defined in plugin\_ftparser.h:246
