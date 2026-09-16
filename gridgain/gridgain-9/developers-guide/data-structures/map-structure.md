---
description: >-
  Create and use distributed maps in GridGain 9 to store key-value pairs, with
  synchronous and asynchronous put, get, remove, and destroy operations.
---

# Distributed Maps

{% hint style="warning" %}
This is an experimental API. The API may change in subsequent releases without maintaining backwards compatibility.
{% endhint %}

In GridGain 9, you can create distributed maps to store key-value pairs, where each key maps to a specific value or object. These maps enable efficient access to values by their unique keys. You can interact with these distributed maps by using either the synchronous or asynchronous API. Below is an example of how to create and use them:

By default, maps are created and stored in the default [distribution zone](../../administrators-guide/storage/distribution-zones.md) and use the default [storage engine](../../administrators-guide/storage/storage-profiles.md) for your cluster.

{% hint style="info" %}
The examples on this page require the `gridgain-map-structure` module (the `org.gridgain.structure` API) in addition to the `ignite-client` module. For repository and dependency configuration, see [Project Setup and Required Modules](../project-setup.md).
{% endhint %}

## Creating Distributed Maps

To create a distributed map, use the `getOrCreateMap` method:

{% tabs %}
{% tab title="Sync" %}
```java
IgniteMap<Integer, String> mapFromNode2 = client2.structures().getOrCreateMap(MapConfiguration.builder("map1", Integer.class, String.class)
        .distributionZone("ZONENAME")
        .storageProfile("profileName")
        .build());
```
{% endtab %}

{% tab title="Async" %}
```java
CompletableFuture<IgniteMap<Integer, String>> mapFuture = client1.structures().getOrCreateMapAsync(
        MapConfiguration.builder("map1", Integer.class, String.class)
                .distributionZone("ZONENAME")
                .storageProfile("profileName")
                .build());
```
{% endtab %}
{% endtabs %}

### Configuring Map Storage

When maps are created, they use the default storage profile and distribution zone. You can configure the following properties:

| Configuration name | Description |
| --- | --- |
| distributionZone | The name of the [distribution zone](../../administrators-guide/storage/distribution-zones.md) to use. |
| storageProfile | The name of the [storage profile](../../administrators-guide/storage/storage-profiles.md) to use. The storage profile must be declared in the distribution zone. |

The example below demonstrates how you can set configuration via Java code:

{% tabs %}
{% tab title="Sync" %}
```java
IgniteMap<Integer, String> mapFromNode2 = client2.structures().getOrCreateMap(MapConfiguration.builder("map1", Integer.class, String.class)
        .distributionZone("ZONENAME")
        .storageProfile("profileName")
        .build());
```
{% endtab %}

{% tab title="Async" %}
```java
CompletableFuture<IgniteMap<Integer, String>> mapFuture = client1.structures().getOrCreateMapAsync(
        MapConfiguration.builder("map1", Integer.class, String.class)
                .distributionZone("ZONENAME")
                .storageProfile("profileName")
                .build());
```
{% endtab %}
{% endtabs %}

## Adding Data to Distributed Maps

Once the map is created, you can start putting data into it and retrieving data as needed.

### Put Operations

Use `put()` to insert or update a value without returning the previous value:

{% tabs %}
{% tab title="Sync" %}
```java
map.put(3, "val3");

String value = map.get(3);

System.out.println("Value: " + value);
```
{% endtab %}

{% tab title="Async" %}
```java
map.putAsync(4, "val4").thenCompose(ignored -> {
    return map.getAsync(4)
            .thenAccept(v -> System.out.println("Value after putAsync: " + v));
}).get(10, TimeUnit.SECONDS);
```
{% endtab %}
{% endtabs %}

The `put()` method returns `void` and does not retrieve the previous value, making it more efficient when you don't need the old value.

### Get-and-Put Operations

Use `getAndPut()` when you need to insert or update a value and retrieve the previous value:

{% tabs %}
{% tab title="Sync" %}
```java
ValueClass previousValue = mapWithCustomSerialization.getAndPut(key1, value1);
```
{% endtab %}

{% tab title="Async" %}
```java
mapFromNode1.getAndPutAsync(1, "val1").thenCompose(prev -> {
    if (prev != null) {
        throw new RuntimeException("Previous value should be null");
    }

    return mapFromNode1.getAsync(1)
            .thenAccept(newValue -> System.out.println("New value from node 1 after getAndPutAsync: " + newValue));
}).get(10, TimeUnit.SECONDS);
```
{% endtab %}
{% endtabs %}

The `getAndPut()` method returns the previous value associated with the key, or `null` if there was no mapping.

## Removing Data from Distributed Maps

GridGain provides several methods for removing data from distributed maps, each serving different use cases.

### Remove Operations

