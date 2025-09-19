# MaxScale KafkaImporter

## KafkaImporter

### Overview

The KafkaImporter module reads messages from Kafka and streams them into a
MariaDB server. The messages are inserted into a table designated by either the
topic name or the message key (see [table\_name\_in](maxscale-kafkaimporter.md#table_name_in) for
details). By default the table will be automatically created with the following
SQL:

```
CREATE TABLE IF NOT EXISTS my_table (
  data JSON NOT NULL,
  id VARCHAR(1024) AS (JSON_EXTRACT(data, '$._id')) UNIQUE KEY
);
```

The payload of the message is inserted into the `data` field from which the `id`
field is calculated. The payload must be a valid JSON object and it must either
contain a unique `_id` field or it must not exist or the value must be a JSON
null. This is similar to the MongoDB document format where the `_id` field is
the primary key of the document collection.

If a message is read from Kafka and the insertion into the table fails due to a
violation of one of the constraints, the message is ignored. Similarly, messages
with duplicate `_id` value are also ignored: this is done to avoid inserting the
same document multiple times whenever the connection to either Kafka or MariaDB
is lost.

The limitations on the data can be removed by either creating the table before
the KafkaImporter is started, in which case the `CREATE TABLE IF NOT EXISTS`
does nothing, or by altering the structure of the existing table. The minimum
requirement that must be met is that the table contains the `data` field to
which string values can be inserted into.

The database server where the data is inserted is chosen from the set of servers
available to the service. The first server labeled as the `Master` with the best
rank will be chosen. This means that a monitor must be configured for the
MariaDB server where the data is to be inserted.

In MaxScale versions 21.06.18, 22.08.15, 23.02.12, 23.08.8, 24.02.4 and 25.01.1
the `_id` field is not required to be present. Older versions of MaxScale used
the following SQL where the `_id` field was mandatory:

```
CREATE TABLE IF NOT EXISTS my_table (
  data LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  id VARCHAR(1024) AS (JSON_EXTRACT(data, '$._id')) UNIQUE KEY,
  CONSTRAINT data_is_json CHECK(JSON_VALID(data)),
  CONSTRAINT id_is_not_null CHECK(JSON_EXTRACT(data, '$._id') IS NOT NULL)
);
```

#### Required Grants

The user defined by the `user` parameter of the service must have `INSERT` and`CREATE` privileges on all tables that are created.

### Settings

#### `bootstrap_servers`

* Type: string
* Mandatory: Yes
* Dynamic: Yes

The list of Kafka brokers as a CSV list in `host:port` format.

#### `topics`

* Type: stringlist
* Mandatory: Yes
* Dynamic: Yes

The comma separated list of topics to subscribe to.

#### `batch_size`

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `100`

Maximum number of uncommitted records. The KafkaImporter will buffer records
into batches and commit them once either enough records are gathered (controlled
by this parameter) or when the KafkaImporter goes idle. Any uncommitted records
will be read again if a reconnection to either Kafka or MariaDB occurs.

#### `kafka_sasl_mechanism`

* Type: [enum](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

SASL mechanism to use. The Kafka broker must be configured with the same
authentication scheme.

#### `kafka_sasl_user`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

SASL username used for authentication. If this parameter is defined,`kafka_sasl_password` must also be provided.

#### `kafka_sasl_password`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

SASL password for the user. If this parameter is defined, `kafka_sasl_user` must
also be provided.

#### `kafka_ssl`

* Type: [boolean](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

Enable SSL for Kafka connections.

#### `kafka_ssl_ca`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

SSL Certificate Authority file in PEM format. If this parameter is not
defined, the system default CA certificate is used.

#### `kafka_ssl_cert`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

SSL public certificate file in PEM format. If this parameter is defined,`kafka_ssl_key` must also be provided.

#### `kafka_ssl_key`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

SSL private key file in PEM format. If this parameter is defined,`kafka_ssl_cert` must also be provided.

#### `table_name_in`

* Type: [enum](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Values: `topic`, `key`
* Default: `topic`

The Kafka message part that is used to locate the table to insert the data into.

Enumeration Values:

* `topic`: The topic named is used as the fully qualified table name.
* `key`: The message key is used as the fully qualified table name. If the Kafka
  message does not have a key, the message is ignored.

For example, all messages with a fully qualified table name of `my_db.my_table`
will be inserted into the table `my_table` located in the `my_db` database. If
the table or database names have special characters that must be escaped to make
them valid identifiers, the name must also contain those escape characters. For
example, to insert into a table named `my table` in the database `my database`,
the name would be:

```
`my database`.`my table`
```

#### `timeout`

* Type: [duration](../../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md)
* Mandatory: No
* Dynamic: Yes
* Default: `5000ms`

Timeout for both Kafka and MariaDB network communication.

#### `engine`

* Type: string
* Default: `InnoDB`
* Mandatory: No
* Dynamic: Yes

The storage engine used for tables that are created by the KafkaImporter.

This defines the `ENGINE` table option and must be the name of a valid storage
engine in MariaDB. When the storage engine is something other than `InnoDB`, the
table is created without the generated column and the check constraints:

```
CREATE TABLE IF NOT EXISTS my_table (data JSON NOT NULL);
```

This is done to avoid conflicts where the custom engine does not support all the
features that InnoDB supports.

### Limitations

* The backend servers used by this service must be MariaDB version 10.2 or
  newer.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
