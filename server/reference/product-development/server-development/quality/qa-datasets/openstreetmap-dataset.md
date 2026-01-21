---
description: >-
  Information on the standardized datasets and database dumps used for
  OpenStreetMap tests.
---

# OpenStreetMap Dataset

This page describes how to use the OpenStreetMap dataset in testing.

## Database Schema

The database schema is available [here](osmdb06sql.md). To import:

```
mysqladmin create osm
cat osmdb06.sql | mysql osm
```

By default, this schema uses a mixture of InnoDB and MyISAM tables. To convert\
all tables to Aria:

```
sed -i -e 's/InnoDB/Aria/gi' osmdb06.sql
sed -i -e 's/MyISAM/Aria/gi' osmdb06.sql
```

30 tables are created.

## Data

The data is provided in the form of XML files (.OSM files) that require the\
Java-based [Osmosis](https://wiki.openstreetmap.org/wiki/Osmosis) tool to load\
into MariaDB. The tool is available from [dev.openstreetmap.org](https://dev.openstreetmap.org/~bretth/osmosis-build/osmosis-latest.tgz).\
Version 0.36 is known to work.

Various .OSM files are available, including the [entire world](https://wiki.openstreetmap.org/wiki/Planet.osm) (>200Gb unzipped)\
and [individual countries](https://download.geofabrik.de/osm/).

Data is loaded with the following command-line (in the example, we're using the\
bulgaria.osm file, replace with the file you choose):

```
chmod +x bin/osmosis
bin/osmosis --read-xml file=bulgaria.osm --write-apidb dbType="mysql" host="localhost:port" validateSchemaVersion=no database="osm" user="root" password="<password-goes-here>"
```

Data is inserted into 19 tables, as follows:

```
MariaDB [(none)]> use information_schema;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [information_schema]> select TABLE_NAME, TABLE_ROWS from TABLES
    -> where TABLE_ROWS > 0
    -> AND
    -> TABLE_SCHEMA='osm'
    -> ORDER BY TABLE_ROWS DESC;
+--------------------------+------------+
| TABLE_NAME               | TABLE_ROWS |
+--------------------------+------------+
| current_way_nodes        |    1559099 |
| way_nodes                |    1559099 |
| current_nodes            |    1477247 |
| nodes                    |    1477247 |
| node_tags                |     311751 |
| way_tags                 |     287585 |
| ways                     |     100007 |
| current_ways             |     100007 |
| changeset_tags           |      18738 |
| current_relation_members |      14560 |
| relation_members         |      14560 |
| changesets               |       9369 |
| relation_tags            |       3948 |
| current_relations        |        937 |
| relations                |        937 |
| users                    |        537 |
+--------------------------+------------+
16 rows in set (0.00 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
