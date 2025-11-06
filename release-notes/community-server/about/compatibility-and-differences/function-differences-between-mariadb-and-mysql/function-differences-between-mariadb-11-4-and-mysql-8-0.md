# Function Differences Between MariaDB 11.4 and MySQL 8.0

The following is a list of all function differences between [MariaDB 11.4](../../../11.4/what-is-mariadb-114.md) and MySQL 8.0. It is based on functions available in the MySQL 8.0.36 and the [MariaDB 11.4.1](../../../11.4/11.4.1.md) releases. For a more complete list of differences, see [Incompatibilities and Feature Differences Between MariaDB 11.4 and MySQL 8.0](../incompatibilities-and-feature-differences-between-mariadb-11-4-and-mysql-8.md)

## Present in MariaDB Only

### Dynamic Columns

* [COLUMN\_ADD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_add)
* [COLUMN\_CHECK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_check)
* [COLUMN\_CREATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_create)
* [COLUMN\_DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_delete)
* [COLUMN\_EXISTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_exists)
* [COLUMN\_GET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_get)
* [COLUMN\_JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_json)
* [COLUMN\_LIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_list)

### Galera

* [WSREP\_LAST\_SEEN\_GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/galera-functions/wsrep_last_seen_gtid)
* [WSREP\_LAST\_WRITTEN\_GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/galera-functions/wsrep_last_written_gtid)
* [WSREP\_SYNC\_WAIT\_UPTO\_GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/galera-functions/wsrep_sync_wait_upto_gtid)

### General

* [ADD\_MONTHS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/add_months)
* [CHR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/chr)
* [DECODE\_ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/decode)
* [DES\_DECRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_decrypt)
* [DES\_ENCRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_encrypt)
* [KDF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/kdf)
* [LENGTHB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/lengthb)
* [NATURAL\_SORT\_KEY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/natural_sort_key)
* [NVL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/control-flow-functions/ifnull) (Synonym for IFNULL)
* [NVL2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/control-flow-functions/nvl2)
* [SFORMAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/sformat)
* [SYS\_GUID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/sys_guid)
* [TO\_CHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/to_char)
* [TRIM\_ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/trim)
* [VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/values-value) - the VALUES() function was renamed after MariaDB introduced Table Value Constructors.

### Geographic

MySQL has removed the following functions in MySQL 8.0.

* [AREA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/polygon-properties/st_area)
* [AsBinary](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/st_asbinary)
* [AsText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/st_astext)
* [AsWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/aswkb)
* [AsWKT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/st_aswkt)
* [Buffer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-constructors/buffer)
* [Centroid](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/polygon-properties/centroid)
* [Contains](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/contains)
* [ConvexHull](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-constructors/convexhull)
* [Crosses](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/crosses)
* [Dimension](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-properties/dimension)
* [Disjoint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/disjoint)
* [EndPoint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/linestring-properties/st_endpoint)
* [Envelope](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-properties/st_envelope)
* [Equals](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/equals)
* [ExteriorRing](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/polygon-properties/st_exteriorring)
* [GeomCollFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/st_geomcollfromtext)
* [GeomCollFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/st_geomcollfromwkb)
* [GeomFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/st_geomfromtext)
* [GeomFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/st_geomfromwkb)
* [GeometryCollectionFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/geometrycollectionfromtext)
* [GeometryCollectionFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/geometrycollectionfromwkb)
* [GeometryFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/geometryfromtext)
* [GeometryFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/geometryfromwkb)
* [GeometryN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-properties/st_geometryn)
* [GeometryType](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-properties/st_geometrytype)
* [GLENGTH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/linestring-properties/glength)
* [InteriorRingN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/polygon-properties/st_interiorringn)
* [Intersects](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/intersects)
* [IsClosed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-properties/isclosed)
* [IsEmpty](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-properties/st_isempty)
* [IsSimple](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-properties/st_issimple)
* [LineFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/st_linefromtext)
* [LineFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/st_linefromwkb)
* [LineStringFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/linestringfromtext)
* [LineStringFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/linestringfromwkb)
* [MLineFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/mlinefromtext)
* [MLineFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/mlinefromwkb)
* [MPointFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/mpointfromtext)
* [MPointFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/mpointfromwkb)
* [MPolyFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/mpolyfromtext)
* [MPolyFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/mpolyfromwkb)
* [MultiLineStringFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/multilinestringfromtext)
* [MultiLineStringFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/multilinestringfromwkb)
* [MultiPointFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/multipointfromtext)\* GeomCollection
* ST\_GeomCollFromTxt
* ST\_NumInteriorRing
* [MultiPointFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/multipointfromwkb)
* [MultiPolygonFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/multipolygonfromtext)
* [MultiPolygonFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/multipolygonfromwkb)
* [NumGeometries](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-properties/st_numgeometries)
* [NumInteriorRings](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/polygon-properties/st_numinteriorrings)
* [NumPoints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/linestring-properties/st_numpoints)
* [Overlaps](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/overlaps)
* [PointFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/st_pointfromtext)
* [PointFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/st_pointfromwkb)
* [PointN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/linestring-properties/st_pointn)
* [PolyFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/st_polyfromtext)
* [PolyFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/st_polyfromwkb)
* [PolygonFromText](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkt/polygonfromtext)
* [PolygonFromWKB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/wkb/polygonfromwkb)
* [SRID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-properties/st_srid)
* [StartPoint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/linestring-properties/st_startpoint)
* [Touches](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/touches)
* [Within](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/within)
* [X](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/point-properties/st_x)
* [Y](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/point-properties/st_y)

