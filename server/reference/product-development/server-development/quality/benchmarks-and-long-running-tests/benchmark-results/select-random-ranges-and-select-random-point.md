# Select Random Ranges and Select Random Point

* `select_random_ranges` (select 10 ranges with a delta as parameter)
* `select_random_points` (select 100 random points)

## Findings

`select_random_ranges`

* A delta of 100 for the ranges gives 3 - 6% performance gain
* A delta of 50 for the ranges gives 3 - 15% performance gain
* A delta of 5 for the ranges gives up to 70% performance gain
* A delta of 1 million shows no difference at all.

`select_random_points`

* We see up to 150% performance gain fetching index only
* We see up to 50% performance gain fetching index and data

The absolute numbers are highly RAM depended

* We see an up to 250% performance difference on a 2GB system compared to a 4GB system.

MariaDB and MySQL were compiled with

```
BUILD/compile-amd64-max
```

MariaDB revision was:

```
revno: 2742
committer: Igor Babaev <igor@askmonty.org>
branch nick: maria-5.2-keycache
timestamp: Tue 2010-02-16 08:41:11 -0800
message:
  WL#86: Partitioned key cache for MyISAM.
  This is the base patch for the task.
```

sysbench was run with the following parameters:

```
--oltp-table-size=20000000 \       # 20 million rows.
--max-requests=0 \
--mysql-table-engine=MyISAM \
--mysql-user=root \
--mysql-engine-trx=no \
--myisam-max-rows=50000000 \
--rand-seed=303
```

and the following variable parameters

```
--num-threads=$THREADS --test=${TEST_DIR}/${SYSBENCH_TEST}
```

Configuration used for MariDB:

```
--no-defaults \
--datadir=/mnt/data/sysbench/data \
--language=./sql/share/english \
--key_buffer_size=512M \
--key_cache_partitions=32 \        # Off | 32 | 64
--max_connections=256 \
--query_cache_size=0 \
--query_cache_type=0 \
--skip-grant-tables \
--socket=/tmp/mysql.sock \
--table_open_cache=512 \
--thread_cache=512 \
--tmpdir=/mnt/data/sysbench
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
