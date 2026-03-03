# Constants

> Constants are declared in mariadb.constants module.

> For using constants of various types, they have to be imported first:
```python
from mariadb.constants import *
```

## CAPABILITY

MariaDB capability flags.

These flags are used to check the capabilities both of a MariaDB server
or the client applicaion.

Capability flags are defined in module *mariadb.constants.CAPABILIY*

*Since version 1.1.4*

```python
import mariadb
from mariadb.constants import *

# connection parameters
conn_params= {
    "user" : "example_user",
    "password" : "GHbe_Su3B8",
    "host" : "localhost"
}

with mariadb.connect(**conn_params) as connection:
    # test if LOAD DATA LOCAL INFILE is supported
    if connection.server_capabilities & CAPABILITY.LOCAL_FILES:
        print("Server supports LOCAL INFILE")
```

*Output*:

```none
Server supports LOCAL INFILE
```

## CLIENT

MariaDB capability flags.

These flags are used to check the capabilities both of a MariaDB server
or the client applicaion.

Capability flags are defined in module *mariadb.constants.CLIENT*

*Since version 1.1.0, deprecated in 1.1.4*

## CURSOR

Cursor constants are used for server side cursors.
Currently only read only cursor is supported.

Cursor constants are defined in module *mariadb.constants.CURSOR*.

*Since version 1.1.0*

#### CURSOR.NONE

This is the default setting (no cursor)

#### CURSOR.READ_ONLY

Will create a server side read only cursor. The cursor is a forward cursor, which
means it is not possible to scroll back.

## ERR (Error)

Using ERR constants instead of error numbers make the code more readable. Error constants
are defined in constants.ERR module

*Since version 1.1.2*

```python
import mariadb
from mariadb.constants import *

# connection parameters
conn_params= {
    "user" : "example_user",
    "password" : "wrong_password",
    "host" : "localhost"
}

# try to establish a connection
try:
    connection= mariadb.connect(**conn_params)
except mariadb.OperationalError as Err:
    if Err.errno == ERR.ER_ACCESS_DENIED_ERROR:
        print("Access denied. Wrong password!")
```

*Output*:

```none
Access denied. Wrong password!
```

## FIELD_FLAG

MariaDB FIELD_FLAG Constants

These constants represent the various field flags. As an addition
to the DBAPI 2.0 standard (PEP-249) these flags are returned as
eighth element of the cursor description attribute.

Field flags are defined in module *mariadb.constants.FIELD_FLAG*

*Since version 1.1.0*

#### FIELD_FLAG.NOT_NULL

column is defined as not NULL

#### FIELD_FLAG.PRIMARY_KEY

column is (part of) a primary key

#### FIELD_FLAG.UNIQUE_KEY

column is (part of) a unique key

#### FIELD_FLAG.MULTIPLE_KEY

column is (part of) a key

#### FIELD_FLAG.BLOB

column contains a binary object

#### FIELD_FLAG.UNSIGNED

numeric column is defined as unsigned

#### FIELD_FLAG.ZEROFILL

column has zerofill attribute

#### FIELD_FLAG.BINARY

column is a binary

#### FIELD_FLAG.ENUM

column is defined as enum

#### FIELD_FLAG.AUTO_INCREMENT

column is an auto_increment column

#### FIELD_FLAG.TIMESTAMP

column is defined as time stamp

#### FIELD_FLAG.SET

column is defined as SET

#### FIELD_FLAG.NO_DEFAULT

column hasn’t a default value

#### FIELD_FLAG.ON_UPDATE_NOW

column will be set to current timestamp on UPDATE

#### FIELD_FLAG.NUMERIC

column contains numeric value

#### FIELD_FLAG.PART_OF_KEY

column is part of a key

## FIELD_TYPE

MariaDB FIELD_TYPE Constants

These constants represent the field types supported by MariaDB.
The field type is returned as second element of cursor description attribute.

Field types are defined in module *mariadb.constants.FIELD_TYPE*

#### FIELD_TYPE.TINY

column type is TINYINT  (1-byte integer)

#### FIELD_TYPE.SHORT

column type is SMALLINT (2-byte integer)

#### FIELD_TYPE.LONG

column tyoe is INT (4-byte integer)

#### FIELD_TYPE.FLOAT

column type is FLOAT (4-byte single precision)

#### FIELD_TYPE.DOUBLE

column type is DOUBLE (8-byte double precision)

#### FIELD_TYPE.NULL

column type is NULL

#### FIELD_TYPE.TIMESTAMP

column tyoe is TIMESTAMP

#### FIELD_TYPE.LONGLONG

column tyoe is BIGINT (8-byte Integer)

#### FIELD_TYPE.INT24

column type is MEDIUMINT (3-byte Integer)

#### FIELD_TYPE.DATE

column type is DATE

#### FIELD_TYPE.TIME

column type is TIME

#### FIELD_TYPE.DATETIME

column type is DATETIME

#### FIELD_TYPE.YEAR

column type is YEAR

#### FIELD_TYPE.VARCHAR

column type is VARCHAR

#### FIELD_TYPE.BIT

column type is BIT

#### FIELD_TYPE.JSON

column type is JSON

#### FIELD_TYPE.NEWDECIMAL

column type is DECIMAL

#### FIELD_TYPE.ENUM

column type is ENUM

#### FIELD_TYPE.SET

column type is SET

#### FIELD_TYPE.TINY_BLOB

