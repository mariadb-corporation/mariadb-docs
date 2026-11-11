---
description: >-
  Reference for the MongoDB database commands that nosqlprotocol supports,
  with their relevant fields, plus the MaxScale-specific commands.
---

# MaxScale NoSQL Protocol Database Commands

This page lists the MongoDB® database commands that nosqlprotocol supports.

The following commands are supported. At each command is specified what fields are relevant for the command.

**All** non-listed fields are ignored; their presence or absence have no impact, unless otherwise explicitly specified.

## Aggregation Commands

### aggregate

The following fields are relevant.

| Field     | Type    | Description                                                                                                                                              |
| --------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| aggregate | string  | The name of the collection used as the input for the aggregation pipeline.                                                                               |
| pipeline  | array   | An array of [aggregation pipeline stages](README.md#aggregation-pipeline-stages) that process and transform the document stream. |
| explain   | boolean | Optional. Specifies to return information on the processing of the pipeline.                                                                             |

Depending on the stages and their parameters, the aggregation pipeline may be performed entirely using SQL, by fetching documents to MaxScale where they are post-processed or by a combination of the two approaches.

### count

The following fields are relevant.

| Field | Type     | Description                                                                  |
| ----- | -------- | ---------------------------------------------------------------------------- |
| count | string   | The name of the collection to count.                                         |
| query | document | Optional. A query that selects which documents to count in the collection    |
| limit | integer  | Optional. The maximum number of matching documents to return.                |
| skip  | integer  | Optional. The number of matching documents to skip before returning results. |

### distinct

The following fields are relevant.

| Field    | Type     | Description                                                               |
| -------- | -------- | ------------------------------------------------------------------------- |
| distinct | string   | The name of the collection to query for distinct values.                  |
| key      | string   | The field for which to return distinct values.                            |
| query    | document | Optional. A query that selects which documents to count in the collection |

## Query and Write Operation Commands

### delete

The following fields are relevant.

| Field   | Type    | Description                                                                                                                                                                                                                              |
| ------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| delete  | string  | The name of the target table.                                                                                                                                                                                                            |
| deletes | array   | An array of one or more delete statements to perform in the named collection.                                                                                                                                                            |
| ordered | boolean | Optional. If true, then when a delete statement fails, return without performing the remaining delete statements. If false, then when a delete statement fails, continue with the remaining delete statements, if any. Defaults to true. |

Each element of the deletes array contains the following fields:

| Field | Type     | Description                                                                                                                       |
| ----- | -------- | --------------------------------------------------------------------------------------------------------------------------------- |
| q     | document | The query that matches documents to delete.                                                                                       |
| limit | integer  | The number of matching documents to delete. Specify either a 0 to delete all matching documents or 1 to delete a single document. |

### find

The following fields are relevant.

| Field       | Type                 | Description                                                                                                                                                                                        |
| ----------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| find        | string               | The name of the target table.                                                                                                                                                                      |
| filter      | document             | Optional. The query predicate. If unspecified, then all documents in the collection will match the predicate.                                                                                      |
| sort        | document             | Optional. The sort specification for the ordering of the results.                                                                                                                                  |
| projection  | document             | Optional. The projection specification to determine which fields to includein the returned documents.                                                                                              |
| skip        | Positive integer     | Optional. Number of documents to skip. Defaults to 0.                                                                                                                                              |
| limit       | Non-negative integer | Optional. The maximum number of documents to return. If unspecified, then defaults to no limit. A limit of 0 is equivalent to setting no limit.                                                    |
| batchSize   | Non-negative integer | Optional. The number of documents to return in the first batch. Defaults to 101. A batchSize of 0 means that the cursor will be established, but no documents will be returned in the first batch. |
| singleBatch | boolean              | Optional. Determines whether to close the cursor after the first batch. Defaults to false.                                                                                                         |
| hint        | any                  | Optional. The value is ignored, but if the `hint` field is present, _nosqlprotocol_ will generate code with the assumption that there is an index for every field referred to in `filter`.         |

All other fields are ignored.

**Projection**

The `projection` parameter determines which fields are returned in the matching documents. The `projection` parameter takes a document of the following form:

```
{ <field1>: <value>, <field2>: <value> ... }
```

If a `projection` document is not provided or if it is empty, the entire document will be returned.

| Projection     | Description                             |
| -------------- | --------------------------------------- |
| : <1 or true>  | Specifies the inclusion of a field.     |
| : <0 or false> | Specifies the exclusion of a field.     |
| :              | Adds a new field or resets an existing. |

**Embedded Field Specification**

For fields in an embedded documents, the field can be specified using:

* dot notation; e.g. `"field.nestedfield": <value>`

In particular, specifying fields in embedded documents using nested form is not supported.

**`_id` Field Projection**

The `_id` field is included in the returned documents by default unless you explicitly specify `_id: 0` in the projection to suppress the field.

**Inclusion or Exclusion**

A `projection` cannot contain both include and exclude specifications, with the exception of the `_id` field:

* In projections that explicitly include fields, the `_id` field is the only field that can be explicitly excluded.
* In projections that explicitly excludes fields, the `_id` field is the only field that can be explicitly include; however, the `_id` field is included by default.

**Filtering by `_id`**

Note that there is a significant difference between

```
> db.runCommand({find: "collection", filter: { _id: 4711 }});
```

and

```
> db.runCommand({find: "collection", filter: { _id: { $eq: 4711 }}});
```

In the former case the generated `WHERE` clause will be

```
... WHERE (id = '4711')
```

and in the latter

```
... WHERE (JSON_EXTRACT(doc, '$._id') = 4711)
```

That is, in the former case the _indexed_ column `id` will be used, in the latter it will not.

### findAndModify

The following fields are relevant.

| Field         | Type     | Description                                                                                                                                               |
| ------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| findAndModify | string   | The name of the target table.                                                                                                                             |
| query         | document | Optional. The query predicate.                                                                                                                            |
| sort          | document | Optional. The sort specification used when the document is selected.                                                                                      |
| remove        | boolean  | Mandatory, if update is not specified. If true, the document will be deleted.                                                                             |
| update        | document | Mandatory, if remove is not specified. See [Update.behavior](nosql-protocol-database-commands.md#update) for details.                                     |
| new           | boolean  | Optional. If true the modified document and not the original document is returned. If remove is specified, then the original document is always returned. |
| fields        | document | Optional. Specified which fields to return. See [Find.projection](nosql-protocol-database-commands.md#find) for details.                              |
| upsert        | boolean  | Optional. If true then a document will be created, if one is not found.                                                                                   |

All other fields are ignored.

### getLastError

The following fields are relevant.

| Field        | Type | Description |
| ------------ | ---- | ----------- |
| getLastError | any  | Ignored.    |

### getMore

The following fields are relevant.

| Field      | Type             | Description                                                    |
| ---------- | ---------------- | -------------------------------------------------------------- |
| getMore    | long             | The cursor id.                                                 |
| collection | string           | The name of the collection over which the cursor is operating. |
| batchSize  | positive integer | Optional. The number of documents to return in the batch.      |

### insert

The `insert` command inserts one or more documents into the table whose name is the same as that of the collection. If the option `auto_create_tables` is `true`, then the table is created if it does not already exist. If the value is `false`, then the insert will fail unless the table already exists.

The following fields are relevant.

| Field     | Type    | Description                                                               |
| --------- | ------- | ------------------------------------------------------------------------- |
| insert    | string  | The name of the target collection (i.e. table).                           |
| documents | array   | An array of one or more documents to be inserted to the named collection. |
| ordered   | boolean | Optional, with default being true. See below for description.             |

**`ordered`**

The impact of `ordered` is dependent upon the value of `ordered_insert_behavior`.

**`default`**

In this case `ordered` has the same impact as in MongoDB®. That is, if the value is `true`, then when an insert of a document fails, return without inserting any remaining documents listed in the inserts array. If `false`, then when an insert of a document fails, continue to insert the remaining documents.

**`atomic`**

If `ordered` is `true`, then all documents will be inserted using a single INSERT command. That is, if the insertion of any document fails, for instance, due to a duplicate id, then no document will be inserted. If `ordered` is `false`, then the behavior is identical with that of `default`.

**Performance**

What combination of `ordered_insert_behavior` and `ordered` is used, has an impact on the performance.

| ordered\_insert\_behavior | ordered = true                                                                                                                        | ordered = false                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| default                   | All documents are inserted within a compound statement, in a transaction containing as many INSERT statements as there are documents. | All documents are inserted in a single multi-statement transaction containing as many INSERT IGNORE statements as there are documents. |
| atomic                    | All documents are inserted using a single INSERT statement.                                                                           | Same as above                                                                                                                          |

Of these, `atomic + true` is the fastest and `atomic|default + false` the slowest, being roughly twice as slow. The performance of 'default + true' is halfway between the two.

### resetError

The following fields are relevant.

| Field      | Type | Description |
| ---------- | ---- | ----------- |
| resetError | any  | Ignored.    |

### update

The following fields are relevant.

| Field   | Type   | Description                                          |
| ------- | ------ | ---------------------------------------------------- |
| update  | string | The name of the target table.                        |
| updates | array  | An array of documents that describe what to updated. |

All other fields are ignored.

**Update Statements**

Each element of the updates array is an update statement document. Each document contains the following fields:

| Field | Type     | Description                                                                                                                                                        |
| ----- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| q     | document | The query that matches documents to update.                                                                                                                        |
| u     | document | The modifications to apply. See behavior below for details.                                                                                                        |
| multi | boolean  | Optional. If true, updates all documents that meet the query criteria. If false limit the update to one document that meets the query criteria. Defaults to false. |

Note that it is possible to set `multi` to `true` in conjunction with a _replacement-style_ update, even though MongoDB® rejects that.

All other fields are ignored, with the exception of `upsert` that if present with the value of `true` will cause the command to fail.

**Behavior**

Only updating using _update operator expressions_ or with a _replacement document_ is supported. In particular, updating using an _aggregation pipeline_ is not supported.

\####### Update with an Update Operator Expressions document

The update statement field `u` can accept a document that only contains [update operator](README.md#update-operators) expressions. For example:

```
updates: [
   {
     q: <query>,
     u: { $set: { status: "D" } },
      ...
   },
   ...
]
```

In this case, the update command updates only the corresponding fields in the document.

\####### Update with a _Replacement Document_

The update statement field `u` field can accept a _replacement document_, i.e. the document contains only `field:value` expressions. For example:

```
updates: [
   {
      q: <query>,
      u: { status: "D", quantity: 4 },
      ...
   },
   ...
]
```

In this case, the update command replaces the matching document with the update document. The update command can only replace a single matching document; i.e. the multi field cannot be true.

**Note** If the replacement document contains an `_id` field, it will be ignored and the document id will remain non-changed while the document otherwise is replaced. This is different from MongoDB® where the presence of the `_id` field in the replacement document causes an error, if the value is not the same as it is in the document being replaced.

## Authentication Commands

### Logout

The following fields are relevant.

| Field  | Type | Description |
| ------ | ---- | ----------- |
| logout | any  | Ignored.    |

If you are not logged in and using authentication, `logout` has no effect.

Note that in order to be logged out, the logging out must be done while using the same database that was used when you logged on.

Always returns

```
{ ok: 1 }
```

## User Management Commands

### createUser

Creates a new MariaDB user and adds an entry to the local nosqlprotocol account database.

The following fields are relevant.

| Field          | Type     | Description                                                                                                    |
| -------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| createUser     | string   | The name of the user to be added.                                                                              |
| pwd            | string   | The password in cleartext.                                                                                     |
| customData     | document | Optional. Any arbitrary information.                                                                           |
| roles          | array    | The roles granted to the user.                                                                                 |
| mechanisms     | array    | Optional. The specific supported SCRAM mechanisms for this user. Must be a subset of the supported mechanisms. |
| digestPassword | boolean  | Optional. If specified, must be true.                                                                          |

The MariaDB user will be created as `'<db>.<user>'@'%'` where `<db>` is the name of the NoSQL database in whose context the user is created, and`<user>` the value of the `createUser` field. For instance, with the following command

```
> use myDatabase;
> db.runCommand({createUser: "user1", pwd: "pwd1", roles: []});
```

the MariaDB user `'myDatabase.user1'@'%'` will be created.

The elements of the `roles` array are converted into privileges as explained in [here](nosql-protocol-authentication.md#roles-and-privileges).

In practice the creation is performed as follows:_First the MariaDB user is created._ Then the privileges are granted.

* Finally the local nosqlprotocol account database is updated.

If the granting of privileges fails, an attempt will be made to drop the user.

### dropAllUsersFromDatabase

Drops all users from the local nosqlprotocol account database and the corresponding MariaDB users.

The following fields are relevant.

| Field                    | Type | Description |
| ------------------------ | ---- | ----------- |
| dropAllUsersFromDatabase | any  | Ignored.    |

If _no_ users can be dropped, e.g. due to an authorization error, then an error will be returned. If even a single user can be dropped the returned document tells how many were dropped, which does not necessarily indicate that _all_ users were dropped.

### dropUser

The following fields are relevant.

| Field    | Type   | Description                         |
| -------- | ------ | ----------------------------------- |
| dropUser | string | The name of the user to be dropped. |

The user will first be dropped from the MariaDB server and if that succeeds also from the local nosqlprotocol account database.

### grantRolesToUser

This command _adds_ more roles to a NoSQL user, which may imply that additional privileges are granted to the corresponding MariaDB user.

| Field            | Type   | Description                                    |
| ---------------- | ------ | ---------------------------------------------- |
| grantRolesToUser | string | The name of the user to give additional roles. |
| roles            | array  | An array of additional roles.                  |

Note that roles assigned to different databases will result in separate GRANT statements, which means that it is possible that some succeed and others do not.

### revokeRolesFromUser

This command _removes_ roles from an NoSQL user, which may imply that privileges are revoked from the corresponding MariaDB user.

| Field               | Type   | Description                                |
| ------------------- | ------ | ------------------------------------------ |
| revokeRolesFromUser | string | The name of the user to remove roles from. |
| roles               | array  | An array of roles to remove.               |

Note that roles to be removed from different databases will result in separate REVOKE statements, which means that it is possible that some succeed and others do not.

### updateUser

This command updates the information about a particular user.

| Field      | Type     | Description                                                                                                                                                                                                                                                        |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| updateUser | string   | The user whose information should be updated.                                                                                                                                                                                                                      |
| pwd        | string   | Optional. The new password in cleartext.                                                                                                                                                                                                                           |
| customData | document | Optional. Any arbitrary information.                                                                                                                                                                                                                               |
| roles      | array    | Optional. The roles granted to the user. Note that the existing ones are replaced and not amended with these roles.                                                                                                                                                |
| mechanisms | array    | Optional. The specific SCRAM mechanisms for user credentials. Note that if a new pwd is provided, then the array can contain all supported SCRAM mechanisms. If a new pwd is not provided, then the array must be a subset of the existing mechanisms of the user. |

Changes to `customData` or `mechanisms` are made only to the local nosqlprotocol database, but changes to `pwd` or `roles` require the MariaDB server to be updated.

### usersInfo

This command returns information about one or more users.

The following fields are relevant.

| Field           | Type    | Description                                                                    |
| --------------- | ------- | ------------------------------------------------------------------------------ |
| usersInfo       | various | Specifies what to return. See below.                                           |
| showCredentials | boolean | Optional, default false. Specifies whether the credentials should be returned. |

The returned information depends the value of `usersInfo`:

| Argument                              | Result                                                                              |
| ------------------------------------- | ----------------------------------------------------------------------------------- |
| { usersInfo: 1 }                      | Returns information of all users in the database where the command is run.          |
| { usersInfo: }                        | Returns information about a specific user in the database where the command is run. |
| { usersInfo: { user: , db: \}}        | Returns information about the user specified by the name and database.              |
| { usersInfo: \[{ user: , db: }, ...]} | Returns information about specified users.                                          |
| { usersInfo: \[ , ... ]}              | Returns information about specified users in the database where the command is run. |

Note that users may always view their own information. Otherwise the user must have the `userAdmin` or `userAdminAnyDatabase` role.

If `showCredentials` is true, the returned object(s) will contain a`mariadb: { password: "*..."}` field, where `password` is the`SHA1(SHA1())` value of the password used when logging to MariaDB. That is, the same string that is found in the `password` column in the `mysql.user` table.

## Replication Commands

### isMaster

The following fields are relevant.

| Field    | Type | Description |
| -------- | ---- | ----------- |
| isMaster | any  | Ignored.    |

### replSetGetStatus

The following fields are relevant.

| Field            | Type | Description |
| ---------------- | ---- | ----------- |
| replSetGetStatus | any  | Ignored.    |

All other fields are ignored.

This command will always return the document

```
{
    "ok" : 0,
    "errmsg" : "not running with --replSet",
    "code" : 76,
    "codeName" : "NoReplicationEnabled"
}
```

## Sessions Commands

### endSessions

The following fields are relevant.

| Field       | Type  | Description |
| ----------- | ----- | ----------- |
| endSessions | array | Ignored.    |

The following document will always be returned:

```
{ "ok" : 1 }
```

## Administration Commands

### create

The following fields are relevant.

| Field  | Type    | Description                                                                              |
| ------ | ------- | ---------------------------------------------------------------------------------------- |
| create | string  | The name of the collection to create.                                                    |
| capped | boolean | Optional. If specified, the value must be false as capped collections are not supported. |
| viewOn | string  | Optional. If specified, the command will fail as views are not supported.                |

_Capped collections_ and _views_ are not supported. Consequently, specifying that the collection should be capped or that it should be a view on another collection, will cause the command to fail.

### createIndexes

| Field         | Type   | Description                                 |
| ------------- | ------ | ------------------------------------------- |
| createIndexes | string | The collection for which to create indexes. |
| indexes       | array  | Specifies the indexes to create.            |

The following fields are relevant for each document in the `indexes` array.

| Field  | Type     | Description                                                                                                                                                                                            |
| ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| key    | document | Contains key/value pairs, where the key is the name of the field to index and value the index direction or the index type. The direction is ignored and a specific type cannot be specified. |
| name   | string   | The name of the index.                                                                                                                                                                                 |
| unique | boolean  | Optional. If true, a unique index will be created.                                                                                                                                                     |
| sparse | boolean  | Optional and has no effect.                                                                                                                                                                            |

For instance, the following command

```
db.runCommand({createIndexes: "cars", indexes: [{keys: { make: 1}, name: "make"}]});
```

results in the following SQL:

```
ALTER TABLE `test`.`cars`
ADD COLUMN IF NOT EXISTS `make` VARCHAR(255) COLLATE utf8mb4_bin AS (JSON_VALUE(doc, '$.make')),
ADD INDEX IF NOT EXISTS `make`(`make`) COMMENT 'Regular';
```

The value of the comment is either `Regular` or `Sparse`, depending on the value of `sparse` at creation time. The only purpose is for `listIndexes` to be able to report whether the index was supposed to be sparse or not.

### drop

The following fields are relevant.

| Field | Type   | Description                         |
| ----- | ------ | ----------------------------------- |
| drop  | string | The name of the collection to drop. |

### dropDatabase

The following fields are relevant.

| Field        | Type | Description |
| ------------ | ---- | ----------- |
| dropDatabase | any  | Ignored.    |

### dropIndexes

The following fields are relevant.

| Field       | Type   | Description                                                 |
| ----------- | ------ | ----------------------------------------------------------- |
| dropIndexes | string | The name of the collection whose indexes should be dropped. |
| index       | string | document                                                    |

### fsync

The following fields are relevant.

| Field | Type | Description |
| ----- | ---- | ----------- |
| fsync | any  | Ignored     |

The response will always be

```
{
  "errmsg" : "fsync not supported by MaxScale:nosqlprotocol",
  "code" : 115,
  "codeName" : "CommandNotSupported",
  "ok" : 0
}
```

### killCursors

The following fields are relevant.

| Field       | Type   | Description                     |
| ----------- | ------ | ------------------------------- |
| killCursors | string | The name of the collection.     |
| cursors     | array  | The ids of the cursors to kill. |

### listCollections

The following fields are relevant.

| Field           | Type     | Description                                                                                                                                      |
| --------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| listCollections | any      | Ignored.                                                                                                                                         |
| filter          | document | The field name is honored, other fields are not but cause warnings to be logged.                                                                 |
| nameOnly        | boolean  | Optional. A flag to indicate whether the command should return just the collection names and type or return both the name and other information. |

Up until version 24.02, the command listed every table in the current database as a collection. From 24.08 onwards, only tables that contain NoSQL data will be returned as NoSQL collections.

### listDatabases

The following fields are relevant.

| Field         | Type    | Description                                                                                                                                 |
| ------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| listDatabases | any     | Ignored.                                                                                                                                    |
| nameOnly      | boolean | Optional. A flag to indicate whether the command should return just the database names, or return both database names and size information. |

### listIndexes

The following fields are relevant.

| Field       | Type   | Description                 |
| ----------- | ------ | --------------------------- |
| listIndexes | string | The name of the collection. |

**NOTE** As it is not possible to actually create indexes, although an attempt to do so using `createIndexes` will succeed, the result will always only contain information about the built-in index `_id_`.

### renameCollection

The following fields are relevant.

| Field            | Type    | Description                                                                                                                                                |
| ---------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| renameCollection | string  | The namespace of the collection to rename. The namespace is a combination of the database name and the name of the collection.                             |
| to               | string  | The new namespace of the collection. Moving a collection/table from one database to another succeeds provided the databases reside in the same filesystem. |
| dropTarget       | boolean | Optional. If true, the target collection/table will be dropped before the renaming is made. The default value is false.                                    |

### setParameter

The following fields are relevant.

| Field        | Type | Description |
| ------------ | ---- | ----------- |
| setParameter | any  | Ignored.    |

Any kind of parameter is accepted and the response will always be:

```
{ "ok" : 1 }
```

## Diagnostic Commands

### buildInfo

The following fields are relevant.

| Field     | Type | Description |
| --------- | ---- | ----------- |
| buildInfo | any  | Ignored.    |

The command returns a document containing the stable fields. In addition, there is a field `maxscale` whose value is the MaxScale version, expressed as a string.

### explain

The following fields are relevant.

| Field     | Type     | Description                                                                                                                                      |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| explain   | document | Document specifying the command to be explained. The commands are aggregate, count, delete, distinct, find, findAndModify, mapReduce and update. |
| verbosity | string   | Either queryPlanner, executionStats or allPlansExecution.                                                                                        |

The command will return a document of the expected layout, but the content is only rudimentary.

### getCmdLineOpts

The following fields are relevant.

| Field          | Type | Description |
| -------------- | ---- | ----------- |
| getCmdLineOpts | any  | Ignored.    |

### getLog

The following fields are relevant.

| Field  | Type   | Description                    |
| ------ | ------ | ------------------------------ |
| getLog | string | \*, global and startupWarnings |

The command returns a document of the correct format, but _no_ actual log data will be returned.

### hostInfo

The following fields are relevant.

| Field    | Type | Description |
| -------- | ---- | ----------- |
| hostInfo | any  | Ignored.    |

### listCommands

The following fields are relevant.

| Field        | Type | Description |
| ------------ | ---- | ----------- |
| listCommands | any  | Ignored.    |

### ping

The following fields are relevant.

| Field | Type | Description |
| ----- | ---- | ----------- |
| ping  | any  | Ignored.    |

### serverStatus

The following fields are relevant.

| Field        | Type | Description |
| ------------ | ---- | ----------- |
| serverStatus | any  | Ignored.    |

### validate

The following fields are relevant.

| Field    | Type   | Description                             |
| -------- | ------ | --------------------------------------- |
| validate | string | The name of the collection to validate. |

The command does not actually perform any validation but for checking that the collection exists. The response will contain in `nrecords` the current number of documents/rows it contains.

### whatsmyuri

The following fields are relevant.

| Field     | Type | Description |
| --------- | ---- | ----------- |
| whatsmyri | any  | Ignored.    |

This is an internal command, implemented only because the Mongo Shell uses it.

## Free Monitoring Commands

### getFreeMonitoringStatus

The following fields are relevant.

| Field                   | Type | Description |
| ----------------------- | ---- | ----------- |
| getFreeMonitoringStatus | any  | Ignored.    |

The following document will always be returned:

```
{ "state" : "undecided", "ok" : 1 }
```

## MaxScale Specific Commands

### mxsAddUser

**Definition**

**mxsAddUser**

The `mxsAddUser` command adds an _existing_ MariaDB user to the local nosqlprotocol account database. Use [createUser](nosql-protocol-database-commands.md#createuser) if the MariaDB user should be created as well.

Note that the `mxsAddUser` command does not check that the user exists or that the specified roles are compatible with the grants of the user.

**Syntax**

The 'mxsAddUser' command has the following syntax:

```
db.runCommand(
    {
        mxsAddUser: "<name>",
        pwd: passwordPrompt(),  // Or "<cleartext password>"
        customData: { <any information> },
        roles: [
            { role: "<role>", db: "<database>" } | "<role>",
            ...
        ],
        mechanisms: [ "<scram-mechanism>", ...],
        digestPassword: <boolean>
    }
)
```

**Command Fields**

The command has the following fields:

| Field          | Type     | Description                                                                                                    |
| -------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| mxsAddUser     | string   | The name of the user to be added.                                                                              |
| pwd            | string   | The password in cleartext.                                                                                     |
| customData     | document | Optional. Any arbitrary information.                                                                           |
| roles          | array    | The roles granted to the user.                                                                                 |
| mechanisms     | array    | Optional. The specific supported SCRAM mechanisms for this user. Must be a subset of the supported mechanisms. |
| digestPassword | boolean  | Optional. If specified, must be true.                                                                          |

The value of `mxsAddUser` should be the name (without the host part) of an existing user in the MariaDB server and the value of `pwd` should be that user's password in cleartext.

The `roles` array should contain roles that a compatible with the grants of the user. Please check [roles and privileges](nosql-protocol-authentication.md#roles-and-privileges) for a discussion on how to map roles map to privileges.

**Returns**

If the addition of the user succeeds, the command returns a document with the single field `ok` whose value is `1`.

```
> db.runCommand({mxsAddUser: "user", pwd: "pwd", roles: ["readWrite"]});
{ "ok" : 1 }
```

If there is a failure of some kind, the command returns an error document

```
> db.runCommand({mxsAddUser: "user2", pwd: "pwd2", roles: ["redWrite"]});
{
    "ok" : 0,
    "errmsg" : "No role named redWrite@test",
    "code" : 31,
    "codeName" : "RoleNotFound"
}
```

### mxsCreateDatabase

**Definition**

**mxsCreateDatabase**

The 'mxsCreateDatabase' command creates a new database and must be run against the `admin` database.

**Syntax**

The 'mxsCreateDatabase' has the following syntax:

```
db.adminCommand(
    {
       mxsCreateDatabase: <name>
    }
)
```

**Command Fields**

The command takes the following fields:

| Field             | Type   | Description                             |
| ----------------- | ------ | --------------------------------------- |
| mxsCreateDatabase | string | The name of the database to be created. |

**Returns**

If database creation succeeds, the command returns a document with the single field `ok` whose value is `1`.

```
> db.adminCommand({mxsCreateDatabase: "db"});
{ "ok" : 1 }
```

If the database creation fails, the command returns an error document.

```
> db.adminCommand({mxsCreateDatabase: "db"});
{
    "ok" : 0,
    "errmsg" : "The database 'db' exists already.",
    "code" : 48,
    "codeName" : "NamespaceExists"
}
```

### mxsDiagnose

**Definition**

**mxsDiagnose**

The `mxsDiagnose` command provides diagnostics for any other command; that is, how MaxScale will handle that command.

**Syntax**

The `mxsDiagnose` command has the following syntax:

```
db.runCommand(
    {
       mxsDiagnose: <command>
    }
)
```

**Command Fields**

The command takes the following fields:

| Field       | Type     | Description                                  |
| ----------- | -------- | -------------------------------------------- |
| mxsDiagnose | document | A command as provided to db.runCommand(...). |

**Returns**

The command returns a document that contains diagnostics of the command provided as argument. For example:

```
> db.runCommand({mxsDiagnose: {ping:1}});
{ "kind" : "immediate", "response" : { "ok" : 1 }, "ok" : 1 }

> db.runCommand({mxsDiagnose: {find:"person", filter: { name: "Bob"}}});
{
  "kind" : "single",
  "sql" : "SELECT doc FROM `test`.`person` WHERE ( JSON_EXTRACT(doc, '$.name') = 'Bob') ",
  "ok" : 1
}

> db.runCommand({mxsDiagnose: {delete:"person", deletes: [{q: { name: "Bob"}, limit:0}, {q: {name: "Alice"}, limit:0}]}});
{
  "kind" : "single",
  "sql" : [
    "DELETE FROM `test`.`person` WHERE ( JSON_EXTRACT(doc, '$.name') = 'Bob') ",
    "DELETE FROM `test`.`person` WHERE ( JSON_EXTRACT(doc, '$.name') = 'Alice') "
  ],
  "ok" : 1
}
```

`kind` specifies of what kind the command is; an _immediate_ command is one for which MaxScale autonomously can generate the response, a _single_ command is one where the command will cause a single SQL statement to be sent to the backend, and a _multi_ command is one where potentially multiple SQL statements will be sent to the backend.

If the command is _immediate_ then there will be a field `response` containing the actual response of the command, if the command is _single_ then there will be a field `sql` containing the actual statement that would have been sent to the backend, and if the command is _multi_ then there will be a field `sql` containing an array of statements that would have been sent to the backend.

If an error occurs while the command is being diagnosed, then there will be no`response` field but an `error` field whose value is an error document. Note that the value of `ok` will always be 1.

### mxsGetConfig

**Definition**

**mxsGetConfig**

The `mxsGetConfig` command returns the current configuration of the session and must be run against the 'admin' database.

**Syntax**

The `mxsGetConfig` has the following syntax:

```
db.runCommand(
    {
        mxsGetConfig: <any>
    });
```

**Command Fields**

The command takes the following fields:

| Field        | Type | Description |
| ------------ | ---- | ----------- |
| mxsGetConfig |      | Ignored.    |

**Returns**

The command returns a document that contains the current configuration of the session. For example:

```
> db.runCommand({mxsGetConfig: 1});
{
    "config" : {
        "on_unknown_command" : "return_error",
        "auto_create_tables" : true,
        "id_length" : 35
                ...
    },
    "ok" : 1
}
```

### mxsListTables

**Definition**

**mxsListTables**

The `mxsListTables` command lists all tables in a database.

**Syntax**

The 'mxsListTables' command has the following syntax:

```
db.runCommand(
    {
        mxsListTables: <any>
    });
```

**Command Fields**

The command takes the following fields:

| Field         | Type | Description |
| ------------- | ---- | ----------- |
| mxsListTables |      | Ignored.    |

**Returns**

The command returns a cursor whose first and only batch contains the names of the tables in the database and whether they are NoSQL collections or not. For example:

```
> db.runCommand({mxsListTables:"hello"});
{
  cursor: {
    id: Long('0'),
    ns: 'test.$cmd.mxsListTables',
    firstBatch: [
      { name: 'Cars', nosql: true },
      { name: 'Customers', nosql: false },
    ]
  },
  ok: 1
}
```

### mxsRemoveUser

**Definition**

**mxsRemoveUser**

The `mxsRemoveUser` removes a user from the local nosqlprotocol account database. Use [dropUser](nosql-protocol-database-commands.md#dropuser) if the MariaDB user should be dropped as well.

**Syntax**

The 'mxsRemoveUser' command has the following syntax:

```
db.runCommand(
    {
        mxsRemoveUser: "<name>"
    }
)
```

**Command Fields**

The command has the following fields:

| Field         | Type   | Description                         |
| ------------- | ------ | ----------------------------------- |
| mxsRemoveUser | string | The name of the user to be removed. |

**Returns**

If the removal of the user succeeds, the command returns a document with the single field `ok` whose value is `1`.

```
> db.runCommand({mxsRemoveUser: "user"});
{ "ok" : 1 }
```

If there is a failure of some kind, the command returns an error document

```
> db.runCommand({mxsRemoveUser: "user"});
{
    "ok" : 0,
    "errmsg" : "User 'user@test' not found",
    "code" : 11,
    "codeName" : "UserNotFound"
}
```

### mxsSetConfig

**Definition**

**mxsSetConfig**

The `mxsSetConfig` command changes the configuration of the session and must be run against the 'admin' database.

Note that the changes only affect the current session and are **not** persisted.

**Syntax**

The `mxsSetConfig` has the following syntax:

```
db.runCommand(
    {
        mxsSetConfig: document
    });
```

**Command Fields**

The command takes the following fields:

| Field        | Type     | Description                              |
| ------------ | -------- | ---------------------------------------- |
| mxsSetConfig | document | A document specifying the configuration. |

The document takes the following fields:

| Field                | Type    | Description                                 |
| -------------------- | ------- | ------------------------------------------- |
| on\_unknown\_command | string  | Either "return\_error" or "return\_empty"   |
| auto\_create\_tables | boolean | Whether tables should be created as needed. |
| id\_length           | integer | id column VARCHAR size in created tables.   |
| transactions         | string  | Either "error" or "ignore"                  |

**Returns**

The command returns a document that contains the changed configuration of the session. For example:

```
> db.runCommand({mxsGetConfig: 1});
{
    "config" : {
        "on_unknown_command" : "return_error",
        "auto_create_tables" : true,
        "id_length" : 35
                ...
    },
    "ok" : 1
}
> db.runCommand({mxsSetConfig: { auto_create_tables: false}});
{
    "config" : {
        "on_unknown_command" : "return_error",
        "auto_create_tables" : false,
        "id_length" : 35
                ...
    },
    "ok" : 1
}
```

### mxsUpdateUser

**Definition**

**mxsUpdateUser**

The `mxsUpdateUser` command updates a user in the local nosqlprotocol account database. Use [updateUser](nosql-protocol-database-commands.md#updateuser) to update MariaDB user as well.

Note that the `mxsUpdateUser` command does not check that the changed data is compatible e.g. with the grants of the corresponding MariaDB user.

**Syntax**

The 'mxsUpdateUser' command has the following syntax:

```
db.runCommand(
    {
        mxsUpdateUser: "<name>",
        pwd: passwordPrompt(),  // Or "<cleartext password>"
        customData: { <any information> },
        roles: [
            { role: "<role>", db: "<database>" } | "<role>",
            ...
        ],
        mechanisms: [ "<scram-mechanism>", ...],
        digestPassword: <boolean>
    }
)
```

**Command Fields**

The command has the following fields:

| Field          | Type     | Description                                                                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mxsUpdateUser  | string   | The name of the user to be updated.                                                                                                                                      |
| pwd            | string   | The password in cleartext.                                                                                                                                               |
| customData     | document | Optional. Any arbitrary information.                                                                                                                                     |
| roles          | array    | The roles granted to the user.                                                                                                                                           |
| mechanisms     | array    | Optional. The specific supported SCRAM mechanisms for this user. If a new password is not provided, the specified mechanisms must be a subset of the current mechanisms. |
| digestPassword | boolean  | Optional. If specified, must be true.                                                                                                                                    |

The `roles` array should contain roles that a compatible with the grants of the user. Please check [roles and privileges](nosql-protocol-authentication.md#roles-and-privileges) for a discussion on how to map roles map to privileges.

**Returns**

If the updating of the user succeeds, the command returns a document with the single field `ok` whose value is `1`.

```
> db.runCommand({mxsUpdateUser: "user", pwd: "pwd", roles: ["readWrite"]});
{ "ok" : 1 }
```

If there is a failure of some kind, the command returns an error document

```
> db.runCommand({mxsUpdateUser: "user", roles: ["redWrite"]});
{
    "ok" : 0,
    "errmsg" : "No role named redWrite@test",
    "code" : 31,
    "codeName" : "RoleNotFound"
}
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
