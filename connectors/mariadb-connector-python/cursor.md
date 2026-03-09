# The cursor class



MariaDB Connector/Python Cursor Object

## Cursor Parameters

Cursors are created using the `connection.cursor()` method and accept the following optional parameters:

### Result Format Parameters

- **`buffered`** (`bool`) - Buffer all results immediately in memory. When `True` (default), all rows are fetched and stored in memory. When `False`, results are streamed from the server, reducing memory usage for large result sets. Default: `True`

- **`named_tuple`** (`bool`) - Return rows as named tuples instead of regular tuples. Allows accessing columns by name (e.g., `row.column_name`). Default: `False`

- **`dictionary`** (`bool`) - Return rows as dictionaries instead of tuples. Allows accessing columns by name (e.g., `row['column_name']`). Default: `False`

- **`native_object`** (`bool`) - Return native Python objects for certain database types. Default: `False`

### Protocol Parameters

- **`binary`** (`bool`) - Use binary protocol (prepared statements) for this cursor. Overrides the connection-level `binary` setting. When `True`, uses COM_STMT_PREPARE + COM_STMT_EXECUTE for better performance with repeated queries. Default: Inherits from connection

### Cursor Examples

**Basic cursor:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()
cursor.execute("SELECT id, name FROM users")
for row in cursor:
    print(f"ID: {row[0]}, Name: {row[1]}")
cursor.close()
conn.close()
```

**Unbuffered cursor for large result sets:**

```python
# Stream results to reduce memory usage
cursor = conn.cursor(buffered=False)
cursor.execute("SELECT * FROM large_table")
for row in cursor:
    process_row(row)  # Process one row at a time
cursor.close()
```

**Dictionary cursor:**

```python
# Access columns by name
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (123,))
user = cursor.fetchone()
print(f"Name: {user['name']}, Email: {user['email']}")
cursor.close()
```

**Named tuple cursor:**

```python
# Access columns as attributes
cursor = conn.cursor(named_tuple=True)
cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (123,))
user = cursor.fetchone()
print(f"Name: {user.name}, Email: {user.email}")
cursor.close()
```

**Binary protocol cursor:**

```python
# Use prepared statements for this cursor
cursor = conn.cursor(binary=True)
# First execution prepares the statement
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
# Subsequent executions reuse the prepared statement
cursor.execute("SELECT * FROM users WHERE id = ?", (2,))
cursor.close()
```

**Combined parameters:**

```python
# Dictionary cursor with streaming results
cursor = conn.cursor(dictionary=True, buffered=False)
cursor.execute("SELECT * FROM large_table")
for row in cursor:
    print(f"Processing: {row['name']}")
cursor.close()
```

## Cursor methods

#### Cursor.callproc(sp: str, data: Sequence[Any] = ()) -> None

Executes a stored procedure sp. The data sequence must contain an
entry for each parameter the procedure expects.

Input/Output or Output parameters have to be retrieved by .fetch
methods, the .sp_outparams attribute indicates if the result set
contains output parameters.

Arguments:
: - sp: Name of stored procedure.
  - data: Optional sequence containing data for placeholder
    : substitution.

Example:

```python
>>>cursor.execute("CREATE PROCEDURE p1(IN i1 VAR  CHAR(20), OUT o2 VARCHAR(40))"
                  "BEGIN"
                  "  SELECT 'hello'"
                  "  o2:= 'test'"
                  "END")
