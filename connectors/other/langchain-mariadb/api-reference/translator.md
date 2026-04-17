# Translator

> **Version:** langchain-mariadb v0.0.20

## MariaDBTranslator

Translate `MariaDB` internal query language elements to valid filters.

### Methods

#### `visit_operation`

```python
visit_operation(operation: Operation) -> Dict
```

#### `visit_comparison`

```python
visit_comparison(comparison: Comparison) -> Dict
```

#### `visit_structured_query`

```python
visit_structured_query(structured_query: StructuredQuery) -> Tuple[str, dict]
```

### Attributes

- **allowed_operators**: Subset of allowed logical operators.
- **allowed_comparators**: Subset of allowed logical comparators.

---
