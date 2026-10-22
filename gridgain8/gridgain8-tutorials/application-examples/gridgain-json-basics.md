---
description: >-
  Populate a GridGain table with JSON data, query it with JSON_VALUE and JSON_QUERY, and speed up queries by flattening fields into indexed columns.
---

# GridGain JSON Basics

## Introduction

{% hint style="info" %}

JSON functions are available only in GridGain Enterprise and Ultimate editions, version 8.9 and above.

{% endhint %}

{% hint style="info" %}

To proceed with this tutorial, you need to [enable the 'gridgain-sql' module](../../gridgain8-development/project-setup.md#enabling-modules).

{% endhint %}

For users storing data in the JSON format - for example, in NoSQL document databases - GridGain offers a number of new functions that simplify working with JSON data. This tutorial shows you how to populate a database with sample JSON data and use the JSON functions to improve query performance.

## Sample Data

The sample JSON data for this tutorial are as follows:

- [The Blue Planet TV show](https://api.tvmaze.com/singlesearch/shows?q=the%20blue%20planet&embed=episodes)
- [Planet Earth TV Show](https://api.tvmaze.com/singlesearch/shows?q=planet%20earth&embed=episodes)

The datasets are relatively large (~15 Kb minified), with many data rows. You may want to tune the node memory defaults (for example, in `bin/ignite.sh`).

## Populate the Database

1. Run a GridGain node.
1. Connect to the node using the embedded sqlline:

   ```bash
   ./bin/sqlline.sh --verbose=true -u jdbc:ignite:thin://127.0.0.1:10800
   ```

1. Create a table to hold the JSON data.

   ```sql
   CREATE TABLE shows(id INT PRIMARY KEY, data VARCHAR);
   ```

{% hint style="info" %}

   Do not forget to escape single quotes `'` with `''` while using SQL.

{% endhint %}

1. For the sake of example comparison, produce duplicates and a few unique rows to be included in the query results.

   ```sql
   INSERT INTO shows(id, data)
   SELECT X, 'put-here-planet-earth-json-sample'
   FROM SYSTEM_RANGE(1, 300000);

   INSERT INTO shows(id, data)
   VALUES (300001, 'put-here-the-blue-planet-json-sample');
   ```

## Query JSON Data

{% hint style="info" %}

The difference between `JSON_QUERY` and `JSON_VALUE` is explained in [JSON Functions](../../reference/sql/functions/json-functions.md).

{% endhint %}

Retrieve a Great Britain (GB) TV show whose first episode aired before 2005:

```sql
SELECT JSON_VALUE(data, '$.name') as name, JSON_VALUE(data, '$.network.name') as network, JSON_QUERY(data, '$.rating') as rating
FROM shows
WHERE TRUE
  AND JSON_VALUE(data, '$.status') = 'Ended'
  AND JSON_VALUE(data, '$.webChannel') is null
  AND ARRAY_CONTAINS(ARRAY['US', 'GB'], JSON_VALUE(data, '$.network.country.code'))
  AND CAST(JSON_VALUE(data, '$.rating.average') AS DOUBLE) > 9
  AND JSON_VALUE(data, '$._embedded.episodes[0].name') = 'Introduction'
  AND JSON_VALUE(data, '$._embedded.episodes[0].airstamp') < '2005-01-01'
;
```

The query plan uses `PUBLIC.SHOWS.__SCAN_` and simply scans the entire table:

```sql
 SELECT
    "PUBLIC".JSON_VALUE("__Z0"."DATA", '$.name') AS "__C0_0",
    "PUBLIC".JSON_VALUE("__Z0"."DATA", '$.network.name') AS "__C0_1",
    "PUBLIC".JSON_QUERY("__Z0"."DATA", '$.rating') AS "__C0_2"
FROM "PUBLIC"."SHOWS" "__Z0"
    /* PUBLIC.SHOWS.__SCAN_ */
WHERE ("PUBLI |
| SELECT
    "__C0_0" AS "NAME",
    "__C0_1" AS "NETWORK",
    "__C0_2" AS "RATING"
FROM "PUBLIC"."__T0"
    /* PUBLIC.merge_scan */ |
```

The query returns the following result:

```
+-------------------+------------+--------------------+
|       NAME        |   NETWORK  |       RATING       |
+-------------------+------------+--------------------+
| The Blue Planet   | BBC One    | {"average":9.1}    |
+-------------------+------------+--------------------+

1 row selected (23.731 seconds)
```

## Improve Performance With Indexes

Now put "JSON" and "performance" in the same sentence by preparing your data and adding indexes.

Your query uses a couple of common fields related to the first episode, hence you can flatten these into separate columns and use them as indexes (read the [automation section below](#automation)):

```sql
ALTER TABLE shows ADD COLUMN first_episode_name VARCHAR;
UPDATE shows SET first_episode_name = JSON_VALUE(data, '$._embedded.episodes[0].name');

ALTER TABLE shows ADD COLUMN first_episode_airstamp timestamp;
UPDATE shows SET first_episode_airstamp = JSON_VALUE(data, '$._embedded.episodes[0].airstamp');

CREATE INDEX shows_first_episode_name_airstamp on shows(first_episode_name, first_episode_airstamp);
```

Now, rewrite the initial query to use the new index:

```sql
SELECT JSON_VALUE(data, '$.name') as name, JSON_VALUE(data, '$.network.name') as network, JSON_QUERY(data, '$.rating') as rating
FROM shows
WHERE TRUE
  AND JSON_VALUE(data, '$.status') = 'Ended'
  AND JSON_VALUE(data, '$.webChannel') is null
  AND ARRAY_CONTAINS(ARRAY['US', 'GB'], JSON_VALUE(data, '$.network.country.code'))
  AND CAST(JSON_VALUE(data, '$.rating.average') AS DOUBLE) > 9
  AND first_episode_name = 'Introduction'
  AND first_episode_airstamp < '2005-01-01'
;
```

Note that the query plan uses the created index - `PUBLIC.SHOWS_FIRST_EPISODE_NAME_AIRST`:

```sql
SELECT
    "PUBLIC".JSON_VALUE("__Z0"."DATA", '$.name') AS "__C0_0",
    "PUBLIC".JSON_VALUE("__Z0"."DATA", '$.network.name') AS "__C0_1",
    "PUBLIC".JSON_QUERY("__Z0"."DATA", '$.rating') AS "__C0_2"
FROM "PUBLIC"."SHOWS" "__Z0"
    /* PUBLIC.SHOWS_FIRST_EPISODE_NAME_AIRST |
| SELECT
    "__C0_0" AS "NAME",
    "__C0_1" AS "NETWORK",
    "__C0_2" AS "RATING"
FROM "PUBLIC"."__T0"
    /* PUBLIC.merge_scan */
```

The query result is:

```
+-------------------+------------+--------------------+
|       NAME        |   NETWORK  |       RATING       |
+-------------------+------------+--------------------+
| The Blue Planet   | BBC One    | {"average":9.1}    |
+-------------------+------------+--------------------+

1 row selected (0.007 seconds)
```

Wasn't that fast? From 23.731 sec to 0.007 sec - more than x3300 improvement!

Now clean up (optional):

```sql
DROP TABLE IF EXISTS shows;
```

## Automation

Flattening using `UPDATE` is good for this tutorial. To automate this, you can add `CacheInterceptor` to your `CacheConfiguration`:

{% hint style="warning" %}
The snippet calls `JsonFunctions`, which is in an `internal` package. It is not a supported public API and can change between versions. For production code, parse the JSON with a JSON library in the interceptor instead.
{% endhint %}

```java
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CacheInterceptorAdapter;
import org.apache.ignite.cache.query.annotations.QuerySqlField;
import org.apache.ignite.configuration.CacheConfiguration;
import org.gridgain.internal.processors.query.h2.sql.JsonFunctions;
import javax.cache.Cache;
import java.io.Serializable;

public class JsonBasics {

    public static void main(String[] args) {
        CacheConfiguration cacheCfg = new CacheConfiguration("shows");
        // set up cache mode, backup, etc.
        cacheCfg.setIndexedTypes(Integer.class, ShowJson.class);
        cacheCfg.setInterceptor(new ShowJsonFlattenInterceptor());

        IgniteConfiguration cfg = new IgniteConfiguration();
        cfg.setCacheConfiguration(cacheCfg);

        Ignition.start(cfg);
    }
}

class ShowJsonFlattenInterceptor extends CacheInterceptorAdapter<Integer, ShowJson> {

    @Override
    public ShowJson onBeforePut(Cache.Entry<Integer, ShowJson> entry, ShowJson newVal) {
        // This method is called within IgniteCache.put(k, v)
        String json = newVal.getData();
        String firstEpisodeName = JsonFunctions.jsonValue(json, "$._embedded.episodes[0].name");
        String firstEpisodeAirstamp = JsonFunctions.jsonValue(json, "$._embedded.episodes[0].airstamp");

        ShowJson result = new ShowJson(json);
        result.setFirstEpisodeName(firstEpisodeName);
        result.setFirstEpisodeAirstamp(firstEpisodeAirstamp);
        return result;
    }
}

class ShowJson implements Serializable {

    @QuerySqlField
    private String data;

    @QuerySqlField(name = "first_episode_name")
    private String firstEpisodeName;

    @QuerySqlField(name = "first_episode_airstamp")
    private String firstEpisodeAirstamp;

    public ShowJson(String data) {
        this.data = data;
    }
    // getters and setters
}
```

## Conclusion

You have successfully completed the tutorial. You have learned how to query semi-structured JSON data, as well as how to improve the JSON query performance by rearranging the data and adding well-chosen indexes.

## Related

- [JSON Functions](../../reference/sql/functions/json-functions.md) for the full reference on `JSON_VALUE` and `JSON_QUERY`
- [Enabling modules](../../gridgain8-development/project-setup.md#enabling-modules) for enabling the `gridgain-sql` module