>>>cursor.callproc('p1', ('foo', 0))
>>> cursor.sp_outparams
False
>>> cursor.fetchone()
('hello',)
>>> cursor.nextset()
True
>>> cursor.sp_outparams
True
>>> cursor.fetchone()
('test',)
```

#### Cursor.execute(sql: str, data: Optional[Union[Sequence[Any], dict]] = None, buffered: Optional[bool] = None) -> None

Prepare and execute a SQL statement.

Parameters may be provided as sequence or mapping and will be bound
to variables in the operation. Variables are specified as question
marks (paramstyle ='qmark'), however for compatibility reasons MariaDB
Connector/Python also supports the 'format' and 'pyformat' paramstyles
with the restriction, that different paramstyles can't be mixed within
a statement.

A reference to the operation will be retained by the cursor.

*Since version 2.0:* If the cursor was created with `binary=True`, the statement
uses the MariaDB binary protocol (prepared statements). With prepared statement
caching enabled (default), the first execution prepares the statement and subsequent
executions reuse the cached prepared statement for better performance.

By default execute() method generates a buffered result unless the
optional parameter buffered was set to False or the cursor was
generated as an unbuffered cursor.

**Protocol Selection (Version 2.0):**
- **Text protocol (default)**: Standard SQL execution, predictable behavior
- **Binary protocol** (`binary=True`): Uses COM_STMT_PREPARE + COM_STMT_EXECUTE
- **Dict parameters**: Always use text protocol for named parameter substitution

#### Cursor.executemany(sql: str, data: Sequence[Union[Sequence[Any], dict]], buffered: Optional[bool] = None) -> None

Prepare a database operation (INSERT,UPDATE,REPLACE or DELETE
statement) and execute it against all parameter found in sequence.

Exactly behaves like .execute() but accepts a list of tuples, where
each tuple represents data of a row within a table.
.executemany() only supports DML (insert, update, delete) statements.

If the SQL statement contains a RETURNING clause, executemany()
returns a result set containing the values for columns listed in the
RETURNING clause.

Example:

The following example will insert 3 rows:

```python
data= [
    (1, 'Michael', 'Widenius')
    (2, 'Diego', 'Dupin')
    (3, 'Lawrin', 'Novitsky')
]
cursor.executemany("INSERT INTO colleagues VALUES (?, ?, ?)", data)
```

To insert special values like NULL or a column default, you need to specify indicators:

- INDICATOR.NULL is used for NULL values
- INDICATOR.IGNORE is used to skip update of a column.
- INDICATOR.DEFAULT is used for a default value (insert/update)
- INDICATOR.ROW is used to skip update/insert of the entire row.

#### NOTE
- All values for a column must have the same data type.
- Indicators can only be used when connecting to a MariaDB Server 10.2 or newer. MySQL servers don’t support this feature.

#### Cursor.fetchall() -> List[Any]

Fetch all remaining rows of a query result, returning them as a
sequence of sequences (e.g. a list of tuples).

An exception will be raised if the previous call to execute() didn't
produce a result set or execute() wasn't called before.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

cursor.execute("SELECT id, name, email FROM users")

# Fetch all rows at once
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

print(f"Total rows: {len(rows)}")

cursor.close()
conn.close()
```

#### Cursor.fetchmany(size: Optional[int] = None) -> List[Any]

Fetch the next set of rows of a query result, returning a sequence
of sequences (e.g. a list of tuples). An empty sequence is returned
when no more rows are available.

The number of rows to fetch per call is specified by the parameter.
If it is not given, the cursor's arraysize determines the number
of rows to be fetched. The method should try to fetch as many rows
as indicated by the size parameter.
If this is not possible due to the specified number of rows not being
available, fewer rows may be returned.

An exception will be raised if the previous call to execute() didn't
produce a result set or execute() wasn't called before.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

cursor.execute("SELECT id, name FROM users ORDER BY id")

# Fetch rows in batches of 10
while True:
    rows = cursor.fetchmany(10)
    if not rows:
        break
    
    print(f"Processing batch of {len(rows)} rows")
    for row in rows:
        print(f"  ID: {row[0]}, Name: {row[1]}")

cursor.close()
conn.close()
```

#### Cursor.fetchone() -> Optional[Any]

Fetch the next row of a query result set, returning a single sequence,
or None if no more data is available.

An exception will be raised if the previous call to execute() didn't
produce a result set or execute() wasn't called before.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

cursor.execute("SELECT id, name FROM users WHERE id = ?", (1,))

# Fetch single row
row = cursor.fetchone()
if row:
    print(f"User found: ID={row[0]}, Name={row[1]}")
else:
    print("User not found")

cursor.close()
conn.close()
```

#### Cursor.next() -> Optional[Any]

