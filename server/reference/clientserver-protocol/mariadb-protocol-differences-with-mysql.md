---
description: >-
  Learn about the specific extensions and differences in the MariaDB protocol
  compared to MySQL, such as extended capability flags and metadata.
---

# MariaDB Protocol Differences with MySQL

Here is a list of the differences between MariaDB and MySQL in terms of protocol, in order to help community driver maintainers.

## MariaDB Capabilities Extension

MariaDB/MySQL servers can advertise feature support using capabilities. To expand the capabilities beyond the original 4 bytes, MariaDB utilizes 4 bytes, unused by MySQL, in the [Initial handshake packet](1-connecting/connection.md#initial-handshake-packet) (server capabilities 3rd part). In order to avoid incompatibility in the future, those 4 bytes have to be read only if capability `CLIENT_MYSQL` is not set (server then being MariaDB).

### Enhanced Capabilities

* `MARIADB_CLIENT_PROGRESS`: [Client progress reporting](../product-development/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting.md).
* `MARIADB_CLIENT_CACHE_METADATA`: Enables clients to cache metadata and avoid repeated network transmissions (since [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes)).
* `MARIADB_CLIENT_EXTENDED_METADATA` : Provides more detailed column metadata information for specific data types (since [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes)).
* `MARIADB_CLIENT_STMT_BULK_OPERATIONS`: Introduces a dedicated command, [COM\_STMT\_BULK\_EXECUTE](3-binary-protocol-prepared-statements/com_stmt_bulk_execute.md), for efficient batch execution of statements.
* MARIADB\_CLIENT\_BULK\_UNIT\_RESULTS: Allows for individual result sets for each bulk operation (since [MariaDB 11.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-1-release-notes)).

See [Connection Capabilities](1-connecting/connection.md#capabilities).

## Prepare Statement Skipping Metadata

{% hint style="info" %}
This feature is available from _MariaDB 10.6.0._
{% endhint %}

Prepared statement metadata, which typically remains unchanged except during table alterations, can be cached by clients when the `MARIADB_CLIENT_CACHE_METADATA` capability is enabled. The server won't then send them again, unless they change. This significantly improves the performance of subsequent executions, especially for large metadata sets.

When `MARIADB_CLIENT_CACHE_METADATA` capability is set, the result set [Column count packet](4-server-response-packets/result-set-packets.md#column-count-packet) format indicates if metadata follows or is skipped:

* int column count,
* if (`MARIADB_CLIENT_CACHE_METADATA` capability set) int<1> metadata follows (0 / 1).

**Example**

Java code:

```java
stmt.execute("CREATE TABLE test_table (id int, val varchar(32))");
stmt.execute("INSERT INTO test_table VALUES (1, 'a'), (2, 'b')");
try (PreparedStatement prep = sharedConnBinary.prepareStatement("SELECT * FROM test_table WHERE id = ?")) {
    prep.setInt(1, 1);
    prep.executeQuery();
}
```

Results with metadata caching:

```
Column count packet:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 02 00 00 01 02 00                                | ......           |
+------+--------------------------------------------------+------------------+
row:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 08 00 00 02 00 00 01 00  00 00 01 61             | ...........a     |
+------+--------------------------------------------------+------------------+

OK_Packet with a 0xFE header:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 07 00 00 03 FE 00 00 22  00 00 00                | ......."...      |
+------+--------------------------------------------------+------------------+
```

The same, without metadata caching:

```
Column count packet:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 01 00 00 01 02                                   | .....            |
+------+--------------------------------------------------+------------------+

Column Definition packet:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 33 00 00 02 03 64 65 66  05 74 65 73 74 6A 0A 74 | 3....def.testj.t |
|000010| 65 73 74 5F 74 61 62 6C  65 0A 74 65 73 74 5F 74 | est_table.test_t |
|000020| 61 62 6C 65 02 69 64 02  69 64 0C 3F 00 0B 00 00 | able.id.id.?.... |
|000030| 00 03 00 00 00 00 00                             | .......          |
+------+--------------------------------------------------+------------------+

Column Definition packet:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 35 00 00 03 03 64 65 66  05 74 65 73 74 6A 0A 74 | 5....def.testj.t |
|000010| 65 73 74 5F 74 61 62 6C  65 0A 74 65 73 74 5F 74 | est_table.test_t |
|000020| 61 62 6C 65 03 76 61 6C  03 76 61 6C 0C FF 00 80 | able.val.val.... |
|000030| 00 00 00 FD 00 00 00 00  00                      | .........        |
+------+--------------------------------------------------+------------------+

row:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 08 00 00 04 00 00 01 00  00 00 01 61             | ...........a     |
+------+--------------------------------------------------+------------------+

OK_Packet with a 0xFE header:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 07 00 00 05 FE 00 00 22  00 00 00                | ......."...      |
+------+--------------------------------------------------+------------------+
```

## Extended Column Information

{% hint style="info" %}
This feature is available from MariaDB 10.5.2.
{% endhint %}

When the `MARIADB_CLIENT_EXTENDED_METADATA` capability is set, [column definition packet](4-server-response-packets/result-set-packets.md#column-definition-packet) can include additional type and format information.

* For geometric fields: Detailed geometric data type (e.g., 'point', 'polygon').
* For JSON fields: Type 'json'.
* For UUID fields: Type 'uuid'.

## Bulk

{% hint style="info" %}
This feature is available for unit results from [MariaDB 10.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1020-release-notes) or [MariaDB 11.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-1-release-notes), respectively.
{% endhint %}

The `MARIADB_CLIENT_STMT_BULK_OPERATIONS` capability enables the [COM\_STMT\_BULK\_EXECUTE](3-binary-protocol-prepared-statements/com_stmt_bulk_execute.md) command for efficient batch processing. However, note that only one result (`OK` or `ERROR`) is returned per batch, containing the total affected rows and the first auto-generated ID. For individual results, the `MARIADB_CLIENT_BULK_UNIT_RESULTS` capability can be set. The server will then return a result set containing for each unitary results (containing auto generated ids and affected rows).

**Example**

Java code:

```java
Statement stmt = connection.createStatement();
stmt.execute("CREATE TABLE test_table (id int, val varchar(32))");

try (PreparedStatement prep = connection.prepareStatement("INSERT INTO test_table VALUES (?, ?)")) {

    prep.setInt(1, 1);
    prep.setString(2, "a");
    prep.addBatch();

    prep.setInt(1, 2);
    prep.setString(2, "b");
    prep.addBatch();

    prep.executeBatch();
}
```

Client send :

```
MARIADB_CLIENT_STMT_BULK_OPERATIONS:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 1B 00 00 00 FA FF FF FF  FF 80 00 03 00 FD 00 00 | ................ |
|000010| 01 00 00 00 00 01 61 00  02 00 00 00 00 01 62    | ......a.......b  |
+------+--------------------------------------------------+------------------+
```

Server response:

```
OK_Packet:
       +--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| 2E 00 00 01 00 02 00 02  00 00 00 26 52 65 63 6F | ...........&Reco |
|000010| 72 64 73 3A 20 32 20 20  44 75 70 6C 69 63 61 74 | rds: 2  Duplicat |
|000020| 65 73 3A 20 30 20 20 57  61 72 6E 69 6E 67 73 3A | es: 0  Warnings: |
|000030| 20 30                                            |  0               |
+------+--------------------------------------------------+------------------+
```

## Authentication Plugins

MariaDB has specific authentication methods.

* [ED25519 plugin](1-connecting/connection.md#client_ed25519-plugin)
* [PARSEC plugin](1-connecting/connection.md#parsec-plugin) (from MariaDB 11.6.1)
* [GSSAPI plugin](1-connecting/connection.md#auth_gssapi_client-plugin)

## Redirection

{% hint style="info" %}
This feature is available from MariaDB 11.3.1 or MaxScale 25.08.0, respectively.
{% endhint %}

MariaDB permits [connection redirection](../../ha-and-performance/connection-redirection-mechanism-in-the-mariadb-clientserver-protocol.md).

**Use Cases**

* Proxy Scenarios: Connection redirection is particularly beneficial when multiple servers share a single proxy.
* Server Management: This feature can also be used during planned server shutdowns or restarts, allowing for a graceful transition to a new server.

Connectors can support 2 different levels:

* On Connection Creation only: The redirection information is included in the initial [OK\_Packet](4-server-response-packets/ok_packet.md#server-status-flag) sent by the server to the client. This allows the client to connect directly to the target server immediately.
* Anytime Redirection: If redirection information becomes available later, the connector can handle it based on the existing transaction state.
  * No Transaction: If no transaction is in progress, the connector can redirect the connection directly.
  * Transaction in Progress: If a transaction is ongoing, the redirection information is stored until the transaction is completed. The transaction state is determined using server status flags like `SERVER_STATUS_IN_TRANS` in the "`OK_Packet`," "`ERR_Packet`," or "`EOF_Packet`."

## Zero-Configuration SSL

{% hint style="info" %}
This feature is available from MariaDB 11.4.1.
{% endhint %}

A feature that enables TLS certificate validation without requiring client-side certificate configuration.

### Limitations

* Requires a nonempty password.
* Only supports the following authentication methods:
  * `mysql_native_password`
  * `client_ed25519`
  * `parsec`

### Operational Mechanism

#### **Server-Side Process**

1. When no SSL certificates are pre-configured, the server automatically generates a temporary self-signed certificate.
2. During connection establishment, the server embeds a special validation hash in the connection's "OK\_Packet" information field.

#### **Client-Side Process**

1. The client connector must postpone SSL error handling until the connection phase is complete.
2. The client captures and stores the SHA256 fingerprint of the server's certificate.
3. If SSL errors occur, the client can only use specific authentication plugins (`mysql_native_password`/`ed25519`/`parsec`) to prevent potential password exposure.
4. At connection conclusion, the server sends an OK\_Packet with a validation hash.
5. The client generates a hash using:

* The password hash;
* The server's seed;
* Stored certificate fingerprint.

{% hint style="warning" %}
The SSL-error connection proceeds only if the client-generated hash matches the server-provided hash.
{% endhint %}

#### Password Hash Generation Methods

* `mysql_native_password`:
  * Hash generation: `SHA1`(`SHA1`(password)).
* `ed25519`:
  * Uses the Ed25519 cryptographic algorithm for hash generation.
* `parsec`:
  * Hash generation involves combining
    * 'P' character;
    * Number of iterations;
    * Salt;
    * Raw public key.

## Initial Session Tracking

MySQL and MariaDB support session tracking when the `CLIENT_SESSION_TRACK` capability is set.

{% hint style="info" %}
One difference is that, since MariaDB 11.5.1, connection ending `OK_Packet` lists all the current variables of tracked variable.
{% endhint %}

This is useful for connectors which have a method to set the transaction type, retrieving database for example to always have the server current value when changed. This permit to avoid executing some queries when not needed

Example of ending connection `OK_Packet` :

```
+--------------------------------------------------+
       |  0  1  2  3  4  5  6  7   8  9  a  b  c  d  e  f |
+------+--------------------------------------------------+------------------+
|000000| A6 00 00 02 00 00 00 02  40 00 00 00 9D 00 0E 0A | ........@....... |
|000010| 61 75 74 6F 63 6F 6D 6D  69 74 02 4F 4E 00 11 09 | autocommit.ON... |
|000020| 74 69 6D 65 5F 7A 6F 6E  65 06 53 59 53 54 45 4D | time_zone.SYSTEM |
|000030| 00 1D 14 63 68 61 72 61  63 74 65 72 5F 73 65 74 | ...character_set |
|000040| 5F 63 6C 69 65 6E 74 07  75 74 66 38 6D 62 34 00 | _client.utf8mb4. |
|000050| 21 18 63 68 61 72 61 63  74 65 72 5F 73 65 74 5F | !.character_set_ |
|000060| 63 6F 6E 6E 65 63 74 69  6F 6E 07 75 74 66 38 6D | connection.utf8m |
|000070| 62 34 00 1E 15 63 68 61  72 61 63 74 65 72 5F 73 | b4...character_s |
|000080| 65 74 5F 72 65 73 75 6C  74 73 07 75 74 66 38 6D | et_results.utf8m |
|000090| 62 34 00 0E 0C 72 65 64  69 72 65 63 74 5F 75 72 | b4...redirect_ur |
|0000a0| 6C 00 01 06 05 74 65 73  74 6A                   | l....testj       |
+------+--------------------------------------------------+------------------+
```

It indicates:

* autocommit = ON
* time\_zone = SYSTEM
* character\_set\_client = utf8mb4
* character\_set\_connection = utf8mb4
* character\_set\_results = utf8mb4
* redirect\_url =

A connector knows that `character_set_client` set to `utf8mb4`, then could avoid executing a command like "`SET NAMES utf8mb4`".

## MySQL Features Not Supported

* The X protocol is not supported.

Unsupported features and associate capabilities:

* `CLIENT_OPTIONAL_RESULTSET_METADATA`: permits setting no `METADATA` at all for a connection. See [Prepare statement skipping metadata](mariadb-protocol-differences-with-mysql.md#prepare-statement-skipping-metadata)'s MariaDB implementation choice.
* `CLIENT_QUERY_ATTRIBUTES` adds some metadata attributes
* `CLIENT_ZSTD_COMPRESSION_ALGORITHM` permits zstd compression
* `MULTI_FACTOR_AUTHENTICATION` Multifactor Authentication capability.

## TIPS

### Identifying MariaDB Server

MariaDB connectors use specific criteria to determine if a server is a MariaDB instance during the initial handshake process.

The two key indicators used are:

* Missing `CLIENT_MYSQL` capability: MariaDB does not set the `CLIENT_MYSQL` capability flag in the initial handshake packet.
* Server version string: The server's version string is examined for the presence of the word "mariadb" (ignoring case sensitivity).

The reason is that some features like using `COM_RESET_CONNECTION` has no capability, and depend on the MySQL or MariaDB server version.

### Pipelining Prepare Execute

Connectors usually follow a two-step process for prepared statements:

1. Prepare: Send a [COM\_STMT\_PREPARE](3-binary-protocol-prepared-statements/com_stmt_prepare.md) command to the server, receiving a statement ID in response.
2. Execute: Send a [COM\_STMT\_EXECUTE](3-binary-protocol-prepared-statements/com_stmt_execute.md) command, using the statement ID obtained in the previous step.

When the server support `MARIADB_CLIENT_STMT_BULK_OPERATIONS` capability, a specific statement ID value of `-1` (or 0xffffffff in hexadecimal) can be used to indicate that the previously prepared statement can be reused. This enables connectors to pipeline the preparation and execution steps into a single request:

* Send a [COM\_STMT\_PREPARE](3-binary-protocol-prepared-statements/com_stmt_prepare.md) then a [COM\_STMT\_EXECUTE](3-binary-protocol-prepared-statements/com_stmt_execute.md) with statement ID `-1` (0xffffffff) commands to the server.
* Read the prepare and execute responses.

If the [COM\_STMT\_PREPARE](3-binary-protocol-prepared-statements/com_stmt_prepare.md) command returns an error (`ERR_Packet`), the subsequent [COM\_STMT\_EXECUTE](3-binary-protocol-prepared-statements/com_stmt_execute.md) with statement ID `-1` also fails and returns an error.

By eliminating the round trip for the separate `COM_STMT_EXECUTE` command, this approach improves performance for the first execution.

Traditionally, connectors send [COM\_STMT\_PREPARE](3-binary-protocol-prepared-statements/com_stmt_prepare.md), wait for results, then execute [COM\_STMT\_EXECUTE](3-binary-protocol-prepared-statements/com_stmt_execute.md) with `statement_id` received from the prepare result.

This description is for [COM\_STMT\_EXECUTE](3-binary-protocol-prepared-statements/com_stmt_execute.md), but [COM\_STMT\_BULK\_EXECUTE](3-binary-protocol-prepared-statements/com_stmt_bulk_execute.md) works exactly the same way.

### Query Timeout

A timeout for all commands can be set using `SET max_statement_time=XXX` with XXX in seconds.

Setting it for a specific query can be done using `SET STATEMENT max_statement_time=XXX FOR ...`

### Collations

Connectors don't care about collations, but normally want to ensure charset in connection exchanges.

The only good solution is to use `SET NAMES utf8mb4` or `SET NAMES utf8mb4 COLLATE someUtf8mb4collation` .

If they support session tracking, connectors can check if the character set of initially tracked variable `character_set_connection` corresponds to the expected value, then permit skipping this `SET NAMES` statement ( 'server default collation' from [initial handshare packet](1-connecting/connection.md#initial-handshake-packet) cannot be trusted, since truncated to one byte. Recent mysql and mariadb collation can go on 2 bytes).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
