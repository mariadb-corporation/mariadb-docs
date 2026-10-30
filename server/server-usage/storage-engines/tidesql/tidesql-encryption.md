---
description: >-
  Per-row data-at-rest encryption in TideSQL through MariaDB key management,
  including key versions and how encryption interacts with compression and
  indexes.
---

# TideSQL Data-at-Rest Encryption

TideSQL can encrypt row data before it is written to the column family. Encryption uses MariaDB's key management infrastructure, so it works with any configured key management plugin such as `file_key_management`.

```sql
CREATE TABLE secrets (
  id INT NOT NULL PRIMARY KEY, val VARCHAR(100)
) ENGINE=TIDESDB `ENCRYPTED`=YES;
```

## On-Disk Format

Each row is encrypted individually. The on-disk record is a 4-byte little-endian key version, then a 16-byte random IV, then the ciphertext. The key-version prefix lets the engine decrypt rows that were written under an older key after a rotation, because `encryption_key_get(key_id, key_version)` resolves the exact key bytes used at write time. On read, the engine decrypts transparently.

## Choosing the Key ID

You can choose the key id:

```sql
CREATE TABLE classified (
  id INT NOT NULL PRIMARY KEY, data TEXT
) ENGINE=TIDESDB `ENCRYPTED`=YES `ENCRYPTION_KEY_ID`=2;
```

`ENCRYPTION_KEY_ID` defaults to 1 and ranges from 1 to 255.

## Encrypting an Existing Table

Encryption can be turned on for an existing table. The change rewrites the table through a copy so the current rows are stored as ciphertext:

```sql
ALTER TABLE existing_table `ENCRYPTED`=YES;
```

{% hint style="info" %}
Because an encryption change re-encrypts every row, TideSQL runs it as a table copy rather than an instant, in-place operation. An `ALTER TABLE ... ENCRYPTED=YES` with `ALGORITHM=INSTANT` or `ALGORITHM=INPLACE` is rejected for this reason, and so is turning encryption off.
{% endhint %}

Changing `ENCRYPTION_KEY_ID` on an encrypted table also copies the table and re-encrypts every row under the new key, and `ALGORITHM=INSTANT` or `INPLACE` is refused for it. A row carries its key version but not its key id, and is decrypted with the table's key id, so the existing rows cannot be left under the old one. An unencrypted table may change its key id instantly, since nothing is yet encrypted with it.

## Interaction With Compression and Indexes

Encryption composes with everything else, including secondary indexes, BLOB columns, and TTL. Only the row data in the data column family is encrypted. Index entries stay in plaintext because they must stay comparable for seeking: secondary-index keys hold the indexed column values, `FULLTEXT` entries hold the document's tokens, and `SPATIAL` entries hold each geometry's bounding box. Because ciphertext does not compress, the engine forces the data column family's compression to `NONE` regardless of the table's `COMPRESSION` option, and the index CFs are unaffected. See [TideSQL Table Options](tidesql-table-options.md) for the compression interaction.

## Key Rotation and Failure Handling

Opening an encrypted table fails if the key management plugin has no current version of the table's key id. The client sees the table as missing (`HA_ERR_NO_SUCH_TABLE`), and the error log records `encryption key N not available`.

If `encryption_key_get()` cannot return the requested key for a single row, a rotation hole, a keyring plugin that is not loaded, or a version that never existed, the encrypt or decrypt call fails closed and logs the failure rather than feeding uninitialized bytes into the cipher:

* On the write path, the `INSERT` or `UPDATE` fails with an error, so the engine never stores a row it could not encrypt.
* On the read path, the statement fails with handler error 192 (decryption failed), so a row written with a key version no longer in the keyring cannot be read until the key is restored, and the statement does not return it with wrong contents.
* An in-place `ADD INDEX` that meets such a row stops and leaves the table unchanged.

Watch the error log for `encryption_key_get failed` after a key rotation.

The envelope carries no integrity check, so encryption keeps row data confidential but does not authenticate it. If the keyring returns different bytes for a key id and version than the rows were written with, reading those rows fails with error 192 as above, except that roughly one row in 256 still passes the cipher's padding check and is returned with wrong contents instead of an error.

<sub>_This page is licensed: GPLv2_</sub>
