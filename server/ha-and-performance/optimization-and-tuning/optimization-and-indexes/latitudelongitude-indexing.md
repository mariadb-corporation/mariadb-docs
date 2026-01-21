# Latitude/Longitude Indexing

## The problem

You want to find the nearest 10 pizza parlors, but you cannot figure out how to do it efficiently in your huge database. Database indexes are good at one-dimensional indexing, but poor at two-dimensions.

You might have tried

* INDEX(lat), INDEX(lon) -- but the optimizer used only one
* INDEX(lat,lon) -- but it still had to work too hard
* Sometimes you ended up with a full table scan -- Yuck.

WHERE [SQRT(...)](../../../reference/sql-functions/numeric-functions/sqrt.md)< ... -- No chance of using any index.

WHERE lat BETWEEN ... AND lng BETWEEN... -- This has some chance of using such indexes.

The goal is to look only at records "close", in both directions, to the target lat/lng.

## A solution -- first, the principles

[PARTITIONs](../../../server-usage/partitioning-tables/) in MariaDB and MySQL sort of give you a way to have two clustered indexes. So, if we could slice up (partition) the globe in one dimension and use ordinary indexing in the other dimension, maybe we can get something approximating a 2D index. This 2D approach keeps the number of disk hits significantly lower than 1D approaches, thereby speeding up "find nearest" queries.

It works. Not perfectly, but better than the alternatives.

What to PARTITION on? It seems like latitude or longitude would be a good idea. Note that longitudes vary in width, from 69 miles (111 km) at the equator, to 0 at the poles. So, latitude seems like a better choice.

How many PARTITIONs? It does not matter a lot. Some thoughts:

