# Expression Filters

> **Version:** langchain-mariadb v0.0.20

A flexible and composable filter expression system for building SQL-like queries.

This module provides a builder pattern implementation for creating complex filter
expressions that can be converted to various query formats.

**Example:**

```python
# Dict filter value
filter = {
   '$or': [{'status': {'$eq': 'active'}}, {'status': {'$eq': 'pending'}}],
   'age': {'$gte': 18}
   'country': {'$in': ['US', 'CA', 'UK']}
}

# Convert to SQL-like string (with a proper converter implementation)
converter = SQLFilterExpressionConverter()  # Some converter
sql_where = converter.convert_expression(filter)
print(sql_where)
# Output:
# (status = 'active' OR status = 'pending')
# AND age >= 18 AND country IN ['US','CA','UK']
```

## Operator

Enumeration of supported filter operations

### Attributes

- **AND**: 
- **OR**: 
- **EQ**: 
- **NE**: 
- **GT**: 
- **GTE**: 
- **LT**: 
- **LTE**: 
- **LIKE**: 
- **NLIKE**: 
- **IN**: 
- **NIN**: 
- **NOT**: 

---

## Key

Represents a key in a filter expression

### Constructor

```python
__init__(key: str)
```

### Attributes

- **key**: 

---

## Value

Represents a value in a filter expression

### Constructor

```python
__init__(value: ValueType)
```

### Attributes

- **value**: 

---

## Expression

Represents a boolean filter expression with a specific structure.

### Constructor

```python
__init__(type_: Operator, left: Operand, right: Optional[Operand] = None)
```

### Attributes

- **type**: 
- **left**: 
- **right**: 

---

## Group

Represents a grouped collection of filter expressions.

### Constructor

```python
__init__(content: Expression)
```

### Attributes

- **content**: 

---

## StringBuilder

Simple StringBuilder implementation for efficient string concatenation

### Constructor

```python
__init__() -> None
```

### Methods

#### `append`

```python
append(string: str) -> None
```

### Attributes

- **buffer** (`List[str]`): 

---

## FilterExpressionConverter

Abstract base class defining the interface for converting filter expressions
into various string-based query representations

### Methods

#### `convert_expression`

```python
convert_expression(filters: dict) -> str
```

Convert a complete expression into its string representation

#### `convert_symbol_to_context`

```python
convert_symbol_to_context(exp: Expression, context: StringBuilder) -> None
```

Determine the appropriate operation symbol for a given expression

#### `convert_operand_to_context`

```python
convert_operand_to_context(operand: Operand, context: StringBuilder) -> None
```

Convert an operand into a string representation within a given context

#### `convert_expression_to_context`

```python
convert_expression_to_context(expression: Expression, context: StringBuilder) -> None
```

Convert an expression to its string representation in the given context

#### `convert_key_to_context`

```python
convert_key_to_context(filter_key: Key, context: StringBuilder) -> None
```

Convert a key to its string representation in the given context

#### `convert_value_to_context`

```python
convert_value_to_context(filter_value: Value, context: StringBuilder) -> None
```

Convert a value to its string representation in the given context

#### `convert_single_value_to_context`

```python
convert_single_value_to_context(value: ValueType, context: StringBuilder) -> None
```

Convert a single value to its string representation in the given context

#### `write_group_start`

```python
write_group_start(group: Group, context: StringBuilder) -> None
```

Write the start of a group in the given context

#### `write_group_end`

```python
write_group_end(group: Group, context: StringBuilder) -> None
```

Write the end of a group in the given context

#### `write_value_range_start`

```python
write_value_range_start(list_value: Value, context: StringBuilder) -> None
```

Write the start of a value range in the given context

#### `write_value_range_end`

```python
write_value_range_end(list_value: Value, context: StringBuilder) -> None
```

Write the end of a value range in the given context

#### `write_value_range_separator`

```python
write_value_range_separator(list_value: Value, context: StringBuilder) -> None
```

Write the separator between values in a range in the given context

---

## BaseFilterExpressionConverter

Base implementation of the FilterExpressionConverter interface providing
common functionality for converting filter expressions to string representations

### Methods

#### `convert_expression`

```python
convert_expression(filters: dict) -> str
```

#### `convert_symbol_to_context`

```python
convert_symbol_to_context(exp: Expression, context: StringBuilder) -> None
```

#### `convert_operand_to_context`

```python
convert_operand_to_context(operand: Operand, context: StringBuilder) -> None
```

#### `convert_value_to_context`

```python
convert_value_to_context(filter_value: Value, context: StringBuilder) -> None
```

#### `convert_single_value_to_context`

```python
convert_single_value_to_context(value: ValueType, context: StringBuilder) -> None
```

#### `write_value_range_start`

```python
write_value_range_start(list_value: Value, context: StringBuilder) -> None
```

#### `write_value_range_end`

