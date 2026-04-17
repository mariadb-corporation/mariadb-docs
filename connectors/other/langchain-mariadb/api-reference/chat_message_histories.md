# Chat Message History

> **Version:** langchain-mariadb v0.0.20

Client for persisting chat message history in a MariaDB database.

## MariaDBChatMessageHistory

Chat message history that persists to a MariaDB database.

### Constructor

```python
__init__(
    table_name: str,
    session_id: str,
    datasource: Union[Engine | str],
    engine_args: Optional[dict[str, Any]] = None
) -> None
```

Initialize a chat message history that persists to a MariaDB database.

**Parameters:**

- **table_name** (`str`): Name of the database table to use (must be alphanum + '_')
- **session_id** (`str`): UUID string to identify the chat session
- **datasource** (`Union[Engine | str]`): datasource (connection string or a sqlalchemy engine)

**Raises:**

- **ValueError**: If pool is not provided, session_id is not a valid UUID,
or table_name contains invalid characters

### Methods

#### `create_tables`

```python
create_tables(datasource: Union[Engine | str], table_name: str) -> None
```

Create the table schema in the database and create relevant indexes.

**Parameters:**

- **datasource** (`Union[Engine | str]`): datasource (connection string or sqlalchemy engine)
- **table_name** (`str`): Name of the table to create

#### `drop_table`

```python
drop_table(datasource: Union[Engine | str], table_name: str) -> None
```

Delete the table schema from the database.

**Parameters:**

- **datasource** (`Union[Engine | str]`): datasource (connection string or sqlalchemy engine)
- **table_name** (`str`): Name of the table to drop

#### `add_messages`

```python
add_messages(messages: Sequence[BaseMessage]) -> None
```

Add messages to the chat history.

**Parameters:**

- **messages** (`Sequence[BaseMessage]`): Sequence of messages to add

#### `get_messages`

```python
get_messages() -> List[BaseMessage]
```

Retrieve messages from the chat history.

**Returns:**

 `List[BaseMessage]` - List of messages in chronological order

#### `clear`

```python
clear() -> None
```

Clear all messages for the current session.

### Attributes

- **messages** (`List[BaseMessage]`): Get all messages in the chat history.

---