Return the next row from the currently executed SQL statement
using the same semantics as .fetchone().

#### Cursor.nextset() -> Optional[bool]

Will make the cursor skip to the next available result set,
discarding any remaining rows from the current set.

#### Cursor.scroll(value: int, mode: str = 'relative') -> None

Scroll the cursor in the result set to a new position according to
mode.

If mode is “relative” (default), value is taken as offset to the
current position in the result set, if set to absolute, value states
an absolute target position.

#### Cursor.setinputsizes() -> None

Required by PEP-249. Does nothing in MariaDB Connector/Python

#### Cursor.setoutputsize() -> None

Required by PEP-249. Does nothing in MariaDB Connector/Python

## Cursor attributes

#### Cursor.arraysize: int

(read/write)

The number of rows to fetch at a time with `.fetchmany()`.

This read/write attribute defaults to 1 meaning to fetch a single row at a time.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Set arraysize for batch processing
cursor.arraysize = 100

cursor.execute("SELECT * FROM large_table")

# fetchmany() will now fetch 100 rows at a time by default
while True:
    rows = cursor.fetchmany()
    if not rows:
        break
    print(f"Processing {len(rows)} rows")

cursor.close()
conn.close()
```

#### Cursor.buffered: bool

(read-only)

Controls whether result sets are buffered in memory or streamed from the server.

**Buffered (True):**
- All result rows are immediately fetched and stored in client memory
- The entire result set is transferred at once
- Connection is freed immediately after execute()
- Multiple cursors can be active on the same connection
- Higher memory usage for large result sets
- Better for small to medium result sets

**Unbuffered (False, default in 2.0):**
- Results are streamed row-by-row from the server
- Only the current row is kept in memory
- Connection remains blocked until all rows are fetched
- Only one unbuffered cursor can be active per connection
- Lower memory usage - ideal for large result sets
- Must fetch all rows before executing another query on the same connection

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

# Unbuffered cursor (default) - streams results, low memory usage
cursor1 = conn.cursor(buffered=False)
print(f"Buffered: {cursor1.buffered}")  # Output: False

cursor1.execute("SELECT * FROM large_table")  # 1 million rows
# Rows are streamed one at a time, not all loaded into memory
for row in cursor1:
    process_row(row)  # Memory efficient
cursor1.close()

# Buffered cursor - fetches all results immediately into memory
cursor2 = conn.cursor(buffered=True)
print(f"Buffered: {cursor2.buffered}")  # Output: True

cursor2.execute("SELECT * FROM small_table")  # 100 rows
rows = cursor2.fetchall()  # All rows loaded into memory at once
# Connection is now free for other operations
cursor2.close()

conn.close()
```

**Best Practices:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

# Use unbuffered for large result sets to avoid memory issues
cursor = conn.cursor(buffered=False)
cursor.execute("SELECT * FROM huge_table")  # Millions of rows

# Process rows one at a time without loading all into memory
for row in cursor:
    # Each row is fetched on demand
    process_large_row(row)

cursor.close()

# Use buffered for small result sets when you need connection freedom
cursor = conn.cursor(buffered=True)
cursor.execute("SELECT * FROM config WHERE active = 1")  # Few rows
config = cursor.fetchall()  # Safe to load all into memory
cursor.close()

# Can now use connection for other operations immediately
cursor2 = conn.cursor()
cursor2.execute("SELECT COUNT(*) FROM users")
count = cursor2.fetchone()[0]
cursor2.close()

conn.close()
```

#### Cursor.close() -> None

Close the cursor and free resources. After closing, the cursor cannot be used anymore.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")

# Using context manager (recommended - auto-closes)
with conn.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    print(f"Total users: {count}")
# Cursor automatically closed here

# Manual close
cursor = conn.cursor()
try:
    cursor.execute("SELECT * FROM users LIMIT 5")
    rows = cursor.fetchall()
finally:
    cursor.close()  # Always close in finally block

conn.close()
```

#### Cursor.connection: Connection

(read-only)