```python
write_value_range_end(list_value: Value, context: StringBuilder) -> None
```

#### `write_value_range_separator`

```python
write_value_range_separator(list_value: Value, context: StringBuilder) -> None
```

---

## MariaDBFilterExpressionConverter

Converter for MariaDB filter expressions.

### Constructor

```python
__init__(metadata_field_name: str)
```

### Methods

#### `convert_expression_to_context`

```python
convert_expression_to_context(expression: Expression, context: StringBuilder) -> None
```

#### `convert_key_to_context`

```python
convert_key_to_context(key: Key, context: StringBuilder) -> None
```

#### `write_value_range_start`

```python
write_value_range_start(_list_value: Value, context: StringBuilder) -> None
```

#### `write_value_range_end`

```python
write_value_range_end(_list_value: Value, context: StringBuilder) -> None
```

#### `write_group_start`

```python
write_group_start(_group: Group, context: StringBuilder) -> None
```

#### `write_group_end`

```python
write_group_end(_group: Group, context: StringBuilder) -> None
```

### Attributes

- **metadata_field_name**: 

---

## `eq`

```python
eq(key: str, value: ValueType) -> Expression
```

Check if a key equals a value.

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **value** (`ValueType`): The value to compare against

**Returns:**

 `Expression` - Expression representing key == value

## `ne`

```python
ne(key: str, value: ValueType) -> Expression
```

Check if a key does not equal a value.

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **value** (`ValueType`): The value to compare against

**Returns:**

 `Expression` - Expression representing key != value

## `gt`

```python
gt(key: str, value: Union[int, str, float]) -> Expression
```

Check if a key is greater than a value.

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **value** (`Union[int, str, float]`): The numeric or string value to compare against

**Returns:**

 `Expression` - Expression representing key > value

## `gte`

```python
gte(key: str, value: Union[int, str, float]) -> Expression
```

Check if a key is greater than or equal to a value.

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **value** (`Union[int, str, float]`): The numeric or string value to compare against

**Returns:**

 `Expression` - Expression representing key >= value

## `lt`

```python
lt(key: str, value: Union[int, str, float]) -> Expression
```

Check if a key is less than a value.

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **value** (`Union[int, str, float]`): The numeric or string value to compare against

**Returns:**

 `Expression` - Expression representing key < value

## `lte`

```python
lte(key: str, value: Union[int, str, float]) -> Expression
```

Check if a key is less than or equal to a value.

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **value** (`Union[int, str, float]`): The numeric or string value to compare against

**Returns:**

 `Expression` - Expression representing key <= value

## `like`

```python
like(key: str, value: Union[int, str, float]) -> Expression
```

Check if a key matches a pattern (SQL LIKE).

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **value** (`Union[int, str, float]`): The pattern to match (use % as wildcard)

**Returns:**

 `Expression` - Expression representing key LIKE value

## `nlike`

```python
nlike(key: str, value: Union[int, str, float]) -> Expression
```

Check if a key does not match a pattern (SQL NOT LIKE).

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **value** (`Union[int, str, float]`): The pattern to not match (use % as wildcard)

**Returns:**

 `Expression` - Expression representing key NOT LIKE value

## `includes`

```python
includes(key: str, values: Union[List[int], List[str], List[bool], List[float]]) -> Expression
```

Check if a key's value is in a list of values (SQL IN operator).

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **values** (`Union[List[int], List[str], List[bool], List[float]]`): List of values to check against

**Returns:**

 `Expression` - Expression representing key IN values

## `excludes`

```python
excludes(key: str, values: Union[List[int], List[str], List[bool], List[float]]) -> Expression
```

Check if a key's value is not in a list of values (SQL NOT IN operator).

**Parameters:**

- **key** (`str`): The metadata field name to filter on
- **values** (`Union[List[int], List[str], List[bool], List[float]]`): List of values to exclude

**Returns:**

 `Expression` - Expression representing key NOT IN values

## `both`

```python
both(left: Operand, right: Operand) -> Expression
```

Combine two expressions with logical AND.

**Parameters:**

- **left** (`Operand`): First expression
- **right** (`Operand`): Second expression

**Returns:**

 `Expression` - Expression representing (left AND right)

## `either`

```python
either(left: Operand, right: Operand) -> Expression
```

Combine two expressions with logical OR.

**Parameters:**

- **left** (`Operand`): First expression
- **right** (`Operand`): Second expression

**Returns:**

 `Expression` - Expression representing (left OR right)

## `negate`

```python
negate(content: Expression) -> Expression
```

Negate an expression with logical NOT.

**Parameters:**

- **content** (`Expression`): Expression to negate

**Returns:**

 `Expression` - Expression representing NOT content

## `group`

```python
group(content: Expression) -> Group
```

Group an expression with parentheses for precedence control.

**Parameters:**

- **content** (`Expression`): Expression to group

**Returns:**

 `Group` - Group wrapping the expression
