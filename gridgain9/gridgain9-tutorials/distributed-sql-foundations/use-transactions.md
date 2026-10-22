---
description: >-
  Group multiple SQL operations into atomic units that either commit together or roll back. Master explicit, managed, and async transaction patterns in Java.
---

# Use Transactions in GridGain 9

<!-- TODO (low): The "Java 17 or later" prerequisite is the tutorial's own choice. The GridGain 9.1.28 client is built for Java 11. Compiled with `javac --release 11`, the samples on this page build without errors. Decide whether to keep "Java 17" (one prerequisite for the whole tutorial series) or say "Java 11 or later" on the pages whose samples allow it, then delete this comment. -->

## Introduction

Every operation in [Work with RecordView and KeyValueView](recordview-keyvalueview.md) passed `null` as the transaction parameter. That `null` tells GridGain to wrap each operation in its own auto-commit transaction: each write commits independently, and there is no coordination between them. When you need multiple operations to succeed or fail together (creating an invoice with its line items, transferring funds between accounts, updating inventory and confirming an order), you replace `null` with a named `Transaction` object.

This tutorial builds a music store invoice workflow that writes to two tables inside one atomic unit. You see the full explicit lifecycle (begin, multi-table writes, commit), verify atomicity by rolling back a partial invoice, then refactor to the `runInTransaction` pattern that handles commit, rollback, and retry automatically. A final step shows the same workflow non-blocking with `runInTransactionAsync`.

## Prerequisites

- **A running 3-node cluster with the Music Store dataset** from [Start Your Local GridGain 9 Development Cluster](start-local-cluster.md)
- **Completed** [Work with RecordView and KeyValueView](recordview-keyvalueview.md) (familiarity with `IgniteClient`, `IgniteSql`, and the Music Store schema)
- **Java 17** or later
- **Maven 3.8** or later

<details>
<summary>Returning to these tutorials? Restore your project.</summary>

This tutorial extends the Maven project from [Work with RecordView and KeyValueView](recordview-keyvalueview.md). If you need to recreate that project, create a directory named `table-api-demo` with the following files.

**`pom.xml`**