### JSON

* [JSON\_ARRAY\_INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_array_intersect)
* [JSON\_COMPACT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_compact)
* [JSON\_DETAILED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_detailed)
* [JSON\_EQUALS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals)
* [JSON\_EXISTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_exists)
* [JSON\_KEY\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_key_value)
* [JSON\_LOOSE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_loose)
* [JSON\_NORMALIZE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize)
* [JSON\_OBJECT\_FILTER\_KEYS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_filter_keys)
* [JSON\_OBJECT\_TO\_ARRAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_to_array)
* [JSON\_QUERY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_query)

### Sequences

* [LASTVAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/previous-value-for-sequence_name)
* [NEXTVAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/next-value-for-sequence_name)
* [SETVAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/setval)

### Window Functions

* [MEDIAN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/median)
* [PERCENTILE\_CONT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percentile_cont)
* [PERCENTILE\_DISC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percentile_disc)

## Present in MySQL Only

### GTID

MariaDB and MySQL have differing [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) implementations.

* GTID\_SUBSET
* GTID\_SUBTRACT
* WAIT\_FOR\_EXECUTED\_GTID\_SET
* WAIT\_UNTIL\_SQL\_THREAD\_AFTER\_GTIDS

### Geographic

* GeomCollection
* MBRCoveredBy
* MBRCovers
* ST\_Buffer\_Strategy
* ST\_Collect
* ST\_FrechetDistance
* ST\_GeoHash
* ST\_GeomCollFromTxt
* ST\_HausdorffDistance
* ST\_IsValid
* ST\_LatFromGeoHash
* ST\_Latitude
* ST\_LineInterpolatePoint
* ST\_LineInterpolatePoints
* ST\_LongFromGeoHash
* ST\_Longitude
* ST\_MakeEnvelope
* ST\_NumInteriorRing
* ST\_PointAtDistance
* ST\_PointFromGeoHash
* ST\_Simplify
* ST\_SwapXY
* ST\_Transform
* ST\_Validate ([MDEV-17398](https://jira.mariadb.org/browse/MDEV-17398))

### JSON

* JSON\_SCHEMA\_VALIDATION\_REPORT
* JSON\_STORAGE\_FREE
* JSON\_STORAGE\_SIZE ([MDEV-17397](https://jira.mariadb.org/browse/MDEV-17397))
* MEMBER\_OF operator

### Regular Expressions

* REGEXP\_LIKE ([MDEV-16599](https://jira.mariadb.org/browse/MDEV-16599))

### UUID

* BIN\_TO\_UUID
* IS\_UUID
* UUID\_TO\_BIN ([MDEV-15854](https://jira.mariadb.org/browse/MDEV-15854))

### Miscellaneous

* ANY\_VALUE ([MDEV-10426](https://jira.mariadb.org/browse/MDEV-10426))
* ASYNCHRONOUS\_CONNECTION\_FAILOVER\_ADD\_SOURCE
* ASYNCHRONOUS\_CONNECTION\_FAILOVER\_DELETE\_SOURCE
* FORMAT\_BYTES ([MDEV-19629](https://jira.mariadb.org/browse/MDEV-19629))
* GROUPING ([MDEV-32789](https://jira.mariadb.org/browse/MDEV-32789))
* PS\_THREAD\_ID ([MDEV-19629](https://jira.mariadb.org/browse/MDEV-19629))
* PS\_CURRENT\_THREAD\_ID
* SOURCE\_POS\_WAIT
* VALIDATE\_PASSWORD\_STRENGTH ([MDEV-25703](https://jira.mariadb.org/browse/MDEV-25703))

## See Also

* [Incompatibilities and Feature Differences Between MariaDB 11.4 and MySQL 8.0](../incompatibilities-and-feature-differences-between-mariadb-11-4-and-mysql-8.md)
* [Function Differences Between MariaDB 11.3 and MySQL 8.0](function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-11-3-and-mysql-8-0.md)
* [System Variable Differences Between MariaDB 11.4 and MySQL 8.0](../system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-11-4-and-mysql-8-0.md)
* [MariaDB versus MySQL - Compatibility](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/compatibility-and-differences/function-differences-between-mariadb-and-mysql/broken-reference/README.md)
* [MariaDB versus MySQL - Features](../mariadb-vs-mysql-features.md)

{% @marketo/form formid="4316" formId="4316" %}