Use `remove()` to delete a mapping and check if the key existed:

{% code title="Sync" %}
```java
mapFromNode1.put(10, "value10");

// Check if key exists and remove it
boolean wasRemoved = mapFromNode1.remove(10);
System.out.println("Key 10 was removed: " + wasRemoved);

// Try to remove non-existent key
boolean notRemoved = mapFromNode1.remove(10);
System.out.println("Key 10 removed again: " + notRemoved); // false
```
{% endcode %}

The `remove()` method returns `true` if the key was present and removed, or `false` if the key did not exist.

### Get-and-Remove Operations

Use `getAndRemove()` when you need to delete a mapping and retrieve its value:

{% code title="Sync" %}
```java
mapFromNode1.put(11, "value11");

// Remove and get the previous value
String removedValue = mapFromNode1.getAndRemove(11);
System.out.println("Removed value: " + removedValue);

// Try to remove non-existent key
String notFound = mapFromNode1.getAndRemove(11);
System.out.println("Removed value (second attempt): " + notFound); // null
```
{% endcode %}

The `getAndRemove()` method returns the value that was associated with the key, or `null` if the key did not exist.

### Batch Remove Operations

Use `removeAll()` to efficiently remove multiple keys in a single operation:

{% tabs %}
{% tab title="Sync" %}
```java
// Add multiple entries
mapFromNode1.put(20, "value20");
mapFromNode1.put(21, "value21");
mapFromNode1.put(22, "value22");

// Remove multiple keys at once
mapFromNode1.removeAll(Set.of(20, 21, 22));
System.out.println("Multiple keys removed");
```
{% endtab %}

{% tab title="Async" %}
```java
// Add entries for async removal
mapFromNode1.put(30, "value30");
mapFromNode1.put(31, "value31");

// Remove multiple keys asynchronously
mapFromNode1.removeAllAsync(Set.of(30, 31, 999)) // 999 doesn't exist
        .thenRun(() -> System.out.println("Async batch removal completed"))
        .get(10, TimeUnit.SECONDS);
```
{% endtab %}
{% endtabs %}

The `removeAll()` method removes all mappings for the specified keys. It is more efficient than calling `remove()` multiple times, as it performs the operation in a single network round-trip.

## Destroying Maps

When a map is no longer needed, you can destroy it to remove all data and the map definition from the cluster.

### Destroying via Map Instance

Use the `destroy()` method on the map instance:

{% tabs %}
{% tab title="Sync" %}
```java
// Create a temporary map
IgniteMap<Integer, String> tempMap = client1.structures()
        .getOrCreateMap("temp_map", Integer.class, String.class);
tempMap.put(1, "temporary data");

// Destroy the map when no longer needed
tempMap.destroy();
System.out.println("Temporary map destroyed");
```
{% endtab %}

{% tab title="Async" %}
```java
// Create another temporary map
IgniteMap<Integer, String> tempMap2 = client1.structures()
        .getOrCreateMap("temp_map2", Integer.class, String.class);
tempMap2.put(1, "temporary data");

// Destroy the map asynchronously
tempMap2.destroyAsync()
        .thenRun(() -> System.out.println("Temporary map destroyed asynchronously"))
        .get(10, TimeUnit.SECONDS);
```
{% endtab %}
{% endtabs %}

### Destroying by Name

You can also destroy a map by name without having a map instance:

```java
// Create a map
client1.structures().getOrCreateMap("map_to_destroy", Integer.class, String.class);

// Destroy by name without map instance
client1.structures().destroyMap("map_to_destroy");
System.out.println("Map destroyed by name");
```

{% hint style="danger" %}
After a map is destroyed, it cannot be used anymore. All data is permanently deleted, and the map metadata is removed from the catalog. You must create a new map if you need to use it again.
{% endhint %}

## Type Safety

GridGain ensures type safety when working with distributed maps. If you attempt to open an existing map with incompatible key or value types, a `MapTypeMismatchException` will be thrown with a clear error message indicating the type mismatch.

```java
// First client creates map with Integer keys and String values
IgniteMap<Integer, String> map1 =
    structures.getOrCreateMap("shared_map", Integer.class, String.class);

// Second client attempts to open with incompatible types
// Throws MapTypeMismatchException
IgniteMap<String, Integer> map2 =
    structures.getOrCreateMap("shared_map", String.class, Integer.class);
```

The exception message will clearly indicate which type (key or value) does not match and show both the expected and actual types.

## Extended Example

The example below demonstrates how you can use data structures API to create a distributed map:

