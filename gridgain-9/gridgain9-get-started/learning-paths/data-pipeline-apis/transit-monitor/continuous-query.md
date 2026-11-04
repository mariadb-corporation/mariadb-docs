---
hidden: true
description: >-
  Implement SQL-based monitoring queries to detect transit service disruptions
---

# Adding a Service Monitor

This module implements a monitoring system that uses SQL queries to detect transit service disruptions such as delayed vehicles, route bunching, and offline vehicles.

## Transit Service Monitoring

An effective transit monitoring system detects potential issues by analyzing the current state of the fleet. The monitoring service checks for several key conditions:

1. **Delayed vehicles**: Vehicles that have been stopped for too long
2. **Vehicle bunching**: Multiple vehicles on the same route too close together
3. **Low route coverage**: Routes with fewer than the minimum required vehicles
4. **Offline vehicles**: Vehicles that haven't reported their position recently

These conditions help operators identify service disruptions before they significantly impact passengers.

## Understanding the Monitor Service

Open the `MonitorService` class:

```bash
open src/main/java/com/example/transit/service/MonitorService.java
```

The class contains configuration and tracking components:

```java
// Thresholds for monitoring conditions
private static final int STOPPED_THRESHOLD_MINUTES = 5;
private static final int BUNCHING_DISTANCE_KM = 1;
private static final int MINIMUM_VEHICLES_PER_ROUTE = 2;
private static final int OFFLINE_THRESHOLD_MINUTES = 15;

// Monitoring infrastructure
private final ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
private final IgniteClient client;

// Statistics tracking
private final Map<String, AtomicInteger> alertCounts = new HashMap<>();
private final List<ServiceAlert> recentAlerts = new ArrayList<>();
```

The service starts with `startMonitoring()`:

```java
public void startMonitoring(int intervalSeconds) {
    System.out.println("--- Starting service disruption monitoring (polling every " + intervalSeconds + " seconds)");

    // Schedule all monitoring tasks
    scheduler.scheduleAtFixedRate(
            this::performMonitoring,
            5,
            intervalSeconds,
            TimeUnit.SECONDS);
}
```

The `performMonitoring` method runs each check:

```java
private void performMonitoring() {
    checkForDelayedVehicles();
    checkForVehicleBunching();
    checkForLowRouteCoverage();
    checkForOfflineVehicles();
}
```

## Monitoring Delayed Vehicles

The delayed vehicles check:

```java
private void checkForDelayedVehicles() {
    try {
        // Query to detect vehicles stopped for more than the threshold time
        String querySql = "SELECT " +
                "    v.vehicle_id, " +
                "    v.route_id, " +
                "    v.current_status, " +
                "    v.latitude, " +
                "    v.longitude, " +
                "    v.time_stamp, " +
                "    TIMESTAMPDIFF(MINUTE, v.time_stamp, CURRENT_TIMESTAMP) as stopped_minutes " +
                "FROM VehiclePosition v " +
                "JOIN (" +
                "    SELECT vehicle_id, MAX(time_stamp) as latest_ts " +
                "    FROM VehiclePosition " +
                "    GROUP BY vehicle_id " +
                ") l ON v.vehicle_id = l.vehicle_id AND v.time_stamp = l.latest_ts " +
                "WHERE " +
                "    v.current_status = 'STOPPED_AT' " +
                "    AND TIMESTAMPDIFF(MINUTE, v.time_stamp, CURRENT_TIMESTAMP) >= ?";

        // Execute the query with the threshold parameter
        var result = client.sql().execute((Transaction) null, querySql, STOPPED_THRESHOLD_MINUTES);

        int count = 0;
        // Process each row in the result
        while (result.hasNext()) {
            var row = result.next();
            count++;

            String vehicleId = row.stringValue("vehicle_id");
            String routeId = row.stringValue("route_id");
            int stoppedMinutes = row.intValue("stopped_minutes");

            // Create and record the alert
            ServiceAlert alert = new ServiceAlert(
                    "DELAYED_VEHICLE",
                    "Vehicle " + vehicleId + " on route " + routeId +
                            " has been stopped for " + stoppedMinutes + " minutes",
                    routeId,
                    vehicleId,
                    row.doubleValue("latitude"),
                    row.doubleValue("longitude"),
                    stoppedMinutes);

            recordAlert(alert);

            // Only log the alert if not in quiet mode
            if (!quietMode) {
                System.out.println("[" + LocalDateTime.now().format(timeFormatter) +
                        "] ALERT: " + alert.getMessage());
            }
        }

        if (count > 0) {
            System.out.println("--- Found " + count + " delayed vehicles");
        }
    } catch (Exception e) {
        System.err.println("Error checking for delayed vehicles: " + e.getMessage());
    }
}
```

This method executes an SQL query that finds vehicles with a "STOPPED_AT" status that have been stopped longer than the threshold time, then creates and records alerts for each match.