{% code title="pom.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>table-api-demo</artifactId>
    <version>1.0.0</version>

    <properties>
        <maven.compiler.release>17</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <exec.mainClass>com.example.musicstore.CreateInvoice</exec.mainClass>
    </properties>

    <repositories>
        <repository>
            <id>gridgain-external</id>
            <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
        </repository>
    </repositories>

    <dependencies>
        <dependency>
            <groupId>org.gridgain</groupId>
            <artifactId>ignite-client</artifactId>
            <!-- Use the latest GridGain 9 version -->
            <version>9.1.28</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.4.1</version>
                <configuration>
                    <mainClass>${exec.mainClass}</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
{% endcode %}

**Model classes.** Create these in `src/main/java/com/example/musicstore/model/`:

{% code title="model/Artist.java" %}
```java
package com.example.musicstore.model;

public class Artist {
    private Integer artistId;
    private String name;

    public Artist() {}

    public Artist(Integer artistId, String name) {
        this.artistId = artistId;
        this.name = name;
    }

    public Integer getArtistId() { return artistId; }
    public void setArtistId(Integer artistId) { this.artistId = artistId; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    @Override
    public String toString() {
        return "Artist{id=" + artistId + ", name='" + name + "'}";
    }
}
```
{% endcode %}

{% code title="model/Customer.java" %}
```java
package com.example.musicstore.model;

public class Customer {
    private Integer customerId;
    private String firstName;
    private String lastName;
    private String company;
    private String address;
    private String city;
    private String state;
    private String country;
    private String postalCode;
    private String phone;
    private String fax;
    private String email;
    private Integer supportRepId;

    public Customer() {}

    public Customer(Integer customerId) {
        this.customerId = customerId;
    }

    public Integer getCustomerId() { return customerId; }
    public void setCustomerId(Integer id) { this.customerId = id; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String v) { this.firstName = v; }
    public String getLastName() { return lastName; }
    public void setLastName(String v) { this.lastName = v; }
    public String getCompany() { return company; }
    public void setCompany(String v) { this.company = v; }
    public String getAddress() { return address; }
    public void setAddress(String v) { this.address = v; }
    public String getCity() { return city; }
    public void setCity(String v) { this.city = v; }
    public String getState() { return state; }
    public void setState(String v) { this.state = v; }
    public String getCountry() { return country; }
    public void setCountry(String v) { this.country = v; }
    public String getPostalCode() { return postalCode; }
    public void setPostalCode(String v) { this.postalCode = v; }
    public String getPhone() { return phone; }
    public void setPhone(String v) { this.phone = v; }
    public String getFax() { return fax; }
    public void setFax(String v) { this.fax = v; }
    public String getEmail() { return email; }
    public void setEmail(String v) { this.email = v; }
    public Integer getSupportRepId() { return supportRepId; }
    public void setSupportRepId(Integer v) { this.supportRepId = v; }

    @Override
    public String toString() {
        return "Customer{id=" + customerId
                + ", name='" + firstName + " " + lastName + "'"
                + ", email='" + email + "'}";
    }
}
```
{% endcode %}

{% code title="model/CustomerContact.java" %}
```java
package com.example.musicstore.model;

public class CustomerContact {
    private String firstName;
    private String lastName;
    private String email;
    private String city;
    private String country;

    public CustomerContact() {}

    public String getFirstName() { return firstName; }
    public void setFirstName(String v) { this.firstName = v; }
    public String getLastName() { return lastName; }
    public void setLastName(String v) { this.lastName = v; }
    public String getEmail() { return email; }
    public void setEmail(String v) { this.email = v; }
    public String getCity() { return city; }
    public void setCity(String v) { this.city = v; }
    public String getCountry() { return country; }
    public void setCountry(String v) { this.country = v; }

    @Override
    public String toString() {
        return "CustomerContact{name='" + firstName + " " + lastName + "'"
                + ", email='" + email + "'}";
    }
}
```
{% endcode %}

After creating these files, verify the cluster is running:

```bash
docker exec gridgain9-node1 /opt/gridgain9cli/bin/gridgain9 sql \
  "SELECT COUNT(*) AS tracks FROM Track;"
```

**Expected result: 3503.** If you need to restore the cluster or reload the dataset, see the full restore instructions in [Start Your Local GridGain 9 Development Cluster](start-local-cluster.md).

</details>

## What You Will Learn

- How to group multiple table operations into a single atomic transaction
- How to verify atomicity by rolling back a partially created invoice
- How `runInTransaction` simplifies lifecycle management with auto-commit, auto-rollback, and auto-retry
- How to run transactions asynchronously with `runInTransactionAsync` and `CompletableFuture`

## What You Will Build

You extend the project from [Work with RecordView and KeyValueView](recordview-keyvalueview.md) with four new Java classes, each using a different transaction pattern to create an invoice with line items in the Music Store database. The workflow writes to two tables (Invoice and InvoiceLine) in a single atomic operation. The classes build in sophistication from the explicit lifecycle to the functional `runInTransaction` pattern to async execution:

```
table-api-demo/
└── src/main/java/com/example/musicstore/
    ├── model/           ← unchanged from the previous tutorial
    ├── CreateInvoice.java          ← Step 1: explicit begin/commit/rollback
    ├── RollbackInvoice.java        ← Step 2: rollback patterns
    ├── InvoiceWorkflow.java        ← Step 3: runInTransaction
    └── AsyncInvoiceWorkflow.java   ← Step 4: runInTransactionAsync
```

All classes clean up their test data, so you can run them in any order.

## Verify the Invoice Tables

Before writing transactional code, verify the Invoice and InvoiceLine tables are loaded with the expected data. The Music Store dataset includes 412 invoices and 2,240 invoice line items. Your test classes use IDs starting at 10001, well above the existing dataset range.

```bash
docker exec gridgain9-node1 /opt/gridgain9cli/bin/gridgain9 sql \
  "SELECT COUNT(*) AS invoice_count FROM Invoice;"
docker exec gridgain9-node1 /opt/gridgain9cli/bin/gridgain9 sql \
  "SELECT COUNT(*) AS line_count FROM InvoiceLine;"
```

```
╔═══════════════╗
║ INVOICE_COUNT ║
╠═══════════════╣
║ 412           ║
╚═══════════════╝
╔════════════╗
║ LINE_COUNT ║
╠════════════╣
║ 2240       ║
╚════════════╝
```

{% hint style="success" %}
**Checkpoint:** Invoice count is 412. InvoiceLine count is 2240. Test IDs 10001–10005 are clear.
{% endhint %}

## Create an Invoice With an Explicit Transaction

An explicit transaction gives you direct control over the lifecycle. You begin it, execute operations, and commit or roll back based on the result.

In [Work with RecordView and KeyValueView](recordview-keyvalueview.md), every SQL call passed `null` as the first argument. That `null` creates an implicit transaction that commits immediately. In this step, you replace `null` with a named `Transaction` object. The cluster holds all writes in an uncommitted state until you call `tx.commit()`. If anything fails before the commit, a `tx.rollback()` discards every write in the transaction as if none of them happened.

The workflow looks up the unit price for three tracks, inserts one line item per track (accumulating the total), then inserts the invoice header with the calculated total. All four writes are grouped into one atomic unit. No partial state is ever visible to other transactions.

Create `CreateInvoice.java` in `src/main/java/com/example/musicstore/`:

{% code title="CreateInvoice.java" %}
```java
package com.example.musicstore;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.IgniteSql;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.tx.Transaction;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Explicit transaction lifecycle: begin, multi-table writes, commit.
 *
 * Creates an invoice with three line items using an explicit transaction.
 * The four SQL operations (three INSERT InvoiceLine, one INSERT Invoice)
 * are grouped into one atomic unit. They either all commit together or
 * none of them persist.
 *
 * This is the same pattern as passing null for the transaction parameter in
 * the previous tutorial, except the Transaction object is now named and
 * shared across every operation in the workflow.
 *
 * Concepts demonstrated:
 *   - Obtaining a transaction from client.transactions().begin()
 *   - Passing the transaction to SQL operations across multiple tables
 *   - Read-your-own-writes: the verification query within the transaction
 *     sees uncommitted data that is invisible to all other transactions
 *   - Explicit commit and error-path rollback with try/catch
 *
 * Run:      mvn compile exec:java
 * Override: mvn compile exec:java -Dexec.mainClass=com.example.musicstore.CreateInvoice
 */
public class CreateInvoice {

    public static void main(String[] args) {
        // Suppress GridGain's verbose client connection and protocol logs so the
        // tutorial output, which demonstrates transaction behavior, is readable.
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            IgniteSql sql = client.sql();

            System.out.println("--- Creating invoice with explicit transaction");

            Transaction tx = client.transactions().begin();
            System.out.println(">>> Transaction started");

            try {
                BigDecimal total = BigDecimal.ZERO;
                int[] trackIds = {1, 2, 3};

                // Look up each track price and insert the line item in one pass.
                // Passing tx to the SELECT ensures the price read participates in
                // the same SERIALIZABLE snapshot as the writes, so concurrent price
                // changes cannot produce an inconsistent invoice.
                for (int i = 0; i < trackIds.length; i++) {
                    int trackId = trackIds[i];
                    int lineId = 10001 + i;

                    BigDecimal unitPrice;
                    // try-with-resources closes the server-side cursor when done.
                    // ResultSet<SqlRow> holds an open stream from the cluster node;
                    // failing to close it leaks the cursor until the connection drops.
                    try (ResultSet<SqlRow> rs = sql.execute(tx,
                            "SELECT UnitPrice FROM Track WHERE TrackId = ?", trackId)) {
                        unitPrice = rs.next().decimalValue("UnitPrice");
                    }

                    sql.execute(tx,
                            "INSERT INTO InvoiceLine (InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity) VALUES (?, ?, ?, ?, ?)",
                            lineId, 10001, trackId, unitPrice, 1);

                    total = total.add(unitPrice);
                    System.out.printf(">>> Added track %d ($%s)%n", trackId, unitPrice);
                }

                // Insert the invoice header with the calculated total. Line items
                // are already in the transaction buffer; the header completes the
                // invoice. Nothing is visible outside the transaction until commit.
                sql.execute(tx,
                        "INSERT INTO Invoice (InvoiceId, CustomerId, InvoiceDate, Total) VALUES (?, ?, ?, ?)",
                        10001, 1, LocalDate.now(), total);
                System.out.printf(">>> Invoice 10001 created for customer 1, total $%s%n", total);

                // Read-your-own-writes: query the data we just wrote, still within
                // the transaction. This returns our uncommitted rows. The same query
                // outside the transaction before commit would return nothing.
                System.out.println("--- Verifying within transaction (read-your-own-writes)");
                try (ResultSet<SqlRow> rs = sql.execute(tx,
                        "SELECT i.InvoiceId, i.Total, COUNT(il.InvoiceLineId) AS LineCount " +
                        "FROM Invoice i JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId " +
                        "WHERE i.InvoiceId = ? GROUP BY i.InvoiceId, i.Total",
                        10001)) {
                    SqlRow row = rs.next();
                    System.out.printf("<<< Within tx: Invoice %d, %d lines, total $%s%n",
                            row.intValue("InvoiceId"),
                            row.longValue("LineCount"),
                            row.decimalValue("Total"));
                }

                tx.commit();
                System.out.println("<<< Transaction committed");

            } catch (Exception e) {
                System.out.println("!!! Error: " + e.getMessage());
                // Rollback discards every write in this transaction (the invoice
                // header and all line items) as if none of it happened. Atomicity
                // is all-or-nothing.
                tx.rollback();
                System.out.println("<<< Transaction rolled back");
                throw e;
            }

            // Verify after commit using an implicit transaction (null). The explicit
            // cast is required: IgniteSql also has an execute(String, Object...)
            // overload, which makes a bare null ambiguous between the
            // Transaction and String parameters.
            System.out.println("--- Verifying after commit");
            try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                    "SELECT i.InvoiceId, i.Total, COUNT(il.InvoiceLineId) AS LineCount " +
                    "FROM Invoice i JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId " +
                    "WHERE i.InvoiceId = ? GROUP BY i.InvoiceId, i.Total",
                    10001)) {
                SqlRow row = rs.next();
                System.out.printf("<<< Invoice %d persisted: %d lines, total $%s%n",
                        row.intValue("InvoiceId"),
                        row.longValue("LineCount"),
                        row.decimalValue("Total"));
            }

            cleanup(sql);

        } catch (Exception e) {
            System.err.println("!!! Fatal: " + e.getMessage());
        }

        // GridGain maintains background threads for cluster communication.
        // System.exit() forces shutdown; without it the JVM hangs after main() returns.
        System.exit(0);
    }

    private static void cleanup(IgniteSql sql) {
        // Delete InvoiceLine before Invoice so no orphaned line items remain,
        // following the logical dependency order of the data.
        sql.execute((Transaction) null, "DELETE FROM InvoiceLine WHERE InvoiceId = ?", 10001);
        sql.execute((Transaction) null, "DELETE FROM Invoice WHERE InvoiceId = ?", 10001);
        System.out.println(">>> Test data cleaned up");
    }
}
```
{% endcode %}

Run the class:

```bash
mvn compile exec:java -q
```

```
--- Creating invoice with explicit transaction
>>> Transaction started
>>> Added track 1 ($0.99)
>>> Added track 2 ($0.99)
>>> Added track 3 ($0.99)
>>> Invoice 10001 created for customer 1, total $2.97
--- Verifying within transaction (read-your-own-writes)
<<< Within tx: Invoice 10001, 3 lines, total $2.97
<<< Transaction committed
--- Verifying after commit
<<< Invoice 10001 persisted: 3 lines, total $2.97
>>> Test data cleaned up
```

{% hint style="success" %}
**Checkpoint:** Transaction committed without errors. Invoice 10001 persists with 3 lines at $0.99 each and a total of $2.97.
{% endhint %}

**What the output shows:**

The "Verifying within transaction" block demonstrates **read-your-own-writes**, a property of GridGain's SERIALIZABLE isolation. Your transaction can read its own uncommitted writes. The data is visible within `tx` even though no commit has happened. Other transactions running on the cluster at the same time cannot see invoice 10001 or its line items until the commit completes.

The two verification queries are structurally identical but behave differently. The first executes within `tx` (uncommitted context) and the second executes with `(Transaction) null` (implicit auto-commit, reads only committed data).

{% hint style="info" %}
GridGain read-write transactions use **SERIALIZABLE isolation**. Locks are acquired on first access and held until commit or rollback. No other read-write transaction can modify the same rows while the lock is held. Read-only transactions use snapshot isolation instead. They see a consistent point-in-time view of the data without acquiring locks.
{% endhint %}

{% hint style="info" %}
The Customer and Invoice tables are a colocated pair. The schema uses `CustomerId` as the colocation key for Invoice, so an invoice lands in the same partition as its customer. InvoiceLine uses `InvoiceId` as its colocation key, which keeps all lines of one invoice in the same partition but does not place them with the Invoice row or the Customer row, because colocation does not chain through a middle table. When a transaction writes only rows that share a partition, such as all lines of one invoice, all lock acquisitions happen on the same node, eliminating network round-trips between nodes for each operation. The benefit is latency reduction at scale: fewer distributed coordination steps per transaction.
{% endhint %}

## Roll Back a Partial Invoice

The value of transactions is clearest when something goes wrong mid-workflow. This step creates an invoice header, then deliberately fails before inserting line items. In both cases, the invoice header vanishes on rollback. No partial record persists.

The class demonstrates two rollback patterns:

- **Part A, Explicit rollback:** the application decides to cancel and calls `tx.rollback()` directly (no exception was thrown)
- **Part B, Error-triggered rollback:** an exception interrupts the workflow and the catch block calls `tx.rollback()` before re-surfacing the error

Create `RollbackInvoice.java`:

{% code title="RollbackInvoice.java" %}
```java
package com.example.musicstore;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.IgniteSql;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.tx.Transaction;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Atomicity in action: two rollback patterns, one guarantee.
 *
 * The power of atomicity is clearest when something goes wrong mid-workflow.
 * Both patterns here start the same way (create an invoice header) and fail
 * before inserting line items. In both cases, the header vanishes completely
 * on rollback. No partial record persists.
 *
 * Concepts demonstrated:
 *   - Part A, Explicit rollback: calling tx.rollback() when the application
 *     decides to cancel (e.g., user cancellation, business rule violation
 *     detected before an exception is thrown)
 *   - Part B, Error-triggered rollback: catching an exception, rolling back
 *     in the catch block. This is the more common production pattern.
 *
 * Run: mvn compile exec:java -Dexec.mainClass=com.example.musicstore.RollbackInvoice
 */
public class RollbackInvoice {

    public static void main(String[] args) {
        // Suppress GridGain's verbose client connection and protocol logs so the
        // tutorial output, which demonstrates rollback behavior, is readable.
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            IgniteSql sql = client.sql();

            partA_explicitRollback(client, sql);
            partB_errorTriggeredRollback(client, sql);

        } catch (Exception e) {
            System.err.println("!!! Fatal: " + e.getMessage());
        }

        // GridGain maintains background threads for cluster communication.
        // System.exit() forces shutdown; without it the JVM hangs after main() returns.
        System.exit(0);
    }

    private static void partA_explicitRollback(IgniteClient client, IgniteSql sql) {
        System.out.println("--- Part A: Explicit rollback");

        Transaction tx = client.transactions().begin();
        System.out.println(">>> Transaction started");

        sql.execute(tx,
                "INSERT INTO Invoice (InvoiceId, CustomerId, InvoiceDate, Total) VALUES (?, ?, ?, ?)",
                10002, 1, LocalDate.now(), new BigDecimal("0.00"));
        System.out.println(">>> Invoice 10002 header created");
        System.out.println(">>> Deciding to cancel, rolling back");

        // No exception was thrown; this rollback is a deliberate application
        // decision. Atomicity means the invoice header is discarded completely.
        tx.rollback();
        System.out.println("<<< Transaction rolled back");

        // Verify: the invoice does not exist. Other transactions never saw it
        // because the write was never committed.
        try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                "SELECT COUNT(*) AS cnt FROM Invoice WHERE InvoiceId = ?", 10002)) {
            long count = rs.next().longValue("cnt");
            System.out.printf("<<< Invoice 10002 exists: %s (expected: false)%n", count > 0);
        }
    }

    private static void partB_errorTriggeredRollback(IgniteClient client, IgniteSql sql) {
        System.out.println("\n--- Part B: Error-triggered rollback");

        Transaction tx = client.transactions().begin();
        System.out.println(">>> Transaction started");

        try {
            sql.execute(tx,
                    "INSERT INTO Invoice (InvoiceId, CustomerId, InvoiceDate, Total) VALUES (?, ?, ?, ?)",
                    10003, 1, LocalDate.now(), new BigDecimal("0.00"));
            System.out.println(">>> Invoice 10003 header created");

            // Simulated validation failure. In a real application this might be
            // a track that is out of stock, a payment method that was declined,
            // or an inventory check that fails mid-transaction.
            System.out.println(">>> Validating track availability...");
            throw new IllegalStateException("Track 999 is not available for purchase");

        } catch (Exception e) {
            System.out.println("!!! Error: " + e.getMessage());
            // Roll back in the catch block. Every write in this transaction is
            // discarded: the invoice header at 10003 does not persist.
            tx.rollback();
            System.out.println("<<< Transaction rolled back");
        }

        // Verify atomicity: the header is gone even though it was written before
        // the exception. A committed partial write would leave orphaned Invoice
        // records without any InvoiceLine rows. That is exactly what transactions prevent.
        try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                "SELECT COUNT(*) AS cnt FROM Invoice WHERE InvoiceId = ?", 10003)) {
            long count = rs.next().longValue("cnt");
            System.out.printf("<<< Invoice 10003 exists: %s (expected: false)%n", count > 0);
        }
        System.out.println("<<< Atomicity confirmed: partial writes do not persist");
    }
}
```
{% endcode %}

Run the class:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.RollbackInvoice -q
```

```
--- Part A: Explicit rollback
>>> Transaction started
>>> Invoice 10002 header created
>>> Deciding to cancel, rolling back
<<< Transaction rolled back
<<< Invoice 10002 exists: false (expected: false)

--- Part B: Error-triggered rollback
>>> Transaction started
>>> Invoice 10003 header created
>>> Validating track availability...
!!! Error: Track 999 is not available for purchase
<<< Transaction rolled back
<<< Invoice 10003 exists: false (expected: false)
<<< Atomicity confirmed: partial writes do not persist
```

{% hint style="success" %}
**Checkpoint:** Invoice 10002 and Invoice 10003 do not exist after rollback. Both parts print "exists: false (expected: false)".
{% endhint %}

**Why both invoices are gone:** The INSERT wrote the invoice header to an uncommitted transaction buffer. `tx.rollback()` discards that buffer entirely. The write never reached durable storage. From the perspective of any other transaction on the cluster, invoice 10002 and invoice 10003 never existed. Without transactions, the INSERT would have committed immediately and left behind an orphaned invoice record with no line items.

## Refactor to runInTransaction

The invoice workflow works, but the `begin()` / `try` / `commit()` / `catch` / `rollback()` lifecycle code is boilerplate that every transactional workflow repeats. `runInTransaction` collapses all of it into a closure:

- **Auto-commit:** GridGain commits the transaction when the closure returns normally
- **Auto-rollback:** GridGain rolls back if the closure throws any exception
- **Auto-retry:** GridGain retries the closure on transient failures (lock conflicts, timeouts, or primary replica changes) without any retry logic in your code

The closure signature is `Function<Transaction, T>` rather than `Consumer<Transaction>` because real workflows need to return a value. In this case the workflow returns the new invoice ID, which the caller uses after the transaction commits.

{% hint style="warning" %}
`runInTransaction` may execute the closure more than once if a transient failure triggers a retry. The closure must produce the same result on every execution. Avoid side effects that cannot be retried safely: sending emails, charging payment cards, or incrementing external counters inside the closure. Perform those actions after `runInTransaction` returns successfully.
{% endhint %}

Create `InvoiceWorkflow.java`:

{% code title="InvoiceWorkflow.java" %}
```java
package com.example.musicstore;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.IgniteSql;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.tx.Transaction;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * The invoice workflow with runInTransaction.
 *
 * The same multi-table workflow as CreateInvoice, refactored into
 * runInTransaction(Function<Transaction, T>). The explicit begin, commit,
 * try/catch, and rollback calls from Step 1 are replaced by a closure that
 * GridGain manages automatically.
 *
 * Why Function<Transaction, T> instead of Consumer<Transaction>: the closure
 * must return the new InvoiceId so the caller can use it after commit.
 * Consumer is void; Function lets the closure return a value that becomes
 * the return value of runInTransaction itself.
 *
 * Concepts demonstrated:
 *   - Auto-commit: GridGain commits the transaction when the closure returns normally.
 *   - Auto-rollback: GridGain rolls back if the closure throws any exception.
 *   - Auto-retry: GridGain retries the closure on transient failures (lock
 *     conflicts, timeouts, or primary replica changes) without the caller
 *     needing retry logic. The closure must be side-effect-free because it
 *     may execute more than once.
 *
 * Run: mvn compile exec:java -Dexec.mainClass=com.example.musicstore.InvoiceWorkflow
 */
public class InvoiceWorkflow {

    public static void main(String[] args) {
        // Suppress GridGain's verbose client connection and protocol logs so the
        // tutorial output, which demonstrates the runInTransaction pattern, is readable.
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            IgniteSql sql = client.sql();

            System.out.println("--- Creating invoice with runInTransaction");

            // runInTransaction manages the full lifecycle. The Function form is used
            // instead of Consumer because the caller needs the InvoiceId after commit.
            int newInvoiceId = client.transactions().runInTransaction(tx -> {
                BigDecimal total = BigDecimal.ZERO;
                int[] trackIds = {1, 2, 3};

                for (int i = 0; i < trackIds.length; i++) {
                    int trackId = trackIds[i];
                    int lineId = 10004 + i;

                    BigDecimal unitPrice;
                    // try-with-resources closes the server-side cursor when done.
                    // ResultSet<SqlRow> holds a streaming result; always close it.
                    try (ResultSet<SqlRow> rs = sql.execute(tx,
                            "SELECT UnitPrice FROM Track WHERE TrackId = ?", trackId)) {
                        unitPrice = rs.next().decimalValue("UnitPrice");
                    }

                    sql.execute(tx,
                            "INSERT INTO InvoiceLine (InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity) VALUES (?, ?, ?, ?, ?)",
                            lineId, 10004, trackId, unitPrice, 1);

                    total = total.add(unitPrice);
                }

                // Insert the invoice header with the calculated total.
                sql.execute(tx,
                        "INSERT INTO Invoice (InvoiceId, CustomerId, InvoiceDate, Total) VALUES (?, ?, ?, ?)",
                        10004, 1, LocalDate.now(), total);
                System.out.printf(">>> Invoice 10004 created, total $%s%n", total);

                // The return value becomes the result of runInTransaction after commit.
                // GridGain commits the transaction automatically when this return executes.
                return 10004;
            });

            System.out.printf("<<< Transaction committed. New invoice ID: %d%n", newInvoiceId);

            // Verify after commit using an implicit transaction (null). The explicit
            // cast is required because IgniteSql also has an execute(String, Object...)
            // overload, which makes a bare null ambiguous.
            System.out.println("--- Verifying after commit");
            try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                    "SELECT i.InvoiceId, i.Total, COUNT(il.InvoiceLineId) AS LineCount " +
                    "FROM Invoice i JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId " +
                    "WHERE i.InvoiceId = ? GROUP BY i.InvoiceId, i.Total",
                    newInvoiceId)) {
                SqlRow row = rs.next();
                System.out.printf("<<< Invoice %d persisted: %d lines, total $%s%n",
                        row.intValue("InvoiceId"),
                        row.longValue("LineCount"),
                        row.decimalValue("Total"));
            }

            cleanup(sql);

        } catch (Exception e) {
            System.err.println("!!! Fatal: " + e.getMessage());
        }

        // GridGain maintains background threads for cluster communication.
        // System.exit() forces shutdown; without it the JVM hangs after main() returns.
        System.exit(0);
    }

    private static void cleanup(IgniteSql sql) {
        // Delete InvoiceLine before Invoice so no orphaned line items remain.
        sql.execute((Transaction) null, "DELETE FROM InvoiceLine WHERE InvoiceId = ?", 10004);
        sql.execute((Transaction) null, "DELETE FROM Invoice WHERE InvoiceId = ?", 10004);
        System.out.println(">>> Test data cleaned up");
    }
}
```
{% endcode %}

Run the class:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.InvoiceWorkflow -q
```

