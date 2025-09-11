# Database Design

## Overview

The design of the database is a key here; a well-designed database with appropriate relationships, naming, etc., is still a solid foundation to build a structure on, but as things evolve, it will change with the application. The task is to implement necessary changes, but also to consider future enhancements in the design of the database.

## Standardization

To make a database schema easy to maintain, it is best to adhere to some kind of naming standard. What this standard is has less importance than ensuring that it is adhered to. Some like to prefix a name with the type indicator, some like to suffix it, and others ignore this; whichever is your preference, stick to it.

```sql
CREATE TABLE `orders_t`(`order_id` BIGINT NOT NULL PRIMARY KEY,
   `order_date` DATETIME NOT NULL,
   `customer_id` BIGINT NOT NULL,
   FOREIGN KEY(`customer_id`) REFERENCES `customer_t`(`customer_id`));

```

In addition, sticking to a standard for data types to use, including character sets and collations, is a good practice.

## Database Data Types

The data types used really need careful consideration. There are performance aspects here, but in addition, the ease of upgrading the schema should also be considered. Any data type has limitations in and of themselves, and in many cases, limits are introduced as part of a column definition, such as the maximum length of string types and the precision of numeric datatypes.

### Choosing an Appropriate Data Type

In some cases, a suitable data type is obvious; in other cases, this is not the case. Take, for example, a product code consisting of 8 digits; is it best stored as an `INTEGER` or as a `VARCHAR(8)`? The former will be more compact in storage and will be faster, the latter less so. Also, are leading zeros significant? If this is the case, then an `INTEGER` is likely not a good option. Actually, in general, if you are not computing a number, it is likely better to be stored as a string.

### Text / String Data Types

The most common text data types are variable length, so in general, there is no need to be conservative when sizing a `VARCHAR`, for example. In MariaDB, there is a limit on the total row size of a table, and in this calculation, the maximum size of `VARCHAR` is used, so this might be a reason not to extend this too much. In some cases, you know the maximum length of a `VARCHAR` column, and in that case, it should be used, of course, but be careful, as things might change over time, say some code of some kind might be extended in the future.

In other situations, you cannot really tell what the maximum might be, say a name, then make sure that there is ample space available, having to upgrade a schema just because you have to extend the size of a `VARCHAR` column is unnecessary.

#### **Character Sets and Collations**

One issue that needs to be considered is what character set to use for text strings. In most cases, it is recommended that UTF-8 be used, but note that MariaDB has a few options here; either you can use 3-byte UTF-8, called utf8mb3, which allows for 2-byte Unicode or 4-byte, called utf8mb4, which allows full Unicode support. When you use UTF-8, though, remember that storage of strings might be longer. MariaDB ensures that space is allocated as appropriate, but the max potential length of a `VARCHAR(8)` string using utf8mb3 will be 24 bytes,  and when it comes to calculating the maximum row size, this is calculated as 24, not 8, bytes.

Collations determine how a string is sorted, for example, when an `ORDER BY` is used and when indexes are created. You really do want to avoid upgrading a schema to change the collation of a column in a table, so be careful here.

#### **Best Practices With Regard to String Data Types**

It is recommended that you allow as much space as possible when you don’t know the maximum length of a column in a table. It is recommended to use UTF-8 for string data; it does have some drawbacks, but in the end, it is the best general-use character set. It might be useful to use a single-byte character set in some cases, say when using some alphanumeric code item such as a product code, but mostly you are best off with UTF-8 even here, as mixing different data types makes things unnecessarily complicated.

Similar things can be said for collations; there are few reasons to deviate from using just a single collation for a specific application database from the point of view of creating a schema that can be easily maintained at least. From a performance point of view, there are things to consider when determining which collation to use.

### Numeric Data Types

Numeric data types come in several flavors, from a high level we are looking at integer types, floating point types and fixed-point types. In MariaDB, all numeric types are fixed-size storage. From the point of view of schema maintenance, the first thing to look for when it comes to creating a database schema that will need less maintenance is to ensure that values fit in the types used. `BIGINT` instead of `INTEGER` is often a good idea, in particular when used for auto-generated primary keys.

Another thing to watch out for is `FLOAT` and `DOUBLE`, including aliases for these, as they are floating-point, which means there might be rounding issues. Using these types for monetary values might not always be a good idea.

An alternative to `FLOAT` and `DOUBLE` is to use the fixed-point `DECIMAL` type, which is exact. Note also that in `SQL_MODE=Oracle` in MariaDB, the Oracle type `NUMERIC` is an alias for `DECIMAL`.

### Temporal Data Types

MariaDB has a range of temporal types, from the standard `DATETIME` and `TIMESTAMP` to the more specialised `DATE`, `YEAR` and `TIME`. The by far most used ones are `DATETIME` and `TIMESTAMP`, and there are some things to consider when it comes to maintenance. `DATETIME` and `TIMESTAMP` both store similar values, but there is a difference in that `DATETIME` stores the time as it is, whereas `TIMESTAMP` takes the time zone on the client side into effect.

From a schema maintenance point of view, make sure that you understand how these two types work before using them.

### Other Data Types

Most database systems on the market have types that are specific to that system in particular, in MariaDB, which includes `ENUM` and `SET` types. Some types are little used, like BIT and smaller variations of `INTEGER` types. As for `ENUM` and `SET`, these have some useful attributes in that they, on the one hand, require limited storage, but to extend them with additional values, the schema has to be altered, which might be an issue in many cases.

### Schema Objects

Beyond this, there are other objects to handle when it comes to schema and application maintenance. Here, we will look at some of them from the point of view of creating a schema that allows itself to be maintained with limited effort.

#### Views

Using views has several advantages, and although using views might have performance issues, they provide many advantages when it comes to maintaining a database schema. When considering that, this assumes that the views are created with performance and maintenance in mind.

Very complex queries that might need to be maintained can well be put in views. It may also be advantageous to use views to support different versions of a schema over time; adding a version string to VIEW names might well be a good idea.

```sql
CREATE VIEW orders_v_1
AS
SELECT o.`order_id`, o.`order_date` FROM `orders_t` o;
```

## See Also

* [Data types](../../reference/data-types/)
* [Character sets and collations](../../reference/data-types/string-data-types/character-sets/)
* [Views](../../server-usage/views/)
