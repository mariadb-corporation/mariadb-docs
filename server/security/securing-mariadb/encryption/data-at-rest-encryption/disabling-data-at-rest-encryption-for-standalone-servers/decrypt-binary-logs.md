# Decrypt Binary Logs

This page covers how to confirm that binlogs are encrypted, recommended approaches for getting decrypted output.

When binary log encryption is enabled, the server writes binlog files to disk in encrypted form. This ensures that anyone with direct access to the filesystem cannot read the contents.

The encryption keys are managed through a keyring or key-management plugin. Whenever the server itself needs to access a binlog—such as during replication, recovery, or when tools like **mysqlbinlog** connect to it—the server transparently decrypts the events using the appropriate active keys.

Since the keys are stored in a server-accessible keyring, the most reliable and secure method to access decrypted binlog data is to request it directly from the running server. In other words, instead of trying to decrypt raw encrypted files offline, you should allow the server to stream already-decrypted events to you.

{% hint style="info" %}
For more information, refer to [MDEV-17271](https://jira.mariadb.org/browse/MDEV-17271).
{% endhint %}

### Approaches to decrypt binary logs

There are two common approaches depending on where you run the decryption and how keys are stored:

1. **Run `mysqlbinlog` on a server that already has access to the key material (recommended).**
   * The server's key provider configuration (for example, a mounted key file or KMS credentials) is already present, so `mysqlbinlog` inherits the ability to open and decrypt logs.
   * This reduces key distribution since the keys remain on the server.
2. **Copy encrypted binlog files to an admin workstation and decrypt locally.**
   * Requires secure transfer of the encrypted binlog file(s) and the decryption key or key-access configuration to the workstation.
   * Use this only when you can ensure secure temporary storage and key handling.

### Using `mysqlbinlog` to decrypt

`mysqlbinlog` will attempt to decrypt binary logs when launched in an environment that allows it to access the same key provider configuration used by the server.

**Basic example (server with key access):**

```sql
# On the MariaDB server (or a host with access to key material)mysqlbinlog /var/lib/mysql/binlog.000012 > decrypted.sql
```

If the environment is correctly configured, `mysqlbinlog` will read, decrypt, and write the plaintext SQL (events) to `decrypted.sql`.

### Decrypting compressed or rotated logs

If your environment compresses or rotates binary logs outside the standard server rotation, decompress the file before passing to `mysqlbinlog` (or use process substitution):

```sql
gzip -dc /backup/binlog.000012.gz | mysqlbinlog - > decrypted.sql
```

#### Decrypt local binlog to file:

```
mysqlbinlog /var/lib/mysql/binlog.000012 > /tmp/binlog.000012.sql
```

#### Decrypt and decode row events verbosely:

```
mysqlbinlog --base64-output=DECODE-ROWS --verbose /var/lib/mysql/binlog.000012 > /tmp/binlog.decoded.sql
```

#### Decrypt from a compressed backup:

```
gzip -dc /backup/binlog.000012.gz | mysqlbinlog - > /tmp/binlog.000012.sql
```