* 90 partitions - 2 degrees each. (I don't like tables with too many partitions; 90 seems like plenty.)
* 50-100 - evenly populated. (This requires code. For 2.7M placenames, 85 partitions varied from 0.5 degrees to very wide partitions at the poles.)
* Don't have more than 100 partitions, there are inefficiencies in the partition implementation.

How to PARTITION? Well, MariaDB and MySQL are very picky. So [FLOAT](../../../reference/data-types/numeric-data-types/float.md)/[DOUBLE](../../../reference/data-types/numeric-data-types/double.md) are out. [DECIMAL](../../../reference/data-types/numeric-data-types/decimal.md) is out. So, we are stuck with some kludge. Essentially, we need to convert Lat/Lng to some size of [INT](../../../reference/data-types/numeric-data-types/int.md) and use PARTITION BY RANGE.

## Representation choices

To get to a datatype that can be used in PARTITION, you need to "scale" the latitude and longitude. (Consider only the \*INTs; the other datatypes are included for comparison)

```
Datatype           Bytes       resolution
   ------------------ -----  --------------------------------
   Deg*100 (SMALLINT)     4  1570 m    1.0 mi  Cities
   DECIMAL(4,2)/(5,2)     5  1570 m    1.0 mi  Cities
   SMALLINT scaled        4   682 m    0.4 mi  Cities
   Deg*10000 (MEDIUMINT)  6    16 m     52 ft  Houses/Businesses
   DECIMAL(6,4)/(7,4)     7    16 m     52 ft  Houses/Businesses
   MEDIUMINT scaled       6   2.7 m    8.8 ft
   FLOAT                  8   1.7 m    5.6 ft
   DECIMAL(8,6)/(9,6)     9    16cm    1/2 ft  Friends in a mall
   Deg*10000000 (INT)     8    16mm    5/8 in  Marbles
   DOUBLE                16   3.5nm     ...    Fleas on a dog
```

(Sorted by resolution)

What these mean...

Deg\*100 ([SMALLINT](../../../reference/data-types/numeric-data-types/smallint.md)) -- you take the lat/lng, multiply by 100, round, and store into a SMALLINT. That will take 2 bytes for each dimension, for a total of 4 bytes. Two items might be 1570 meters apart, but register as having the same latitude and longitude.

[DECIMAL(4,2)](../../../reference/data-types/numeric-data-types/decimal.md) for latitude and DECIMAL(5,2) for longitude will take 2+3 bytes and have no better resolution than Deg\*100.

SMALLINT scaled -- Convert latitude into a SMALLINT SIGNED by doing (degrees / 90 \* 32767) and rounding; longitude by (degrees / 180 \* 32767).

[FLOAT](../../../reference/data-types/numeric-data-types/float.md) has 24 significant bits; [DOUBLE](../../../reference/data-types/numeric-data-types/double.md) has 53. (They don't work with PARTITIONing but are included for completeness. Often people use DOUBLE without realizing how much an overkill it is, and how much space it takes.)

Sure, you could do DEG_1000 and other "in between" cases, but there is no advantage. DEG_1000 takes as much space as DEG\*10000, but has less resolution.

So, go down the list to see how much resolution you need, then pick an encoding you are comfortable with. However, since we are about to use latitude as a "partition key", it must be limited to one of the INTs. For the sample code, I will use Deg\*10000 ([MEDIUMINT](../../../reference/data-types/numeric-data-types/mediumint.md)).

## GCDist -- compute "great circle distance"

GCDist is a helper FUNCTION that correctly computes the distance between two points on the globe.

The code has been benchmarked at about 20 microseconds per call on a 2011-vintage PC. If you had to check a million points, that would take 20 seconds -- far too much for a web application. So, one goal of the Procedure that uses it will be to minimize the usage of this function. With the code presented here, the function need be called only a few dozen or few hundred times, except in pathological cases.

Sure, you could use the Pythagorean formula. And it would work for most applications. But it does not take extra effort to do the GC. Furthermore, GC works across a pole and across the dateline. And, a Pythagorean function is not that much faster.

For efficiency, GCDist understands the scaling you picked and has that stuff hardcoded. I am picking "Deg\*10000", so the function expects 350000 for representing 35 degrees. If you choose a different scaling, you will need to change the code.

GCDist() takes 4 scaled DOUBLEs -- lat1, lon1, lat2, lon2 -- and returns a scaled number of "degrees" representing the distance.

The table of representation choices says 52 feet of resolution for Deg\*10000 and DECIMAL(x,4). Here is how it was calculated: To measuring a diagonal between lat/lng (0,0) and (0.0001,00001) (one 'unit in the last place'): GCDist(0,0,1,1) \* 69.172 / 10000 \* 5280 = 51.65, where

* 69.172 miles/degree of latitude
* 10000 units per degree for the scaling chosen
* 5280 feet / mile.

(No, this function does not compensate for the Earth being an oblate spheroid, etc.)

## Required table structure

There will be one table (plus normalization tables as needed). The one table must be partitioned and indexed as indicated below.

Fields and indexes

* PARTITION BY RANGE(lat)
* lat -- scaled latitude (see above)
* lon -- scaled longitude
* PRIMARY KEY(lon, lat, ...) -- lon must be first; something must be added to make it UNIQUE
* id -- (optional) you may need to identify the rows for your purposes; AUTO\_INCREMENT if you like
* INDEX(id) -- if `id` is [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md), then this plain INDEX (not UNIQUE, not PRIMARY KEY) is necessary
* ENGINE=[InnoDB](../../../server-usage/storage-engines/innodb/) -- so the PRIMARY KEY will be "clustered"
* Other indexes -- keep to a minimum (this is a general performance rule for large tables)

For most of this discussion, lat is assumed to be MEDIUMINT -- scaled from -90 to +90 by multiplying by 10000. Similarly for lon and -180 to +180.

The PRIMARY KEY must

* start with `lon` since the algorithm needs the "clustering" that InnoDB will provide, and
* include `lat` somewhere, since it is the PARTITION key, and
* contain something to make the key UNIQUE (lon+lat is unlikely to be sufficient).

The FindNearest PROCEDURE will do multiple SELECTs something like this:

```sql
WHERE lat    BETWEEN @my_lat - @dlat
                       AND @my_lat + @dlat   -- PARTITION Pruning and bounding box
        AND lon    BETWEEN @my_lon - @dlon
                       AND @my_lon + @dlon   -- first part of PK
        AND condition                        -- filter out non-pizza parlors
```

The query planner will

* Do PARTITION "pruning" based on the latitude; then
* Within a PARTITION (which is effectively a table), use lon do a 'clustered' range scan; then
* Use the "condition" to filter down to the rows you desire, plus recheck lat.\
  This design leads to very few disk blocks needing to be read, which is the main goal of the design.

Note that this does not even call GCDist. That comes in the last pass when the ORDER BY and LIMIT are used.

The [stored procedure](../../../server-usage/stored-routines/stored-procedures/) has a loop. At least two SELECTs will be executed, but with proper tuning; usually no more than about 6 SELECTs will be performed. Because of searching by the PRIMARY KEY, each SELECT hits only one block, sometimes more, of the table. Counting the number of blocks hit is a crude, but effective way, of comparing the performance of multiple designs. By comparison, a full table scan will probably touch thousands of blocks. A simple INDEX(lat) probably leads to hitting hundreds of blocks.

Filtering... An argument to the FindNearest procedure includes a boolean expression ("condition") for a WHERE clause. If you don't need any filtering, pass in "1". To avoid "SQL injection", do not let web users put arbitrary expressions; instead, construct the "condition" from inputs they provide, thereby making sure it is safe.

## The algorithm

The algorithm is embodied in a [stored procedure](../../../server-usage/stored-routines/stored-procedures/) because of its complexity.

* You feed it a starting width for a "square" and a number of items to find.
* It builds a "square" around where you are.
* A SELECT is performed to see how many items are in the square.
* Loop, doubling the width of the square, until enough items are found.
* Now, a 'last' SELECT is performed to get the exact distances, sort them (ORDER BY) and LIMIT to the desired number.
* If spanning a pole or the dateline, a more complex SELECT is used.

The next section ("Performance") should make this a bit clearer as it walks through some examples.

## Performance

Because of all the variations, it is hard to get a meaningful benchmark. So, here is some hand-waving instead.

Each SELECT is constrained by a "square" defined by a latitude range and a longitude range. (See the WHERE clause mentioned above, or in the sample code below.) Because of the way longitude lines warp, the longitude range of the "square" will be more degrees than the latitude range. Let's say the latitude partitioning is 3 degrees wide in the area where you are searching. That is over 200 miles (over 300km), so you are very likely to have a latitude range smaller than the partition width. Still, if you are reaching from the edge of a latitude stripe, the square could span two partitions. After partition pruning down to one (sometimes more) partition, the query is then constrained by a longitude range. (Remember, the PRIMARY KEY starts with `lon`.) If an InnoDB data block contains 100 rows (a handy Rule of Thumb), the select will touch one (or a few) block. If the square spans two (or more) partitions, then the same logic applies to each partition.

So, scanning the square will involve as little as one block; rarely more than a few blocks. The number of blocks is mostly independent of the dataset size.

The primary use case for this algorithm is when the data is significantly larger than will fit into cache (the buffer\_pool). Hence, the main goal is to minimize the number of disk hits.

Now let's look at some edge cases, and argue that the number of blocks is still better (usually) than with traditional indexing techniques.

What if you are looking for Starbucks in a dense city? There would be dozens, maybe hundreds per square mile. If you start the guess at 100 miles, the SELECTs would be hitting lots of blocks -- not efficient. In this case, the "starting distance" should be small, say, 2 miles. Let's say your app wants the closest 10 stores. In this example, you would probably find more than 10 Starbucks within 2 miles in 1 InnoDB block in one partition. Even though there is a second SELECT to finish off the query, it would be hitting the same block. Total: One block hit == cheap.

Let's say you start with a 5 mile square. Since there are upwards of 200 Starbucks within a 5-miles radius in some dense cities of the world, that might imply 300 in our "square". That maps to about 4 disk blocks, and a modest amount of CPU to chew through the 300 records. Still not bad.

Now, suppose you are on an ocean liner somewhere in the Pacific. And there is one Starbucks onboard, but you are looking for the nearest 10. If you again start with 2 miles, it will take several iterations to find 10 sites. But, let's walk through it anyway. The first probe will hit one partition (maybe 2), and find just one hit. The second probe doubles the width of the square; 4 miles will still give you one hit -- the same hit in the same block, which is now cached, so we won't count it as a second disk I/O. Eventually the square will be wide enough to span multiple partitions. Each extra partition will be one new disk hit to discover no sites in the square. Finally, the square will hit Chile or Hawaii or Fiji and find some more sites, perhaps enough to stop the iteration. Since the main criteria in determining the number of disk hits is the number of partitions hit, we do not want to split the world into too many partitions. If there are, say, 40 partitions, then I have just described a case where there might be 20 disk hits.

2-degree partitions might be good for a global table of stores or restaurants. A 5-mile starting distance might be good when filtering for Starbucks. 20 miles might be better for a department store.

Now, let's discuss the 'last' SELECT, wherein the square is expanded by SQRT(2) and it uses the Great Circle formula to precisely order the N results. The SQRT(2) is in case that the N items were all at the corners of the 'square'. Growing the square by this much allows us to catch any other sites that were just outside the old square.

First, note that this 'last' SELECT is hitting the same block(s) that the iteration hit, plus possibly hitting some more blocks. It is hard to predict how many extra blocks might be hit. Here's a pathological case. You are in the middle of a desert; the square grows and grows. Eventually it finds N sites. There is a big city just outside the final square from the iterating. Now the 'last' SELECT kicks in, and it includes lots of sites in this big city. "Lots of sites" --> lots of blocks --> lots of disk hits.

## Discussion of reference code

Here's the gist of the [stored procedure](../../../server-usage/stored-routines/stored-procedures/) FindNearest().

* Make a guess at how close to "me" to look.
* See how many items are in a 'square' around me, after filtering.
* If not enough, repeat, doubling the width of the square.
* After finding enough, or giving up because we are looking "too far", make one last pass to get all the data, ORDERed and LIMITed

Note that the loop merely uses 'squares' of lat/lng ranges. This is crude, but works well with the partitioning and indexing, and avoids calling to GCDist (until the last step). In the sample code, I picked 15 miles as starting value. Adjusting this will have some impact on the Procedure's performance, but the impact will vary with the use cases. A rough way to set the radius is to guess what will find the desired LIMIT about half the time. (This value is hardcoded in the PROCEDURE.)

Parameters passed into FindNearest():

* your Latitude -- -90..90 (not scaled -- see hardcoded conversion in PROCEDURE)
* your Longitude -- -180..180 (not scaled)
* Start distance -- (miles or km) -- see discussion below
* Max distance -- in miles or km -- see hardcoded conversion in PROCEDURE
* Limit -- maximum number of items to return
* Condition -- something to put after 'AND' (more discussion above)

The function will find the nearest items, up to Limit that meet the Condition. But it will give up at Max distance. (If you are at the South Pole, why bother searching very far for the tenth pizza parlor?)

Because of the "scaling", "hardcoding", "Condition", the table name, etc, this PROCEDURE is not truly generic; the code must be modified for each application. Yes, I could have designed it to pass all that stuff in. But what a mess.

The "\_start\_dist" gives some control over the performance. Making this too small leads to extra iterations; too big leads to more rows being checked. If you choose to tune the Stored Procedure, do the following. "SELECT @iterations" after calling the SP for a number of typical values. If the value is usually 1, then decrease \_start\_dist. If it is usually 2 or more, then increase it.

Timing: Under 10ms for "typical" usage; any dataset size. Slower for pathological cases (low min distance, high max distance, crossing dateline, bad filtering, cold cache, etc)

End-cases:

* By using GC distance, not Pythagoras, distances are 'correct' even near poles.
* Poles -- Even if the "nearest" is almost 360 degrees away (longitude), it can find it.
* Dateline -- There is a small, 'contained', piece of code for crossing the Dateline. Example: you are at +179 deg longitude, and the nearest item is at -179.

The procedure returns one resultset, SELECT \*, distance.

* Only rows that meet your Condition, within Max distance are returned
* At most Limit rows are returned
* The rows will be ordered, "closest" first.
* "dist" will be in miles or km (based on a hardcoded constant in the SP)

## Reference code, assuming deg\*10000 and 'miles'

This version is based on scaling "Deg\*10000 (MEDIUMINT)".

```sql
DELIMITER //

DROP function IF EXISTS GCDist //
CREATE FUNCTION GCDist (
        _lat1 DOUBLE,  -- Scaled Degrees north for one point
        _lon1 DOUBLE,  -- Scaled Degrees west for one point
        _lat2 DOUBLE,  -- other point
        _lon2 DOUBLE
    ) RETURNS DOUBLE
    DETERMINISTIC
    CONTAINS SQL  -- SQL but does not read or write
    SQL SECURITY INVOKER  -- No special privileges granted
-- Input is a pair of latitudes/longitudes multiplied by 10000.
--    For example, the south pole has latitude -900000.
-- Multiply output by .0069172 to get miles between the two points
--    or by .0111325 to get kilometers
BEGIN
    -- Hardcoded constant:
    DECLARE _deg2rad DOUBLE DEFAULT PI()/1800000;  -- For scaled by 1e4 to MEDIUMINT
    DECLARE _rlat1 DOUBLE DEFAULT _deg2rad * _lat1;
    DECLARE _rlat2 DOUBLE DEFAULT _deg2rad * _lat2;
    -- compute as if earth's radius = 1.0
    DECLARE _rlond DOUBLE DEFAULT _deg2rad * (_lon1 - _lon2);
    DECLARE _m     DOUBLE DEFAULT COS(_rlat2);
    DECLARE _x     DOUBLE DEFAULT COS(_rlat1) - _m * COS(_rlond);
    DECLARE _y     DOUBLE DEFAULT               _m * SIN(_rlond);
    DECLARE _z     DOUBLE DEFAULT SIN(_rlat1) - SIN(_rlat2);
    DECLARE _n     DOUBLE DEFAULT SQRT(
                        _x * _x +
                        _y * _y +
                        _z * _z    );
    RETURN  2 * ASIN(_n / 2) / _deg2rad;   -- again--scaled degrees
END;
//
DELIMITER ;

DELIMITER //
-- FindNearest (about my 6th approach)
DROP PROCEDURE IF EXISTS FindNearest6 //
CREATE
PROCEDURE FindNearest (
        IN _my_lat DOUBLE,  -- Latitude of me [-90..90] (not scaled)
        IN _my_lon DOUBLE,  -- Longitude [-180..180]
        IN _START_dist DOUBLE,  -- Starting estimate of how far to search: miles or km
        IN _max_dist DOUBLE,  -- Limit how far to search: miles or km
        IN _limit INT,     -- How many items to try to get
        IN _condition VARCHAR(1111)   -- will be ANDed in a WHERE clause
    )
    DETERMINISTIC
BEGIN
    -- lat and lng are in degrees -90..+90 and -180..+180
    -- All computations done in Latitude degrees.
    -- Thing to tailor
    --   *Locations* -- the table
    --   Scaling of lat, lon; here using *10000 in MEDIUMINT
    --   Table name
    --   miles versus km.

    -- Hardcoded constant:
    DECLARE _deg2rad DOUBLE DEFAULT PI()/1800000;  -- For scaled by 1e4 to MEDIUMINT

    -- Cannot use params in PREPARE, so switch to @variables:
    -- Hardcoded constant:
    SET @my_lat := _my_lat * 10000,
        @my_lon := _my_lon * 10000,
        @deg2dist := 0.0069172,  -- 69.172 for miles; 111.325 for km  *** (mi vs km)
        @start_deg := _start_dist / @deg2dist,  -- Start with this radius first (eg, 15 miles)
        @max_deg := _max_dist / @deg2dist,
        @cutoff := @max_deg / SQRT(2),  -- (slightly pessimistic)
        @dlat := @start_deg,  -- note: must stay positive
        @lon2lat := COS(_deg2rad * @my_lat),
        @iterations := 0;        -- just debugging

    -- Loop through, expanding search
    --   Search a 'square', repeat with bigger square until find enough rows
    --   If the inital probe found _limit rows, then probably the first
    --   iteration here will find the desired data.
    -- Hardcoded table name:
    -- This is the "first SELECT":
    SET @sql = CONCAT(
        "SELECT COUNT(*) INTO @near_ct
            FROM Locations
            WHERE lat    BETWEEN @my_lat - @dlat
                             AND @my_lat + @dlat   -- PARTITION Pruning and bounding box
              AND lon    BETWEEN @my_lon - @dlon
                             AND @my_lon + @dlon   -- first part of PK
              AND ", _condition);
    PREPARE _sql FROM @sql;
    MainLoop: LOOP
        SET @iterations := @iterations + 1;
        -- The main probe: Search a 'square'
        SET @dlon := ABS(@dlat / @lon2lat);  -- good enough for now  -- note: must stay positive
        -- Hardcoded constants:
        SET @dlon := IF(ABS(@my_lat) + @dlat >= 900000, 3600001, @dlon);  -- near a Pole
        EXECUTE _sql;
        IF ( @near_ct >= _limit OR         -- Found enough
             @dlat >= @cutoff ) THEN       -- Give up (too far)
            LEAVE MainLoop;
        END IF;
        -- Expand 'square':
        SET @dlat := LEAST(2 * @dlat, @cutoff);   -- Double the radius to search
    END LOOP MainLoop;
    DEALLOCATE PREPARE _sql;

    -- Out of loop because found _limit items, or going too far.
    -- Expand range by about 1.4 (but not past _max_dist),
    -- then fetch details on nearest 10.

    -- Hardcoded constant:
    SET @dlat := IF( @dlat >= @max_deg OR @dlon >= 1800000,
                @max_deg,
                GCDist(ABS(@my_lat), @my_lon,
                       ABS(@my_lat) - @dlat, @my_lon - @dlon) );
            -- ABS: go toward equator to find farthest corner (also avoids poles)
            -- Dateline: not a problem (see GCDist code)

    -- Reach for longitude line at right angle:
    -- sin(dlon)*cos(lat) = sin(dlat)
    -- Hardcoded constant:
    SET @dlon := IFNULL(ASIN(SIN(_deg2rad * @dlat) /
                             COS(_deg2rad * @my_lat))
                            / _deg2rad -- precise
                        , 3600001);    -- must be too near a pole

    -- This is the "last SELECT":
    -- Hardcoded constants:
    IF (ABS(@my_lon) + @dlon < 1800000 OR    -- Usual case - not crossing dateline
        ABS(@my_lat) + @dlat <  900000) THEN -- crossing pole, so dateline not an issue
        -- Hardcoded table name:
        SET @sql = CONCAT(
            "SELECT *,
                    @deg2dist * GCDist(@my_lat, @my_lon, lat, lon) AS dist
                FROM Locations
                WHERE lat BETWEEN @my_lat - @dlat
                              AND @my_lat + @dlat   -- PARTITION Pruning and bounding box
                  AND lon BETWEEN @my_lon - @dlon
                              AND @my_lon + @dlon   -- first part of PK
                  AND ", _condition, "
                HAVING dist <= ", _max_dist, "
                ORDER BY dist
                LIMIT ", _limit
                        );
    ELSE
        -- Hardcoded constants and table name:
        -- Circle crosses dateline, do two SELECTs, one for each side
        SET @west_lon := IF(@my_lon < 0, @my_lon, @my_lon - 3600000);
        SET @east_lon := @west_lon + 3600000;
        -- One of those will be beyond +/- 180; this gets points beyond the dateline
        SET @sql = CONCAT(
            "( SELECT *,
                    @deg2dist * GCDist(@my_lat, @west_lon, lat, lon) AS dist
                FROM Locations
                WHERE lat BETWEEN @my_lat - @dlat
                              AND @my_lat + @dlat   -- PARTITION Pruning and bounding box
                  AND lon BETWEEN @west_lon - @dlon
                              AND @west_lon + @dlon   -- first part of PK
                  AND ", _condition, "
                HAVING dist <= ", _max_dist, " )
            UNION ALL
            ( SELECT *,
                    @deg2dist * GCDist(@my_lat, @east_lon, lat, lon) AS dist
                FROM Locations
                WHERE lat BETWEEN @my_lat - @dlat
                              AND @my_lat + @dlat   -- PARTITION Pruning and bounding box
                  AND lon BETWEEN @east_lon - @dlon
                              AND @east_lon + @dlon   -- first part of PK
                  AND ", _condition, "
                HAVING dist <= ", _max_dist, " )
            ORDER BY dist
            LIMIT ", _limit
                        );
    END IF;

    PREPARE _sql FROM @sql;
    EXECUTE _sql;
    DEALLOCATE PREPARE _sql;
END;
//
DELIMITER ;
<<code>>

== Sample

Find the 5 cities with non-zero population (out of 3 million) nearest to (+35.15, -90.15). Start with a 10-mile bounding box and give up at 100 miles.

<<code>>
CALL FindNearestLL(35.15, -90.05, 10, 100, 5, 'population > 0');
+---------+--------+---------+---------+--------------+--------------+-------+------------+--------------+---------------------+------------------------+
| id      | lat    | lon     | country | ascii_city   | city         | state | population | @gcd_ct := 0 | dist                | @gcd_ct := @gcd_ct + 1 |
+---------+--------+---------+---------+--------------+--------------+-------+------------+--------------+---------------------+------------------------+
| 3023545 | 351494 | -900489 | us      | memphis      | Memphis      | TN    |     641608 |            0 | 0.07478733189367963 |                      3 |
| 2917711 | 351464 | -901844 | us      | west memphis | West Memphis | AR    |      28065 |            0 |   7.605683607627499 |                      2 |
| 2916457 | 352144 | -901964 | us      | marion       | Marion       | AR    |       9227 |            0 |     9.3994963998986 |                      1 |
| 3020923 | 352044 | -898739 | us      | bartlett     | Bartlett     | TN    |      43264 |            0 |  10.643941157860604 |                      7 |
| 2974644 | 349889 | -900125 | us      | southaven    | Southaven    | MS    |      38578 |            0 |  11.344042217329935 |                      5 |
+---------+--------+---------+---------+--------------+--------------+-------+------------+--------------+---------------------+------------------------+
5 rows in set (0.00 sec)
Query OK, 0 rows affected (0.04 sec)

SELECT COUNT(*) FROM ll_table;
+----------+
| COUNT(*) |
+----------+
|  3173958 |
+----------+
1 row in set (5.04 sec)

FLUSH STATUS;
CALL...
SHOW SESSION STATUS LIKE 'Handler%';

SHOW session status LIKE 'Handler%';
+----------------------------+-------+
| Variable_name              | Value |
+----------------------------+-------+
| Handler_read_first         | 1     |
| Handler_read_key           | 3     |
| Handler_read_next          | 1307  |  -- some index, some tmp, but far less than 3 million.
| Handler_read_rnd           | 5     |
| Handler_read_rnd_next      | 13    |
| Handler_write              | 12    |  -- it needed a tmp
+----------------------------+-------+
```

## Postlog

There is a "Haversine" algorithm that is twice as fast as the GCDist function here. But it has a fatal flaw of sometimes returning NULL for the distance between a point and itself. (This is because of computing a number slightly bigger than 1.0, then trying to take the ACOS of it.)

## See also

* [Cities used for testing](https://www.maxmind.com/en/worldcities)
* [A forum thread](https://forums.mysql.com/read.php?20,619712,619712)
* [StackOverflow discussion](https://stackoverflow.com/questions/29058863/mysql-query-takes-long-time/)
* [Sample](https://dba.stackexchange.com/questions/134028/select-the-minimum-of-a-calculated-distance-value-without-sorting)
* [Z-ordering](https://en.wikipedia.org/wiki/Geohash)

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [latlng](https://mysql.rjweb.org/doc.php/latlng)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