```
--- Creating invoice with runInTransaction
>>> Invoice 10004 created, total $2.97
<<< Transaction committed. New invoice ID: 10004
--- Verifying after commit
<<< Invoice 10004 persisted: 3 lines, total $2.97
>>> Test data cleaned up
```

{% hint style="success" %}
**Checkpoint:** Transaction committed. Invoice 10004 persists with 3 lines and a total of $2.97.
{% endhint %}

The `runInTransaction` version eliminates `begin()`, the `try` / `catch(Exception e)` block, `tx.commit()`, and `tx.rollback()`. The workflow code (price lookups, line item inserts, header insert) is unchanged. GridGain manages the lifecycle; your code focuses on the business logic.

## Async Transactions

`runInTransactionAsync` is the non-blocking form of the same pattern. The method returns immediately with a `CompletableFuture<T>` that completes when the transaction commits. The closure signature is `Function<Transaction, CompletableFuture<T>>`: the closure must return a future representing the async work, and the transaction commits when that future completes.

**When async transactions matter:** Services that handle many concurrent requests cannot afford one thread per transaction. A blocking call to `runInTransaction` occupies the calling thread for the entire round-trip to the cluster. `runInTransactionAsync` frees the calling thread immediately so it can handle other work while waiting for the commit.

The workflow logic inside the closure is unchanged. The differences are structural. The operations are wrapped in `CompletableFuture.supplyAsync()` to lift synchronous SQL calls into a future, and post-commit work chains on with `thenAccept`. In a fully async service, you would replace `supplyAsync` with chained async GridGain operations using `thenCompose`.