Returns the reference to the connection object on which the cursor was created.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Access connection from cursor
print(f"Database: {cursor.connection.database}")
print(f"User: {cursor.connection.user}")
print(f"Connection ID: {cursor.connection.connection_id}")

cursor.close()
conn.close()
```

#### Cursor.description: Optional[Sequence[Tuple]]

(read-only)

This read-only attribute is a sequence of 11-item tuples.
Each tuple contains information describing one result column:

1. **name** - Column name
2. **type_code** - Column type code
3. **display_size** - Display size
4. **internal_size** - Internal size
5. **precision** - Precision
6. **scale** - Scale
7. **null_ok** - Whether NULL values are allowed
8. **field_flags** - Field flags (extension to PEP-249)
9. **table_name** - Table name (extension to PEP-249)
10. **original_column_name** - Original column name (extension to PEP-249)
11. **original_table_name** - Original table name (extension to PEP-249)

This attribute will be None for operations that do not return rows or if the cursor has
not had an operation invoked via the `.execute*()` method yet.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

cursor.execute("SELECT id, name, email, created_at FROM users LIMIT 1")

# Get column information
if cursor.description:
    print("Column Information:")
    for i, col in enumerate(cursor.description):
        print(f"\nColumn {i}:")
        print(f"  Name: {col[0]}")
        print(f"  Type: {col[1]}")
        print(f"  Nullable: {col[6]}")
        print(f"  Table: {col[8]}")
        print(f"  Original Name: {col[9]}")

# Example output:
# Column 0:
#   Name: id
#   Type: 3
#   Nullable: 0
#   Table: users
#   Original Name: id

cursor.close()
conn.close()
```

**Checking BLOB vs TEXT fields:**

```python
import mariadb
from mariadb.constants import FIELD_TYPE, FIELD_FLAG

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

cursor.execute("SELECT content FROM documents LIMIT 1")

if cursor.description[0][1] == FIELD_TYPE.BLOB:
    if cursor.description[0][7] & FIELD_FLAG.BINARY:
        print("Column is BLOB")
    else:
        print("Column is TEXT")

cursor.close()
conn.close()
```

#### Cursor.lastrowid

Returns the ID generated by a query on a table with a column having
the AUTO_INCREMENT attribute or the value for the last usage of
LAST_INSERT_ID().

If the last query wasn’t an INSERT or UPDATE
statement or if the modified table does not have a column with the
AUTO_INCREMENT attribute and LAST_INSERT_ID was not used, the returned
value will be None

#### Cursor.metadata: Optional[Dict[str, List]]

(read-only)

Similar to the `description` property, this property returns a dictionary with complete metadata for all columns in the result set.

Each dictionary key contains a list of values, one for each column in the result set.

**Dictionary Keys:**

- **catalog** - Catalog name (always 'def')
- **schema** - Current schema/database name
- **field** - Column alias name, or original column name if no alias
- **org_field** - Original column name
- **table** - Table alias name, or original table name if no alias
- **org_table** - Original table name
- **type** - Column type (values from `mariadb.constants.FIELD_TYPE`)
- **charset** - Character set (e.g., 'utf8mb4' or 'binary')
- **length** - Maximum length of the column
- **max_length** - Maximum length of data in the result set
- **decimals** - Number of decimals for numeric types
- **flags** - Field flags (values from `mariadb.constants.FIELD_FLAG`)
- **ext_type_or_format** - Extended data type (values from `mariadb.constants.EXT_FIELD_TYPE`)

*Since version 1.1.8*

**Example:**

