# Function Differences Between MariaDB 10.6 and MySQL 8.0

The following is a list of all function differences between [MariaDB 10.6]({release-notes}/community-server/10.6/what-is-mariadb-106) and MySQL 8.0. It is based on functions available in the MySQL 8.0.23 and the [MariaDB 10.6.12]({release-notes}/community-server/10.6/10.6.12) releases. For a more complete list of differences, see [Incompatibilities and Feature Differences Between MariaDB 10.6 and MySQL 8.0](../incompatibilities-and-feature-differences-between-mariadb-10-6-and-mysql-8.md)

## Present in MariaDB Only

### Dynamic Columns

* [COLUMN\_ADD](../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_add.md)
* [COLUMN\_CHECK](../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_check.md)
* [COLUMN\_CREATE](../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_create.md)
* [COLUMN\_DELETE](../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_delete.md)
* [COLUMN\_EXISTS](../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_exists.md)
* [COLUMN\_GET](../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_get.md)
* [COLUMN\_JSON](../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_json.md)
* [COLUMN\_LIST](../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_list.md)

### Galera

* [WSREP\_LAST\_SEEN\_GTID](../../../reference/sql-functions/special-functions/galera-functions/wsrep_last_seen_gtid.md)
* [WSREP\_LAST\_WRITTEN\_GTID](../../../reference/sql-functions/special-functions/galera-functions/wsrep_last_written_gtid.md)
* [WSREP\_SYNC\_WAIT\_UPTO\_GTID](../../../reference/sql-functions/special-functions/galera-functions/wsrep_sync_wait_upto_gtid.md)

### General

* [ADD\_MONTHS](../../../reference/sql-functions/date-time-functions/add_months.md)
* [CHR](../../../reference/sql-functions/string-functions/chr.md)
* [DECODE\_ORACLE](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/decode.md)
* [DES\_DECRYPT](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_decrypt.md)
* [DES\_ENCRYPT](../../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_encrypt.md)
* [LENGTHB](../../../reference/sql-functions/string-functions/lengthb.md)
* [NVL](../../../reference/sql-functions/control-flow-functions/ifnull.md) (Synonym for IFNULL)
* [NVL2](../../../reference/sql-functions/control-flow-functions/nvl2.md)
* [SYS\_GUID](../../../reference/sql-functions/secondary-functions/miscellaneous-functions/sys_guid.md)
* [TO\_CHAR](../../../reference/sql-functions/string-functions/to_char.md)
* [TRIM\_ORACLE](../../../reference/sql-functions/string-functions/trim.md)
* [VALUE](../../../reference/sql-functions/secondary-functions/miscellaneous-functions/values-value.md) - the VALUES() function was renamed after MariaDB introduced Table Value Constructors.

### Geographic

MySQL has removed the following functions in MySQL 8.0.

