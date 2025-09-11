# Canary Testing

For canary testing new versions of an application, there are some tools to work with, but it has to be said that this is hardly ever 100% clear. If we assume that the advice above has been followed to some extent, then the following are some tools to work with.

## Database Naming

In a MariaDB instance, there is the concept of a database, which is similar to a schema. A database is a kind of namespace, which means that an object, say a table, in one database may have the same name as an object in some other database in the same instance. Given this, databases are a key to allowing somewhat different schemas to coexist, which in turn means that it is good practice not to hard-code the database name in applications or schema objects, unless this makes sense.

## Views

Views are an excellent way of hiding complexities, and a good way of dealing with this is to have a separate database for a new version with `VIEW`s referencing the actual data in some other database.

```sql
MariaDB> USE prod_v2;
MariaDB> CREATE VIEW `orders_t` AS
  SELECT `order_id`, `order_date` FROM `prod_v1`.`orders_t`;
```

When adding a new version of the schema/application, it is sometimes necessary to migrate the data to the new schema and have a `VIEW` in the "old" schema referencing the new one. A view is not always necessary in this case, but any added columns have to be handled by a trigger or by a sensible default.

```sql
MariaDB> USE prod_v2;
MariaDB> CREATE TABLE `orders_t`(
  `order_id` INTEGER NOT NULL PRIMARY KEY,
  `order_date` DATETIME NOT NULL,
  `customer_id` INTEGER NOT NULL DEFAULT 0);
MariaDB> INSERT INTO `orders_t` SELECT `order_id`, `order_date`
  FROM `prod_v1`.`orders_t`;

MariaDB> USE prod_v1;
MariaDB> RENAME TABLE `orders_t` TO `orders_t_v1`;
MariaDB> CREATE VIEW `orders_t` AS
  SELECT `order_id`, `order_date` FROM `prod_v2`.`orders_t`;
```

## Replication

A good way of dealing with canary testing with MariaDB is to use replication, which works even in cases with schemas that are different, to an extent, if statement-based replication (SBR) is used. Using this, a new version is built on one server and a new schema is installed there. This is then set to replicate from the current production system. This is not likely to work for all cases, but in many cases, this is a useful tool to allow for canary testing.

## Invisible Columns

Hidden or invisible columns in MariaDB are a feature that allows a column to exist in a table without being exposed by default, for instance a `SELECT *` or an `INSERT` without column names will not touch this column. If the advice given in the previous sections of the document is followed, then this should not be necessary much, but in some cases, it is still a useful feature.

For example, in the example above with the orders\_t table, if it is the case that the current application actually does `INSERT` without specifying the columns to insert into, then a new column, say customer\_id, cannot be added. We can then use an invisible column to support this application, including a new version that does use column names in the `INSERT` and also use the customer\_id column:

<pre class="language-sql"><code class="lang-sql">MariaDB> USE prod_v1

MariaDB> ALTER TABLE `orders_t`
  ADD `customer_id` INTEGER NOT NULL DEFAULT 0 INVISIBLE;
MariaDB> SELECT * FROM `orders_t`;
+----------+---------------------+
| order_id | order_date          |
+----------+---------------------+
|        1 | 2024-05-17 18:01:01 |
|        2 | 2025-12-12 18:44:08 |
+----------+---------------------+
2 rows in set (0.004 sec)
<strong>
</strong><strong>MariaDB> INSERT INTO `orders_t`
</strong>  (`order_id`, `order_date`, `customer_id`) VALUES(3, NOW(), 2);
</code></pre>

## See Also

* [Database](../../reference/sql-functions/secondary-functions/information-functions/database.md)
* [Views](../../server-usage/views/)
* [Replication](../../ha-and-performance/standard-replication/)
* [Invisible columns](canary-testing.md#invisible-columns)
