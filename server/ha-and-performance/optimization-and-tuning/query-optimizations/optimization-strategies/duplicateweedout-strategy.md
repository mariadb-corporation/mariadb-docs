# Duplicate Weedout Strategy

`DuplicateWeedout` is an execution strategy for [Semi-join subqueries](../subquery-optimizations/semi-join-subquery-optimizations.md).

## The idea

The idea is to run the semi-join (a query with uses `WHERE X IN (SELECT Y FROM ...)`) as if it were a regular inner join, and then eliminate the duplicate record combinations using a temporary table.

Suppose, you have a query where you're looking for countries which have more than 33% percent of their population in one big city:

```sql
SELECT * 
FROM Country 
WHERE 
   Country.code IN (SELECT City.Country
                    FROM City 
                    WHERE 
                      City.Population > 0.33 * Country.Population AND 
                      City.Population > 1*1000*1000);
```

First, we run a regular inner join between the `City` and `Country` tables:

```mermaid
flowchart LR
    accTitle: Inner join between the city and country tables
    accDescr { The city table contains rows Berlin, Paris, Munich, and Koln; the country table contains rows Germany and France. Berlin, Munich, and Koln each join to Germany, and Paris joins to France, producing one output row per match: Germany (Berlin), France (Paris), Germany (Munich), and Germany (Koln), so Germany appears three times because it has three big cities. }

    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef proc fill:#fbe5d6,stroke:#c15911,stroke-width:2px,color:#111;
    classDef file fill:#eaf2fb,stroke:#2f5b8f,stroke-width:2px,color:#111;

    subgraph city["city"]
        Berlin
        Paris
        Munich
        Koln
    end

    subgraph country["country"]
        Germany
        France
    end

    Berlin --> Germany
    Munich --> Germany
    Koln --> Germany
    Paris --> France

    Germany --> O1["Germany (Berlin)"]
    Germany --> O3["Germany (Munich)"]
    Germany --> O4["Germany (Koln)"]
    France --> O2["France (Paris)"]

    class Berlin,Paris,Munich,Koln,Germany,France node
    class O1,O2,O3,O4 file
```

_The inner join between `city` and `country` produces a duplicate `Germany` row for each of its three big cities._

Now, lets put `DuplicateWeedout` into the picture:

```mermaid
flowchart LR
    accTitle: DuplicateWeedout using a temporary table to remove duplicate join rows
    accDescr { Start temporary creates a temporary table tmp1 with country.rowid as its primary key. The city table (Berlin, Paris, Munich, Koln) joins the country table (Germany, France) the same way as the plain inner join, producing candidate rows Germany (Berlin), France (Paris), Germany (Munich), and Germany (Koln). Each candidate tries to INSERT INTO tmp1 VALUES (country.rowid). The Germany (Berlin) and France (Paris) inserts succeed with OK, but the Germany (Munich) and Germany (Koln) inserts fail because country.rowid for Germany is already in tmp1, so those duplicate rows are weeded out before End temporary. }

    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef proc fill:#fbe5d6,stroke:#c15911,stroke-width:2px,color:#111;
    classDef file fill:#eaf2fb,stroke:#2f5b8f,stroke-width:2px,color:#111;

    StartTemp["Start temporary:<br/>CREATE TEMPORARY TABLE tmp1<br/>(country.rowid PRIMARY KEY)"]

    subgraph city2["city"]
        Berlin2["Berlin"]
        Paris2["Paris"]
        Munich2["Munich"]
        Koln2["Koln"]
    end

    subgraph country2["country"]
        Germany2["Germany"]
        France2["France"]
    end

    Berlin2 --> Germany2
    Munich2 --> Germany2
    Koln2 --> Germany2
    Paris2 --> France2

    Germany2 --> P1["Germany (Berlin)"]
    Germany2 --> P3["Germany (Munich)"]
    Germany2 --> P4["Germany (Koln)"]
    France2 --> P2["France (Paris)"]

    P1 --> I1["try: INSERT INTO tmp1<br/>VALUES (country.rowid)"]
    P2 --> I2["try: INSERT INTO tmp1<br/>VALUES (country.rowid)"]
    P3 --> I3["try: INSERT INTO tmp1<br/>VALUES (country.rowid)"]
    P4 --> I4["try: INSERT INTO tmp1<br/>VALUES (country.rowid)"]

    I1 --> R1["OK"]
    I2 --> R2["OK"]
    I3 --> R3["Fail"]
    I4 --> R4["Fail"]

    StartTemp --> EndTemp["End temporary"]
    R1 --> EndTemp
    R2 --> EndTemp
    R3 -.-> EndTemp
    R4 -.-> EndTemp

    class Berlin2,Paris2,Munich2,Koln2,Germany2,France2 node
    class StartTemp,EndTemp,I1,I2,I3,I4 proc
    class P1,P2,P3,P4,R1,R2,R3,R4 file
```

