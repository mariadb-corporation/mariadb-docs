---
description: How mariadb-backup backs up and restores encrypted data files.
---

# Encrypted Files Backup (mariadb-backup)

This page addresses a major misconception: Many users assume that, because `mariadb-backup` reads encrypted files, it "unlocks" them. However, the encryption remains intact throughout the entire lifecycle, as explained in the following.

## Compatibility with Data-at-Rest Encryption (TDE)

While [this page](using-encryption-and-compression-tools-with-mariadb-backup.md) primarily discusses using external tools like `openssl` to encrypt a backup stream, `mariadb-backup` is also fully compatible with MariaDB's internal data-at-rest encryption (TDE) for InnoDB and Aria tables.

When backing up a server where encryption is enabled, there are specific behaviors and requirements during the backup, prepare, and restore phases.

### 1. The Backup Phase

When `mariadb-backup` performs a backup, it copies the physical files exactly as they exist on disk. If the files are encrypted at rest by the MariaDB server, the backup files remain encrypted.

* **No "double encryption" required:** You do not _need_ to pipe the backup through `openssl` to secure it, as the data is already encrypted. However, you may still choose to do so for additional security or to encrypt non-InnoDB files (like configuration files or metadata).
* **Key Access:** `mariadb-backup` must be able to read the encrypted files. In order to do that, `mariadb-backup` queries the server as to what encryption plugin is used:

{% code overflow="wrap" %}
```sql
SELECT plugin_name, plugin_library, @@plugin_dir FROM information_schema.plugins WHERE plugin_type='ENCRYPTION';
+---------------------+------------------------+---------------------------------------+
| plugin_name         | plugin_library         | @@plugin_dir                          |
+---------------------+------------------------+---------------------------------------+
| file_key_management | file_key_management.so | /opt/homebrew/opt/mariadb/lib/plugin/ |
+---------------------+------------------------+---------------------------------------+
```
{% endcode %}

Once `mariadb-backup` knows that `file_key_management` is used, it queries the server for details, like the location of the key file, and which encryption algorithm is used:

```sql
SHOW VARIABLES LIKE 'file_key_management%';                                                                 +------------------------------------------+------------------------------------------------+
| Variable_name                            | Value                                          |
+------------------------------------------+------------------------------------------------+
| file_key_management_digest               | sha1                                           |
| file_key_management_encryption_algorithm | aes_ctr                                        |
| file_key_management_filekey              |                                                |
| file_key_management_filename             | /opt/homebrew/etc/mysql/encryption/keyfile.txt |
| file_key_management_use_pbkdf2           | 0                                              |
+------------------------------------------+------------------------------------------------+
```

`mariadb-backup` uses that information to calculate the checksums of `.ibd` files/pages, and to decrypt the redo log for further information.

### 2. The Prepare Phase

The "Prepare" phase is when `mariadb-backup` makes the data consistent by applying the redo logs.

* **Requirement:** To perform the prepare phase, the tool _must_ have access to the same encryption keys used by the server at the time of the backup.
* **Persistence:** After the prepare phase is complete, the data files _remain encrypted_. The tool does not "decrypt" the database into plain text; it only ensures the encrypted pages are consistent.

### 3. The Restore Phase

The restore phase simply moves the encrypted files back to the target server's data directory.

{% hint style="warning" %}
**CRITICAL LIMITATION:** A restore is **only** successful if the target server is configured with the **exact same keys** and KMS method used by the original server. If the target server has a different key or cannot load the key management plugin, the MariaDB service fails to start, or tables are marked as "corrupted" because the engine cannot decrypt the pages.
{% endhint %}

## TDE Backup Requirements Checklist

To ensure a restorable backup of an encrypted MariaDB instance, you must:

1. **Access to encryption information:** Ensure that `mariadb-backup` has the same access to encryption information as the server does.
2. **Back up the keys:** The encryption keys themselves are **not** stored inside the backup. You must manually back up your `keyfile.txt`, AWS KMS credentials, or HashiCorp Vault tokens separately.
3. **Synchronize target keys:** Before running `mariadb-backup --copy-back`, verify that the destination server’s configuration points to the identical keys used during the backup.

### Key Takeaways

* **Data State:** Encrypted at source → Encrypted in backup → Encrypted at destination.
* **Prepare Phase:** Needs the key to read/apply logs, but writes encrypted data back out.
* **Restoration:** If you lose your keys, your backup is permanently unrecoverable.

## Mixed-Encryption Backups

Mixed-encryption backups are a common scenario, especially in large production environments where a full "rotation" (encrypting all old data) can take days or weeks.

`mariadb-backup` is "smart" enough to handle a mixed-state tablespace.

