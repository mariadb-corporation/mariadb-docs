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
Because an encryption change re-encrypts every row, TideSQL runs it as a table copy rather than an instant, in-place operation. An `ALTER TABLE ... ENCRYPTED=YES, ALGORITHM=INSTANT` is rejected for this reason.
{% endhint %}

## Interaction With Compression and Indexes

Encryption composes with everything else, including secondary indexes, BLOB columns, and TTL. The secondary-index keys are not encrypted, because they must stay comparable for seeking, but the row data those keys point at is encrypted in the data column family. Because ciphertext does not compress, the engine forces the data column family's compression to `NONE` regardless of the table's `COMPRESSION` option, and the index CFs are unaffected. See [TideSQL Table Options](tidesql-table-options.md) for the compression interaction.

## Key Rotation and Failure Handling

If `encryption_key_get()` cannot return the requested key, a rotation hole, a keyring plugin that is not loaded, or a version that never existed, the encrypt or decrypt call fails closed. The engine logs the failure and returns an error to the SQL layer rather than feeding uninitialized bytes into the cipher. A row written with a key version no longer in the keyring is unreadable until the key is restored, and the engine never silently mis-encrypts or returns zeroed plaintext.

<sub>_This page is licensed: GPLv2_</sub>
