{#metadatainstrumentation}

# Metadata Instrumentation

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Macros

| Name | Description |
|------|-------------|
| [`mysql_mdl_create`](#mysql_mdl_create)  | Instrumented metadata lock creation. |
| [`mysql_mdl_set_status`](#mysql_mdl_set_status)  |  |
| [`mysql_mdl_destroy`](#mysql_mdl_destroy)  | Instrumented metadata lock destruction. |

---

{#mysql_mdl_create}

### mysql_mdl_create

```cpp
#define mysql_mdl_create(I, K, T, D, S, F, L, I, K, T, D, S, F, L) NULL
```

Defined in psi/mysql_mdl.h:74

Instrumented metadata lock creation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `I` |  | Metadata lock identity |
| `K` |  | Metadata key |
| `T` |  | Metadata lock type |
| `D` |  | Metadata lock duration |
| `S` |  | Metadata lock status |
| `F` |  | request source file |
| `L` |  | request source line |
| `I` |  | Metadata lock identity |
| `K` |  | Metadata key |
| `T` |  | Metadata lock type |
| `D` |  | Metadata lock duration |
| `S` |  | Metadata lock status |
| `F` |  | request source file |
| `L` |  | request source line |

---

{#mysql_mdl_set_status}

### mysql_mdl_set_status

```cpp
#define mysql_mdl_set_status(L, S, L, S) do {} while (0)
```

Defined in psi/mysql_mdl.h:81

---

{#mysql_mdl_destroy}

### mysql_mdl_destroy

```cpp
#define mysql_mdl_destroy(M, M) do {} while (0)
```

Defined in psi/mysql_mdl.h:95

Instrumented metadata lock destruction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `M` |  | Metadata lock |
| `M` |  | Metadata lock |

