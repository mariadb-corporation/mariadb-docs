---
hidden: true
description: >-
  Implement batch data ingestion with transactions into Apache Ignite
---

# Building the Data Ingestion Service

This module implements a data ingestion service that continuously fetches vehicle position data from GTFS feeds and stores it in Apache Ignite using batch transactions.

## Understanding Data Ingestion Requirements

Real-time transit monitoring demands a reliable data pipeline with specific characteristics:

1. **Periodic data collection**: Regularly fetching the latest data to maintain freshness
2. **Efficient data storage**: Minimizing database overhead during insertion
3. **Fault tolerance**: Handling errors without service disruption
4. **Resource management**: Properly managing connections and threads
5. **Configurable behavior**: Adjusting parameters like frequency based on requirements

## The Data Ingestion Workflow

The data ingestion workflow follows these steps:

1. **Scheduled execution**: A timer triggers data collection at regular intervals
2. **Data fetching**: The GTFS client retrieves vehicle positions from the transit feed
3. **Data transformation**: Vehicle data is converted to the domain model format
4. **Batch processing**: Records are grouped into batches for efficient storage
5. **Transactional storage**: Each batch is stored atomically in the database
6. **Statistics tracking**: Metrics are collected to monitor ingestion performance

## Ingest Service Implementation

Open the `DataIngestionService` class:

```bash
open src/main/java/com/example/transit/service/DataIngestionService.java
```

The core functionality is in the `fetchAndStoreData()` method, which the scheduler calls periodically:

```java
private void fetchAndStoreData() {
    long fetchStartTime = System.currentTimeMillis();
    try {
        // Fetch the latest vehicle positions
        List<VehiclePosition> positions = gtfsService.getVehiclePositions();
        lastFetchCount.set(positions.size());
        totalFetched.addAndGet(positions.size());

        if (!positions.isEmpty()) {
            // Store the positions in the database
            int recordsStored = storeVehiclePositions(positions);
            totalStored.addAndGet(recordsStored);

            System.out.println(">>> Fetched " + positions.size() +
                    " and stored " + recordsStored +
                    " vehicle positions");
        } else {
            System.out.println("No vehicle positions fetched from feed");
        }

    } catch (Exception e) {
        logger.error("Error in data ingestion: {}", e.getMessage());
    } finally {
        lastFetchTime.set(System.currentTimeMillis() - fetchStartTime);
    }
}
```

This method records the start time for performance measurement, calls the GTFS service to fetch vehicle positions, updates statistics counters, delegates to `storeVehiclePositions()` for persistence, and captures timing statistics.

The actual storage happens in `storeVehiclePositions()`:

```java
private int storeVehiclePositions(List<VehiclePosition> positions) {
    if (positions.isEmpty()) {
        return 0;
    }

    int recordsProcessed = 0;
    IgniteClient client = connectionManager.getClient();

    try {
        // Get table and record view for vehicle positions
        Table vehiclePositionsTable = client.tables().table(VehiclePosition.class.getSimpleName());
        RecordView<VehiclePosition> recordView = vehiclePositionsTable.recordView(VehiclePosition.class);

        // Process records in batches
        for (int i = 0; i < positions.size(); i += batchSize) {
            // Determine the end index for current batch
            int endIndex = Math.min(i + batchSize, positions.size());
            List<VehiclePosition> batch = positions.subList(i, endIndex);

            // Use runInTransaction to automatically handle transaction lifecycle
            client.transactions().runInTransaction(tx -> {
                recordView.upsertAll(tx, batch);
                return null;
            });

            recordsProcessed += batch.size();
        }

        return recordsProcessed;
    } catch (Exception e) {
        logger.error("Error storing vehicle positions: {}", e.getMessage());
        return recordsProcessed;
    }
}
```

This method obtains a reference to the vehicle positions table, creates a `RecordView` for type-safe operations, processes records in configurable batches, and uses `runInTransaction` to ensure each batch is stored atomically. If any upsert within a batch fails, the entire batch rolls back.

## Statistics Tracking

The service tracks performance metrics using atomic variables:

```java
// Statistics tracking
private final AtomicLong totalFetched = new AtomicLong(0);
private final AtomicLong totalStored = new AtomicLong(0);
private final AtomicLong lastFetchCount = new AtomicLong(0);
private final AtomicLong lastFetchTime = new AtomicLong(0);
private long startTime;
```

These statistics are exposed through the `IngestStats` class, an immutable data container:

```bash
open src/main/java/com/example/transit/model/IngestStats.java
```

```java
public class IngestStats {
    private final long totalFetched;
    private final long totalStored;
    private final long lastFetchCount;
    private final long lastFetchTimeMs;
    private final long runningTimeMs;
    private final boolean running;

    // Constructor and getters...
}
```

## Service Lifecycle Management

The `DataIngestionService` includes methods to start and stop the service:

