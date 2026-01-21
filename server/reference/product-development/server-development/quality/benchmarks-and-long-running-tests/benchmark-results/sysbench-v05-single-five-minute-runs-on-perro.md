# sysbench v0.5 - Single Five Minute Runs on perro

MariDB/MySQL sysbench benchmark comparison in %\
Each test was run for 5 minutes.

```
Number of threads
                     1       4       8       16      32      64      128
 sysbench test
  delete            103.72  101.84  106.56  102.80   94.19   86.23   65.13
  insert            102.01   95.04   97.44   89.00   82.42   81.82   85.63
  oltp_complex_ro   104.21  104.98  105.30  102.67  102.69  102.95  101.10
  oltp_complex_rw   105.08  104.34  103.60  102.90  100.76   98.41   89.94
  oltp_simple       100.66  100.44  102.82  104.23  103.08  100.55   95.90
  select            102.93  101.56  103.70  104.18  102.25  100.65   97.33
  update_index      101.74   92.33  101.69   93.09   76.45   73.67   72.88
  update_non_index  101.58   98.13   98.91   92.32   84.00   76.75   74.19

(MariaDB q/s / MySQL q/s * 100)
```

Benchmark was run on perro: Linux openSUSE 11.1 (x86\_64), single socket dual-core Intel 3.2GHz. with 1MB L2 cache, 2GB RAM, data\_dir on 2 disk software RAID 0

MariaDB and MySQL were compiled with

```
BUILD/compile-amd64-max
```

MariaDB revision was:

```
revno: 2821
committer: Sergei Golubchik <sergii@pisem.net>
branch nick: maria-5.1
timestamp: Tue 2010-02-23 13:04:58 +0100
message:
fix for a possible DoS in the my_net_skip_rest()
```

MySQL revision was:

```
revno: 3360 [merge]
author: hery.ramilison@sun.com
committer: MySQL Build Team <build@mysql.com>
branch nick: mysql-5.1
timestamp: Wed 2010-02-17 18:48:40 +0100
message:
Merge from mysql-5.1.44-release
```

sysbench was run with these parameters:

```
--oltp-table-size=2000000 \
--max-time=300 \
--max-requests=0 \
--mysql-table-engine=InnoDB \
--mysql-user=root \
--mysql-engine-trx=yes
```

and this variable part of parameters

```
--num-threads=$THREADS --test=${TEST_DIR}/${SYSBENCH_TEST}
```

Configuration used for MariDB and MySQL:

```
--no-defaults \
--skip-grant-tables \
--language=./sql/share/english \
--datadir=$DATA_DIR \
--tmpdir=$TEMP_DIR \
--socket=$MY_SOCKET \
--table_open_cache=512 \
--thread_cache=512 \
--query_cache_size=0 \
--query_cache_type=0 \
--innodb_data_home_dir=$DATA_DIR \
--innodb_data_file_path=ibdata1:128M:autoextend \
--innodb_log_group_home_dir=$DATA_DIR \
--innodb_buffer_pool_size=1024M \
--innodb_additional_mem_pool_size=32M \
--innodb_log_file_size=256M \
--innodb_log_buffer_size=16M \
--innodb_flush_log_at_trx_commit=1 \
--innodb_lock_wait_timeout=50 \
--innodb_doublewrite=0 \
--innodb_flush_method=O_DIRECT \
--innodb_thread_concurrency=0 \
--innodb_max_dirty_pages_pct=80"
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