```java
public class DistributedMapExample {
    /**
     * This example demonstrates the usage of the IgniteStructures API.
     */

    public static void main(String[] args) throws Exception {

        try (IgniteClient client1 = IgniteClient.builder()
                .addresses("127.0.0.1:10800")
                .build();
                IgniteClient client2 = IgniteClient.builder()
                        .addresses("127.0.0.1:10801")
                        .build()) {

            //--------------------------------------------------------------------------------------
            //
            // Base put and get operations with distributed maps.
            //
            //--------------------------------------------------------------------------------------

        CompletableFuture<IgniteMap<Integer, String>> mapFuture = client1.structures().getOrCreateMapAsync(
                MapConfiguration.builder("map1", Integer.class, String.class)
                        .distributionZone("ZONENAME")
                        .storageProfile("profileName")
                        .build());

        IgniteMap<Integer, String> mapFromNode1 = mapFuture.get(10, TimeUnit.SECONDS);

        basicOperationsSync(mapFromNode1);

        basicOperationsAsync(mapFromNode1);

        mapFromNode1.getAndPutAsync(1, "val1").thenCompose(prev -> {
            if (prev != null) {
                throw new RuntimeException("Previous value should be null");
            }

            return mapFromNode1.getAsync(1)
                    .thenAccept(newValue -> System.out.println("New value from node 1 after getAndPutAsync: " + newValue));
        }).get(10, TimeUnit.SECONDS);

        IgniteMap<Integer, String> mapFromNode2 = client2.structures().getOrCreateMap(MapConfiguration.builder("map1", Integer.class, String.class)
                .distributionZone("ZONENAME")
                .storageProfile("profileName")
                .build());

        mapFromNode2.getAsync(1).thenAccept(v -> System.out.println("Before getAndPutAsync - node2 get: " + v)).get(10, TimeUnit.SECONDS);

        mapFromNode2.getAndPutAsync(1, "val2").thenCompose(prev -> {
            System.out.println("Result of getAndPutAsync(previous): " + prev);

            return mapFromNode2.getAsync(1).thenAccept(newValue ->
                    System.out.println("After getAndPutAsync - node2 get: " + newValue));
        }).get(10, TimeUnit.SECONDS);


        //--------------------------------------------------------------------------------------
        //
        // Base put and get operations with custom key/value classes based map.
        //
        //--------------------------------------------------------------------------------------
        CompletableFuture<IgniteMap<KeyClass, ValueClass>> mapFuture2 = client1.structures()
                .getOrCreateMapAsync("map2", new KeySerializer(), new ValueSerializer());

        IgniteMap<KeyClass, ValueClass> mapWithCustomSerialization = mapFuture2.get(10, TimeUnit.SECONDS);

        KeyClass key1 = new KeyClass("keyStr1", 1);
        ValueClass value1 = new ValueClass(List.of("valStr1"));

        ValueClass previousValue = mapWithCustomSerialization.getAndPut(key1, value1);

        if (previousValue != null) {
            throw new RuntimeException("Previous value should be null");
        }

        ValueClass valueFromGet = mapWithCustomSerialization.get(key1);
        if (!Objects.equals(valueFromGet, value1)) {
            throw new RuntimeException("Values should be equal");
        }

        System.out.println("New value after getAndPut: " + valueFromGet);

        //--------------------------------------------------------------------------------------
        //
        // Demonstrate remove operations
        //
        //--------------------------------------------------------------------------------------

        mapFromNode1.put(10, "value10");

        // Check if key exists and remove it
        boolean wasRemoved = mapFromNode1.remove(10);
        System.out.println("Key 10 was removed: " + wasRemoved);

        // Try to remove non-existent key
        boolean notRemoved = mapFromNode1.remove(10);
        System.out.println("Key 10 removed again: " + notRemoved); // false

        mapFromNode1.put(11, "value11");

        // Remove and get the previous value
        String removedValue = mapFromNode1.getAndRemove(11);
        System.out.println("Removed value: " + removedValue);

        // Try to remove non-existent key
        String notFound = mapFromNode1.getAndRemove(11);
        System.out.println("Removed value (second attempt): " + notFound); // null

        // Add multiple entries
        mapFromNode1.put(20, "value20");
        mapFromNode1.put(21, "value21");
        mapFromNode1.put(22, "value22");

        // Remove multiple keys at once
        mapFromNode1.removeAll(Set.of(20, 21, 22));
        System.out.println("Multiple keys removed");

        // Add entries for async removal
        mapFromNode1.put(30, "value30");
        mapFromNode1.put(31, "value31");

        // Remove multiple keys asynchronously
        mapFromNode1.removeAllAsync(Set.of(30, 31, 999)) // 999 doesn't exist
                .thenRun(() -> System.out.println("Async batch removal completed"))
                .get(10, TimeUnit.SECONDS);

        //--------------------------------------------------------------------------------------
        //
        // Demonstrate map destruction
        //
        //--------------------------------------------------------------------------------------

        // Create a temporary map
        IgniteMap<Integer, String> tempMap = client1.structures()
                .getOrCreateMap("temp_map", Integer.class, String.class);
        tempMap.put(1, "temporary data");

        // Destroy the map when no longer needed
        tempMap.destroy();
        System.out.println("Temporary map destroyed");

        // Create another temporary map
        IgniteMap<Integer, String> tempMap2 = client1.structures()
                .getOrCreateMap("temp_map2", Integer.class, String.class);
        tempMap2.put(1, "temporary data");

        // Destroy the map asynchronously
        tempMap2.destroyAsync()
                .thenRun(() -> System.out.println("Temporary map destroyed asynchronously"))
                .get(10, TimeUnit.SECONDS);

        // Create a map
        client1.structures().getOrCreateMap("map_to_destroy", Integer.class, String.class);

        // Destroy by name without map instance
        client1.structures().destroyMap("map_to_destroy");
        System.out.println("Map destroyed by name");
    }
    }


    private static void basicOperationsSync(IgniteMap<Integer, String> map) {
        map.put(3, "val3");

        String value = map.get(3);

        System.out.println("Value: " + value);
    }

    private static void basicOperationsAsync(IgniteMap<Integer, String> map) throws ExecutionException, InterruptedException, TimeoutException {
        map.putAsync(4, "val4").thenCompose(ignored -> {
            return map.getAsync(4)
                    .thenAccept(v -> System.out.println("Value after putAsync: " + v));
        }).get(10, TimeUnit.SECONDS);
    }

    //--------------------------------------------------------------------------------------
    //
    // Key class used to create map2 example.
    //
    //--------------------------------------------------------------------------------------
    private static class KeyClass {
        private final String str;

        private final Integer integer;

        public KeyClass(String s, Integer i) {
            this.str = s;
            this.integer = i;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (!(o instanceof KeyClass)) {
                return false;
            }
            KeyClass keyClass = (KeyClass) o;
            return Objects.equals(str, keyClass.str) && Objects.equals(integer, keyClass.integer);
        }

        @Override
        public int hashCode() {
            return Objects.hash(str, integer);
        }

        @Override
        public String toString() {
            return "KeyClass{" +
                    "str='" + str + '\'' +
                    ", integer=" + integer +
                    '}';
        }
    }

    //--------------------------------------------------------------------------------------
    //
    // Value serializer for the KeyClass.
    //
    //--------------------------------------------------------------------------------------
    private static class KeySerializer implements ByteArrayMarshaller<KeyClass> {
        @Override
        public byte [] marshal(KeyClass object) {
            if (object == null) {
                return null;
            }

            String result = object.integer + ":" + Base64.getEncoder().encodeToString(object.str.getBytes(UTF_8));

            return result.getBytes(UTF_8);
        }

        @Override
        public  KeyClass unmarshal(byte  [] raw) {
            if (raw == null) {
                return null;
            }

            String rawStr = new String(raw, UTF_8);
            int index = rawStr.indexOf(':');

            return new KeyClass(
                    new String(Base64.getDecoder().decode(rawStr.substring(index + 1)), UTF_8),
                    Integer.parseInt(rawStr.substring(0, index))
            );
        }
    }

    //--------------------------------------------------------------------------------------
    //
    // Value class used to create map2 example.
    //
    //--------------------------------------------------------------------------------------
    private static class ValueClass {
        private final List<String> list;

        public ValueClass(List<String> v) {
            this.list = v;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (!(o instanceof ValueClass)) {
                return false;
            }
            ValueClass that = (ValueClass) o;
            return Objects.equals(list, that.list);
        }

        @Override
        public int hashCode() {
            return Objects.hashCode(list);
        }

        @Override
        public String toString() {
            return "ValueClass{" +
                    "list=" + list +
                    '}';
        }
    }

    //--------------------------------------------------------------------------------------
    //
    // Value serializer for the ValueClass.
    //
    //--------------------------------------------------------------------------------------
    private static class ValueSerializer implements ByteArrayMarshaller<ValueClass> {
        @Override
        public byte  [] marshal( ValueClass object) {
            if (object == null) {
                return null;
            }

            String result = object.list.stream().map(it -> Base64.getEncoder().encodeToString(it.getBytes(UTF_8)))
                    .collect(Collectors.joining(":"));

            return result.getBytes(UTF_8);
        }


        @Override
        public  ValueClass unmarshal(byte  [] raw) {
            if (raw == null) {
                return null;
            }

            String[] split = new String(raw, UTF_8).split(":");

            return new ValueClass(Arrays.stream(split)
                    .map(it -> new String(Base64.getDecoder().decode(it), UTF_8))
                    .collect(Collectors.toUnmodifiableList())
            );

        }
    }
}
```
