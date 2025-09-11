# Decrypt InnoDB Redo Logs

When **data-at-rest encryption** is enabled in MariaDB Enterprise Server, InnoDB can encrypt redo logs. If you later disable encryption or need to recover data from encrypted redo logs, you may need to **decrypt the redo log files** before MariaDB can process them.

{% hint style="info" %}
For more information, refer to [MDEV-17270](https://jira.mariadb.org/browse/MDEV-17270).
{% endhint %}

1.  **Stop MariaDB Enterprise Server**

    ```bash
    sudo systemctl stop mariadb
    ```
2.  **Locate the redo log files**\
    By default, InnoDB redo log files are stored in the data directory, typically as:

    ```
    ib_logfile0
    ib_logfile1
    ```

    or in the `#innodb_redo` directory for MariaDB versions using the new redo log format.
3.  **Prepare configuration for decryption**

    * Make sure `innodb_redo_log_encrypt` is set to `ON` (to ensure the redo logs are recognized as encrypted).
    * Ensure that the key management plugin (such as `file_key_management` or `aws_key_management`) is configured exactly as it was when the redo logs were created.

    Example:

    ```ini
    [mysqld]
    plugin_load_add = file_key_management
    file_key_management_filename = /etc/mysql/encryption/keyfile.enc
    file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
    innodb_redo_log_encrypt = ON
    ```
4.  **Start MariaDB with decryption enabled**

    * Start the server normally. MariaDB will automatically attempt to decrypt redo logs at startup using the configured key management plugin.
    * If successful, the redo logs are decrypted on-the-fly and crash recovery proceeds.

    ```bash
    sudo systemctl start mariadb
    ```
5.  **Disable redo log encryption if no longer required**\
    After recovery or once you confirm that decrypted redo logs are no longer needed, you can disable redo log encryption in the configuration:

    ```ini
    [mysqld]
    innodb_redo_log_encrypt = OFF
    ```

    Then restart the server. New redo logs will be created in plaintext.

### Verification

You can verify the redo log encryption status with:

```sql
SHOW GLOBAL VARIABLES LIKE 'innodb_redo_log_encrypt';
```

Example output:

```
+------------------------+-------+
| Variable_name          | Value |
+------------------------+-------+
| innodb_redo_log_encrypt| OFF   |
+------------------------+-------+
```

###
