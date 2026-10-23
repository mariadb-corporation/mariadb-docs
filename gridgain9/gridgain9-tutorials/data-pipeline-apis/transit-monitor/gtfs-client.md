---
hidden: true
description: >-
  Build a client to fetch and parse real-time transit data from GTFS feeds
---

# Building and Testing the GTFS Client

This module implements a client that communicates with GTFS-realtime feeds to fetch transit vehicle positions, forming the data acquisition layer of the application.

## Obtaining an API Token

To access real transit data, you need an API token from a transit data provider. This tutorial uses the San Francisco Bay Area's 511.org API, which provides GTFS-realtime data for multiple transit agencies.

1. Visit [https://511.org/open-data/token](https://511.org/open-data/token)
2. Complete the registration form with your details
3. Submit the form
4. Save the API token that arrives by email

{% hint style="info" %}
The process of obtaining an API token is similar for most transit data providers. If you want to use data from a different agency, check their developer portal for access instructions.
{% endhint %}

## Configuring Environment Variables

To securely manage API tokens without hardcoding them in source code, the application loads environment variables from a `.env` file.

Create a file named `.env` in the root of the project with the following content, replacing `your_token_here` with your actual API token:

```properties
# 511.org API token - get yours at https://511.org/open-data/token
API_TOKEN=your_token_here

# GTFS Feed URL
GTFS_BASE_URL=https://api.511.org/transit/vehiclepositions

# GTFS Agency - default is San Francisco Muni
GTFS_AGENCY=SF
```

{% hint style="warning" %}
Never commit the `.env` file to version control. Add it to `.gitignore` to prevent accidentally exposing API credentials.
{% endhint %}

## Understanding the Client's Role

The GTFS client is responsible for:

1. **External Data Acquisition**: Connecting to a GTFS-realtime feed provided by a transit agency
2. **Protocol Buffer Processing**: Parsing the binary format used by GTFS-realtime
3. **Data Transformation**: Converting external data structures into the domain model
4. **Error Handling**: Dealing with network issues, data format changes, and other potential problems

## Configuration Service

Open the `ConfigService.java` file to see how the application loads configuration from the `.env` file:

```bash
open src/main/java/com/example/transit/config/ConfigService.java
```

The `ConfigService` uses the `dotenv-java` library to load environment variables:

```java
// Load environment variables from .env file
Dotenv dotenv = Dotenv.configure().ignoreIfMissing().load();

// Get required config values
this.apiToken = dotenv.get(API_TOKEN_KEY);
this.baseUrl = dotenv.get(BASE_URL_KEY);
this.agency = dotenv.get(AGENCY_KEY);

// Pre-build the feed URL
if (isValid()) {
    this.feedUrl = String.format("%s?api_key=%s&agency=%s", baseUrl, apiToken, agency);
} else {
    this.feedUrl = null;
}
```

This code loads environment variables from the `.env` file, retrieves the API token, base URL, and agency values, constructs the complete feed URL with query parameters, and provides methods to access these values throughout the application.

## Implementing the GTFS Client

The GTFS client is implemented in the `GtfsService` class. Open it:

```bash
open src/main/java/com/example/transit/service/GtfsService.java
```

The core of the implementation is the `getVehiclePositions()` method:

```java
public List<VehiclePosition> getVehiclePositions() throws IOException {
    List<VehiclePosition> positions = new ArrayList<>();

    try {
        // Parse feed from URL
        URL url = new URL(feedUrl);
        FeedMessage feed = FeedMessage.parseFrom(url.openStream());

        // Process each entity in the feed
        for (FeedEntity entity : feed.getEntityList()) {
            if (entity.hasVehicle()) {
                com.google.transit.realtime.GtfsRealtime.VehiclePosition vehicle = entity.getVehicle();

                if (vehicle.hasPosition() && vehicle.hasVehicle() && vehicle.hasTrip()) {
                    Position position = vehicle.getPosition();
                    String vehicleId = vehicle.getVehicle().getId();
                    String routeId = vehicle.getTrip().getRouteId();
                    String status = mapVehicleStatus(vehicle);

                    // Get timestamp (convert seconds to milliseconds or use current time)
                    long timestamp = vehicle.hasTimestamp() ? vehicle.getTimestamp() * 1000
                            : System.currentTimeMillis();

                    // Convert to LocalDateTime for Ignite storage
                    LocalDateTime localDateTime = LocalDateTime.ofInstant(
                            Instant.ofEpochMilli(timestamp),
                            ZoneId.systemDefault());

                    // Create VehiclePosition object
                    VehiclePosition vehiclePosition = new VehiclePosition(
                            vehicleId,
                            localDateTime,
                            routeId,
                            position.getLatitude(),
                            position.getLongitude(),
                            status
                    );

                    positions.add(vehiclePosition);
                }
            }
        }
    } catch (IOException e) {
        System.err.println("Error fetching GTFS feed: " + e.getMessage());
        throw e;
    } catch (Exception e) {
        System.err.println("Error parsing GTFS feed: " + e.getMessage());
        throw new IOException("Failed to process GTFS feed", e);
    }

    return positions;
}
```

This method opens a connection to the GTFS feed URL, uses `FeedMessage.parseFrom()` to parse the binary Protocol Buffer data, iterates through each entity in the feed, extracts relevant fields (vehicle ID, route ID, position, timestamp, status), converts timestamps to `LocalDateTime` for Ignite compatibility, and creates `VehiclePosition` objects matching the database schema.

The `mapVehicleStatus()` method converts GTFS enum values to readable strings:

```java
private String mapVehicleStatus(com.google.transit.realtime.GtfsRealtime.VehiclePosition vehicle) {
    if (!vehicle.hasCurrentStatus()) {
        return "UNKNOWN";
    }

    switch (vehicle.getCurrentStatus()) {
        case IN_TRANSIT_TO:
            return "IN_TRANSIT_TO";
        case STOPPED_AT:
            return "STOPPED_AT";
        case INCOMING_AT:
            return "INCOMING_AT";
        default:
            return "UNKNOWN";
    }
}
```

## Testing the GTFS Client

Run the GTFS feed example to test the client:

```bash
mvn compile exec:java@gtfs-feed-example
```

This runs the `GtfsFeedExample` class. Open it:

```bash
open src/main/java/com/example/transit/examples/GtfsFeedExample.java
```

The example loads configuration, connects to the Ignite cluster, sets up the schema, creates the GTFS feed service, fetches vehicle positions, displays sample data, and analyzes statistics.

The core part:

```java
// Create the feed service
GtfsService feedService = new GtfsService(config.getFeedUrl());

try {
    // Fetch vehicle positions
    System.out.println("=== Fetching vehicle positions...");
    List<VehiclePosition> positions = feedService.getVehiclePositions();

    System.out.println(">>> Fetched " + positions.size() + " vehicle positions from feed");

    if (positions.isEmpty()) {
        System.out.println("Warning: No vehicle positions found in the feed.");
        System.out.println("This could indicate an issue with the feed URL, API token, or the agency may not have active vehicles at this time.");
        return;
    }

    // Print sample data (first 5 vehicles)
    System.out.println("\nSample data (first 5 vehicles):");
    positions.stream()
            .limit(5)
            .forEach(pos -> System.out.println(reportingService.formatVehicleData(pos)));

    // Analyze the data
    reportingService.analyzeVehicleData(positions);
}
```

Expected output:

```text
=== GTFS Feed Example ===
+++ Using GTFS feed URL: https://api.511.org/transit/vehiclepositions?api_key=[API_TOKEN]&agency=SF
Connected to Ignite cluster: [ClientClusterNode [id=269b35be-01cb-4013-9333-add1ef38e05a, name=node3, address=127.0.0.1:10802, nodeMetadata=null]]
--- Vehicle positions table already exists
=== Fetching vehicle positions...
>>> Fetched 536 vehicle positions from feed
=== Success!

Sample data (first 5 vehicles):
+++ Vehicle 1006 on route F at (37.798801, -122.397285) - Status: IN_TRANSIT_TO
+++ Vehicle 1010 on route F at (37.758701, -122.427879) - Status: IN_TRANSIT_TO
+++ Vehicle 1051 on route F at (37.793968, -122.395416) - Status: IN_TRANSIT_TO
+++ Vehicle 1056 on route F at (37.781357, -122.411392) - Status: INCOMING_AT
+++ Vehicle 1057 on route F at (37.808189, -122.416672) - Status: IN_TRANSIT_TO

=== Transit System Statistics ===
• Unique routes: 56
• Unique vehicles: 536

Vehicle status distribution:
• IN_TRANSIT_TO: 204 vehicles (38.1%)
• STOPPED_AT: 220 vehicles (41.0%)
• INCOMING_AT: 112 vehicles (20.9%)

Top 5 routes by vehicle count:
• Route 49: 22 vehicles
• Route 14R: 22 vehicles
• Route 29: 22 vehicles
• Route 1: 20 vehicles
• Route 22: 19 vehicles

Geographic coverage:
• Latitude range: 37.705257415771484 to 37.81974411010742
• Longitude range: -122.50987243652344 to -122.36726379394531
Ignite client connection closed
=== GTFS Feed Example Completed
```

{% hint style="success" %}
**Checkpoint:** You should see fetched vehicle positions with sample data and statistics. If you see "No vehicle positions found," verify the API token in the `.env` file and that the transit agency has active vehicles at this time.
{% endhint %}

The actual output varies depending on the current state of the transit system.

## Analyzing the Data

The `ReportingService` class implements data analysis. Open it:

```bash
open src/main/java/com/example/transit/service/ReportingService.java
```

The `analyzeVehicleData()` method provides statistics about the transit system:

```java
public void analyzeVehicleData(List<VehiclePosition> positions) {
    // Count unique routes and vehicles
    long uniqueRoutes = positions.stream()
            .map(VehiclePosition::getRouteId)
            .distinct()
            .count();

    long uniqueVehicles = positions.stream()
            .map(VehiclePosition::getVehicleId)
            .distinct()
            .count();

    // Count vehicles by status
    Map<String, Long> statusCounts = positions.stream()
            .collect(java.util.stream.Collectors.groupingBy(
                    VehiclePosition::getCurrentStatus,
                    java.util.stream.Collectors.counting()));

    // Find top 5 routes by vehicle count
    Map<String, Long> routeCounts = positions.stream()
            .collect(java.util.stream.Collectors.groupingBy(
                    VehiclePosition::getRouteId,
                    java.util.stream.Collectors.counting()));

    List<Map.Entry<String, Long>> topRoutes = routeCounts.entrySet().stream()
            .sorted(Map.Entry.<String, Long>comparingByValue().reversed())
            .limit(5)
            .collect(java.util.stream.Collectors.toList());

    // Display statistics
    System.out.println("\n=== Transit System Statistics ===");
    System.out.println("• Unique routes: " + uniqueRoutes);
    System.out.println("• Unique vehicles: " + uniqueVehicles);

    // Display more statistics...
}
```

## Next Steps

This module built and tested a GTFS client that forms the data acquisition layer of the transit monitoring system. The client handles connecting to external data sources, parsing protocol buffer formats, and transforming the data into the domain model.

The next module implements a data ingestion service that uses this client to regularly fetch transit data and store it in the Ignite database.
