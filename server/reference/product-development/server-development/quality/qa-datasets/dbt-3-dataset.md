---
description: >-
  Information on the standardized datasets and database dumps used for DBT-3
  Dataset tests.
---

# DBT-3 Dataset

This page describes our setup for DBT-3 tests. A very cogent resource on the [DBT3 Benchmark](../benchmarks-and-long-running-tests/benchmarks/dbt3-automation-scripts.md) is also available. See also [dbt-3-queries](dbt-3-queries.md)

## Get and compile DBT3

* Get [DBT3](https://osdldbt.sourceforge.net/)
* Make sure that you have pg\_ctl and createdb of PostgreSQL installed. On\
  Ubuntu look for postgresql and postgresql-client and make sure that pg\_ctl is\
  in your PATH, for instance:

```
PATH=/usr/lib/postgresql/8.4/bin:$PATH
```

* Compile DBT3

```
gunzip -c dbt3-1.9.tar.gz | tar xvf -
cd dbt3-1.9
./configure
make
cd src/dbgen
make
```

* Generate data:

```
./dbgen -s30
```

## DDL

Substitute `${ENGINE}` with the storage engine you want to use:

```
CREATE TABLE supplier (
  s_suppkey  INTEGER PRIMARY KEY,
  s_name CHAR(25),
  s_address VARCHAR(40),
  s_nationkey INTEGER,
  s_phone CHAR(15),
  s_acctbal REAL,
  s_comment VARCHAR(101)) Engine ${ENGINE};

CREATE TABLE part (
  p_partkey INTEGER PRIMARY KEY,
  p_name VARCHAR(55),
  p_mfgr CHAR(25),
  p_brand CHAR(10),
  p_type VARCHAR(25),
  p_size INTEGER,
  p_container CHAR(10),
  p_retailprice REAL,
  p_comment VARCHAR(23)) Engine ${ENGINE};

CREATE TABLE partsupp (
  ps_partkey INTEGER,
  ps_suppkey INTEGER,
  ps_availqty INTEGER,
  ps_supplycost REAL,
  ps_comment VARCHAR(199),
  PRIMARY KEY (ps_partkey, ps_suppkey)) Engine ${ENGINE};

CREATE TABLE customer (
  c_custkey INTEGER PRIMARY KEY,
  c_name VARCHAR(25),
  c_address VARCHAR(40),
  c_nationkey INTEGER,
  c_phone CHAR(15),
  c_acctbal REAL,
  c_mktsegment CHAR(10),
  c_comment VARCHAR(117))  Engine ${ENGINE};

CREATE TABLE orders (
  o_orderkey INTEGER PRIMARY KEY,
  o_custkey INTEGER,
  o_orderstatus CHAR(1),
  o_totalprice REAL,
  o_orderDATE DATE,
  o_orderpriority CHAR(15),
  o_clerk CHAR(15),
  o_shippriority INTEGER,
  o_comment VARCHAR(79))  Engine ${ENGINE};

CREATE TABLE lineitem (
  l_orderkey INTEGER,
  l_partkey INTEGER,
  l_suppkey INTEGER,
  l_linenumber INTEGER,
  l_quantity REAL,
  l_extendedprice REAL,
  l_discount REAL,
  l_tax REAL,
  l_returnflag CHAR(1),
  l_linestatus CHAR(1),
  l_shipDATE DATE,
  l_commitDATE DATE,
  l_receiptDATE DATE,
  l_shipinstruct CHAR(25),
  l_shipmode CHAR(10),
  l_comment VARCHAR(44),
  PRIMARY KEY (l_orderkey, l_linenumber)) Engine ${ENGINE};

CREATE TABLE nation (
  n_nationkey INTEGER PRIMARY KEY,
  n_name CHAR(25),
  n_regionkey INTEGER,
  n_comment VARCHAR(152)) Engine ${ENGINE};

CREATE TABLE region (
  r_regionkey INTEGER PRIMARY KEY,
  r_name CHAR(25),
  r_comment VARCHAR(152)) Engine ${ENGINE};

CREATE TABLE time_statistics (
  task_name VARCHAR(40),
  s_time TIMESTAMP,
  e_time TIMESTAMP,
  int_time INTEGER)  Engine ${ENGINE};
```

## Load data

Substitute `${DATA_DIR}` with the path to your generated data.

```
LOAD DATA LOCAL INFILE '${DATA_DIR}/supplier.tbl' into table supplier fields terminated by '|';
  LOAD DATA LOCAL INFILE '${DATA_DIR}/part.tbl' into table part fields terminated by '|';
  LOAD DATA LOCAL INFILE '${DATA_DIR}/partsupp.tbl' into table partsupp fields terminated by '|';
  LOAD DATA LOCAL INFILE '${DATA_DIR}/customer.tbl' into table customer fields terminated by '|';
  LOAD DATA LOCAL INFILE '${DATA_DIR}/orders.tbl' into table orders fields terminated by '|';
  LOAD DATA LOCAL INFILE '${DATA_DIR}/lineitem.tbl' into table lineitem fields terminated by '|';
  LOAD DATA LOCAL INFILE '${DATA_DIR}/nation.tbl' into table nation fields terminated by '|';
  LOAD DATA LOCAL INFILE '${DATA_DIR}/region.tbl' into table region fields terminated by '|';
```

## Indexes we need

```
ALTER TABLE lineitem 
  ADD INDEX i_l_shipdate(l_shipdate),
  ADD INDEX i_l_suppkey_partkey (l_partkey, l_suppkey),
  ADD INDEX i_l_partkey (l_partkey),
  ADD INDEX i_l_suppkey (l_suppkey),
  ADD INDEX i_l_receiptdate (l_receiptdate),
  ADD INDEX i_l_orderkey (l_orderkey),
  ADD INDEX i_l_orderkey_quantity (l_orderkey, l_quantity),
  ADD INDEX i_l_commitdate (l_commitdate);

CREATE INDEX i_c_nationkey ON customer (c_nationkey);

ALTER TABLE orders
  ADD INDEX i_o_orderdate (o_orderdate),
  ADD INDEX i_o_custkey (o_custkey);

CREATE INDEX i_s_nationkey ON supplier (s_nationkey);

ALTER TABLE partsupp 
  ADD INDEX i_ps_partkey (ps_partkey),
  ADD INDEX i_ps_suppkey (ps_suppkey);

CREATE INDEX i_n_regionkey ON nation (n_regionkey);
```

## Analyze tables

```
ANALYZE TABLE supplier;
ANALYZE TABLE part;
ANALYZE TABLE partsupp;
ANALYZE TABLE customer;
ANALYZE TABLE orders;
ANALYZE TABLE lineitem;
ANALYZE TABLE nation;
ANALYZE TABLE region;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
