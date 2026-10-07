---
description: >-
  Query and index geometry data types such as points, lines, and polygons in
  GridGain 8 using spatial SQL, the ignite-geospatial library, and the GEOMETRY
  type.
---

# Geospatial SQL Capabilities

In addition to the standard ANSI-99 SQL queries that are executed over primitive data types, or objects of custom types, GridGain also allows querying and indexing geometry data types such as points, lines, and polygons, while considering the spatial relationship between these geometries.

Spatial query capabilities, as well as available functions and operands, are defined by the [Simple Features Specification for SQL](http://www.opengeospatial.org/docs/is/). Currently, GridGain supports the intersection operation (`&&`) using the [JTS Topology Suite](http://tsusiatsoftware.net/jts/main.html).

## Including Geospatial Library

The Geospatial library (`ignite-geospatial`) depends on [JTS](http://tsusiatsoftware.net/jts/main.html), which is available under the LGPL license. The latter is not aligned with the Apache license, which prevents inclusion of `ignite-geospatial` in the GridGain binary deliveries. This is why a binary version of the `ignite-geospatial` library is hosted in a separate Maven repository:

```xml
<repositories>
    <repository>
    <id>GridGain External Repository</id>
    <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>
```

Add this repository and the Maven dependency below to your `pom.xml` file to include the `geospatial` library in your application:

```xml
<dependency>
    <groupId>org.gridgain</groupId>
  <artifactId>ignite-geospatial</artifactId>
  <version>${gridgain.version}</version>
</dependency>
```

## GEOMETRY

`GEOMETRY` is a spatial geometry type, based on the `com.vividsolutions.jts` library. It is usually represented in a textual format using WKT (well-known text).

`GEOMETRY` maps to:

- Java/JDBC: data types from the `com.vividsolutions.jts` package
- .NET/C#: N/A
- C/C++: N/A
- ODBC: N/A

```java
import org.locationtech.jts.io.WKTReader;
import org.locationtech.jts.geom.GeometryFactory;

new WKTReader().read("POINT(x y)");
new GeometryFactory().createPoint(new Coordinate(x, y))
```

## Geospatial Queries

The `geospatial module` can be used only for the objects of the `com.vividsolutions.jts` type.

To configure indexes and/or queryable fields of geometric types, use the same approach you do for non-geospatial types. You can define indexes:

- With the use of `org.apache.ignite.cache.QueryEntity`, which is convenient for Spring XML-based configurations
- By annotating indexes with `@QuerySqlField`, which will be converted to `QueryEntities` internally

### QuerySqlField

```java
/**
 * Map point with indexed coordinates.
 */
private static class MapPoint {
    /** Coordinates. */
    @QuerySqlField(index = true)
    private Geometry coords;

    /**
     * @param coords Coordinates.
     */
    private MapPoint(Geometry coords) {
        this.coords = coords;
    }
}

CacheConfiguration<K, V> ccfg = new CacheConfiguration<K, V>(name)
    .setIndexedTypes(Integer.class, MapPoint.class);
```

### QueryEntity XML

```xml
<bean class="org.apache.ignite.configuration.CacheConfiguration">
    <property name="name" value="mycache"/>
    <!-- Configure query entities. -->
    <property name="queryEntities">
        <list>
            <bean class="org.apache.ignite.cache.QueryEntity">
                <property name="keyType" value="java.lang.Integer"/>
                <property name="valueType" value="org.apache.ignite.examples.MapPoint"/>

                <property name="fields">
                    <map>
                        <entry key="coords" value="com.vividsolutions.jts.geom.Geometry"/>
                    </map>
                </property>

                <property name="indexes">
                    <list>
                        <bean class="org.apache.ignite.cache.QueryIndex">
                            <constructor-arg value="coords"/>
                        </bean>
                    </list>
                </property>
            </bean>
        </list>
    </property>
</bean>
```

### QueryEntity Java

```java
// Create a cache configuration with the indexed types.
CacheConfiguration<Integer,MapPoint> ccfg;
ccfg.setIndexedTypes(keyCls, valCls);
Collection<QueryEntity> entities = ccfg.getQueryEntities();
QueryEntity entity = entities.iterator().next();
Collection<QueryIndex> idxs = entity.getIndexes();
// idxs: [QueryIndex [name=EnemyCamp_coords_idx, fields=LinkedHashMap {coords=true}, type=GEOSPATIAL, inlineSize=-1]]
```

### SQL

```java
// Create a table with the GEOMETRY column type.
qry = new SqlFieldsQuery("CREATE TABLE PUBLIC.AFF_CACHE (ID1 INT, ID2 INT, GEOM GEOMETRY, PRIMARY KEY (ID1))");

// Create a custom spatial index.
qry = new SqlFieldsQuery("CREATE SPATIAL INDEX IDX_GEO_1 ON PUBLIC.AFF_CACHE(GEOM)");

// Create a custom spatial index for a complex type.
// 'Coords' refers to the GEOMETRY field name.
qry = new SqlFieldsQuery("CREATE SPATIAL INDEX \"MapPoint_coords_idx\" ON MAPPOINT (\"coords\" ASC)");

cache.query(qry).getAll();
```

## Examples

After the GEOMETRY-type fields are defined using one of the above methods, you can execute queries using values stored in these fields.

### Example 1

```java
// Find points that fit into a polygon.
SqlQuery<Integer, MapPoint> query = new SqlQuery<>(MapPoint.class, "coords && ?");

// Define the polygon's boundaries.
query.setArgs("POLYGON((0 0, 0 99, 400 500, 300 0, 0 0))");

// Execute the query.
Collection<Cache.Entry<Integer, MapPoint>> entries = cache.query(query).getAll();

// Print the number of points that fit into the area defined by the polygon.
System.out.println("Fetched points [" + entries.size() + ']');
```

### Example 2

```java
// 'coords' refer to the Geometry field name.

WKTReader r = new WKTReader();
cache.getAndPut(0, new MapPoint(r.read("POINT(25 75)")));
cache.getAndPut(1, new MapPoint(r.read("POINT(70 70)")));

// Check if a cache value is within a polygon.
qry = new SqlQuery(MapPoint.class, "coords && ?")
  .setArgs(r.read("POLYGON((5 70, 5 80, 30 80, 30 70, 5 70))"));

// Explain the query.
qry = new SqlFieldsQuery("explain select * from MapPoint where coords && 'POINT(25 75)'");

// Cache-execute the query.
cache.query(qry).getAll();
```

## A Complete Example

A ready-to-run example of geospatial query usage can be found [here](https://github.com/gridgain/gridgain/tree/master/modules/geospatial) or [here](https://github.com/dmagda/geospatial).
