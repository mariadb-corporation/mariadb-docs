---
description: >-
  Distribution zones in GridGain 9 and the SQL commands that manage them: CREATE
  ZONE, ALTER ZONE, and DROP ZONE, with keywords, parameters, and examples.
---

# Distribution Zones

This section describes GridGain 9 distribution zones. In GridGain 9, you can fine-tune distribution of your partitions on nodes for better performance and stability.

## CREATE ZONE

Creates a new distribution zone.

{% hint style="info" %}
This can also be done via the [Java API](../../gridgain9-usage/tables-from-java-classes.md).
{% endhint %}

```bnf
CREATE ZONE [ IF NOT EXISTS ] qualified_zone_name
  [ ( zone_parameter [, zone_parameter]... ) ]
  STORAGE PROFILES [storage_profile [, storage_profile]...] ;
```

<!-- Diagram(
Terminal("CREATE ZONE"),
Optional(Terminal("IF NOT EXISTS")),
NonTerminal("qualified_zone_name", { href: "./grammar-reference/#qualified-zone-name" }),
Optional(
Sequence(
Terminal("("),
OneOrMore(
NonTerminal("zone_parameter", { href: "./grammar-reference/#zone-parameter" }),
Terminal(",")
),
Terminal(")")
)
),
End({ type: "complex" })
)

Diagram(
Start({ type: "complex" }),
Terminal("STORAGE PROFILES"),
Terminal("["),
OneOrMore(
NonTerminal("storage_profile", { href: "./grammar-reference/#storage-profile" }),
Terminal(",")
),
Terminal("]"),
Terminal(";")
) -->

**Keywords and parameters**