```java
public void start(int intervalSeconds) {
    if (scheduledTask != null) {
        System.out.println("Ingestion service is already running. Stop it first before restarting.");
        return;
    }

    // Reset statistics tracking
    this.startTime = System.currentTimeMillis();
    this.totalFetched.set(0);
    this.totalStored.set(0);
    this.lastFetchCount.set(0);
    this.lastFetchTime.set(0);

    // Schedule the task to run at fixed intervals
    scheduledTask = scheduler.scheduleAtFixedRate(
            this::fetchAndStoreData,
            0,  // Start immediately
            intervalSeconds,
            TimeUnit.SECONDS);

    System.out.println("--- Data ingestion service started with "
            + intervalSeconds + " second interval");
}

public void stop() {
    if (scheduledTask != null) {
        scheduledTask.cancel(false); // Don't interrupt if running
        scheduledTask = null;

        // Properly shut down the executor service
        try {
            // Attempt to shut down gracefully
            scheduler.shutdown();
            if (!scheduler.awaitTermination(5, TimeUnit.SECONDS)) {
                // Force shutdown if graceful shutdown fails
                scheduler.shutdownNow();
            }
            System.out.println("=== Data ingestion service stopped");
        } catch (InterruptedException e) {
            // If interrupted during shutdown, force immediate shutdown
            scheduler.shutdownNow();
            Thread.currentThread().interrupt(); // Preserve interrupt status
            System.err.println("Data ingestion service shutdown interrupted");
        }
    } else {
        System.err.println("Ingestion service is not running");
    }
}
```

The `start()` method resets statistics and schedules `fetchAndStoreData` at fixed intervals. The `stop()` method performs a graceful shutdown with a 5-second timeout, falling back to forced shutdown if necessary.

## Running the Ingest Example

Run the ingestion service example:

```bash
mvn compile exec:java@ingest-example
```

This runs the `IngestExample` class:

```bash
open src/main/java/com/example/transit/examples/IngestExample.java
```

The example verifies database connectivity, sets up the schema if needed, starts the ingestion service with a 15-second interval, runs for 45 seconds while showing a progress indicator, displays statistics, and stops the service.

The core part:

```java
// Create GTFS feed service and data ingestion service
System.out.println("\n=== Starting data ingestion service");
GtfsService feedService = new GtfsService(config.getFeedUrl());
DataIngestionService ingestService = new DataIngestionService(
        feedService, connectionManager)
        .withBatchSize(100); // Configure batch size

try {
    ingestService.start(15); // Fetch every 15 seconds
    reportingService.displayIngestionStatus(ingestService.getStatistics());

    // Wait for some data to be ingested
    System.out.println("\n=== Waiting for data ingestion (45 seconds)...");

    // ... (waiting code) ...

    // Verify data after ingestion
    System.out.println("\n--- Data state after ingestion");
    reportingService.displaySystemStatistics();

    // Display ingestion statistics
    ingestService.printStatistics();
} finally {
    // Always stop the ingestion service before exiting
    System.out.println("\n=== Stopping data ingestion service");
    ingestService.stop();
    reportingService.displayIngestionStatus(ingestService.getStatistics());
}
```

Expected output:

```text
=== Data Ingestion Service Example ===
--- Setting up database schema
--- Vehicle positions table already exists

--- Initial data state
Verifying data in VehiclePosition table
<<< Table contains 1532 records

Sample records (most recent):
Vehicle: 5730, Route: 22, Status: STOPPED_AT, Time: 2025-03-25 16:54:46
Vehicle: 1010, Route: F, Status: IN_TRANSIT_TO, Time: 2025-03-25 16:54:46
Vehicle: 5813, Route: 1, Status: IN_TRANSIT_TO, Time: 2025-03-25 16:54:46

Top routes by number of records:
Route 29: 88 records
Route 14R: 88 records
Route 49: 88 records
Route 1: 80 records
Route 22: 80 records

=== Starting data ingestion service
--- Data ingestion service started with 15 second interval
• Status: Running
• Records fetched: 0
• Records stored: 0
• Last fetch count: 0
• Running time: 00:00:00

=== Waiting for data ingestion (45 seconds)...
--- Data ingestion wait complete!

--- Data state after ingestion
• Total records: 2068
• Unique vehicles: 536
• Oldest record: 2025-03-25 16:54:46
• Newest record: 2025-03-25 17:01:11
• Data collection active

=== Ingestion Statistics ===
• Status: Running
• Running time: 00:00:45
• Total records fetched: 536
• Total records stored: 536
• Last fetch count: 536
• Last fetch time: 1253ms
• Ingestion rate: 11.91 records/second
============================

=== Stopping data ingestion service
=== Data ingestion service stopped
• Status: Stopped
• Records fetched: 536
• Records stored: 536
• Last fetch count: 536
• Last fetch time: 1253ms
• Running time: 00:00:46

=== Example completed successfully!
```

{% hint style="success" %}
**Checkpoint:** You should see the ingestion service start, fetch vehicle positions, and display statistics showing records fetched and stored. The total records count should increase after the ingestion run.
{% endhint %}

## Next Steps

This module implemented a data ingestion service that periodically fetches vehicle position data from GTFS-realtime feeds, stores it efficiently using batch transactions, handles errors gracefully, and provides performance statistics.

The next module builds on this foundation by implementing a monitoring service that detects service disruptions in real-time.
