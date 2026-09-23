---
description: >-
  Connect to a GridGain 9 cluster with the C++ client, covering the client
  connector configuration, timeouts and retry policies, authentication, object
  serialization, and the SQL and table APIs.
---

# C++ Client

GridGain 9 clients connect to the cluster via a standard socket connection. Unlike GridGain 2.x, there is no separate Thin and Thick clients in GridGain 9. All clients are 'thin'.

Clients do not become a part of the cluster topology, never hold any data, and are not used as a destination for compute calculations.

## Supported Platforms

The C++ client is distributed as a pre-built binary for the following platforms:

- Linux x86-64,
- Windows using MSVC toolchain versions 2017, 2019 and 2022

## Getting Started

### Installation

[Download](https://www.gridgain.com/tryfree) the client and unpack it. Then, add it to your project.

## Client Connector Configuration

Client connection parameters are controlled by the client connector configuration. By default, GridGain accepts client connections on port 10800. You can change the configuration for the node by using the [CLI tool](../../ignite-cli-tool.md) at any time.

Here is how the client connector configuration looks like in the JSON format.

{% hint style="info" %}
In GridGain 9, you can create and maintain the configuration in either JSON or HOCON format.
{% endhint %}

```json
"ignite" : {
  "clientConnector" : {
    "port" : 10800,
    "idleTimeoutMillis" :3000,
    "sendServerExceptionStackTraceToClient" : true,
    "ssl" : {
      "enabled" : true,
      "clientAuth" : "require",
      "keyStore" : {
        "path" : "KEYSTORE_PATH",
        "password" : "SSL_STORE_PASS"
      },
      "trustStore" : {
        "path" : "TRUSTSTORE_PATH",
        "password" : "SSL_STORE_PASS"
      },
    },
  },
}
```

The table below covers the configuration for client connector:

| Property | Default | Description |
| --- | --- | --- |
| connectTimeoutMillis | 5000 | Connection attempt timeout, in milliseconds. |
| idleTimeoutMillis | 0 | How long the client can be idle before the connection is dropped, in milliseconds. By default, there is no limit. |
| metricsEnabled | `false` | Defines if client metrics are collected. |
| port | 10800 | The port the client connector will be listening to. |
| sendServerExceptionStackTraceToClient | `false` | Defines if cluster exceptions are sent to the client. |
| ssl.ciphers | | The cipher used for SSL communication. |
| ssl.clientAuth | | Type of client authentication used by clients. For more information, see [SSL/TLS](../../administrators-guide/security/ssl-tls.md). |
| ssl.enabled | | Defines if SSL is enabled. |
| ssl.keyStore.password | | SSL keystore password. |
| ssl.keyStore.path | | Path to the SSL keystore. |
| ssl.keyStore.type | `PKCS12` | The type of SSL keystore used. |
| ssl.trustStore.password | | SSL keystore password. |
| ssl.trustStore.path | | Path to the SSL keystore. |
| ssl.trustStore.type | `PKCS12` | The type of SSL keystore used. |

Here is how you can change the parameters:

```bash
node config update ignite.clientConnector.port=10469
```

## Connecting to Cluster

To initialize a client, use the `IgniteClient` class, and provide it with the configuration:

{% code title="C++" %}
```cpp
using namespace ignite;

ignite_client_configuration cfg{"127.0.0.1"};
auto client = ignite_client::start(cfg, std::chrono::seconds(5));
```
{% endcode %}

### Using Dependency Injection

GridGain client provides support for using [Dependency Injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection) when initializing a client instance.

This approach can be used to simplify initializing the client in DI containers:

- Register the `IgniteClientGroup` in your DI container:

  ```cpp
  builder.Services.AddSingleton<IgniteClientGroup>(_ => new IgniteClientGroup(
      new IgniteClientGroupConfiguration
      {
          Size = 3,
          ClientConfiguration = new("localhost"),
      }));
  ```
- Use an instance of the group you created in your methods:

  ```cpp
  public async Task<IActionResult> Index([FromServices] IgniteClientGroup igniteGroup)
  {
      IIgnite ignite = await igniteGroup.GetIgniteAsync();
      var tables = await ignite.Tables.GetTablesAsync();
      return Ok(tables);
  }
  ```

### Operation Timeout

You can configure operation timeout in your client configuration. If configured, an operation will be cancelled if no response is received within the specified time. By default, there is no timeout.

Some APIs may send multiple requests, and each request will have an individual timeout. For example, compute jobs consist of 2 requests - one that submits the job, and another that received the job result. For this kind of job, the real duration may be larger than timeout.

```cpp
ignite_client_configuration cfg{"127.0.0.1"};
cfg.set_operation_timeout(std::chrono::seconds{2});

auto client = ignite_client::start(cfg, std::chrono::seconds(5));
```

### Connect Timeout

When the client opens a connection to a server node, it sends a handshake message. You can limit how long the
client waits for that handshake to complete. If the handshake does not complete in time, the client closes the
connection and can re-connect to the node instead of keeping a socket that never becomes usable.

Every connection performs its own handshake, so the timeout applies per connection. By default there is no
timeout. The timeout covers only the handshake: it does not include establishing the TCP connection or the
TLS connection.

```cpp
ignite_client_configuration cfg{"127.0.0.1"};
cfg.set_connect_timeout(std::chrono::seconds{5});

auto client = ignite_client::start(cfg, std::chrono::seconds(5));
```

{% hint style="info" %}
A negative timeout is rejected with an `ILLEGAL_ARGUMENT` error.
{% endhint %}

### Retry Policy

If an operation fails because the connection to the node is lost, the client can retry it on another connection. You control this behavior with a retry policy.

By default, no retry policy is set and operations are not retried. To enable retries, set a policy in the client configuration:

{% code title="C++" %}
```cpp
ignite_client_configuration cfg{"127.0.0.1"};
cfg.set_retry_policy(std::make_shared<retry_read_policy>());

auto client = ignite_client::start(cfg, std::chrono::seconds(5));
```
{% endcode %}

The client provides the following policies:

| Policy | Description |
| --- | --- |
| `retry_none_policy` | Never retries. This is the same as leaving the retry policy unset. |
| `retry_limit_policy` | Retries an operation up to the configured number of times. The default limit is 16. Pass 0 to the constructor to disable retries, or a negative value for unlimited retries, for example `std::make_shared<retry_limit_policy>(5)`. |
| `retry_read_policy` | Retries only the operations that do not modify data, up to the configured limit: `TABLES_GET`, `TABLE_GET`, `TUPLE_GET`, `TUPLE_GET_ALL` and `TUPLE_CONTAINS_KEY`. Write, SQL and compute operations are not retried. |

Regardless of the policy, the client never retries:

- operations performed in an explicit transaction;
- operations that are bound to a specific connection, for example fetching the next page of an SQL cursor, or scanning a partition for a continuous query.

When all retries permitted by the policy are exhausted, the operation fails with a connection error that reports the last error encountered.

#### Custom Retry Policies

To define your own policy, implement the `retry_policy` interface and return `true` from `should_retry()` when the operation should be retried.
The `retry_context` argument provides the operation type, the number of retries already performed, and the last error:

{% code title="C++" %}
```cpp
class my_retry_policy : public retry_policy {
public:
    [[nodiscard]] bool should_retry(const retry_context &ctx) const override {
        return ctx.operation() == client_operation_type::TUPLE_GET && ctx.iteration() < 3;
    }
};
```
{% endcode %}

The iteration counter is zero-based: it is 0 on the first retry decision. If `should_retry()` throws an exception, the operation fails with that exception and no further retries are attempted.

## Authentication

To pass authentication information, pass it to `IgniteClient` builder:

{% code title="C++" %}
```cpp
auto authenticator = std::make_shared<ignite::basic_authenticator>("myUser", "myPassword");

ignite::ignite_client_configuration cfg{"127.0.0.1:10800"};
cfg.set_authenticator(authenticator);
auto client = ignite_client::start(std::move(cfg), std::chrono::seconds(30));
```
{% endcode %}

## User Object Serialization

GridGain supports mapping user objects to table tuples. This ensures that objects created in any programming language can be used for key-value operations directly.

### Limitations

There are limitations to user types that can be used for such a mapping. Some limitations are common, and others are platform-specific due to the programming language used.

- Only flat field structure is supported, meaning no nesting user objects. This is because Ignite tables, and therefore tuples have flat structure themselves;
- Fields should be mapped to Ignite types;
- All fields in user type should either be mapped to Table column or explicitly excluded;
- All columns from Table should be mapped to some field in the user type;
- **C++ only**: User has to provide marshalling functions explicitly as there is no reflection to generate them based on user type structure.

### Usage Examples

{% code title="C++" %}
```cpp
struct account {
  account() = default;
  account(std::int64_t id) : id(id) {}
  account(std::int64_t id, std::int64_t balance) : id(id), balance(balance) {}

  std::int64_t id{0};
  std::int64_t balance{0};
};

namespace ignite {

  template<>
  ignite_tuple convert_to_tuple(account &&value) {
    ignite_tuple tuple;

    tuple.set("id", value.id);
    tuple.set("balance", value.balance);

    return tuple;
  }

  template<>
  account convert_from_tuple(ignite_tuple&& value) {
    account res;

    res.id = value.get<std::int64_t>("id");

    // Sometimes only key columns are returned, i.e. "id",
    // so we have to check whether there are any other columns.
    if (value.column_count() > 1)
      res.balance = value.get<std::int64_t>("balance");

    return res;
  }

} // namespace ignite
```
{% endcode %}

## SQL API

GridGain 9 is focused on SQL, and SQL API is the primary way to work with the data. You can read more about supported SQL statements in the [SQL Reference](../../sql-reference/ddl.md) section. Here is how you can send SQL requests:

{% code title="C++" %}
```cpp
result_set result = client.get_sql().execute(nullptr, {"select name from tbl where id = ?"}, {std::int64_t{42});
std::vector<ignite_tuple> page = result_set.current_page();
ignite_tuple& row = page.front();
```
{% endcode %}

### SQL Scripts

The default API executes SQL statements one at a time. If you want to execute large SQL statements, pass them to the `executeScript()` method. These statements will be executed in order.

{% code title="C++" %}
```cpp
std::string script = ""
	+ "CREATE TABLE IF NOT EXISTS Person (id int primary key, city_id int, name varchar, age int, company varchar);"
	+ "INSERT INTO Person (1,3, 'John', 43, 'Sample')";

client.get_sql().execute_script(script);
```
{% endcode %}

{% hint style="info" %}
Execution of each statement is considered complete when the first page is ready to be returned. As a result, when working with large data sets, SELECT statement may be affected by later statements in the same script.
{% endhint %}

## Transactions

All table operations in GridGain 9 are transactional. You can provide an explicit transaction as a first argument of any Table and SQL API call. If you do not provide an explicit transaction, an implicit one will be created for every call.

Here is how you  can provide a transaction explicitly:

{% code title="C++" %}
```cpp
auto accounts = table.get_key_value_view<account, account>();

account init_value(42, 16'000);
accounts.put(nullptr, {42}, init_value);

auto tx = client.get_transactions().begin();

std::optional<account> res_account = accounts.get(&tx, {42});
res_account->balance += 500;
accounts.put(&tx, {42}, res_account);

assert(accounts.get(&tx, {42})->balance == 16'500);

tx.rollback();

assert(accounts.get(&tx, {42})->balance == 16'000);
```
{% endcode %}

## Table API

To execute table operations on a specific table, you need to get a specific view of the table and use one of its methods. You can only create new tables by using SQL API.

When working with tables, you can use built-in Tuple type, which is a set of key-value pairs underneath, or map the data to your own types for a strongly-typed access. Here is how you can work with tables:

### Getting a Table Instance

First, get an instance of the table. To obtain an instance of table, use the `IgniteTables.table(String)` method. You can also use `IgniteTables.tables()` method to list all existing tables.

{% code title="C++" %}
```cpp
using namespace ignite;

auto table_api = client.get_tables();
std::vector<table> existing_tables = table_api.get_tables();
table first_table = existing_tables.front();

std::optional<table> my_table = table_api.get_table("MY_TABLE);
```
{% endcode %}

### Basic Table Operations

Once you've got a table you need to get a specific view to choose how you want to operate table records.

#### Tuple Record View

A tuple record view. It can be used to operate table tuples directly.

{% code title="C++" %}
```cpp
record_view<ignite_tuple> view = table.get_record_binary_view();

ignite_tuple record{
  {"id", 42},
  {"name", "John Doe"}
};

view.upsert(nullptr, record);
std::optional<ignite_tuple> res_record = view.get(nullptr, {"id", 42});

assert(res_record.has_value());
assert(res_record->column_count() == 2);
assert(res_record->get<std::int64_t>("id") == 42);
assert(res_record->get<std::string>("name") == "John Doe");
```
{% endcode %}

#### Record View

A record view mapped to a user type. It can be used to operate table using user objects which are mapped to table tuples.

{% code title="C++" %}
```cpp
record_view<person> view = table.get_record_view<person>();

person record(42, "John Doe");

view.upsert(nullptr, record);
std::optional<person> res_record = view.get(nullptr, person{42});

assert(res.has_value());
assert(res->id == 42);
assert(res->name == "John Doe");
```
{% endcode %}

#### Key-Value Tuple View

A tuple key-value view. It can be used to operate table using key and value tuples separately.

{% code title="C++" %}
```cpp
key_value_view<ignite_tuple, ignite_tuple> kv_view = table.get_key_value_binary_view();

ignite_tuple key_tuple{{"id", 42}};
ignite_tuple val_tuple{{"name", "John Doe"}};

kv_view.put(nullptr, key_tuple, val_tuple);
std::optional<ignite_tuple> res_tuple = kv_view.get(nullptr, key_tuple);

assert(res_tuple.has_value());
assert(res_tuple->column_count() == 2);
assert(res_tuple->get<std::int64_t>("id") == 42);
assert(res_tuple->get<std::string>("name") == "John Doe");
```
{% endcode %}

#### Key-Value View

A key-value view with user objects. It can be used to operate table using key and value user objects mapped to table tuples.

{% code title="C++" %}
```cpp
key_value_view<person, person> kv_view = table.get_key_value_view<person, person>();

kv_view.put(nullptr, {42}, {"John Doe"});
std::optional<person> res = kv_view.get(nullptr, {42});

assert(res.has_value());
assert(res->id == 42);
assert(res->name == "John Doe");
```
{% endcode %}