column type is TINYBLOB (max. length of 255 bytes)

#### FIELD_TYPE.MEDIUM_BLOB

column type is MEDIUMBLOB (max. length of 16,777,215 bytes)

#### FIELD_TYPE.LONG_BLOB

column type is LONGBLOB (max. length 4GB bytes)

#### FIELD_TYPE.BLOB

column type is BLOB (max. length of 65.535 bytes)

#### FIELD_TYPE.VAR_STRING

column type is VARCHAR (variable length)

#### FIELD_TYPE.STRING

column type is CHAR (fixed length)

#### FIELD_TYPE.GEOMETRY

column type is GEOMETRY

## INDICATORS

Indicator values are used in executemany() method of cursor class to
indicate special values when connected to a MariaDB server 10.2 or newer.

#### INDICATOR.NULL

indicates a NULL value

#### INDICATOR.DEFAULT

indicates to use default value of column

#### INDICATOR.IGNORE

indicates to ignore value for column for UPDATE statements.
If set, the column will not be updated.

#### INDICATOR.IGNORE_ROW

indicates not to update the entire row.

## INFO

For internal use only

## TPC_STATE

For internal use only

## STATUS

The STATUS constants are used to check the server status of the current connection.

*Since version 1.1.0*

> Example:

> ```python
> cursor.callproc("my_storedprocedure", (1,"foo"))

> if (connection.server_status & STATUS.SP_OUT_PARAMS):
>     print("retrieving output parameters from store procedure")
>     ...
> else:
>     print("retrieving data from stored procedure")
>     ....
> ```

#### STATUS.IN_TRANS

Pending transaction

#### STATUS.AUTOCOMMIT

Server operates in autocommit mode

#### STATUS.MORE_RESULTS_EXIST

The result from last executed statement contained two or more result
sets which can be retrieved by cursors nextset() method.

#### STATUS.QUERY_NO_GOOD_INDEX_USED

The last executed statement didn’t use a good index.

#### STATUS.QUERY_NO_INDEX_USED

The last executed statement didn’t use an index.

#### STATUS.CURSOR_EXISTS

The last executed statement opened a server side cursor.

#### STATUS.LAST_ROW_SENT

For server side cursors this flag indicates end of a result set.

#### STATUS.DB_DROPPED

The current database in use was dropped and there is no default
database for the connection anymore.

#### STATUS.NO_BACKSLASH_ESCAPES

Indicates that SQL mode NO_BACKSLASH_ESCAPE is active, which means
that the backslash character ‘' becomes an ordinary character.

#### STATUS.QUERY_WAS_SLOW

The previously executed statement was slow (and needs to be optimized).

#### STATUS.PS_OUT_PARAMS

The current result set contains output parameters of a stored procedure.

#### STATUS.SESSION_STATE_CHANGED

The session status has been changed.

#### STATUS.ANSI_QUOTES

SQL mode ANSI_QUOTES is active.

#### STATUS.METADATA_CHANGED

Metadata has changed (e.g., table structure modified).

#### STATUS.IN_TRANS_READONLY

Pending read-only transaction.

## EXT_FIELD_TYPE

MariaDB Extended FIELD_TYPE Constants

These constants represent the extended field types supported by MariaDB.
Extended field types provide additional type information beyond standard SQL types.

Extended field types are defined in module *mariadb.constants.EXT_FIELD_TYPE*

*Since version 2.0*

#### EXT_FIELD_TYPE.NONE

No extended type information (value: 0)

#### EXT_FIELD_TYPE.JSON

JSON data type (value: 1)

#### EXT_FIELD_TYPE.UUID

UUID data type (value: 2)

#### EXT_FIELD_TYPE.INET4

IPv4 address data type (value: 3)

#### EXT_FIELD_TYPE.INET6

IPv6 address data type (value: 4)

#### EXT_FIELD_TYPE.POINT

Geometry POINT type (value: 5)

#### EXT_FIELD_TYPE.MULTIPOINT

Geometry MULTIPOINT type (value: 6)

#### EXT_FIELD_TYPE.LINESTRING

Geometry LINESTRING type (value: 7)

#### EXT_FIELD_TYPE.MULTILINESTRING

Geometry MULTILINESTRING type (value: 8)

#### EXT_FIELD_TYPE.POLYGON

Geometry POLYGON type (value: 9)

#### EXT_FIELD_TYPE.MULTIPOLYGON

Geometry MULTIPOLYGON type (value: 10)

#### EXT_FIELD_TYPE.GEOMETRYCOLLECTION

Geometry GEOMETRYCOLLECTION type (value: 11)

**Example:**

```python
import mariadb
from mariadb.constants import EXT_FIELD_TYPE

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

cursor.execute("SELECT id, data, location FROM test_table")
metadata = cursor.metadata

if metadata:
    for i, ext_type in enumerate(metadata['ext_type_or_format']):
        if ext_type == EXT_FIELD_TYPE.JSON:
            print(f"Column {i} is JSON type")
        elif ext_type == EXT_FIELD_TYPE.UUID:
            print(f"Column {i} is UUID type")
        elif ext_type == EXT_FIELD_TYPE.POINT:
            print(f"Column {i} is POINT geometry type")

cursor.close()
conn.close()
```

## SESSION_TRACK

Session tracking constants for monitoring session state changes.

Session tracking constants are defined in module *mariadb.constants.SESSION_TRACK*

*Since version 2.0*

{% @marketo/form formId="4316" %}
