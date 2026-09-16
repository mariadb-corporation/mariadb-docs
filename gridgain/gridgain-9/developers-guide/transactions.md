---
description: >-
  Perform explicit and implicit transactions in GridGain 9 — lifecycle,
  isolation, read-only transactions, timeouts, labels, and runInTransaction.
---

# Performing Transactions

All queries in GridGain 9 are transactional. You can provide an explicit transaction as a first argument of any Table and SQL API call. If you do not provide an explicit transaction, an implicit one will be created for every call.

{% hint style="info" %}
The Java examples on this page use the thin client, which requires the `ignite-client` module. For repository and dependency configuration, see [Project Setup and Required Modules](project-setup.md).
{% endhint %}

## Transaction Lifecycle

Thin client transactions start lazily.
Creating a transaction sends nothing to the cluster: the transaction begins on the server when you perform the first operation in it.
Until then, it holds no locks and consumes no cluster resources.

The *transaction coordinator* is chosen when the transaction begins, that is, when you perform that first operation. The coordinator finds the required [partitions](../administrators-guide/storage/data-partitions.md) and sends the read or write requests to the nodes holding primary partitions. For correct transaction operation, all nodes in cluster must have similar time, that can be different by no more than `schemaSync.maxClockSkewMillis`.

Lazy start has two consequences to plan for:

- Connection and cluster errors surface on the first operation in the transaction, not when you create it.
- Committing or rolling back a transaction that was never used sends no request and reports success.

If the key is not locked by a different transaction, the node gets the locks on the involved keys, and attempts to apply the changes in the transaction. When the operation finishes, the lock is removed. This way, several transactions can work on the same partition, while changing separate keys. Additionally, some operations may perform *short-term* locks on the keys in advance, to ensure operations proceed correctly.

If the node with primary replica of the partition involved in the transaction fail, the transaction is eventually automatically rolled back. GridGain will return `TransactionException` on commit attempt.

## Transaction Isolation and Concurrency