_`DuplicateWeedout` inserts each candidate row's `country.rowid` into a temporary table with a primary key; the insert fails for rows that would duplicate `Germany`, so only one `Germany` row survives._

## DuplicateWeedout in action

The `Start temporary` and `End temporary` from the last diagram are shown in the `EXPLAIN` output:

```sql
EXPLAIN SELECT * FROM Country WHERE Country.code IN 
  (select City.Country from City where City.Population > 0.33 * Country.Population 
   AND City.Population > 1*1000*1000)\G
*************************** 1. row ***************************
           id: 1
  select_type: PRIMARY
        TABLE: City
         type: RANGE
possible_keys: Population,Country
          KEY: Population
      key_len: 4
          ref: NULL
         ROWS: 238
        Extra: USING INDEX CONDITION; Start temporary
*************************** 2. row ***************************
           id: 1
  select_type: PRIMARY
        TABLE: Country
         type: eq_ref
possible_keys: PRIMARY
          KEY: PRIMARY
      key_len: 3
          ref: world.City.Country
         ROWS: 1
        Extra: USING WHERE; End temporary
2 rows in set (0.00 sec)
```

This query will read 238 rows from the `City` table, and for each of them will make a primary key lookup in the `Country` table, which gives another 238 rows. This gives a total of 476 rows, and you need to add 238 lookups in the temporary table (which are typically _much_ cheaper since the temporary table is in-memory).

If we run the same query with semi-join optimizations disabled, we'll get:

```sql
EXPLAIN SELECT * FROM Country WHERE Country.code IN 
  (select City.Country from City where City.Population > 0.33 * Country.Population 
    AND City.Population > 1*1000*1000)\G
*************************** 1. row ***************************
           id: 1
  select_type: PRIMARY
        TABLE: Country
         type: ALL
possible_keys: NULL
          KEY: NULL
      key_len: NULL
          ref: NULL
         ROWS: 239
        Extra: USING WHERE
*************************** 2. row ***************************
           id: 2
  select_type: DEPENDENT SUBQUERY
        TABLE: City
         type: index_subquery
possible_keys: Population,Country
          KEY: Country
      key_len: 3
          ref: func
         ROWS: 18
        Extra: USING WHERE
2 rows in set (0.00 sec)
```

This plan will read `(239 + 239*18) = 4541` rows, which is much slower.

## Factsheet

* `DuplicateWeedout` is shown as "Start temporary/End temporary" in `EXPLAIN`.
* The strategy can handle correlated subqueries.
* But it cannot be applied if the subquery has meaningful `GROUP BY` and/or aggregate functions.
* `DuplicateWeedout` allows the optimizer to freely mix a subquery's tables and the parent select's tables.
* There is no separate @@optimizer\_switch flag for `DuplicateWeedout`. The strategy can be disabled by switching off all semi-join optimizations with `SET @@optimizer_switch='optimizer_semijoin=off'` command.

## See Also

* [Subquery Optimizations Map](../subquery-optimizations/subquery-optimizations-map.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