Create `AsyncInvoiceWorkflow.java`:

{% code title="AsyncInvoiceWorkflow.java" %}
```java
package com.example.musicstore;

import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.sql.IgniteSql;
import org.apache.ignite.sql.ResultSet;
import org.apache.ignite.sql.SqlRow;
import org.apache.ignite.tx.Transaction;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.concurrent.CompletableFuture;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * The invoice workflow with runInTransactionAsync.
 *
 * The same workflow as InvoiceWorkflow, using the async variant.
 * runInTransactionAsync never blocks the calling thread: it returns a
 * CompletableFuture<T> that completes when the transaction commits.
 * The commit, rollback, and retry semantics are identical to the sync form.
 *
 * The closure signature is Function<Transaction, CompletableFuture<T>>.
 * The closure must return a future that represents the async work. Here, the
 * work is wrapped in CompletableFuture.supplyAsync() to lift synchronous
 * GridGain SQL calls into a CompletableFuture. In a fully async service, you
 * would chain async GridGain operations with thenCompose instead.
 *
 * Why async matters: services that handle many concurrent requests cannot
 * afford one thread per transaction. Non-blocking transactions let one thread
 * manage many in-flight operations without blocking on network round-trips.
 *
 * Run: mvn compile exec:java -Dexec.mainClass=com.example.musicstore.AsyncInvoiceWorkflow
 */
public class AsyncInvoiceWorkflow {

    public static void main(String[] args) {
        // Suppress GridGain's verbose client connection and protocol logs so the
        // tutorial output, which demonstrates async transaction behavior, is readable.
        Logger.getLogger("org.apache.ignite").setLevel(Level.WARNING);

        try (IgniteClient client = IgniteClient.builder()
                .addresses("localhost:10800", "localhost:10801", "localhost:10802")
                .build()) {

            IgniteSql sql = client.sql();

            System.out.println("--- Creating invoice with runInTransactionAsync");

            // runInTransactionAsync returns immediately with a future. The transaction
            // commits (or rolls back) when the future returned by the closure completes.
            CompletableFuture<Integer> invoiceFuture = client.transactions()
                    .runInTransactionAsync(tx -> {
                        // supplyAsync lifts the synchronous SQL operations into a
                        // CompletableFuture so the closure satisfies the required
                        // Function<Transaction, CompletableFuture<T>> signature.
                        // In a fully async service, replace supplyAsync with chained
                        // async GridGain operations using thenCompose.
                        return CompletableFuture.supplyAsync(() -> {
                            BigDecimal total = BigDecimal.ZERO;
                            int[] trackIds = {1, 2, 3};

                            for (int i = 0; i < trackIds.length; i++) {
                                int trackId = trackIds[i];
                                int lineId = 10005 + i;

                                BigDecimal unitPrice;
                                // try-with-resources closes the server-side cursor when done.
                                // ResultSet<SqlRow> holds a streaming result; always close it.
                                try (ResultSet<SqlRow> rs = sql.execute(tx,
                                        "SELECT UnitPrice FROM Track WHERE TrackId = ?", trackId)) {
                                    unitPrice = rs.next().decimalValue("UnitPrice");
                                }

                                sql.execute(tx,
                                        "INSERT INTO InvoiceLine (InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity) VALUES (?, ?, ?, ?, ?)",
                                        lineId, 10005, trackId, unitPrice, 1);

                                total = total.add(unitPrice);
                            }

                            sql.execute(tx,
                                    "INSERT INTO Invoice (InvoiceId, CustomerId, InvoiceDate, Total) VALUES (?, ?, ?, ?)",
                                    10005, 1, LocalDate.now(), total);
                            System.out.printf(">>> Invoice 10005 created, total $%s%n", total);

                            return 10005;
                        });
                    });

            // Chain post-commit work. thenAccept runs only after the transaction
            // commits successfully; exceptionally handles commit failure or any
            // exception thrown inside the closure.
            invoiceFuture
                    .thenAccept(invoiceId -> {
                        System.out.printf("<<< Transaction committed. New invoice ID: %d%n", invoiceId);

                        System.out.println("--- Verifying after commit");
                        // The explicit (Transaction) null cast is required (see above).
                        // See CreateInvoice for the full explanation.
                        try (ResultSet<SqlRow> rs = sql.execute((Transaction) null,
                                "SELECT i.InvoiceId, i.Total, COUNT(il.InvoiceLineId) AS LineCount " +
                                "FROM Invoice i JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId " +
                                "WHERE i.InvoiceId = ? GROUP BY i.InvoiceId, i.Total",
                                invoiceId)) {
                            SqlRow row = rs.next();
                            System.out.printf("<<< Invoice %d persisted: %d lines, total $%s%n",
                                    row.intValue("InvoiceId"),
                                    row.longValue("LineCount"),
                                    row.decimalValue("Total"));
                        }
                    })
                    .exceptionally(e -> {
                        System.err.println("!!! Transaction failed: " + e.getMessage());
                        return null;
                    })
                    // join() blocks this thread until the async chain completes.
                    // A standalone main() has no event loop to keep running, so without
                    // join() the JVM would exit before the future resolves. In a real
                    // async service (servlet container, reactive framework), you would
                    // return the future to the framework instead of calling join().
                    .join();

            cleanup(sql);

        } catch (Exception e) {
            System.err.println("!!! Fatal: " + e.getMessage());
        }

        // GridGain maintains background threads for cluster communication.
        // System.exit() forces shutdown; without it the JVM hangs after main() returns.
        System.exit(0);
    }

    private static void cleanup(IgniteSql sql) {
        // Delete InvoiceLine before Invoice so no orphaned line items remain.
        sql.execute((Transaction) null, "DELETE FROM InvoiceLine WHERE InvoiceId = ?", 10005);
        sql.execute((Transaction) null, "DELETE FROM Invoice WHERE InvoiceId = ?", 10005);
        System.out.println(">>> Test data cleaned up");
    }
}
```
{% endcode %}