All read-write transactions in GridGain acquire locks during the first read or write access, and hold the lock until the transaction is committed or rolled back. All read-write transactions are `SERIALIZABLE`, so as long as the lock persists, no other transaction can make changes to locked data, however data can still be read by [Read-Only Transactions](#read-only-transactions).

### Deadlock Prevention

GridGain 9 uses the `WOUND_WAIT` deadlock prevention algorithm. When a transaction requests data that is already locked by a newer (younger) transaction, the newer transaction is cancelled and retried, so that the older transaction can proceed. When a transaction requests data locked by an older transaction, it waits for the lock to be freed.

## Executing Transactions

Here is how you  can provide a transaction explicitly:

{% tabs %}
{% tab title="Java" %}
```java
KeyValueView<Long, Account> accounts =
  table.keyValueView(Mapper.of(Long.class), Mapper.of(Account.class));

accounts.put(null, 42, new Account(16_000));

Transaction tx = client.transactions().begin();

Account account = accounts.get(tx, 42);
account.balance += 500;
accounts.put(tx, 42, account);

assert accounts.get(tx, 42).balance == 16_500;

tx.rollback();

assert accounts.get(tx, 42).balance == 16_000;
```
{% endtab %}

{% tab title=".NET" %}
```csharp
var accounts = table.GetKeyValueView<long, Account>();
await accounts.PutAsync(transaction: null, 42, new Account(16_000));

await using ITransaction tx = await client.Transactions.BeginAsync();

(Account account, bool hasValue) = await accounts.GetAsync(tx, 42);
account = account with { Balance = account.Balance + 500 };

await accounts.PutAsync(tx, 42, account);

Debug.Assert((await accounts.GetAsync(tx, 42)).Value.Balance == 16_500);

await tx.RollbackAsync();

Debug.Assert((await accounts.GetAsync(null, 42)).Value.Balance == 16_000);

public record Account(decimal Balance);
```
{% endtab %}

{% tab title="C++" %}
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
{% endtab %}
{% endtabs %}

## Transaction Management

You can also manage transactions by using the `runInTransaction` [method](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/tx/IgniteTransactions.html#runInTransaction(java.util.function.Consumer)). When using it, the following will be done automatically:

- The transaction is started and substituted to the closure.
- The transaction is committed if no exceptions were thrown during the closure.
- The transaction will be retried in case of recoverable error. Closure must be purely functional - not causing side effects.

You can run transactions both synchronously and asynchronously.

This example shows how to update an account’s balance synchronously:

{% code title="Java" %}
```java
client.transactions().runInTransaction(tx -> {
    Account acct = accounts.get(tx, key);
    if (acct != null) {
        acct.balance += 200.0d;
    }
    accounts.put(tx, key, acct);
});
```
{% endcode %}

And this example performs the same logic in an asynchronous manner:

{% code title="Java" %}
```java
CompletableFuture<Void> future = client.transactions().runInTransactionAsync(tx ->
        accounts.getAsync(tx, key)
                .thenCompose(acct -> {
                    acct.balance += 300.0d;
                    return accounts.putAsync(tx, key, acct);
                })
);
future.join();
```
{% endcode %}

## Read-Only Transactions

When starting a transaction, you can configure the transaction as a *read-only* transaction. In these transactions, no data modification can be performed, but they also do not secure locks and can be performed on non-primary [partitions](../administrators-guide/storage/data-partitions.md), further improving their performance. Read-only transactions always check the data for the moment they were started, even if new data was written to the database. The read timestamp is fixed when you create the transaction, not when its first operation runs.

Here is how you can make a read-only transaction:

{% tabs %}
{% tab title="Java" %}
```java
var tx = client.transactions().begin(new TransactionOptions().readOnly(true));
int balance = accounts.get(tx, 42).balance;
tx.commit();
```
{% endtab %}

{% tab title=".NET" %}
```csharp
await using var tx = await client.Transactions.BeginAsync(
    new TransactionOptions { ReadOnly = true });
var account = await accounts.GetAsync(tx, 42);
int balance = account.Value.Balance;
await tx.CommitAsync();
```
{% endtab %}

{% tab title="C++" %}
```cpp
auto tx_opts = transaction_options()
        .set_read_only(true);

auto tx = m_client.get_transactions().begin(tx_opts);

record_view.get(&tx, 42);

tx.commit();
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Read-only transactions read data at a specific time. If new data was written since, old data will still be stored in [Version Storage](../administrators-guide/storage/data-partitions.md#version-storage) and will be available until low watermark. If low watermark is reached during the transaction, data will be kept available until it is over.
{% endhint %}

## Transaction Timeout

In certain scenarios, it is preferable to drop the transaction if it is taking too long. When the timeout is reached, the transaction is automatically rolled back.

Here is how you can configure transaction timeout:

{% tabs %}
{% tab title="Java" %}
```java
KeyValueView<Long, Account> accounts =
  table.keyValueView(Mapper.of(Long.class), Mapper.of(Account.class));

var tx = client.transactions().begin(new TransactionOptions().timeoutMillis(10000));
accounts.put(tx, 42, account);
tx.commit();
```
{% endtab %}

{% tab title=".NET" %}
```csharp
await using var tx = await Client.Transactions.BeginAsync(
    new TransactionOptions { TimeoutMillis = 10_000 });
await accounts.PutAsync(tx, 42, account);
await tx.CommitAsync();
```
{% endtab %}

{% tab title="C++" %}
```cpp
auto accounts = table.get_key_value_view<account, account>();

auto tx_opts = transaction_options()
       .set_timeout_millis(10000);

auto tx = m_client.get_transactions().begin(tx_opts);

record_view.insert(&tx, 42);

tx.commit();
```
{% endtab %}
{% endtabs %}

## Transaction Labels

You can assign custom labels to transactions to help identify and track them. Once set, a transaction label remains unchanged for the lifetime of the transaction and is propagated across all nodes involved in the transaction.

Here is how you can set a transaction label:

{% tabs %}
{% tab title="Java" %}
```java
KeyValueView<Long, Account> accounts =
  table.keyValueView(Mapper.of(Long.class), Mapper.of(Account.class));

var tx = client.transactions().begin(
    new TransactionOptions().label("ACCOUNT_UPDATE_TX"));

accounts.put(tx, 42, account);
tx.commit();
```
{% endtab %}

{% tab title=".NET" %}
```csharp
await using var tx = await Client.Transactions.BeginAsync(
    new TransactionOptions { Label = "ACCOUNT_UPDATE_TX" });

await accounts.PutAsync(tx, 42, account);
await tx.CommitAsync();
```
{% endtab %}

{% tab title="C++" %}
```cpp
auto accounts = table.get_key_value_view<account, account>();

auto tx_opts = transaction_options()
       .set_label("ACCOUNT_UPDATE_TX");

auto tx = m_client.get_transactions().begin(tx_opts);

record_view.insert(&tx, 42);

tx.commit();
```
{% endtab %}
{% endtabs %}

Transaction label will be visible in:

- **Log messages** - When transactions timeout, fail, or produce warnings, the label is included in log output for easy identification
- **System views** - Labels are visible in transaction system views for monitoring active and historical transactions
- **Diagnostic outputs** - Labels help correlate transaction activity across distributed nodes