When you run a backup on a mixed-encryption database, here is exactly what happens under the hood:

### 1. File-by-File Detection

`mariadb-backup` reads the _header_ of every tablespace file (`.ibd` files). Each header contains metadata that tells the tool whether that specific file is encrypted or plain text.

* If the header says "Encrypted," the tool uses the configured KMS keys to read the pages.
* If the header says "Plain Text," it reads them normally.

### 2. Preservation of State

The backup is an exact physical replica. This means:

* **Table A (Encrypted)** stays encrypted in the backup.
* **Table B (Unencrypted)** stays unencrypted in the backup. The backup does not "standardize" the encryption; it respects the individual state of each table at the exact moment the backup started.

### 3. The Prepare Phase in a Mixed Environment

This is where the KMS[^1] configuration is vital. During the "Prepare" phase (`--prepare`), `mariadb-backup` applies the Redo Log to the tables to ensure consistency.

* If a transaction in the Redo Log involves an _encrypted_ table, the tool uses the keys to apply that change.
* If the transaction involves an _unencrypted_ table, it applies it without keys.
* **The Result:** After the prepare phase, your backup remains in a mixed state, exactly matching the original source.

## Key Limitations & Risks for Mixed Backups

| Scenario           | Behavior                                                                                               | Risk                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **Missing Keys**   | The backup fails or the `prepare` phase crashes when it hits the first encrypted table.                | Even if 99% of your tables are unencrypted, 1 encrypted table requires the KMS to be active for the backup to be valid. |
| **New Tables**     | If you enable encryption _during_ a long-running backup, `mariadb-backup` handles it via the Redo Log. | Ensure the key used for the new table is the same one available to the backup tool.                                     |
| **Restore Target** | You restore to a server without a KMS plugin.                                                          | The unencrypted tables work fine, but the encrypted tables are unreadable/corrupted.                                    |

{% hint style="info" %}
**Note on Mixed Environments:** `mariadb-backup` supports databases containing a mix of encrypted and unencrypted tables. The tool detects the encryption status of each tablespace individually. However, if even a single table in the backup is encrypted, the **entire** `--prepare` process requires access to the Key Management System (KMS). Without valid keys, the tool cannot verify the consistency of encrypted tables, and the backup preparation fails.
{% endhint %}

## Handling Mixed-Encryption Environments

In many production environments, a database may contain a mix of encrypted and unencrypted tables. This occurs frequently during a rolling migration to TDE or when only specific sensitive tables are targeted for encryption.

### **1. Tablespace Detection**

`mariadb-backup` detects the encryption status of each tablespace individually by reading the file headers. It does not "force" encryption on unencrypted tables, nor does it decrypt encrypted ones. The backup is an exact physical replica of the source's mixed state.

### **2. The Prepare Phase Requirement**

Even if only one table in your database is encrypted, the **entire** `--prepare` phase requires the Key Management System (KMS) to be active and configured. The tool must be able to read the encryption keys to apply redo logs and ensure consistency across the entire dataset. If the KMS is unavailable, the prepare phase fails.

### **3. Best Practice: Layered Encryption**

Because a mixed-state backup leaves unencrypted tables (and database metadata) vulnerable in the backup file, it is a recommended best practice to use **Layered Encryption**.

By piping the `mariadb-backup` stream through an external encryption tool (like OpenSSL), you ensure that:

* **Legacy/Unencrypted tables** are protected within the backup archive.
* **Metadata** (file names, schemas, and logs) is hidden.
* **Transport Security** is maintained regardless of the destination server's TDE configuration.

#### **Example: Encrypting a Mixed-State Backup Stream**

{% code overflow="wrap" %}
```bash
mariadb-backup --backup --stream=xbstream | \ openssl enc -aes-256-cbc -k $BACKUP_PASSWORD > full_secure_backup.xb.enc
```
{% endcode %}

{% hint style="warning" %}
**Warning:** When using Layered Encryption, the restoration process requires **two** sets of credentials: the external password/key to decrypt the stream, and the MariaDB KMS keys to prepare and run the database. Loss of either set renders the backup unrecoverable.
{% endhint %}

## Summary of TDE Backup Behavior

| Component                  | State in Backup           | Requires KMS for Prepare?      |
| -------------------------- | ------------------------- | ------------------------------ |
| **Encrypted InnoDB Table** | Encrypted                 | **Yes**                        |
| **Plaintext InnoDB Table** | Plaintext                 | **Yes** (to initialize engine) |
| **Aria System Tables**     | Encrypted (if configured) | **Yes**                        |
| **Binary / Redo Logs**     | Encrypted (if configured) | **Yes**                        |
| **Backup Metadata**        | Plaintext                 | No                             |

[^1]: Key Management System
