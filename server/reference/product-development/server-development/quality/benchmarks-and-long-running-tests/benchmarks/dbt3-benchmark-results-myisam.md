# DBT3 Benchmark Results MyISAM

## Introduction

This page shows the results for benchmarking the following configuration:

* [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/5.3.2) + MyISAM
* [MariaDB 5.5.18](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-5518-release-notes/README.md) + MyISAM
* MySQL 5.5.19 + MyISAM
* MySQL 5.6.4 + MyISAM

The test is performed using the automation script `/mariadb-tools/dbt3_benchmark/launcher.pl`.

Details about this automation script can be found on the [DBT3 automation scripts](dbt3-automation-scripts.md) page.

## Hardware

The tests were performed on our `facebook-maria1` machine. It has the following parameters:

* CPU: 16 Intel® Xeon® CPU L5520 @ 2.27GHz
* Memory: Limited to 16 GB out of 72 by adding 'mem=16G' parameter to /boot/grub/menu.lst
* Logical disk: HDD 2 TB
* Operating system:

## Scale factor 30

This test was performed with the following parameters:

* Scale factor: 30
* Query timeout: 2 hours
* Number of tests per query: 1
* Total DB size on disk: about 50GB
* Available memory: 16 GB

**NOTE:** The available memory is controlled by a parameter `mem=16G` added to the file `/boot/grub/menu.lst`

### Steps to reproduce

Follow the instructions in [DBT3 automation scripts](dbt3-automation-scripts.md) to prepare the environment for the test.