* [AREA](../../../reference/sql-statements/geometry-constructors/polygon-properties/st_area.md)
* [AsBinary](../../../reference/sql-statements/geometry-constructors/wkb/st_asbinary.md)
* [AsText](../../../reference/sql-statements/geometry-constructors/wkt/st_astext.md)
* [AsWKB](../../../reference/sql-statements/geometry-constructors/wkb/aswkb.md)
* [AsWKT](../../../reference/sql-statements/geometry-constructors/wkt/st_aswkt.md)
* [Buffer](../../../reference/sql-statements/geometry-constructors/geometry-constructors/buffer.md)
* [Centroid](../../../reference/sql-statements/geometry-constructors/polygon-properties/centroid.md)
* [Contains](../../../reference/sql-statements/geometry-constructors/geometry-relations/contains.md)
* [ConvexHull](../../../reference/sql-statements/geometry-constructors/geometry-constructors/convexhull.md)
* [Crosses](../../../reference/sql-statements/geometry-constructors/geometry-relations/crosses.md)
* [Dimension](../../../reference/sql-statements/geometry-constructors/geometry-properties/dimension.md)
* [Disjoint](../../../reference/sql-statements/geometry-constructors/geometry-relations/disjoint.md)
* [EndPoint](../../../reference/sql-statements/geometry-constructors/linestring-properties/st_endpoint.md)
* [Envelope](../../../reference/sql-statements/geometry-constructors/geometry-properties/st_envelope.md)
* [Equals](../../../reference/sql-statements/geometry-constructors/geometry-relations/equals.md)
* [ExteriorRing](../../../reference/sql-statements/geometry-constructors/polygon-properties/st_exteriorring.md)
* [GeomCollFromText](../../../reference/sql-statements/geometry-constructors/wkt/st_geomcollfromtext.md)
* [GeomCollFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/st_geomcollfromwkb.md)
* [GeomFromText](../../../reference/sql-statements/geometry-constructors/wkt/st_geomfromtext.md)
* [GeomFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/st_geomfromwkb.md)
* [GeometryCollectionFromText](../../../reference/sql-statements/geometry-constructors/wkt/geometrycollectionfromtext.md)
* [GeometryCollectionFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/geometrycollectionfromwkb.md)
* [GeometryFromText](../../../reference/sql-statements/geometry-constructors/wkt/geometryfromtext.md)
* [GeometryFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/geometryfromwkb.md)
* [GeometryN](../../../reference/sql-statements/geometry-constructors/geometry-properties/st_geometryn.md)
* [GeometryType](../../../reference/sql-statements/geometry-constructors/geometry-properties/st_geometrytype.md)
* [GLENGTH](../../../reference/sql-statements/geometry-constructors/linestring-properties/glength.md)
* [InteriorRingN](../../../reference/sql-statements/geometry-constructors/polygon-properties/st_interiorringn.md)
* [Intersects](../../../reference/sql-statements/geometry-constructors/geometry-relations/intersects.md)
* [IsClosed](../../../reference/sql-statements/geometry-constructors/geometry-properties/isclosed.md)
* [IsEmpty](../../../reference/sql-statements/geometry-constructors/geometry-properties/st_isempty.md)
* [IsSimple](../../../reference/sql-statements/geometry-constructors/geometry-properties/st_issimple.md)
* [LineFromText](../../../reference/sql-statements/geometry-constructors/wkt/st_linefromtext.md)
* [LineFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/st_linefromwkb.md)
* [LineStringFromText](../../../reference/sql-statements/geometry-constructors/wkt/linestringfromtext.md)
* [LineStringFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/linestringfromwkb.md)
* [MLineFromText](../../../reference/sql-statements/geometry-constructors/wkt/mlinefromtext.md)
* [MLineFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/mlinefromwkb.md)
* [MPointFromText](../../../reference/sql-statements/geometry-constructors/wkt/mpointfromtext.md)
* [MPointFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/mpointfromwkb.md)
* [MPolyFromText](../../../reference/sql-statements/geometry-constructors/wkt/mpolyfromtext.md)
* [MPolyFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/mpolyfromwkb.md)
* [MultiLineStringFromText](../../../reference/sql-statements/geometry-constructors/wkt/multilinestringfromtext.md)
* [MultiLineStringFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/multilinestringfromwkb.md)
* [MultiPointFromText](../../../reference/sql-statements/geometry-constructors/wkt/multipointfromtext.md)
* [MultiPointFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/multipointfromwkb.md)
* [MultiPolygonFromText](../../../reference/sql-statements/geometry-constructors/wkt/multipolygonfromtext.md)
* [MultiPolygonFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/multipolygonfromwkb.md)
* [NumGeometries](../../../reference/sql-statements/geometry-constructors/geometry-properties/st_numgeometries.md)
* [NumInteriorRings](../../../reference/sql-statements/geometry-constructors/polygon-properties/st_numinteriorrings.md)
* [NumPoints](../../../reference/sql-statements/geometry-constructors/linestring-properties/st_numpoints.md)
* [Overlaps](../../../reference/sql-statements/geometry-constructors/geometry-relations/overlaps.md)
* [PointFromText](../../../reference/sql-statements/geometry-constructors/wkt/st_pointfromtext.md)
* [PointFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/st_pointfromwkb.md)
* [PointN](../../../reference/sql-statements/geometry-constructors/linestring-properties/st_pointn.md)
* [PolyFromText](../../../reference/sql-statements/geometry-constructors/wkt/st_polyfromtext.md)
* [PolyFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/st_polyfromwkb.md)
* [PolygonFromText](../../../reference/sql-statements/geometry-constructors/wkt/polygonfromtext.md)
* [PolygonFromWKB](../../../reference/sql-statements/geometry-constructors/wkb/polygonfromwkb.md)
* [SRID](../../../reference/sql-statements/geometry-constructors/geometry-properties/st_srid.md)
* [StartPoint](../../../reference/sql-statements/geometry-constructors/linestring-properties/st_startpoint.md)
* [Touches](../../../reference/sql-statements/geometry-constructors/geometry-relations/touches.md)
* [Within](../../../reference/sql-statements/geometry-constructors/geometry-relations/within.md)
* [X](../../../reference/sql-statements/geometry-constructors/point-properties/st_x.md)
* [Y](../../../reference/sql-statements/geometry-constructors/point-properties/st_y.md)