## Understanding the Query Structure

The query uses a subquery with a JOIN to find the latest position for each vehicle:

```sql
SELECT v.vehicle_id, v.route_id, v.current_status, v.latitude, v.longitude, v.time_stamp,
       TIMESTAMPDIFF(MINUTE, v.time_stamp, CURRENT_TIMESTAMP) as stopped_minutes
FROM VehiclePosition v
JOIN (
    SELECT vehicle_id, MAX(time_stamp) as latest_ts
    FROM VehiclePosition
    GROUP BY vehicle_id
) l ON v.vehicle_id = l.vehicle_id AND v.time_stamp = l.latest_ts
WHERE v.current_status = 'STOPPED_AT'
  AND TIMESTAMPDIFF(MINUTE, v.time_stamp, CURRENT_TIMESTAMP) >= ?
```

The subquery finds the latest timestamp for each vehicle. The JOIN retrieves only the most recent position data. The WHERE clause filters for stopped vehicles exceeding the threshold. `TIMESTAMPDIFF` calculates the duration in minutes between the vehicle's last report and the current time.

## Service Alerts

The monitoring service creates `ServiceAlert` objects to represent detected issues. Open the class:

```bash
open src/main/java/com/example/transit/model/ServiceAlert.java
```

```java
public class ServiceAlert {
    private final String type;
    private final String message;
    private final String routeId;
    private final String vehicleId;
    private final double latitude;
    private final double longitude;
    private final int severity;
    private final LocalDateTime timestamp;

    // Constructor and getters...
}
```

Each alert captures the alert type (e.g., "DELAYED_VEHICLE"), a human-readable message, related route and vehicle IDs, geographic coordinates, a severity value, and the timestamp when the alert was created.

## Running the Service Monitor Example

Run the example:

```bash
mvn compile exec:java@service-monitor-example
```

Open the example:

```bash
open src/main/java/com/example/transit/examples/ServiceMonitorExample.java
```

The example connects to the cluster, verifies data exists, creates and starts the monitoring service, schedules periodic statistics output, and waits for user input to stop.

The core part:

```java
// Create and start the monitoring service
System.out.println("\n=== Starting monitoring service...");
MonitorService monitor = new MonitorService(connectionManager);

// Set quiet mode to true to suppress individual alert output
monitor.setQuietMode(true);

// Start monitoring (check every 60 seconds)
monitor.startMonitoring(60);

// Schedule a task to regularly print monitoring statistics
System.out.println("\n=== Setting up statistics reporting...");
scheduler.scheduleAtFixedRate(
        () -> reportingService.displayAlertStatistics(monitor.getAlertCounts()),
        30,  // Initial delay of 30 seconds
        30,  // Print stats every 30 seconds
        TimeUnit.SECONDS
);

// Let the monitor run and wait for user input to stop
System.out.println("\n--- Monitor is running. Press Enter to stop...");
System.in.read();
```

Expected output:

```text
=== Service Monitor Example ===
Connected to Ignite cluster: [ClientClusterNode [id=269b35be-01cb-4013-9333-add1ef38e05a, name=node3, address=127.0.0.1:10802, nodeMetadata=null]]

--- Verifying database data...
Verifying data in VehiclePosition table...
Table contains 2154 records

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

=== Starting monitoring service...
--- Starting service disruption monitoring (polling every 60 seconds)

=== Setting up statistics reporting...

--- Monitor is running. Press Enter to stop...
--- Found 206 delayed vehicles
--- Found 76 instances of vehicle bunching

===== SERVICE MONITORING ALERTS =====
Time: 2025-03-25 17:07:28

Alert counts by type:
• DELAYED_VEHICLE: 206 alerts
• VEHICLE_BUNCHING: 76 alerts
• LOW_ROUTE_COVERAGE: 0 alerts
• OFFLINE_VEHICLE: 0 alerts

Total alerts detected: 282
===========================================

[Press Enter to stop the monitor]

=== Stopping monitoring service...
+++ Service monitoring stopped

=== Monitoring Results ===
Total alerts detected: 282

Sample alerts:
• Vehicle 1000 on route 14R has been stopped for 89 minutes [17:07:28]
• Vehicle 1001 on route 14R has been stopped for 89 minutes [17:07:28]
• Vehicle 1006 on route F has been stopped for 89 minutes [17:07:28]
• Vehicle 1008 on route F has been stopped for 89 minutes [17:07:28]
• Vehicle 1010 on route F has been stopped for 89 minutes [17:07:28]

Example completed successfully!
```

{% hint style="success" %}
**Checkpoint:** You should see alert counts by type (delayed vehicles, vehicle bunching, etc.) and sample alerts with vehicle and route details. The specific counts depend on the current state of the ingested data.
{% endhint %}

## Other Monitoring Conditions

