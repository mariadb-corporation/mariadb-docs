---
description: >-
  Use MariaDB as a backend for MongoDB applications. This module allows MaxScale
  to accept MongoDB wire protocol commands and transparently convert them into
  SQL queries.
---

# MaxScale NoSQL Protocol Module

## Overview

The `nosqlprotocol` module allows a MariaDB server or cluster to be used as the backend of an application using a MongoDB® client library. Internally, all documents are stored in a table containing two columns; an `id` column for the object id and a `doc` column for the document itself.

When the MongoDB® client application issues MongoDB protocol _commands_, either directly or indirectly via the client library, they are transparently converted into the equivalent SQL and executed against the MariaDB backend. The MariaDB responses are then in turn converted into the format expected by the MongoDB® client library and application.

## Configuring

There are a number of [settings](README.md#settings) with which the behavior of _nosqlprotocol_ can be adjusted. A minimal configuration looks like:

```
[TheService]
type=service
...

[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
nosqlprotocol.user=the_user
nosqlprotocol.password=the_password
port=17017
```

`nosqlprotocol.user` and `nosqlprotocol.password` specify the credentials that will be used when accessing the backend database or cluster. Note that the same credentials will be used for _all_ connecting MongoDB® clients.

Since _nosqlprotocol_ is a _listener_, there must be a _service_ to which the client requests will be sent. _Nosqlprotocol_ places no limitations on what filters, routers or backends can be used.

To configure the same listener with MaxCtrl, the parameters must be passed in a JSON object in the following manner:

```
maxctrl create listener TheService MongoDB-Listener --protocol=nosqlprotocol 'nosqlprotocol={"user":"the_user", "password": "the_password"}'
```

All the parameters that the nosqlprotocol module takes must be passed in the same JSON object.

A complete example can be found at the [end](README.md#example) of this document.

## Authentication

Client authentication, NoSQL users and roles, and how to bootstrap them are described in [MaxScale NoSQL Protocol Authentication](nosql-protocol-authentication.md).

## Wire Protocol

_Nosqlprotocol_ reports that it supports wire protocol versions 0 to 9. The
functionality is that of wire protocol version 6, with the exception that
the commands needed for transactions are recognized, see [transaction
support](README.md#transaction-support). Earlier
wire protocol versions are supported only rudimentarily.

The maximum version is 9, as recent client versions refuse to connect if it
is lower.

## Client Library

As the goal of _nosqlprotocol_ is to implement, to the extent that it is feasible, the wire protocol and the database commands the way MongoDB® implements them, it should be possible to use any language specific driver.

However, only a few client libraries have been verified to work. They are
version 3.6 of _MongoDB Node.JS Driver_ and the _MongoDB Shell_ (`mongosh`)
2.13.0, which uses version 7.5 of the Node.JS driver.

## Settings

Every nosqlprotocol setting, with its type, default, and behavior, is described in [MaxScale NoSQL Protocol Settings](nosql-protocol-settings.md), in alphabetical order.

## Transaction Support

Multi-document transactions, which were introduced in MongoDB 4.0, are not
supported. A transaction is started by a command that contains the field
`startTransaction: true` or `autocommit: false`, and finished with the
`commitTransaction` or `abortTransaction` command.

What happens is controlled by the
[transactions](nosql-protocol-settings.md#transactions) setting. By
default, an error with the code `115` (`CommandNotSupported`) is returned
for the starting command and for `commitTransaction` and `abortTransaction`.
If the value is `ignore`, the commands within a transaction are executed
independently and `commitTransaction` and `abortTransaction` return
`{ "ok" : 1 }`.

Note that a `txnNumber` field alone does not start a transaction, as it is
also used by retryable writes.

When transactions are supported, there will be a third value, `support`,
which will then become the default.

## Databases and Tables

By default, _nosqlprotocol_ automatically creates databases as needed. The default behavior can be changed by setting `auto_create_databases` to false. In that case, databases must manually be created.

Each MongoDB® _collection_ corresponds to a MariaDB table with the same name. However, it is always possible to access a collection irrespective of whether the corresponding table exists or not; it will simply appear to be empty.

Inserting documents into a collection, whose corresponding table does not exist, succeeds, provided `auto_create_tables` is `true`, as the table will in that case be created.

When _nosqlprotocol_ creates a table, it uses a statement like

```
CREATE TABLE name (id VARCHAR(35) AS (JSON_COMPACT(JSON_EXTRACT(doc, "$._id"))) UNIQUE KEY,
                   doc JSON,
                   CONSTRAINT id_not_null CHECK(id IS NOT NULL));
```

where the length of the `VARCHAR` is specified by the value of `id_length`, whose default and minimum is 35.

_NOTE_ If the tables are created manually, then the `CREATE` statement\_must\_ contain a similar `AS`-clause as the one above and _should_ contain a similar constraint.

Note that _nosqlprotocol_ does not in any way verify that the table corresponding to a collection being accessed or modified does indeed have the expected columns `id` and `doc` of the expected types, but it simply uses the table, which will fail if the layout is not the expected one.

To reduce the risk for confusion, the recommendation is to use a specific database for tables that contain documents.

## Indexes

_Nosqlprotocol_ supports indexes but there are some limitations.

In MongoDB®, a query like

```
db.runCommand({find: "toys", filter: { color: "red" }});
```

will return objects like

```
{
  ...
  "color": "red"
}
```

as well as objects like

```
{
  ...
  "color": [ "red", "blue" ]
}
```

_Nosqlprotocol_ translates that query into something like

```
... WHERE JSON_VALUE(doc, "$.color") = "red" OR JSON_CONTAINS(doc, "$.color", "red")
```

The former condition picks out objects whose `color` field contains a literal value `"red"` while the latter picks out objects whose `color` field contains an array containing the value `"color"`.

In MariaDB Server it is not possible to create an index that would be appropriate for that use-case. It is also not possible to create an index that would work predictably, if the data types of the values of a field are different.

An index is created with the assumption that the field is a literal text-value.

When an index is created like

```
db.runCommand({createIndexes: "cars", indexes: [{keys: { color:1 }, name "color"}]});
```

the generated SQL will basically be like

```
ALTER TABLE `test`.`cars`
ADD COLUMN `color` VARCHAR(255) COLLATE utf8mb3_general_ci
    AS (JSON_UNQUOTE(JSON_EXTRACT(doc, '$.color'))),
ADD INDEX `color`(`color`);
```

The index expression - `JSON_UNQUOTE(JSON_EXTRACT(doc, '$.color'))` - does not match the `WHERE` clause shown above, but even if it would match the first part, the second part would still require a table scan, so the index would not be used.

Therefore, it is necessary to provide a hint that an index is present, so that different code can be generated. The hint need not specify the index to be used; it is sufficient that the field is present.

For instance,

```
db.runCommand({find: "cars", filter: {color: "red"}, hint: undefined});
```

will cause the following `WHERE` clause to be generated

```
... WHERE JSON_UNQUOTE(JSON_EXTRACT(doc, '$.color')) = "red"
```

which will cause the index to be used.

Due to the way JSON values are handled, the index will work correctly for exact match searches also when the value is an array or a document.

For instance, with a collection and documents like

```
docs = db.docs;
docs.createIndexes([{f:1}]);
docs.save({f: 1});
docs.save({f: "hello"});
docs.save({f: [1, 2, 3]});
docs.save({f: {g:3}});
```

the following indexed queries will return the correct documents.

```
docs.find({f: "hello"}).hint();
docs.find({f: [1, 2, 3]}).hint();
docs.find({f: {g:3}}).hint();
```

Even integer values can be sought after using the index, but the index will not be used unless the value is enclosed in quotes and the conversion is correct. For instance,

```
docs.find({f: "1"}).hint();
```

will return nothing, but

```
docs.find({f: "1.0"}).hint();
```

will. Without quotes

```
docs.find({f: 1}).hint();
```

the document will be found, but the index will not be used.

## Operators

The following operators are supported.

### Query and Projection Operators

#### Comparison Query Operators

* $eq
* $gt
* $gte
* $in
* $lt
* $lte
* $ne
* $nin

#### Logical Query Operators

* $and
* $not
* $nor
* $or
* $alwaysFalse
* $alwaysTrue

#### Element Query Operators

* $exists
* $type

#### `$type`

When `$type` is used, it will be converted into a condition involving one or more [JSON\_TYPE](../../../../server/reference/sql-functions/special-functions/json-functions/json_type.md) comparisons. The following subset of types can be used in `$type` queries:

| Type           | Number | Alias    | MariaDB Type |
| -------------- | ------ | -------- | ------------ |
| Double         | 1      | "double" | DOUBLE       |
| String         | 2      | "string" | STRING       |
| object         | 3      | "object" | OBJECT       |
| Array          | 4      | "array"  | ARRAY        |
| Boolean        | 5      | "bool"   | BOOLEAN      |
| 32-bit integer | 16     | "int"    | INTEGER      |

The _"number"_ alias is supported and will match values whose MariaDB type is`DOUBLE` or `INTEGER`.

#### Evaluation Query Operators

* $mod
* $regex

#### Array Query Operators

* $all
* $elemMatch
* $size

#### `$elemMatch`

As arguments, only the operators `$eq` and `$ne` are supported.

### Update Operators

#### Field Update Operators

* $bit
* $currentDate
* $inc
* $max
* $min
* $mul
* $pop
* $push
* $rename
* $set
* $unset

### Aggregation Pipeline Stages

* $addFields
* $collStats
* $count
* $group
* $limit
* $listSearchIndexes
* $match
* $project
* $sample
* $skip
* $sort
* $unset
* $unwind

### Aggregation Pipeline Operators

* $abs
* $add
* $and
* $arrayElemAt
* $binarySize
* $bsonSize
* $ceil
* $cmp
* $concat
* $cond
* $convert
* $divide
* $eq
* $exp
* $first
* $floor
* $gt
* $gte
* $ifNull
* $indexOfBytes
* $indexOfCP
* $isArray
* $isNumber
* $last
* $literal
* $ln
* $log
* $log10
* $lt
* $lte
* $ltrim
* $mod
* $multiply
* $ne
* $not
* $or
* $pow
* $reverseArray
* $rtrim
* $size
* $slice
* $split
* $sqrt
* $strCaseCmp
* $strLenBytes
* $strLenCP
* $substr
* $substrBytes
* $substrCP
* $subtract
* $switch
* $toBool
* $toDate
* $toDecimal
* $toDouble
* $toInt
* $toLong
* $toLower
* $toObjectId
* $toString
* $toUpper
* $trim
* $trunc
* $type

#### Accumulators ($group)

* $avg
* $first
* $last
* $max
* $min
* $push
* $sum

## Database Commands

The supported database commands and their fields are described in [MaxScale NoSQL Protocol Database Commands](nosql-protocol-database-commands.md).

## Object Id

When a document is created, an id of type `ObjectId` will be autogenerated by the MongoDB® client library. If the id is provided explicitly, by assigning a value to the `_id` field, the value must be an `ObjectId`, a string or an integer.

## Caching

The conversion of the BSON used in the communication between the client and MaxScale, to the SQL used in the communication between MaxScale and the server carries a not insignificant cost, as does the conversion of result sets returned by the server to the BSON returned by MaxScale to the client. The regular [cache filter](../../maxscale-filters/maxscale-cache/README.md) provides no remedy for this, as it is located after the protocol and uses SQL as the key and stores result sets as values.

From 23.08 onwards, the nosqlprotocol has a built-in cache that when used under certain conditions diminishes the conversion cost. The cache is enabled by adding the following line to the NoSQL listener.

```
[My-NoSQL-Listener]
...
nosqlprotocol.internal_cache=cache
```

This effectively causes the [cache filter](../../maxscale-filters/maxscale-cache/README.md) to be used inside the NoSQL protocol module. The internal cache can be configured just like the cache filter is, by using the following nested configuration syntax.

```
[My-NoSQL-Listener]
...
nosqlprotocol.internal_cache=cache
nosqlprotocol.cache.max_size=10M
nosqlprotocol.cache.soft_ttl=30s
nosqlprotocol.cache.hard_ttl=40s
...
```

A limitation is that _only_ the default storage `storage_inmemory` is supported; `storage_redis` and `storage_memcached` cannot be used.

The cache works on both the SQL and the BSON layer. When a NoSQL request that potentially is cacheable arrives, a lookup for the BSON response is made. If it is found, the response is returned to the client. That is, in this case neither BSON -> SQL, nor a Result Set -> BSON translation will be made.

If the request is not potentially cacheable or the response is not available, the request is processed normally, which may mean that the request is translated into SQL. If the SQL is a SELECT, a second lookup will be made for the corresponding result set. If that is found, the result set is processed, but the roundtrip to the server will be saved.

So, when a result set is received from the server, it will be cached and if the generated NoSQL response is also cacheable, it will be cached as well. The benefit of this approach is that two `Find` NoSQL requests may effectively return the same documents, even though one but not the other NoSQL response is cacheable. Both will benefit the result set being in the cache. Since the used storage follows an LRU-approach when evicting data from the cache, the less valuable result will be evicted first.

### Cached Commands

The responses of the following commands are cached.

* [count](nosql-protocol-database-commands.md#count)
* [distinct](nosql-protocol-database-commands.md#distinct)
* [find](nosql-protocol-database-commands.md#find), provided all found documents can be returned in one response, i.e., if `singleBatch` is `true` or `batchSize` is large enough.

## Compatibility

Currently 30% of the tests in the [MongoDB® core](https://github.com/mongodb/mongo/tree/master/jstests/core) test-suite pass.

## Example

The following is a minimal setup for getting _nosqlprotocol_ up and running. It is assumed the reader knows how to configure MaxScale for normal use. If not, please start with the [MaxScale tutorial](../../../mariadb-maxscale-tutorials/maxscale-administration-tutorial.md). Note that as _nosqlprotocol_ is the first component in the MaxScale routing chain, it can be used with all routers and filters.

### Configuring MaxScale

In the following it is assumed that MaxScale already has been configured for normal use and that there exists a _service_ `[TheService]`.

```
[TheService]
type=service
...

[NoSQL-Listener]
type=listener
service=TheService
protocol=nosqlprotocol
nosqlprotocol.user=the_user
nosqlprotocol.password=the_password
port=17017
```

The values `the_user` and `the_password` must be replaced with the actual credentials to be used for every MongoDB® client that connects.

If MaxScale is now started, the following entry should appear in the log file.

```
... notice : (NoSQL-Listener); Listening for connections at [127.0.0.1]:17017
```

### MongoDB® Shell

The mongo Shell is a powerful tool with which to access and manipulate a MongoDB database. It is part of the MongoDB® package. Having the native MongoDB database installed is convenient, as it makes it easy to ascertain whether a problem is due to _nosqlprotocol_ not fully implementing something or due to the API not being used in the correct fashion.

With the _mongo shell_, all that is needed is to invoke it with the port\_nosqlprotocol\_ is listening on:

```
$ mongo --port 17017
MongoDB shell version v4.4.1
connecting to: mongodb://127.0.0.1:17017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("694f3eed-329f-487a-8d73-9a2d4cf82d62") }
MongoDB server version: 4.4.1
---
        ...
---
>
```

If the shell prompt appears, then a connection was successfully established and the shell can be used.

```
> db.runCommand({insert: "collection", documents: [{_id: 1, "hello": "world"}]});
{ "n" : 1, "ok" : 1 }
```

The `db` variable is implicitly available, and refers by default to the `test` database.

The command inserted a document into the collection called `collection`. The table corresponding to that collection is created implicitly because the default value of `auto_create_tables` is `true`. Here, the object id is specified explicitly, but there is no need for that, as one will be created if needed.

To check whether the documents was inserted into the collection, the`find` command can be issued:

```
> db.runCommand({find: "collection"});
{
    "cursor" : {
        "firstBatch" : [
            {
                "_id" : 1,
                "hello" : "world"
            }
        ],
        "id" : NumberLong(0),
        "ns" : "test.collection"
    },
    "ok" : 1
}
```

As can be seen, the document was indeed inserted into the collection

With the `mysql` shell, the content of the actual table can be checked.

```
MariaDB [(none)]> select * from test.collection;
+------+------------------------------------+
| id   | doc                                |
+------+------------------------------------+
| 1.0  | { "_id" : 1.0, "hello" : "world" } |
+------+------------------------------------+
```

The collection `collection` is represented by a table `collection` with the two columns `id` and `doc`. `id` is a virtual column whose content is the value of the `_id` field of the document in the `doc` column.

All MongoDB® commands that _mongdbprotocol_ support (but for the ones that do not require database access), basically access or manipulate the content in the `doc` column using the [JSON functions](../../../../server/reference/sql-functions/special-functions/json-functions/json_type.md) of MariaDB.

From within the mongo shell itself it is easy to find out just what SQL a particular MongoDB command is translated into.

For instance, the SQL that the insert command with which the document was added can be found out like:

```
> db.runCommand({mxsDiagnose: {insert: "collection", documents: [{_id: 1, "hello": "world"}]}});
{
    "kind" : "multi",
    "sql" : [
        "INSERT INTO `test`.`collection` (doc) VALUES ('{ \"_id\" : 1.0, \"hello\" : \"world\" }')"
    ],
    "ok" : 1
}
```

Similarly, the SQL of the `find` command can be find out like:

```
> db.runCommand({mxsDiagnose: {find: "collection"}});
{
    "kind" : "single",
    "sql" : "SELECT doc FROM `test`.`collection` ",
    "ok" : 1
}
```

The returned SQL can be directly pasted at the `mysql` prompt, which is quite convenient in case the MongoDB® command does not behave as expected.

### MongoDB® Node.JS Driver

As all client libraries implement and depend on the MongoDB® wire protocol, all client libraries should work with _nosqlprotocol_. However, the only client library that has been used and that has been verified to work is version 3.6 of the _MongoDB Node.JS Driver_.

In principle, the only thing that needs to be altered in an existing program using the library is to change the uri string that typically is something like

```
const uri = "mongodb+srv://<user>:<password>@<cluster-url>?writeConcern=majority";
```

to

```
const uri = "mongodb://<maxscale-ip>:17017";
```

with the assumption that the default _nosqlprotocol_ port is used.

In practice, additional modifications may be needed since _nosqlprotocol_ does not implement all commands and does not in all cases implement the full functionality of the commands that it supports.

#### Inserting a Document

Store the following into a file called `insert.js`.

```
const { MongoClient } = require("mongodb");

const uri = "mongodb://127.0.0.1:17017";

const client = new MongoClient(uri, { useUnifiedTopology: true });
async function run() {
  try {
    await client.connect();
    const database = client.db("mydb");
    const movies = database.collection("movies");
    // create a document to be inserted
    const movie = { title: "Apocalypse Now", director: "Francis Ford Coppola" };
    const result = await movies.insertOne(movie);
    console.log(
      `${result.insertedCount} documents were inserted with the _id: ${result.insertedId}`,
    );
  } finally {
    await client.close();
  }
}
run().catch(console.dir);
```

Then, run the program like

```
$ nodejs insert.js
1 documents were inserted with the _id: 60afca73bf486114e3fb48b8
```

As the id is not explicitly provided, it will not be the same.

#### Finding a Document

Store the following into a file called `find.js`.

```
const { MongoClient } = require("mongodb");

const uri = "mongodb://127.0.0.1:17017";

const client = new MongoClient(uri, { useUnifiedTopology: true });
async function run() {
  try {
    await client.connect();
    const database = client.db("mydb");
    const movies = database.collection("movies");
    // Query for a movie that has the title 'Apocalypse Now'
    const query = { title: "Apocalypse Now" };
    const options = {
      // Include only the 'director' field in the returned document
      projection: { _id: 0, director: 1 },
    };
    const movie = await movies.findOne(query, options);
    // Returns a document and not a cursor, so print directly.
    console.log(movie);
  } finally {
    await client.close();
  }
}
run().catch(console.dir);
```

Then, run the program like

```
$ nodejs find.js
{ director: 'Francis Ford Coppola' }
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
