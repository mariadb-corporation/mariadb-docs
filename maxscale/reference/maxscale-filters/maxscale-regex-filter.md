# MaxScale Regex Filter

### Overview

The Regex filter is a filter module for MariaDB MaxScale that is able to rewrite
query content using regular expression matches and text substitution. The
regular expressions use the [PCRE2 syntax](https://www.pcre.org/current/doc/html/pcre2syntax.html).

PCRE2 library uses a different syntax than POSIX to refer to capture
groups in the replacement string. The main difference is the usage of the dollar
character instead of the backslash character for references e.g. `$1` instead of`\1`. For more details about the replacement string differences, please read the [Creating a new string with substitutions](https://www.pcre.org/current/doc/html/pcre2api.html#SEC34)
chapter in the PCRE2 manual.

### Configuration

The following demonstrates a minimal configuration.

```
[MyRegexFilter]
type=filter
module=regexfilter
match=some string
replace=replacement string

[MyService]
type=service
router=readconnroute
servers=server1
user=myuser
password=mypasswd
filters=MyRegexfilter
```

### Settings

The Regex filter has two mandatory parameters: _match_ and _replace_.

#### `match`

* Type: [regex](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: Yes
* Dynamic: Yes

Defines the text in the SQL statements that is replaced.

```
match=TYPE[ ]*=
options=case
```

#### `options`

* Type: [enum](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

The _options_-parameter affects how the patterns are compiled as [usual](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).

#### `replace`

* Type: string
* Mandatory: Yes
* Dynamic: Yes

This is the text that should replace the part of the SQL-query matching the
pattern defined in _match_.

```
replace=ENGINE =
```

#### `source`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

The optional source parameter defines an address that is used to match against
the address from which the client connection to MariaDB MaxScale
originates. Only sessions that originate from this address will have the match
and replacement applied to them.

```
source=127.0.0.1
```

#### `user`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

The optional user parameter defines a username that is used to match against
the user from which the client connection to MariaDB MaxScale originates. Only
sessions that are connected using this username will have the match and
replacement applied to them.

```
user=john
```

#### `log_file`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

The optional log\_file parameter defines a log file in which the filter writes
all queries that are not matched and matching queries with their replacement
queries. All sessions will log to this file so this should only be used for
diagnostic purposes.

```
log_file=/tmp/regexfilter.log
```

#### `log_trace`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

The optional log\_trace parameter toggles the logging of non-matching and
matching queries with their replacements into the log file on the _info_ level.
This is the preferred method of diagnosing the matching of queries since the log
level can be changed at runtime. For more details about logging levels and
session specific logging, please read the [Configuration Guide](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md).

```
log_trace=true
```

### Examples

#### Example 1 - Replace MySQL 5.1 create table syntax with that for later versions

MySQL 5.1 used the parameter TYPE = to set the storage engine that should be
used for a table. In later versions this changed to be ENGINE =. Imagine you
have an application that you cannot change for some reason, but you wish to
migrate to a newer version of MySQL. The regexfilter can be used to transform
the create table statements into the form that could be used by MySQL 5.5

```
[CreateTableFilter]
type=filter
module=regexfilter
options=ignorecase
match=TYPE\s*=
replace=ENGINE=

[MyService]
type=service
router=readconnroute
servers=server1
user=myuser
password=mypasswd
filters=CreateTableFilter
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