```python
import mariadb
from mariadb.constants import FIELD_TYPE, FIELD_FLAG, EXT_FIELD_TYPE

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

cursor.execute("""
    SELECT 
        id,
        name AS user_name,
        email,
        created_at
    FROM users
    LIMIT 1
""")

# Get complete metadata
metadata = cursor.metadata

if metadata:
    print("Complete Column Metadata:")
    print(f"Number of columns: {len(metadata['field'])}\n")
    
    for i in range(len(metadata['field'])):
        print(f"Column {i}:")
        print(f"  Field (alias): {metadata['field'][i]}")
        print(f"  Original field: {metadata['org_field'][i]}")
        print(f"  Table (alias): {metadata['table'][i]}")
        print(f"  Original table: {metadata['org_table'][i]}")
        print(f"  Schema: {metadata['schema'][i]}")
        print(f"  Type: {metadata['type'][i]}")
        print(f"  Charset: {metadata['charset'][i]}")
        print(f"  Length: {metadata['length'][i]}")
        print(f"  Max length: {metadata['max_length'][i]}")
        print(f"  Decimals: {metadata['decimals'][i]}")
        print(f"  Flags: {metadata['flags'][i]}")
        print()

# Example output:
# Column 0:
#   Field (alias): id
#   Original field: id
#   Table (alias): users
#   Original table: users
#   Schema: mydb
#   Type: 3
#   Charset: binary
#   Length: 11
#   Max length: 1
#   Decimals: 0
#   Flags: 16899

cursor.close()
conn.close()
```

**Detecting Extended Types (JSON, UUID, INET, Geometry):**

```python
import mariadb
from mariadb.constants import FIELD_TYPE, EXT_FIELD_TYPE

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Create table with extended types
cursor.execute("""
    CREATE TEMPORARY TABLE test_types (
        data JSON,
        user_id UUID,
        ip_addr INET4,
        location POINT
    )
""")

cursor.execute("SELECT data, user_id, ip_addr, location FROM test_types")
metadata = cursor.metadata

# Check extended types
for i, field_name in enumerate(metadata['field']):
    ext_type = metadata['ext_type_or_format'][i]
    base_type = metadata['type'][i]
    
    print(f"{field_name}:")
    print(f"  Base type: {base_type}")
    
    if ext_type == EXT_FIELD_TYPE.JSON:
        print(f"  Extended type: JSON")
    elif ext_type == EXT_FIELD_TYPE.UUID:
        print(f"  Extended type: UUID")
    elif ext_type == EXT_FIELD_TYPE.INET4:
        print(f"  Extended type: INET4")
    elif ext_type == EXT_FIELD_TYPE.POINT:
        print(f"  Extended type: POINT (Geometry)")
    print()

cursor.close()
conn.close()
```

#### Cursor.sp_outparams: bool

(read-only)

Indicates if the current result set contains OUT or INOUT parameters from a previously executed stored procedure.

When calling a stored procedure with OUT or INOUT parameters using `callproc()` or `execute()`, the output parameters are returned as a separate result set. This attribute is `True` when the current result set contains these output parameters, and `False` otherwise.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Create a stored procedure with OUT parameter
cursor.execute("DROP PROCEDURE IF EXISTS calculate_total")
cursor.execute("""
    CREATE PROCEDURE calculate_total(
        IN user_id INT,
        OUT total_amount DECIMAL(10,2)
    )
    BEGIN
        SELECT SUM(amount) INTO total_amount
        FROM orders
        WHERE user_id = user_id;
    END
""")

# Call the procedure with OUT parameter
cursor.callproc("calculate_total", (123, 0))

# First check if current result set contains output parameters
print(f"Has output params: {cursor.sp_outparams}")  # Output: True

# Fetch the output parameter value
result = cursor.fetchone()
total = result[0]
print(f"Total amount: {total}")

cursor.close()
conn.close()
```

**Example with Multiple Result Sets:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Create procedure that returns data AND has OUT parameter
cursor.execute("DROP PROCEDURE IF EXISTS get_user_stats")
cursor.execute("""
    CREATE PROCEDURE get_user_stats(
        IN user_id INT,
        OUT order_count INT
    )
    BEGIN
        -- First result set: user details
        SELECT id, name, email FROM users WHERE id = user_id;
        
        -- Set OUT parameter
        SELECT COUNT(*) INTO order_count
        FROM orders
        WHERE user_id = user_id;
    END
""")

# Call the procedure
cursor.callproc("get_user_stats", (123, 0))

# First result set: user details
print(f"Has output params: {cursor.sp_outparams}")  # Output: False
user = cursor.fetchone()
print(f"User: {user}")

# Move to next result set (OUT parameters)
cursor.nextset()
print(f"Has output params: {cursor.sp_outparams}")  # Output: True
out_params = cursor.fetchone()
order_count = out_params[0]
print(f"Order count: {order_count}")

cursor.execute("DROP PROCEDURE IF EXISTS get_user_stats")
cursor.close()
conn.close()
```

