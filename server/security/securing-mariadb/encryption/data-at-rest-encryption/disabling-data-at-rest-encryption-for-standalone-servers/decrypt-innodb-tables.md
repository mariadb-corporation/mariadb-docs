# Decrypt InnoDB Tables

When **data-at-rest encryption** is enabled, InnoDB tables and tablespaces are transparently encrypted and decrypted by the storage engine. In some cases, administrators may need to **decrypt an InnoDB table**—for example, when migrating data to an environment where encryption is not required, or when disabling encryption to simplify configuration.



{% hint style="info" %}
For more information, refer to, [MDEV-17269](https://jira.mariadb.org/browse/MDEV-17269).
{% endhint %}

### Decrypting a Table

To decrypt a specific InnoDB table, use the `ENCRYPTION` clause with `ALTER TABLE`:

```sql
ALTER TABLE mydb.mytable ENCRYPTION='N';
```

This statement rewrites the table in an unencrypted format.

* If the table is stored in a **file-per-table tablespace**, the corresponding `.ibd` file is decrypted and rewritten.
* If the table resides in the **system tablespace**, the data is also rewritten unencrypted.

### Decrypting All Tables in a Schema

To decrypt all tables in a schema, you can generate and run `ALTER TABLE` statements programmatically:

```sql
SELECT CONCAT('ALTER TABLE ', table_schema, '.', table_name, ' ENCRYPTION="N";')
FROM information_schema.tables
WHERE engine='InnoDB'
  AND table_schema='mydb';
```

Copy and execute the generated statements.

### Verifying Decryption

After decryption, you can verify the encryption status of a table with:

```sql
SELECT table_name, create_options
FROM information_schema.tables
WHERE table_schema='mydb';
```

If the table is unencrypted, the `create_options` column will not include `ENCRYPTION="Y"`.