Run the class:

```bash
mvn compile exec:java -Dexec.mainClass=com.example.musicstore.AsyncInvoiceWorkflow -q
```

```
--- Creating invoice with runInTransactionAsync
>>> Invoice 10005 created, total $2.97
<<< Transaction committed. New invoice ID: 10005
--- Verifying after commit
<<< Invoice 10005 persisted: 3 lines, total $2.97
>>> Test data cleaned up
```

{% hint style="success" %}
**Checkpoint:** Transaction committed asynchronously. Invoice 10005 persists with 3 lines and a total of $2.97.
{% endhint %}

The output is identical to the synchronous `InvoiceWorkflow`. From the cluster's perspective the transaction is the same: begin, write, commit. The difference is in the calling thread: `runInTransactionAsync` returned immediately after the closure was submitted. The `thenAccept` handler ran on a separate thread when the future resolved.

`.join()` at the end of the chain blocks `main()` until the async work completes. A standalone `main()` has no event loop; without `.join()` the JVM would exit before the future resolves. In a servlet container or reactive framework, you return the future to the framework instead.

{% hint style="info" %}
`TransactionOptions` controls three settings when passed to `client.transactions().begin()`:

- **`timeoutMillis(long)`**: How long the transaction waits before automatically rolling back (default: 30 seconds). Set this lower for time-sensitive workflows where a stalled transaction should fail fast.
- **`readOnly(boolean)`**: When `true`, the transaction uses snapshot isolation instead of SERIALIZABLE, acquiring no locks. Read-only transactions are faster for analytics queries that do not modify data.
- **`label(String)`**: A diagnostic string visible in the `SYSTEM.TRANSACTIONS` system view. Use labels in production to identify transaction types during troubleshooting.