**Using with Binary Protocol:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor(binary=True)

# Call procedure using CALL statement with binary protocol
cursor.execute("CALL calculate_total(?, ?)", (123, 0))

# Check if result contains output parameters
if cursor.sp_outparams:
    result = cursor.fetchone()
    print(f"Total: {result[0]}")

cursor.close()
conn.close()
```


#### Cursor.rowcount: int

(read-only)

Returns the number of rows that the last `execute*()` method produced (for DQL statements like SELECT) or affected (for DML statements like UPDATE, INSERT, DELETE).

**Return Values:**
- **Positive number** - Number of rows returned (SELECT) or affected (INSERT/UPDATE/DELETE)
- **-1** - No `execute*()` has been performed, or rowcount cannot be determined
- **0** - Statement executed but no rows were affected/returned

**Important Notes:**
- For **unbuffered cursors** (default in 2.0), the exact row count is only available **after all rows have been fetched**
- For **buffered cursors**, the row count is immediately available after `execute()`
- For **INSERT/UPDATE/DELETE**, the row count is always immediately available

**Examples:**

**Unbuffered Cursor (Default):**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor(buffered=False)  # Default

# Execute SELECT
cursor.execute("SELECT * FROM users")

# Rowcount is -1 until all rows are fetched
print(f"Rowcount before fetch: {cursor.rowcount}")  # Output: -1

# Fetch all rows
rows = cursor.fetchall()

# Now rowcount is available
print(f"Rowcount after fetch: {cursor.rowcount}")  # Output: 150 (actual count)
print(f"Rows fetched: {len(rows)}")  # Output: 150

cursor.close()
conn.close()
```

**Buffered Cursor:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor(buffered=True)

# Execute SELECT
cursor.execute("SELECT * FROM users WHERE active = 1")

# Rowcount is immediately available for buffered cursors
print(f"Rowcount: {cursor.rowcount}")  # Output: 42 (immediately)

# Fetch the rows
rows = cursor.fetchall()
print(f"Rows fetched: {len(rows)}")  # Output: 42

cursor.close()
conn.close()
```

**DML Statements (INSERT/UPDATE/DELETE):**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# INSERT - rowcount shows affected rows
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
               ("John Doe", "john@example.com"))
print(f"Rows inserted: {cursor.rowcount}")  # Output: 1

# UPDATE - rowcount shows affected rows
cursor.execute("UPDATE users SET active = 1 WHERE created_at < NOW()")
print(f"Rows updated: {cursor.rowcount}")  # Output: 25

# DELETE - rowcount shows affected rows
cursor.execute("DELETE FROM users WHERE active = 0")
print(f"Rows deleted: {cursor.rowcount}")  # Output: 10

# UPDATE with no matching rows
cursor.execute("UPDATE users SET active = 1 WHERE id = 99999")
print(f"Rows updated: {cursor.rowcount}")  # Output: 0 (no rows matched)

conn.commit()
cursor.close()
conn.close()
```

**Batch Operations with executemany():**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Insert multiple rows
data = [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com")
]

cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", data)
print(f"Total rows inserted: {cursor.rowcount}")  # Output: 3

conn.commit()
cursor.close()
conn.close()
```

**Practical Use Case - Verify Operation Success:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Update a specific user
user_id = 123
cursor.execute("UPDATE users SET last_login = NOW() WHERE id = ?", (user_id,))

if cursor.rowcount == 0:
    print(f"Warning: User {user_id} not found or not updated")
elif cursor.rowcount == 1:
    print(f"User {user_id} updated successfully")
    conn.commit()
else:
    print(f"Error: Multiple rows affected ({cursor.rowcount})")
    conn.rollback()

cursor.close()
conn.close()
```

#### Cursor.statement: Optional[str]

(read-only)

