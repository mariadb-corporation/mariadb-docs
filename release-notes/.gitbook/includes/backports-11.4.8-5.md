---
title: backports-11.4.8-5
---

* Segmented key cache for Aria ([MENT-2361](https://jira.mariadb.org/browse/MENT-2361))
  * A new variable [aria-pagecache-segments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_pagecache_segments) (default 1) to define the number of segments has been added. The default disables the new feature.
* Backport fixes for Vectors to MariaDB Enterprise 11.4 ([MENT-2365](https://jira.mariadb.org/browse/MENT-2365))
  * Overflow/inf in vec\_distance\_euclidean
  * Sporadic segmentation faults possibly related to vector search
  * Incorrect error/docs for Vector column lengths (max = 65532
  * Unexpected ER\_TABLE\_EXISTS\_ERROR on primary or replica upon CREATE OR REPLACE for partitioned table
  * Cannot access shared MEM\_ROOT without a lock
  * Can't find record in 't1' on INSERT to Vector table
  * Create vector table failed with VECTOR INDEX when innodb\_force\_primary\_key=on
  * Assertion when adding FK to MyISAM/Aria table with a vector index
  * UBSAN: 32801 is outside the range of representable values of type 'short'
  * Always release ctx in mhnsw\_delete\_all
  * Optimise dot\_product by loop-unrolling by a factor of 4
  * Vector index search allocates too much memory for large ef\_search
  * ALTER performs vector truncation without WARN\_DATA\_TRUNCATED or similar warnings/errors
  * DATA/INDEX DIRECTORY options are ignored for vector index
  * DATA/INDEX DIRECTORY handling is inconsistent
  * Assert with vector index and very long PK
  * InnoDB: Failing assertion: prebuilt->select\_lock\_type != LOCK\_NONE || srv\_read\_only\_mode || trx->read\_view.is\_open()
  * Crash on disconnect when dropped Aria table with vector key under lock
  * InnoDB assert with vector index under LOCK TABLES
  * mhnsw: support powerpc64 SIMD instructions
  * mhnsw: support aarch64 SIMD instructions
  * IGNORED attribute has no effect on vector keys
  * IMPORT TABLESPACE does not work for tables with vector, although allowed
  * Vector-related error messages worth improving when possible
  * Adding a regular index on a vector column leads to invalid table structure
  * Vector values do not survive mariadb-dump / restore
  * Server crashes in Charset::mbminlen / Item\_func\_vec\_fromtext::val\_str upon mixing vector type with string
  * Server crashes in mhnsw\_read\_first upon using vector key with views
  * Server crashes when checking/updating a table having vector key after enabling innodb\_force\_primary\_key
  * ALTER TABLE re-creating vector key is no-op with non-copying alter algorithms (default)
  * Server crash in FVector::distance\_to upon concurrent SELECT
  * Server crashes in Item\_func\_vec\_distance\_common::get\_const\_arg
  * Non-copying ALTER does not pad VECTOR column, vector search further does not work
  * Assertion `bitmap_is_set(&read_partitions, next->id)` failed in int partition\_info::vers\_set\_hist\_part(THD \*)