* `IF NOT EXISTS` - create a zone only if a different zone with the same name does not exist.
* `qualified_zone_name` - a name of the distribution zone. Can be specified as a case-sensitive string or case-insensitive identifier. Does not need to exist at the moment of table creation, and can be created before writing data.
* `STORAGE PROFILES` - Required. Comma-separated list of the profiles of the storage engines to use.
* `PARTITIONS` - the number of partition the data is divided into. Partitions are then split between nodes for storage.
* `REPLICAS` - the number of copies of each partition.
* `NODES FILTER` - specifies the nodes that can be used to store data in the distribution zone based on node attributes. You can configure node attributes by using the CLI. Filter uses JSONPath rules. Missing attributes are treated as `null`: for example, `$[?(@.storage != 'SSD']` will also include nodes without the `storage` attribute specified.
It's also possible to combine multiple attribute-related expressions in one filter using:

  - `OR (||)`, for example `$[?(@.region == "US" || @.region == "EU")]` or `$[?(@.region == "US" || @.storage == "SSD")]`
  - `AND (&&)`, for example `$[?(@.region == "US" && @.storage == "SSD")]`
  - `NOT (!)`, for example `$[?(@.region != "US"]`

  Please see JSONPath [documentation](https://docs.oracle.com/cd/E60058_01/PDF/8.0.8.x/8.0.8.0.0/PMF_HTML/JsonPath_Expressions.htm) for more details.

* `AUTO SCALE UP` - Configures automatic scaling up of the distribution zone. Possible values:
  - `OFF` - disables the automatic distribution zone adjustment.
  - `integer` - the delay in seconds between the new node joining and the start of distribution zone adjustment. Possible values are between 0 and 2147483647. Default value: 5.
* `AUTO SCALE DOWN` - Configures automatic scaling down of the distribution zone. Possible values:
  - `OFF` - disables the automatic distribution zone adjustment. Default value.
  - `integer` - the delay in seconds between the new node joining and the start of distribution zone adjustment. Possible values are between 0 and 2147483647.
* `CONSISTENCY MODE` - how the zone handles partition majority losses. If set to `STRONG CONSISTENCY`, the data will become unavailable until majority is restored (typically, this means nodes leaving and returning to the cluster). `HIGH AVAILABILITY` means that the data will be written and read from remaining nodes, accepting possible data loss. Default value: `STRONG_CONSISTENCY`.
* `QUORUM SIZE` - the size of the majority of nodes in the consensus of a replication group. Quorum size is determined by the replica count.

  *Minimal* value: `1` if there is only one replica and `2` if there is more than one.
  *Maximum* value: half the total number of replicas rounded up.

  *Default values*: `3` if there are 5 and more replicas. Otherwise, the smallest of 2 and the total replica count.

**Examples**

- Creates an `exampleZone` distribution zone that is specified as a *case-insensitive* identifier:

  ```sql
  CREATE ZONE IF NOT EXISTS exampleZone STORAGE PROFILES['default'];
  ```

- Creates a `"myExampleZone"` distribution zone that is specified as a *case-sensitive* string:

  ```sql
  CREATE ZONE IF NOT EXISTS "myExampleZone" STORAGE PROFILES['default'];
  ```

- Creates an `exampleZone` distribution zone that will adjust 300 seconds after cluster topology changes before adding nodes:

  ```sql
  CREATE ZONE IF NOT EXISTS exampleZone (AUTO SCALE UP 300) STORAGE PROFILES['default'];
  ```

- Creates an `exampleZone` distribution zone that will wait 600 seconds before scaling down any idle nodes once the cluster topology changes:

  ```sql
  CREATE ZONE IF NOT EXISTS exampleZone (AUTO SCALE DOWN 600) STORAGE PROFILES['default'];
  ```

- Creates an `exampleZone` distribution zone where data will only be stored on nodes that have SSD attribute:

  ```sql
  CREATE ZONE IF NOT EXISTS exampleZone (NODES FILTER '$[?(@.storage == "SSD")]') STORAGE PROFILES['default'];
  ```

  {% hint style="info" %}
  The example above assumes that there are nodes that have the attribute set in [node filtering](../../architecture/storage/distribution-zones.md#node-filtering) example.
  {% endhint %}

- Creates an `exampleZone` distribution zone with consistency mode set to `HIGH_AVAILABILITY`:

  ```sql
  CREATE ZONE IF NOT EXISTS exampleZone (REPLICAS 5, CONSISTENCY MODE 'HIGH_AVAILABILITY') STORAGE PROFILES['default'];
  ```

## ALTER ZONE

Modifies a distribution zone.

### ALTER ZONE RENAME TO new_qualified_zone_name

```bnf
ALTER ZONE [ IF EXISTS ] qualified_zone_name RENAME TO new_qualified_zone_name
```

<!-- Diagram(
Terminal('ALTER ZONE'),
Optional(Terminal('IF EXISTS')),
NonTerminal('qualified_zone_name'),
Terminal('RENAME TO'),
NonTerminal('new_qualified_zone_name'),
) -->

**Keywords and parameters**

* `IF EXISTS` - do not throw an error if a zone with the specified name does not exist.
* `qualified_zone_name` - the current name of the distribution zone.
* `RENAME TO` - renames the selected zone to the new name.
* `new_qualified_zone_name` - the new name of the distribution zone (assigned by `RENAME`).

**Examples**

Renames the `exampleZone` to `renamedZone`:

```sql
ALTER ZONE IF EXISTS exampleZone RENAME TO renamedZone;
```

### ALTER ZONE SET

```bnf
ALTER ZONE [ IF EXISTS ] qualified_zone_name
  { SET [(] parameter [, parameter]... [)] | SET parameter }
```

<!-- Diagram(
Terminal('ALTER ZONE'),
Optional(Terminal('IF EXISTS')),
NonTerminal('qualified_zone_name'),
Choice(0,
Sequence(
Terminal('SET'),
Optional('('),
OneOrMore(
NonTerminal('parameter', {href:'./grammar-reference/#parameter'}),
','),
Optional(')')
),
Sequence(
Terminal('SET'),
NonTerminal('parameter', {href:'./grammar-reference/#parameter'})
)
)
) -->

**Keywords and parameters**

* `IF EXISTS` - do not throw an error if a zone with the specified name does not exist.
* `qualified_zone_name` - a name of the distribution zone.
* `SET` - assigns values to any or all of the following parameters:
  - `PARTITIONS` - the number of partitions.
  - `REPLICAS` - the number of copies of each partition.
  - `NODES FILTER` - specifies the nodes that can be used to store data in the distribution zone based on node attributes.
  - `AUTO SCALE` - Configures automatic distribution zone adjustment. Possible values:
    - `OFF` - disables the automatic distribution zone adjustment. Default value.
    - `integer` - the delay in seconds between the new node joining and the start of distribution zone adjustment. Possible values are between 0 and 2147483647.
  - `AUTO SCALE UP` - Configures automatic scaling up of the distribution zone. Possible values:
    - `OFF` - disables the automatic distribution zone adjustment. Default value.
    - `integer` - the delay in seconds between the new node joining and the start of distribution zone adjustment. Possible values are between 0 and 2147483647.
  - `AUTO SCALE DOWN` - Configures automatic scaling down of the distribution zone. Possible values:
    - `OFF` - disables the automatic distribution zone adjustment. Default value.
  - `QUORUM SIZE` - the size of the majority of nodes in the consensus of a replication group. Quorum size is determined by the replica count.

    *Minimal* value: `1` if there is only one replica and `2` if there is more than one.
    *Maximum* value: half the total number of replicas rounded up.

    *Default values*: `3` if there are 5 and more replicas. Otherwise, the smallest of 2 and the total replica count.

**Examples**

- Sets the number of data replicas to 10:

  ```sql
  ALTER ZONE IF EXISTS exampleZone SET REPLICAS 10;
  ```

- Sets data nodes filter to match the specific region, set the number of data replicas to 5 and quorum size to 3:

  ```sql
  ALTER ZONE IF EXISTS exampleZone SET (REPLICAS 5, QUORUM SIZE 3, NODES FILTER '$[?(@.region == "US")]');
  ```

### ALTER ZONE SET DEFAULT

Sets the zone as the default zone to use if no other zone is specified.

```bnf
ALTER ZONE [ IF EXISTS ] qualified_zone_name SET DEFAULT
```

<!-- Diagram(
Terminal('ALTER ZONE'),
Optional(Terminal('IF EXISTS')),
NonTerminal('qualified_zone_name'),
Sequence(
Terminal('SET'),
Terminal('DEFAULT')
)
) -->

**Examples**

- Sets the distribution zone as default zone:

  ```sql
  ALTER ZONE IF EXISTS exampleZone SET DEFAULT;
  ```

## DROP ZONE

Drops an existing distribution zone.

{% hint style="info" %}
This can also be done via the [Java API](../../gridgain9-usage/tables-from-java-classes.md).
{% endhint %}

```bnf
DROP ZONE IF EXISTS qualified_zone_name
```

<!-- Diagram(
Terminal('DROP ZONE'),
Terminal('IF EXISTS'),
NonTerminal('qualified_zone_name')
) -->

**Keywords and parameters**

* `IF EXISTS` - do not throw an error if a zone with the specified name does not exist.
* `qualified_zone_name` - the name of the distribution zone.

**Examples**

Drop Person table if the one exists:

```sql
DROP ZONE IF EXISTS exampleZone;
```