Before you run the test, ensure that the settings in the test configuration\
files match your prepared environment. For more details on the test\
configuration, please, refer to the [Test configuration parameters](dbt3-automation-scripts.md#test-configuration).

After the environment is prepared, the following command should be executed in the shell:

```
perl launcher.pl \
--results-output-dir=/home/mariadb/benchmark/dbt3/results/myisam_test \
--project-home=/home/mariadb/benchmark/dbt3/ \
--datadir=/home/mariadb/benchmark/dbt3/db_data/ \
--test=./tests/myisam_test_mariadb_5_3_mysql_5_5_mysql_5_6.conf \
--queries-home=/home/mariadb/benchmark/dbt3/gen_query/ --scale-factor=30 \
--TIMEOUT=7200
```

### Compared configurations

The following configurations have been compared in this test:

#### Case 1: [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/5.3.2) + MyISAM

Here are the common options that the mysqld server was started with:

```
net_read_timeout = 300
net_write_timeout = 600
key_buffer_size = 3G
skip-external-locking
key_buffer = 16M
max_allowed_packet = 16M
table_open_cache = 1024
thread_cache = 512
sort_buffer_size = 512K
net_buffer_length = 8K
read_buffer_size = 256K
read_rnd_buffer_size = 512K
myisam_sort_buffer_size = 8M
max_connections = 256
query_cache_size = 0
query_cache_type = 0
sql-mode = NO_ENGINE_SUBSTITUTION

#Per-test optimizations
optimizer_switch='index_merge=on'
optimizer_switch='index_merge_union=on'
optimizer_switch='index_merge_sort_union=on'
optimizer_switch='index_merge_intersection=on'
optimizer_switch='index_merge_sort_intersection=off'
optimizer_switch='index_condition_pushdown=on'
optimizer_switch='derived_merge=on'
optimizer_switch='derived_with_keys=on'
optimizer_switch='firstmatch=off'
optimizer_switch='loosescan=off'
optimizer_switch='materialization=on'
optimizer_switch='in_to_exists=on'
optimizer_switch='semijoin=on'
optimizer_switch='partial_match_rowid_merge=on'
optimizer_switch='partial_match_table_scan=on'
optimizer_switch='subquery_cache=off'
optimizer_switch='mrr=on'
optimizer_switch='mrr_cost_based=off'
optimizer_switch='mrr_sort_keys=on'
optimizer_switch='outer_join_with_cache=on'
optimizer_switch='semijoin_with_cache=off'
optimizer_switch='join_cache_incremental=on'
optimizer_switch='join_cache_hashed=on'
optimizer_switch='join_cache_bka=on'
optimizer_switch='optimize_join_buffer_size=on'
optimizer_switch='table_elimination=on'

join_buffer_space_limit = 3072M
join_buffer_size = 1536M
join_cache_level = 6
mrr_buffer_size = 96M
tmp_table_size = 96M
max_heap_table_size = 96M
```

#### Case 2: [MariaDB 5.5.18](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-5518-release-notes/README.md) + MyISAM

Uses the same configuration file as [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/5.3.2) in Case 1.

#### Case 3: MySQL 5.5.19 + MyISAM

Here are the common options that the mysqld server was started with:

```
net_read_timeout = 300
net_write_timeout = 600
key_buffer_size = 3G
skip-external-locking
key_buffer = 16M
max_allowed_packet = 16M
table_open_cache = 1024
thread_cache = 512
sort_buffer_size = 512K
net_buffer_length = 8K
read_buffer_size = 256K
myisam_sort_buffer_size = 8M
max_connections = 256
query_cache_size = 0
query_cache_type = 0
sql-mode = NO_ENGINE_SUBSTITUTION

join_buffer_size = 1536M
tmp_table_size = 96M
max_heap_table_size = 96M
read_rnd_buffer_size = 96M
```

#### Case 4: MySQL 5.6.4 + MyISAM

Here are the common options that the mysqld server was started with:

```
net_read_timeout = 300
net_write_timeout = 600
key_buffer_size = 3G
skip-external-locking
key_buffer = 16M
max_allowed_packet = 16M
table_open_cache = 1024
thread_cache = 512
sort_buffer_size = 512K
net_buffer_length = 8K
read_buffer_size = 256K
myisam_sort_buffer_size = 8M
max_connections = 256
query_cache_size = 0
query_cache_type = 0
sql-mode = NO_ENGINE_SUBSTITUTION

optimizer_switch='mrr=on'
optimizer_switch='mrr_cost_based=off'
optimizer_switch='batched_key_access=on'
optimizer_switch='index_condition_pushdown=on'

join_buffer_size = 1536M
tmp_table_size = 96M
max_heap_table_size = 96M
read_rnd_buffer_size = 96M
```

The server has been restarted between each query run and the caches have been\
cleared between each query run.

### Results (without q20)

Here is the graphics of the results:

(Smaller bars are better)

**NOTE:** Queries that are cut off by the graphics have timed out the period of 2 hours.

Here are the actual results in seconds (smaller is better):

| Configuration             | 1.sql                                                                                                            | 2.sql | 2-opt.sql                                                                                                                          | 3.sql | 4.sql                                                                                              | 5.sql | 6.sql                                                                                         | 7.sql | 8.sql | 9.sql | 10.sql | 11.sql | 12.sql | 13.sql | 14.sql | 15.sql | 16.sql | 17.sql | 17-opt1.sql | 17-opt2.sql | 18.sql | 18-opt.sql | 19.sql | 19-opt1.sql | 19-opt2.sql | 20.sql | 21.sql | 22.sql | Version | Query and explain details |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------- | ----- | ----- | ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ----------- | ----------- | ------ | ---------- | ------ | ----------- | ----------- | ------ | ------ | ------ | ------- | ------------------------- |
| Configuration             | [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/5.3.2) + MyISAM | Ratio | [MariaDB 5.5.18](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-5518-release-notes/README.md) + MyISAM | Ratio | MySQL 5.5.19 + MyISAM                                                                              | Ratio | MySQL 5.6.4 + MyISAM                                                                          | Ratio |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 1.sql                     | 261                                                                                                              | 1.00  | 308                                                                                                                                | 1.18  | 259                                                                                                | 0.99  | 277                                                                                           | 1.06  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 2.sql                     | 47                                                                                                               | 1.00  | 48                                                                                                                                 | 1.02  | 499                                                                                                | 10.62 | 49                                                                                            | 1.04  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 2-opt.sql                 | 46                                                                                                               | 1.00  | 48                                                                                                                                 | 1.04  | -                                                                                                  | -     | -                                                                                             | -     |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 3.sql                     | 243                                                                                                              | 1.00  | 246                                                                                                                                | 1.01  | >7200                                                                                              | -     | 1360                                                                                          | 5.60  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 4.sql                     | 137                                                                                                              | 1.00  | 135                                                                                                                                | 0.99  | 4117                                                                                               | 30.05 | 137                                                                                           | 1.00  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 5.sql                     | 181                                                                                                              | 1.00  | 187                                                                                                                                | 1.03  | 6164                                                                                               | 34.06 | 1254                                                                                          | 6.93  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 6.sql                     | 198                                                                                                              | 1.00  | 205                                                                                                                                | 1.04  | >7200                                                                                              | -     | 194                                                                                           | 0.98  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 7.sql                     | 779                                                                                                              | 1.00  | 896                                                                                                                                | 1.15  | 814                                                                                                | 1.04  | 777                                                                                           | 1.00  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 8.sql                     | 270                                                                                                              | 1.00  | 287                                                                                                                                | 1.06  | 749                                                                                                | 2.77  | 1512                                                                                          | 5.60  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 9.sql                     | 252                                                                                                              | 1.00  | 254                                                                                                                                | 1.01  | >7200                                                                                              | -     | 298                                                                                           | 1.18  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 10.sql                    | 782                                                                                                              | 1.00  | 854                                                                                                                                | 1.09  | >7200                                                                                              | -     | 1881                                                                                          | 2.41  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 11.sql                    | 45                                                                                                               | 1.00  | 36                                                                                                                                 | 0.80  | 357                                                                                                | 7.93  | 49                                                                                            | 1.09  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 12.sql                    | 211                                                                                                              | 1.00  | 217                                                                                                                                | 1.03  | >7200                                                                                              | -     | 213                                                                                           | 1.01  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 13.sql                    | 251                                                                                                              | 1.00  | 236                                                                                                                                | 0.94  | 1590                                                                                               | 6.33  | 244                                                                                           | 0.97  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 14.sql                    | 88                                                                                                               | 1.00  | 91                                                                                                                                 | 1.03  | 1590                                                                                               | 18.07 | 94                                                                                            | 1.07  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 15.sql                    | 162                                                                                                              | 1.00  | 164                                                                                                                                | 1.01  | 4580                                                                                               | 28.27 | 165                                                                                           | 1.02  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 16.sql                    | 154                                                                                                              | 1.00  | 152                                                                                                                                | 0.99  | 174                                                                                                | 1.13  | 173                                                                                           | 1.12  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 17.sql                    | 1493                                                                                                             | 1.00  | 1495                                                                                                                               | 1.00  | 865                                                                                                | 0.58  | 794                                                                                           | 0.53  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 17-opt1.sql               | 795                                                                                                              | 1.00  | 794                                                                                                                                | 1.00  | 862                                                                                                | 1.08  | 794                                                                                           | 1.00  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 17-opt2.sql               | 1482                                                                                                             | 1.00  | 1458                                                                                                                               | 0.98  | 2167                                                                                               | 1.46  | 1937                                                                                          | 1.31  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 18.sql                    | 971                                                                                                              | 1.00  | 931                                                                                                                                | 0.96  | >7200                                                                                              | -     | >7200                                                                                         | -     |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 18-opt.sql                | 121                                                                                                              | 1.00  | 125                                                                                                                                | 1.03  | -                                                                                                  | -     | -                                                                                             | -     |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 19.sql                    | 212                                                                                                              | 1.00  | 212                                                                                                                                | 1.00  | 2004                                                                                               | 9.45  | 61                                                                                            | 0.29  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 19-opt1.sql               | 59                                                                                                               | 1.00  | 59                                                                                                                                 | 1.00  | 1999                                                                                               | 33.88 | 61                                                                                            | 1.03  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 19-opt2.sql               | 260                                                                                                              | 1.00  | 216                                                                                                                                | 0.83  | 443                                                                                                | 1.70  | 236                                                                                           | 0.91  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 20.sql                    | -                                                                                                                | -     | -                                                                                                                                  | -     | -                                                                                                  | -     | -                                                                                             | -     |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 21.sql                    | 173                                                                                                              | 1.00  | 179                                                                                                                                | 1.03  | >7200                                                                                              | -     | 183                                                                                           | 1.06  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| 22.sql                    | 13                                                                                                               | 1.00  | 14                                                                                                                                 | 1.08  | 10                                                                                                 | 0.77  | 13                                                                                            | 1.00  |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| Version                   | 5.3.2-MariaDB-beta                                                                                               |       | 5.5.18-MariaDB                                                                                                                     |       | 5.5.19                                                                                             |       | 5.6.4-m7                                                                                      |       |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |
| Query and explain details | [Explain details](https://askmonty.org/w/images/5/56/DBT3_MyISAM_HDD_s30_mariadb_5_3_2.txt)                      |       | [Explain details](https://askmonty.org/w/images/9/9e/DBT3_MyISAM_HDD_s30_mariadb_5_5_18.txt)                                       |       | [Explain details](https://askmonty.org/w/images/c/cc/Explain_DBT3_MyISAM_HDD_s30_mysql_5_5_19.txt) |       | [Explain details](https://askmonty.org/w/images/d/d1/Explain_MyISAM_HDD_s30_mysql_5_6_4_.txt) |       |       |       |        |        |        |        |        |        |        |        |             |             |        |            |        |             |             |        |        |        |         |                           |

**NOTE:** The columns named "_Ratio_" are calculated values of the ratio between the\
current value compared to the value in the first test configuration. The\
formula for it is `(current_value/value_in_first_row)`. For example if [MariaDB\
5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/5.3.2) (the first column) handles a query for 100 seconds and MySQL 5.6.4 (the last\
configuration) handles the same query for 120 seconds, the ratio will be`120/100 = 1.20`. This means that it takes MySQL 5.6.4 20% more time to handle\
the same query.

The archived folder with all the results and details for that benchmark can be\
downloaded from here:[MyISAM s30 on facebook-maria1](https://askmonty.org/w/images/e/e1/Myisam_test_2011-12-01_203150.tar.bz2)

### Notes

Queries 2-opt.sql and 18-opt.sql are tested only for [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/5.3.2) and [MariaDB\
5.5.18](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-5518-release-notes/README.md)

* Additional startup parameters for 2\_opt:

```
--optimizer_switch='mrr_sort_keys=off'
```

* Additional startup parameters for 18\_opt:

```
--optimizer_switch='semijoin=off' --optimizer_switch='index_condition_pushdown=on'
```

* Additional modifications for 17-opt1:

```
SELECT
SUM(l_extendedprice) / 7.0 AS avg_yearly
FROM
 part STRAIGHT_JOIN lineitem
WHERE
p_partkey = l_partkey
...
```

* Additional modifications for 17-opt2:

```
SELECT
 	SUM(l_extendedprice) / 7.0 AS avg_yearly
FROM
 	lineitem STRAIGHT_JOIN part
WHERE
 	p_partkey = l_partkey
...
```

* Additional modifications for 19-opt1:

```
SELECT
 	SUM(l_extendedprice* (1 - l_discount)) AS revenue
FROM
 	part STRAIGHT_JOIN lineitem
WHERE
 	(
 		p_partkey = l_partkey
...
```

* Additional modifications for 19-opt2:

```
SELECT
 	SUM(l_extendedprice* (1 - l_discount)) AS revenue
FROM
 	lineitem STRAIGHT_JOIN part
WHERE
 	(
 		p_partkey = l_partkey
...
```

### Benchmark for q20

This benchmarked only q20 with the same settings as described above for the\
other queries. The only difference is the timeout that was used: 30000 seconds\
(8 hours and 20 min).

#### Compared cases

The benchmark for q20 compares the following cases:

* q20.sql - the original query is run with the IN-TO-EXISTS strategy for all servers.\
  The following optimizer switches were used for MariaDB:

```
--optimizer_switch='in_to_exists=on,materialization=off,semijoin=off';
```

* q20-opt0.sql - the original query is changed so that the same join order is chosen as\
  for the two subsequent variants that test materialization where this order is optimal.\
  The join order is:

```
SELECT s_name, s_address
 FROM supplier, nation
 WHERE s_suppkey IN (SELECT DISTINCT (ps_suppkey)
 FROM '''part straight_join partsupp'''
 WHERE ps_partkey = p_partkey ...
```

* Since the IN-TO-EXISTS strategy is essentially the same for both MariaDB\
  and MySQL, this query was tested for MySQL only.
* q20-opt1.sql - modifies the original query in two ways:
  * enforces the MATERIALIZATION strategy, and
  * enforces an optimal JOIN order via straight\_join as follows:

```
SELECT s_name, s_address
 FROM supplier, nation
 WHERE s_suppkey IN (SELECT DISTINCT (ps_suppkey)
 FROM '''part straight_join partsupp'''
 WHERE ps_partkey = p_partkey ...
```

q20-opt1.sql uses the following optimizer switches for\
MariaDB:

```
--optimizer_switch='in_to_exists=off,materialization=on,semijoin=off';
```

* q20-opt2.sql - the same as q20-opt1.sql but allows the optimizer to choose\
  the subquery strategy via the following switch:

```
--optimizer_switch='in_to_exists=on,materialization=on,semijoin=on';
```

* This switch results in the choice of SJ-MATERIALIZATION.

**NOTE:** For MySQL there are no such _optimizer-switch_ parameters, and\
the tests were started without any additional startup parameters. The default\
algorithm in MySQL is _in\_to\_exists_.

#### Results for q20

Here is the graphics of the results of the benchmarked q20:\
(Smaller bars are better)

**NOTE:** Queries that are cut off by the graphics have timed out the period of\
30000 seconds.

Here are the actual results in seconds (smaller is better):

| Configuration                                                                                                                      | 20.sql | 20-opt0.sql | 20-opt1.sql | 20-opt2.sql | Version            | Query and explain details                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------ | ----------- | ----------- | ----------- | ------------------ | ------------------------------------------------------------------------------------------------ |
| [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/5.3.2) + MyISAM                   | 20070  | -           | 5560        | 5615        | 5.3.2-MariaDB-beta | [Explain details](https://askmonty.org/w/images/9/9a/DBT3_MyISAM_HDD_s30_q20_mariadb_5_3_2.txt)  |
| [MariaDB 5.5.18](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-5518-release-notes/README.md) + MyISAM | 19922  | -           | 5529        | 5572        | 5.5.18-MariaDB     | [Explain details](https://askmonty.org/w/images/e/e8/DBT3_MyISAM_HDD_s30_q20_mariadb_5_5_18.txt) |
| MySQL 5.5.19 + MyISAM                                                                                                              | 17832  | >30000      | -           | -           | 5.5.19             | [Explain details](https://askmonty.org/w/images/a/ae/DBT3_MyISAM_HDD_s30_q20_mysql_5_5_19.txt)   |
| MYSQL 5.6.4 + MyISAM                                                                                                               | 19845  | >30000      | -           | -           | 5.6.4-m7           | [Explain details](https://askmonty.org/w/images/c/cc/DBT3_MyISAM_HDD_s30_q20_mysql_5_6_4.txt)    |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
