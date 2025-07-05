# Block-Based Join Algorithms

In the versions of MariaDB/MySQL before 5.3 only one block-based join algorithm was implemented: the Block Nested Loops (BNL) join algorithm which could only be used for inner joins.

[MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) enhanced the implementation of BNL joins and provides a variety of block-based join algorithms that can be used for inner joins, outer joins, and semi-joins. Block-based join algorithms in MariaDB employ a join buffer to accumulate records of the first join operand before they start looking for matches in the second join operand.

This page documents the various block-based join algorithms.

* Block Nested Loop (BNL) join
* Block Nested Loop Hash (BNLH) join
* Block Index join known as Batch Key Access (BKA) join
* Block Index Hash join known as Batch Key Access Hash (BKAH) join

## Block Nested Loop Join

The major difference between the implementation of BNL join in [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)\
compared to earlier versions of MariaDB/MySQL is that the former uses a new\
format for records written into join buffers. This new format allows:

* More efficient use of buffer space for null field values and field values of\
  flexible length types (like the varchar type)
* Support for so-called incremental join buffers saving buffer space for\
  multi-way joins
* Use of the algorithm for outer joins and semi-joins

### How Block Nested Loop Join Works

The algorithm performs a join operation of tables t1 and t2 according to the following schema.\
The records of the first operand are written into the join buffer one by one until the buffer is full.\
The records of the second operand are read from the base/temporary table one by one. For every read record r2 of table t2 the join buffer is scanned, and, for any record r1 from the buffer such that r2 matches r1 the concatenation of the interesting fields of r1 and r2 is sent to the result stream of the corresponding partial join.\
To read the records of t2 a full table scan, a full index scan or a range index scan is performed. Only the records that meet the condition pushed to table t2 are checked for a match of the records from the join buffer.\
When the scan of the table t2 is finished a new portion of the records of the first operand fills the buffer and matches for these records are looked for in t2.\
The buffer refills and scans of the second operand that look for matches in the join buffer are performed again and again until the records of first operand are exhausted.\
In total the algorithm scans the second operand as many times as many refills of the join buffer occur.

### More Efficient Usage of Join Buffer Space

No join buffer space is used for null field values.\
Any field value of a flexible length type is not padded by 0 up to the maximal field size anymore.

### Incremental Join Buffers

If we have a query with a join of three tables t1, t2, t3 such that table t1 is joined with table t2 and the result of this join operation is joined with table t3 then two join buffers can be used to execute the query. The first join buffer B1 is used to store the records comprising interesting fields of table t1, while the second join buffer B2 contains the records with fields from the partial join of t1 and t2. The interesting fields of any record r1 from B1 are copied into B2 for any record r1,r2 from the partial join of t1 and t2.\
One could suggest storing in B2 just a pointer to the position of the r1 fields in B1 together with the interesting fields from t2. So for any record r2 matching the record r1 the buffer B2 would contain a reference to the fields of r1 in B1 and the fields of r2. In this case the buffer B2 is called incremental.\
Incremental buffers allow to avoid copying field values from one buffer into another. They also allow to save a significant amount of buffer space if for a record from t1 several matches from t2 are expected.

### Using Join Buffers for Simple Outer Joins and Semi-joins

If a join buffer is used for a simple left outer join of tables t1 and t1\
t1 LEFT JOIN t2 ON P(t1,t2)\
then each record r1 stored in the buffer is provided with a match flag. Initially this flag is set off. As soon as the first match for r1 is found this flag is set on. When all matching candidates from t2 have been check, the record the join buffer are scanned and for those of them that still have there match flags off null-complemented rows are generated.\
The same match flag is used for any record in the join buffer is a semi-join operation\
t1 SEMI JOIN t2 ON P(t1,t2)\
is performed with a block based join algorithm. When this match flag is set to on for a record r1 in the buffer no matches from table t2 for record r1 are looked for anymore.

## Block Hash Join

Block based hash join algorithm is a new option to be used for join operations in [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3). It can be employed in the cases when there are equi-join sub-condition for the joined tables, in the other words when equalities of the form t2.f1= e1(t1),...,t2.fn=en(t1) can be extracted from the full join condition. As any block based join algorithm this one used a join buffer filled with the records of\
the first operand and looks through the records of the second operand to find matches for the records in the buffer.

### How Block Hash Join Works

For each refill of the join buffer and each record r1 from it the algorithm builds a hash table with the keys constructed over the values e1(r1),...en(r1). Then the records of t2 are looked through. For each record r2 from t2 that the condition pushed to the table t2 a hash key over the fields r2.f1,..., r2.fn is calculated to probe into the hash table. The probing returns those records from the buffer to which r2 matches.\
As for BNL join algorithm this algorithm scans the second operand as many time as many refills of the buffer occur. Yet it has to look only through the records of one bucket in the hash table when looking for the records to which a record from t2 matches, not through all records in the join buffer as BNL join algorithm does.\
The implementation of this algorithm in MariaDB builds the hash table with hash keys at the very end of the join buffer. That's why the number of records written into the buffer at one refill is less then for BNL join algorithms. However a much shorter list of possible matching candidates makes this the block hash join algorithm usually much faster then BNL join.

## Batch Key Access Join

Batch Keys Access join algorithm performs index look-ups when looking for possible matching candidates provided by the second join operand. With this respect the algorithm behave itself as the regular join algorithm. Yet BKA performs index look-ups for a batch of the records from the join buffer. For conventional database engines like InnoDB/MyISAM it allows to fetch matching candidates in an optimal way. For the engines with remote data store such as FederateX/Spider the algorithm allows to save on transfers between the MySQL node and the data store nodes.

