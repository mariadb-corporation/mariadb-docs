---
description: >-
  SPATIAL indexes in TideSQL built on a Hilbert-curve encoding, the supported
  MBR predicates, and how Hilbert range decomposition avoids full scans.
---

# TideSQL Spatial Indexes

TideSQL supports `SPATIAL` indexes for geographic and geometric data using a Hilbert-curve encoding on the LSM-tree. Rather than an R-tree, which needs in-place node updates that clash with append-only LSM semantics, each geometry's MBR center is mapped to a 64-bit Hilbert value and stored as a sorted key in a dedicated column family.

```sql
CREATE TABLE places (
  id INT NOT NULL PRIMARY KEY, name VARCHAR(100),
  location GEOMETRY NOT NULL, SPATIAL INDEX (location)
) ENGINE=TIDESDB;

INSERT INTO places VALUES (1, 'NYC', ST_GeomFromText('POINT(40.7128 -74.0060)'));
```

## Queries

MBR-based predicates work through the standard MariaDB spatial functions:

```sql
SELECT name FROM places
WHERE MBRIntersects(location, ST_GeomFromText('POLYGON((39 -76, 43 -76, 43 -72, 39 -72, 39 -76))'));

SELECT name FROM places
WHERE MBRWithin(location, ST_GeomFromText('POLYGON((25 -125, 45 -125, 45 -70, 25 -70, 25 -125))'));
```

The supported predicates are `MBRIntersects`, `MBRContains`, `MBRWithin`, `MBREquals`, and `MBRDisjoint`, and all geometry types are supported, POINT, LINESTRING, POLYGON, MULTIPOINT, MULTILINESTRING, MULTIPOLYGON, and GEOMETRYCOLLECTION.

## How It Works

Each geometry is a single index entry. The key is the 64-bit Hilbert value of the MBR center, big-endian for lexicographic ordering, followed by the primary-key suffix, and the value stores the full MBR (four doubles) for predicate evaluation during a scan. The Hilbert curve gives good spatial locality, geographically close geometries tend to have numerically adjacent values, so they cluster in the LSM-tree and read sequentially.

A spatial query uses Hilbert range decomposition instead of scanning the whole index. The query bounding box is mapped to a coarse 256 by 256 grid on the curve, only the cells overlapping the box are kept, those cells are merged into contiguous Hilbert ranges, and the engine seeks directly to each range. Each candidate then passes exact MBR filtering to drop false positives from the curve approximation. A box that covers more than 4096 grid cells skips the decomposition and scans the whole curve as one range, since the MBR filter drops the extra rows anyway.

Because an entry is keyed by its MBR center, a line or polygon that crosses the query box can be centered well outside it. `MBRWithin` and `MBREquals` need only the cells of the box, since a matching geometry is centered inside it. For `MBRIntersects`, `ST_Intersects`, and `MBRContains(col, const)` the engine widens the scanned area by the largest half-extent the index has held, so these predicates return exact results through the index for every geometry type, not only points. After a server restart that extent is not yet known, so these predicates scan the whole index until one such scan reads it to the end and learns it. The one predicate this cannot accelerate is `MBRDisjoint`, because a non-overlapping geometry can lie anywhere on the curve, so a disjoint query scans the full index and filters.

INSERT, UPDATE, and DELETE maintain the spatial index transactionally alongside the row, the same as secondary and full-text indexes. An UPDATE that changes the primary key re-keys the row's spatial entry, and an UPDATE on a table with a `TTL` option or `TTL` column, in a session with a non-zero `tidesdb_ttl`, or of a row that already carries an expiry from an earlier session TTL, rewrites the entry so it carries the row's new expiry, or none when the update leaves the row without one.

<sub>_This page is licensed: GPLv2_</sub>