Returns the last SQL statement that was executed by the cursor.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM users WHERE id = ?", (123,))

# Get the executed statement
print(f"Last statement: {cursor.statement}")
# Output: Last statement: SELECT * FROM users WHERE id = ?

# Execute another query
cursor.execute("UPDATE users SET last_login = NOW() WHERE id = ?", (123,))
print(f"Last statement: {cursor.statement}")
# Output: Last statement: UPDATE users SET last_login = NOW() WHERE id = ?

cursor.close()
conn.close()
```

#### Cursor.warnings: int

(read-only)

Returns the number of warnings from the last executed statement, or zero if there are no warnings.

**Note:** Detailed warning messages can be retrieved using the `connection.show_warnings()` method.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Execute statement that may generate warnings
cursor.execute("SET session sql_mode=''")
cursor.execute("CREATE TEMPORARY TABLE test_warn (a tinyint)")
cursor.execute("INSERT INTO test_warn VALUES (300)")  # Out of range

# Check warning count from cursor
if cursor.warnings > 0:
    print(f"Number of warnings: {cursor.warnings}")
    
    # Get detailed warnings from connection
    warnings = conn.show_warnings()
    for level, code, message in warnings:
        print(f"{level} ({code}): {message}")
    # Output: Warning (1264): Out of range value for column 'a' at row 1

cursor.close()
conn.close()
```

#### Cursor.rownumber: Optional[int]

(read-only)

Returns the current 0-based index of the cursor in the result set, or `None` if no result set is available.

This property tracks the position within the current result set as rows are fetched.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

cursor.execute("SELECT id, name FROM users ORDER BY id LIMIT 5")

print(f"Initial rownumber: {cursor.rownumber}")  # Output: 0

# Fetch rows one by one
row1 = cursor.fetchone()
print(f"After 1st fetch: {cursor.rownumber}")  # Output: 1

row2 = cursor.fetchone()
print(f"After 2nd fetch: {cursor.rownumber}")  # Output: 2

# Fetch remaining rows
remaining = cursor.fetchall()
print(f"After fetchall: {cursor.rownumber}")  # Output: 5

cursor.close()
conn.close()
```

#### Cursor.field_count: int

(read-only)

Returns the number of columns in the current result set, or 0 if there is no result set.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

# Before executing any query
print(f"Field count: {cursor.field_count}")  # Output: 0

# Execute SELECT with 3 columns
cursor.execute("SELECT id, name, email FROM users LIMIT 1")
print(f"Field count: {cursor.field_count}")  # Output: 3

# Execute SELECT with all columns
cursor.execute("SELECT * FROM users LIMIT 1")
print(f"Field count: {cursor.field_count}")  # Output: (number of columns in users table)

# Execute non-SELECT statement
cursor.execute("UPDATE users SET active = 1 WHERE id = 1")
print(f"Field count: {cursor.field_count}")  # Output: 0 (no result set)

cursor.close()
conn.close()
```

#### Cursor.closed: bool

(read-only)

Returns `True` if the cursor is closed, `False` otherwise.

A cursor is considered closed if either the cursor itself was closed or the parent connection was closed.

**Example:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

print(f"Cursor closed: {cursor.closed}")  # Output: False

# Execute a query
cursor.execute("SELECT 1")
print(f"Cursor closed: {cursor.closed}")  # Output: False

# Close the cursor
cursor.close()
print(f"Cursor closed: {cursor.closed}")  # Output: True

# Trying to use a closed cursor raises an error
try:
    cursor.execute("SELECT 2")
except mariadb.ProgrammingError as e:
    print(f"Error: {e}")  # Output: Error: Cursor is closed

conn.close()
```

**Connection closure also closes cursors:**

```python
import mariadb

conn = mariadb.connect("mariadb://user:password@localhost/mydb")
cursor = conn.cursor()

print(f"Cursor closed: {cursor.closed}")  # Output: False

# Close the connection
conn.close()

# Cursor is now also considered closed
print(f"Cursor closed: {cursor.closed}")  # Output: True
```

{% @marketo/form formId="4316" %}