The `MonitorService` class implements several other monitoring conditions, each with a specialized SQL query:

### Vehicle Bunching

```java
private void checkForVehicleBunching() {
    // This query finds pairs of vehicles on the same route that are close to each other
    String querySql = "WITH latest_positions AS (" +
            "    SELECT v.vehicle_id, v.route_id, v.latitude, v.longitude " +
            "    FROM VehiclePosition v " +
            "    JOIN (" +
            "        SELECT vehicle_id, MAX(time_stamp) as latest_ts " +
            "        FROM VehiclePosition " +
            "        GROUP BY vehicle_id " +
            "    ) l ON v.vehicle_id = l.vehicle_id AND v.time_stamp = l.latest_ts " +
            "    WHERE v.current_status = 'IN_TRANSIT_TO' " +
            ") " +
            "SELECT " +
            "    a.vehicle_id as vehicle1, " +
            "    b.vehicle_id as vehicle2, " +
            "    a.route_id, " +
            "    a.latitude as lat1, " +
            "    a.longitude as lon1, " +
            "    b.latitude as lat2, " +
            "    b.longitude as lon2, " +
            "    SQRT(POWER(a.latitude - b.latitude, 2) + POWER(a.longitude - b.longitude, 2)) * 111 as distance_km " +
            "FROM latest_positions a " +
            "JOIN latest_positions b ON a.route_id = b.route_id AND a.vehicle_id < b.vehicle_id " +
            "WHERE SQRT(POWER(a.latitude - b.latitude, 2) + POWER(a.longitude - b.longitude, 2)) * 111 < ? " +
            "ORDER BY distance_km";

    // ... execution and alert creation ...
}
```

This query finds the latest position for each in-transit vehicle, self-joins to find pairs on the same route, calculates the distance between them in kilometers, and filters for pairs closer than the threshold distance.

### Low Route Coverage

```java
private void checkForLowRouteCoverage() {
    String querySql = "WITH active_vehicles AS (" +
            "    SELECT DISTINCT v.route_id, v.vehicle_id " +
            "    FROM VehiclePosition v " +
            "    JOIN (" +
            "        SELECT vehicle_id, MAX(time_stamp) as latest_ts " +
            "        FROM VehiclePosition " +
            "        GROUP BY vehicle_id " +
            "    ) l ON v.vehicle_id = l.vehicle_id AND v.time_stamp = l.latest_ts " +
            "    WHERE TIMESTAMPDIFF(MINUTE, v.time_stamp, CURRENT_TIMESTAMP) < 15" +
            ") " +
            "SELECT route_id, COUNT(*) as vehicle_count " +
            "FROM active_vehicles " +
            "GROUP BY route_id " +
            "HAVING COUNT(*) < ? " +
            "ORDER BY vehicle_count";

    // ... execution and alert creation ...
}
```

This query finds recent positions, groups by route, counts vehicles per route, and filters for routes below the minimum vehicle threshold.

### Offline Vehicles

```java
private void checkForOfflineVehicles() {
    String querySql = "WITH latest_timestamps AS (" +
            "    SELECT vehicle_id, MAX(time_stamp) as latest_ts " +
            "    FROM VehiclePosition " +
            "    GROUP BY vehicle_id " +
            "), active_routes AS (" +
            "    SELECT DISTINCT route_id " +
            "    FROM VehiclePosition v " +
            "    JOIN latest_timestamps l ON v.vehicle_id = l.vehicle_id AND v.time_stamp = l.latest_ts " +
            "    WHERE TIMESTAMPDIFF(MINUTE, v.time_stamp, CURRENT_TIMESTAMP) < 15" +
            ") " +
            "SELECT v.vehicle_id, v.route_id, v.latitude, v.longitude, v.time_stamp, " +
            "       TIMESTAMPDIFF(MINUTE, v.time_stamp, CURRENT_TIMESTAMP) as offline_minutes " +
            "FROM VehiclePosition v " +
            "JOIN latest_timestamps l ON v.vehicle_id = l.vehicle_id AND v.time_stamp = l.latest_ts " +
            "WHERE v.route_id IN (SELECT route_id FROM active_routes) " +
            "  AND TIMESTAMPDIFF(MINUTE, v.time_stamp, CURRENT_TIMESTAMP) >= ? " +
            "ORDER BY offline_minutes DESC";

    // ... execution and alert creation ...
}
```

This query identifies routes with some active vehicles, then finds vehicles on those routes that haven't reported in longer than the threshold. Checking only active routes avoids false positives for routes that are simply not running.

## Next Steps

This module implemented a monitoring system that continuously checks for service disruptions including delayed vehicles, vehicle bunching, low route coverage, and offline vehicles. The system tracks alert statistics and provides a foundation for operator notifications.

The monitoring system transforms the transit application from a passive data collection system into an active monitoring tool.