```java
// A labelled read-only transaction with a 5-second timeout
TransactionOptions opts = new TransactionOptions()
        .readOnly(true)
        .timeoutMillis(5_000)
        .label("invoice-report");
Transaction tx = client.transactions().begin(opts);
```

See [Performing Transactions](../../gridgain9-development/transactions.md) for the full `TransactionOptions` reference.
{% endhint %}

## Summary

You have written the same multi-table invoice workflow at three levels of sophistication:

**Explicit lifecycle.** `begin()` / `commit()` / `rollback()`. You control every step. The explicit pattern is the right choice when you need fine-grained control, when you are debugging a transaction, or when the workflow has branch points where you decide to commit or roll back based on business logic before any exception is thrown.

**`runInTransaction`.** A closure-based pattern that auto-commits on success, auto-rolls-back on failure, and auto-retries on transient errors. This is the recommended pattern for production code. The boilerplate is gone; the workflow logic is unchanged.

**`runInTransactionAsync`.** The same pattern, non-blocking. Use this in services that handle many concurrent requests and cannot afford one thread per in-flight transaction.

**When to choose each pattern:**

| Pattern | Choose when |
|---|---|
| Explicit `begin()` / `commit()` | Debugging, branch-based commit decisions, fine-grained lifecycle control |
| `runInTransaction` | Standard production workflows, most multi-table operations |
| `runInTransactionAsync` | High-concurrency services, event-driven architectures, reactive pipelines |

Continue to [Design a Schema for Distributed SQL](../schema-design-for-distributed-sql/schema-distributed-sql.md) to learn how colocation and distribution zones shape performance. To run Java logic directly on the nodes where data lives, see [About Distributed Computing](../../gridgain9-development/distributed-computing/about-distributed-computing.md).
