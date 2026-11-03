---
hidden: true
description: >-
  Learn the GTFS data format and design the transit schema with Ignite annotations
---

# Understanding GTFS Data and Creating the Transit Schema

This module covers the General Transit Feed Specification (GTFS) data format and how to model transit data within Apache Ignite using Java annotations.

## The GTFS Format: Transit Data in Motion

The [General Transit Feed Specification](https://gtfs.org) (GTFS) is the industry standard used by transit agencies worldwide to share transit information in a consistent, machine-readable format. It was created through a collaboration between Google and Portland's TriMet transit agency in 2006.

GTFS comes in two formats:

1. **GTFS Static**: The foundation of transit data, containing:
   - Route definitions (paths that vehicles travel)
   - Stop locations (where vehicles pick up passengers)
   - Schedules (when vehicles are expected at stops)
   - Fares (how much it costs to ride)

2. **GTFS Realtime**: The dynamic extension that provides near real-time updates:
   - Vehicle Positions (where vehicles are right now)
   - Service Alerts (disruptions, detours, etc.)
   - Trip Updates (predictions of arrival/departure times)

The transit monitoring system focuses on the **Vehicle Positions** component of GTFS Realtime. This provides a continuous stream of data points showing where each transit vehicle is located, what route it serves, and its current status (in transit, stopped at a location, etc.).

## Analyzing the Data: What's in a Vehicle Position?

Before designing the schema, examine what information is available in a GTFS vehicle position record:

| Field | Description | Example | Used? |
|-------|-------------|---------|-------|
| Vehicle ID | Unique identifier for the vehicle | "1234" | Yes - Primary key |
| Route ID | Identifier for the route the vehicle is servicing | "42" | Yes - For filtering |
| Trip ID | Identifier for the specific trip being made | "trip_morning_1" | No - Not needed for monitoring |
| Position | Latitude and longitude coordinates | (37.7749, -122.4194) | Yes - For mapping |
| Timestamp | When the position was recorded | 1616724123000 | Yes - Primary key component |
| Status | Current status of the vehicle | "IN_TRANSIT_TO", "STOPPED_AT" | Yes - For monitoring |
| Stop ID | Identifier of the stop if the vehicle is stopped | "stop_downtown_3" | No - Not needed for basic monitoring |
| Congestion Level | Level of traffic congestion | "RUNNING_SMOOTHLY" | No - Not in scope |
| Occupancy Status | How full the vehicle is | "MANY_SEATS_AVAILABLE" | No - Not in scope |

The application uses the most essential fields: vehicle ID, route ID, position coordinates, timestamp, and status. This provides the core information needed for monitoring while keeping the schema focused.

## Ignite 3 Annotation System

Apache Ignite 3 provides an annotation system that defines database schemas directly in Java code. This creates a clear mapping between application objects and database tables:

- **Type safety**: Compile-time checking prevents many schema-related errors
- **Co-location of code and schema**: Changes to objects automatically reflect in the schema
- **Reduced boilerplate**: No need for separate SQL schema definitions
- **IDE support**: Code completion and refactoring tools help maintain consistency

### Core Annotations

| Annotation | Purpose | Location |
|------------|---------|----------|
| `@Table` | Marks a class as an Ignite table | Class level |
| `@Id` | Designates a field as part of the primary key | Field level |
| `@Column` | Maps a field to a database column | Field level |
| `@Zone` | Specifies the distribution zone for the table | Inside `@Table` |
| `@Index` | Creates a secondary index on columns | Inside `@Table` |
| `@ColumnRef` | References a column in an index or co-location | Inside `@Index` or co-location |

## Creating the Model Class With Annotations

Open `VehiclePosition.java` from the repository:

```bash
open src/main/java/com/example/transit/model/VehiclePosition.java
```

The key part of the class with annotations:

```java
@Table(
        zone = @Zone(value = "transit", storageProfiles = "default"),
        indexes = {
                @Index(value = "IDX_VP_ROUTE_ID", columns = { @ColumnRef("route_id") }),
                @Index(value = "IDX_VP_STATUS", columns = { @ColumnRef("current_status") })
        }
)
public class VehiclePosition {
    @Id
    @Column(value = "vehicle_id", nullable = false)
    private String vehicleId;

    @Id
    @Column(value = "time_stamp", nullable = false)
    private LocalDateTime timestamp;

    @Column(value = "route_id", nullable = false)
    private String routeId;

    @Column(value = "latitude", nullable = false)
    private Double latitude;

    @Column(value = "longitude", nullable = false)
    private Double longitude;

    @Column(value = "current_status", nullable = false)
    private String currentStatus;

    // Constructors, getters, setters...
}
```

### @Table Annotation

```java
@Table(
    zone = @Zone(value = "transit", storageProfiles = "default"),
    indexes = {
        @Index(value = "IDX_VP_ROUTE_ID", columns = { @ColumnRef("route_id") }),
        @Index(value = "IDX_VP_STATUS", columns = { @ColumnRef("current_status") })
    }
)
```

The `@Table` annotation marks this class as a database table in Ignite:

- **zone**: Specifies which distribution zone the table belongs to
- **indexes**: Defines secondary indexes for query optimization
- The table name defaults to the class name ("VehiclePosition")

### @Zone Annotation

```java
@Zone(value = "transit", storageProfiles = "default")
```

A distribution zone in Ignite controls how data is distributed across the cluster, including how many partitions the data is split into, how many replicas exist for redundancy, and which storage engines are used. The `value` names the zone ("transit") and `storageProfiles` specifies the storage profile.

### @Index Annotation

```java
@Index(value = "IDX_VP_ROUTE_ID", columns = { @ColumnRef("route_id") })
```

The `@Index` annotation creates secondary indexes that improve query performance when filtering or sorting on specific columns. The `value` provides a unique name for the index, and `columns` specifies which columns to index using their database names.

### @Id Annotation

```java
@Id
@Column(value = "vehicle_id", nullable = false)
private String vehicleId;

@Id
@Column(value = "time_stamp", nullable = false)
private LocalDateTime timestamp;
```

Multiple `@Id` annotations create a composite primary key. This allows storing multiple positions for the same vehicle (at different times) while enforcing uniqueness for each vehicle's position at a given timestamp. The first `@Id` field is the most significant in the key.

### @Column Annotation

```java
@Column(value = "route_id", nullable = false)
private String routeId;
```

The `@Column` annotation maps a Java field to a database column. The `value` attribute specifies the column name in the database, and `nullable` controls whether NULL values are allowed.

## Understanding the Table Manager

The repository includes a `VehiclePositionTableManager` class that handles creating the schema. Open it:

```bash
open src/main/java/com/example/transit/config/VehiclePositionTableManager.java
```

The key method is `createSchema()`:

```java
public boolean createSchema() {
    try {
        IgniteClient client = connectionManager.getClient();

        // Check if table exists
        if (tableExists(client, VEHICLE_POSITIONS_TABLE)) {
            System.out.println("--- Vehicle positions table already exists");
            return true;
        }

        // Create zone if it doesn't exist
        System.out.println(">>> Creating 'transit' zone if it doesn't exist");
        ZoneDefinition transitZone = ZoneDefinition.builder("transit")
                .ifNotExists()
                .replicas(2)
                .storageProfiles("default")
                .build();
        client.catalog().createZone(transitZone);

        // Create table
        System.out.println(">>> Creating table: " + VEHICLE_POSITIONS_TABLE);
        client.catalog().createTable(VehiclePosition.class);

        return true;
    } catch (Exception e) {
        logger.error("Failed to create schema: {}", e.getMessage());
        return false;
    }
}
```

This method:

1. Checks if the table already exists to avoid duplicate creation
2. Creates a distribution zone named "transit" with 2 replicas for redundancy
3. Creates the `VehiclePosition` table using the annotations in the POJO class

The call `client.catalog().createTable(VehiclePosition.class)` reads the annotations from the `VehiclePosition` class and creates a corresponding table in the Ignite cluster.

### From Annotations to SQL DDL

Under the hood, Ignite translates the annotated class into SQL DDL statements. The `VehiclePosition` class generates the equivalent of:

```sql
-- Create the zone if it doesn't exist
CREATE ZONE IF NOT EXISTS transit
WITH STORAGE_PROFILES='default', REPLICAS=2;

-- Create the table
CREATE TABLE VehiclePosition (
    vehicle_id VARCHAR NOT NULL,
    time_stamp TIMESTAMP NOT NULL,
    route_id VARCHAR NOT NULL,
    latitude DOUBLE NOT NULL,
    longitude DOUBLE NOT NULL,
    current_status VARCHAR NOT NULL,
    PRIMARY KEY (vehicle_id, time_stamp)
) ZONE transit;

-- Create the indexes
CREATE INDEX IDX_VP_ROUTE_ID ON VehiclePosition(route_id);
CREATE INDEX IDX_VP_STATUS ON VehiclePosition(current_status);
```

## Schema Design Decisions

Key decisions in this schema design:

1. **Composite Primary Key**: The primary key consists of `vehicle_id` and `time_stamp`. This allows storing multiple positions for the same vehicle (at different times), efficiently querying the history of a specific vehicle, and enforcing uniqueness for each vehicle's position at a given time.

2. **Column Types**: `VARCHAR` for string identifiers, `DOUBLE` for precise geographic coordinates, and `TIMESTAMP` for temporal data that supports SQL time functions and comparisons.

3. **Distribution Zone**: The "transit" zone with 2 replicas provides data redundancy (each record exists on two nodes), fault tolerance (the system continues if one node fails), and load balancing (queries can be directed to either replica).

4. **Indexes**: Two secondary indexes on `route_id` (to quickly find all vehicles on a specific route) and `current_status` (to filter by vehicle status).

## Interacting With Ignite

Run the schema setup example to see the annotations in action:

```bash
mvn compile exec:java@schema-setup-example
```

This runs the `SchemaSetupExample` class. Open it:

```bash
open src/main/java/com/example/transit/examples/SchemaSetupExample.java
```

{% hint style="success" %}
**Checkpoint:** The schema setup example should connect to the cluster, create the transit zone and VehiclePosition table, then run CRUD operations. If you see "Schema creation failed," verify the cluster is initialized.
{% endhint %}

The example performs a complete cycle of operations:

1. Connects to the Ignite cluster using the connection manager
2. Creates the schema using the `VehiclePositionTableManager`
3. Tests CRUD (Create, Read, Update, Delete) operations on the `VehiclePosition` table

The key table operations:

```java
// Get table and record view
Table vehicleTable = client.tables().table(VEHICLE_TABLE);
RecordView<VehiclePosition> vehicleView = vehicleTable.recordView(VehiclePosition.class);

// Insert test record
System.out.println(">>> Inserting test vehicle: " + testVehicle.getVehicleId());
vehicleView.upsert(null, testVehicle);

// Retrieve the record
VehiclePosition keyVehicle = new VehiclePosition();
keyVehicle.setVehicleId(testVehicle.getVehicleId());
keyVehicle.setTimestamp(testVehicle.getTimestamp());

VehiclePosition retrievedVehicle = vehicleView.get(null, keyVehicle);
```

This demonstrates:

1. **Obtaining a Table Reference**: `client.tables().table(VEHICLE_TABLE)`
2. **Creating a RecordView**: A typed interface for working with table records
3. **Upserting Data**: Adding a record to the table
4. **Retrieving Data**: Reading a record by its primary key

The `RecordView` interface provides a type-safe way to interact with the database. Ignite handles the mapping between Java objects and database records based on the annotations.

### Working With Primary Keys

When retrieving or deleting records, only set the primary key fields in the POJO. For the composite key:

```java
// Create an object with just the primary key fields
VehiclePosition keyVehicle = new VehiclePosition();
keyVehicle.setVehicleId(testVehicle.getVehicleId());
keyVehicle.setTimestamp(testVehicle.getTimestamp());

// Use it to retrieve a record
VehiclePosition retrievedVehicle = vehicleView.get(null, keyVehicle);
```

This pattern is common in Ignite applications: create a minimal object with just the key fields set.

### Using SQL With the Schema

While the POJO annotation approach provides type-safe interactions, SQL queries work against the same schema:

```java
// SQL query to verify deletion
var countResult = client.sql().execute((Transaction) null,
        "SELECT COUNT(*) as cnt FROM " + VEHICLE_TABLE +
                " WHERE vehicle_id = ?", testVehicle.getVehicleId());

long count = 0;
if (countResult.hasNext()) {
    count = countResult.next().longValue("cnt");
}
```

This SQL query counts records matching a specific vehicle ID, demonstrating how to combine the strongly-typed POJO approach with flexible SQL queries.

## Next Steps

This module covered the GTFS data format, Ignite 3's annotation system for schema definition, the `VehiclePosition` model class, and basic operations for working with the schema.

The schema provides the foundation for the transit monitoring system. The next module builds a client to fetch real-time GTFS data from a transit agency and feed it into the Ignite database.
