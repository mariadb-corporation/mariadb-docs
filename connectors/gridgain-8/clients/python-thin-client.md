---
hidden: true
description: >-
  How to install and use the GridGain 8 Python thin client: connecting to a cluster, partition awareness, key-value operations, transactions, scan, vector, and SQL queries, SSL/TLS, and authentication.
---

# Python Thin Client

## Prerequisites

Python 3.11 or later. Pre-built binaries are available for Python 3.11 to 3.15.

{% hint style="info" %}
Starting with version 1.7.0, the Python thin client does not support Python 3.9 and 3.10. To use the client with these Python versions, install version 1.6.0 or earlier.
{% endhint %}

## Installation

You can install the Python thin client either using `pip` or from a zip archive.

### Using PIP

The Python thin client package is called `pygridgain`. You can install it using the following command:

{% include "../.gitbook/includes/gg8-install-python-pip.md" %}

{% hint style="warning" %}
The `pygridgain` package on PyPI also contains the GridGain 9 client, which has version numbers 9.0 and higher. Always specify a version lower than 9, as in the command above. A plain `pip install pygridgain` installs the GridGain 9 client, which does not work with GridGain 8.
{% endhint %}

### Using ZIP Archive

The thin client can be installed from the zip archive available for download from the GridGain website:

- Go to the website and download the [GridGain Python Thin Client](https://www.gridgain.com/resources/download) archive.
- Unpack the archive and navigate to the root folder.
- Install the client using the command below.

```shell
pip3 install .
```

This will install `pygridgain` in your environment in the so-called "develop" or "editable" mode. Learn more
about the mode from the [official documentation](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs).

Check the `requirements` folder and install additional requirements, if needed, using the following command:

```shell
pip3 install -r requirements/<your task>.txt
```

Refer to the [Setuptools manual](https://setuptools.readthedocs.io/en/latest/) for more details about `setup.py` usage.

## Connecting to Cluster

The ZIP distribution package contains runnable examples that demonstrate
basic usage scenarios of the Python thin client. The examples are located in
the `{client_dir}/examples` directory.

The following code snippet shows how to connect to a cluster from the Python thin client:

```python
from pygridgain import Client

## Open a connection
client = Client()
client.connect('127.0.0.1', 10800)
```

## Client Failover

You can configure the client to automatically fail over to another node if the connection to the current node fails or times out.

When the connection fails, the client propagates the initial exception (`OSError` or `SocketError`), but keeps its constructor’s parameters intact and tries to reconnect transparently.
When the client fails to reconnect, it throws a special `ReconnectError` exception.

In the following example, the client is given the addresses of three cluster nodes.

```python
from pygridgain import Client
from pygridgain.datatypes.cache_config import CacheMode
from pygridgain.datatypes.prop_codes import *
from pygridgain.exceptions import SocketError

nodes = [
    ('127.0.0.1', 10800),
    ('217.29.2.1', 10800),
    ('200.10.33.1', 10800),
]

client = Client(timeout=40.0)
client.connect(nodes)
print('Connected to {}'.format(client))

my_cache = client.get_or_create_cache({
    PROP_NAME: 'my_cache',
    PROP_CACHE_MODE: CacheMode.REPLICATED,
})
my_cache.put('test_key', 0)

# Abstract main loop
while True:
    try:
        # Do the work
        test_value = my_cache.get('test_key')
        my_cache.put('test_key', test_value + 1)
    except (OSError, SocketError) as e:
        # Recover from error (repeat last command, check data
        # consistency or just continue − depends on the task)
        print('Error: {}'.format(e))
        print('Last value: {}'.format(my_cache.get('test_key')))
        print('Reconnected to {}'.format(client))
```

## Partition Awareness

{% include "../.gitbook/includes/gg8-partition-awareness.md" %}

To enable partition awareness, set the `partition_aware` parameter to true in the client constructor and provide
addresses of all the server nodes in the connection string.

```python
client = Client(partition_aware=True)
nodes = [
    ('127.0.0.1', 10800),
    ('217.29.2.1', 10800),
    ('200.10.33.1', 10800),
]

client.connect(nodes)
```

## Creating a Cache

You can get an instance of a cache using one of the following methods:

- `get_cache(settings)` — creates a local Cache object with the given name or set of parameters. The cache must exist in the cluster; otherwise, an exception will be thrown when you attempt to perform operations on that cache.
- `create_cache(settings)` — creates a cache with the given name or set of parameters.
- `get_or_create_cache(settings)` — returns an existing cache or creates it if the cache does not exist.

Each method accepts a cache name or a dictionary of properties that represents a cache configuration.

```python
from pygridgain import Client

# Open a connection
client = Client()
client.connect('127.0.0.1', 10800)

# Create a cache
my_cache = client.create_cache('myCache')
```

Here is an example of creating a cache with a set of properties:

```python
from collections import OrderedDict

from pygridgain import Client, GenericObjectMeta
from pygridgain.datatypes import *
from pygridgain.datatypes.prop_codes import *

# Open a connection
client = Client()
client.connect('127.0.0.1', 10800)

cache_config = {
    PROP_NAME: 'my_cache',
    PROP_BACKUPS_NUMBER: 2,
    PROP_CACHE_KEY_CONFIGURATION: [
        {
            'type_name': 'PersonKey',
            'affinity_key_field_name': 'companyId'
        }
    ]
}

my_cache = client.create_cache(cache_config)


class PersonKey(metaclass=GenericObjectMeta, type_name='PersonKey', schema=OrderedDict([
    ('personId', IntObject),
    ('companyId', IntObject),
])):
    pass


personKey = PersonKey(personId=1, companyId=1)
my_cache.put(personKey, 'test')

print(my_cache.get(personKey))
```

See the next section for the list of supported cache properties.

### Cache Configuration

The list of property keys that you can specify are provided in the `prop_codes` module.

| Property name | Type | Description |
| --- | --- | --- |
| PROP_NAME | str | Cache name. This is the only required property. |
| PROP_CACHE_MODE | int | [Cache mode](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/data-modeling/data-partitioning#partitionedreplicated-mode):<br>REPLICATED=1,<br>PARTITIONED=2 |
| PROP_CACHE_ATOMICITY_MODE | int | [Cache atomicity mode](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/configuring-caches/atomicity-modes):<br>TRANSACTIONAL=0,<br>ATOMIC=1 |
| PROP_BACKUPS_NUMBER | int | [Number of backup partitions](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/data-modeling/data-partitioning#backup-partitions). |
| PROP_WRITE_SYNCHRONIZATION_MODE | int | Write synchronization mode:<br>FULL_SYNC=0,<br>FULL_ASYNC=1,<br>PRIMARY_SYNC=2 |
| PROP_COPY_ON_READ | bool | The copy on read flag. The default value is `true`. |
| PROP_READ_FROM_BACKUP | bool | The flag indicating whether entries will be read from the local backup partitions, when available, or will always be requested from the primary partitions. The default value is `true`. |
| PROP_DATA_REGION_NAME | str | [Data region](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/memory-configuration/data-regions) name. |
| PROP_IS_ONHEAP_CACHE_ENABLED | bool | Enable [on-heap caching](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/configuring-caches/on-heap-caching) for the cache. |
| PROP_QUERY_ENTITIES | list | A list of query entities. See the [Query Entities](#query-entities) section below for details.) |
| PROP_QUERY_PARALLELISM | int | [Query parallelism](https://www.gridgain.com/sdk/8.9.38/javadoc/org/apache/ignite/configuration/CacheConfiguration.html#getQueryParallelism) |
| PROP_QUERY_DETAIL_METRIC_SIZE | int | Query detail metric size |
| PROP_SQL_SCHEMA | str | SQL Schema |
| PROP_SQL_INDEX_INLINE_MAX_SIZE | int | SQL index inline maximum size |
| PROP_SQL_ESCAPE_ALL | bool | Turns on SQL escapes |
| PROP_MAX_QUERY_ITERATORS | int | Maximum number of query iterators |
| PROP_REBALANCE_MODE | int | Rebalancing mode:<br>SYNC=0,<br>ASYNC=1,<br>NONE=2 |
| PROP_REBALANCE_DELAY | int | Rebalancing delay (ms) |
| PROP_REBALANCE_TIMEOUT | int | Rebalancing timeout (ms) |
| PROP_REBALANCE_BATCH_SIZE | int | Rebalancing batch size |
| PROP_REBALANCE_BATCHES_PREFETCH_COUNT | int | Rebalancing prefetch count |
| PROP_REBALANCE_ORDER | int | Rebalancing order |
| PROP_REBALANCE_THROTTLE | int | Rebalancing throttle interval (ms) |
| PROP_GROUP_NAME | str | Group name |
| PROP_CACHE_KEY_CONFIGURATION | list | Cache Key Configuration (see [Cache key](#cache-key)) |
| PROP_DEFAULT_LOCK_TIMEOUT | int | Default lock timeout (ms) |
| PROP_MAX_CONCURRENT_ASYNC_OPERATIONS | int | Maximum number of concurrent asynchronous operations |
| PROP_PARTITION_LOSS_POLICY | int | [Partition loss policy](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/partition-loss-policy):<br>READ_ONLY_SAFE=0,<br>READ_ONLY_ALL=1,<br>READ_WRITE_SAFE=2,<br>READ_WRITE_ALL=3,<br>IGNORE=4 |
| PROP_EAGER_TTL | bool | [Eager TTL](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/configuring-caches/expiry-policies#eager-ttl) |
| PROP_STATISTICS_ENABLED | bool | The flag that enables statistics. |

#### Query Entities

Query entities are objects that describe [queryable fields](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/SQL/sql-api#configuring-queryable-fields), i.e. the fields of the cache objects that can be queried using SQL queries.

- `table_name`: SQL table name.
- `key_field_name`: name of the key field.
- `key_type_name`: name of the key type (Java type or complex object).
- `value_field_name`: name of the value field.
- `value_type_name`: name of the value type.
- `field_name_aliases`: a list of 0 or more dicts of aliases (see [Field Name Aliases](#field-name-aliases)).
- `query_fields`: a list of 0 or more query field names (see [Query Fields](#query-fields)).
- `query_indexes`: a list of 0 or more query indexes (see [Query Indexes](#query-indexes)).

#### Field Name Aliases

Field name aliases are used to give a convenient name for the full property name (object.name -> objectName).

- `field_name`: field name.
- `alias`: alias (str).

#### Query Fields

Query fields define the fields that are queryable.

- `name`: field name.
- `type_name`: name of Java type or complex object.
- `is_key_field`: (optional) boolean value, False by default.
- `is_notnull_constraint_field`: boolean value.
- `default_value`: (optional) anything that can be converted to type_name type. None (Null) by default.
- `precision`:  (optional) decimal precision: total number of digits in decimal value. Defaults to -1 (use cluster default). Ignored for non-decimal SQL types (other than java.math.BigDecimal).
- `scale`: (optional) decimal precision: number of digits after the decimal point. Defaults to -1 (use cluster default). Ignored for non-decimal SQL types.

#### Query Indexes

Query indexes define the fields that will be indexed.

- `index_name`: index name.
- `index_type`: index type code as an integer value in unsigned byte range.
- `inline_size`: integer value.
- `fields`: a list of 0 or more indexed fields (see Fields).

#### Fields

- `name`: field name.
- `is_descending`: (optional) boolean value; False by default.

#### Cache key

- `type_name`: name of the complex object.
- `affinity_key_field_name`: name of the affinity key field.

## Using Key-Value API

The `pygridgain.cache.Cache` class provides methods for working with cache entries by using key-value operations, such as put, get, put all, get all, replace, and others.
The following example shows how to do that:

```python
from pygridgain import Client

client = Client()
client.connect('127.0.0.1', 10800)

# Create cache
my_cache = client.create_cache('my cache')

# Put value in cache
my_cache.put('my key', 42)

# Get value from cache
result = my_cache.get('my key')
print(result)  # 42

result = my_cache.get('non-existent key')
print(result)  # None

# Get multiple values from cache
result = my_cache.get_all([
    'my key',
    'non-existent key',
    'other-key',
])
print(result)  # {'my key': 42}
```

### Using type hints

The pygridgain methods that deal with a single value or key have an additional optional parameter, either `value_hint` or `key_hint`, that accepts a parser/constructor class.
Nearly any structure element (inside dict or list) can be replaced with a 2-tuple `(the element, type hint)`.

```python
from pygridgain import Client
from pygridgain.datatypes import CharObject, ShortObject

client = Client()
client.connect('127.0.0.1', 10800)

my_cache = client.get_or_create_cache('my cache')

my_cache.put('my key', 42)
# Value ‘42’ takes 9 bytes of memory as a LongObject

my_cache.put('my key', 42, value_hint=ShortObject)
# Value ‘42’ takes only 3 bytes as a ShortObject

my_cache.put('a', 1)
# ‘a’ is a key of type String

my_cache.put('a', 2, key_hint=CharObject)
# Another key ‘a’ of type CharObject is created

value = my_cache.get('a')
print(value)  # 1

value = my_cache.get('a', key_hint=CharObject)
print(value)  # 2

# Now let us delete both keys at once
my_cache.remove_keys([
    'a',  # a default type key
    ('a', CharObject),  # a key of type CharObject
])
```

### Transactions

Client transactions are supported for caches with `CacheAtomicityMode.TRANSACTIONAL` mode.

#### Executing Transactions

To start a transaction, obtain the `ClientTransactions` object from `IgniteClient`.
`ClientTransactions` has a number of  `txStart(...)` methods, each of which starts a new transaction and returns an object (`ClientTransaction`) that represents the transaction.
Use this object to commit or rollback the transaction.

```python
client = Client()
with client.connect('127.0.0.1', 10800):
    cache = client.get_or_create_cache({
        PROP_NAME: 'tx_cache',
        ROP_CACHE_ATOMICITY_MODE: CacheAtomicityMode.TRANSACTIONAL
    })

    # starting transaction
    key = 1
    with client.tx_start(timeout=2000, label='tx-sync') as tx:
        cache.put(key, 'success')
        tx.commit()
```

#### Transaction Configuration

Client transactions can have different [concurrency modes, isolation levels](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/key-value-api/transactions#concurrency-modes-and-isolation-levels), and execution timeout, which can be set for all transactions or on a per transaction basis.

The `ClientConfiguration` object supports setting the default concurrency mode, isolation level, and timeout for all transactions started with this client interface.

```python
//Add a configuration example here
```

You can specify the concurrency mode, isolation level, and timeout when starting an individual transaction.
In this case, the provided values override the default settings.

```python
client = Client()
with client.connect('127.0.0.1', 10800):
    cache = client.get_or_create_cache({
        PROP_NAME: 'tx_cache',
        ROP_CACHE_ATOMICITY_MODE: CacheAtomicityMode.TRANSACTIONAL
    })

    # starting transaction
    key = 1
    with client.tx_start(
            isolation=TransactionIsolation.REPEATABLE_READ,
            concurrency=TransactionConcurrency.PESSIMISTIC
    ) as tx:
        cache.put(key, 'success')
        tx.commit()
```

## Scan Queries

The `scan()` method of the cache object can be used to get all objects from the cache. It returns a generator that yields `(key,value)` tuples. You can iterate through the generated pairs as follows:

```python
from pygridgain import Client

client = Client()
client.connect('127.0.0.1', 10800)

my_cache = client.create_cache('myCache')

my_cache.put_all({'key_{}'.format(v): v for v in range(20)})
# {
#     'key_0': 0,
#     'key_1': 1,
#     'key_2': 2,
#     ... 20 elements in total...
#     'key_18': 18,
#     'key_19': 19
# }

result = my_cache.scan()

for k, v in result:
    print(k, v)
# 'key_17' 17
# 'key_10' 10
# 'key_6' 6,
# ... 20 elements in total...
# 'key_16' 16
# 'key_12' 12


```

Alternatively, you can convert the generator to a dictionary in one go:

```python
result = my_cache.scan()
print(dict(result))
# {
#     'key_17': 17,
#     'key_10': 10,
#     'key_6': 6,
#     ... 20 elements in total...
#     'key_16': 16,
#     'key_12': 12
# }
```

{% hint style="info" %}
Be cautious: if the cache contains a large set of data, the dictionary may consume too much memory!
{% endhint %}

## Vector Queries

The `vector()` method of the cache object can be used to search the vector index of the cache. It returns a cursor object that can be used to parse the results normally.

To start using vector queries:

- Make sure your GridGain license provides access to vector search feature.
- Enable the optional  `gridgain-vector-query` [module](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/setup#enabling-modules) in GridGain.

Below is the example of creating a vector index:

```python
from pygridgain.datatypes.cache_config import IndexType

'query_indexes': [
    {
        'index_name': 'vec',
        'index_type': IndexType.VECTOR,
        'inline_size': 1024,
        'fields': [
            {
                'name': 'vector_field'
            }
        ]
    }
]
```

### Vector Index Parameters

Starting with version 1.7.0, a vector index accepts the following optional keys. They require GridGain 8.10.0 or later. If the cluster does not support a parameter that you set, the client raises `NotSupportedByClusterError` instead of creating the index without it. If you set one of these keys on an index that is not a vector index, the client raises `ValueError`.

| Key | Values (default) | Description |
| --- | --- | --- |
| `hnsw_m` | 1–512 (`0`, engine default) | Number of graph connections for each vector in the HNSW graph. A higher value improves recall and costs graph memory and build time. Changing it requires an index rebuild. |
| `hnsw_ef_construction` | 1–3200 (`0`, engine default) | Build-time beam width: how many candidates the engine keeps while it chooses the connections of each vector. A higher value costs build time but no extra index memory. Changing it requires an index rebuild. |
| `quantization` | A `VectorQuantization` value (`ENGINE_DEFAULT`) | How the index stores vectors: `NONE` (full precision), `INT8` (one byte per dimension), or `BINARY` (one bit per dimension, requires the Lucene 10 vector module on the cluster). `ENGINE_DEFAULT` leaves the choice to the node. |
| `max_segments` | 1–1024 (`0`, engine default) | Target maximum number of index segments. A query searches one graph per segment, so fewer segments answer faster, but merging the index down to them costs more. |
| `query_threads` | 1–64 (`0`, engine default) | Number of threads that search the segments of the index concurrently for one query. |

For details about these settings, see [Vector Search](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/vector).

```python
from pygridgain.datatypes.cache_config import IndexType, VectorQuantization

'query_indexes': [
    {
        'index_name': 'vec',
        'index_type': IndexType.VECTOR,
        'inline_size': 1024,
        'fields': [{'name': 'vector_field'}],
        'hnsw_m': 32,
        'hnsw_ef_construction': 200,
        'quantization': VectorQuantization.INT8,
    }
]
```

### Running Vector Queries

If the cache has the vector index, use the vector from your model in the query:

```python
query_vector = # Get from your model
cursor = cache.vector(type_name=Article.type_name, field='vector_field', clause_vector=query_vector, k=1, threshold=0)
```

The `vector()` method takes the following parameters:

| Parameter | Description |
| --- | --- |
| `type_name` | Name of the type. |
| `field` | Name of the vector field. |
| `clause_vector` | The search vector. Any sequence of floats works. A NumPy array of dtype `'<f4'` is sent without conversion, which is the fastest option. |
| `k` | Number of nearest vectors to return. Must be positive; otherwise the client raises `ValueError`. The cluster also limits it (10000 by default). |
| `threshold` | Similarity threshold. `0` or a negative value disables it. |
| `page_size` | Optional. Number of rows in one response page. Defaults to `k`, so the whole result arrives in one page. |
| `ef_search` | Optional. Search beam width: how many candidate vectors the engine keeps while it walks the index graph. A value wider than `k` improves recall and increases latency. A value below `k` is treated as `k`. `0` (the default) uses the engine default. |
| `with_scores` | Optional. If `True`, each row includes the similarity score. Scores are raw engine values: they depend on the similarity function and are not normalized. |
| `no_content` | Optional. If `True`, rows do not include values. This is the smallest response. |
| `field_filter` | Optional. A dictionary of field names and values. The query returns only entries whose fields equal all the given values. See [Filtering Vector Queries](#filtering-vector-queries). |
| `oversample` | Optional. A non-negative integer. Applies only to an index that stores `BINARY` codes: the engine searches at least `k` × `oversample` candidates and re-scores them at full precision. `0` (the default) leaves it unset. |

The shape of the result rows depends on the flags:

| Flags | Row |
| --- | --- |
| None | `(key, value)` |
| `with_scores=True` | `(key, value, score)` |
| `no_content=True` | `key` |
| `with_scores=True, no_content=True` | `(key, score)` |

`ef_search`, `with_scores`, `no_content`, `field_filter`, and `oversample` were added in version 1.7.0 and require GridGain 8.10.0 or later. If the cluster does not support them, the client raises `NotSupportedByClusterError`. A query that does not use them works with earlier GridGain versions.

{% hint style="info" %}
Starting with version 1.7.0, `page_size` defaults to `k`. Earlier versions used a page size of 1, which made one server round trip for each result row. To keep a smaller page, set `page_size` explicitly.
{% endhint %}

```python
cursor = cache.vector(
    type_name=Article.type_name,
    field='vector_field',
    clause_vector=query_vector,
    k=10,
    threshold=0,
    ef_search=100,
    with_scores=True,
)
for key, value, score in cursor:
    print(key, score)
```

### Filtering Vector Queries

Use `field_filter` to restrict a query to entries with given field values. GridGain applies the filter while it searches the index, so the query returns `k` matching entries, not the `k` nearest entries of which only some match. For example, one index can serve several tenants, with one filter for each tenant.

```python
cursor = cache.vector(
    type_name=Article.type_name,
    field='vector_field',
    clause_vector=query_vector,
    k=10,
    threshold=0,
    field_filter={'tenant': 'acme'},
)
```

The filter works as follows:

- An entry matches when every field in the filter equals its value.
- The filter can only use fields of the text (`FULLTEXT`) index of the type. If a field is not indexed, the cluster rejects the query and the client raises `CacheError`.
- A value can be a `str`, `int`, `float`, `bool`, `Decimal`, `UUID`, `datetime`, `date`, or a `(datetime, nanos)` tuple. For any other value, including `None`, or for an empty field name, the client raises `ValueError` before it sends the query.
- The cluster compares the text forms of the values, so the value must match the Java type of the stored field. A `datetime` or `date` matches a `java.util.Date` field, to the second. For a `java.sql.Timestamp` field, use the `(datetime, nanos)` tuple.
- A `Decimal` keeps its scale: `Decimal('12.50')` does not match a stored `12.5`. The client stores decimals in normalized form, so filter values that this client wrote by their normalized form.

## Executing SQL Statements

The Python thin client supports all [SQL commands](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/sql-reference-overview) that are supported by GridGain.
The commands are executed via the `sql()` method of the cache object.
The `sql()` method returns a generator that yields the resulting rows.

{% hint style="info" %}
For high-load environments, use `pyodbc` module as described in [ODBC](../sql/odbc/odbc-driver.md#using-pyodbc).
{% endhint %}

Refer to the [SQL Reference](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/sql-reference-overview) section for the list of supported commands.

```python
from pygridgain import Client

client = Client()
client.connect('127.0.0.1', 10800)

CITY_CREATE_TABLE_QUERY = '''CREATE TABLE City (
    ID INT(11),
    Name CHAR(35),
    CountryCode CHAR(3),
    District CHAR(20),
    Population INT(11),
    PRIMARY KEY (ID, CountryCode)
) WITH "affinityKey=CountryCode"'''

client.sql(CITY_CREATE_TABLE_QUERY)

CITY_CREATE_INDEX = '''CREATE INDEX idx_country_code ON city (CountryCode)'''

client.sql(CITY_CREATE_INDEX)

CITY_INSERT_QUERY = '''INSERT INTO City(
    ID, Name, CountryCode, District, Population
) VALUES (?, ?, ?, ?, ?)'''

CITY_DATA = [
    [3793, 'New York', 'USA', 'New York', 8008278],
    [3794, 'Los Angeles', 'USA', 'California', 3694820],
    [3795, 'Chicago', 'USA', 'Illinois', 2896016],
    [3796, 'Houston', 'USA', 'Texas', 1953631],
    [3797, 'Philadelphia', 'USA', 'Pennsylvania', 1517550],
    [3798, 'Phoenix', 'USA', 'Arizona', 1321045],
    [3799, 'San Diego', 'USA', 'California', 1223400],
    [3800, 'Dallas', 'USA', 'Texas', 1188580],
]

for row in CITY_DATA:
    client.sql(CITY_INSERT_QUERY, query_args=row)

CITY_SELECT_QUERY = "SELECT * FROM City"

cities = client.sql(CITY_SELECT_QUERY)
for city in cities:
    print(*city)

```

The `sql()` method returns a generator that yields the resulting rows.

Note that if you set the `include_field_names` argument to `True`, the `sql()` method will generate a list of column names in the first yield. You can access the field names using the `next` function of Python.

```python
field_names = client.sql(CITY_SELECT_QUERY, include_field_names=True).__next__()
print(field_names)
```

## Security

### SSL/TLS

To use encrypted communication between the thin client and the cluster, you have to enable SSL/TLS both in the cluster configuration and the client configuration.
Refer to the [Enabling SSL/TLS for Thin Clients](getting-started-with-thin-clients.md#enabling-ssl-tls-for-thin-clients) section for the instruction on the cluster configuration.

Here is an example configuration for enabling SSL in the thin client:

```python
from pygridgain import Client
import ssl

client = Client(
                use_ssl=True,
                ssl_cert_reqs=ssl.CERT_REQUIRED,
                ssl_keyfile='/path/to/key/file',
                ssl_certfile='/path/to/client/cert',
                ssl_ca_certfile='/path/to/trusted/cert/or/chain',
)

client.connect('localhost', 10800)
```

{% hint style="info" %}
Starting with version 1.7.0, the client uses TLS 1.3 or later by default. To connect to a cluster that supports only TLS 1.2, set `ssl_version=ssl.TLSVersion.TLSv1_2`. The client does not check the server host name.
{% endhint %}

Supported parameters:

| Parameter | Description |
| --- | --- |
| `use_ssl` | Set to True to enable SSL/TLS on the client. |
| `ssl_keyfile` | Path to the file containing the SSL key. |
| `ssl_certfile` | Path to the file containing the SSL certificate. |
| `ssl_ca_certfile` | The path to the file with trusted certificates. |
| `ssl_cert_reqs` | `ssl.CERT_NONE` − remote certificate is ignored (default),<br>`ssl.CERT_OPTIONAL` − remote certificate will be validated, if provided,<br>`ssl.CERT_REQUIRED` − valid remote certificate is required, |
| `ssl_version` | The minimum TLS version, as an `ssl.TLSVersion` value. The default is `ssl.TLSVersion.TLSv1_3`. To connect to a cluster that supports only TLS 1.2, set it to `ssl.TLSVersion.TLSv1_2`. The legacy `ssl.PROTOCOL_TLSv1_2`, `ssl.PROTOCOL_TLSv1_1`, and `ssl.PROTOCOL_TLSv1` constants are also accepted and allow only that TLS version. |
| `ssl_ciphers` | The cipher list in the OpenSSL cipher list format. The default is the Python default cipher list. This parameter does not apply to TLS 1.3. |

### Authentication

Configure [authentication on the cluster side](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication) and provide a valid user name and password in the client configuration.

```python
from pygridgain import Client
import ssl


client = Client(
                ssl_cert_reqs=ssl.CERT_REQUIRED,
                ssl_keyfile='/path/to/key/file',
                ssl_certfile='/path/to/client/cert',
                ssl_ca_certfile='/path/to/trusted/cert/or/chain',
                username='ignite',
                password='ignite',)

client.connect('localhost', 10800)
```

Note that supplying credentials automatically turns SSL on.
This is because sending credentials over an insecure channel is not a best practice and is strongly discouraged.
If you still want to use authentication without securing the connection, simply disable SSL when creating the client object:

```python
client = Client(username='ignite', password='ignite', use_ssl=False)
```

### Authorization

For information about authorizing thin client connections, see the [Client Authorization](authorization.md) page.