### JSON

* [JSON\_COMPACT](../../../reference/sql-functions/special-functions/json-functions/json_compact.md)
* [JSON\_DETAILED](../../../reference/sql-functions/special-functions/json-functions/json_detailed.md)
* [JSON\_EXISTS](../../../reference/sql-functions/special-functions/json-functions/json_exists.md)
* [JSON\_LOOSE](../../../reference/sql-functions/special-functions/json-functions/json_loose.md)
* [JSON\_QUERY](../../../reference/sql-functions/special-functions/json-functions/json_query.md)
* [JSON\_VALUE](../../../reference/sql-functions/special-functions/json-functions/json_value.md)

### Sequences

* [LASTVAL](../../../reference/sql-structure/sequences/sequence-functions/previous-value-for-sequence_name.md)
* [NEXTVAL](../../../reference/sql-structure/sequences/sequence-functions/next-value-for-sequence_name.md)
* [SETVAL](../../../reference/sql-structure/sequences/sequence-functions/setval.md)

### Window Functions

* [MEDIAN](../../../reference/sql-functions/special-functions/window-functions/median.md)
* [PERCENTILE\_CONT](../../../reference/sql-functions/special-functions/window-functions/percentile_cont.md)
* [PERCENTILE\_DISC](../../../reference/sql-functions/special-functions/window-functions/percentile_disc.md)

## Present in MySQL Only

### GTID

MariaDB and MySQL have differing [GTID](../../../ha-and-performance/standard-replication/gtid/README.md) implementations.

* GTID\_SUBSET
* GTID\_SUBTRACT
* WAIT\_FOR\_EXECUTED\_GTID\_SET
* WAIT\_UNTIL\_SQL\_THREAD\_AFTER\_GTIDS

### Geographic

* GeomCollection
* MBRCoveredBy
* MBRCovers
* ST\_Buffer\_Strategy
* ST\_FrechetDistance
* ST\_GeoHash
* ST\_GeomCollFromTxt
* ST\_HausdorffDistance
* ST\_IsValid
* ST\_LatFromGeoHash
* ST\_Latitude
* ST\_LongFromGeoHash
* ST\_Longitude
* ST\_MakeEnvelope
* ST\_NumInteriorRing
* ST\_PointFromGeoHash
* ST\_Simplify
* ST\_SwapXY
* ST\_Transform
* ST\_Validate ([MDEV-17398](https://jira.mariadb.org/browse/MDEV-17398))

### JSON

* JSON\_OVERLAPS ([MDEV-27677](https://jira.mariadb.org/browse/MDEV-27677))
* JSON\_SCHEMA\_VALID ([MDEV-27128](https://jira.mariadb.org/browse/MDEV-27128))
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
* FORMAT\_PICO\_TIME ([MDEV-19629](https://jira.mariadb.org/browse/MDEV-19629))
* GROUPING ([MDEV-32789](https://jira.mariadb.org/browse/MDEV-32789))
* PS\_THREAD\_ID ([MDEV-19629](https://jira.mariadb.org/browse/MDEV-19629))
* PS\_CURRENT\_THREAD\_ID
* RANDOM\_BYTES ([MDEV-25704](https://jira.mariadb.org/browse/MDEV-25704))
* VALIDATE\_PASSWORD\_STRENGTH ([MDEV-25703](https://jira.mariadb.org/browse/MDEV-25703))

## See Also

* [Incompatibilities and Feature Differences Between MariaDB 10.6 and MySQL 8.0](../incompatibilities-and-feature-differences-between-mariadb-10-6-and-mysql-8.md)
* [Function Differences Between MariaDB 10.5 and MySQL 8.0](function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-10-5-and-mysql-8-0.md)
* [Function Differences Between MariaDB 10.4 and MySQL 8.0](function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-10-4-and-mysql-8-0.md)
* [System Variable Differences Between MariaDB 10.6 and MySQL 8.0](../system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-10-6-and-mysql-8-0.md)
* [MariaDB versus MySQL - Compatibility](../mariadb-vs-mysql-compatibility.md)
* [MariaDB versus MySQL - Features](../mariadb-vs-mysql-features.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