### How Batch Keys Access Join Works

The implementation of the algorithm in 5.3 heavily exploits the multi-range-read interface and its properties. The interface hides the actual mechanism of fetching possible candidates for matching records from the table to be joined.\
As any block based join algorithm the BKA join repeatedly fills the join buffer with records of the first operand and for each refill it finds records from the join table that could match the records in the buffer.\
To find such records it asks the MRR interface to perform index look-ups with the keys constructed over all records from the buffer. Together with each key the interface receives a return address - a reference to the record over which this key has been constructed. The actual implementation functions of the MRR interface organize and optimize somehow the process of fetching the records of the joined table by the received keys. Each fetched record r2 is appended with the return address associated with the key by which the record has been found and the result is passed to the BKA join procedure. The procedure takes the record r1 from the join buffer by the return address, joins it with r2 and checks the join condition. If the condition is evaluated to true the joined records is sent to the result stream of the join operation. So for each record returned by the MRR interface only one record from the join buffer is accessed.\
The number of records from table t2 fetched by the BKA join is exactly the same as for the regular nested loops join algorithm. Yet BKA join allows to optimize the order in which the records are fetched.

### Interaction of BKA Join With the MRR Functions

BKA join interacts with the MRR functions respecting the following contract.\
The join procedure calls the MRR function multi\_range\_read\_init passing it the callback functions that\
allows to initialize reading keys for the records in the join buffer and to iterate over these keys. It also passes the parameters of the buffer for MRR needs allocated within the join buffer space.\
Then BKA join repeatedly calls the MRR function multi\_range\_read\_next. The function works as an iterator function over the records fetched by index look-ups with the keys produced by a callback function set in the call of multi\_range\_read\_init. A call of the function multi\_range\_read\_next returns the next fetched record through the dedicated record buffer, and the associated reference to the matched record from the join buffer as the output parameter of the function.

## Managing Usage of Block-Based Join Algorithms

Currently 4 different types of block-based join algorithms are supported. For a particular join operation each of them can be employed with a regular (flat) join buffer or with an incremental join buffer.

Three optimizer switches - `join_cache_incremental`, `join_cache_hashed`, `join_cache_bka` – and the system variable [join\_cache\_level](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level) control which of the 8 variants of the block-based algorithms will be used for join operations.

If `join_cache_bka` is off then BKA and BKAH join algorithms are not allowed.\
If `join_cache_hashed` is off then BNLH and BKAH join algorithms are not allowed.\
If `join_cache_incremental` is off then no incremental variants of the block-based join algorithms are allowed.

By default the switches `join_cache_incremental`, `join_cache_hashed`, `join_cache_bka` are set to 'on'.\
However it does not mean that by default any of block-based join algorithms is allowed to be used. All of them are allowed only if the system variable [join\_cache\_level](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level) is set to 8. This variable can take an integer value in the interval from 0 to 8.

If the value is set to 0 no block-based algorithm can be used for a join operation.\
The values from 1 to 8 correspond to the following variants of block-based join algorithms :

* 1 – Flat BNL
* 2 – Incremental BNL
* 3 – Flat BNLH
* 4 – Incremental BNLH
* 5 – Flat BKA
* 6 – Incremental BKA
* 7 – Flat BKAH
* 8 – Incremental BKAH

If the value of [join\_cache\_level](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level) is set to N, any of block-based algorithms with the level greater than N is disallowed.

So if [join\_cache\_level](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level) is set to 5, no usage of BKAH is allowed and usage of incremental BKA is not allowed either while usage of all remaining variants are controlled by the settings of the optimizer switches `join_cache_incremental`, `join_cache_hashed`, `join_cache_bka`.

By default [join\_cache\_level](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_cache_level) is set to 2. In other words only usage of flat or incremental BNL is allowed.

By default block-based algorithms can be used only for regular (inner) join operations. To allow them for outer join operations (left outer joins and right outer joins) the optimizer switch `outer_join_with_cache` has to be set to 'on'.\
Setting the optimizer switch `semijoin_with_cache` to 'on' allows using these algorithms for semi-join operations.

Currently, only incremental variants of the block-based join algorithms can be used for nested outer joins and nested semi-joins.

### Size of Join Buffers

The maximum size of join buffers used by block-based algorithms is controlled by setting the [join\_buffer\_size](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size) system variable.\
This value must be large enough in order for the join buffer employed for a join operation to contain all relevant fields for at least one joined record.

[MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) introduced the system variable [join\_buffer\_space\_limit](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_space_limit) that limits the total memory used for join buffers in a query.

To optimize the usage of the join buffers within the limit set by `join_buffer_space_limit`, one should use the [optimizer switch](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_switch) `optimize_join_buffer_size=on`.\
When this flag is set to 'off' (default until [MariaDB 10.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1042-release-notes)), the size of the used join buffer is taken directly from the [join\_buffer\_size](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size) system variable.\
When this flag is set to 'on' (default from [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes)) then the size of the buffer depends on the estimated number of rows in the partial join whose records are to be stored in the buffer.

### Related MRR Settings

To use BKA/BKAH join algorithms for InnoDB/MyISAM, one must set the optimizer switch `mrr` to 'on'. When using these algorithms for InnoDB/MyISAM the overall performance of the join operations can be dramatically improved if the optimizer switch `mrr_sort_keys` is set 'on'.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
